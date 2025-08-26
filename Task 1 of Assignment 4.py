# Task 1: Read a File and Handle Errors

print("(This input is used to test how the error handler works. If you type ‘no’, the error handler will be activated.)")
choice = input("Do you want to create 'sample.txt'? (yes/no):").strip().lower()

if choice == "yes":

    # Step 1: Create the sample file
    with open('sample.txt', 'w') as file:
        file.write("Line 1: This is a sample text file.\n")
        file.write("Line 2: It contains multiple lines.\n")

elif choice == "no":

    # Instead of os.remove, empty the file by overwriting with nothing
    try:
        with open("sample.txt", "w") as file:
            pass
    except FileNotFoundError:
        print("'sample.txt' does not exist, so error handler will be tested.")

else:
    print()
    print("(Invalid input! please write 'yes/no' only)")
    exit()   # Stop further execution if input is invalid

# Step 2: Try reading the file and handle errors
try:
    with open("sample.txt", "r") as file:
        reading_file = file.read()
        if reading_file.strip() == "":
            raise FileNotFoundError   # Treat empty file as "not found"
        print()
        print(reading_file)

except FileNotFoundError:
    print()
    print("Error: The file 'sample.txt' was not found.")

except Exception as e:
    print()
    print(f"An unexpected error occurred: {e}")

