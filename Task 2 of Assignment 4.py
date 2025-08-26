# Task 2: Write and Append Data to a File

# Step 1: Take user input and write it to output.txt
writing = input("Enter text to write to the file: ")
file = open('output.txt','w')
writing_file = file.write(writing + "\n")
print("Data successfully written to output.txt.")
file.close()

# Step 2: Append additional text
appending = input("\nEnter additional text to append: ")
file = open('output.txt','a')
appending_file = file.write(appending + "\n")
print("Data successfully appended.")
file.close()

# Step 3: Read and display final content of the file
print("\nFinal content of output.txt:")
file = open('output.txt','r')
final_content = file.read()
print(final_content)