import random as rnd
from tkinter import *
from tkinter import ttk


''' This function determines the winner between two items based on specific rules: 
    "kaghaz" beats "sang", "gheichi" beats "kaghaz", and "sang" beats "gheichi".
    The function returns True if item_2 wins. '''
def which_one(item_1, item_2):
    if item_1 != item_2 : # If the computer and the user have equal choices, no one wins.
        if item_1 == "sang" and item_2 == "gheichi":
            return False
        elif item_1 == "sang" and item_2 == "kaghaz":
            return True
        elif item_1 == "kaghaz" and item_2 == "sang":
            return False
        elif item_1 == "kaghaz" and item_2 == "gheichi":
            return True
        elif item_1 == "gheichi" and item_2 == "kaghaz":
            return False
        else :
            return True

# This function is executed if the paper button is pressed.
def paper():
    global user_selection, pc_selection
    user_selection = 'kaghaz'
    pc_selection = rnd.choice(options)
    control()

# This function is executed if the scissor button is pressed.
def scissor():
    global user_selection, pc_selection
    user_selection = 'gheichi'
    pc_selection = rnd.choice(options)
    control()

# This function is executed if the stone button is pressed.
def stone():
    global user_selection, pc_selection
    user_selection = 'sang'
    pc_selection = rnd.choice(options)
    control()

def control():
    global user_selection, pc_selection, flag, round_counter, pc_wins, user_wins
    flag = which_one(pc_selection, user_selection)
    if flag == True :
        user_wins += 1 # if the function return True, it means the user won
        round_counter += 1
    elif flag == False : # if the function return False, it means the pc won
        pc_wins += 1
        round_counter += 1
    else : # and if the function return nothing it means both of selections are same
        pass
    label_info.config(text= f"امتیاز تو : {user_wins} | امتیاز سیستم : {pc_wins} | دور بازی : {round_counter}")
    label_result.config(text=f"pc selection : {pc_selection}")
    if round_counter >= 3 :
        if user_wins > pc_wins :
            label_result.config(text= f"بردی")
        else :
            label_result.config(text= f"باختی")
        round_counter, pc_wins, user_wins = 0, 0, 0 # start a new game after 3 round game


options = ["sang", "kaghaz", "gheichi"]
pc_selection = ''
user_selection = ''
flag = 'nothing yet'
pc_wins, user_wins = 0, 0
round_counter = 0

root = Tk()
root.title("بازی")
frm = ttk.Frame(root, padding=10)
frm.grid()
label_1 = ttk.Label(frm, text="سنگ ، کاغذ یا قیچی ؟").grid(column=1, row=0)
ttk.Button(frm, text="کاغذ", command=paper).grid(column=1, row=1)
ttk.Button(frm, text="قیچی", command=scissor).grid(column=1, row=2)
ttk.Button(frm, text="سنگ", command=stone).grid(column=1, row=3)
label_info = ttk.Label(frm, text="امتیاز تو : 0 |امتیاز سیستم : 0 | دور بازی : 0")
label_info.grid(column=0, row=4)
label_result = ttk.Label(frm, text=f"pc selection : ")
label_result.grid(column=0, row=2)
ttk.Button(frm, text="پایان", command=root.destroy).grid(column=1, row=5)
root.mainloop()