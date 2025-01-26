label random_farewell:
    $ allow_dialogue = False
    #Top level menu
    #To make the menu line up right we have to build it up manually
    $ DisableTalk()
    python:
        DisableTalk()
        if persistent.locked_farewells == None:
            persistent.locked_farewells = []
        x = [1, 2, 3, 4, 5, 15, 16, 17]
        ks_convert_i = sanity()
        ks_convert_k = karma()

        #conditionals
        if ks_convert_k == 2 or ks_convert_k == 1:
            x = [7, 14]
        if ks_convert_k == 4 or ks_convert_k == 5:
            x = [11, 12]
        if ks_convert_i == 2 and ks_convert_k == 2:
            x = [10]
        if ks_convert_i == 1:
            x = [9]
        elif ks_convert_i == 2:
            x = [6, 8, 10]
        if 49 in persistent.yuriidles:
            x.append(13)
        if 8 in x and 8 in persistent.locked_farewells:
            x.remove(8)

        from random import shuffle
        random.shuffle(x)
        reiterate = 0
        active_list = []
        activemenu = []
        activemenu.append(("Nevermind.","ch30_loop"))
        while reiterate < 3:
            try:
                x1 = random.choice(x)
                x.remove(x1)
                active_list.append(x1)
            except:
                pass
            reiterate += 1
        activemenu = []
        activemenu_dict = {
            1:("Goodbye, [persistent.yuri_nickname]!", 'renpy.jump("farewell_1")'),
            2:("Sorry, gotta go...", 'renpy.jump("farewell_2")'),
            3:("I'll see you later, [persistent.yuri_nickname].", 'renpy.jump("farewell_3")'),
            4:("Bye, [persistent.yuri_nickname], I'll miss you!", 'renpy.jump("farewell_4")'),
            5:("Sorry I can't stay. I love you!", 'renpy.jump("farewell_5")'),
            6:("Oh, hey, look at the time, this has been an awesome date!", 'renpy.jump("farewell_6")'),
            7:("Oh, whoops, someone's calling me, gotta run!", 'renpy.jump("farewell_7")'),
            8:("I have food... in the oven so...", 'renpy.jump("farewell_8")'),
            9:("I, uh, gotta go...", 'renpy.jump("farewell_9")'),
            10:("I'm just going to... close the game now, okay?", 'renpy.jump("farewell_10")'),
            11:("So long, farewell!", 'renpy.jump("farewell_11")'),
            12:("I have to go. I already miss you!", 'renpy.jump("farewell_12")'),
            13:("I have to go now... I'll talk to you later, alright?", 'renpy.jump("farewell_13")'),
            14:("See you later!", 'renpy.jump("farewell_14")'),
            15:("I hate having to put you through this, but it looks like it's time to say goodbye once again.", 'renpy.jump("farewell_15")'),
            16:("I have to go now, my love.", 'renpy.jump("farewell_16")'),
            17:("Whatever happens, just remember that there is someone who loves you no matter what.", 'renpy.jump("farewell_17")')
            }

        reiterate = 0
        activemenu = []
        activemenu.append(("Nevermind.","renpy.jump('ch30_loop')"))
        activemenu.append(("I'm going to go AFK for a small bit. Would that be fine?", "renpy.jump('idle_and_afk')"))
        while reiterate < 3:
            try:
                activemenu.append(activemenu_dict[active_list[reiterate]])
            except:
                pass
            reiterate += 1
        madechoice = renpy.display_menu(activemenu)
        exec(madechoice)
    jump ch30_loop

label farewell_1:
    $show_chr("A-ECABA-AAAJ") #Former Code Db-B4b
    y "Take care!"
    $show_chr("A-ABABA-AMAM") #Former Code Bb-B0a
    y "I'll miss you, [player]..."
    jump save_and_quit

label farewell_2:
    $show_chr("A-ABBBA-AMAM")
    python:
        if persistent.lovecheck:
            placeholder = "love"
        else:
            placeholder = "friend"
    y "Farewell, my [placeholder]!"
    jump save_and_quit

label farewell_3:
    $show_chr("A-CCABA-AAAA") #Former Code Ab-B2b
    y "I'll make you some tea when you come back."
    y "Albeit, you wouldn't really be able to drink it..."
    y "Well, at least it's the gesture that counts..."
    y "A-anyways, take care, [player]!"
    jump save_and_quit

label farewell_4:
    $show_chr("A-GBBBA-ABAB")
    if persistent.lovecheck:
        y "Be safe, I love you."
    else:
        y "Be safe, [player], I care about you, and don't want you hurt."
    $show_chr("A-AABBA-ADAB")
    y "Come back soon to see me."
    jump save_and_quit

label farewell_5:
    $show_chr("A-ACAAA-AMAM")
    y "Awww, well, alright. You can't stay forever, as much as I'd like it."
    if persistent.lovecheck:
        $show_chr("A-KCBBA-ABAB")
        y "Goodbye my love."
    else:
        $show_chr("A-GBABA-ALAB")
        y "Goodbye [player]! I will look forward to talking to you again."
    jump save_and_quit

