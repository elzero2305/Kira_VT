import speech_recognition as sr

#Transforma el audio a texto
def transformar_audio_a_texto():
    r = sr.Recognizer()
    with sr.Microphone() as origen:
        r.pause_threshold = 0.8
        name = ""
        print("Escuchando")
        audio = r.listen(origen)
        try:
            pedido = r.recognize_google(audio, language="es-MX") # Se debe especificar el lenguaje con el que se reconoce la voz
            print(f"\n {name}: " + pedido)
            return pedido

        except sr.UnknownValueError:
            print("Ups, no entendi!")
            return " "

        except sr.RequestError:
            print("Ups, no hay servicio!")
            return " "

        except:
            print("Ups, algo salio mal!")
            return " "

