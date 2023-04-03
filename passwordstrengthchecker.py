import re 

def strength(password):

    if len(password) < 8:
        return "Weak: Password is too short"
    
    if not (any(c.isupper() for c in password) and any(c.islower() for c in password)):
        return "Weak: Password should contain both uppercase and lowercase letters."
    
    if not any(c.isdigit() for c in password):
        return "Weak: Password should contain at least one number."
    
    specialchars = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if not specialchars.search(password):
        return "Medium: Password should contain at least one special character (Special characters include: [@_!#$%^&*()<>?/\|}{~:]))"
    
    return "Strong: Password meets all requirements."

while True:
    password = input('Enter your password: ')
    pstrength = strength(password)
    print(pstrength)
    if pstrength == "Strong: Password meets all requirements.":
        break
    else:
        print("Please try again with a stronger password.")