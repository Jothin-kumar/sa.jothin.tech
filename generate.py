new_app = lambda name, url: f'<li><a href="{url}">{name}</a></li>'

apps = [
    {"name": "qw", "url": "https://joth.in"}, 
    {"name": "ert", "url": "https://joth.in"}, 
    {"name": "yuiop", "url": "https://joth.in"}, 
    {"name": "as", "url": "https://joth.in"}, 
    {"name": "df", "url": "https://joth.in"}, 
    {"name": "gh", "url": "https://joth.in"}, 
    {"name": "jkl", "url": "https://joth.in"}, 
    {"name": "zxc", "url": "https://joth.in"}, 
    {"name": "vbn", "url": "https://joth.in"}, 
    {"name": "m", "url": "https://joth.in"}, 
]

with open("index.html", "r") as html_file:
    html_content = html_file.read()
with open("index.html", "w") as html_file:
    html_file.write(html_content.replace("<!-- apps-here -->", "\n".join([new_app(data["name"], data["url"]) for data in apps])))