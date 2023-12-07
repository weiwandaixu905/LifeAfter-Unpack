# Read the original file
file_path = input("请输入txt模版路径：")  # Replace with your file path
with open(file_path, 'r') as file:
    content = file.read()

# Split the content into lines
lines = content.split('\n')

# Create a new list for modified lines
new_lines = []

# Define the ranges for the new prefixes along with the prefix to replace
ranges = [
    ('m_', 1001, 1259),
    ('m_', 2001, 2021),
    ('m_', 3001, 3011),
    ('m_', 4001, 4011),
    ('m_', 5001, 5010),
    ('m_', 6001, 6030),
    ('m_', 8001, 8010),
    ('n_', 1001, 1031),
    ('n_', 3001, 3005),
    ('n_', 4001, 4015),
    ('n_', 5001, 5009)
]

# Iterate through each range
for prefix, start, end in ranges:
    # Replace the original prefix ('m_1006') with the new ones in each range
    for i in range(start, end):
        for line in lines:
            if line.strip():  # Check if the line is not empty
                # Adjusting the replacement logic to accommodate the new prefix
                new_line = line.replace('m_1006', f'{prefix}{i}')
                new_lines.append(new_line)

# Join the new lines into a single string
new_content = '\n'.join(new_lines)

# Define the path for the new file
new_file_path = input("请输入输出文件路径：")  # Replace with your desired file path

# Write the new content into the new file
with open(new_file_path, 'w') as new_file:
    new_file.write(new_content)

print(f"New file created at {new_file_path}")
