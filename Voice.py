import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat
from azure.cognitiveservices.speech.audio import AudioOutputConfig

speech_key, service_region = "UseYourSpeechAPI", "eastus"

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

voice="Microsoft Server Speech Text to Speech Voice (en-US, GuyNeural)" #en-US-GuyRUS
speech_config.speech_synthesis_voice_name = voice
speech_config.set_speech_synthesis_output_format(SpeechSynthesisOutputFormat["Riff24Khz16BitMonoPcm"])

audio_config = AudioOutputConfig(filename="c:/OutputVoiceFile.mp3")

synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
synthesizer.speak_text_async("Hello World, This is a test of creating a playable mp3 file")
