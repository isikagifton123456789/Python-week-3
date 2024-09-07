# File Handling Assignment

# File Creation and Writing
try:
    # Create a new text file in write mode and write three lines
    with open("my_file.txt", "w") as file:
        file.write("This is line 1.\n")
        file.write("123 - This is line 2.\n")
        file.write("The quick brown fox jumps over 456 lazy dogs.\n")
    print("File created and content written successfully.")

    # File Reading and Display
    with open("my_file.txt", "r") as file:
        print("\nReading the contents of my_file.txt:")
        content = file.read()
        print(content)

    # File Appending
    with open("my_file.txt", "a") as file:
        file.write("Appended line 1.\n")
        file.write("789 - Appended line 2.\n")
        file.write("Appending is fun with Python.\n")
    print("Additional content appended successfully.")

    # Read the file again to confirm appending
    with open("my_file.txt", "r") as file:
        print("\nReading the updated contents of my_file.txt:")
        updated_content = file.read()
        print(updated_content)

except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You don't have permission to access the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File handling operations completed.")
