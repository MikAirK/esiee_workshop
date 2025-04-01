"""
print("Hello")
print("")
print("TDB")
"""
#TASK Write an IF ELSE statement to validate if x is larger than y. Return TRUE if YES




def superiorornot ():
    x = int(input("Entre x : "))
    y = int(input("Entre y : "))
    
    
    if x > y :
        return True
    else:
        return False

print(superiorornot())