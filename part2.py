# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: IIT:20200499 | UoW:w1830218
# Date: 30/04/2021

#Part 2
print("THIS PROGRAM PREDICTS PROGRESSION OUTCOMES FOR EACH ACADEMIC YEAR")
print("Please enter valid inputs to obtain relevant outcomes.\n")
def tot(a,b,c):
    if (a+b+c)==120:
        return True
    else:
        print("Total incorrect. Try again.\n")
        return False
def cred_range(x):
        if x in range(0,121,20):
            return True
        else:
            print("Out of range. Input should be within the range: {0, 20, 40, 60, 80, 100, 120}. Try again.\n")
            return False

while True:
#******************************PASS CREDITS********************************
    try:
        pass_creds=int(input("Please enter your credits at pass: "))
        if cred_range(pass_creds)==False:
            continue
    except ValueError:
        print("Integer required. Try again.\n") 
        continue

#******************************DEFER CREDITS********************************
    try:
        defer_creds=int(input("Please enter your credits at defer: "))
        if cred_range(defer_creds)==False:
            continue
    except ValueError:
        print("Integer required. Try again.\n")
        continue
        
#*******************************FAIL CREDITS*********************************
    try:
        fail_creds=int(input("Please enter your credits at fail: "))
        if cred_range(fail_creds)==False:
            continue
    except ValueError:
        print("Integer required. Try again.\n")
        continue
        
#*****************CHECKING FOR TOTAL*****************************
    if tot(pass_creds,defer_creds,fail_creds)==False:
        continue

#********************PROGRESSION OUTCOMES*************************
    if pass_creds==120:
       print("Progress\n")
                 
    elif pass_creds==100:
        outcome=print("Progress(module trailer)\n")
        
    elif fail_creds>=80:
        outcome=print("Exclude\n")
        
    else:
        outcome=print("Do not progress - module retriever\n")
