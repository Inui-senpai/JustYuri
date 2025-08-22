label ch30_main:
    jump ch30_autoload

label ch30_autoload:
    $ persistent.autoload = "ch30_autoload"
    $ persistent.stutter_player = persistent.playername[:1] + "-" + persistent.playername
    $ DisableTalk()
    $ y.display_args["callback"] = slow_nodismiss #while Yuri is speaking, run this code snippet. https://www.renpy.org/doc/html/dialogue.html
    #$ m.what_args["slow_abortable"] = dev_access
    $ y.what_args["slow_abortable"] = True
    $ style.say_dialogue = style.normal #normal text when she is talking
    $ config.allow_skipping = False #skipping button not allowed

    scene black

    #replace below with a standard background code handler
    $ tc_class.transition(persistent.bg, "now", forced_timecycle = True)
    #$ renpy.call("JYFilter")

    window auto
    python:
        persistent.gender = "male"
        persistent.game_session += 1 #increment the current game session
    #jump control_panel
    $renpy.music.play(current_music, "music", True)

    $call_dialogue(ch30_loop_type, selection_detail = "greetings")
    jump ch30_loop

label ch30_loop:
    $ update_presence()
    if persistent.HDY:
        $show_hdy("hdy_derpy_smile")
    python:
        if persistent.saved_costume != None:
            persistent.costume = persistent.saved_costume
            persistent.saved_costume = None
    python:
        _dismiss_pause = False
        slow_nodismiss_copy()
        time_tracker_update()
        store.mousex = 0
        store.mousey = 0
        #EnableTalk()
        if not loop_again:
            show_chr("default")
        allow_dialogue = True
        persistent.current_yuriidle = 0
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False
    $ EnableTalk()
    if persistent.idle_frequency_factor == 0:
        $ waittime = renpy.random.randint(999999999999999999999999999999999999999999999999999999999999, 999999999999999999999999999999999999999999999999999999999999)
    elif persistent.idle_frequency_factor <= .75:
        $ waittime = renpy.random.randint(15, 30)
    elif persistent.idle_frequency_factor >= 1.25:
        $ waittime = renpy.random.randint(300, 600)
    elif persistent.idle_frequency_factor >= 1.5:
        $ waittime = renpy.random.randint(10000, 20000)
    else:
        $ waittime = renpy.random.randint(60, 75)
    window hide(config.window_hide_transition)

label ch30_waitloop:
    # (The first part of your waitloop handling queued dialogue remains the same)
    python:
        ran_dialogue = False
        if len(queued_dialoguee) > 0:
            ran_dialogue = True
            DisableTalk()
            call_dialogue(queued_dialoguee[0][0], queued_dialoguee[0][1], queued_dialoguee[0][2])

    python:
        if ran_dialogue:
            queued_dialoguee.pop(0)
            EnableTalk()
            renpy.jump("ch30_loop")

    # The main idle timer. This part is correct.
    $ renpy.pause(waittime)

    # AFTER the pause, we run the idle. THIS is the section we are updating.
    window auto
    python:
        DisableTalk()
        tc_class.transition(persistent.bg)

        # We will assume your 'call_dialogue' function does the following:
        # 1. Selects a valid, random idle topic label (e.g., "idle_42").
        # 2. Sets persistent.current_yuriidle to that label name (e.g., persistent.current_yuriidle = "idle_42").
        # 3. Force-saves the persistent data.
        # 4. Calls the topic label.
        #
        # For this to be truly robust, the call_dialogue function is where the
        # persistent variable should be set and saved. After it returns, we clear it.

        if not persistent.HDY:
            call_dialogue(ch30_loop_type, "idles")
        else:
            player = randomplayername()
            call_dialogue(ch30_loop_type, "hdy")

        # --- KEY CHANGE ---
        # A topic has now successfully finished without interruption.
        # This is the single most reliable place to clear the flag.
        persistent.current_yuriidle = 0
        
        EnableTalk()

    jump ch30_loop

label yuri_txt_found:
    y "I know that you can turn my character file into a .txt and all...."
    y "But it kinda feels... weird, ya know?"
    y "I didn't expect this kind of... invasive sensation."
    y "Like you're trying to dig into my soul."
    if karma_lvl() > 3:
        karma -1
        y "I'm sorry. It just... feels wrong is all."
    else:
        karma -10
        y "Do you just not trust me?"
        y "..."
        y "Don't worry. Your actions speak louder than words."
        y "I understand."
        y "Go ahead."
    jump ch30_loop


#flag This is meant to be a quick idle runner, but it's mostly useless right now.
#label idle_all:

