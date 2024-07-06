import Pyro5.api
import sys
import time

def main():
    if len(sys.argv) != 2:
        print("Usage: python client.py <path_to_video>")
        sys.exit(1)

    video_path = sys.argv[1]
    with Pyro5.api.Proxy("PYRONAME:example.video_control") as server:
        while True:
            cmd = input("Enter command (play/pause/stop/exit): ")
            if cmd == "play":
                server.play(video_path)
            elif cmd == "pause":
                server.pause()
            elif cmd == "stop":
                server.stop()
            elif cmd == "exit":
                break
            time.sleep(1)

if __name__ == "__main__":
    main()
