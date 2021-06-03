name = input("Name: ")
subject = input("Subject: ")

#f strings
story = f"{name}'s fav subject is {subject}"

#%s strings
story = "%s's fav subject is %s. %d" % (name, subject, 10)

print(story)