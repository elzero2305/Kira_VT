from open_ai import generate_response
from speach_to_text import transformar_audio_a_texto
from subtitles_app import SubtitleApp
from Eleven import *
import winsound

#INICIA EL SCRIPT PARA LOS SUBTITULOS
subtitle_app = SubtitleApp()
subtitle_app.start()

#INICIAR EL PROGRAMA
def main():
    name = ""
    user_input = ""

    # Beep para saber si el programa inicio
    duration = 500  
    freq = 1000 
    winsound.Beep(freq, duration)

    while True:

        #TOMA LA PREGUNTA CONVERTIDA A TEXTO
        question = transformar_audio_a_texto().lower()
        
        '''
        #MUESTRA LA PREGUNTA COMO SUBTITULOS
        subtitle_app.set_text(question)

        #DICE LA PREGUNTA COMO VOZ
        try:
            audio_data = voice.generate_and_play_audio(question, playInBackground=False)
            if audio_data is not None:
                with open("Kira_VT/kira/pregunta.wav", "wb") as f:
                    f.write(audio_data)
                play(audio_data)
            else:
                print(" ")
        except Exception as e:
            print(f"Error al generar el audio: {str(e)}")
        '''

        #INGRESTA LA PREGUNTA EN CHAT-GPT
        user_input += f"\n {name}: " + question 

        #CREA LA RESPUESTA
        response = generate_response(user_input)

        if response:

            #TOMA LA RESPUESTA 
            answer = response.choices[0].text.strip()
            resp = f"Kira: " + answer + "\n"
            print(resp)
            
            #MUESTRA LA RESPUESTA COMO SUBTITULOS
            subtitle_app.set_text(answer)

            #DICE LA RESPUESTA COMO VOZ
            try:
                audio_data = voice.generate_and_play_audio(answer, playInBackground=False)
                if audio_data is not None:
                    with open("Kira_VT/kira/respuesta.wav", "wb") as f:
                        f.write(audio_data)
                    play(audio_data)
                else:
                    print("")
            except Exception as e:
                print(f"Error al generar el audio: {str(e)}")

#EJECUTA EL PROGRAMA
if __name__ == "__main__":
    main()



