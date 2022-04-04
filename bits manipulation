import os.path

import numpy as np
import matplotlib.pyplot as plt
from shutil import copy2
import cv2
from bitarray import bitarray
import struct
import wave

def split_new(word):
    return [char for char in word]

def string_to_binary(text):
    text_str = str(text)
    text_binary = ""
    text_binary += ''.join(format(ord(i), '08b')for i in text_str)

    return text_binary, len(text_binary)


def text_len_encryption(new_sound_wave, text_len):
    text_len_bit = str(format(text_len, '08b'))
    j = len(text_len_bit) - 1
    for i in range(106, 50, -1): #encrypt the len of the text, the max is 9,999,999
        current_bit = format(new_sound_wave[i], '016b')
        if j < 0:
            new_bit = current_bit[:-1] + '0'
            decimal_encrypted = int(new_bit, 2)
            new_sound_wave[i] = decimal_encrypted
        else:
            new_bit = current_bit[:-1] + text_len_bit[j]
            decimal_encrypted = int(new_bit, 2)
            new_sound_wave[i] = decimal_encrypted
            j -= 1
    return new_sound_wave


def encrypt_in_file(file_path: str, recived_text):
    text, text_len = string_to_binary(recived_text)
    if not file_path.endswith('.wav'):
        return None
    obj = wave.open(file_path) # audio source
    channels, get_sample_width, frame_rate, frames, comp_type, comp_name = obj.getparams()
    new_file = wave.open((file_path[:-4] + " encrypted_file.wav"), 'w')
    new_file.setparams((channels, get_sample_width, frame_rate, frames, comp_type, comp_name))

    wav_by_bytes = obj.readframes(-1) # bytes of the source
    data_sound_wave = np.frombuffer(wav_by_bytes, 'int16') # converting bytes to a list of numbers
    new_sound_wave = data_sound_wave.copy()
    bits_str_array = [] # 16bit format for the source file
    obj.close()
    count = 0
    text_len_bit = str(format(text_len, '08b'))
    if len(data_sound_wave) < len(text_len_bit) + len(text):
        # text is too long to encrypt
        print("return")
        return
    new_sound_wave = text_len_encryption(new_sound_wave, text_len)

    j = 0
    for i in range(110, text_len * 10 + 110, 10):  # adding 1 to all LSB of the audio
        if j >= text_len:
            break
        bits_str_array.append(format(new_sound_wave[i], '016b')) #inserting bits to list
        current_bit = format(new_sound_wave[i], '016b')

        if current_bit[-1] != text[j]:
            count += 1
            new_bit = current_bit[:-1] + text[j]
            decimal_encrypted = int(new_bit, 2)
            new_sound_wave[i] = decimal_encrypted
        j += 1
    new_file.writeframesraw(new_sound_wave)

    return data_sound_wave, new_sound_wave


def decrypt_from_file(file_path: str):
    if not file_path.endswith('.wav'):
        return None

    obj = wave.open(file_path) #audio source
    wav_by_bytes = obj.readframes(-1) #bytes of the source
    data_sound_wave = np.frombuffer(wav_by_bytes, 'int16') #converting bytes to a list of numbers
    obj.close()
    text_len = ""
    for i in range(51, 107): #dencrypt the len of the text
        current_bit = format(data_sound_wave[i], '016b')
        text_len += current_bit[-1]
    text_len = int(text_len, 2)

    j = 110 + text_len * 10
    text = ""
    letter = ""
    binary_text = ""
    k = 0
    for i in range(110, j, 10):
        current_bit = format(data_sound_wave[i], '016b')
        p = len(binary_text)
        if p > text_len:
            break
        if k != 8:
            letter += current_bit[-1]
        else:
            binary_text += letter
            char = chr(int(letter, 2))
            k = 0
            text += char
            letter = current_bit[-1]
        k += 1
    return text



