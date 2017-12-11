#!/usr/bin/env python

from jinja2 import Environment, FileSystemLoader
import json, os, shutil

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(THIS_DIR, 'recipes')
OUTPUT_DIR = os.path.join(THIS_DIR, 'output')

HTML_NAME = 'recipe.html'
PHOTO_NAME = 'photo.jpg'
JSON_NAME = 'recipe.json'

def render_html(input_dir, output_dir, recipe_dir):
    with open(os.path.join(input_dir, JSON_NAME)) as input_data_file:
        input_data = json.load(input_data_file)
        env = Environment(loader=FileSystemLoader(INPUT_DIR), trim_blocks=True, lstrip_blocks=True)
        rendered_html = env.get_template(os.path.join(recipe_dir, HTML_NAME)).render(input_data)
        output_path = os.path.join(output_dir, 'recipe.html')
        with open(output_path, 'w') as output_file:
            output_file.write(rendered_html)

def copy_photo(input_dir, output_dir):
    input_file = os.path.join(input_dir, PHOTO_NAME)
    shutil.copy(input_file, output_dir)

def render_recipes():
    for recipe_dir in os.listdir(INPUT_DIR):
        input_dir = os.path.join(INPUT_DIR, recipe_dir)
        if os.path.isdir(input_dir):
            output_dir = os.path.join(OUTPUT_DIR, recipe_dir)
            os.makedirs(output_dir)
            render_html(input_dir, output_dir, recipe_dir)
            copy_photo(input_dir, output_dir)

if __name__ == '__main__':
    if os.path.isdir(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)
    render_recipes()
