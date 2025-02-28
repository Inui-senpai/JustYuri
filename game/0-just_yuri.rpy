#==================================================#
#  Just Yuri Mod - Main File
#==================================================#
#  This file is the main file that runs in the mod 
#  and handles the initialization process.
#  
#  :D
#==================================================#

#==================================================#
# Pre Initialization
#==================================================#
python early:
    import os, shutil, datetime, singleton, random, subprocess, base64, string, math, time, webbrowser, json, traceback, inspect, rstr
    import re as regex
    #import jycrypt
    from typing import Any
    
    dev_access = not "scripts" in config.archives
    initial_dev_access = bool(dev_access)
    me = singleton.SingleInstance()
    today = datetime.date.today()
    sys.path.append(os.path.join(renpy.config.gamedir, 'python-packages'))

    if renpy.windows:
        import ctypes, ctypes.wintypes as wintypes
        user32 = ctypes.windll.user32
        win_callback = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)
    elif renpy.linux:
        import Xlib
        from Xlib.display import Display
        from Xlib.Xutil import IconicState # Used to see if a window is minimized

        linux_display = Display() # Gets the default display in linux
        linux_root = linux_display.screen().root # Gets the root window in linux to get important information

    def get_home_directory():
        if initial_dev_access:
            return os.path.join(config.gamedir, "saves")

        if renpy.macintosh:
            return os.path.expanduser("~/Library/RenPy/")
        elif renpy.windows:
            if 'APPDATA' in os.environ:
                return os.environ['APPDATA'] + "/RenPy/"
            else:
                return os.path.expanduser("~/RenPy/")
        else:
            return os.path.expanduser("~/.renpy/")

    def copy_file(file_path, new_file_path):
        with open(file_path, "rb") as file:
            with open(new_file_path, "wb") as new_file:
                from shutil import copyfileobj
                copyfileobj(file, new_file)

    def load_persistent(file_path):
        from renpy.compat.pickle import loads
        from glob import glob
        import codecs
        path = glob(os.path.join(file_path, "persistent"))

        if path:
            path = path[0]
            with open(path,"rb") as file:
                persistent_data = codecs.decode(file.read(), encoding='zlib', errors='strict')
                persistent_var = loads(persistent_data)
                
                persistent_data = vars(persistent_var)
                for key, value in sorted(persistent_data.items()):
                    try:
                        setattr(persistent_var, key, value)
                    except:
                        pass
                return persistent_var
        return None
    
    def save_persistent(persistent_var, file_path, file_name = "persistent"):
        from renpy.compat.pickle import dumps
        import zlib

        if file_path and file_name:
            path = os.path.join(file_path, file_name)
            with open(path,"wb") as file:
                print("Attempting to write...")
                try:
                    persistent_data = dumps(persistent_var)
                    compressed = zlib.compress(persistent_data, 3)
                    compressed += renpy.savetoken.sign_data(persistent_data).encode("utf-8")
                    file.write(compressed)
                    print("- Success")
                except Exception as e:
                    print_error(e, False)

    def apply_persistent(persistent_var, overwrite=True):
        if not persistent_var:
            print_error(NameError("Failed to apply persistent as it is None"))
        persistent_data = vars(persistent_var)
        for key, value in sorted(persistent_data.items()):
            try:
                if not overwrite and hasattr(persistent, key):
                    continue
                setattr(persistent, key, value)
            except:
                pass

    save_directory = get_home_directory() if initial_dev_access else os.path.join(get_home_directory(), "JustYuri")
    backup_directory = os.path.join(save_directory, "backups")

#==================================================#
# Initialization
#==================================================#
define current_label = None

