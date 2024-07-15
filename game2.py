#step 1

import tkinter
from PIL import Image, ImageTk
import random


#step 2

root = tkinter.Tk()
root.geometry('1920x1080')
root.title('Roll the dice')
root.configure(bg='white')


#step 3
l0 = tkinter.Label(root, text='  ')
l0.pack()
l1 = tkinter.Label(root, text='Hello this is a dice rolling game', fg="black", bg="#B9C6C9",
                   font="Algerian 16 bold italic")
l1.pack()


#step4

dice = ['1st Face.png', '2ed Face.png', '3ed Face.png', '4th Face.png', '5th Face.png', '6th Face.png']
image2 = ImageTk.PhotoImage(file='dice.png')
label1 = tkinter.Label(root, image=image2)
label1.image = image2
label1.pack( expand=True)


#step5

def rolling_dice():
    image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1 ,bg='#B9C6C9')
    label1.image=image1

button = tkinter.Button(root, text='Roll the Dice', font="Algerian", width=20, height=2, bg="#FE3939", fg="white", command=rolling_dice)
button.pack(expand=True)
root.mainloop()
