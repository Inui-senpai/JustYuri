#==================================================#
#  Just Yuri Mod - Main File
#==================================================#
#  This file is ran second and is responsible for
#  loading submods in the game/submods folder
#  
#  :D
#==================================================#


init -999 python:
    import json
    import traceback
    import re as regex

    submods = {}
    submods.mods = {}
    submods.folder = os.path.join(config.basedir, "game", "submods")
    submods.mod_count = 0
    submods.help = {}
    submods.help.getting_started = """Welcome to the submodding community!


If you ever need to regenerate these docs, delete the modinfo.json file and reboot the game. Have fun!
"""
    submods.help.modinfo = """{{
\t####################################################################################
\t# This is what the Just Yuri mod reads to figure out what this submod is.          #
\t# This is always automatically generated when a modinfo.json file is not detected. #
\t####################################################################################

\t# The name of your submod. This will show up in game in the mods menu.
\t\"name\": \"{0}\",

\t# The unique id of your submod. This is used in the dependencies blocks of other mods.
\t\"id\": \"{1}\",

\t# The version of your submod. This can be anything you want, but keep it close to the format #.#.#
\t\"version\": \"1.0.0\",

\t# The unique ids of each submod that this submod requires.
\t# If any id is present here and the mod isn't loaded, the game will crash and display any mods that are missing
\t# Also supports putting a single string as well if you don't want to use a list
\t\"dependencies\": []
}}"""
    submods.modinfo = """{{
\t\"name\": \"{0}\",
\t\"id\": \"{1}\",
\t\"version\": \"1.0.0\",
\t\"dependencies\": []
}}"""

    def parse_mod_id(name):
        match = regex.match("[a-z0-9\\_\\-]*", name.lower().replace(" ", "_"))
        return match.group(0) if match != None else "unknown"

    print("Checking for submods...")
    if not os.path.isdir(submods.folder):
        print("Creating submods folder...")
        os.mkdir(submods.folder)
    else:
        for directory in os.scandir(submods.folder):
            print("Scanning mod: " + directory.name)
            submods.mod_count = submods.mod_count + 1
            mod_name = directory.name
            mod_id = parse_mod_id(directory.name)
            mod_version = "1.0.0"
            mod_dependencies = []

            mod_docs_dir = os.path.join(directory.path, "documentation")
            mod_error_path = os.path.join("game", "submods", directory.name)
            mod_info_path = os.path.join(directory.path, "modinfo.json")
            mod_help_path = os.path.join(mod_docs_dir, ".Getting Started.txt")
            mod_help_modinfo_path = os.path.join(mod_docs_dir, "Setting Up Modinfo.txt")
            
            if not os.path.isfile(mod_info_path):
                print("  - Mod " + mod_id + " does not contain a modinfo.json file. Creating new files...")
                if not os.path.isdir(mod_docs_dir):
                    print("  - Creating documentation...")
                    os.mkdir(mod_docs_dir)
                try:
                    with open(mod_help_path, 'w') as file:
                        file.write(submods.help.getting_started)
                except:
                    pass
                try:
                    with open(mod_help_modinfo_path, 'w') as file:
                        file.write(submods.help.modinfo.format(mod_name, mod_id))
                except:
                    pass
                    
                    print("  - Creating modinfo.json...")
                try:
                    with open(mod_info_path, 'w') as file:
                        file.write(submods.modinfo.format(mod_name, mod_id))
                    print("  - Finished!")
                except:
                    print_error("  - Failed to create modinfo.json", path=mod_error_path)
            
            try:
                with open(mod_info_path) as file:
                    modinfo = json.load(file)
                    mod_name = str(modinfo.get("name", mod_name))
                    mod_id = str(modinfo.get("id", mod_id))
                    mod_version = str(modinfo.get("version", mod_version))
                    mod_dependencies = modinfo.get("dependencies", mod_dependencies)
                    if type(mod_dependencies) == str:
                        mod_dependencies = [mod_dependencies]
                    else:
                        if (str(type(mod_dependencies)) != "<class 'list'>"):
                            mod_dependencies = []
            except:
                print_error("  - Failed to load modinfo.json", path=mod_error_path)

            submods.mods[mod_id] = { "name": mod_name, "id": mod_id, "version": mod_version, "dependencies": mod_dependencies }
            print("  - Mod ID: " + mod_id + ", Version: " + mod_version + os.linesep + "  - Dependencies: " + str(mod_dependencies))
    print("Checking loaded submods for missing dependencies...")

    #TODO: Make sure to check all dependencies first before raising any errors as ideally we want to show all dependencies that are missing.
    for key, submod in submods.mods.items():
        if len(submod["dependencies"]) > 0:
            for dependency in submod["dependencies"]:
                if not parse_mod_id(dependency) in submods.mods:
                    try:
                        raise KeyError("Failed to load submods as submod " + submod["id"] + " is missing dependency " + parse_mod_id(dependency))
                    except:
                        print_error("  - Failed to load submods as submod " + submod["id"] + " is missing dependency " + parse_mod_id(dependency), path=mod_error_path)
                        raise
    print("Mod loading complete! Loaded " + str(submods.mod_count) + " mod(s)")