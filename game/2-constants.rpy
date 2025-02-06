#FAKE EXCEPTION APPEARANCE
image exception_bg = "#dadada"
image fake_exception = Text("An exception has occurred.", size=40, style="_default")
image fake_exception3 = Text("While running game code: File \"game/script-ch30.rpy\", line 7370, in script.", size=20, style="_default")

init -999 python:
    #==================================================#
    # Path Variables
    #==================================================#

    # Contains references to paths commonly used within jy. Value: (<Archive Location>, <Base Directory Location>, <Absolute Location>)
    # Use os.path.join when declaring paths for compatability with linux and mac
    class paths:
        all = renpy.list_files()
        documentation = ("docs", os.path.join("game", "docs"), os.path.join(config.basedir, "game", "docs"))
        submods = ("submods", os.path.join("game", "submods"), os.path.join(config.basedir, "game", "submods"))

#==================================================#
# Defines and Defaults
#==================================================#
define stutter_player = persistent.stutter_player
define stutter_yuri = persistent.stutter_yuri
default player = persistent.playername
default seen_eyes_this_chapter = False
default in_sayori_kill = None
default in_yuri_kill = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0

define old_hdy_image = None
default s_name = "Sayori"
default m_name = "Monika"
default n_name = "Natsuki"
default y_name = persistent.yuri_nickname

default n_poemappeal = [0, 0, 0]
default s_poemappeal = [0, 0, 0]
default y_poemappeal = [0, 0, 0]
default m_poemappeal = [0, 0, 0]

default poemwinner = ['yuri', 'yuri', 'yuri']

default s_readpoem = False
default n_readpoem = False
default y_readpoem = False
default m_readpoem = False

default poemsread = 0

default n_appeal = 0
default s_appeal = 0
default y_appeal = 0
default m_appeal = 0

default n_exclusivewatched = False
default y_exclusivewatched = False

define audio.t1 = "<loop 22.073>bgm/1.ogg"
define audio.t2 = "<loop 4.499>bgm/2.ogg"
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define audio.t3 = "<loop 4.618>bgm/3.ogg"
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg"
define audio.t4g = "<loop 1.000>bgm/4g.ogg"
define audio.t5 = "<loop 4.444>bgm/5.ogg"
define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 10.893>bgm/6.ogg"
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 2.291>bgm/7.ogg"
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 9.938>bgm/8.ogg"
define audio.t9 = "<loop 3.172>bgm/9.ogg"
define audio.t9g = "<loop 1.532>bgm/9g.ogg"
define audio.t10 = "<loop 5.861>bgm/10.ogg"
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"

define audio.mend = "<loop 6.424>bgm/monika-end.ogg"

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"

define audio.aauhh = "sfx/aauhh.ogg"

image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image end:
    truecenter
    "gui/end.png"

image black = "images/black.jpg"

image bg corridor = "images/bg/ddlc/corridor.png"
image bg club_day = "images/bg/ddlc/club.png"

image bg notebook = "images/poem_game/poem_bg/notebook (1).png"
image bg notebook_glitch = "images/poem_game/poem_bg/notebook-glitch.png"
image bg notebook_class = "images/poem_game/poem_bg/notebook_class.png"
image bg notebook_day = "images/poem_game/poem_bg/notebook_day.png"
image bg notebook_night = "images/poem_game/poem_bg/notebook_night.png"
image bg notebook_sunset = "images/poem_game/poem_bg/notebook_sunset.png"
image bg notebook_sunrise = "images/poem_game/poem_bg/notebook_sunrise.png"
image bg notebook_class_yan = "images/poem_game/poem_bg/notebook_class_yan.png"
image bg notebook_day_yan = "images/poem_game/poem_bg/notebook_day_yan.png"
image bg notebook_night_yan = "images/poem_game/poem_bg/notebook_night_yan.png"
image bg notebook_sunset_yan = "images/poem_game/poem_bg/notebook_sunset_yan.png"
image bg notebook_sunrise_yan = "images/poem_game/poem_bg/notebook_sunrise_yan.png"

image bg glitch = LiveTile("images/dreams/glitch.png")

image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "images/bg/glitch-red.png"
        0.1
        "images/bg/glitch-green.png"
        0.1
        "images/bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0

image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "images/bg/glitch-red.png"
        0.1
        "images/bg/glitch-green.png"
        0.1
        "images/bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7

