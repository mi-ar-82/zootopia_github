import json


# Loads animal data from a JSON file.
def load_data(filepath):
    """Loads animal data from a JSON file.

    Args:
        filepath (str): The path to the JSON file.

    Returns:
        list: A list of animal dictionaries.
    """
    print(f"Loading animal data from '{filepath}'...")
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        raise
    except json.JSONDecodeError:
        print(f"Error: File '{filepath}' contains invalid JSON.")
        raise


# Serializes an animal object into an HTML list item.
def serialize_animal(animal_obj):
    """Serializes an animal object into an HTML list item.

    Args:
        animal_obj (dict): A dictionary containing the animal's information.
        Expected keys include:
            - 'name' (str): The name of the animal.
            - 'characteristics' (dict, optional):
             A dictionary with keys like 'diet' and 'type'.
            - 'locations' (list, optional): A list of strings
            representing locations where the animal can be found.

    Returns:
        str: An HTML list item representing the animal.
    """
    print(f"Serializing animal: {animal_obj['name']}")
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'
    output += '  <p class="card__text">\n'

    # Serialize characteristics if they exist
    if 'characteristics' in animal_obj:
        if 'diet' in animal_obj['characteristics']:
            output += (f'      <strong>Diet:</strong> '
                       f'{animal_obj["characteristics"]["diet"]}<br>\n')
        if 'type' in animal_obj['characteristics']:
            output += (f'      <strong>Type:</strong> '
                       f'{animal_obj["characteristics"]["type"]}<br>\n')

    # Serialize locations if they exist
    if 'locations' in animal_obj and animal_obj['locations']:
        output += (f'      <strong>Location:</strong> '
                   f'{", ".join(animal_obj["locations"])}<br>\n')

    output += '  </p>\n'
    output += '</li>'
    return output


# Generates HTML code for animal cards.
def generate_animal_cards(data):
    """Generates HTML code for animal cards.

    Args:
        data (dict): A dictionary containing the animal data.

    Returns:
        str: An HTML string containing the animal cards.
    """
    print("Generating animal cards...")
    output = ''
    if data is not None:
        for animal_obj in data:
            output += serialize_animal(animal_obj)
    print("Animal cards generated successfully.")
    return output


# Updates an HTML template file with animal cards.
def update_html_template(
        template_path, output_path, animals_info):
    """Updates an HTML template file with animal cards.

    Args:
        template_path (str): Path to the HTML template file.
        output_path (str): Path for the output HTML file.
        animals_info (str): HTML code for the animal cards.
    """
    print(f"Updating HTML template '{template_path}'...")
    try:
        with open(template_path, "r") as file:
            html_content = file.read()
        updated_content = html_content.replace(
            "__REPLACE_ANIMALS_INFO__", animals_info
        )
        with open(output_path, "w") as file:
            file.write(updated_content)
        print(f"HTML template updated successfully. "
              f"Output written to '{output_path}'.")
    except FileNotFoundError:
        print(f"Error: File '{template_path}' not found.")
        raise


def main():
    json_file_path = "animals_data.json"
    template_file_path = "animals_template.html"
    output_file_path = "animals.html"

    animals_data = load_data(json_file_path)
    print("Loaded animal data:", animals_data)
    animals_info = generate_animal_cards(animals_data)
    print("Generated HTML:", animals_info)
    update_html_template(template_file_path, output_file_path, animals_info)


if __name__ == "__main__":
    main()
