import os
import sys
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound

def transcribe_translate_speak(audio_path):
    # Função para transcrever o áudio em texto
    def transcribe_audio(audio_path):
        recognizer = sr.Recognizer()
        audio_file = sr.AudioFile(audio_path)
        
        with audio_file as source:
            audio_data = recognizer.record(source)
        
        try:
            text = recognizer.recognize_google(audio_data, language='pt-BR')
            return text
        except sr.UnknownValueError:
            return "Não reconhecimento da fala."
        except sr.RequestError:
            return "Erro na requisição."

    # Não era necessário, mas já que teve a pergunta de tradução - função para traduzir o texto
    def translate_text(text):
        translator = Translator()
        translation = translator.translate(text, src='pt', dest='en')
        return translation.text

    # Função para converter texto em fala e reproduzir
    def speak_text(text):
        tts = gTTS(text=text, lang='en')
        tts.save("prova2.mp3")
        playsound.playsound("prova2.mp3")
        os.remove("prova2.mp3")

    recognized_text = transcribe_audio(audio_path)
    if recognized_text:
        print("Texto reconhecido:", recognized_text)
        translated_text = translate_text(recognized_text)
        print("Texto traduzido:", translated_text)
        speak_text(translated_text)
    else:
        print("Não foi possível reconhecer a fala no arquivo.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python nome_do_arquivo.py caminho_para_o_arquivo_de_audio")
    else:
        audio_file_path = sys.argv[1]
        transcribe_translate_speak(audio_file_path)