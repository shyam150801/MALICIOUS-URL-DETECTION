# Define the path to the input data file
input_file_path = r"D:\sem 5\secure coding\\project\AMEVulDetector-master\AMEVulDetector-master\\graph_feature\\reentrancy\\reentrancy_final_train.txt"

# Define the path to the output cleaned data file
output_file_path = r"D:\sem 5\secure coding\\project\AMEVulDetector-master\AMEVulDetector-master\\graph_feature\\reentrancy\\reentrancy_final_train_clean.txt"

# Initialize an empty list to store cleaned lines of data
cleaned_lines = []

# Open the input file for reading
with open(input_file_path, 'r') as input_file:
    # Iterate through each line in the input file
    for line in input_file:
        # Remove leading and trailing whitespace
        cleaned_line = line.strip()
        
        # Remove commas at the end of numbers (if any)
        cleaned_line = cleaned_line.replace(',', '')
        
        # Append the cleaned line to the list
        cleaned_lines.append(cleaned_line)

# Open the output file for writing
with open(output_file_path, 'w') as output_file:
    # Write the cleaned lines to the output file
    for cleaned_line in cleaned_lines:
        output_file.write(cleaned_line + '\n')

print(f"Data cleaned and saved to {output_file_path}")
