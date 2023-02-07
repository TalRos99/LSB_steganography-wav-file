# steganography in wav file
I'm using windows 10 and python 3.8

tkinter and cryptography should be installed on your environment. Otherwise install it using pip or on any preprable way.

***The code uses LSB method to hide the data in the file and AES method to encrypt the text***

For start I would say that the length of the text that can be encrypted depends on the wav file that choosed, as a practice you can download free wav sound effects on the following link:
https://mixkit.co/free-sound-effects/

## The GUI
For encrypt/decrypt buttons I used photos to make it look better but of course it's not an issue and you can use default tkinter buttons
you can see it in lines 81-92 in the main file, an example of how to use tkinter buttons you'll find on wav_plot lines 114-120.


![1](https://user-images.githubusercontent.com/89344951/161540214-cd80ef91-de31-4237-91d6-d8ba15ca3180.jpg)

![Screenshot 2022-04-04 145602](https://user-images.githubusercontent.com/89344951/161540281-64aaf9b0-79f2-48f7-a2b6-de6267a04e4e.jpg)


![3](https://user-images.githubusercontent.com/89344951/161540352-7debd812-a254-419d-ac7d-a8bc7863fefe.jpg)

## Encryption
I choose to make a copy for encryption in order to not do any harm to the original file.
In this case, the sound wave represnts by an array (longer file = longer array) and its define from -32767 to 32767

![4](https://user-images.githubusercontent.com/89344951/161542056-697394cd-c0a2-454c-97b8-a037185141cd.jpg)

## Plotting the difference 
*the program will show this plot in any case, wheater the contiue or exit pressed
![5](https://user-images.githubusercontent.com/89344951/161542092-7f700bed-4d65-4bcc-919e-4df300bbd9a4.jpg)

as it seems the difference between the files is so small because we only change the least significant bit

## Decryption
***If you encrypt more then one file and the secret key has changed its harder to decrypt, the solution is to save the secret key and use it on the matching file***

![7](https://user-images.githubusercontent.com/89344951/161544698-635a121b-9c34-4b1e-bff0-fcac298d6586.jpg)

![Screenshot 2022-04-04 150109](https://user-images.githubusercontent.com/89344951/161544726-7c9ec203-c69a-42e3-9770-f4ae579f3e18.jpg)

