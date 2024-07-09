import argparse
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk, ImageSequence
import qrcode

class App:
    def __init__(self, root, gif_path, code_text, top_message):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')

        # Load GIF
        self.gif_label = Label(self.root, bg='black')
        self.gif_label.pack(fill=tk.BOTH, expand=tk.YES)
        self.gif = Image.open(gif_path)
        self.gif_frames = [ImageTk.PhotoImage(img.copy().resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))) for img in ImageSequence.Iterator(self.gif)]
        self.gif_index = 0
        self.update_gif()

        # Create overlay for QR code and text at the bottom
        self.overlay_frame_bottom = tk.Frame(self.root, bg='black', bd=0)
        self.overlay_frame_bottom.place(relx=1.0, rely=1.0, anchor='se')

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=1,
        )
        qr.add_data(code_text)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save('qrcode.png')

        qr_img = Image.open('qrcode.png')
        qr_img = qr_img.resize((self.root.winfo_screenwidth() // 9, self.root.winfo_screenwidth() // 9))
        self.qr_code_image = ImageTk.PhotoImage(qr_img)

        # Display QR code
        self.qr_code_label = Label(self.overlay_frame_bottom, image=self.qr_code_image, bg='black')
        self.qr_code_label.pack(side=tk.BOTTOM, anchor='s')

        # Display code text
        self.text_label = Label(self.overlay_frame_bottom, text=code_text, font=('Arial', 64), bg='black', fg='white')
        self.text_label.pack(side=tk.BOTTOM, anchor='s')

        # Create overlay for top message
        self.overlay_frame_top = tk.Frame(self.root, bg='black', bd=0)
        self.overlay_frame_top.place(relx=0.5, rely=0.0, anchor='n')

        # Display top message
        self.top_message_label = Label(self.overlay_frame_top, text=top_message, font=('Arial', 46), bg='black', fg='white')
        self.top_message_label.pack(side=tk.TOP, anchor='n')

    def update_gif(self):
        self.gif_label.config(image=self.gif_frames[self.gif_index])
        self.gif_index = (self.gif_index + 1) % len(self.gif_frames)
        self.root.after(50, self.update_gif)  # Adjust the delay as needed

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Display a fullscreen GIF with a QR code and messages.")
    parser.add_argument('code_text', type=str, help="Text to encode in the QR code.")
    parser.add_argument('bg_gif', type=str, help="Path to the GIF file.")
    args = parser.parse_args()

    code_text = args.code_text
    gif_path = args.bg_gif
    top_message = "Leia o qrCode ou digite o codiog em nosso Site para controlar a exibição."

    root = tk.Tk()
    app = App(root, gif_path, code_text, top_message)
    root.mainloop()