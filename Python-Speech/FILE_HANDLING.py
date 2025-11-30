file = open("test.py")
print(file.read())
file = open("Text2.txt", "x")
file = open("Text.txt", "w")
file.write("This is an example of file creation.")
file.close
file = open("Text.txt", "r")
print(file.read())
file.close
file = open("newText.txt", "a")
file.write("This is an example of file appending.")
file.close