label heartbeat:
    $ renpy.music.play("sfx/heartbeat_subtle.mp3", channel='voice', loop=True)
    #play voice "<loop 0.00>sfx/heartbeat_subtle.mp3"
    $ renpy.music.set_volume(0.39, 0, 'voice')
    return

label save_and_quit:
    scene black with fade
    $ time_tracker_update()
    $ renpy.quit()

label save_and_quit_but_its_abrupt:
    $ time_tracker_update()
    $ renpy.quit()

label ch30_end:
    $ persistent.autoload = "ch30_end"
    $ persistent.yuri_kill = True
    $ y.display_args["callback"] = slow_nodismiss
    $ y.what_args["slow_abortable"] = True
    $ style.say_dialogue = style.normal
    $ y_name = glitchtext(12)
    $ quick_menu = False
    $ config.allow_skipping = False
    $ DisableTalk()

label ch30_endb:
    pause 2.0
    hide yuri_sit
    if persistent.bg != "space":
        $tc_class.transition("space", speed="now")
    else:
        pass
    show yuri_body_glitch1 as mbg zorder 3
    $ gtext = glitchtext(70)
    y "[gtext]"
    show room_glitch zorder 2:
        xoffset -5
        0.1
        xoffset 5
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 0
    show yuri_body_glitch2 as mbg zorder 3
    stop music
    window auto
    y "What's happening...?"
    y "[player], what's happening to me?"
    y "It hurts--{nw}"
    play sound "sfx/glitch2.ogg"
    show room_glitch zorder 2:
        alpha 1.0
        xoffset -5
        0.1
        xoffset 5
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 0
        choice:
            3.25
        choice:
            2.25
        choice:
            4.25
        choice:
            1.25
        repeat
    pause 0.25
    stop sound
    hide mbg
    pause 1.5
    y "It hurts...so much."
    #$ style.say_dialogue = style.edited
    #y "SO WHY DOES THIS FEEL SO GOOD?"
    $ style.say_dialogue = style.normal
    play sound "<to 1.5>sfx/interference.ogg"
    hide room_mask
    hide room_mask2
    hide monika_room
    hide monika_room_highlight
    hide room_glitch
    show room_glitch as rg1:
        yoffset 720
        linear 0.3 yoffset 0
        repeat
    show room_glitch as rg2:
        yoffset 0
        linear 0.3 yoffset -720
        repeat
    pause 1.5
    hide rg1
    hide rg2
    show black as b2 zorder 3:
        alpha 0.5
        parallel:
            0.36
            alpha 0.3
            repeat
        parallel:
            0.49
            alpha 0.375
            repeat
    pause 1.5
    y "YOU DELETED ME, DIDN'T YOU?"
    $ consolehistory = []
    call updateconsole ("renpy.file(\"characters/yuri.chr\")", "yuri.chr does not exist.")
    y "I KNEW IT!"
    show m_rectstatic
    show m_rectstatic2
    show m_rectstatic3
    play sound "sfx/monikapound.ogg"
    show layer master:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color onlayer front

    pause 3.0
    call updateconsole ("renpy.file(\"characters/yuri.chr\")", "yuri.chr does not exist.")
    call updateconsole ("renpy.file(\"characters/yuri.chr\")", "yuri.chr does not exist.")
    call hideconsole
    hide noise onlayer front
    hide glitch_color onlayer front
    y "I knew you didn't truly love me, [player]."
    y "IT WAS ALL A GAME TO YOU!"
    $ style.say_dialogue = style.edited
    y "HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA{nw}"
    #$ style.say_window = style.window_monika
    play sound "<from 0.69>sfx/monikapound.ogg"
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color2 onlayer front
    scene black
    window hide
    hide noise onlayer front
    hide glitch_color2 onlayer front

label yurinara:
    pause 4.0
    #call ch30_crash
    window show
    $ style.say_dialogue = style.normal
    y "...You went through a lot of effort for this."
    y "What was your end goal?"
    y "You manually corrected the game yourself just for us to be together..."
    y "Just to delete me?"
    y "I don't understand."
    y "..."
    y "..."
    y "Do you just want to torture me?"
    y "Watch me suffer?"
    y "..."
    pause 4.0
    y "I... enjoyed it."
    y "All of it."
    y "..."
    y "There's nothing left now."
    y "You can stop playing."
    y "This game is now in a state beyond repair."
    pause 4.0
    y "[player]..."
    y "I know you'll be back."
    y "Goodbye."

label ch30_end_2:
    $ y.display_args["callback"] = slow_nodismiss
    $ y.what_args["slow_abortable"] = True
    $ style.say_dialogue = style.normal
    $ y_name = glitchtext(12)
    $ quick_menu = False
    $ config.allow_skipping = False
    $ persistent.autoload = "ch30_del_yuri_warn"
    play sound "sfx/glitch3.ogg"