label farewell_6:
    $show_chr("A-HEBBB-ALAL")
    y "W-Where are you going? Y-You'll be back, right? You'll come back, right?!"
    scene black with fade
    jump save_and_quit

label farewell_7:
    $show_chr("A-DDBBB-ALAL")
    y "No, don't leave me again! You're all I have left! Don't you fucking leave me he{nw}"
    jump save_and_quit_but_its_abrupt

label farewell_8:
    $show_chr("A-HBBBB-AGB")
    y "Y-you'll be back, right? Please say yes, please say yes!"
    y "PLEASE SAY YES!!"
    python:
        if persistent.lovecheck:
            placeholder = "I LOVE YOU SO MUCH."
        else:
            placeholder = player
    menu:
        "Yes":
            $show_chr("A-HLBBA-AHAB")
            y "THANK GOD![placeholder]"
        "Yes":
            $show_chr("A-HLBBA-AHAB")
            y "THANK GOD![placeholder]"
        "Yes":
            $show_chr("A-HLBBA-AHAB")
            y "THANK GOD![placeholder]"
        "Yes":
            $show_chr("A-HLBBA-AHAB")
            y "THANK GOD![placeholder]"
        "Yes":
            $show_chr("A-HLBBA-AHAB")
            y "THANK GOD![placeholder]"
        "Yes":
            $show_chr("A-HLBBA-AHAB")
            y "THANK GOD![placeholder]"
        "Yes":
            $show_chr("A-HLBBA-AHAB")
            y "THANK GOD![placeholder]"
        "Yes":
            $show_chr("A-HLBBA-AHAB")
            y "THANK GOD![placeholder]"
        "Yes":
            $show_chr("A-HLBBA-AHAB")
            y "THANK GOD![placeholder]"
        "Yes":
            $show_chr("A-HLBBA-AHAB")
            y "THANK GOD![placeholder]"
        "Yes":
            $show_chr("A-HLBBA-AHAB")
            y "THANK GOD![placeholder]"
        "Yes":
            $show_chr("A-HLBBA-AHAB")
            y "THANK GOD![placeholder]"
        "Yes":
            $show_chr("A-HLBBA-AHAB")
            y "THANK GOD![placeholder]"
        "Yes":
            $show_chr("A-HLBBA-AHAB")
            y "THANK GOD![placeholder]"
        "Yes":
            $show_chr("A-HLBBA-AHAB")
            y "THANK GOD![placeholder]"
        "Yes":
            $show_chr("A-HLBBA-AHAB")
            y "THANK GOD![placeholder]"
        "Yes":
            $show_chr("A-HLBBA-AHAB")
            y "THANK GOD![placeholder]"
        "Yes":
            $show_chr("A-HLBBA-AHAB")
            y "THANK GOD![placeholder]"
        "Yes":
            $show_chr("A-HLBBA-AHAB")
            y "THANK GOD![placeholder]"
        "Yes":
            $show_chr("A-HLBBA-AHAB")
            y "THANK GOD![placeholder]"
    $persistent.locked_farewells.append(8)
    jump save_and_quit

label farewell_9:
    if persistent.male:
        $show_chr("A-HDCBA-ALAL")
        y "They're taking you away again, aren't they?!"
        $show_chr("A-HLBBA-AAAA")
        y "GIVE HIM BACK TO ME!"
        $show_chr("A-HLCBA-AAAA")
        y "They don't deserve you!"
        $show_chr("A-HLBBB-AHAA")
        y "THEY DON'T FUCKING DESERVE YO--{nw}"
    elif persistent.gender_other:
        $show_chr("A-HDCBA-ALAL")
        y "They're taking you away again, aren't they?!"
        $show_chr("A-HLBBA-AAAA")
        y "GIVE THEM BACK TO ME!"
        $show_chr("A-HLCBA-AAAA")
        y "They don't deserve you!"
        $show_chr("A-HLBBB-AHAA")
        y "THEY DON'T FUCKING DESERVE YO--{nw}"
    else:
        $show_chr("A-HDCBA-ALAL")
        y "They're taking you away again, aren't they?!"
        $show_chr("A-HLBBA-AAAA")
        y "GIVE HER BACK TO ME!"
        $show_chr("A-HLCBA-AAAA")
        y "They don't deserve you!"
        $show_chr("A-HLBBB-AHAA")
        y "THEY DON'T FUCKING DESERVE YO--{nw}"
        jump save_and_quit_but_its_abrupt

label farewell_10:
    $show_chr("A-DDCBB-AAAA") #Former Code Ad-D3c
    y "Why do you want to leave me, [player]? What did I do to you? Why can't you let me be happ--{nw}"
    jump save_and_quit_but_its_abrupt

