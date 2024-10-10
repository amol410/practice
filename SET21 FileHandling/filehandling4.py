# Write a Python program to copy the contents of one text file to another.

# Open the source file in read mode and the destination file in write mode
with open('source.txt', 'r') as source_file:
    with open('destination.txt', 'w') as destination_file:
        # Read the content from the source file and write it to the destination file
        for line in source_file:
            destination_file.write(line)

print("File copied successfully.")
