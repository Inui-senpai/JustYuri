python early:
    import os, shutil, datetime, singleton, random, subprocess, base64, string, math, time, webbrowser
    #import jycrypt
    me = singleton.SingleInstance()
    today = datetime.date.today()

init -999 python:
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
    #if persistent.alpha_save and not persistent.adjusted:
    #    persistent.karma_points = persistent.karma_points * 1.5
    #    persistent.sanity_points = persistent.sanity_points * 1.5
    #    persistent.adjusted = True
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
    #Check for each archive needed
    for archive in ['audio','images','fonts']:
        if not archive in config.archives:
            #If one is missing, throw an error and close
            renpy.error("DDLC archive files not found in /game folder. Check installation and try again.")

    #If game closed with HDY enabled, disable it
    persistent.HDY = False

#########################################
#RUN THESE AFTER FUNCTION ESTABLISHMENT##
#########################################

init python:
    year, month, day, hour, minute, second = tc_class.cur_time()
    
