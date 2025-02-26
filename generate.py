import argparse

import yaml
from jinja2 import Environment, FileSystemLoader


def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate CV HTML")
    parser.add_argument("--contact", action="store_true")
    return parser.parse_args()


def load_yaml_file(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


def merge_contact_info(cv_data):
    try:
        contact_data = load_yaml_file("contact.yaml")
        return {**cv_data, **contact_data}
    except FileNotFoundError:
        return cv_data


def generate_html(cv_data):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("cv_template.html")
    return template.render(cv=cv_data)


def save_html(html_content, output_file="index.html"):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)


def main():
    args = parse_arguments()
    cv_data = load_yaml_file("cv_data.yaml")

    if args.contact:
        cv_data = merge_contact_info(cv_data)

    html_content = generate_html(cv_data)
    save_html(html_content)


if __name__ == "__main__":
    main()
