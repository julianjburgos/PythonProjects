"""
This program is intended as a tracer round for the flow of control as a user
of a social media account makes, deletes, and edits posts. For testing,
a user should be able to enter their user name, change which user name they
are currently using, add a post using their current user name, remove a post
made under their current user name, edit a post made under their current user 
name, print the contents of the list of posts, or quit the program.
"""

#This line of code tells the Python interpreter that it needs to reference the 
#post.py file in order to run the rest of the code in this file.
from CSE_322_post import Post



# What is the user name they want to use?

# Welcome user to the program 

#Store initial user input in a variable identified by user_input
post_list = []
post_index = 0
#You may need to use this statement again to complete the activity.
print("Welcome to Skeleton Social Media!")
user_name = input("What is your username? ")

user_input = input(""" \nWhat would you like to do?
"add" - Add a post to the archive
"remove" - Remove a post from the archive
"change user" - Change the user name associated with any future posts
"print" - Display the current up to date list of all posts
"quit" - End the program

""").lower()




#This while loop ensures that the program will continue executing statements
# at the next indentation level until the user types "quit" in response to the 
# prompt.
while user_input != "quit":

    #code for adding a post here
    if user_input == "add":
        add_input = input("Type what you would like to add: ")
        draftpost = Post(user_name, add_input)
        post_list.append(draftpost)
        post_index += 1
        user_input = input("What would you like to do? ")
        
        #code for removing a post here
    elif user_input == "remove":
        rem_input = int(input("What # post item would you like to remove? "))
        del post_list[rem_input]
        user_input = input("What would you like to do? ")
        
        #code for changing the current user here
    elif user_input == "change user":
        user_name = input("What is your new username? ")
        user_input = input("What would you like to do? ")
        
    #code to display all posts, you can use the code in comments below
    elif user_input == "print":
        post_index = 0
        
        for post in post_list:
            print (post_index, post)
            post_index += 1
        user_input = input("What would you like to do? ")
    #code to inform the user that their input was not valid here
    else:
        user_input = input("What would you like to do? ")
    #Code that will allow the user to make a new selection
    #This code will finish the loop
