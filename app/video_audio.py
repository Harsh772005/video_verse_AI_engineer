from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip

def synchronize_audio_video(audio_path, video_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)
    final_video = video_clip.with_audio(audio_clip)
    output_path = video_path.replace(".mp4", "_synced.mp4")
    final_video.write_videofile(output_path, codec="libx264", audio_codec="aac",fps=video_clip.fps)
    return output_path
