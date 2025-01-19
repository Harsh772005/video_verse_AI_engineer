# import librosa
# import os

# def trim_audio(audio_path, temp_dir):
#     output_path = os.path.join(temp_dir, "trimmed_audio.wav")
#     audio, sr = librosa.load(audio_path, sr=None)
#     trimmed_audio = audio[:10 * sr]  # Trim to 10 seconds
#     librosa.output.write_wav(output_path, trimmed_audio, sr)
#     return output_path, sr

# def detect_beats(audio_path):
#     audio, sr = librosa.load(audio_path, sr=None)
#     tempo, beat_frames = librosa.beat.beat_track(y=audio, sr=sr)
#     beat_times = librosa.frames_to_time(beat_frames, sr=sr)
#     return tempo, beat_times





import librosa
import soundfile as sf
import os

def trim_audio(audio_path, temp_dir="./temp/audio", duration=30):
    """
    Trims the audio to a specified duration.

    Args:
        audio_path (str): Path to the audio file.
        temp_dir (str): Directory to save the trimmed audio.
        duration (int): Duration in seconds to trim the audio.

    Returns:
        tuple: Path to the trimmed audio file and sample rate.
    """
    try:
        os.makedirs(temp_dir, exist_ok=True)
        y, sr = librosa.load(audio_path, sr=None)
        trimmed_audio = y[:int(sr * duration)]
        output_path = os.path.join(temp_dir, "trimmed_audio.wav")
        sf.write(output_path, trimmed_audio, sr)
        return output_path, sr
    except Exception as e:
        raise RuntimeError(f"Error trimming audio: {str(e)}")

def detect_beats(audio_path):
    """
    Detects beats and tempo from the audio.

    Args:
        audio_path (str): Path to the audio file.

    Returns:
        tuple: Tempo and beat frames as a list of timestamps.
    """
    try:
        y, sr = librosa.load(audio_path, sr=None)
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        beat_times = librosa.frames_to_time(beat_frames, sr=sr)
        return tempo, beat_times.tolist()
    except Exception as e:
        raise RuntimeError(f"Error detecting beats: {str(e)}")
