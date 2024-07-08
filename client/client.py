import os
import time
import Pyro5.api
from dotenv import load_dotenv

def main():
    token = os.getenv("SERVER_SECRET_TOKEN")
    with Pyro5.api.Proxy("PYRONAME:MUSEU_SALA_1.video_control") as server:
        while True:
            try:
                cmd = input("Enter command (play/pause/stop/exit): ")
                if cmd == "play":
                    server.play(token)
                elif cmd == "pause":
                    server.pause(token)
                elif cmd == "stop":
                    server.stop(token)
                elif cmd == "exit":
                    break
                time.sleep(1)
            except Exception as e:
                print(f"Erro ao executar comando: {e}")

if __name__ == "__main__":
    load_dotenv()
    main()
