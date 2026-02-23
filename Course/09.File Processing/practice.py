
from pathlib import Path

UNIT_DIR = Path(__file__).parent
DATA_DIR = UNIT_DIR / "data"
TEXT_PATH = DATA_DIR / "text.txt"

# we need to read data from a text file and store it in a variable
# we need to loop through the text files text, and count how many times each letter appear.
# we need to check if the letter exists as a key in the dictionary , if it does, add one to the key
# if it doesnt , assign value to 1 by ex, mydictionary["b"]=1

with open(TEXT_PATH, "r" ) as f:
    file_text= f.read().lower().replace(" ","").replace("\n","")
    print(file_text)
    
alphabet_dict = {
    "a":0,
    "b":0,
}

for letter in file_text:
    if letter.isalpha():
        if letter in alphabet_dict:
            alphabet_dict[letter]+=1
            print(alphabet_dict[letter]) 
        else:
            alphabet_dict[letter]=1
            print(alphabet_dict[letter])    
print(alphabet_dict)