init -999 python:
    print("Loading " + config.name + " - " + config.version + "..." + os.linesep + "-------------------------------")
    dismiss_keys = config.keymap['dismiss']
    allow_dialogue = False
    allow_skipping = False
    quick_menu = False
    dissolve_time = 5

    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    config.skipping = False
    config.allow_skipping = False
    config.keymap["console"] = ["shift_O", "alt_shift_K_o"]
    renpy.music.register_channel("music2", mixer="music", tight=True)
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    
    if persistent.alpha_save == None:
        if persistent.game_session == None and persistent.karma_points != None: #There is no game session, but karma does exist
            persistent.alpha_save = True #there is an alpha save
        else:
            persistent.alpha_save = False

    persistent.temp_memory = []
    if persistent.game_session == None:
        persistent.game_session = 0
    if not persistent.costume in ["school", "sweater", "valentines"]: #increase this list with new costumes
        persistent.costume = "school"
    if persistent.bg == None:
        persistent.bg = "space"
    if persistent.karma_points == None:
        persistent.karma_points = 0
    if persistent.sanity_points == None:
        persistent.sanity_points = 0
    if persistent.insanity_points != None:
        persistent.sanity_points = -1 * persistent.insanity_points
    if persistent.autoload == "ch30_loop":
        persistent.autoload = "ch30_autoload"

    #Checking if player has older version of persistent.costume
    #If so, we append it to the newest version
    if persistent.costume is not None:
        if type(persistent.costume)==list:
            persistent.costume = persistent.costume[0]
    #Check for each archive needed. If one is missing, throw an error and close
    for archive in ['fonts']:
        if not archive in config.archives:
            renpy.error("DDLC archive files not found in /game folder. Check installation and try again.")
    
    #If game closed with HDY enabled, disable it
    persistent.HDY = False

    def is_callable(obj):
        return hasattr(obj, "__call__")

    def change_exception_arg(exception: BaseException, msg: str):
        if len(exception.args) > 0 and type(exception.args[0]) == str:
            exception.args = exception.args[1:]
            exception.args = (msg,) + exception.args

    def type_str(obj):
        return regex.sub("\<class '([^']*)'\>", "\\1", str(type(obj)))

    def print_debug(message):
        if not dev_access: return
        print(message)

    # Prints an error message and optionally writes the full error in the specified path relative to the base directory. Path must be a string.
    def print_error(message, new_traceback=True, path=config.basedir):
        exception_type, exception, tb = sys.exc_info()

        if isinstance(message, BaseException):
            exception = message
            exception_type = type(message)
        else:
            exception = Exception(message)
            exception_type = type(exception)

        if new_traceback:
            tb = exception.__traceback__
        elif tb:
            exception.__traceback__ = tb
        exception_type = type_str(exception)
        

        if type(path) == str:
            print(os.linesep + "------------ ERROR ------------" + os.linesep + exception_type + ": " + str(exception))
            traceback.print_tb(tb, file=sys.stdout)
            print("")
            with open(os.path.join(config.basedir, path, "error.log"), mode='a') as file_error:
                file_error.write(os.linesep + "------------ ERROR ------------" + os.linesep + exception_type + ": " + str(exception) + os.linesep)
                try:
                    traceback.print_tb(tb, file=file_error)
                except:
                    pass
                print("  - Created error.log file in " + path)
        elif type(path) == tuple:
            print(os.linesep + "------------ ERROR ------------" + os.linesep + exception_type + ": " + str(exception))
            traceback.print_tb(tb, file=sys.stdout)
            print("")
            for sub_path in path:
                with open(os.path.join(config.basedir, sub_path, "error.log"), mode='a') as file_error:
                    file_error.write(os.linesep + "------------ ERROR ------------" + os.linesep + exception_type + ": " + str(exception) + os.linesep)
                    try:
                        traceback.print_tb(tb, file=file_error)
                    except:
                        pass
                    print("  - Created error.log file in " + sub_path)
        else:
            print(os.linesep + "-------- SILENT ERROR ---------" + os.linesep + exception_type + ": " + str(exception))
            traceback.print_tb(tb, file=sys.stdout)
            print("")
        return exception

    # Prints a fatal error message and optionally writes the full error in the specified path relative to the base directory. Path must be a string. Once complete, raises the exception
    def print_fatal(message, status=1, new_traceback=True, path=config.basedir):
        exception_type, exception, tb = sys.exc_info()

        if isinstance(message, BaseException):
            exception = message
            exception_type = type(message)
        else:
            exception = Exception(message)
            exception_type = type(exception)

        if new_traceback:
            tb = exception.__traceback__
        elif tb:
            exception.__traceback__ = tb
        exception_type = type_str(exception)
        
        print(os.linesep + "------------ FATAL ------------" + os.linesep + exception_type + ": " + str(exception))
        traceback.print_tb(tb, file=sys.stdout)
        print("")

        if type(path) == str:
            with open(os.path.join(config.basedir, path, "fatal.log"), mode='w') as file_error:
                file_error.write(os.linesep + "------------ FATAL ------------" + os.linesep + exception_type + ": " + str(exception) + os.linesep)
                try:
                    traceback.print_tb(tb, file=file_error)
                except:
                    pass
                print("  - Created fatal.log file in " + path)
        elif type(path) == tuple:
            print(os.linesep + "------------ FATAL ------------" + os.linesep + exception_type + ": " + str(exception))
            traceback.print_tb(tb, file=sys.stdout)
            print("")
            for sub_path in path:
                with open(os.path.join(config.basedir, sub_path, "fatal.log"), mode='a') as file_error:
                    file_error.write(os.linesep + "------------ FATAL ------------" + os.linesep + exception_type + ": " + str(exception) + os.linesep)
                    try:
                        traceback.print_tb(tb, file=file_error)
                    except:
                        pass
                    print("  - Created fatal.log file in " + sub_path)
        raise exception


#==================================================#
# Post Initialization
#==================================================#
init 999 python:
    year, month, day, hour, minute, second = tc_class.cur_time()
    print(os.linesep + "Loading of " + config.name + " - " + config.version + " complete!" + os.linesep + "-------------------------------" + os.linesep + os.linesep)