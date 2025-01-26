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
    import os, shutil, datetime, singleton, random, subprocess, base64, string, math, time, webbrowser
    #import jycrypt
    me = singleton.SingleInstance()
    today = datetime.date.today()

#==================================================#
# Initialization
#==================================================#
init -999 python:
    print("Loading " + config.name + " - " + config.version + "...")
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
    for archive in ['audio','images','fonts']:
        if not archive in config.archives:
            renpy.error("DDLC archive files not found in /game folder. Check installation and try again.")

    #If game closed with HDY enabled, disable it
    persistent.HDY = False

#==================================================#
# Post Initialization
#==================================================#
init python:
    year, month, day, hour, minute, second = tc_class.cur_time()