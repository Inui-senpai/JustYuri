#==================================================#
#  Just Yuri Mod - Main File
#==================================================#

init -999 python:  # Use -999 for early initialization of data structures
    submods = {}
    submods.mods = {}
    submods.mod_count = 0
    submods.modinfo = """{
\t"name": "%s",
\t"id": "%s",
\t"version": "1.0.0",
\t"description": "This is a mod description.\\nHi! :D",
\t"dependencies": [],
\t"developer_mode": false
}"""
    submods.submods_dir = None  # Initialize as None
    submods.initialized = False

    def parse_mod_id(name):
        match = regex.match("[a-z0-9\\_\\-]*", name.lower().replace(" ", "_"))
        return match.group(0) if match != None else "unknown"

    class Submod:
        def __init__(self, mod_name, mod_id, path):
            self.name = mod_name
            self.id = mod_id
            self.path = path
            self.version = "1.0.0"
            self.description = None
            self.dependencies = []
            self.icon = Transform("images/default_submod.png", size=(100,100), fit="contain")

init python:  # Use a standard init python block (init 0)
    def load_submods():
        if submods.initialized:  # Check if already initialized
            return

        print("Checking for submods...")
        request_dev_access = False

        # --- CRITICAL CHANGE: Use renpy.config and store the path ---
        if submods.submods_dir is None:  # Only calculate once
             submods.submods_dir = os.path.join(renpy.config.savedir, "submods")

        if not os.path.isdir(submods.submods_dir):
            print("Creating submods folder...")
            os.makedirs(submods.submods_dir, exist_ok=True)
        else:
            for directory in os.scandir(submods.submods_dir):
                if not directory.is_dir():
                    continue
                print("Scanning mod: " + directory.name)
                submods.mod_count += 1

                mod_docs_dir =  os.path.join(directory.path, "documentation")
                mod_error_path = os.path.join(directory.path)
                mod_info_path = os.path.join(directory.path, "modinfo.json")
                mod_icon_path = os.path.join(directory.path, "icon.png")
                submod = Submod(directory.name, parse_mod_id(directory.name), mod_error_path)


                if not os.path.isfile(mod_info_path):
                    print("  - Mod " + submod.id + " does not contain a modinfo.json file. Creating new files...")
                    if not os.path.isdir(mod_docs_dir):
                        print("  - Creating documentation...")
                        os.makedirs(mod_docs_dir, exist_ok=True)  #Create it
                    print("  - Creating modinfo.json...")
                    try:
                        with open(mod_info_path, 'w') as file:
                            file.write(submods.modinfo % (submod.name, submod.id))
                        print("  - Finished!")
                    except BaseException as exception:
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
                        if type(submod.dependencies) == str:
                            submod.dependencies = [submod.dependencies]
                        elif not isinstance(submod.dependencies, list):
                            submod.dependencies = []
                except BaseException as exception:
                    print("  - Failed to load modinfo.json")
                    print_error(exception, path=mod_error_path)

                if os.path.isfile(mod_icon_path):
                    print("  - Mod " + submod.id + " has an icon.  Loading image...")
                    try:
                        submod.icon = Transform("submods/" + directory.name + "/icon.png", size=(100,100), fit="contain")
                    except BaseException as exception:
                        print("  - Failed to load icon.png")
                        print_error(exception, path=mod_error_path)

                renpy.image(submod.id + ":icon", submod.icon)
                submods.mods[submod.id] = submod
                print("  - Mod ID: " + submod.id + ", Version: " + submod.version + os.linesep + "  - Dependencies: " + str(submod.dependencies))

        print("Checking loaded submods for missing dependencies...")

        should_continue = True
        for key, submod in submods.mods.items():
            if len(submod.dependencies) > 0:
                for dependency in submod.dependencies:
                    if not parse_mod_id(dependency) in submods.mods:
                        print("  - Submod " + submod.id + " is missing dependency " + parse_mod_id(dependency))
                        print_error(KeyError("Submod " + submod.id + " is missing dependency " + parse_mod_id(dependency)), path=(submod.path, renpy.config.basedir)) #Use renpy.config here
                        should_continue = False
        if not should_continue:
            print_fatal(KeyError("One or more submods are missing dependencies. Read error.log for more info"))
        if request_dev_access:
            print("One or more mods have requested developer mode.  Enabling developer mode...")
            dev_access = True
        print("Mod loading complete! Loaded " + str(submods.mod_count) + " mod(s)")
        submods.initialized = True # Set to True after initialization

    #Dummy print_error and print_fatal
    def print_error(exception, path):
        print(f"Error: {exception} at {path}")

    def print_fatal(exception):
        print(f"Fatal Error: {exception}")

# Ensure load_submods is called *after* renpy.config is ready
$ load_submods()