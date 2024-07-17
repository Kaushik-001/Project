import tkinter as tk
from PIL import Image , ImageTk
import random 

window = tk.Tk()
window.geometry("500x360")
window.title("Dice Roll")

def roll_dice():
    a=random.randint(1,6)
    label = tk.Label(window,text=a).pack()
    
# PROVIDE THE LIST OF IMAGES
dice = ["Games/dice-six-faces-two.png","Games/dice-six-faces-three.png"
        ,"Games/dice-six-faces-six.png","Games/dice-six-faces-one.png"
        ,"Games/dice-six-faces-four.png","Games/dice-six-faces-five.png"] 

image1 = ImageTk.PhotoImage(Image.open(random.choice(dice))) #choose randomly from dice list for dice1
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice))) #choose randomly from dice list for dice2

label1 = tk.Label(window,image=image1)
label2 = tk.Label(window,image=image2)

label1.image = image1
label2.image = image2
 
label1.place(x=40,y=100) #coordinates for position of dice1
label2.place(x=600,y=100) #coordinates for position of dice2

def dice_roll():
    image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image = image1)
    label1.image = image1
    
    image2=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image = image2)
    label2.image = image2
    
button = tk.Button(window,text="ROLL",bg="green",fg="white",font= "Times 20 bold",command=dice_roll ) #FINALLT ROLLING THE DICE AND SETTING THE COLOR and FONT OF BUTTON
button.place(x=500,y=0) #Position of the Button

window.mainloop()