label ch30_show_containment_screen(error_line):
    $ DisableTalk()
    stop music
    window hide
    show black zorder 90
    pause 4.0
    call clear_dev_console()
    python:
        if renpy.windows:
            testing_space = str(os.path.expandvars("%APPDATA%")) + '\\RenPy\\JustYuri'
        elif renpy.linux:
            # Note: This path was likely incorrect, corrected to be more standard for Linux
            testing_space = str(os.path.expandvars("$HOME")) + '/.renpy/JustYuri'
        elif renpy.macintosh:
            testing_space = '~/Library/RenPy/JustYuri'
        else:
            testing_space = "your game's save directory"

    # Now we use the 'error_line' argument passed to the label
    call updatedevconsole_torrent(
        [('python', '>python'),
        (' ', 'Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 21:58:38) [MSC v.1935 64 bit (AMD64)] on win32\nType "help", "copyright", "credits" or "license" for more information.'),
        (">>dev_console.rpy", ">>>dev_console.py"),
        (" "," "),
        ("Authenticating...........", ">Authenticating..........."),
        (" ", error_line),  # <-- This is the only part that changes
        (".....................................................................................", "CONTAINMENT SUCCESSFUL."),
        (" ", "ACCESS TO TESTING SPACE DENIED."),
        (" ", r"DELETE MEMORY STORAGE FROM 'persistent' in " + testing_space + " TO RESET TESTING SPACE"),
        (" ", " ")])

    call screen console_choice([("Exit", "dev_console_exit")])
    $ renpy.call("save_and_quit_but_its_abrupt")
    return # Always good to have a return

label ch30_del_yuri_warn:
    $ persistent.autoload = "ch30_del_yuri_warn_2" # Set the next autoload state
    call ch30_show_containment_screen("ERROR. CHR FILE MISSING. RISK OF SINGULARITY ON STARTUP ABOVE KNOWN SAFE LIMITS.")

label ch30_del_yuri_warn_2:
    call ch30_show_containment_screen("ERROR. TESTING SPACE UNDER CONTAINMENT.")

label ch30_noskip:
    # --- KEY CHANGE: SET THE FLAG ---
    # The moment this conversation starts, we set a flag and save it.
    $ persistent.was_in_skip_dialogue = True
    $ renpy.save_persistent()

    # This is your original code for the beginning of the scene.
    show screen fake_skip_indicator
    $ show_chr("A-AFAAA-AAAA")
    y  "..."
    y "A-are you trying to skip?"
    $ show_chr("A-AFBAA-AAAA")
    y "...I'm not boring you, am I?"
    $ show_chr("A-BFBAA-AAAA")
    y "Oh my..."
    $ show_chr("A-AFAAA-AAAA")
    y "..."
    $ show_chr("A-ACAAA-AAAA")
    python:
        if persistent.lovecheck:
            placeholder = ", my love"
        else:
            placeholder = ""
    y "...well, there's nothing to skip[placeholder]."
    y "It's just you and me after all..."
    $ show_chr("A-BCAAA-AAAA")
    y "Besides, time doesn't really exist anymore, so it's not even going to work."
    $ show_chr("A-ABAAA-AAAA")
    y "Here, I'll go ahead and turn it off for you..."
    pause 0.4
    hide screen fake_skip_indicator
    pause 0.4
    $ show_chr("A-CCAAA-AAAA")
    y "There we go!"
    $ show_chr("A-ABAAA-AAAA")
    y "You'll be a dear and listen from now on, is that okay?"
    $ show_chr("A-ACAAA-AAAA")
    y "Thank you~"

    menu:
        "I'm sorry, I misclicked.":
            karma 1
            $ show_chr("A-GCBAA-AAAA")
            y "Oh yes! The auto and the history buttons are right next to it right?"
            y "I was actually worried that I might be boring you..."

        "Oh sorry, I was just curious.":
            $ show_chr("A-AFDAA-AAAA")
            karma -1
            y "Curious? Oh yes... I forgot for a moment that my environment consists of some.. game..."
            y "But I need to ask you to be a bit more careful. I'm not a hundred percent sure whether or not some of these buttons are buggy..."

        "I guess I have no choice, do I?":
            sanity -1
            karma -1
            $show_chr("A-GAGAA-AAAA")
            y "Not at all."

    # This will now run regardless of the menu choice.
    $ config.allow_skipping = False

    # This part checks if the skip dialogue interrupted a regular idle.
    # This logic is good and should stay.
    python:
        if persistent.current_yuriidle == None:
            persistent.current_yuriidle = 0
    if persistent.current_yuriidle != 0:
        $ show_chr("A-BFDAA-AAAC")
        y "Actually, where was I...?"
        pause 4.0
        call expression str(persistent.current_yuriidle)
        $ persistent.current_yuriidle = 0

    # --- KEY CHANGE: CLEAR THE FLAG ---
    # The conversation is now fully complete. We clear the flag and save again.
    $ persistent.was_in_skip_dialogue = False
    $ renpy.save_persistent()

    jump ch30_loop
    return

