# import torch
# import whisperx
# import gc
from dotenv import load_dotenv
import os
import time
import json

# Load environment variables from .env file
load_dotenv()


class Transcribe():
    def __init__(self, model_name="small", device="cpu", compute_type="int8", use_auth_token=None):
        # self.model = whisperx.load_model(
        #     model_name, device, compute_type=compute_type)
        # self.model_a = None
        # self.metadata = None
        # self.diarize_model = whisperx.DiarizationPipeline(
        #     use_auth_token=use_auth_token, device=device)
        self.device = device
        self.audio_file = "None"
        self.audio = None

    def check_audio(self, audio_file):
        if self.audio_file != audio_file:
            self.audio_file = audio_file
            # self.audio = whisperx.load_audio(audio_file)

    def transcribe_audio(self, audio_file, batch_size=16, store_transcription=False):
        # self.check_audio(audio_file)
        # result = self.model.transcribe(self.audio, batch_size=batch_size)
        result = {
            "segments": [
                {
                    "text": " Kalau angkat dari Bapak",
                    "start": 0.537,
                    "end": 30.153
                }],
            "language": "id"
        }
        time.sleep(5)
        return result

    def align_transcription(self, result, audio_file):
        # self.check_audio(audio_file)
        # if self.model_a is None:
        #     self.model_a, self.metadata = whisperx.load_align_model(
        #         language_code=result["language"], device=self.device)
        # result = whisperx.align(result["segments"], self.model_a,
        #                         self.metadata, self.audio, self.device, return_char_alignments=False)
        result = {
            "segments": [
                {
                    "start": 0.031,
                    "end": 3.097,
                    "text": " There's a",
                    "words": [
                        {"word": "There's", "start": 0.031,
                            "end": 0.251, "score": 0.671},
                        {"word": "a", "start": 0.292, "end": 0.312, "score": 0.999},
                    ]
                }
            ],
            "word_segments": [
                {"word": "There's", "start": 0.031, "end": 0.251, "score": 0.671},
                {"word": "a", "start": 0.292, "end": 0.312, "score": 0.999},
            ]
        }
        time.sleep(5)
        return result

    def diarize_transcription(self, result, audio_file):
        # self.check_audio(audio_file)
        # diarize_segments = self.diarize_model(self.audio)
        # result = whisperx.assign_word_speakers(diarize_segments, result)
        result = {
            "segments": [
                {
                    "start": 1.128,
                    "end": 3.97,
                    "text": " Hello Karl",
                    "words": [
                        {
                            "word": "Hello",
                            "start": 1.128,
                            "end": 1.368,
                            "score": 0.639,
                            "speaker": "SPEAKER_00"
                        },
                        {
                            "word": "Karl",
                            "start": 1.428,
                            "end": 1.768,
                            "score": 0.813,
                            "speaker": "SPEAKER_00"
                        },
                    ],
                    "speaker": "SPEAKER_00"
                },
            ],
            "word_segments": [
                {
                    "word": "Hello",
                    "start": 1.128,
                    "end": 1.368,
                    "score": 0.639,
                    "speaker": "SPEAKER_00"
                },
                {
                    "word": "Karl,",
                    "start": 1.428,
                    "end": 1.768,
                    "score": 0.813,
                    "speaker": "SPEAKER_00"
                },
            ]
        }
        time.sleep(5)
        return result

    def delete_models(self):
        del self.model
        del self.model_a
        del self.metadata
        # gc.collect()
        # torch.cuda.empty_cache()


# Usage
if __name__ == "__main__":
    print("Loading Model...")
    start = time.time()
    transcriber = Transcribe(use_auth_token=os.getenv("HUGGINGFACE_TOKEN"))
    print(f"Model Loaded in {time.time() - start} seconds")
    # for 21.2s audio file:
    # transcribing in 143.05448389053345 second -> 0.14s per second
    # aligning in 42.37880206108093 second -> 0.04s per second
    # diarizing in 2426.9272611141205 second -> 2.42s per second

    audio_file = "sounds/test 1/Karl Harrison_converted.mp3"
    audio_file = "sounds/test 2/Jokowi Mata Najwa.mp3"
    # audio_file = "sounds/test 2/Vivek Podcast.mp3"

    file_extension = "." + audio_file.split(".")[-1]

    start = time.time()
    print("Transcribing Audio...")
    result = transcriber.transcribe_audio(audio_file)
    json.dump(result, open(audio_file.replace(
        file_extension, "_transcription.json"), "w"))
    print(f"Transcribed in {time.time() - start} seconds")

    start = time.time()
    print("Aligning Transcription...")
    result = transcriber.align_transcription(result, audio_file)
    json.dump(result, open(audio_file.replace(
        file_extension, "_transcription.json"), "w"))
    print(f"Aligned in {time.time() - start} seconds")

    start = time.time()
    print("Diarizing Audio...")
    result = transcriber.diarize_transcription(result, audio_file)
    json.dump(result, open(audio_file.replace(
        file_extension, "_transcription.json"), "w"))
    print(f"Diarized in {time.time() - start} seconds")
