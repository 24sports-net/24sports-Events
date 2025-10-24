import json
import os
import sys

SOURCE_FILE = 'match.json'
# UPDATED: Added 'Kabaddi' to the list of categories to process
CATEGORIES = ['Cricket', 'Football', 'Kabaddi'] 
OUTPUT_PREFIX = '24spn-'

def load_json(filename):
    """Loads JSON data from a file."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Source file '{filename}' not found. Exiting.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in '{filename}'. Please check for missing brackets or commas.")
        sys.exit(1)

def save_json(data, filename):
    """Saves data to a JSON file."""
    try:
        with open(filename, 'w') as f:
            # Use 'indent=4' for readable and standard formatting
            json.dump(data, f, indent=4)
        print(f"Successfully saved data to '{filename}'.")
    except Exception as e:
        print(f"Error saving to '{filename}': {e}. Exiting.")
        sys.exit(1)

def process_matches(all_matches):
    """Filters matches and writes to category-specific files."""
    if not isinstance(all_matches, list):
        print(f"Error: '{SOURCE_FILE}' must contain a JSON array (list). Exiting.")
        sys.exit(1)

    for category in CATEGORIES:
        # 1. Filter matches based on the original 'id'
        filtered_matches = [match for match in all_matches if match.get('id') == category]

        # 2. Create the new list with sequential 'id' numbers
        output_list = []
        for index, match in enumerate(filtered_matches):
            new_item = {
                # Assign sequential string ID starting from "1"
                "id": str(index + 1), 
                "title": match.get('title'),
                "link": match.get('link')
            }
            output_list.append(new_item)

        # 3. Save the new file (e.g., 24spn-Football.json)
        output_filename = f"{OUTPUT_PREFIX}{category}.json"
        save_json(output_list, output_filename)

if __name__ == "__main__":
    all_matches = load_json(SOURCE_FILE)
    process_matches(all_matches)