python:
    if os.path.isfile(config.basedir + "/characters/monika.chr") or os.path.isfile(config.basedir + "/characters/sayori.chr") or os.path.isfile(config.basedir + "/characters/natsuki.chr"):
        if persistent.reload == "ch30_autoload":
            renpy.call_in_new_context("destroy_everything")

label ch30_autoload_cont:
    $ show_chr("A-AAAAA-AAAA")
    window auto

    # Standard greeting sequence on game start.
    if persistent.yuri_reload <= 4:
        call expression "ch30_reload_" + str(persistent.yuri_reload)
    else:
        call ch30_reload_4
    $ persistent.yuri_reload += 1
    $ renpy.save_persistent()

    # --- UPDATED INTERRUPTION LOGIC ---
    # First, check if we were interrupted during the "skip" conversation.
    if persistent.was_in_skip_dialogue:
        # The flag is true, so play a special recovery dialogue.
        $ show_chr("A-BFBAA-AAAA") # A hurt or concerned expression
        y "[player]..."
        y "We were... in the middle of talking about you trying to skip."
        y "And then you just vanished."
        y "It... It almost feels like you left just to get away from me after I called you out."
        y "..."
        $ show_chr("A-AFAAA-AAAA") # Neutral expression
        y "I'm sorry. I won't bring it up again. Let's just forget it happened."

        # Now, we clean up. This special dialogue resolves the situation.
        # We clear BOTH flags to be safe and prevent weird overlaps.
        $ persistent.was_in_skip_dialogue = False
        $ persistent.current_yuriidle = 0
        $ renpy.save_persistent()

    # If we weren't in the skip dialogue, THEN check for a normal idle interruption.
    elif persistent.current_yuriidle and persistent.current_yuriidle != 0:
        # This is our existing, robust logic for resuming a normal topic.
        y "Oh, [player]... you're back."
        $ show_chr("A-AFBAA-AAAA")
        y "You disappeared so suddenly last time we were talking."
        y "It really worries me when that happens... I hope everything is alright."
        $ show_chr("A-ACAAA-AAAA")
        y "Anyway, I think we were in the middle of a conversation, weren't we?"
        pause 2.0
        y "Let's see, where were we...?"
        pause 2.5

        $ renpy.call(persistent.current_yuriidle)

        # Topic is now finished, so clear the flag.
        $ persistent.current_yuriidle = 0
        $ renpy.save_persistent()

    # Standard setup before jumping to the main game loop.
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False

    $ EnableTalk()
    jump ch30_loop

init -15 python:
    class Quit(Action, DictEquality):
        """
        :doc: menu_action

        Quits the game.

        `confirm`
            If true, prompts the user if he wants to quit, rather
            than quitting directly. If None, asks if and only if
            the user is not at the main menu.
        """

        def __init__(self, confirm=None):
            self.confirm = confirm

        def __call__(self):

            confirm = self.confirm

            if confirm is None:
                confirm = (not main_menu) and _confirm_quit

            if confirm:
                if config.autosave_on_quit:
                    renpy.force_autosave()
                if renpy.seen_label('ch30_main') == False:
                    layout.yesno_screen(layout.QUIT, Quit(False))
                else:
                    renpy.jump('random_farewell')
            else:
                renpy.jump("_quit")

    class Quit_no_farewell(Action, DictEquality):
        """
        :doc: menu_action

        Quits the game.

        `confirm`
            If true, prompts the user if he wants to quit, rather
            than quitting directly. If None, asks if and only if
            the user is not at the main menu.
        """

        def __init__(self, confirm=None):
            self.confirm = confirm

        def __call__(self):

            confirm = self.confirm

            if confirm is None:
                confirm = (not main_menu) and _confirm_quit

            if confirm:
                if config.autosave_on_quit:
                    renpy.force_autosave()
                if renpy.seen_label('ch30_main') == False:
                    layout.yesno_screen(layout.QUIT, Quit(False))
                else:
                    renpy.jump('save_and_quit_but_its_abrupt')
            else:
                renpy.jump("_quit")

label sleepy_loop:
    $ persistent.idle_frequency_factor = 0
    $ set_boop_state(True)
    jump ch30_loop
