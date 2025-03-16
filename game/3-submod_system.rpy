#==================================================#
#  Just Yuri Mod - Main File
#==================================================#
#  This file is responsible for loading submods in
#  the game/submods folder and providing the
#  documentation for mod developers
#  :D
#==================================================#

init -999 python:

    submods = {}
    submods.mods = {}
    submods.mod_count = 0

    submods.modinfo_template = {
        "name": "",
        "id": "",
        "version": "1.0.0",
        "dependencies": [],
        "developer_mode": False
    }

    #==================================================#
    #  Functions
    #==================================================#

    def parse_mod_id(name):
        match = regex.match("[a-z0-9\\_\\-]*", name.lower().replace(" ", "_"))
        return match.group(0) if match != None else "unknown"

    class Submod:
        name = None
        id = None
        version = "1.0.0"
        description = None
        dependencies = []
        icon = None
        path = None

        def __init__(self, mod_name, mod_id, path):
            self.name = mod_name
            self.id = mod_id
            self.path = path
            # Important: Default icon is still loaded from the *game* directory.
            self.icon = Transform(os.path.join(config.gamedir, "images", "default_submod.png"), size=(100,100), fit="contain")

    print("Checking for submods...")
    request_dev_access = False
    dev_access = False

    #==================================================#
    #  Start Submod System
    #==================================================#

    submods_dir = os.path.join(config.savedir, "JustYuri_Submods")
    placeholder_dir = os.path.join(submods_dir, "_placeholder")
    print("submods_dir is:", submods_dir)

    if not os.path.isdir(submods_dir):
        print("Creating submods folder...")
        os.makedirs(submods_dir, exist_ok=True)

    if not os.path.isdir(placeholder_dir):
        print("Creating placeholder folder...")
        os.makedirs(placeholder_dir, exist_ok=True)

        try:
            placeholder_info_path = os.path.join(placeholder_dir, "modinfo.json")
            with open(placeholder_info_path, 'w') as f:
                placeholder_info = submods.modinfo_template.copy()
                placeholder_info["name"] = "Placeholder"
                placeholder_info["id"] = "placeholder"
                json.dump(placeholder_info, f, indent=4)

            # --- Icon Copying (Corrected) ---
            placeholder_icon_path = os.path.join(placeholder_dir, "icon.png")
            source_icon_path = os.path.join(config.gamedir, "images", "default_submod.png")

            print(f"Attempting to copy icon from: {source_icon_path}")
            print(f"Destination icon path: {placeholder_icon_path}")

            try:
                if os.path.isfile(source_icon_path):
                    copyfile(source_icon_path, placeholder_icon_path)
                    print("Icon copied successfully!")
                else:
                    print(f"Error: Source icon file not found at {source_icon_path}")
            except FileNotFoundError:
                print(f"Error: Source icon file not found at {source_icon_path}")
            except PermissionError:
                print(f"Error: Permission denied. Could not copy icon to {placeholder_icon_path}")
            except SameFileError:
                print(f"The files are the same")
            except Exception as e:
                print(f"An unexpected error occurred while copying the icon: {e}")


            placeholder_docs_dir = os.path.join(placeholder_dir, "documentation")
            if not os.path.isdir(placeholder_docs_dir):
                os.makedirs(placeholder_docs_dir, exist_ok=True)
                try:
                    unpack_source = os.path.join(config.gamedir, "documentation", "submods")
                    if os.path.exists(unpack_source):
                        unpack(unpack_source, placeholder_docs_dir)
                    else:
                        print(f"Warning: Documentation source not found: {unpack_source}")
                except Exception as e:
                    print(f"Error unpacking default documentation: {e}")

        except Exception as e:
            print(f"Error creating placeholder files: {e}")

    for directory in os.scandir(submods_dir):
        if not directory.is_dir() or directory.path == placeholder_dir:
            continue

        print("Scanning mod: " + directory.name)
        submods.mod_count += 1
        mod_docs_dir = os.path.join(directory.path, "documentation")
        mod_error_path = directory.path
        mod_info_path = os.path.join(directory.path, "modinfo.json")
        mod_icon_path = os.path.join(directory.path, "icon.png")

        print("mod_docs_dir:", mod_docs_dir)
        print("mod_info_path:", mod_info_path)
        print("mod_icon_path", mod_icon_path)

        submod = Submod(directory.name, parse_mod_id(directory.name), mod_error_path)

        if not os.path.isfile(mod_info_path):
            print("  - Mod " + submod.id + " does not contain a modinfo.json file.  Creating...")

            if not os.path.isdir(mod_docs_dir):
                print("  - Creating documentation directory...")
                os.makedirs(mod_docs_dir, exist_ok=True)

            try:
                print("  - Unpacking documentation...")
                unpack_source = os.path.join(config.gamedir, "documentation", "submods")
                if os.path.exists(unpack_source):
                    unpack(unpack_source, mod_docs_dir)
                else:
                    print(f"Warning: Documentation source not found: {unpack_source}")
            except Exception as e:
                print(f"  - Error unpacking documentation: {e}")
                print_error(e, path=mod_error_path)

            print("  - Creating modinfo.json...")
            try:
                with open(mod_info_path, 'w') as file:
                    modinfo = submods.modinfo_template.copy()
                    modinfo["name"] = submod.name or ""
                    modinfo["id"] = submod.id or ""
                    json.dump(modinfo, file, indent=4)
                print("  - Finished!")
            except Exception as e:
                print("  - Failed to create modinfo.json")
                print_error(e, path=mod_error_path)

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
                if isinstance(submod.dependencies, str):
                    submod.dependencies = [submod.dependencies]
                elif not isinstance(submod.dependencies, list):
                    submod.dependencies = []
        except Exception as e:
            print("  - Failed to load modinfo.json")
            print_error(e, path=mod_error_path)

        # --- Icon Loading (Corrected) ---
        if os.path.isfile(mod_icon_path):
            print("  - Mod " + submod.id + " has an icon. Loading image...")
            try:
                # Load the icon from the *writable* directory (where submods are stored)
                submod.icon = Transform(mod_icon_path, size=(100, 100), fit="contain")
            except Exception as e:
                print("  - Failed to load icon.png")
                print_error(e, path=mod_error_path)

        renpy.image(submod.id + ":icon", submod.icon)  # This line remains the same
        submods.mods[submod.id] = submod
        print("  - Mod ID: " + submod.id + ", Version: " + submod.version + os.linesep + "  - Dependencies: " + str(submod.dependencies))

    print("Checking loaded submods for missing dependencies...")

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
        dev_access = True
    print("Mod loading complete! Loaded " + str(submods.mod_count) + " mod(s)")
