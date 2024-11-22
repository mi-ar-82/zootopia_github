import json

def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)

def serialize_animal(animal_obj):
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'
    output += '  <p class="card__text">\n'
    
    if 'characteristics' in animal_obj:
        if 'diet' in animal_obj['characteristics']:
            output += f'      <strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n'
        if 'locations' in animal_obj and animal_obj['locations']:
            output += f'      <strong>Location:</strong> {", ".join(animal_obj["locations"])}<br/>\n'
        if 'type' in animal_obj['characteristics']:
            output += f'      <strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>\n'
    output += '  </p>\n'
    output += '</li>\n'
    return output

def generate_animal_cards(data):
    output = ''
    for animal_obj in data:
        output += serialize_animal(animal_obj)
    return output

def update_html_template(template_path, output_path, animals_info):
    with open(template_path, "r") as file:
        html_content = file.read()
    updated_content = html_content.replace("__REPLACE_ANIMALS_INFO__", animals_info)
    with open(output_path, "w") as file:
        file.write(updated_content)

def main():
    json_file_path = "animals_data.json"
    template_file_path = "animals_template.html"
    output_file_path = "animals.html"
    
    animals_data = load_data(json_file_path)
    
    animals_info = generate_animal_cards(animals_data)
    
    update_html_template(template_file_path, output_file_path, animals_info)

if __name__ == "__main__":
    main()