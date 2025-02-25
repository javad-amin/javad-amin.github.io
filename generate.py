import yaml
from jinja2 import Environment, FileSystemLoader

with open("cv_data.yaml", "r") as f:
    cv_data = yaml.safe_load(f)

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("cv_template.html")

rendered_html = template.render(cv=cv_data)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(rendered_html)

print("CV generated as index.html")
