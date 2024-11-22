import json


def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)

def generate_animal_info(data):
    output = ''
    for animal in data:
        if 'name' in animal:
            output += f"Name: {animal['name']}<br>\n"
        if 'characteristics' in animal and 'diet' in animal['characteristics']:
            output += f"Diet: {animal['characteristics']['diet']}<br>\n"
        if 'locations' in animal and animal['locations']:
            output += f"Location: {animal['locations'][0]}<br>\n"
        if 'characteristics' in animal and 'type' in animal['characteristics']:
            output += f"Type: {animal['characteristics']['type']}<br>\n"
        output += "<br>\n"  # Add a blank line between animals
    return output


def update_html_template(template_path, output_path, animals_info):
    with open(template_path, "r") as file:
        html_content = file.read()
    
    updated_content = html_content.replace("__REPLACE_ANIMALS_INFO__", animals_info)
    
    with open(output_path, "w") as file:
        file.write(updated_content)


json_file_path = "animals_data.json"
template_file_path = "animals_template.html"
output_file_path = "animals.html"

animals_data = load_data(json_file_path)

animals_info_string = generate_animal_info(animals_data)

update_html_template(template_file_path, output_file_path, animals_info_string)
