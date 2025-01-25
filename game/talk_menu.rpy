style talkbutton_vbox is vbox
style talkbutton_button is button
style talkbutton_button_text is button_text
define gui.talkbutton_button_width = 120

style talkbutton_vbox:
    xalign 0.5
    ypos 270
    yalign 0.95
    yanchor 0.5

    spacing 0

style talkbutton_button is default:
    properties gui.button_properties("talkbutton_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound
    idle_background "gui/talk_button_idle.png"
    hover_background "gui/talk_button_hover.png"

style talkbutton_button_text is default:
    properties gui.button_text_properties("talkbutton_button")
    xalign 0.5

style talkbutton_button_text is button_text
define gui.distalkbutton_button_width = 120

screen distalkbutton():
    vbox:
        textbutton "nothing.png" action NullAction()

init python:
    def DisableTalk():
        if persistent.talk_visible == None:
            persistent.talk_visible = False
        try:
            config.overlay_screens.remove("talkbutton")
        except:
            pass
        renpy.hide_screen("talkbutton")
        persistent.talk_visible = False
    def EnableTalk():
        if persistent.talk_visible == True:
            persistent.talk_visible = True
        if not persistent.talk_visible:
            config.overlay_screens.append("talkbutton")
            renpy.show_screen("talkbutton")
        else:
            pass
        persistent.talk_visible = True
    def ShowTalk():
        if persistent.talk_visible == None:
            persistent.talk_visible = True
        try:
            config.overlay_screens.append("untalkbutton")
            renpy.show_screen("untalkbutton")
        except:
            pass
        persistent.talk_visible = True
    def HideTalk():
        if persistent.talk_visible == True:
            persistent.talk_visible = False
        try:
            config.overlay_screens.remove("untalkbutton")
        except:
            pass
        renpy.hide_screen("untalkbutton")
        persistent.talk_visible = False


label prompt_menu:
    #Top level menu
    #To make the menu line up right we have to build it up manually
    python:
        allow_dialogue = False
        DisableTalk()
        boopable = False

        talk_menu = []
        if dev_access:
            talk_menu.append((_("Control Panel."), "renpy.jump(\"control_panel\")"))
        talk_menu.append((_("Ask a question."), "call_dialogue(\"pool\", \"actives\")"))
        if "last_compliment_time" in persistent.memory:
            if (datetime.datetime.now() - persistent.memory["last_compliment_time"]) >= datetime.timedelta(seconds = 900): #if it's been less than 15 minutes since last complement
                talk_menu.append((_("Compliment."), "renpy.jump(\"compliment_menu\")"))
                talk_menu.append((_("Antagonize."), "renpy.jump(\"insult_menu\")"))
            else:
                print(datetime.datetime.now() - persistent.memory["last_compliment_time"])
        else:
            talk_menu.append((_("Compliment."), "renpy.jump(\"compliment_menu\")"))
            talk_menu.append((_("Antagonize."), "renpy.jump(\"insult_menu\")"))
        talk_menu.append((_("Sleep."), "renpy.jump('sleepy_yuri')"))
        #talk_menu.append((_("Leave for a bit."), "renpy.jump('AFK_yuri')"))
        talk_menu.append((_("Goodbye."), "call_dialogue(\"pool\", \"farewells\")"))
        talk_menu.append((_("Nevermind."),"renpy.jump('ch30_loop')"))#"_return = None"))

        randomnum = renpy.random.randint(0,6)
        ran_response = [
            _("Hmm?, What is it?"),
            _("Yes, " + str(player) + "?"),
            _("Yes, my love?"),
            _("Hiya."),
            _("What would you like to talk about?"),
            _("Yes, darling?"),
            _("Hmm?")]
        renpy.say(y, ran_response[randomnum], interact=False)
        madechoice = renpy.display_menu(talk_menu)
        exec(madechoice)
    python:
        EnableTalk()
        renpy.jump("ch30_loop")



screen talkbutton():
    if not persistent.HDY and hide_yuri_sit==False:
        vbox xalign 0.03 yalign 0.1:
            style_prefix "talkbutton"
            textbutton "Dreams":
                action Call("talk_slow_no_dismiss", "dream_menu")
    #       null height 10
    #           textbutton "Nightmares":
    #               action Call("talk_slow_no_dismiss", "nightmare_menu")
    #           null height 
            if renpy.android:
                if persistent.lovecheck and persistent.bg != "laboratory":
                    textbutton "Dates":
                        action Call("talk_slow_no_dismiss", "dates_menu")
                textbutton "Music":
                    action Call("talk_slow_no_dismiss", "change_music")
            else:
                if persistent.lovecheck and persistent.bg != "laboratory":
                    textbutton "Dates":
                        action Call("talk_slow_no_dismiss", "dates_menu")
                textbutton "Music":
                    action Call("talk_slow_no_dismiss", "change_music")
                if renpy.seen_label("a_tetris"): #or renpy.seen_label ("chessintro"):
                    textbutton "Games":
                        action Call("talk_slow_no_dismiss", "games_menu")


        vbox xalign 0.50 yalign 0.99:
            style_prefix "talkbutton"
            textbutton "Talk":
                action Call("talk_slow_no_dismiss", "prompt_menu")
    elif hide_yuri_sleep==True:
        $ allow_dialogue = False
        vbox xalign 0.97 yalign 0.99:
            style_prefix "talkbutton"
            textbutton "Wake up":
                action Call("yuriwakeup")

    else:
        vbox xalign 0.50 yalign 0.99:
            #style_prefix "talkbutton"
            textbutton "Change back to Yuri":
                action Call("changeoutfit")



label games_menu:
    $ DisableTalk()
    $ Dream_type = "game"
    $ boopable = False
    $show_chr("A-ABAAA-ALAL")
    y "Up for a game [player]?"
    $show_chr("A-CCAAA-ALAL")
    y "Please take a look at the games I have available for us currently. Do any look appealing to you?"
    menu:
        "Tetris":
            jump tetris
        #"Khet":
        #    jump Khet
        "Chess":
            jump chess
        #"Solitaire":
        #    jump solitaire
        #"Reversi":
        #    jump reversi
        "Nevermind":
            jump ch30_loop

screen untalkbutton():
    vbox xalign 0.03 yalign 0.1:
        style_prefix "talkbutton"
        textbutton "Dreams":
            action NullAction()
#       null height 10
#           textbutton "Nightmares":
#               action NullAction()
#           null height 10
        if persistent.lovecheck:
            textbutton "Dates":
                action NullAction()
        textbutton "Music":
            action NullAction()

    vbox xalign 0.50 yalign 0.99:
        style_prefix "talkbutton"
        if persistent.alpha_save or renpy.seen_label("a_games") or renpy.seen_label("featuregreetings"):
            textbutton "games":
                action NullAction()
            null height 10
            #textbutton "Khet":
            #    action NullAction()
            #null height 10
        textbutton "Talk":
            action NullAction()

label talk_slow_no_dismiss(jumper):
    $slow_nodismiss_copy()
    $renpy.jump(jumper)
