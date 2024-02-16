from json import load

new_app = lambda name, url: f'<li><a href="{url}">{name}</a></li>'

with open("sa.json") as sa:
    apps = load(sa)

with open("index.html", "r") as html_file:
    html_content = html_file.read()
with open("index.html", "w") as html_file:
    html_file.write(html_content.replace("<!-- apps-here -->", "\n".join([new_app(data["name"], "/" + data["url-slug"]) for data in apps])))