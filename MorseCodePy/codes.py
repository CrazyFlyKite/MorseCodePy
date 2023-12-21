import json
from os import path

# Get the absolute path of the current module
current_module_path = path.dirname(path.abspath(__file__))

# Construct the paths to the .json files
encodes_file_path = path.join(current_module_path, 'codes', 'encodes.json')
decodes_file_path = path.join(current_module_path, 'codes', 'decodes.json')

# Load the JSON files
with open(encodes_file_path, 'r') as file:
	encodes = json.load(file)

with open(decodes_file_path, 'r') as file:
	decodes = json.load(file)
