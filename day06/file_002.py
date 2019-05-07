file_name = "bok.txt"
content = "Hello, this is python's programming world!"

# file = open(file_name, "w")
file = open(file_name, "a")

file.write(content)

file.close()
