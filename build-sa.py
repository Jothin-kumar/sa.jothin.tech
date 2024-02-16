import json, os, shutil

with open("sa.json") as sa:
    datas = json.loads(sa.read())
if os.path.exists("__cloned__"):
    shutil.rmtree("__cloned__")

for data in datas:
    cloned_path = f"__cloned__/{data["url-slug"]}"
    os.system(f"git clone {data["repo"]} {cloned_path}")
    build_data = {
        "parent-dir": cloned_path,
        "line-end": "\n",
        "vars": [],
        "pages": ["/index.html"]
    }
    build_config_path = f"{cloned_path}/build-config.json"
    if os.path.exists(build_config_path):
        with open(build_config_path) as bc:
            new_data = json.loads(bc.read())
        build_data["line-end"] = new_data["line-end"]
        build_data["vars"] = new_data["vars"]
        build_data["pages"] = new_data["pages"]
    with open("build-config.json", "w") as bc:
        json.dump(build_data, bc)
    os.system(f"python3 build/build.py && cp -r build-output {data["url-slug"]}")
    print(f"{data["name"]} done")
