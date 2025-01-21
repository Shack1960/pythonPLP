def modify_file_content(input_filename, output_filename):
    
    try:
        # Open the input file and read its content
        with open(input_filename, 'r') as infile:
            content = infile.readlines()
        
        # Modify the content (e.g., adding line numbers)
        modified_content = [f"{idx + 1}: {line}" for idx, line in enumerate(content)]
        
        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)
        
        print(f"File '{input_filename}' successfully read and modified content written to '{output_filename}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist. Please check the filename and try again.")
    except PermissionError:
        print(f"Error: Permission denied. Unable to read or write to the specified files.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ask the user for input and output filenames
try:
    input_file = input("Enter the name of the file to read from: ")
    output_file = input("Enter the name of the file to write the modified content to: ")
    
    # Call the function to process the files
    modify_file_content(input_file, output_file)
except KeyboardInterrupt:
    print("\nProcess interrupted by the user.")
