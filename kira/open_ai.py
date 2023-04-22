import openai
import os

#Carga la api de openai
def load_api_key():
    api_key_path = os.path.abspath("Kira_VT/kira/keys/api_key.txt")
    with open(api_key_path, "r") as f:
        return f.read().strip()

openai.api_key = load_api_key()

#Carga el prompt
def prompt():
    try:
        rol_path = os.path.abspath("Kira_VT/kira/prompt/rol.txt")
        with open(rol_path, "r", encoding="utf-8") as f:
            prompt = f.read()
        return prompt
    except Exception as e:
        print(f"Error al cargar el archivo de roles: {e}")
        return None
    
#Inicia la api de chat-gpt en base al prompt
def generate_response(prompt):
    name = ("Xabian")
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.8,
            max_tokens=80,
            top_p=0.3,
            frequency_penalty=0.5,
            presence_penalty=0.0,
            stop=["\n", f"\n {name}: ", " Kira:"]
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error: {e}")
        return None
    

