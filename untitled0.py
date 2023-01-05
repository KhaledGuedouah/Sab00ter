# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 19:27:12 2023

@author: khale
"""
from tkinter import *
from PIL import Image , ImageTk
D = 'LiN+'
F = 'D'
card = Image.open(f"CARDS\D.png")
def resize_cards(cardPath) : 
     card_img = Image.open(cardPath)
     #resize the image
     global resized_card_img
     resized_card_img = card_img.resize((50,50)) 
     our_card_image = ImageTk.PhotoImage(resized_card_img)
     return our_card_image
 
def helloCallBack():
   msg = Message(root, text = "tizmokk")
   msg.config(bg='lightgreen', font=('times', 24, 'italic'))
   msg.pack()
"""
root = Tk()
root.title('SabOOter')
root.geometry("900x500")
root.configure(background = "green")
global frame
frame = Frame(root,bg = "green")
frame.pack(pady = 20)
"""
cardlist = ["D" , "LiN+","LiNx","LiPN+","PN+","LN-"]
def close_win():
   root.destroy()
   return 1 
def display_text():
   global string
   string= e1.get()
   print(string)
   root.destroy()
def DisplayHand(cardlist) : 
    global root
    root = Tk()
    root.title('SabOOter')
    root.geometry("900x500")
    root.configure(background = "green")
    global frame
    frame = Frame(root,bg = "green")
    frame.pack(pady = 20)
    
    Card1 = LabelFrame(frame,text = "Card 1" , bd = 0)
    Card1.grid(row = 0 , column = 0 , padx = 20 , ipadx = 20)
    Card2 = LabelFrame(frame,text = "Card 2" , bd = 0)
    Card2.grid(row = 0 , column = 2 , padx = 20 , ipadx = 20)
    Card3 = LabelFrame(frame,text = "Card 3" , bd = 0)
    Card3.grid(row = 0 , column = 3 , padx = 20 , ipadx = 20)
    Card4 = LabelFrame(frame,text = "Card 4" , bd = 0)
    Card4.grid(row = 0 , column = 4 , padx = 20 , ipadx = 20)
    Card5 = LabelFrame(frame,text = "Card 5" , bd = 0)
    Card5.grid(row = 0 , column = 5 , padx = 20 , ipadx = 20)
    Card6 = LabelFrame(frame,text = "Card 6" , bd = 0)
    Card6.grid(row = 0 , column = 6 , padx = 20 , ipadx = 20)
    
    Card1_label = Label(Card1  , text = '')
    Card1_label.pack(pady = 20)
    Card2_label = Label(Card2  , text = '')
    Card2_label.pack(pady = 20)
    Card3_label = Label(Card3 , text = '')
    Card3_label.pack(pady = 20)
    Card4_label = Label(Card4 , text = '')
    Card4_label.pack(pady = 20)
    Card5_label = Label(Card5 , text = '')
    Card5_label.pack(pady = 20)
    Card6_label = Label(Card6 , text = '')
    Card6_label.pack(pady = 20)
    
    
    C1_image = resize_cards(f'CARDS\{cardlist[0]}.png')
    Card1_label.config(image = C1_image)
    
    C2_image = resize_cards(f'CARDS\{cardlist[1]}.png')
    Card2_label.config(image = C2_image)
    
    C3_image = resize_cards(f'CARDS\{cardlist[2]}.png')
    Card3_label.config(image = C3_image)
    
    C4_image = resize_cards(f'CARDS\{cardlist[3]}.png')
    Card4_label.config(image = C4_image)
    
    C5_image = resize_cards(f'CARDS\{cardlist[4]}.png')
    Card5_label.config(image = C5_image)
    
    C6_image = resize_cards(f'CARDS\{cardlist[5]}.png')
    Card6_label.config(image = C6_image)
    """
    
    B = Button(root, text ="Hello", command = display_text)
    B.place(x=400, y=200)
    e1 = Entry(root, width= 40)
    e1.pack()
    root.mainloop()

    

p_frame = LabelFrame(frame,text = "player 2" , bd = 0)

p_frame.grid(row = 0 , column = 1 , ipadx = 20)

pl_label = Label(pl_frame , text = '')
pl_label.pack(pady = 20)
pl_image = resize_cards(f'CARDS\{D}.png')
#pl_label.config(image =pl_image)
#another frame 

p_label = Label(p_frame , text = '')
p_label.pack(pady = 20)
p_image = resize_cards(f'CARDS\{F}.png')
#p_label.config(image =p_image)
"""
"""
Card1 = LabelFrame(frame,text = "Card 1" , bd = 0)
Card1.grid(row = 0 , column = 0 , padx = 20 , ipadx = 20)
Card2 = LabelFrame(frame,text = "Card 2" , bd = 0)
Card2.grid(row = 0 , column = 2 , padx = 20 , ipadx = 20)
Card3 = LabelFrame(frame,text = "Card 3" , bd = 0)
Card3.grid(row = 0 , column = 3 , padx = 20 , ipadx = 20)
Card4 = LabelFrame(frame,text = "Card 4" , bd = 0)
Card4.grid(row = 0 , column = 4 , padx = 20 , ipadx = 20)
Card5 = LabelFrame(frame,text = "Card 5" , bd = 0)
Card5.grid(row = 0 , column = 5 , padx = 20 , ipadx = 20)
Card6 = LabelFrame(frame,text = "Card 6" , bd = 0)
Card6.grid(row = 0 , column = 6 , padx = 20 , ipadx = 20)
    
Card1_label = Label(Card1  , text = '')
Card1_label.pack(pady = 20)
Card2_label = Label(Card2  , text = '')
Card2_label.pack(pady = 20)
Card3_label = Label(Card3 , text = '')
Card3_label.pack(pady = 20)
Card4_label = Label(Card4 , text = '')
Card4_label.pack(pady = 20)
Card5_label = Label(Card5 , text = '')
Card5_label.pack(pady = 20)
Card6_label = Label(Card6 , text = '')
Card6_label.pack(pady = 20)
    
C1_image = resize_cards(f'CARDS\{cardlist[0]}.png')
Card1_label.config(image = C1_image)
    
C2_image = resize_cards(f'CARDS\{cardlist[1]}.png')
Card2_label.config(image = C2_image)
    
C3_image = resize_cards(f'CARDS\{cardlist[2]}.png')
Card3_label.config(image = C3_image)
    
C4_image = resize_cards(f'CARDS\{cardlist[3]}.png')
Card4_label.config(image = C4_image)
    
C5_image = resize_cards(f'CARDS\{cardlist[4]}.png')
Card5_label.config(image = C5_image)
    
C6_image = resize_cards(f'CARDS\{cardlist[5]}.png')
Card6_label.config(image = C6_image)
"""
DisplayHand(cardlist)


DisplayHand(cardlist) 



print("ydk fihhh")
print(string)
