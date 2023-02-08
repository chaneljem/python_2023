# Defining and Using Python Functions
# 1 Write a 'split_name' function that takes a string and returns a dictionary with first_name and last_name

def split_name(name):
    first_name, last_name = name.split(maxsplit=1)
    return {
        'first_name': first_name,
        'last_name': last_name,
    }
assert split_name("Beyoncé Knowles") == {
    "first_name": "Beyoncé",
    "last_name": "Knowles",
    
}

# 2 Ensure that 'split_name' can handle multi-word last names

assert split_name("Beyoncé Knowles Carter") == {
    "first_name": "Beyoncé",
    "last_name": "Knowles Carter",
}

# 3 Write an 'is_palindrome' function to check if a string is a palindrome (reads the same from left-to-right)
def is_palindrome(item):
    item = str(item)
    return item == item[::-1]
    
assert is_palindrome("radar") == True
assert is_palindrome("stop") == False

# 4 Make 'is_palindrome' work with numbers

assert is_palindrome(101) == True
assert is_palindrome(10) == False

# 5 Write a 'build_list' function that takes an item and a number to include in a list
def build_list(item, count=1):
    items = []
    for _ in range(count):
        items.append(item)
    return items
    
assert build_list("Apple", 3) == [
    "Apple",
    "Apple",
    "Apple",
]
    
assert build_list("Orange") == [
    "Orange"
]