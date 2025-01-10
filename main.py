route = "/home/martin/workspace/github.com/Maschart/bookbot/books/frankenstein.txt"

with open(route) as f:
    file_contents = f.read()

print(file_contents)