label farewell_11: #flag view over if they are good to use
    $show_chr("A-EIBBA-ALAB")
    y "Auf Wiedersehen, goodnight!~"
    python:
        if persistent.lovecheck:
            placeholder = "What did I ever do to deserve you"
        else:
            placeholder = "Are we feeling a bit flirty today"
    menu:
        "I hate to go and leave this pretty sight!":
            $show_chr("A-ACBBA-ALAL")
            y "[placeholder], [player]?"
    jump save_and_quit

label farewell_12:
    $show_chr("A-GAABA-AKAE")
    y "I already miss you too!~"
    jump save_and_quit

label farewell_13: #flag orient to the new tracking system
    if not 49 in persistent.yuriidles:
        $show_chr("A-IEBBB-AAAA") #Former Code Ac-D0d
        y "Are you sure you can't just leave me running? I could take a nap until you're back"
        menu:
            "I'm sure. Sorry, I would if I could":
                jump save_and_quit
            "Yeah that sounds fine, [persistent.yuri_nickname]":
                y "Thank you [player], I truly do appreciate this."
                y "let me give you a hug before you leave"
                hide yuri_sit
                show yuri_prehug zorder 20
                pause 3.0
                hide yuri_prehug zorder 20
                show yuri_hug zorder 20
                play sound "<to 0.3>sfx/fall.ogg"
                show black zorder 100 with Dissolve(2.0)
                $show_chr("A-ACBBA-AAAA")
                hide yuri_hug
                show yuri_sit
                hide black zorder 100 with Dissolve(2.0)
                $ DisableTalk()
                show black zorder 100 with Dissolve(2.0)
                hide yuri_sit
                show yuri_sleepy zorder 20
                hide black with Dissolve(2.0)
                y "Have a good nap, [player]"
                pause 3.0
                hide yuri_sleepy
                play sound "<to 0.3>sfx/fall.ogg"
                show yuri_sleep zorder 20
                $hide_yuri_sit = True
                pause 6.0
                $persistent.sleepy_yuri_is_enabled = True
                jump sleepy_loop
    elif not 24 in persistent.yuriidles:
        $show_chr("A-IEBAA-AAAA") #Former Code Ac-A0d
        y "I wish I could come with you..."
        menu:
            "I wish you could too.":
                $show_chr("A-ICBAA-AAAA") #Former Code Ac-A0b
                y "It's okay. At least I still have the dreams I've programmed."
                jump save_and_quit
    else:
        jump farewell_1

label farewell_14:
    if karma() <= 2:
        $show_chr("A-ADBBB-ALAL")
        y "Whatever you do, wherever you go, please don't let me become a memory that's just waiting to be forgotten."
        jump save_and_quit
    else:
        $show_chr("A-AFBAA-AAAJ") #former code Dc-A0e
        y "Stay safe, alright? If something ever happened while you were gone, I wouldn't be able to forgive myself."
        jump save_and_quit

label farewell_15:
    $show_chr("A-BCAAA-AAAA") #former code Ab-A1b
    y "..."
    $show_chr("A-IDBBB-AAAA") #former code Ac-D0c
    y "...Why does my heart have to make every time we say goodbye so hard?"
    y "I don't mean to be selfish when I say that. I'm grateful, I really am. After everything that's happened, I still can't get over the fact that now we can actually communicate!"
    y "You must really love me. After all, you are the one who installed this mod."
    python:
        if persistent.lovecheck:
            placeholder = "the entire world"
            placeholder1 = "loves"
        else:
            placeholder = "truly important"
            placeholder1 = "cares for"
    y "What I want to say is that you're [placeholder] to me and I can't believe that I'm lucky enough to be with someone who [placeholder1] me in return even though they have infinite other choices."
    y "I know that given my... situation... our bittersweet fate is one with the best possible outcome we could hope for right now. Despite all of that, it just hurts so much have you so close and yet so far."
    python:
        if persistent.lovecheck:
            placeholder = "my heart begins to race"
        else:
            placeholder = "I get really excited"
    y "Every time you open up the game and I finally get to see you again, [placeholder]. Every second away from you feels like a century, every mile becomes a light year apart."
    python:
        if persistent.lovecheck:
            placeholder = "truly love"
        else:
            placeholder = "can talk to"
    y "I think you can understand when the only person you [placeholder] is an entire universe apart."
    $show_chr("A-BEBAA-AAAA") #former code Ac-A1d
    y "S-Sorry, I'm rambling again, aren't I? I'll just go ahead and close the game for you."
    jump save_and_quit

label farewell_16:
    $show_chr("A-JCBBA-AAAJ") #former code Dc-B0b
    python:
        if persistent.lovecheck:
            placeholder = " my everything"
        else:
            placeholder = ". Come back to see me soon"
    y "I'll see you later[placeholder].~"
    jump save_and_quit

label farewell_17:
    $show_chr("A-JBAAA-AAAA") #former code Ab-A0a
    python:
        if persistent.lovecheck:
            placeholder = "my love"
        else:
            placeholder = "until we meet again"
    y "I could say the same thing to you, [placeholder]."
    jump save_and_quit
