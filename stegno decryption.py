import cv2
import os
import string

# Load the encrypted image
img = cv2.imread("encryptedImage.jpg")  # Replace with the correct image path

# Check if the image was loaded properly
if img is None:
    print("Error: Image not found. Please check the path.")
    exit()

# Input the original message and password (used during encryption)
msg = input("Enter secret message:")  # The same message used for encryption
password = input("Enter passcode used during encryption:")

# Create dictionaries for encoding and decoding characters
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

# Initialize the decrypted message and coordinates
message, n, m, z = "This is a decrypted message", 0, 0, 0

# Input the password for decryption
pas = input("Enter passcode for Decryption: ")

# Check if the password matches and decrypt the message
if password == pas:
    for _ in range(len(msg)):
        message += c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT auth")
