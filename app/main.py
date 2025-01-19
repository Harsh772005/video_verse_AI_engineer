# import os
# import gradio as gr
# from audio_processing import trim_audio, detect_beats
# from prompt_generator import prepare_final_prompt
# from video_generation import generate_video
# from video_audio import synchronize_audio_video
# from video_effects import apply_colorization, apply_rotation
# from utils import cleanup_temp_files

# # Temporary directories
# TEMP_DIR = {
#     "audio": "./temp/audio",
#     "videos": "./temp/videos"
# }
# os.makedirs(TEMP_DIR["audio"], exist_ok=True)
# os.makedirs(TEMP_DIR["videos"], exist_ok=True)

# def process_audio_and_generate(prompt, audio_file, theme, effects):
#     """
#     Main function to process audio, generate video, and apply effects.
#     """
#     try:
#         # Step 1: Trim and process audio
#         trimmed_audio_path, _ = trim_audio(audio_file, temp_dir=TEMP_DIR["audio"])
#         tempo, beat_times = detect_beats(trimmed_audio_path)

#         # Step 2: Generate video based on user prompt and theme
#         audio_data = {"tempo": tempo, "beat_times": beat_times}
#         final_prompt = prepare_final_prompt(prompt, theme, effects, audio_data)
#         generated_video_path = generate_video(final_prompt, TEMP_DIR["videos"])

#         # Step 3: Synchronize audio with the generated video
#         synced_video_path = synchronize_audio_video(trimmed_audio_path, generated_video_path)

#         # Step 4: Apply optional effects
#         if "Color Patterns" in effects:
#             synced_video_path = apply_colorization(synced_video_path)
#         if "Rotation" in effects:
#             synced_video_path = apply_rotation(synced_video_path)

#         return "Video generation complete!", synced_video_path
#     except Exception as e:
#         return f"Error: {str(e)}", None

# # Gradio Interface
# with gr.Blocks(title="AI Video Generator") as ui:
#     gr.Markdown("# AI Video Generator")

#     # Input fields
#     prompt = gr.Textbox(label="Enter Prompt")
#     audio = gr.Audio(label="Upload Audio File", type="filepath")
#     theme = gr.Radio(choices=["Realistic", "Animation"], label="Choose Visual Theme")
#     effects = gr.CheckboxGroup(choices=["Color Patterns", "Rotation"], label="Effects")

#     # Outputs
#     status = gr.Textbox(label="Status")
#     video_preview = gr.Video(label="Preview")

#     # Button to process
#     generate_button = gr.Button("Generate Video")
#     generate_button.click(
#         process_audio_and_generate,
#         inputs=[prompt, audio, theme, effects],
#         outputs=[status, video_preview]
#     )

# # Launch app
# if __name__ == "__main__":
#     ui.launch()












































import os
import gradio as gr
from audio_processing import trim_audio, detect_beats
from prompt_generator import prepare_final_prompt
from video_generation import generate_video_with_kling_api
from video_audio import synchronize_audio_video
from config import Config
import librosa


# Temporary directory setup
os.makedirs(Config.TEMP_DIR_AUDIO, exist_ok=True)
os.makedirs(Config.TEMP_DIR_VIDEO, exist_ok=True)

def generate_video_workflow(prompt, audio, theme, effects):
    try:
        # Process audio
        trimmed_audio_path, sr = trim_audio(audio, temp_dir=Config.TEMP_DIR_AUDIO)
        tempo, beat_times = detect_beats(trimmed_audio_path)
        audio_data = {"tempo": tempo, "beat_times": beat_times}

        # Prepare final prompt
        final_prompt = prepare_final_prompt(prompt, theme, effects, audio_data)

        # Generate video
        video_path = generate_video_with_kling_api(final_prompt)

        # Synchronize audio with video
        final_video_path = synchronize_audio_video(trimmed_audio_path, video_path)

        return f"Final Video Path: {final_video_path}", final_video_path
    except Exception as e:
        return f"Error: {str(e)}", None

# Gradio UI
with gr.Blocks(title="AI Video Generator") as ui:
    gr.Markdown("# AI Video Generator")
    prompt = gr.Textbox(label="Enter Prompt", placeholder="Describe your video")
    audio = gr.Audio(label="Upload Audio", type="filepath")
    theme = gr.Radio(
        choices=["Realistic", "Animation", "Funny", "Abstract"], 
        label="Choose Visual Theme"
    )
    effects = gr.CheckboxGroup(
        choices=["Beat Sync", "Color Patterns", "Animation"], 
        label="Select Effects"
    )
    generate_btn = gr.Button("Generate Video")
    output_text = gr.Textbox(label="Details")
    video_preview = gr.Video(label="Video Preview")

    generate_btn.click(
        generate_video_workflow, 
        inputs=[prompt, audio, theme, effects], 
        outputs=[output_text, video_preview]
    )

if __name__ == "__main__":
    ui.launch(share=True)
