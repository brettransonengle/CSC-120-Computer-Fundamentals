""" Check even/odd """ 

user_input = input("Input number: ")

# check negative first 
if int(user_input) <  0:
    print("negative number") # if negative output, print "negative number"
# check even 
elif int(user_input) % 2 == 0:
    print("even number") # if even output, print "even number" 
# check odd 
elif int(user_input) % 2 != 0:
    print("odd number") # else print "odd number" 
    
# %% 
""" Print first 20 even numbers """
# initialize variables 
even_number = 0
count_iter = 1

while(count_iter <= 20):
    # add 2 
    even_number = even_number + 2 # add 2 to previous even number
    print(even_number)

    # add to iteration count 
    count_iter = count_iter + 1
    # print(count_iter)
    



