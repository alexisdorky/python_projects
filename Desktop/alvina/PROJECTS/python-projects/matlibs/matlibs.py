import random

with open("stories.txt", "r") as file:
    stories = file.readlines()

selected_story = random.choice(stories).strip()


print("Let's play Matlip! Fill in the blanks below:\n")

noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
noun3 = input("Enter one more noun: ")

verb1 = input("Enter a verb: ")
verb2 = input("Enter another verb: ")
verb3 = input("Enter one more verb: ")

adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
adjective3 = input("Enter one more adjective: ")

famous_person = input("Enter the name of a famous person: ")
place = input("Enter a place: ")


final_story= selected_story.format(
    noun1=noun1,
    noun2=noun2,
    noun3=noun3,
    verb1=verb1,
    verb2=verb2,
    verb3=verb3,
    adjective1=adjective1,
    adjective2=adjective2,
    adjective3=adjective3,
    place=place,
    famous_person=famous_person)
print(final_story)