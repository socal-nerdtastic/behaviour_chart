#! usr/bin/python
import tkinter as tk
import datetime

def add_happy_sticker(happy_x_pos, happy_y_pos):
    """
    Displays sticker to screen
    as set by happy_button_call,
    writes details to log
    """
    global happy_count
    now = datetime.datetime.now()
    timedate = now.strftime("%A, %B %d, %Y ")+now.strftime("%I:%M%p:")
    happy_count += 1
    print(happy_count)
    file = open("log/behaviour.log", "a")
    file.write(str(timedate)+"\nBehaviour: GOOD\nGood count: " \
                                        +str(happy_count)+"\n\n")
    file.close() 
    happy = tk.Label(happy_frame, image=happy_img, bg="light green")
    happy.place(x=happy_x_pos, y=happy_y_pos)

def add_sad_sticker(sad_x_pos, sad_y_pos):
    """
    Displays sticker to screen
    as set by sad_button_call,
    writes details to log
    """
    global sad_count
    now = datetime.datetime.now()
    timedate = now.strftime("%A, %B %d, %Y ")+now.strftime("%I:%M%p:")
    sad_count += 1
    print(sad_count)
    file = open("log/behaviour.log", "a")
    file.write(str(timedate)+"\nBehaviour: BAD\nBad count: " \
                                        +str(sad_count)+"\n\n")
    file.close() 
    sad = tk.Label(sad_frame, image=sad_img, bg="red3")
    sad.place(x=sad_x_pos, y=sad_y_pos)
    
def happy_button_call():
    """
    On button press, this will 
    set the position of the sticker
    according to their x,y values
    set by the conditionals below,
    then calls the function
    add_happy_sticker
    """
    global happy_x_pos, happy_y_pos
    print(happy_x_pos)
    
    if happy_x_pos == 0:
        add_happy_sticker(happy_x_pos, happy_y_pos)
        happy_x_pos += 75
    elif happy_x_pos == 75:
        happy_x_pos += 1
    if happy_x_pos == 76:
        happy_x_pos = 75
        add_happy_sticker(happy_x_pos, happy_y_pos)
        happy_x_pos += 75
    elif happy_x_pos > 75 and happy_x_pos != 76:
        add_happy_sticker(happy_x_pos, happy_y_pos)
        happy_x_pos += 75
    
    if happy_x_pos > 225:
        happy_x_pos = 0
        if happy_y_pos == 0:
            add_happy_sticker(happy_x_pos, happy_y_pos)
            happy_y_pos += 75
        elif happy_y_pos == 75:
            happy_y_pos += 1
        if happy_y_pos == 76:
            happy_y_pos = 75
            add_happy_sticker(happy_x_pos, happy_y_pos)
            happy_y_pos += 75
        elif happy_y_pos > 75 and happy_y_pos != 76:
            add_happy_sticker(happy_x_pos, happy_y_pos)
            happy_y_pos += 75
    return happy_x_pos, happy_y_pos

def sad_button_call():
    """
    On button press, this will 
    set the position of the sticker
    according to their x,y values
    set by the conditionals below,
    then calls the function
    add_sad_sticker 
    """
    global sad_x_pos, sad_y_pos
    print(sad_x_pos)
    
    if sad_x_pos == 0:
        add_sad_sticker(sad_x_pos, sad_y_pos)
        sad_x_pos += 75
    elif sad_x_pos == 75:
        sad_x_pos +=1
    if sad_x_pos == 76:
        sad_x_pos = 75
        add_sad_sticker(sad_x_pos, sad_y_pos)
        sad_x_pos += 75
    elif sad_x_pos > 75 and sad_x_pos != 76:
        add_sad_sticker(sad_x_pos, sad_y_pos)
        sad_x_pos += 75
    
    if sad_x_pos > 225:
        sad_x_pos = 0
        if sad_y_pos == 0:
            add_sad_sticker(sad_x_pos, sad_y_pos)
            sad_y_pos += 75
        elif sad_y_pos == 75:
            sad_y_pos +=1
        if sad_y_pos == 76:
            sad_y_pos = 75
            add_sad_sticker(sad_x_pos, sad_y_pos)
            sad_y_pos += 75
        elif sad_y_pos > 75 and sad_y_pos != 76:
            add_sad_sticker(sad_x_pos, sad_y_pos)
            sad_y_pos += 75
    return sad_x_pos, sad_y_pos
    

root = tk.Tk()
root.wm_attributes("-type", "splash")
root.geometry("900x750")

happy_x_pos = 0
happy_y_pos = 0
happy_count = 0
sad_x_pos = 0
sad_y_pos = 0
sad_count = 0

happy_img = tk.PhotoImage(file = "gfx/happy.png") # dimensions 75x75
sad_img = tk.PhotoImage(file = "gfx/sad.png") # dimensions 75x75
name_img = tk.PhotoImage(file = "gfx/name.png") # dimensions 200x237
                                                
happy_frame = tk.Frame(root, height=750, width=300, bg="light green")
happy_frame.pack(side=tk.LEFT)
sad_frame = tk.Frame(root, height=750, width=300, bg="red3")
sad_frame.pack(side=tk.RIGHT)
name_frame = tk.Frame(root, height=750, width=300,bg="cyan")
name_frame.pack()
name = tk.Label(name_frame, image=name_img, bg="cyan")
name.place(x=50, y=0)                    

name_label = tk.Label(name_frame, text="Name's", bg="cyan") # This 
name_label.config(font=("MonospaceRegular, 38"))       # may need to be 
name_label.place(x=61, y=300)              # adjusted according to name

behaviour_label = tk.Label(name_frame, text="Behaviour", bg="cyan")
behaviour_label.config(font=("MonospaceRegular, 38"))
behaviour_label.place(x=38, y=360)
good_bad_label = tk.Label(name_frame, text="GOOD\nor\nBAD", bg="cyan")
good_bad_label.config(font=("MonospaceRegular, 50"))
good_bad_label.place(x=48, y=500)

happy_button = tk.Button(happy_frame, height=67, width=67, \
                command=happy_button_call, image=happy_img, bg="black")
happy_button.place(x=105, y=674)

sad_button = tk.Button(sad_frame, height=67, width=67, \
                    command=sad_button_call, image=sad_img, bg="black")
sad_button.place(x=115, y=673)

root.mainloop()
