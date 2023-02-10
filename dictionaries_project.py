# Define the Variables to be used in the script
import os
path = os.getcwd()
print(os.getcwd())

the_files = (os.listdir(path))

# Create an empty list
dict_list = []

# Create for loop to repeat script actions
for file in the_files:
    files_dict = {} # creates an empty dictionary
    files_dict['file_name'] = os.path.realpath(path)
    files_dict['file_size'] = os.path.getsize(path)
    
# Append the dictonary to the List
dict_list.append(files_dict)

# Print list of items in the dictionary
print(files_dict)