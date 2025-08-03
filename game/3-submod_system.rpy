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

    # --- Define Documentation Content ---
    getting_started_content = """Welcome to the submodding community! - Docs Version 1.0.0

If you are seeing this for the first time, these files automatically generate anytime a submod folder is missing a modinfo.json file.
To create a submod, change any of the information you want in the modinfo.json file, create your first .rpy file and start implementing whatever you can think of.

For a brief introduction into renpy, see: https://www.renpy.org/doc/html/quickstart.html#the-ren-py-launcher
If you intend on creating a more advanced submod, you may need knowledge of python as well. The one good place to learn the basics is: https://www.w3schools.com/python/python_intro.asp

To add dialogue to the talk menu, you use the add_dialogue method and provide it with your own Dialogue instance:

label test_label:
    $ show_chr("A-ABGBA-AAAA")
    y "Hi there!"

init python:
    add_dialogue(Dialogue("test_label", DialogueAPI.category_talk, name="Greet Yuri", sub_category="Greetings"))

You can get the sprite code via the control panel when you enable developer mode.

This mod contains various apis to help speed up development since the Just Yuri source is kinda messy at the moment. We will rectify the mess in time.
You can find the sources here: https://github.com/DarkskullDawnZenith/JustYuri

In the future, this documentation will be more fleshed out and user friendly, but for now this will only cover the bare minimum.

You can feel free to delete these documents if you would like to free up space for your mod. If you ever need to regenerate these docs, delete the modinfo.json file and reboot the game. Have fun!
"""

    modinfo_setup_content = """{
    ####################################################################################
    # This is what the Just Yuri mod reads to figure out what this submod is.          #
    # This is always automatically generated when a modinfo.json file is not detected. #
    ####################################################################################

    # The name of your submod. This will show up in game in the mods menu.
    "name": "",

    # The unique id of your submod. This is used in the dependencies blocks of other mods.
    "id": "",

    # The version of your submod. This can be anything you want, but keep it close to the format #.#.#
    "version": "1.0.0",

    # The unique ids of each submod that this submod requires.
    # If any id is present here and the mod isn't loaded, the game will crash and display any mods that are missing
    # Also supports putting a single string as well if you don't want to use a list
    "dependencies": [],

    # Whether to enable debug mode for Just Yuri. Adds additional information to the logs and allows access to the control panel
    "developer_mode": false
}
"""
    # Note: The above is intended for a TXT file, but the content looks like JSON with comments.
    # If it should be a valid JSON file instead, remove the comments (#) or use a different format.
    # Assuming it's intended as a descriptive TXT file as requested.

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
            # Default icon is still loaded from the *game* directory's images.
            self.icon = Transform(os.path.join(config.gamedir, "images", "default_submod.png"), size=(100,100), fit="contain")

    print("Checking for submods...")
    request_dev_access = False
    dev_access = False

    #==================================================#
    #  Start Submod System
    #==================================================#

    # Use game directory for submods
    submods_dir = os.path.join(config.gamedir, "submods")
    placeholder_dir = os.path.join(submods_dir, "_placeholder")
    print("submods_dir is:", submods_dir)

    # --- Create base submods directory if it doesn't exist ---
    if not os.path.isdir(submods_dir):
        print("Creating submods folder...")
        try:
            os.makedirs(submods_dir, exist_ok=True)
        except Exception as e:
            print(f"Error creating submods directory at {submods_dir}: {e}")

    # --- Create placeholder directory and files if they don't exist ---
    # (This part remains largely the same, creating the initial placeholder example)
    if os.path.isdir(submods_dir) and not os.path.isdir(placeholder_dir):
        print("Creating placeholder folder...")
        try:
            os.makedirs(placeholder_dir, exist_ok=True)

            # Create placeholder modinfo.json
            placeholder_info_path = os.path.join(placeholder_dir, "modinfo.json")
            with open(placeholder_info_path, 'w', encoding='utf-8') as f:
                placeholder_info = submods.modinfo_template.copy()
                placeholder_info["name"] = "Placeholder"
                placeholder_info["id"] = "placeholder"
                json.dump(placeholder_info, f, indent=4)

            # Copy default icon
            placeholder_icon_path = os.path.join(placeholder_dir, "icon.png")
            source_icon_path = os.path.join(config.gamedir, "images", "default_submod.png")
            print(f"Attempting to copy icon from: {source_icon_path} to {placeholder_icon_path}")
            try:
                if os.path.isfile(source_icon_path):
                    copyfile(source_icon_path, placeholder_icon_path)
                    print("Icon copied successfully!")
                else:
                    print(f"Error: Source icon file not found at {source_icon_path}")
            except Exception as e:
                 print(f"An error occurred while copying the placeholder icon: {e}")


            # Create placeholder documentation directory
            placeholder_docs_dir = os.path.join(placeholder_dir, "documentation")
            if not os.path.isdir(placeholder_docs_dir):
                 os.makedirs(placeholder_docs_dir, exist_ok=True)

            # --- Write the specific doc files for the placeholder ---
            getting_started_path_placeholder = os.path.join(placeholder_docs_dir, "0 - Getting Started.txt")
            modinfo_setup_path_placeholder = os.path.join(placeholder_docs_dir, "Setting Up Modinfo.txt")

            try:
                print("  - Creating placeholder '0 - Getting Started.txt'...")
                with open(getting_started_path_placeholder, 'w', encoding='utf-8') as f:
                    f.write(getting_started_content)
            except Exception as e:
                print(f"  - Failed to create placeholder '0 - Getting Started.txt': {e}")

            try:
                print("  - Creating placeholder 'Setting Up Modinfo.txt'...")
                with open(modinfo_setup_path_placeholder, 'w', encoding='utf-8') as f:
                    f.write(modinfo_setup_content)
            except Exception as e:
                print(f"  - Failed to create placeholder 'Setting Up Modinfo.txt': {e}")

        except Exception as e:
            print(f"Error creating placeholder files in {placeholder_dir}: {e}")

    # --- Scan for actual submods ---
    if os.path.isdir(submods_dir):
        for directory in os.scandir(submods_dir):
            if not directory.is_dir() or directory.path == placeholder_dir:
                continue

            print("Scanning mod: " + directory.name)
            submods.mod_count += 1
            mod_docs_dir = os.path.join(directory.path, "documentation")
            mod_error_path = directory.path # Used for error reporting context
            mod_info_path = os.path.join(directory.path, "modinfo.json")
            mod_icon_path = os.path.join(directory.path, "icon.png")

            print("mod_docs_dir:", mod_docs_dir)
            print("mod_info_path:", mod_info_path)
            print("mod_icon_path", mod_icon_path)

            submod = Submod(directory.name, parse_mod_id(directory.name), mod_error_path)

            # --- Check if modinfo.json exists, create it and docs if not ---
            if not os.path.isfile(mod_info_path):
                print("  - Mod " + submod.id + " does not contain a modinfo.json file. Creating default files...")

                # 1. Ensure documentation directory exists
                if not os.path.isdir(mod_docs_dir):
                    print("  - Creating documentation directory...")
                    try:
                        os.makedirs(mod_docs_dir, exist_ok=True)
                    except Exception as e:
                        print(f"  - Failed to create documentation directory: {e}")
                        # Log the error, but might still attempt to create modinfo.json
                        print_error(e, path=mod_error_path)

                # 2. Create the specific documentation files IF the docs directory exists
                if os.path.isdir(mod_docs_dir):
                    getting_started_path = os.path.join(mod_docs_dir, "0 - Getting Started.txt")
                    modinfo_setup_path = os.path.join(mod_docs_dir, "Setting Up Modinfo.txt")

                    # Write "Getting Started" doc
                    try:
                        print("  - Creating '0 - Getting Started.txt'...")
                        with open(getting_started_path, 'w', encoding='utf-8') as f:
                            f.write(getting_started_content)
                    except Exception as e:
                        print(f"  - Failed to create '0 - Getting Started.txt': {e}")
                        print_error(e, path=mod_error_path) # Use existing error reporting

                    # Write "Setting Up Modinfo" doc
                    try:
                        print("  - Creating 'Setting Up Modinfo.txt'...")
                        with open(modinfo_setup_path, 'w', encoding='utf-8') as f:
                            f.write(modinfo_setup_content)
                    except Exception as e:
                        print(f"  - Failed to create 'Setting Up Modinfo.txt': {e}")
                        print_error(e, path=mod_error_path) # Use existing error reporting
                else:
                     print("  - Skipping documentation file creation because directory doesn't exist.")


                # 3. Create modinfo.json
                print("  - Creating modinfo.json...")
                try:
                    with open(mod_info_path, 'w', encoding='utf-8') as file:
                        modinfo = submods.modinfo_template.copy()
                        modinfo["name"] = submod.name or "" # Use existing name if available
                        modinfo["id"] = submod.id or ""     # Use existing ID if available
                        json.dump(modinfo, file, indent=4)
                    print("  - Finished creating default files!")
                except Exception as e:
                    print("  - Failed to create modinfo.json")
                    print_error(e, path=mod_error_path)

            # --- Load modinfo.json (if it exists now or existed before) ---
            if os.path.isfile(mod_info_path):
                try:
                    with open(mod_info_path, 'r', encoding='utf-8') as file: # Read with utf-8
                        modinfo = json.load(file)
                        submod.name = str(modinfo.get("name", submod.name))
                        submod.id = str(modinfo.get("id", submod.id))
                        submod.version = str(modinfo.get("version", submod.version))
                        submod.description = modinfo.get("description", submod.description)
                        submod.dependencies = modinfo.get("dependencies", submod.dependencies)
                        request_dev_access = modinfo.get("developer_mode", request_dev_access)

                        if submod.description is not None:
                            submod.description = str(submod.description)
                        if isinstance(submod.dependencies, str):
                            submod.dependencies = [submod.dependencies]
                        elif not isinstance(submod.dependencies, list):
                            submod.dependencies = []

                except json.JSONDecodeError as e:
                     print(f"  - Failed to load modinfo.json: Invalid JSON format - {e}")
                     print_error(e, path=mod_error_path)
                except Exception as e:
                    print(f"  - Failed to load modinfo.json: {e}")
                    print_error(e, path=mod_error_path)

            # --- Load icon ---
            if os.path.isfile(mod_icon_path):
                print("  - Mod " + submod.id + " has an icon. Loading image...")
                try:
                    # 1. Get the path to the icon relative to the game directory.
                    relative_icon_path = os.path.relpath(mod_icon_path, config.gamedir)
                    # 2. Normalize the path separators to forward slashes, which Ren'Py prefers.
                    relative_icon_path = relative_icon_path.replace(os.path.sep, '/')

                    # 3. Use this relative path for the Transform. Ren'Py will now find it correctly.
                    submod.icon = Transform(relative_icon_path, size=(100, 100), fit="contain")
                    print(f"  - Successfully created Transform for icon at: {relative_icon_path}")
                except Exception as e:
                    print("  - Failed to load icon.png")
                    print_error(e, path=mod_error_path)
            # If no custom icon is found, the default icon set in Submod.__init__ will be used.

            # This line now correctly registers the Transform (either the default or the custom one)
            renpy.image(submod.id + ":icon", submod.icon)
            submods.mods[submod.id] = submod
            print("  - Mod ID: " + submod.id + ", Version: " + submod.version)
            print("  - Dependencies: " + str(submod.dependencies))

    else:
        print(f"Warning: Submod directory {submods_dir} does not exist or is not accessible. Skipping submod loading.")


    # --- Dependency check ---
    print("Checking loaded submods for missing dependencies...")
    should_continue = True
    missing_dependency_errors = []

    for key, submod in submods.mods.items():
        if len(submod.dependencies) > 0:
            for dependency in submod.dependencies:
                parsed_dependency_id = parse_mod_id(dependency)
                if parsed_dependency_id not in submods.mods:
                    error_message = f"Submod '{submod.id}' is missing dependency '{parsed_dependency_id}'"
                    print(f"  - {error_message}")
                    missing_dependency_errors.append({
                        "submod_id": submod.id,
                        "missing_dependency": parsed_dependency_id,
                        "path": submod.path
                    })
                    print_error(KeyError(error_message), path=(submod.path, config.basedir))
                    should_continue = False

    if not should_continue:
        print_fatal(KeyError("One or more submods are missing dependencies. Check error.log or console output for details."))

    # --- Developer mode check ---
    if request_dev_access:
        print("One or more mods have requested developer mode. Enabling developer mode...")
        config.developer = True # Standard Ren'Py way
        dev_access = True # Your script's flag

    print("Mod loading complete! Loaded " + str(submods.mod_count) + " mod(s)")
