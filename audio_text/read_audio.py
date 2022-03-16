from pydub import AudioSegment
import speech_recognition as sr
import math

# mp3 轉 aac
def trans_mp3_to_aac(filepath, filename):
    song = AudioSegment.from_file(filepath, "mp3")
    song.export("./" + filename + ".aac", format="mp4")
    return math.ceil(song.duration_seconds)

# aac 轉 wav
def trans_aac_to_wav(filepath, filename):
    song = AudioSegment.from_file(filepath, "mp4")
    song.export("./" + filename + ".wav", format="wav")

def trans_wav_to_text(filepath):
	r = sr.Recognizer()#預設辨識英文
	with sr.WavFile(filepath) as source:#讀取wav檔
	    audio = r.record(source)
	try:
	    print("Transcription: " + r.recognize_google(audio,language="zh-TW")) #使用Google的服務
	    return r.recognize_google(audio,language="zh-TW")
	except LookupError:
	    return "Could not understand audio"

trans_aac_to_wav('./002.m4a', '002')
trans_wav_to_text('./002.wav')
