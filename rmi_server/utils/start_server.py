import requests
import os

def server_registry(server_name,server_uri):
  server_url = os.getenv("SERVICE_EXPORT_BACKEND_URI")
  server_token = os.getenv("SERVICE_EXPORT_BACKEND_ACCESS_TOKEN")
  request_data = {
    "nmRmiServer":server_name,
    "nmRmiServerUri":server_uri
  }
  resp = requests.post(f"{server_url}/api/museu",json=request_data,headers={"session_token":server_token})
  if resp.status_code != 200:
    raise Exception(f"Erro ao iniciar servidor: falha ao contactar servidor princial. Erro: {resp.text}")
  