# This a tell me a story application

'''
This is a python program that gives the user an option to select a story they want to read and
displays that story
'''

print("Please choose a story you would love to read\n")
print("Option 1: The Princess and the Pea \n Option 2: The Princess and the Frog\n\n")

select_story = int(input("Enter the number 1 for Option 1 and 2 for Option 2: "))


if select_story == 1:
    print("The princess went to sleep and put many mattresses but still felt discomfort all because there was a pea.")
    print("Moral of the story is that sometimes the things that cause us discomfort are not that big")
elif select_story == 2:
    print("The princess met a frog and gave him a kiss, he then transformed into a handsome Prince")
else:
    print("Invalid Option Selected")





# Code by Tatenda Mapfumo