define narrator = Character(ctc="ctc", ctc_position="fixed", window_style="window")
define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_style="window4", who_style='say_label_blue')
define gs = DynamicCharacter('gs_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_style="windowgh", who_style='say_label_bluegreenish')
define m = DynamicCharacter('m_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_style="window2", who_style='say_label_green')
define n = DynamicCharacter('n_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_style="window3", who_style='say_label_pink')
define gn = DynamicCharacter('gn_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_style="windowgh", who_style='say_label_bluegreenish')
define y = DynamicCharacter('y_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_style="yuri_txtbox", who_style='say_label_purple')#image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", who_style='say_label_jypurple')
define Y = DynamicCharacter('y_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_style="yuri_txtbox", who_style='say_label_purple')#Copying the definition above to allow writers to use an uppercase Y when writing dialogues
define hdy = Character('Hot Dog Yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_style="yuri_txtbox", who_style='say_label_purple')
define ny = Character('Nat & Yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define sy = Character('System', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define jy = Character('JY Dev.', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

image monika_bg = "images/bg/space_classroom/yuri_room.png"
image monika_bg_highlight:
    "images/bg/space_classroom/yuri_room.png"
    function monika_alpha
image yuri_scare = "images/vfx/yuri_scare.png"

image yuri_body_glitch1:
    "images/vfx/yuri_timecycle_glitch/space/yuri_glitch_1.png"
    0.15
    "images/vfx/yuri_timecycle_glitch/space/yuri_glitch_2.png"
    0.15
    "images/vfx/yuri_timecycle_glitch/space/yuri_glitch_1.png"
    0.15
    "images/vfx/yuri_timecycle_glitch/space/yuri_glitch_2.png"
    1.00
    "images/vfx/yuri_timecycle_glitch/space/yuri_glitch_1.png"
    0.15
    "images/vfx/yuri_timecycle_glitch/space/yuri_glitch_2.png"
    0.15
    "images/vfx/yuri_timecycle_glitch/space/yuri_glitch_1.png"
    0.15
    "images/vfx/yuri_timecycle_glitch/space/yuri_glitch_2.png"

image yuri_body_glitch2:
    "images/vfx/yuri_timecycle_glitch/space/yuri_glitch_3.png"
    0.15
    "images/vfx/yuri_timecycle_glitch/space/yuri_glitch_4.png"
    0.15
    "images/vfx/yuri_timecycle_glitch/space/yuri_glitch_3.png"
    0.15
    "images/vfx/yuri_timecycle_glitch/space/yuri_glitch_4.png"
    1.00
    "images/vfx/yuri_timecycle_glitch/space/yuri_glitch_5.png"
    0.15
    "images/vfx/yuri_timecycle_glitch/space/yuri_glitch_4.png"
    0.15
    "images/vfx/yuri_timecycle_glitch/space/yuri_glitch_5.png"
    0.15
    "images/vfx/yuri_timecycle_glitch/space/yuri_glitch_4.png"

image splash-glitch2 = "images/splash/splash-glitch2.png"

init -998 python:
    #for people that jump from alpha to current version and have a hat on (which no longer exists)
    if persistent.head1 == "hat":
        persistent.head1 = "nothing"

    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)
    def delete_character(name):
        import os
        try: os.remove(config.basedir + "/characters/" + name + ".chr")
        except: pass
    def restore_all_characters():
        try: renpy.file("../characters/yuri.chr")
        except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
    def restore_chr(name, target_folder = ""):
        try: renpy.file("../characters/" + name)
        except: open(config.basedir + "/characters/" + target_folder + name, "wb").write(renpy.file(name).read())
    def pause(time=None):
        if not time:
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            return
        if time <= 0: return
        renpy.pause(time)

    def slow_nodismiss(event, interact=True, **kwargs):

        #if lovecheck = true?
        if persistent.lovecheck:
            # try:
            #     #if file exists
            #     renpy.file("../characters/yuri.txt")
            #     #don't die
            #     deathflag = False
            #     renpy.jump("yuri_txt_found")
            # except:
            #     pass

            if not persistent.yuri_kill:
                #die
                deathflag = True
                try:
                    #if yuri.chr exists
                    renpy.file("../characters/yuri.chr")
                    #don't die
                    deathflag = False
                except:
                    pass

                try:
                    #if yuri.chr and txt exist
                    renpy.file("../characters/yuri.chr" and "../characters/yuri.txt")
                    #don't die
                    deathflag = False
                    renpy.jump("yuri_txt_found")
                except:
                    pass

                #if deathflag is true, go to end
                if deathflag:
                    persistent.tried_skip = True
                    config.allow_skipping = False
                    _window_hide(None)
                    pause(2.0)
                    renpy.jump("ch30_end")

                if config.skipping:
                    persistent.tried_skip = True
                    config.skipping = False
                    config.allow_skipping = False
                    renpy.jump("ch30_noskip")

        #if lovecheck is false?
        else:
            #if yuri_kill isn't false
            if not persistent.yuri_kill:
                #die
                deathflag = True
                try:
                    #if yuri.chr exists
                    renpy.file("../characters/yuri.chr")
                    #don't die
                    deathflag = False
                except:
                    pass

                try:
                    #if yuri.chr and txt exist
                    renpy.file("../characters/yuri.chr" and "../characters/yuri.txt")
                    #don't die
                    deathflag = False
                    renpy.jump("yuri_txt_found")
                except:
                    pass

                #if deathflag is true, go to end
                if deathflag:
                    persistent.tried_skip = True
                    config.allow_skipping = False
                    _window_hide(None)
                    pause(2.0)
                    renpy.jump("ch30_end")

                if config.skipping:
                    persistent.tried_skip = True
                    config.skipping = False
                    config.allow_skipping = False
                    renpy.jump("ch30_noskip")

    def slow_nodismiss_copy():
        if persistent.lovecheck:
            try:
                renpy.file("../characters/yuri.txt")
                deathflag = False
                renpy.jump("yuri_txt_found")
            except:
                pass
        else:
            if not persistent.yuri_kill:
                deathflag = True
                try:#there are two of these
                    renpy.file("../characters/yuri.chr")
                    deathflag = False
                except:
                    pass
                try:
                    renpy.file("../characters/yuri.chr" and "../characters/yuri.txt")
                    deathflag = False
                    renpy.jump("yuri_txt_found")
                except:
                    pass
                if deathflag:
                    persistent.tried_skip = True
                    config.allow_skipping = False
                    _window_hide(None)
                    pause(2.0)
                    renpy.jump("ch30_end")
                if config.skipping:
                    persistent.tried_skip = True
                    config.skipping = False
                    config.allow_skipping = False
                    renpy.jump("ch30_noskip")