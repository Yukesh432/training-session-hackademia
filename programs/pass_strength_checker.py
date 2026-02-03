# Rules:
"""
Rules:
1. Count uppercase, lowercase, digits
 
- Strong: atleast 1 uppercase, 1 lowercase, 1 digit, and length >= 8
- moderate: length>=6
- weak: otherwise

"""

password= input("Enter password: ")

#counter variables
has_upper= 0
has_lower=0
has_digit=0

for character in password:
    # print(character)
    if character.isupper():
        has_upper= has_upper+1
    elif character.islower():
        has_lower+=1
    elif character.isdigit():
        has_digit+=1
    else:
        pass

length= len(password)

if length>=8 and has_upper and has_lower and has_digit:
    strength= "Strong"
elif length>=6:
    strength= "Moderate"
else:
    strength= "Weak"

print("Password STRENGTH: ", strength)

# info of password
print(f"Length: {length}, Uppercase: {has_upper}, Lowercase: {has_lower}, Digits: {has_digit}")

