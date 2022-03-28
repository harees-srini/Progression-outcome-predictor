# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: IIT:20200499 | UoW:w1830218
# Date: 30/04/2021

#Part 5
print("THIS PROGRAM PREDICTS PROGRESSION OUTCOMES FOR EACH ACADEMIC YEAR\n")
pass_creds=[120,100,100,80,60,40,20,20,20,0]
defer_creds=[0,20,0,20,40,40,40,30,0,0]
fail_creds=[0,0,20,20,20,40,60,80,100,120]
progress=0
trailer=0
exclude=0
retriever=0
student=0

def outcome():
    global progress
    global trailer
    global exclude
    global retriever
    global student
    if pass_creds[x]==120:
        print("Progress")
        progress=progress+1
        student=student+1
    elif pass_creds[x]==100:
        print("Progress(module trailer)")
        trailer=trailer+1
        student=student+1
    elif fail_creds[x]>=80:
        print("Exclude")
        exclude=exclude+1
        student=student+1
    else:
        print("Do not progress - module retriever")
        retriever=retriever+1
        student=student+1

for x in range(0,10):
    outcome()

#*********************HORIZONTAL HISTOGRAM*******************************
print("\n-------------------------------------------------------\n")
print("Horizontal histogram for", student, "outcomes in total")
print("Progress", progress,":", "*"*progress)
print("Trailer", trailer,":", "*"*trailer)
print("Exclude", exclude,":", "*"*exclude)
print("Retriever", retriever,":", "*"*retriever)

      


    

    



           
           

            
