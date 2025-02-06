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
    import os, shutil, datetime, singleton, random, subprocess, base64, string, math, time, webbrowser, json, traceback
    import re as regex
    #import jycrypt
    from collections.abc import Callable as CHE
    from typing import Any
    

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

#==================================================#
# Initialization
#==================================================#
define current_label = None

init -999 python:
    print("Loading " + config.name + " - " + config.version + "..." + os.linesep + "-------------------------------")
    dev_access = config.developer
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