import tkinter as tk
import threading


class SubtitleApp(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.text = None
        self.text_initialized_event = threading.Event()

    def run(self):
        self.root = tk.Tk()
        self.root.title('KIRA Subs')
        self.root.configure(background='#ff007f')
        self.root.minsize(200, 100)
        self.root.maxsize(600, 800)
        self.root.wm_attributes("-topmost", 1)

        self.text = tk.StringVar()
        self.text.set('Iniciando KIRA...')
        self.text_initialized_event.set()

        label = tk.Label(self.root, textvariable=self.text, wraplength=480, font=(
            'Cute Letters', 30), fg='white', bg='black')
        label.pack()

        self.root.mainloop()

    def set_text(self, new_text):
        if not self.text_initialized_event.wait(timeout=1):
            raise RuntimeError("Timed out waiting for text initialization")
        self.text.set(new_text)

    def quit(self):
        self.root.destroy()
