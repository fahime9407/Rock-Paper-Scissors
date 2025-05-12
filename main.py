import random as rnd
from tkinter import *
from tkinter import ttk


''' This function determines the winner between two items based on specific rules: 
    "kaghaz" beats "sang", "gheichi" beats "kaghaz", and "sang" beats "gheichi".
    The function returns True if item_2 wins. '''
def which_one(item_1, item_2):
    if item_1 != item_2 : # If the computer and the user have equal choices, no one wins.
        if item_1 == "Rock" and item_2 == "Scissors":
            return False
        elif item_1 == "Rock" and item_2 == "Paper":
            return True
        elif item_1 == "Paper" and item_2 == "Rock":
            return False
        elif item_1 == "Paper" and item_2 == "Scissors":
            return True
        elif item_1 == "Scissors" and item_2 == "Paper":
            return False
        else :
            return True

# This function is executed if the paper button is pressed.
def paper():
    global user_selection, pc_selection
    user_selection = 'Paper'
    pc_selection = rnd.choice(options)
    control()

# This function is executed if the scissors button is pressed.
def scissors():
    global user_selection, pc_selection
    user_selection = 'Scissors'
    pc_selection = rnd.choice(options)
    control()

# This function is executed if the Rock button is pressed.
def stone():
    global user_selection, pc_selection
    user_selection = 'Rock'
    pc_selection = rnd.choice(options)
    control()

def control():
    global user_selection, pc_selection, flag, round_counter, pc_score, user_score
    flag = which_one(pc_selection, user_selection)
    if flag == True :
        user_score += 1 # if the function return True, it means the user won
        round_counter += 1
    elif flag == False : # if the function return False, it means the pc won
        pc_score += 1
        round_counter += 1
    else : # and if the function return nothing it means both of selections are same
        pass
    label_info.config(text= f"Round : {round_counter} | Your score : {user_score} | Pc score : {pc_score}")
    label_result.config(text=f"pc selection : {pc_selection}")
    if round_counter >= 5 :
        if user_score > pc_score :
            label_result.config(text= f"You Won.")
        else :
            label_result.config(text= f"You Lost!")
        round_counter, pc_score, user_score = 0, 0, 0 # start a new game after 5 round game


options = ["Rock", "Paper", "Scissors"]
pc_selection, user_selection = '', ''
flag = ''
pc_score, user_score = 0, 0
round_counter = 0

root = Tk()
root.title("play window")
frm = ttk.Frame(root, padding=5) # padding determines the distance betweeen the edges of the frame and the Widgets in the frame
frm.grid()
label_1 = ttk.Label(frm, text= "Rock, Paper or Scissors ?").grid(column=0, row=0)
ttk.Button(frm, text="Paper", command=paper).grid(column=0, row=1)
ttk.Button(frm, text="Scissors", command=scissors).grid(column=0, row=2)
ttk.Button(frm, text="Rock", command=stone).grid(column=0, row=3)
label_info = ttk.Label(frm, text= f"Round : {round_counter} | Your score : {user_score} | Pc score : {pc_score}")
label_info.grid(column=1, row=4)
label_result = ttk.Label(frm, text=f"pc selection : ")
label_result.grid(column=1, row=2)
ttk.Button(frm, text="End", command=root.destroy).grid(column=0, row=5)
root.mainloop()