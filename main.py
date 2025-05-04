import random as rnd
from tkinter import *
from tkinter import ttk


''' This function determines the winner between two items based on specific rules: 
    "kaghaz" beats "sang", "gheichi" beats "kaghaz", and "sang" beats "gheichi".
    The function returns True if item_1 wins. '''
def which_one(item_1, item_2):
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
    global user_selection, pc_selection, flag, round_counter
    user_selection = 'kaghaz'
    flag = which_one(pc_selection, user_selection)

# This function is executed if the scissor button is pressed.
def scissor():
    global user_selection, pc_selection, flag, round_counter
    user_selection = 'gheichi'
    flag = which_one(pc_selection, user_selection)

# This function is executed if the stone button is pressed.
def stone():
    global user_selection, pc_selection, flag, round_counter
    user_selection = 'sang'
    flag = which_one(pc_selection, user_selection)

# The next two lines of code randomly selects an item from the list ["sang", "kaghaz", "gheichi"].
options = ["sang", "kaghaz", "gheichi"]
pc_selection = rnd.choice(options)
user_selection = ''
flag = False
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
label_result = ttk.Label(frm, text="result : ")
label_result.grid(column=0, row=4)

# The game is played in three rounds.
for i in range(3):
    # If the user's selection is not in options, it repeatedly asks for a valid selection until a correct one is provided.
    user_selection = input("sang, kaghaz or gheichi ? ")
    while user_selection not in options :
        print("invalid selection!")
        user_selection = input("enter your selection : ")
    if pc_selection != user_selection: # If the computer and the user have equal choices, no one wins.
        flag = which_one(pc_selection, user_selection)
        if flag:
            user_wins += 1 # if the function return True, one is added to the user's points.
            print (f"pc selection : {pc_selection}, result : user ")
        else: # Otherwise one is added to the computer's points.
            pc_wins += 1
            print (f"pc selection : {pc_selection}, result : computer ")

# At the end, whoever has the most points wins.
if user_wins > pc_wins :
    print("you won!")
else :
    print("you failed!")
