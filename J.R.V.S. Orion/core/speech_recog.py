import torch
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import sounddevice as sd

# Ładowanie modelu
model_name = "facebook/wav2vec2-base-960h"
processor = Wav2Vec2Processor.from_pretrained(model_name)
model = Wav2Vec2ForCTC.from_pretrained(model_name)

def record_audio(duration=5, sample_rate=16000):
    """
    Nagrywa dźwięk z mikrofonu przez określony czas.
    """
    print("Nagrywam...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
    sd.wait()
    print("Nagrywanie zakończone!")
    return audio.flatten()

def speech_to_text(audio):
    """
    Zamienia nagrany dźwięk na tekst za pomocą modelu Wav2Vec2.
    """
    input_values = processor(audio, sampling_rate=16000, return_tensors="pt").input_values
    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)
    return transcription[0]
