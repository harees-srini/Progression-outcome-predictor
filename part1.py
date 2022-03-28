# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: IIT:20200499 | UoW:w1830218
# Date: 30/04/2021

#Part 1
print("THIS PROGRAM PREDICTS PROGRESSION OUTCOMES FOR EACH ACADEMIC YEAR")
print("Please enter valid inputs to obtain relevant outcomes.\n")

pass_creds=int(input("Please enter your credits at pass: "))
defer_creds=int(input("Please enter your credits at defer: "))
fail_creds=int(input("Please enter your credits at fail: "))

if pass_creds==120:
    print("Progress")
elif pass_creds==100:
    print("Progress(module trailer)")
elif fail_creds>=80:
    print("Exclude")
else:
    print("Do not progress - module retriever")

