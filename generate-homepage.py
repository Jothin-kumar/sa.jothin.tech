new_app = lambda name, url: f'<li><a href="{url}">{name}</a></li>'

apps = [
    {"name": "qw", "url-slug": "qw"}, 
]

with open("index.html", "r") as html_file:
    html_content = html_file.read()
with open("index.html", "w") as html_file:
    html_file.write(html_content.replace("<!-- apps-here -->", "\n".join([new_app(data["name"], "/" + data["url-slug"]) for data in apps])))