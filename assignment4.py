
                      #task1


def read_file(filename):
    """
    Read and display the content of a file, handling errors if file doesn't exist.
    
    Args:
        filename (str): The name of the file to read
    """
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            print("Reading file content:")
            # Read and print each line
            for line_number, line in enumerate(file, 1):
                # Remove trailing newline characters and print
                print(f"Line {line_number}: {line.rstrip()}")
                
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main program
def main():
    filename = "sample.txt"
    read_file(filename)

# Run the program
if __name__ == "__main__":
    main()

                   #task2

def write_to_file(filename, content):
    """
    Write content to a file.
    
    Args:
        filename (str): The name of the file
        content (str): The content to write
    """
    try:
        with open(filename, 'w') as file:
            file.write(content + '\n')
        print("Data successfully written to output.txt.")
    except Exception as e:
        print(f"Error writing to file: {e}")

def append_to_file(filename, content):
    """
    Append content to a file.
    
    Args:
        filename (str): The name of the file
        content (str): The content to append
    """
    try:
        with open(filename, 'a') as file:
            file.write(content + '\n')
        print("Data successfully appended.")
    except Exception as e:
        print(f"Error appending to file: {e}")

def read_file(filename):
    """
    Read and display the content of a file.
    
    Args:
        filename (str): The name of the file to read
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print("\nFinal content of output.txt:")
        print(content, end='')  # end='' to avoid extra newline
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

def main():
    filename = "output.txt"
    
    # Step 1: Write initial content
    initial_text = input("Enter text to write to the file: ")
    write_to_file(filename, initial_text)
    
    # Step 2: Append additional content
    additional_text = input("\nEnter additional text to append: ")
    append_to_file(filename, additional_text)
    
    # Step 3: Read and display final content
    read_file(filename)

# Run the program
if __name__ == "__main__":
    main()