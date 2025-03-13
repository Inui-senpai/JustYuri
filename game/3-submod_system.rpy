#==================================================#
#  Just Yuri Mod - Main File
#==================================================#
#  This file is responsible for loading submods in
#  the game/submods folder and providing the
#  documentation for mod developers
#  :D
#==================================================#
init -999 python:

    import os
    import json
    import re as regex  # Better practice to import re as its conventional name

    submods = {}
    submods.mods = {}
    submods.mod_count = 0
    submods.modinfo = """{
    "name": "{0}",
    "id": "{1}",
    "version": "1.0.0",
    "description": "This is a mod description.\\nHi! :D",
    "dependencies": [],
    "developer_mode": false
}"""
    #==================================================#
    #  Functions
    #==================================================#
    def parse_mod_id(name):
        match = regex.match("[a-z0-9\\_\\-]*", name.lower().replace(" ", "_"))
        return match.group(0) if match != None else "unknown"

    class Submod:
        # Use default values directly in the class definition
        name = None
        id = None
        version = "1.0.0"
        description = None
        dependencies = []
        icon = None  # Initialize icon to None
        path = None

        def __init__(self, mod_name, mod_id, path):
            self.name = mod_name
            self.id = mod_id
            self.path = path
            # Set the default icon here, so it's only created once per Submod.
            self.icon = Transform("images/default_submod.png", size=(100,100), fit="contain")


    #==================================================#
    #  Start Submod System
    #==================================================#
    print("Checking for submods...")
    request_dev_access = False

    # Use config.savedir for the submods directory
    submods_dir = os.path.join(config.savedir, "submods")
    print("submods_dir is:", submods_dir) # Debug print

    if not os.path.isdir(submods_dir):
        print("Creating submods folder...")
        os.makedirs(submods_dir, exist_ok=True)  # Use makedirs and exist_ok
    #else: # No need for an else here, the loop can be unconditional
    for directory in os.scandir(submods_dir):
        if not directory.is_dir():
            continue
        print("Scanning mod: " + directory.name)
        submods.mod_count = submods.mod_count + 1
        mod_docs_dir =  os.path.join(directory.path, "documentation")
        mod_error_path = directory.path #Use the correct path
        mod_info_path = os.path.join(directory.path, "modinfo.json")
        mod_icon_path = os.path.join(directory.path, "icon.png")

        print("mod_docs_dir:", mod_docs_dir) # Debug Prints
        print("mod_info_path:", mod_info_path)
        print("mod_icon_path", mod_icon_path)


        submod = Submod(directory.name, parse_mod_id(directory.name), mod_error_path)

        if not os.path.isfile(mod_info_path):
            print("  - Mod " + submod.id + " does not contain a modinfo.json file. Creating new files...")
            if not os.path.isdir(mod_docs_dir):
                print("  - Creating documentation...")
                # Unpack documentation *only if it doesn't exist*
                try:
                    unpack(paths.documentation[0] + "/submods", mod_docs_dir) #Be careful where documentation comes from
                except Exception as e:
                    print(f"  - Error unpacking documentation: {e}") # Handle unpacking errors
                    print_error(e, path=mod_error_path)


                print("  - Creating modinfo.json...")
            try:
                with open(mod_info_path, 'w') as file:
                    file.write(submods.modinfo.format(submod.name, submod.id))
                print("  - Finished!")
            except Exception as exception:  # Catch specific exceptions if possible
                print("  - Failed to create modinfo.json")
                print_error(exception, path=mod_error_path)

        try:
            with open(mod_info_path) as file:
                modinfo = json.load(file)
                submod.name = str(modinfo.get("name", submod.name))
                submod.id = str(modinfo.get("id", submod.id))
                submod.version = str(modinfo.get("version", submod.version))
                submod.description = modinfo.get("description", submod.description)
                submod.dependencies = modinfo.get("dependencies", submod.dependencies)
                request_dev_access = modinfo.get("developer_mode", request_dev_access)
                if submod.description:
                    submod.description = str(submod.description)
                if isinstance(submod.dependencies, str):  # Use isinstance for type checking
                    submod.dependencies = [submod.dependencies]
                elif not isinstance(submod.dependencies, list):
                    submod.dependencies = []
        except Exception as exception:  # Catch specific exceptions if possible
            print("  - Failed to load modinfo.json")
            print_error(exception, path=mod_error_path)

        if os.path.isfile(mod_icon_path):
            print("  - Mod " + submod.id + " has an icon. Loading image...")
            try:
                # Load directly, don't construct a path relative to "submods/"
                submod.icon = Transform(mod_icon_path, size=(100,100), fit="contain")
            except Exception as exception:  # Catch specific exceptions
                print("  - Failed to load icon.png")
                print_error(exception, path=mod_error_path)

        renpy.image(submod.id + ":icon", submod.icon)
        submods.mods[submod.id] = submod
        print("  - Mod ID: " + submod.id + ", Version: " + submod.version + os.linesep + "  - Dependencies: " + str(submod.dependencies))
    print("Checking loaded submods for missing dependencies...")

    #TODO: Make sure to check all dependencies first before raising any errors as ideally we want to show all dependencies that are missing.
    should_continue = True
    for key, submod in submods.mods.items():
        if len(submod.dependencies) > 0:
            for dependency in submod.dependencies:
                if not parse_mod_id(dependency) in submods.mods:
                    print("  - Submod " + submod.id + " is missing dependency " + parse_mod_id(dependency))
                    print_error(KeyError("Submod " + submod.id + " is missing dependency " + parse_mod_id(dependency)), path=(submod.path, config.basedir))
                    should_continue = False
    if not should_continue:
        print_fatal(KeyError("One or more submods are missing dependencies. Read error.log for more info"))
    if request_dev_access:
        print("One or more mods have requested developer mode. Enabling developer mode...")
        dev_access = True #Should be defined somewhere, ensure it is.
    print("Mod loading complete! Loaded " + str(submods.mod_count) + " mod(s)")
