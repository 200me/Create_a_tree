# Output from the left
#for i in range(1, user_input1+1):
    #print("*"*i)
   
#Output from the right
#for i in range(1, user_input1+1):
    #print(" "*(user_input1 - i) + ('*'*i))

#Create a tree
    
user_input1 = int(input("Please enter the number of lines. :"))

for i in range(1, user_input1 +1):
    print(" " *(user_input1 - i) + ('*' * (2*i -1)))

