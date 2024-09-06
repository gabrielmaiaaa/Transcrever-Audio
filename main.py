import whisper

modelo = whisper.load_model("medium")

resposta = modelo.transcribe("teste.ogg")

print(resposta["text"])