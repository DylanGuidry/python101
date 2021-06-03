#Ask for name
user_name = input("Hi there! Let's start off if your name.")

#Greet user
print("Nice to meet you " + user_name + "! ")

#Check if name is longer than 10 or not as long as 10
if len(user_name) > 10:
    print("How that's is one long name!" )
elif len(user_name) == 5:
    print("You are an amazing person.")
else:
    print("That's a boring name.")


print("Get lost.")