import re
from pyfiglet import figlet_format

"""
    Verify the strength of 'password'
    Returns a dict indicating the wrong criteria
    A password is considered strong if:
        8 characters length or more
        1 digit or more
        1 symbol or more
        1 uppercase letter or more
        1 lowercase letter or more
        1 space or more
        
    """
    
def pwdchecker(pwd) :
    
    #Length test
    length_error = len(pwd) < 8
    
    #Digit test
    digit_error = re.search(r"[0-9]", pwd) is None
    
    #Symbol test
    symbol_error = re.search(r"\W", pwd) is None
    
    #Uppercase test
    uppercase_error = re.search(r"[A-Z]", pwd) is None
    
    #Lowercase test
    lowercase_error = re.search(r"[a-z]", pwd) is None
    
    #Space test
    space_error = re.search(r" ", pwd) is None
    
    pwd_strong = not (length_error or digit_error or symbol_error or uppercase_error or lowercase_error or space_error)
        
    results = {
            "pwd_strong" : pwd_strong, 
            "Length is less than 8 characters" : length_error, 
            "Doesn't contain number" : digit_error, 
            "Doesn't contain symbol" : symbol_error, 
            "Doesn't contain uppercase character" : uppercase_error, 
            "Doesn't contain lowercase character" : lowercase_error, 
            "Doesn't contain space" : space_error,
        }
    
    print(figlet_format(pwd))
    
    if results["pwd_strong"] :
        print("Password is strong! Congrats.")
    else:
        print("Password is not strong! Try again...")
    print()  
    
    print("Because : ")
    
    for key,val in results.items() :
        if results[key] :
            print(key)
        
    print("-"*10)
    print()


''' '''


pwd = input("What is the password you want to check? ")
pwdchecker(pwd)
