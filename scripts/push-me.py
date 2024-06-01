import tkinter as tk
import tkinter.ttk as ttk
import random

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Push me!!")
        self.master.geometry("450x450")
        self.master.resizable(False, False)
        self.createWidgets()

    def createWidgets(self):
        # Define objects
        self.title_label = ttk.Label(self.master, text="Click on the button below ...", font=("Meiryo", 18))
        self.button = ttk.Button(self.master, text="Push me :D", command=self.onButtonClick)

        # Layout objects
        self.title_label.place(x=60, y=20)
        self.button.place(x=190, y=220)

    def onButtonClick(self):
        i = random.randrange(0, 374, 1)
        j = random.randrange(60, 400, 1)
        self.button.place(x=i, y=j)

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
