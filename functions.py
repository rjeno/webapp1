FILEPATH = r"TODOMAIN.txt"


# function makes function call
# todos variable is only valid/usable inside the function.
# coffe shop gives you the coffee, not the ingredients
def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    # print(help(get_todos)) ^^
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

# local variables, not global
# must respect order of filepath
def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# no need for breaklines or extra code. This is good for multiline txt, strs.

#text = """
#Principles of productivity:
#Managing your inflow.
#Systemizing everything that repeats.
#"""

#print(text)

# variable hidden in Python.. __name__ = __main__

if __name__ == "__main__":

    print("Hello")
    print(get_todos())