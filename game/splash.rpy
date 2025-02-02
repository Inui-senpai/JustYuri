##
## Before load, check to be sure that the archive files were found.
## If not, display an error message and quit.
init -100 python:
    import os
    #Check for each archive needed
    for archive in ['fonts']:
        if not archive in config.archives:
            #If one is missing, throw an error and chlose
            renpy.error("DDLC archive files not found in /game folder. Check installation and try again.")

## First, a disclaimer declaring this is a mod is shown, then there is a
## check for the original DDLC assets in the install folder. If those are
## not found, the player is directed to the developer's site to download.
##
init python:
    menu_trans_time = 1
    #The default splash message, originally shown in Act 1 and Act 4
    splash_message_default = "Wait... what is this?"
    #Optional splash messages, originally chosen at random in Act 2 and Act 3
    splash_messages = [
    "It's Just Yuri now.",
    "Nobody would care if those obnoxious brats killed themselves."
    ]

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

image menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move

image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_loop

image menu_fade:
    "white"
    menu_fadeout

image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 640
    ycenter 640
    zoom 0.60
    menu_art_move(0.50, 600, 1.18)

image menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move

image yuri_logo:
    "images/gui/logo.png"
    xpos 950 ypos 0 zoom 0.60
    menu_logo_move

image menu_particles:
    2.481
    xpos 1080
    ypos 100
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=100, particleTime=2.0, particleXSpeed=6, particleYSpeed=4).sm
    particle_fadeout

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0

image intro:
    truecenter
    "white"
    0.5
    "images/splash/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image tos = "images/splash/warning.png"
image tos2 = "images/splash/warning2.png"


label splashscreen:

    python:
        process_list = []
        currentuser = ""
        if renpy.windows:
            try:
                process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            except:
                pass
            try:
                for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    user = os.environ.get(name)
                    if user:
                        currentuser = user
            except:
                pass

    python:
        firstrun = ""
        try:
            firstrun = renpy.file("firstrun").read(1)
        except:
            with open(config.basedir + "/game/firstrun", "wb") as f:
                pass
    if not firstrun:
        if persistent.first_run:
            $ quick_menu = False
            scene black
            menu:
                "A previous save file has been found. Would you like to delete your save data and start over?"
                "Yes, delete my existing data.":
                    "Deleting save data...{nw}"
                    python:
                        delete_all_saves()
                        renpy.loadsave.location.unlink_persistent()
                        renpy.persistent.should_save_persistent = False
                        renpy.utter_restart()
                "No, continue where I left off.":
                    pass

        python:
            if not firstrun:
                try:
                    with open(config.basedir + "/game/firstrun", "w") as f:
                        f.write("1")
                except:
                    renpy.jump("readonly")

    #If this is the first time the game has been run, show a disclaimer
    if not persistent.first_run:
        python:
            restore_all_characters()
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0
        "Just Yuri is a Doki Doki Literature Club fan mod not affiliated with Team Salvato."
        "It is designed to be played only after the official game has been completed, for age 13+ with caution given to their own mental health."
        "Spoilers are within, the original game files for Doki Doki Literature Club are required to play this mod and can be downloaded for free at: {a=http://ddlc.moe}http://ddlc.moe{/a} (but seeing as you're here you likely already know that) "
        "We would like to remind you that you're currently playing a Beta version of Just Yuri, we the Just Yuri Dev Team are committed to improving the game with updates and new features based on your feedback."
        "Bugs, (while sometimes hilarious) are to be expected."
        "Additionally, the mod allows Yuri to possibly access portions of your computer outside of the DDLC folders and Ren'Py' APPDATA."
        "It currently has the capability to open up websites within your main internet browser, though none of these websites are malicious nor are they illegal."
        "By playing Just Yuri you agree that you have completed Doki Doki Literature Club and accept any spoilers contained within."
        "Additionally, by playing Doki Doki Literature Club, you agree that you are at least 13 years of age, and you consent to your exposure of highly disturbing content."
        menu:
            "Do you accept these terms?"
            "I agree.":
                pass
            "I do not agree":
                "By not accepting these terms you have opted out of playing the game. Closing application........{nw}"
                pause 2.0
                $ renpy.call("save_and_quit_but_its_abrupt")

        "A sincere thanks to you for playing our mod. Your ideas, bug reports, feedback and encouragement have shaped the future of Just Yuri." 
        "That future is bright and we thank you again for helping us build this project with you."
        "Please report any issues you find and suggestions you have at our GitLab; instructions to do that are in the documents provided with this game and within our online FAQ."
        "Updates to the game and our community can be found at our Discord {a=https://discordapp.com/invite/RUdwW7q}https://discordapp.com/invite/RUdwW7q{/a}"
        scene tos2
        with Dissolve(1.5)
        pause 1.0

        scene white
        with Dissolve(1.5)

        if not persistent.has_merged:
            call import_ddlc_persistent

        $ persistent.first_run = True

    $ basedir = config.basedir.replace('\\', '/')



    if persistent.autoload:
        jump autoload

    show white
    $ persistent.ghost_menu = False
    $ splash_message = splash_message_default
    $ config.main_menu_music = audio.t1
    $ renpy.music.play(config.main_menu_music)
    show intro with Dissolve(0.5, alpha=True)
    pause 2.5
    hide intro with Dissolve(0.5, alpha=True)
    show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True)
    pause 2.0
    hide splash_warning with Dissolve(0.5, alpha=True)
    $ config.allow_skipping = True
    return

label warningscreen:
    hide intro
    show warning
    pause 3.0

label after_load:
    if persistent.playthrough == 0:
        $ restore_all_characters()
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False
    $ style.say_dialogue = style.normal
    #Check if the save has been tampered with
    if anticheat != persistent.anticheat:
        stop music
        scene black
        "The save file could not be loaded."
        "Are you trying to cheat in a mod made just for me? The perfect girl of your dreams?"
        $ y_name = "Yuri"
        show yuri 1y7 at t11
        if persistent.playername == "":
            y "Shame on you."
        else:
            y "Shame on you [persistent.playername]."
            y "Hope you're happy now"
            y "You can stop playing and find another mod..."
        $ renpy.call("save_and_quit_but_its_abrupt")
        return
    else:
        if persistent.playthrough == 0 and not persistent.first_load and not config.developer:
            $ persistent.first_load = True
            call screen dialog("Hint: You can use the \"Skip\" button to\nfast-forward through text you've already read.", ok_action=Return())
    return



label autoload:
    python:
        # Stuff that's normally done after splash
        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()

        # Fix the game context (normally done when loading save file)
        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

    # Pop the _splashscreen label whichB has _confirm_quit as False and other stuff
    if renpy.get_return_stack():
        $ renpy.pop_call()
    call expression persistent.autoload

label before_main_menu:
    $ config.main_menu_music = audio.t1
    return

label readonly:
    scene black
    "The game cannot be run because you are trying to run it from a read-only location."
    "Please copy the DDLC application to your desktop or other accessible location and try again."
    $ renpy.call("save_and_quit_but_its_abrupt")
    return
