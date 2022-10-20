from tkinter import messagebox
from tkinter import *
import time
import mySQLconnection
import tkinter as tk
import json

# global variables defined here
username = ''
password = ''
email = ''
balance = ''
enterBalance = ''
id = ''
count = 1
# dictionary userInformation initialized here
with open('userInfo.json') as f:
    userInformation = json.loads(f.read())
    print(userInformation)

# create account function will use the user input on create account screen to store account information within the
# dictionary for later recall
def createAccount(username, password, email, balance, loginScreen, createAccountScreen, createUsernameText,
                  createPasswordText, createEmailText, initialDepositText):
    balance = balance
    global count
    if count == 1:
        exit
    else:
        count += 1
    print(count)

    if '$' in balance:
        temp = balance.split("$")
        balance = temp[1]

    if not balance.isnumeric():
        messagebox.showerror('Error', 'Invalid Deposit Value.')
        return

    for i in userInformation:
        print(userInformation[i])
        if username == userInformation[i]['username']:
            messagebox.showinfo('Error', 'Username Taken')
            return
        if email == userInformation[i]['email']:
            messagebox.showinfo('Error', 'Email Already in Use')
            return
    userInformation[count] = {'username': username, 'password': password, 'email': email, 'balance': balance}
    count += 1


    createAccountScreen.forget()
    loginScreen.pack(fill='both', expand=1)
    createUsernameText.delete(0, END)
    createPasswordText.delete(0, END)
    createEmailText.delete(0, END)
    initialDepositText.delete(0, END)
    createUsernameText.insert(0, 'Username')
    createPasswordText.insert(0, 'Password')
    createEmailText.insert(0, 'Email Address')
    initialDepositText.insert(0, '$0')

    print(userInformation)

    a_file = open("userInfo.json", "w")
    json.dump(userInformation, a_file)
    a_file.close()

# login function will use the user data entered in login screen to ensure a valid login was entered, and if so,
# the login screen will be changed to the welcome screen
def login(username, password, loginScreen, welcomeScreen, balanceLabel):
    tempUsername = username
    tempPassword = password
    for key in (userInformation):
        if tempUsername == userInformation[key]["username"] and tempPassword == userInformation[key]["password"]:
            loginScreen.forget()
            welcomeScreen.pack(fill='both', expand=1)
            usernameLabel = Label(welcomeScreen, text=tempUsername, font=('Helvatical bold', 15)).place(relx=0.95,
                                                                                                        rely=0.05,
                                                                                                        anchor=E)
            emailLabel = Label(welcomeScreen, text=userInformation[key]['email'], font=('Helvatical bold', 15)).place(
                relx=0.95,
                rely=0.1, anchor=E)

            balanceLabel.config(text = '$' + userInformation[key]["balance"])
            global id
            id = key
            return

    messagebox.showerror('Error', 'Login Invalid')

def createScreen(screenNumber, loginScreen, createAccountScreen, welcomeScreen, depositScreen, withdrawScreen, helpScreen, thankyouScreen):
    if screenNumber == 0:
        thankyouScreen.forget()
        loginScreen.pack(fill = 'both', expand = 1)
    if screenNumber == 1:
        loginScreen.forget()
        createAccountScreen.pack(fill='both', expand=1)
    elif screenNumber == 2:
        welcomeScreen.forget()
        depositScreen.pack(fill='both', expand=1)
    elif screenNumber == 3:
        depositScreen.forget()
        welcomeScreen.pack(fill='both', expand=1)
    elif screenNumber == 4:
        welcomeScreen.forget()
        withdrawScreen.pack(fill='both', expand=1)
    elif screenNumber == 5:
        withdrawScreen.forget()
        welcomeScreen.pack(fill='both', expand=1)
    elif screenNumber == 6:
        welcomeScreen.forget()
        helpScreen.pack(fill='both', expand=1)
    elif screenNumber == 7:
        helpScreen.forget()
        welcomeScreen.pack(fill='both', expand=1)
    elif screenNumber == 8:
        welcomeScreen.forget()
        thankyouScreen.pack(fill = 'both', expand = 1)
        thankyouLabel = Label(thankyouScreen, text="Thank you!", font=('Helvatical bold', 15)).place(relx=.5, rely=0.4,
                                                                                                     anchor=CENTER)
        BackButton = Button(thankyouScreen, text="Return", height=3, width=10, command=lambda: createScreen(0, loginScreen, createAccountScreen, welcomeScreen, depositScreen, withdrawScreen, helpScreen, thankyouScreen)).place(relx=0.5, rely=.75, anchor=CENTER)




def deposit(userDepValue, welcomeScreen, dCustomEntry, balanceLabel):

    if userDepValue == 0:
        customAmount = dCustomEntry.get()

        if '$' in customAmount:
            temp = customAmount.split("$")
            customAmount = temp[1]

        if not customAmount.isnumeric():
            messagebox.showerror('Error', 'Invalid Deposit Value.')
        intBal = int(userInformation[id]["balance"])
        intBal += int(customAmount)
        stringBal = str(intBal)
    else:
        intBal = int(userInformation[id]["balance"])
        intBal += userDepValue
        print(intBal)
        stringBal = str(intBal)
    userInformation[id]["balance"] = stringBal
    balanceLabel.config(text = '$' + userInformation[id]["balance"])


def withdraw(userWithValue, welcomeScreen, wCustomEntry, balanceLabel):

    if userWithValue == 0:
        customAmount = wCustomEntry.get()

        if '$' in customAmount:
            temp = customAmount.split("$")
            customAmount = temp[1]

        if not customAmount.isnumeric():
            messagebox.showerror('Error', 'Invalid Deposit Value.')
        intBal = int(userInformation[id]["balance"])
        intBal -= int(customAmount)
        if intBal < 0:
            messagebox.showerror('Error', 'Balance will go negative!')
        stringBal = str(intBal)
    else:
        intBal = int(userInformation[id]["balance"])
        intBal -= userWithValue
        print(intBal)
        stringBal = str(intBal)
    userInformation[id]["balance"] = stringBal
    balanceLabel.config(text = '$' + userInformation[id]["balance"])
