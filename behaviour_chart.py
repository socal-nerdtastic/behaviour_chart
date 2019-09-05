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

        self.stickers = tk.Frame(self, bg=self['bg'])
        self.stickers.pack()
        btn = tk.Button(self, command=self.add_sticker, image=self.img, bg="black")
        btn.pack(side=tk.BOTTOM)

    def add_sticker(self):
        lbl = tk.Label(self.stickers, image=self.img, bg=self['bg'])
        r, c = divmod(self.count, COLUMNS)
        lbl.grid(row=r, column=c)
        self.count += 1
        add_to_log(self.behaviour, self.count)

def main():
    root = tk.Tk()
    root.wm_attributes("-type", "splash")
    root.geometry("900x750")

    name_img = tk.PhotoImage(file = "gfx/name.png") # dimensions 200x237

    happy_frame = StickerFrame(root, behaviour='good', height=750, width=300, bg="light green")
    happy_frame.pack_propagate(False) # obey size definition above (do not adjust to child widget size)
    happy_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # set up the name Frame
    name_frame = tk.Frame(root, height=750, width=300,bg="cyan")
    name_frame.rowconfigure(1, weight=1) # fill all available vertical space, giving any extra room to the middle row
    name_frame.columnconfigure(0, weight=1) # fill all available horizontal space
    name_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    name = tk.Label(name_frame, image=name_img, bg="cyan")
    name.grid(sticky=tk.N)

    name_label = tk.Label(name_frame, text="Name's\nBehaviour", bg="cyan") # This
    name_label.config(font=("MonospaceRegular, 38"))       # may need to be
    name_label.grid()              # adjusted according to name

    good_bad_label = tk.Label(name_frame, text="GOOD\nor\nBAD", bg="cyan")
    good_bad_label.config(font=("MonospaceRegular, 50"))
    good_bad_label.grid(sticky=tk.S)

    sad_frame = StickerFrame(root, behaviour='bad', height=750, width=300, bg="red3")
    sad_frame.pack_propagate(False)
    sad_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    root.mainloop()

if __name__ == '__main__':
    main()
