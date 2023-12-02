# Instructions for UpdateCode.py

# This file contains a set of JSON instructions to modify the ListNames.py script.
# There are three operations: INSERT, DELETE, and MODIFY.

# The INSERT operation adds code to print filenames with extensions.
# The DELETE operation removes a specific comment from the script.
# The MODIFY operation changes a specific line in the script.

# Note: It will only apply a change to the first instance of a line if your document has multiple

import json
import os

def find_line_in_file(file_path, line_content):
    with open(file_path, 'r') as file:
        for number, line in enumerate(file, 1):
            if line_content in line:
                return number
    return None

def delete_line_from_file(file_path, line_number):
    if line_number is None:
        return False
    with open(file_path, 'r') as file:
        lines = file.readlines()
    with open(file_path, 'w') as file:
        for i, line in enumerate(lines):
            if i != line_number - 1:
                file.write(line)
    return True

def insert_line_in_file(file_path, line_content, line_number):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    print("\n===== Debug: File Content Before Insertion =====")
    print('\n'.join(line.strip('\n') for line in lines))
    for line in lines:
        print(repr(line))

    if 0 <= line_number - 1 < len(lines):
        lines = lines[:line_number - 1] + [line_content + "\n"] + lines[line_number - 1:]
    else:
        lines.append(line_content + "\n")

    print(f"\nDebug: Number of lines after insertion: {len(lines)}")
    print("\n===== Debug: File Content After Insertion =====")
    print('\n'.join(line.strip('\n') for line in lines))
    for line in lines:
        print(repr(line))

    # Confirmation prompt
    confirm = input("\nDo you want to apply these changes? (Yes/No) [Yes]: ").strip().lower()
    if confirm == '' or confirm == 'yes':
        with open(file_path, 'w') as file:
            file.writelines(lines)
        print("Changes applied successfully.")
    else:
        print("Changes not applied.")

def process_json_instructions(json_data):
    file_path = json_data['file_path']
    find_line = json_data['find_line']
    insert_line = json_data.get('insert_line', '')
    delete_line = json_data.get('delete_line', '')
    modify_line = json_data.get('modify_line', '')

    line_number_to_find = find_line_in_file(file_path, find_line)

    if line_number_to_find is not None:
        print(f"\nProcessing instruction for line: {find_line} at line {line_number_to_find}")

        # Read the file content before changes
        with open(file_path, 'r') as file:
            lines = file.readlines()
        print("\n===== BEFORE Changes =====")
        print(''.join(lines))

        # Apply delete, modify, or insert as needed
        if delete_line:
            lines.pop(line_number_to_find - 1)
        if modify_line:
            lines[line_number_to_find - 1] = modify_line + "\n"
        if insert_line:
            lines.insert(line_number_to_find, insert_line + "\n")

        # Show the file content after changes
        print("\n===== AFTER Changes =====")
        print(''.join(lines))

        # Confirmation prompt
        confirm = input("\nDo you want to apply these changes? (Yes/No) [Yes]: ").strip().lower()
        if confirm == '' or confirm == 'yes':
            with open(file_path, 'w') as file:
                file.writelines(lines)
            print("Changes applied successfully.")
        else:
            print("Changes not applied.")
    else:
        print(f"\nLine to find not found: {find_line}")

if __name__ == "__main__":
    file_path = "instructions.json"
    try:
        with open(file_path, 'r') as file:
            instructions = json.load(file)
        for json_data in instructions:
            process_json_instructions(json_data)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error reading JSON file: {e}")