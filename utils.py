"""
Save content into a file.
"""
def save_into_file(filename, content):
    with open(filename, "w+") as file:
        file.write(content)
