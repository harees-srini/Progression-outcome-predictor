# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: IIT:20200499 | UoW:w1830218
# Date: 30/04/2021

#Part 3
print("THIS PROGRAM PREDICTS PROGRESSION OUTCOMES FOR EACH ACADEMIC YEAR")
print("Please enter valid inputs to obtain relevant outcomes.\n")
cred_range=[0, 20, 40, 60, 80, 100, 120]
student=0
progress=0
trailer=0
exclude=0
retriever=0
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
    if (pass_creds + defer_creds + fail_creds)!=120:
        print("Total incorrect. Try again.\n")
        continue
        
#********************PROGRESSION OUTCOMES*************************
    
    if pass_creds==120:
       print("Progress")
       progress=progress+1
         
            
    elif pass_creds==100:
        outcome=print("Progress(module trailer)")
        trailer=trailer+1
        
    elif fail_creds>=80:
        outcome=print("Exclude")
        exclude=exclude+1
        
    else:
        outcome=print("Do not progress - module retriever")
        retriever=retriever+1
   
    student=student+1
    
    print("\nWould you like to enter another set of data?")
    new_data=(input("Enter 'y' for yes or 'q' to quit and view results: "))

    if new_data.lower()=='y':
        continue
    elif new_data.lower()=='q':
        break
#************************HORIZONTAL HISTOGRAM****************************
print ("\n---------------------------------------------------------\n")
print("Horizontal histogram for", student, "outcomes in total")
print("Progress", progress,":", "*"*progress)
print("Trailer", trailer,":", "*"*trailer)
print("Exclude", exclude,":", "*"*exclude)
print("Retriver", retriever,":", "*"*retriever)

      


    

    



           
           

            
