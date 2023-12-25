import tkinter as tk
from PIL import Image, ImageTk
import random



window=tk.Tk()
window.geometry("500x360")
window.title("Dice Roll")
# def roll_dice():
#     a=random.randint(1,6)
#     label=tk.Label(window,text=a).pack()

# button = tk.Button(window,text="click",command=roll_dice)
# button.pack()




dice = ["1.png","2.png","3.png","4.png","5.png","6.png"]
image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2=ImageTk.PhotoImage(Image.open(random.choice(dice)))
label1=tk.Label(window,image=image1)
label2=tk.Label(window,image=image2)


label1.image=image1
label2.palce=image2

label1.place(x=40,y=100)
label2.place(x=300,y=100)

def dice_roll():
    image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image=image1
    
    
    image2=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image=image2)
    label2.image=image2



button = tk.Button(window,text="Roll",bg="green",fg="white",command=dice_roll)
button.place(x=230,y=0)


window.mainloop()