import os

# Get the current working directory
cwd = os.getcwd()
print("Current directory:", cwd)

# Check if the XML files exist in the expected directory
xml_dir = os.path.join(cwd, '')
print("XML files directory:", xml_dir)
print("Files in the directory:", os.listdir(xml_dir))
