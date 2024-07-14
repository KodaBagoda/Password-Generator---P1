import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
  letters = string.ascii_letters
  digits = string.digits
  special = string.punctuation

characters = letters
if numbers:
  characters += digits
elif special_characters:
  characters += special

pwd = ""
meets_criteria = False
has_Number = False
has_Special = False

while not meets_criteria or len(pwd) < min_length:
  new_char = random.choice(characters)
  pwd += new_char
  if new_char in digits:
    has_number = True
  elif new_char in special:
    has_special = True
    
