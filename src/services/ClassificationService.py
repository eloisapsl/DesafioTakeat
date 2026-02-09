import os
from dotenv import load_dotenv
from openai import OpenAI
from models.Schemas import MensagemRequest, MensagemResponse
from pathlib import Path
import json

load_dotenv()

dir_prompt = Path("..\src\prompts\prompt.txt")


# Carrega o prompt base de classificação a partir do arquivo prompt.txt presente no diretório.
def load_prompt() -> str:
    try:
        with open(dir_prompt, 'r') as f:
            prompt = f.read()
            return prompt
    except Exception as e:
        raise ValueError("Erro ao abrir arquivo. Tente novamente.")


# Envia o prompt e a mensagem do usuário para a OpenAI Responses API e retorna o texto da resposta ainda sem formatação.
def call_responses_api(prompt: str, message: MensagemRequest) -> str:
    client = OpenAI(api_key=os.getenv("API_KEY"))

    message_json = message.model_dump_json()
    context = [
        {
            "role": "system",
            "content": (
                prompt
            )
        },
        {
            "role": "user",
            "content": message_json
        }
    ]

    response = client.responses.create(
        model="gpt-4o",
        input=context,
    )
    return response.output_text


# Orquestra o fluxo de classificação, valida a resposta da API e converte a resposta em JSON.
def classify_message(message: MensagemRequest) -> MensagemResponse:

    prompt = load_prompt()
    texto_response = call_responses_api(prompt, message)

    if not texto_response:
        raise ValueError("Resposta da Requests API vazia. Tente novamente.")

    try:
        data = json.loads(texto_response)
    except json.JSONDecodeError as e:
        raise ValueError(
            f"Resposta não é JSON válido:\n{texto_response}"
        ) from e

    return data
