from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import wave
from PIL import ImageTk
from PIL import Image as image_fun


def decrypt_details(text):

    def continue_1():
        data.destroy()

    def program_exit():
        data.destroy()
        exit()

    data = Tk()
    data.title('Encrypted data information')
    data.geometry('300x200')
    data.config(bg='#f1ebeb')

    label = Label(data, text="The decrypted text is")
    label.config(bg='#f1ebeb', fg='#378bec', font=('Helvatical', 12, 'bold'))
    label.place(relx=0.5, y=30, anchor='center')


    label = Label(data, text=text)
    label.config(bg='#f1ebeb', fg='black', font=('Helvatical', 10))
    label.place(relx=0.5, y=70, anchor='center')


    data_button = Button(data, height=2, width=8, bg='#378bec', fg='#f1ebeb', text='Continue', command=continue_1)
    data_button2 = Button(data, height=2, width=8, bg='#378bec', fg='#f1ebeb', text="Exit", command=program_exit)
    data_button.place(relx=0.5, x=-50, y=130, anchor='center')
    data_button.config(font=('Helvatical', 10, 'bold'), relief='flat')
    data_button2.place(relx=0.5, x=50, y=130, anchor='center')
    data_button2.config(font=('Helvatical', 10, 'bold'), relief='flat')

    data.mainloop()



def encrypt_details(input_text, original_text_len, old_wave, new_wave, encrypt_message, file_name):


    def plot_and_continue():
        data.destroy()
        plot_the_waves(old_wave, new_wave)


    def plot_exit():
        data.destroy()
        plot_the_waves(old_wave, new_wave)
        exit()

    data = Tk()
    data.title('Encrypted data information')
    data.geometry('800x350')
    data.config(bg='#f1ebeb')


    label = Label(data, text="Your info\n")
    # label.font = ("Arial", 16)
    label.config(bg='#f1ebeb', fg='black', font=('Helvatical', 15, 'bold'))
    label.place(relx=0.5, y=13, anchor='center')
    label.pack(pady=0)


    label = Label(data, text="Your text")
    # label.font = ("Arial", 16)
    label.config(bg='#f1ebeb', fg='#378bec', font=('Helvatical', 12, 'bold'))
    label.place(relx=0.5, y=15, anchor='center')
    label.pack(pady=0)

    label = Label(data, text=input_text[:-1])
    # label.font = ("Arial", 16)
    label.config(bg='#f1ebeb', fg='black', font=('Helvatical', 10))
    label.place(relx=0.5, y=17, anchor='center')
    label.pack(pady=0)

    label = Label(data, text="The len of the text is")
    label.config(bg='#f1ebeb', fg='#378bec', font=('Helvatical', 12, 'bold'))
    label.place(relx=0.5, y=12, anchor='center')
    label.pack(pady=0)

    label = Label(data, text=str(original_text_len))
    label.config(bg='#f1ebeb', fg='black', font=('Helvatical', 10))
    label.place(relx=0.5, anchor='center')
    label.pack(pady=0)

    label = Label(data, text="The encrypted file name:")
    label.config(bg='#f1ebeb', fg='#378bec', font=('Helvatical', 12, 'bold'))
    label.place(relx=0.5, anchor='center')
    label.pack(pady=0)

    label = Label(data, text=file_name + " encrypted_file")
    label.config(bg='#f1ebeb', fg='black', font=('Helvatical', 10))
    label.place(relx=0.5, anchor='center')
    label.pack(pady=0)


    label = Label(data, text="Encrypted text")
    # label.font = ("Arial", 16)
    label.config(bg='#f1ebeb', fg='#378bec', font=('Helvatical', 12, 'bold'))
    label.place(relx=0.5, anchor='center')
    label.pack(pady=0)

    label = Label(data, text=str(encrypt_message)[2:-1])
    label.config(bg='#f1ebeb', fg='black', font=('Helvatical', 10))
    label.place(relx=0.5, anchor='center')
    label.pack(pady=0)

    data_button = Button(data, height=2, width=8, bg='#378bec', fg='#f1ebeb', text="Continue", command=plot_and_continue)
    data_button2 = Button(data, height=2, width=8, bg='#378bec', fg='#f1ebeb', text="Exit", command=plot_exit)
    data_button.place(relx=0.5, x=-50, y=300, anchor='center')
    data_button.config(font=('Helvatical', 10, 'bold'), relief='flat')
    data_button2.place(relx=0.5, x=50, y=300, anchor='center')
    data_button2.config(font=('Helvatical', 10, 'bold'), relief='flat')
    data.mainloop()


def plot_the_waves(old_wave, new_wave):

    plt.figure()
    axis = plt.subplot(222)
    plt.plot(new_wave, color='springgreen')
    plt.title('Embedded wave form')
    plt.subplot(221, sharex=axis, sharey=axis)
    plt.plot(old_wave, color='cadetblue')
    plt.title('Original wave form')

    plt.subplot(223, sharex=axis, sharey=axis)
    plt.plot(new_wave, color='black')
    plt.plot(old_wave, color='white')
    plt.title('Represents the difference after using stenography')

    plt.show()
