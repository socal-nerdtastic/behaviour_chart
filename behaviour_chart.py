#! usr/bin/python
import tkinter as tk
import datetime

COLUMNS = 4 # number of columns of happy / sad faces

def add_happy_sticker():
    """
    Displays sticker to screen
    as set by happy_button_call,
    writes details to log
    """
    global happy_count
    happy = tk.Label(happy_faces, image=happy_img, bg="light green")
    r, c = divmod(happy_count, COLUMNS)
    happy.grid(row=r, column=c)

    now = datetime.datetime.now()
    timedate = now.strftime("%A, %B %d, %Y ")+now.strftime("%I:%M%p:")
    happy_count += 1
    print(happy_count)
    file = open("log/behaviour.log", "a")
    file.write(str(timedate)+"\nBehaviour: GOOD\nGood count: " \
                                        +str(happy_count)+"\n\n")
    file.close()

def add_sad_sticker():
    """
    Displays sticker to screen
    as set by sad_button_call,
    writes details to log
    """
    global sad_count
    sad = tk.Label(sad_faces, image=sad_img, bg="red3")
    r, c = divmod(sad_count, COLUMNS)
    sad.grid(row=r, column=c)

    now = datetime.datetime.now()
    timedate = now.strftime("%A, %B %d, %Y ")+now.strftime("%I:%M%p:")
    sad_count += 1
    print(sad_count)
    file = open("log/behaviour.log", "a")
    file.write(str(timedate)+"\nBehaviour: BAD\nBad count: " \
                                        +str(sad_count)+"\n\n")
    file.close()

root = tk.Tk()
# ~ root.wm_attributes("-type", "splash")
root.geometry("900x750")

happy_count = 0
sad_count = 0

happy_img = tk.PhotoImage(file = "gfx/happy.png") # dimensions 75x75
sad_img = tk.PhotoImage(file = "gfx/sad.png") # dimensions 75x75
name_img = tk.PhotoImage(file = "gfx/name.png") # dimensions 200x237

happy_frame = tk.Frame(root, height=750, width=300, bg="light green")
happy_frame.pack_propagate(False) # obey size definition above (do not adjust to child widget size)
happy_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
happy_faces = tk.Frame(happy_frame, bg="light green")
happy_faces.pack(fill=tk.BOTH, expand=True)
# when using an image, let the size of the image define the Button size; don't override it
happy_button = tk.Button(happy_frame, # note newline escapes are not needed
    command=add_happy_sticker,
    image=happy_img, bg="black")
happy_button.pack(side=tk.BOTTOM)

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

sad_frame = tk.Frame(root, height=750, width=300, bg="red3")
sad_frame.pack_propagate(False)
sad_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
sad_faces = tk.Frame(sad_frame, bg="red3")
sad_faces.pack(fill=tk.BOTH, expand=True)
sad_button = tk.Button(sad_frame, command=add_sad_sticker, image=sad_img, bg="black")
sad_button.pack(side=tk.BOTTOM)

root.mainloop()
