import random
import csv

#Got this box code from ChatGPT, thank you AI. Builds a nice UI for the output
def create_box(*args):
    header = "Created DND NPC - 5e, 2024"  # Default header
    longest = max(len(str(arg)) for arg in (header,) + args)  # Find longest string
    width = longest + 4  # Adjust for padding
    top_bottom = "|" + "-" * (width - 2) + "|"
    header_line = f"| {header.ljust(longest)} |"
    separator = "|" + "-" * (width - 2) + "|"

    print(top_bottom)
    print(header_line)
    print(separator)  # Separator line after header
    for arg in args:
        print(f"| {str(arg).ljust(longest)} |")  # Left-align text for uniform width
    print(top_bottom)

#creates the gender for the NPC
gender = ['F', 'M']
gender = random.choice(gender)
gender_output = "Gender: " + gender

#creates the age for the NPC
age = list(range(18,70))
age = random.choice(age)
age = "Age: " + str(age)

#source for first names: https://momlovesbest.com/medieval-names
#source for last names: https://momlovesbest.com/medieval-last-names

first_name = []
last_name = []
male_names_file = "male_names.csv"
female_names_file = "female_names.csv"
last_names_file = "last_names.csv"

#getting and creating first name based on gender
if gender == "F":
    with open(female_names_file, newline="", encoding="utf-8") as names:
        reader = csv.reader(names)
        first_name = list(reader)
else:
    with open(male_names_file, newline="", encoding="utf-8") as names1:
        reader1 = csv.reader(names1)
        first_name = list(reader1)

first_name = random.choice(first_name)
#strips [''] from name from list
first_name = first_name[0]
first_name_output = "First Name: " + str(first_name)

#getting and creating last name
with open(last_names_file, newline="", encoding="utf-8") as names2:
    reader2 = csv.reader(names2)
    last_name = list(reader2)

last_name = random.choice(last_name)
last_name = last_name[0]
last_name_output = "Last Name: " + str(last_name)

#source for species (races): https://dungeonmister.com/guides/races-and-species-in-dnd-2024/
species_list = "species.csv"

with open(species_list, newline="", encoding="utf-8") as species1:
    reader3 = csv.reader(species1)
    species = list(reader3)

species = random.choice(species)
species = species[0]
species_output = "Species(race): " + str(species)

#creating the character's class
#source: https://www.dndbeyond.com/classes
classes_list = "classes.csv"

with open(classes_list, newline="", encoding="utf-8") as class_:
    reader4 = csv.reader(class_)
    classes = list(reader4)

classes = random.choice(classes)
classes = classes[0]
classes_output = "Class: " + str(classes)

#creating the character's background
#source: https://www.dndbeyond.com/backgrounds
background_list = "background.csv"

with open(background_list, newline="", encoding="utf-8") as background_:
    reader5 = csv.reader(background_)
    background = list(reader5)

background = random.choice(background)
background = background[0]
background_output = "Background: " + str(background)

#creating morality alignment
#Source: https://en.wikipedia.org/wiki/Alignment_(Dungeons_%26_Dragons)
morality_list = "morality_alignment.csv"
with open(morality_list, newline="", encoding="utf-8") as morality_:
    reader6 = csv.reader(morality_)
    morality = list(reader6)

morality = random.choice(morality)
morality = morality[0]
morality_output = "Morality Alignment: " + str(morality)

#creating character trope for npc
#source: https://thescriptlab.com/blogs/40182-101-character-tropes/
tropes_list = "character_tropes.csv"
with open(tropes_list, newline="", encoding="utf-8") as tropes_:
    reader7 = csv.reader(tropes_)
    character_trope = list(reader7)

character_trope = random.choice(character_trope)
character_trope = character_trope[0]
character_trope_output = "Character Trope: " + str(character_trope)

#body description
#source: https://gracedgirl.com/physical-descriptions/
body_description_list = "body_description.csv"
with open(body_description_list, newline="", encoding="utf-8") as descriptions_:
    reader8 = csv.reader(descriptions_)
    body_description = list(reader8)

body_description = random.choice(body_description)
body_description = body_description[0]
body_description_output = "Body Description: " + str(body_description)

#calls function to print character
create_box(age,gender_output,first_name_output, last_name_output, species_output, classes_output, background_output, morality_output, character_trope_output, body_description_output)
