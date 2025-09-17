# main() function prompts the user for a filename, and the user enters the name of the file
#after running the modified input.txt displays the context
def main():
    filename = input("Enter the filename to read: ")
    try:
        with open(filename, 'r') as infile:
            content = infile.read()
    except FileNotFoundError:
        print("Error: File not found type the correct nameof the file.")
        return
    except IOError:
        print("Error: Cannot read the file.")
        return

    # Modify the content (example: convert to uppercase)
    modified_content = content.upper()

    # Write to a new file if it fails it prints an error message
    new_filename = "modified_" + "output.txt"
    try:
        with open(new_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"Modified content written to {new_filename}")
    except IOError:
        print("Error: Cannot write to the new file.")

if __name__ == "__main__":
    main()
print("ooooohraaaaay!!!!  input.txt created, processed, and output.txt generated successfully!")


# Error Handling Lab

try:
    # Ask user for a filename
    filename = input("Enter the filename to read: ")

    # Try opening the file
    with open(filename, "r") as file:
        contents = file.read()
        print("\n File content successfully read:\n")
        print(contents)

except FileNotFoundError:
    print("Error: The file does not exist. Please check the name and try again.")
except PermissionError:
    print(" Error: You don't have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
