#==================================================#
#  Just Yuri Mod - Main File
#==================================================#
#  This file is responsible for loading submods in
#  the game/submods folder and providing the
#  documentation for mod developers
#  :D
#==================================================#
init -996 python:
    import json
    import traceback
    import re as regex

    submods = {}
    submods.mods = {}
    submods.mod_count = 0
    submods.mod_icon = Image(os.path.join("images", "default_submod.png"))
    submods.modinfo = """{{
\t\"name\": \"{0}\",
\t\"id\": \"{1}\",
\t\"version\": \"1.0.0\",
\t\"dependencies\": []
}}"""
    #==================================================#
    #  Functions
    #==================================================#
    def parse_mod_id(name):
        match = regex.match("[a-z0-9\\_\\-]*", name.lower().replace(" ", "_"))
        return match.group(0) if match != None else "unknown"
    
    class Submod:
        name = None
        id = None
        version = None
        dependencies = None
        icon = None

        def __init__(self, mod_name, mod_id, mod_version, mod_dependencies, mod_icon):
            self.name = mod_name
            self.id = mod_id
            self.version = mod_version
            self.dependencies = mod_dependencies
            self.icon = mod_icon


    #==================================================#
    #  Start Submod System
    #==================================================#
    print("Checking for submods...")
    if not os.path.isdir(paths.submods[2]):
        print("Creating submods folder...")
        os.mkdir(paths.submods[2])
    else:
        for directory in os.scandir(paths.submods[2]):
            print("Scanning mod: " + directory.name)
            submods.mod_count = submods.mod_count + 1
            submod = Submod(directory.name, parse_mod_id(directory.name), "1.0.0", [], submods.mod_icon)

            mod_docs_dir =  os.path.join(directory.path, "documentation")
            mod_error_path = os.path.join("game", "submods", directory.name)
            mod_info_path = os.path.join(directory.path, "modinfo.json")
            mod_icon_path = os.path.join(directory.path, "icon.png")

            if not os.path.isfile(mod_info_path):
                print("  - Mod " + submod.id + " does not contain a modinfo.json file. Creating new files...")
                if not os.path.isdir(mod_docs_dir):
                    print("  - Creating documentation...")
                    unpack(paths.documentation[0] + "/submods", mod_docs_dir)
                    print("  - Creating modinfo.json...")
                try:
                    with open(mod_info_path, 'w') as file:
                        file.write(submods.modinfo.format(submod.name, submod.id))
                    print("  - Finished!")
                except:
                    print_error("  - Failed to create modinfo.json", path=mod_error_path)

            try:
                with open(mod_info_path) as file:
                    modinfo = json.load(file)
                    submod.name = str(modinfo.get("name", submod.name))
                    submod.id = str(modinfo.get("id", submod.id))
                    submod.version = str(modinfo.get("version", submod.version))
                    submod.dependencies = modinfo.get("dependencies", submod.dependencies)
                    if type(submod.dependencies) == str:
                        submod.dependencies = [submod.dependencies]
                    else:
                        if (str(type(submod.dependencies)) != "<class 'list'>"):
                            submod.dependencies = []
            except:
                print_error("  - Failed to load modinfo.json", path=mod_error_path)

            if os.path.isfile(mod_icon_path):
                print("  - Mod " + submod.id + " has an icon. Loading image...")
                try:
                    submod.icon = Image("submods/" + directory.name + "/icon.png")
                except:
                    print_error("  - Failed to load icon.png", path=mod_error_path)

            renpy.image(submod.id + ":icon", submod.icon)
            submods.mods[submod.id] = submod
            print("  - Mod ID: " + submod.id + ", Version: " + submod.version + os.linesep + "  - Dependencies: " + str(submod.dependencies))
    print("Checking loaded submods for missing dependencies...")

    #TODO: Make sure to check all dependencies first before raising any errors as ideally we want to show all dependencies that are missing.
    for key, submod in submods.mods.items():
        if len(submod.dependencies) > 0:
            for dependency in submod.dependencies:
                if not parse_mod_id(dependency) in submods.mods:
                    try:
                        raise KeyError("Failed to load submods as submod " + submod.id + " is missing dependency " + parse_mod_id(dependency))
                    except:
                        print_error("  - Failed to load submods as submod " + submod.id + " is missing dependency " + parse_mod_id(dependency), path=mod_error_path)
                        raise
    print("Mod loading complete! Loaded " + str(submods.mod_count) + " mod(s)")