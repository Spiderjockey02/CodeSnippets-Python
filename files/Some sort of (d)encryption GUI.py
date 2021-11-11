##--Imports--#
import time
import random
import tkinter

##--Random number generator--##
Key = 8
window = tkinter.Tk()
print("Th key is:", Key)

        ##--Functions--##
##-Opening encoding window
def Encoding_msg():
    msg = Ent.get()
    if len(msg) != 0:
        print("Creating encryption.")
        print("=-=-=-=-=-=-=-=-=-=-=-==-=-=")
        time.sleep(.500)
        print("Encryption complete...")
        Encryption()
    else:
        print("Please enter a message to encrypt.")
##-Opening decoding window
def Decoding_msg():
    msg = Ent.get()
    if len(msg) != 0:
        print("Decoding message")
        time.sleep(.500)
        Decryption()
    else:
        print("Please enter a message to decrypt.")

##--Encryption and Decryption--##
def Encryption():
    msg = Ent.get()
    result = ''
    for i in range(0,len(msg)):
        result = result + chr(ord(msg[i]) - Key)
    print("Encryped message: " + result)
    
def Decryption():
    msg = Ent.get()
    result = ''
    for i in range(0,len(msg)):
        result = result + chr(ord(msg[i]) + Key)
    print("decrypted message: " + result)

    ##--Windows--##
##-Program has opened Encryption window    
def EncryptionOpened():
    global Ent
    print('Encryption has opened.')
    print("=-=-=-=-=-=-=-=-=-=-=-==-=-=")
    window.geometry("220x220")
    window.title("Encryption Page")
    label4 = tkinter.Label(window, text="Welcome to the CodeBreaker 1.01V", bg = "#15EAD6",)
    label5 = tkinter.Label(window, text="-------------------------------------", bg = "#15EAD6")
    Ent = tkinter.Entry(window, text="")
    button3 = tkinter.Button(window, text="1 - Encode a message", command = Encoding_msg)
    button4 = tkinter.Button(window, text="2 - Decode a message", command = Decoding_msg)
    ##-Packs and widgets-##
    label4.pack()
    label5.pack()
    Ent.pack()
    button3.pack()
    button4.pack()
##-Has opened Encryption Window
def OpenEncryption():
    print("Opening encryption....")
    print("=-=-=-=-=-=-=-=-=-=-=-==-=-=")
    try:
        label1.destroy()
        label2.destroy()
        label3.destroy()
        button1.destroy()
        label4.destroy()
        button1.destroy()
        EncryptionOpened()
    except:
        print("yeet")
    
def start():
    global label1, label2, label3, label4, button1, button2
    ##--GUI--##
    window.geometry("420x300")
    window.title("Home page")
    window.configure(background="#15EAD6")
    window.resizable(0,0)
    ##-Labels and stuff
    label1 = tkinter.Label(window, text="Welcome to the main Page", bg = "#15EAD6", font=("Ariel", 20))
    label2 = tkinter.Label(window, text="-------------------------------------", bg = "#15EAD6")
    label3 = tkinter.Label(window, text="Please choose an option", bg = "#15EAD6", font=("Ariel", 10))
    button1 = tkinter.Button(window, text="Encryption", command=OpenEncryption)
    label4 = tkinter.Label(window, text="", bg = "#15EAD6", font=("Ariel", 5))
    button2 = tkinter.Button(window, text="Decryption")
    ##--Packs and widgets--##
    label1.pack()
    label2.pack()
    label3.pack()
    button1.pack()
    label4.pack()
    button2.pack()
    window.mainloop()

start()
