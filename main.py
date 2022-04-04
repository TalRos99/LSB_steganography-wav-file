from wavPlot import *
from tkinter import messagebox
from tkinter import *
from Crypto import *
from shutil import copy2
from bit_manipulation import *


ws = Tk()
ws.title('Encrypt message')
ws.geometry('800x500')
ws.config(bg='#383838')


yy = ""


def read_from_file():
    text_box.delete('1.0', 'end')  # Clear text box
    filetypes = (
        ('WAV files', '*.wav'),
        ('All files', '*.*')
    )

    file_path = filedialog.askopenfilename(title='Open a file',
                                           initialdir='C:\\Users\\Desktop',
                                           filetypes=(
                                               ('WAV files', '*.wav'),
                                               ('All files', '*.*')
                                           ))  # Open file Dialog

    if not file_path:
        return
    decrypt_text = decrypt_from_file(file_path)
    res = bytes(decrypt_text[2:], 'utf-8')  # convert string to bytes
    decrypted = decrypt(res)
    if decrypted is not None:
        decrypt_details(decrypted)
    else:
        messagebox.showinfo('Warning', 'The is no secret message in the file')



def write_to_file():

    if len(text_box.get("1.0", "end")) < 2:
        messagebox.showinfo("Info", "You must type a text in text box")
        return

    file_path = filedialog.askopenfilename(title='Open a file',
                                           filetypes=(
                                               ('WAV files', '*.wav'),
                                               ('All files', '*.*')
                                           ))  # Open file Dialog
    if not file_path:
        return

    generate_key()  # Generate a secret key
    input_text = text_box.get("1.0", "end")  # Get text from textbox, from start to end
    encrypt_message = encrypt(input_text)
    old_wave, new_wave = encrypt_in_file(file_path, encrypt_message)
    original_text_len = int(len(text_box.get("1.0", "end")) - 1)
    encrypted_text_len = len(encrypt_message)

    text_box.delete('1.0', 'end')
    encrypt_details(input_text, original_text_len, old_wave, new_wave, encrypt_message)


# *********** Main GUI section ***************
label = Label(ws, text='Hello and welcome to our \n Encrypt / Decrypt message system to / from wav file')
label.config(bg='#383838', fg='#f1ebeb')
label.place(relx=0.5, y=100, anchor='center')
label.config(font=('Helvatical', 21, "bold"))

img = image_fun.open('encrypt_to_file.png')
resized_img = img.resize((160, 80))
encrypt_button = ImageTk.PhotoImage(resized_img)
B = Button(ws, image=encrypt_button, command=write_to_file, borderwidth=0, bg='#383838')
B.place(relx=0.5, x=-90, y=370, anchor='center')

img2 = image_fun.open('decrypt_from_file.png')
resized_img_2 = img2.resize((160, 80))
decrypt_button = ImageTk.PhotoImage(resized_img_2)
C = Button(ws, image=decrypt_button, command=read_from_file, borderwidth=0, bg='#383838')
C.place(relx=0.5, x=90, y=370, anchor='center')


label = Label(ws, text='Write the text you wish to encrypt in the box and press below \n'
                       'if you wish to decrypt press the button')
label.config(font=('Helvatical', 16), bg='#383838', fg='#f1ebeb')
label.place(relx=0.5, y=180, anchor='center')

img = ImageTk.PhotoImage(file='textbox.jpg')
box = Label(ws, image=img, bg='#383838')
box.place(relx=0.5, y=280, anchor='center')

text_box = Text(ws, height=3, width=60, bg='#383838', bd=3, fg='#f1ebeb', relief='flat', insertbackground='#f1ebeb')
text_box.place(relx=0.5, y=280, anchor='center')
text_box.insert('end', "")
text_box.config(state='normal', font=('Helvatical', 11))
text_box.focus()


# ******************* Menu Bar ***********************************
menu_bar = Menu(ws)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Write encrypt text to wav file", command=write_to_file)
file_menu.add_command(label="Read encrypt text from wav file", command=read_from_file)

file_menu.add_separator()

file_menu.add_command(label="Exit", command=ws.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
edit_menu = Menu(menu_bar, tearoff=0)

ws.config(menu=menu_bar)
# ******************* End Menu Bar ***********************************

ws.mainloop()
