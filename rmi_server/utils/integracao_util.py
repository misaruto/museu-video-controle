import os
import requests

server_url = os.getenv("SERVICE_EXPORT_BACKEND_URI")
server_token = os.getenv("SERVICE_EXPORT_BACKEND_ACCESS_TOKEN")

def generate_new_auth_code(server_name):
    # Monta os dados da requisição
    request_data = {
        "rmiServer": {
            "nmRmiServer": server_name
        }
    }

    try:
        # Faz a requisição POST
        resp = requests.post(
            f"http://127.0.0.1:5000/api/museu/server/auth/code",
            json=request_data,
            headers={"session_token": server_token}
        )

        # Verifica o código de status da resposta
        if resp.status_code != 200:
            raise Exception(f"Erro ao iniciar servidor: falha ao contactar servidor principal. Erro: {resp.text}")

        # Obtém e retorna os dados da resposta JSON
        data = resp.json().get("data")
        return data.get("cdRmiServerAuth")

    except requests.exceptions.RequestException as e:
        # Captura e trata exceções de requisição
        raise Exception(f"Erro ao fazer requisição HTTP: {str(e)}")