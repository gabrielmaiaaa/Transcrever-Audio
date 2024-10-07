import whisper

modelo = whisper.load_model("base")

resposta = modelo.transcribe("teste.ogg")

print(resposta["text"])