#! usr/bin/python3
import tkinter as tk
import datetime

COLUMNS = 4 # number of columns of happy / sad faces

def add_to_log(behaviour, count):
    now = datetime.datetime.now()
    with open("log/behaviour.log", "a") as f:
        #It's tradition to put lines on separate lines of code
        f.write(now.strftime("%A, %B %d, %Y %I:%M%p:\n"))
        f.write(f"Behaviour: {behaviour.upper()}\n")
        f.write(f"Good count: {count}\n")
        f.write("\n")

class StickerFrame(tk.Frame):
    def __init__(self, master, behaviour, **kwargs):
        super().__init__(master, **kwargs)
        self.behaviour = behaviour
        self.img = tk.PhotoImage(file = f'gfx/{behaviour}.png')
        self.count = 0

        self.stickers = tk.Text(self, width=2, bg=self['bg'], highlightthickness=0, border=0)
        self.stickers.pack(fill=tk.BOTH, expand=True)
        btn = tk.Button(self, command=self.add_sticker, image=self.img, bg="black")
        btn.pack(side=tk.BOTTOM)

    def add_sticker(self):
        self.stickers.image_create(tk.END, image=self.img)
        self.count += 1
        add_to_log(self.behaviour, self.count)

class NameFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, bg="cyan", **kwargs)
        self.rowconfigure(1, weight=1) # fill all available vertical space, giving any extra room to the middle row
        self.columnconfigure(0, weight=1) # fill all available horizontal space

        self.name_img = tk.PhotoImage(file = "gfx/name.png") # dimensions 200x237
        name = tk.Label(self, image=self.name_img, bg="cyan")
        name.grid(sticky=tk.N)

        name_label = tk.Label(self, text="Name's\nBehaviour", bg="cyan") # This
        name_label.config(font=("MonospaceRegular, 38"))       # may need to be
        name_label.grid()              # adjusted according to name

        good_bad_label = tk.Label(self, text="GOOD\nor\nBAD", bg="cyan")
        good_bad_label.config(font=("MonospaceRegular, 50"))
        good_bad_label.grid(sticky=tk.S)

def main():
    root = tk.Tk()
    root.geometry("900x750")
    root.rowconfigure(0, weight=1) # fill all available vertical space
    # fill all available horizontal space, giving any extra room equally to column index 0 and 2 (the side columns)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(2, weight=1)

    happy_frame = StickerFrame(root, behaviour='good', bg="light green")
    happy_frame.grid(row=0, column=0, sticky='nsew')

    # set up the name Frame
    name_frame = NameFrame(root)
    name_frame.grid(row=0, column=1, sticky='nsew')

    sad_frame = StickerFrame(root, behaviour='bad', height=750, width=300, bg="red3")
    sad_frame.grid(row=0, column=2, sticky='nsew')

    root.mainloop()

if __name__ == '__main__':
    main()
