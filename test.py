import subprocess
from pydub import AudioSegment

# Convert the MP3 to WAV manually using ffmpeg
subprocess.run([
    r"C:\ffmpeg\bin\ffmpeg.exe",
    "-y",  # Overwrite output if it exists
    "-i", "Fallen_Symphony.mp3",
    "temp_output.wav"
])

# Now load the WAV file
song = AudioSegment.from_wav("temp_output.wav")
print(f"Song length: {len(song)} ms")  # Should be correct
