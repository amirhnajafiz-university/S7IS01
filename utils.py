"""
Save content into a file.
"""
def save_into_file(filename, content):
    with open(filename, "a+") as file:
        file.write(content)
