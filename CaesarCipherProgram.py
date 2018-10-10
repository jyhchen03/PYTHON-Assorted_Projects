from easygui import *

#findIndex: finds the index of the first time an element occurs in a list
#arguments: char, a character, and testList, a list
#returns: the index where char occurs in testList
def findIndex(char, testList):
    for letters in range(len(testList)):
        if testList[letters] == char:
            return letters
            
#cEncryptLetter: encrypts a single character (Caesar cipher)
#arguments: refAlphabet, a list of the alphabet; letter, the letter to be encrypted; key, the key.
#returns: the encrypted letter
def cEncryptLetter(refAlphabet, letter, key):
    if letter in refAlphabet:
        singlechar = refAlphabet[(findIndex(letter, refAlphabet)+key)%26]
        return singlechar
    return 
    
#cCipher: encrypts a string with a Caesar (shift) cipher
#arguments: refAlphabet (a list of the alphabet), plaintext (a list) and key (a shift number)
#returns: ciphertext, an encrypted string
def cCipher(refAlphabet, plaintext, key):
    cCiph_text = ""
    for something in plaintext:
        cCiph_text += cEncryptLetter(refAlphabet, something, key)
    return cCiph_text
    
refAlphabet=[
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
'y', 'z'
]

key = int(enterbox("Please enter the key: ", "Encryption Key"))
plaintext = enterbox("Please enter the string to be encrypted: ", "Encryption Text")

ciphertext = cCipher(refAlphabet, plaintext, key)
textbox("This is the encrypted text:", "Encrypted Text", ciphertext)
