import random

#receiving input from the user
l=int(input("please select the no.of OTP required "))

#creating function def and setting a name to it and addressing a parameter as "length"
def otp_generation(length):
#telling the function to take any number from 0-9 in "numbers" variable
    numbers="0123456789"
#creating a variable inside the functions by "otp" and instructing to combine all the number which are
#are running in random order to form a OTP, and initiating a loop to run the function and instructing
# loop to return the value to "otp"
    otp="".join(random.choice(numbers) for a in range(length))
    return otp
#creating a object to run the program by creating a variable "obj" and address the behaviour "otp_generation" and to
#display the input value by giving "l" to it
obj = otp_generation(l)
print("your final OTP is: ",obj)


