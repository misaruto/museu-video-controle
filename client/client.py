import os
import time
import Pyro5.api
from dotenv import load_dotenv

def main():
    token = os.getenv("SERVER_SECRET_TOKEN")
    # sala = input("A qual sala voce quer se conectar? ")
    sala = 'MUSEU_SALA_1'
    ns = Pyro5.api.locate_ns(host=os.getenv('NAME_SERVER_HOST'),port=os.getenv('NAME_SERVER_PORT'))
    uri = ns.lookup(f'{sala}.video_handler')
    with Pyro5.api.Proxy(uri) as server:
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
