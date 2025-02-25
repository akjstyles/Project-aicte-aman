import cv2
import os
import string

# Load the image
img = cv2.imread("mypic.jpg")  # Replace with the correct image path

# Input the secret message and password
msg = input("Enter secret message:")
password = input("Enter a passcode:")

# Create dictionaries for encoding and decoding characters
d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

# Initialize coordinates
m = 0
n = 0
z = 0

# Encode the message into the image
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

# Save the encrypted image
cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Use 'start' to open the image on Windows
