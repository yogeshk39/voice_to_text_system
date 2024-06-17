# audio_processing.py

import noisereduce as nr
import webrtcvad
from pydub import AudioSegment
from pydub.silence import split_on_silence

def preprocess_audio(file_path):
    audio = AudioSegment.from_file(file_path)
    normalized_audio = audio.normalize()

    samples = normalized_audio.get_array_of_samples()
    reduced_noise_samples = nr.reduce_noise(y=samples, sr=normalized_audio.frame_rate)
    reduced_noise_audio = normalized_audio._spawn(reduced_noise_samples)

    vad = webrtcvad.Vad()
    vad.set_mode(1)
    chunks = split_on_silence(reduced_noise_audio, min_silence_len=500, silence_thresh=reduced_noise_audio.dBFS-14)
    return chunks

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python audio_processing.py <audio_file>")
    else:
        chunks = preprocess_audio(sys.argv[1])
        for i, chunk in enumerate(chunks):
            chunk.export(f"chunk{i}.wav", format="wav")
        print(f"Processed audio into {len(chunks)} chunks.")
