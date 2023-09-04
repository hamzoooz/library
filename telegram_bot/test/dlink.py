import re

def convert_ids_to_links(file_path):
    with open('ids1.txt', 'r') as file:
        content = file.read()
        ids = re.findall(r'@(\w+)', content)  # Extract all usernames starting with '@'
        
        for id in ids:
            link = f'https://t.me/{id}'  # Construct the direct link
            content = content.replace(f'@{id}', link)  # Replace the ID with the link
        
    with open('output.txt', 'w') as output_file:  # Write the converted content to a new file
        output_file.write(content)

# Usage example
# convert_ids_to_links('input.txt')
# ```

# Make sure to replace `'input.txt'` with the path to your input text file. The converted content will be written to a new file named `'output.txt'`. You can then use this output file on your website.