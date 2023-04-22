import speech_recognition as sr

#Transforma el audio a texto
def transformar_audio_a_texto():
    r = sr.Recognizer()
    with sr.Microphone() as origen:
        r.pause_threshold = 0.8

        #nombre del uruario
        name = ""

        #muestra esto cuando el microfono esta abierto y se puede hablar
        print("Escuchando")
        audio = r.listen(origen)

        #Toma el texto y lo imprime en la terminal
        try:
            pedido = r.recognize_google(audio, language="es-MX") # Se debe especificar el lenguaje con el que se reconoce la voz
            print(f"\n {name}: " + pedido)
            return pedido

        #Si no se obtiene un texto
        except sr.UnknownValueError:
            print("Ups, no entendi!")
            return " "

        #Si la api falla
        except sr.RequestError:
            print("Ups, no hay servicio!")
            return " "

        #Si no se puede tomar el texto
        except:
            print("Ups, algo salio mal!")
            return " "

