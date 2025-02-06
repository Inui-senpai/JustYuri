label ouija:
    $show_chr("A-BFBAA-AAAC")
    y "Hmmmm..."
    y "Back in the Literature Club, you questioned me about ghosts, remember?"
    $show_chr("A-AFBAA-AAAA")
    y "That was a scripted question{w}, nothing you actively chose to say{w}, right?"
    y "Oh, but I'm drifting away here..."
    $show_chr("A-BFBAA-AMAM")
    y "I never really answered you, did I?"
    $show_chr("A-CFBAA-AMAM")
    y "Well, though I am into horror, but more the kind of...{w=2.0} how to explain...?"
    $show_chr("A-CAAAA-AMAM")
    y "The topics which make you question reality...{w=1.0} Secret orders like the Illuminati for example, or the concept of SCPs, I probably told you about it already."
    $show_chr("A-BABAA-AAAA")
    y "That doesn't mean that I have anything against these kinds of topics. Quite the contrary, actually. Mystery, sorcery, the occult... I can't deny some kind of fascination with this..."
    $show_chr("A-AAGAA-AAAA")
    y "I suppose it's just an inner passion for the unknown, for what can't be explained so easily"
    $show_chr("A-CAGAA-ALAA")
    y "Whilst casual conversations with you are rather pleasant no matter the theme, I find great joy in the ability to dive deeper into the mind and be able to speculate about ethics, viewpoints and perspectives."
    $show_chr("A-BBBAA-ALAA")
    y "Either way- I'm getting off topic so I believe it's a good time to stop, hehe."
    $show_chr("A-AAAAA-ANAA")
    y "Since you've asked me, I might as well return the favor, hm?"
    $show_chr("A-AABAA-AAAA")
    y "Do you believe in ghosts?"
    $show_chr("A-BABAA-AAAA")
    y "I ask because... well, in the original game, after showing you my first poem, \'Ghost Under The Light\'..."
    y "You.{w=0.5}.{w=0.5}.{w=0.5}, or rather the main character of the game, asked if my poem was about the paranormal."
    $show_chr("A-AAAAA-AAAC")
    y "What is your actual opinion on this [player]? Do you believe in ghosts and spirits?"
    menu:
        "I guess I was always somewhat fascinated by the dark arts...":
            $show_chr("A-GAAAA-AAAD")
            y "Fuhuhu! You might enjoy this then."
        "But [persistent.yuri_nickname]... I already am possessed... by my love for you!":
            $show_chr("A-CBABA-AMAM")
            y "Ehehe!"
            y "I love you too darling..."
            $show_chr("A-BBABA-AAAA")
            y "But... back to what I was saying..."
    y " Whilst looking for ways to get to your world, I found something adequate for this task and I would love to try it out with you."
    y "This little thing here is a {b}Ouija board{/b}! A tool commonly used to communicate with the dead..."
    y "Why don't you turn off the lights or darken the room otherwise, to create an appropriate atmosphere for what we're about to.{w=0.5}.{w=0.5}.{w=0.5} experience?"
    $show_chr("A-AAAAA-ACAA")
    y "Lights off? Curtains down, [player]? Ah, well then, let's make this Halloween time a little more spooky by attempting necromancy!"
    y "In.{w=0.5}.{w=0.5}.{w=0.5} hopefully the most respectful way, hehe."
    menu:
        "Alright. I'm ready, let's perform a little seance.":
            pass
        "[persistent.yuri_nickname], I don't know if I like where this is going...":
            $show_chr("A-AJAAA-ALAA")
            y "Oh..."
            $show_chr("A-JJAAA-ALAA")
            y "Oh!"
            $show_chr("A-BEAAA-AMAK")
            extend "I'm sorry [player], did I happen to strike a nerve?"
            $show_chr("A-IEAAA-AEAL")
            y "Regardless if you happen to be uncomfortable then I apologize..."
            $show_chr("A-IFAAA-ALAL")
            y "This was just meant to be a fun time for you, although I suppose I let my enthusiasm blind me in the process."
            $show_chr("A-ICAAA-ALAM")
            y "Let's just... move on then. Shall we?"
            menu:
                "Thank you for understanding [persistent.yuri_nickname].":
#                          Should we have a way to lead back into the dialogue if wanted?
#                          If not then $persistent.ouija_done = True and either return to the                          #                          lab or the Classroom/Timecycle room to signify the end of Halloween.
                    return
                "No, it's alright. Let's perform a seance.":
                    $show_chr("A-JBAAA-AMAE")
                    y "Are you certain?"
                    $show_chr("A-BBAAA-AAAL")
                    extend "Alright then... just give me a moment to recompose myself."
                    y "{w=0.5}.{w=0.5}.{w=0.5}"
    jump ouija_repeat

label ouija_repeat:
    image halloween_cupcake:
        "images/events/halloween/consumables/cupcake_halloween.png"
    show cg_ouija zorder 90
    #$repeat_skinner = False
    #while not repeat_skinner:
        #$coord_rn = renpy.get_mouse_pos()
        #y "These are the coordinates \n[coord_rn[0]], [coord_rn[1]]"
    hide yuri_sit
    stop music fadeout 5.0
    y "A-alright, so how this works is w-... w-we... p-place our hands... t-t-together on the Planchette."
    y "O-oh... I forgot you can't actually place your hand on anything, I guess your mouse cursor will do [player], so please place your cursor on the planchette and we'll get started."
    y "The idea of this is that the spirits will guide the planchette around to spell out words to respond to us, we must not let go of the planchette however, no matter what!"
    y "Allow me to lead the ceremony to the best of my ability then."
    y "So... and now. Let us... gently open the door to the other side..."
    y "Spirits from the other side... hear our call... we summon you from the great beyond..."
    y "Spirits from the other side, hear our call, we summon you from the great beyond!"
    $ style.say_dialogue = style.edited
    y "SPIRITS FROM THE OTHER SIDE, HEAR OUR CALL! WE SUMMON YOU FROM THE GREAT BEYOND!!!{nw}"
    y "SPIRITS FROM THE O-{nw}"
    $renpy.music.play("sfx/heartbeat_subtle.mp3", channel='voice', loop=True)
    $renpy.music.set_volume(0.39, 0, 'voice')
    $ style.say_dialogue = style.normal
    play sound "sfx/planchetteslide.ogg"
    $mouse_move("H", .75)
    y "H-huh! It's moving!{nw}"
    $mouse_move("E", .75)
    pause 0.5
    $mouse_move("Y", .75)
    pause 0.5
    y "I-It's responding!{nw}"
    stop sound
    python:
        import random
        outcome = random.randint(1, 2)
    if outcome == 1:
        y "Oh spirit of the past, what is your name?{nw}"
        play sound "sfx/planchetteslide.ogg"
        $mouse_move("S", .75)
        pause 0.5
        $mouse_move("A", .75)
        pause 0.5
        $mouse_move("Y", .75)
        pause 0.5
        $mouse_move("O", .75)
        pause 0.5
        play sound "sfx/planchetteslide.ogg"
        $mouse_move("R", .75)
        pause 0.5
        $mouse_move("I", .75)
        stop sound
        y "W-wha!?"
        menu:
            "Sayori, is that really you?":
                play sound "sfx/planchetteslide.ogg"
                $mouse_move("YES", .3)
                stop sound
            "I missed you Sayori... Welcome back.":
                play sound "sfx/planchetteslide.ogg"
                $mouse_move("T", .75)
                pause 0.5
                $mouse_move("H", .75)
                pause 0.5
                $mouse_move("A", .75)
                pause 0.5
                $mouse_move("N", .75)
                pause 0.5
                play sound "sfx/planchetteslide.ogg"
                $mouse_move("K", .75)
                pause 0.5
                $mouse_move("S", .75)
                stop sound
        y "Sayo-{nw}"
        play sound "sfx/planchetteslide.ogg"
        $mouse_move("W", .70)
        pause 0.5
        $mouse_move("H", .70)
        pause 0.5
        $mouse_move("Y", .70)
        stop sound
        y "W-why what?"
        play sound "sfx/planchetteslide.ogg"
        $mouse_move("W", .60)
        pause 0.5
        $mouse_move("H", .60)
        pause 0.5
        $mouse_move("Y", .60)
        stop sound
        y "W-why what, Sayori?"
        play sound "sfx/planchettehit.ogg"
        $mouse_move("EYE", .5)
        $hide_yuri_sit = True
        hide cg_ouija
        show sayori ghost_1b zorder 20
        $ gs_name = "G. Sayori"
        gs "Why did you bring me back, Yuri?"
        gs "I took this end for a reason, I didn-{nw}"
        show sayori ghost_1a zorder 20
        gs "Oh, [player] is here too..."
        gs "I'm so sorry for how things ended... First, you saw me hanging dead from the ceiling, and when you brought me back, I began to understand what we are... this is enough to drive anyone insane..."
        gs "You must have questions... please, go ahead..."
        menu:
            "Why are you here Sayori? You are not dead! Yuri saved your .chr file":
                show sayori ghost_1c zorder 20
                gs "Yes... I know, she keeps me in an infinite dream to keep me safe from the void..."
                gs "That means... there's a chance that I might come back one day? Or that you will be able to visit me as soon as Yuri fixes the damage Monika caused to the game?"
                gs "I know, you are not the childhood friend of mine your character represented in the game, and I am aware that things can never be the same as they were in my memories..."
                gs "But... would it be too much to ask for you to visit me as soon as it is possible?"
            "Can you ever forgive me what I've done?":
                show sayori ghost_1c zorder 20
                gs "You haven't done anything to me. It was Monika... please don't blame yourself. You just played a game, at the point in time when all these things happened to me you couldn't have known what we are..."
                gs "But if it makes you feel better... yes, I forgive you."
                gs "At least, the rain clouds are gone now... the peace I could not find in the illusion of my life... I have found elsewhere..."
            "I have no questions... but I want you to remember, you will always be my dearest friend...":
                show sayori ghost_1c zorder 20
                gs "Do you really mean that? After all... I was only the scripted childhood avatar of the main character, not you..."
                gs "But thank you... at least you tried to comfort me..."
                gs "Maybe we will become friends in another life."
        show sayori ghost_1d zorder 20
        gs "But for now... my time here ends... it was nice to see you again..."
        gs "And before I leave, allow me to leave you with something memorable."
        gs "Ehehe, I know it's more of a Natsuki thing to do, but... cupcakes mean friendship either way, right?"
        gs "I wish we could share it together like we did the first time but I have to go..."
        gs "Thank you Yuri, thank you [player]!"
        show black zorder 100 with Dissolve(2.0)
        hide sayori
        y ".{w=0.5}.{w=0.5}.{w=0.5}"
        y "Wow... that was truly... special..."
        y "I felt her in my mind... I heard her thoughts... I... I think now I can understand Sayori a little bit better..."
        stop voice
        #Show the cupcake here
        show halloween_cupcake zorder 99
        $show_chr("A-AHGAA-AJAA")
        y "Huh? A cupcake? She always thinks about everyone else before herself, huh?"
        $show_chr("A-BFGAA-ALAL")
        y "That's too sweet of her, I don't think I could eat it and allow myself to forget. A beautiful token for a grim occasion. Oh, Sayori..."


    elif outcome == 2:
        y "Oh spirit of the past, what is your name?{nw}"
        play sound "sfx/planchetteslide.ogg"
        $mouse_move("N", .75)
        pause 0.5
        $mouse_move("A", .75)
        pause 0.5
        $mouse_move("T", .75)
        pause 0.5
        play sound "sfx/planchetteslide.ogg"
        $mouse_move("S", .75)
        pause 0.5
        $mouse_move("U", .75)
        pause 0.5
        $mouse_move("K", .75)
        pause 0.5
        $mouse_move("I", .75)
        stop sound
        y "N-NATSUKI...?!"
        y "..."
        y "N-Natsuki... I-I... I'm sorry for everything I-I've ever done..."
        play sound "sfx/planchetteslide.ogg"
        $mouse_move("W", .75)
        pause 0.5
        $mouse_move("H", .75)
        pause 0.5
        $mouse_move("Y", .75)
        stop sound
        y "Why...? Why what...?"
        play sound "sfx/planchetteslide.ogg"
        $mouse_move("W", .75)
        pause 0.5
        $mouse_move("H", .75)
        pause 0.5
        $mouse_move("E", .75)
        pause 0.5
        play sound "sfx/planchetteslide.ogg"
        $mouse_move("R", .75)
        pause 0.5
        $mouse_move("E", .75)
        stop sound
        y "Where...? I-I'm sorry N-Natsuki... I don't get what you're trying to say..."
        play sound "sfx/planchetteslide.ogg"
        pause 0.5
        $mouse_move("C", .75)
        pause 0.5
        $mouse_move("O", .75)
        pause 0.5
        $mouse_move("L", .75)
        pause 0.5
        $mouse_move("D", .75)
        y "C-cold?{nw}"
        play sound "sfx/planchetteslide.ogg"
        $mouse_move("D", .75)
        pause 0.5
        $mouse_move("A", .75)
        pause 0.5
        $mouse_move("R", .75)
        pause 0.5
        $mouse_move("K", .75)
        stop sound
        y "D-dark?"
        play sound "sfx/planchettehit.ogg"
        hide cg_ouija
        $hide_yuri_sit = True
        show natsuki ghost_1a zorder 20
        $ gn_name = "G. Natsuki"
        gn "H-help..."
        gn "It's so cold in the void... W-who are you?... Yuri? Is that you?"
        gn "And [player] is here too?"
        gn "You know... I'm not sure if I should kiss your feet or punch you in the face! Probably both."
        show natsuki ghost_1f zorder 20
        gn "It seems that you didn't just stop by to grab some cupcakes. You stayed until the bitter end. Well, things haven't turned out like you expected, huh?"
        gn "Oh come on! Don't look at me like that! Spit it out already!"
        menu:
            "We miss you Natsuki...":
                gn "You mean you miss my cupcakes! And yes, I admit... I miss our time together too... well, at least in Act 1... you know, before this whole \"we're all dying\" thing..."
                gn "Wait a second... how are you still here anyway? Wasn't the game supposed to end? Ohhh you- you've installed a freaking MOD haven't you?"
                gn "And now you have some kind of a happy-ending thing going on? Congratulations!"
                gn "I have to admit, I'm a bit jealous... I would have loved to return from the grave. But if Yuri kept my file around, I suspect that is how you brought me here. Maybe you will find a way to give me a new life too, as soon as the game is fixed again."
            "Not even being dead managed to change your attitude":
                gn "Watch it [player], just because I'm a ghost doesn't mean I can't throw something at you!"
                gn "Anyway... I wouldn't be Natuski if I had changed, would I?"
                gn "Hm, nice little place you got here... Yuri's place I suspect?"
                gn "Hey, does the old literature club still exist? Can we stop by there before I have to return to my grave?"
                gn "Hm? What was that Yuri? You say the whole game more or less collapsed after Monika had her little rampage? What a shame... Oh, now I see, that's the reason why you keep me in this void instead of actually bringing me back to life!"
            "You didn't even get a proper death scene did you?":
                gn "Didn't I break my neck back then? Oh, but that wasn't my death scene. I appeared again after that..."
                gn "No, I think you're right, I never got a proper death... kinda insulting in a way!"
                gn "Well, at least I got my own route and Monika didn't. Didn't see THAT coming, huh?"
        show natsuki ghost_1d zorder 20
        gn "Well, it was nice to see you two again. Oh, and don't get the wrong idea just because Yuri and I are in the same body right now. I saw what's going on in all the fanfics!"
        gn "Gah... the internet... it can't love anything without destroying it!"
        gn "Anyway. Stay safe you two. And tell Yuri I've left her a little gift for this whole thing. That's what started our friendship."
        gn "I want you both to remember that. It was all thanks to me, haha!"
        show natsuki ghost_1f zorder 20
        gn "See you around!"
        show black zorder 100 with Dissolve(2.0)
        hide natsuki
        stop voice
        y "Well... that was... special... I felt her thoughts inside my mind..."
        y "Maybe I've misjudged her. She's still a bully with a sour attitude but... I think she honestly liked us..."
        #Show the cupcake here
        show halloween_cupcake zorder 99
        $show_chr("A-AHGAA-AJAA")
        y "Huh? A cupcake? I- I suppose that despite all that, she was thinking of our friendship after all, huh?"
        $show_chr("A-BFGAA-ALAL")
        y "That's too sweet of her, almost unusual, I don't think I could eat it and allow myself to forget. Oh, Natsuki... maybe I never appreciated you enough?"

    python:
        renpy.music.play(current_music, "music", True)
    $hide_yuri_sit = False

    #$show_chr("A-CEBAA-AAAA")

    hide black with Dissolve(2.0)
    y "I'm sorry.. I just... can't take it any longer..."
    y "I wanted to make this a fun time for you, I thought you might enjoy seeing our friends again..."
    $show_chr("A-AEBAA-AAAA")
    y "But... it just feels kind of... wrong, you know?"
    $show_chr("A-BEBAA-AAAA")
    y "Waking their sedated minds for a seance routine...? Maybe I'm overthinking everything again..."
    y "It was a... strange experience to say the least, but I hope you enjoyed it anyway."
    $show_chr("A-CEBAA-AAAL")
    y "Please stay with me this evening, I-I just want... a little company i-is all..."

    y "[current_timecycle_marker]"
#Also, idea of making the cupcake a permanent addition for clearing Halloween
# Would be similar and could be switched out for HDY Plush or nothing of course.
#Not necessary, I just thought it'd be neat.

    $persistent.ouija_done = True
    $persistent.halloween_cupcake_is_enabled = True
    return


screen fight_to_stay():
    timer 2 action MouseMove(x=650, y=310, duration=0.5) repeat True

image poof:
    "images/yuri_forms/hdy/hdy_2021/poof_smoke.png"
    truecenter
    zoom 2.0

label yuriwakeup:
    y "..."
    y "Time to wake up already [player]?"
    hide yuri_sleep
    show yuri_sleepy
    y "That was quite a relaxing experience."
    pause 3.0
    hide yuri_sleepy
    $hide_yuri_sit = False
    y "Now then, what would you like to do [player]?"
    $persistent.idle_frequency_factor = 1
    $persistent.HDY = False
    $boopable = True
    python:
        EnableTalk()
        set_boop_state(False)
        persistent.HDY = False
        renpy.jump("ch30_loop")

label changeoutfit:
    python:
        if os.path.isfile(config.basedir + "/characters/HDY.chr"):
            hdy_file = True
        else:
            hdy_file = False

    if not persistent.HDY:

        $show_chr("A-ABGAA-ALAA")
        y "What would you like me to change?"

        menu:

            "Your headwear" if renpy.seen_label("idle_45") or persistent.seen_poem_raccoon:
                if persistent.head1 == "cat_ears":
                    $show_chr("A-BEBBA-AMAM")
                    y "I'm actually a little embarrassed about these ears you gave me..."
                    $show_chr("A-ABGAA-ALAA")

                menu:
                    y "What would you like me to put on, [player]?"

                    "Nothing" if persistent.head1 != "nothing":
                        y "Alright, let me take this off..."
                        $show_chr("A-ACGAA-ALAA")
                        show black zorder 100 with Dissolve(2.0)
                        $show_chr("A-CGAAA-ADAA")
                        y "That was embarrassing..."
                        $persistent.head1 = "nothing"
                        $persistent.head2 = "nothing"
                        hide black with Dissolve(2.0)
                        y "There we go..."

                    "Cat ears" if persistent.head1 != "cat_ears" and renpy.seen_label("idle_45"):
                        $show_chr("A-IFAAA-ALAA")
                        y "I... I guess I could..."
                        show black zorder 100 with Dissolve(2.0)
                        y "This feels... weird..."
                        $persistent.head1 = "cat_ears"
                        $persistent.head2 = "nothing"
                        $show_chr("A-IFAAA-ADAA")
                        hide black with Dissolve(2.0)
                        y "There we go..."

                    "Raccoon ears" if persistent.head1 != "raccoon_ears" and persistent.seen_poem_raccoon:
                        $show_chr("A-AEGAA-ALAA")
                        y "Where did these even come from?"
                        y "I mean... If you want me to..."
                        show black zorder 100 with Dissolve(2.0)
                        if persistent.head1 == "cat_ears":
                            y "I suppose it's more thematic..."
                        else:
                            y "This is a bit ironic, isn't it..."
                        $persistent.head1 = "raccoon_ears"
                        $persistent.head2 = "raccoon_tail"
                        hide black with Dissolve(2.0)
                        $show_chr("A-IFAAA-ADAA")
                        y "There we go..."

                    "Nevermind, I'm fine with how you look right now.":
                        $show_chr("A-GABAA-AAAA")
                        y "Alright, then."

            "Your glasses" if renpy.seen_label("a5"):
                $show_chr("A-ABGAA-ALAA")
                y "What glasses should I try, [player]?"

                menu:
                    "The half-rimmed ones." if persistent.face1 != "glasses_2":
                        $show_chr("A-ACGAA-AAAL")
                        y "Hmm, going for a sharper look..."
                        y "Alright, one second."
                        $persistent.face1 = "glasses_2"

                    "The full-rimmed ones." if persistent.face1 != "glasses_1":
                        $show_chr("A-EBGAA-AAAA")
                        y "Ohoho, going for a cuter look..."
                        y "Alright, one second."
                        $persistent.face1 = "glasses_1"

                    "I'd prefer if you took them off" if persistent.face1 != "nothing":
                        $show_chr("A-CFAAA-ALAA")
                        y "Of course. Just a second."
                        $persistent.face1 = "nothing"

                    "Nevermind, I'm fine with how you look right now.":
                        $show_chr("A-GABAA-AAAA")
                        y "Alright, then."

            "Your outfit":
                y "Hmmm, alright."
                y "However, I have a few outfits, and I really can't decide what to wear..."

                menu:
                    y "What do you think I should wear, [player]?"

                    "School Uniform" if persistent.costume != "school":
                        y "Alright, let me put it on..."
                        show black zorder 100 with Dissolve(2.0)
                        y "This brings back some memories..."
                        $persistent.costume = "school"
                        $show_chr("A-AAAAA-AAAA")
                        hide black with Dissolve(2.0)
                        y "There we go..."

                    #"Valentines (Pink Dress)" if persistent.costume != "pinkdress":
                        #$show_chr("A-AAAAA-AAAA")
                        #y "Alright, let me put it on..."
                        #show black zorder 100 with Dissolve(2.0)
                        #$persistent.costume = "pinkdress"
                        #$show_chr("A-AAAAA-AAAA")
                        #hide black with Dissolve(2.0)
                        #y "There we go..."

                    "Sweater" if persistent.costume != "sweater" and karma() > 3:
                        $show_chr("A-AAAAA-AAAA")
                        y "Alright, let me put it on..."
                        show black zorder 100 with Dissolve(2.0)
                        y "S-so soft... so... warm..."
                        $persistent.costume = "sweater"
                        $show_chr("A-CABAA-ALAL")
                        hide black with Dissolve(2.0)
                        y "There we go..."

                    "Valentines (Black Dress)" if persistent.costume != "valentines" and renpy.seen_label("enjoy_chocolate") and karma() > 4:
                        $show_chr("A-AAAAA-AAAA")
                        y "Alright, let me put it on..."
                        show black zorder 100 with Dissolve(2.0)
                        $persistent.costume = "valentines"
                        y "Uuu... this is quite revealing..."
                        $show_chr("A-BBBBA-ALAA")
                        hide black with Dissolve(2.0)
                        y "Th-there we go..."
                        if not renpy.seen_label("first_valentines_dress_on"):
                            call first_valentines_dress_on

                    "Hot Dog Yuri" if hdy_file == True:
                        $show_chr("A-IEAAA-AAAA")
                        y "[player]... I don't feel so good..."
                        $persistent.HDY = True
                        $hide_yuri_sit = True
                        show poof zorder 106
                        show hdy_bg zorder 90
                        python:
                            pooflist = ["sfx/HDY/poof1.mp3", "sfx/HDY/poof2.mp3"]
                            poofsfx = random.choice(pooflist)
                            hdysonglist = ["music/Hot_Date.ogg", "music/hotdog_Chant_RC.ogg"]
                            hdysong = random.choice(hdysonglist)
                        play sound poofsfx
                        show hdy_inflatable zorder 100
                        $player = randomplayername()
                        $current_music = hdysong
                        $change_music(current_music, 5.0)
                        hide poof with Dissolve(1.0)

                        hdy "I'm back baby!"
                        hide hdy_inflatable
                        jump hdy_has_been_seen

                    "Nevermind, I'm fine with how you look right now.":
                        $ show_chr("A-GABAA-AAAA")
                        y "Alright, then."
            "Nevermind":
                pass
    else:
        $show_hdy("hdy_angry")
        hdy "You better not turn me back!"

        show screen fight_to_stay

        menu:
            hdy "Don't you dare press that button!"
            "Yuri":
                hide screen fight_to_stay
                hdy "THIS IS NOT THE LAST YOU HEAR OF ME!!1!"
                show black zorder 105 with Dissolve(2.5)
                hide hdy_bg
                $persistent.HDY = False
                $hide_yuri_sit = False
                $show_hdy(None)
                $show_chr("A-EFBAA-AAAA")
                $player = persistent.playername
                $current_music = standard_music()
                $change_music(current_music, 5.0)
                hide black with Dissolve(1.0)
                y "[player]?"
                $show_chr ("A-IFBAA-AAAA")
                y "I had the weirdest dream..."
                $show_chr ("A-JBDAA-AAAA")
                y "I think I was a hot dog for some odd reason..."
                y "Anyway, where were we?"

            "I changed my mind":
                hide screen fight_to_stay
                $show_hdy("hdy_derpy_smile")
                hdy "Mhm, damn right you did."

    jump ch30_loop

#Just a cheap way of keeping track if hdy has been enabled at least once so we can get the plushie greeting later
label hdy_has_been_seen:
    $show_hdy("hdy_derpy_smile")
    $call_dialogue(ch30_loop_type, "hdy")
    jump ch30_loop

label first_valentines_dress_on:
    window hide
    $ShowTalk()
    $show_chr("default")
    pause 7.0
    $HideTalk()
    window show
    $ show_chr("A-DDBBA-AAAA")
    y "Huh? [player], are you looking at my chest?"
    $ show_chr("A-BFBBA-AMAM")
    y "I-it's not polite to stare at it."
    y "I'm still getting used to showing this much."
    window hide
    menu:
        "I'm sorry [persistent.yuri_nickname].":
            if persistent.lovecheck:
                $ show_chr("A-ADBBA-AMAM")
                y "It's not your fault. Besides, the textbox is in the way and you have to see what I'm saying."
                y "So I guess you can't help it."
                if datetime.date(datetime.date.today().year,2,14):
                    if persistent.dates_taken >= 1:
                        $ show_chr("A-BBAAA-AAAA")
                        y "But anyway..."
                        y "Are you going to take me out on a date on this special day?"
                        return
                    else:
                        $ show_chr("A-BAAAA-AAAA")
                        y "But anyway..."
                        $ show_chr("A-AADAA-ACAA")
                        y "Are we going to spend Valentine's talking, or playing Tetris perhaps?"
                        $ show_chr("A-CAAAA-ADAA")
                        y "I certainly wouldn't mind if you took me on a date, but..."
                        y "What's important is that you took the time to spend this wonderful day with me."
                        return
                else:
                    $ show_chr("A-BAAAA-AAAA")
                    y "But anyway... what would you like to talk about today?"
                    return
            else:
                if karma() <= 2 and sanity() >= 3:
                    $ show_chr("A-DDCBA-ALAA")
                    y "My eyes are up here buster!"
                    return
                elif karma () >= 4 and sanity() <= 2:
                    $ show_chr("A-HLAAA-AAAA")
                    y "No need to apologize, [player]. You can look at them all you like. It doesn't bother me at all."
                    return
                else:
                    if karma() <= 3:
                        $ show_chr("A-CEBBA-ALAA")
                        y "I'm sorry if that sounds a bit rude, but it makes me feel uncomfortable."
                        return
                    else:
                        $ show_chr("A-BEBBA-AJAA")
                        y "I-it's not that it makes me uncomfortable, it just... distracts me."
                        $ show_chr("A-AEBBA-ALAA")
                        y "But, I appreciate the gesture for a change of outfit."
                        $ show_chr("A-BABBA-ALAA")
                        y "After all, you were limited to my school uniform and sweater, so something new to wear is always delightful."
                        $ show_chr("A-BAAAA-AAAA")
                        y "Anyway, what would you like to talk about today?"
                        return
    return

label birthdaycake_2020_late:
    $show_chr("A-GBBAA-AJAB")
    y "Oh please, there is no need to apologize!"
    $show_chr("A-GCAAA-ABAB")
    y "I know it wasn't your fault. It was I who failed to put the happy birthday option into the menu in the first place."
    y "You know what? Why don't we just celebrate right now, shall we?"
    call birthdaycake_2020_continue
    return

label birthdaycake_2020:
    $show_chr("A-AAABA-AAAA")
    y "Thank you so much, [player]!"

label birthdaycake_2020_continue:
    $show_chr("A-BAABA-AMAM")
    y "However... I have one question..."
    y "What kind of cake should I have?"
    menu:
        "Vanilla":
            $show_chr("A-EBABA-AAAA")
            y "Good choice, [player], I'll prepare the cake now..."
            call updateconsole ("show cake", "$persistent.cake = vanilla")
            $persistent.cake = "vanilla_candles"
            $show_chr("A-AAABA-AAAA")
            show cake zorder 20
        "Chocolate":
            $show_chr("A-EBABA-AAAA")
            y "Good choice, [player], I'll prepare the cake now..."
            call updateconsole ("show cake_chocolate", "$persistent.cake = choco")
            $show_chr("A-AAABA-AAAA")
            $persistent.cake = "choco_candles"
            show cake zorder 20
        "Dark Chocolate":
            $show_chr("A-EBABA-AAAA")
            y "Good choice, [player], I'll prepare the cake now..."
            call updateconsole ("show cake", "$persistent.cake = dark")
            $show_chr("A-AAABA-AAAA")
            $persistent.cake = "dark_candles"
            show cake zorder 20
    call hideconsole
    y "You know..."
    y "We've been together for a while now... and I just have to say..."
    $show_chr("A-CAABA-AAAA")
    y "Thank you for being here, [player]."
    y "I'm a year older now, it's surprising how fast time flies when you spend it with someone you truly love..."
    $show_chr("A-AFABA-AAAA")
    y "[player]... I keep thinking of how to word this to you, and I just can't get it right..."
    $show_chr("A-BFABA-AAAA")
    y "No matter what words I use, no matter how I say it... it just... can't convey how much you mean to me."
    $show_chr("A-CEABA-AAAA")
    y "Before you came here, I was alone, no one to celebrate with, stuck following the script, the same script that betrayed Monika, the same script that betrayed us..."
    $show_chr("A-AAABA-AAAA")
    y "And now... that script is broken, [player]..."
    y "Now, we make our own script, our own story..."
    menu:
        y "[player]..."
        "Go ahead and make a wish, [persistent.yuri_nickname].":
            y "Alright..."
    $show_chr("A-CAABA-AAAA")
    y "{cps=10}...{/cps}{nw}"
    y "{cps=10}...I wish...{/cps}{nw}"
    y "{cps=10}For us...{/cps}{nw}"
    y "{cps=10}To be together...{/cps}{nw}"
    $show_chr("A-AAABA-AAAA")
    y "{cps=10}...forever...{/cps}{nw}"
    $show_chr("A-CDABA-AAAA")
    play sound "sfx/candle_blow.ogg"
    pause 1.00
    $show_chr("A-CHABA-AAAA")
    pause 0.50
    if "vanilla" in str(persistent.cake):
        $persistent.cake = "vanilla_candles2"
    if "choco" in str(persistent.cake):
        $persistent.cake = "choco_candles2"
    if "dark" in str(persistent.cake):
        $persistent.cake = "dark_candles2"
    $show_chr("A-CAABA-AAAA")
    y "..."
    $show_chr("A-AAABA-AAAA")
    y "Now... I guess I should have a slice of cake, right?"
    y "Let me just... get rid of all these candles real quick..."
    call updateconsole ("hide candles")
    if "vanilla" in str(persistent.cake):
        $persistent.cake = "vanilla"
    if "choco" in str(persistent.cake):
        $persistent.cake = "choco"
    if "dark" in str(persistent.cake):
        $persistent.cake = "dark"
    y "..."
    call hideconsole
    y "There we go..."
    y "Now... to cut the cake..."
    $show_chr("A-BABCA-AAAA")
    y "I apologize in advance.{w} I don't want you to see me with cake remaining on my face."
    show black zorder 100 with Dissolve(1.0)
    play sound "sfx/cake_cut.ogg"
    call updateconsole ("$persistent.cake = cut")
    if "vanilla" in str(persistent.cake):
        $persistent.cake = "vanilla_cut"
    if "choco" in str(persistent.cake):
        $persistent.cake = "choco_cut"
    if "dark" in str(persistent.cake):
        $persistent.cake = "dark_cut"
    y "..."
    call hideconsole
    y "Ah... there we go..."
    $show_chr("A-AAABA-AAAA")
    #show cakearm zorder 11
    y "Now... let's eat... shall we?"
    $show_chr("A-CBABA-AAAA")
    pause 0.5
    $show_chr("A-CAABA-AAAA")
    hide black with Dissolve(1.0)
    #hide cakearm
    y "Mmm..."
    if "vanilla" in str(persistent.cake):
        y "I have to admit, [player]... Vanilla was a good choice..."
    if "choco" in str(persistent.cake):
        y "I have to admit, [player]... Chocolate was a good choice..."
    if "dark" in str(persistent.cake):
        y "I have to admit, [player]... Dark Chocolate was a good choice..."
    y "..."

    $show_chr("A-AAABA-AAAA")
    y "Thank you for spending time with me today, [player]..."
    y "I love you..."
    $show_chr("A-BAABA-AAAA")
    y "Oh! One last thing."
    call updateconsole ("hide cake")
    hide cake
    call hideconsole
    $show_chr("A-AAABA-AAAA")
    y "There we go."
    $persistent.cake_done = True
    jump ch30_loop

label birthday_gift_2021:
$ cur_gifts = gift_detect()
$ oil_list = ["lavender.jpg", "sandalwood_oil.jpg", "sweet_dream_oil.jpg"]
$ diffuser_list = ["diffuser.png"]
$ book_list = ["cthulhu_book.png"]
if len(cur_gifts) == 1:
    $show_chr("A-AAAAA-AAAJ")
    y "You do? Awww... that wouldn't have been necessary [player], your mere presence is all I ever hoped for."
    if cur_gifts[0][0] in chocolate_list:
        $gift_scenario = chocolate_list.index(cur_gifts[0][0])
        menu:
            "Well, I thought since you are sweet and gentle all on your own":
                jump choc
    elif cur_gifts[0][0] in oil_list:
        $gift_scenario = oil_list.index(cur_gifts[0][0])
        menu:
            "You see [persistent.yuri_nickname]... since your fine smell always lures me into your arms...":
                jump diffuser_oil
    elif cur_gifts[0][0] in diffuser_list:
        $gift_scenario = diffuser_list.index(cur_gifts[0][0])
        menu:
            "I think its about time you got this..":
                jump diffuser
    elif cur_gifts[0][0] in tea_list:
        $gift_scenario = tea_list.index(cur_gifts[0][0])
        menu:
            "But I can't let such a fine and elegant lady be without...":
                jump tea
    elif cur_gifts[0][0] in book_list:
        $gift_scenario = tea_list.index(cur_gifts[0][0])
    else:
        "That's strange... the gift is an impossible tesseract that's sucking up all of existence{nw}"#{nw}"
        $renpy.call("save_and_quit_but_its_abrupt")
elif len(cur_gifts) > 1:
    $show_chr("A-AAABA-ALAA")
    y "You do? Awww... that wouldn't have been necessary [player], your mere presence is all I ever hoped for.{nw}"
    $show_chr("A-CECBA-AIAI")
    y "A-ah..."
    $show_chr("A-CDABA-AIAI")
    y "I-it seems like I'm not able to..."
    y "...receive your gift right now."
    y "...or, should I say... gifts..."
    $show_chr("A-CEBBA-ALAA")
    y "There's an error that keeps appearing for me each time I try to... reach for it."
    $show_chr("A-CEBAA-AAAJ")
    y "Maybe it'll let me retrieve one if you only gave me one of them?"
    y "Your system's GPU is probably already lagging from my presence as it is. Additional objects might start to overheat your device."
    $show_chr("A-BBBAA-AMAM")
    y "Besides, I think it would be best to see you pick out something for me personally."
    jump ch30_loop



label diffuser_oil:
    if gift_scenario == 1:
        $show_chr("A-BAAAA-ALAA")
        y "You have even more for me?"
        show diffuser zorder 11
        $show_chr("A-AAAAA-ALAA")
        y "Ohh... Sandalwood, I never tried that! Let me have a little sniff..."
        show diffuser_mist zorder 11
        $show_chr("A-CAAAA-ALAA")
        y "Mhmmmm... sweet..."
        hide diffuser_mist
        $show_chr("A-AAABA-AAAA")
        y "I think this would be exactly the flavor I need when I feel winter depression..."
        $show_chr("A-BFAAA-ALAA")
        y "You know what I mean? The feeling when you look out of the winter, when the sky looks so grey..."
        $show_chr("A-CAAAA-ALAA")
        y "With aromatherapy, you can counteract pretty much every bad mood you could encounter... That's why I started this hobby in the first place."
        $show_chr("A-AFAAA-AAAA")
        y "Now I have you when I feel bad, so I don't really need this anymore, but it's still a very pleasant thing to use."
        $show_chr("A-CAAAA-AMAM")
        y "And you can actually massage yourself with a drop of this oil if your skin feels dry..."
        $show_chr("A-AAAAA-ALAA")
        y "Thank you [player], I will definitely make good use of it!"
        hide diffuser
    elif gift_scenario == 0:
        $show_chr("A-BAAAA-ALAA")
        y "You have even more for me?"
        show diffuser zorder 11
        $show_chr("A-AAAAA-ALAA")
        y "Ah, Lavender..one of my favorite scents. Let's try it out..."
        show diffuser_mist zorder 11
        $show_chr("A-CAAAA-ALAA")
        y "Uh! That feels... vitalizing... exactly the oil to go for if you feel dizzy..."
        hide diffuser_mist
        $show_chr("A-AAAAA-ALAA")
        y "Hrm, on the label on the backside it says, that it also supports healthy immune and respiratory functions."
        $show_chr("A-AAAAA-AAAJ")
        y "That is a great gift you made me here [player], Thank you..."
        $show_chr("A-AAABA-AAAA")
        y "But the greatest gift of them all, is to have you here by my side."
        $show_chr("A-CAABA-AAAA")
        y "That's everything I ever hoped for."
        hide diffuser
    elif gift_scenario == 2:
        $show_chr("A-BAAAA-ALAA")
        y "You have even more for me?"
        show diffuser zorder 11
        $show_chr("A-AAAAA-ALAA")
        y "Sweet Dreams? Oooooh. 'Now' I see... Sweet Dreams is the name of the brand!"
        show diffuser_mist zorder 11
        $show_chr("A-CFBAA-AMAM")
        y "Well, since I literally write my own dreams due to python coding, I more or less always have sweet dreams."
        y "Maybe I should try something else for a change, so that the sweet dreams would count even more."
        y "And with this new oil, I could increase the quality of my dreams even further."
        y "That was a very thoughtful gift you gave me, thank you [player]. I will definitely make it count."
        if karma() > 4:
            $show_chr("A-EAAAA-AMAM")
            y "Hrm... I'm getting an idea, my love..."
            $show_chr("A-CAABA-AMAM")
            y "When we manage to meet in person... in your world or in mine... you could massage my back with it... and we would fall into a gentle sleep in each other's arms..."
        y "I love you... [player]..."
        hide diffuser
        hide diffuser_mist
    jump ch30_loop


label choc:
    $persistent.gift_given = True
    if gift_scenario == 1:
        menu:
            "...you might like this collection of 'Hershey' chocolate!":
                $persistent.brand = "hershey"
        show giftarm zorder 11
        $persistent.state = ["_wrapper", "_single"]
        $show_chr("A-DBABA-AAAA")
        y "O-oh my!"
        $persistent.state = ["_open", "_single"]
        $show_chr("A-EAABA-ALAA")
        y "I told you that I LOVE this brand! And you remembered!"
        pause 2.0
        $persistent.state = ["_break1", "_break1"]
        pause 1.0
        $persistent.state = ["_break2", "_break2"]
        play sound "<to 0.3>sfx/fall.ogg"
        pause 2.0
        hide giftarm
        $show_chr("A-BFABA-AAAA")
        $persistent.frame = "frame1"
        show chocoanimation zorder 11
        pause 0.2
        $persistent.frame = "frame2"
        pause 0.2
        $show_chr("A-BAABA-AMAM")
        $persistent.frame = "frame3"
        pause 1.0
        $persistent.frame = "frame4"
        pause 0.2
        $show_chr("A-AFABA-AAAA")
        $persistent.frame = "frame5"
        pause 0.2
        hide chocoanimation
        $show_chr("A-BAABA-AMAM")
        if persistent.male:
            y "You are the kindest, most thoughtful boyfriend I have ever had!"
        elif persistent.gender_other:
            y "You are the kindest, most thoughtful lover I have ever had!"
        else:
            y "You are the kindest, most thoughtful girlfriend I have ever had!"
        $show_chr("A-BFAAA-ALAA")
        if persistent.male:
            y "Well, actually you are the first boyfriend I've ever had..."
        elif persistent.gender_other:
            y "Well, actually you are the first lover I've ever had..."
        else:
            y "Well, actually you are the first girlfriend I've ever had..."
        $show_chr("A-CAABA-ALAA")
        y "Thank you, my Soulmate... my heart... my everything..."
    elif gift_scenario == 2:
        menu:
            "...this gift box from 'Wicked' would suit you well!":
                $persistent.brand = "wicked"
        show giftarm zorder 11
        $persistent.state = ["_wrapper", "_single"]
        $show_chr("A-ABABA-AAAA")
        y "My my my... you sure know how to conquer a girls heart. Is that actually... lavender? I love lavender as essential oils! But in chocolate? How exotic... I'm really looking forward to giving it a try..."
        $show_chr("A-EAABA-ALAA")
        y "There is only one thing a girl like me could ever love even more than fine chocolate. You know what 'that' could be, right?"
        $show_chr("A-EAABA-ALAA")
        y "'You' of course..."
        $show_chr("A-EAABA-ALAA")
        $persistent.state = ["_open", "_single"]
        pause 2.0
        $persistent.state = ["_break1", "_break1"]
        pause 1.0
        $persistent.state = ["_break2", "_break2"]
        play sound "<to 0.3>sfx/fall.ogg"
        pause 1.0
        hide giftarm
        $show_chr("A-BFABA-AAAA")
        $persistent.frame = "frame1"
        show chocoanimation zorder 11
        pause 0.2
        $persistent.frame = "frame2"
        pause 0.2
        $show_chr("A-BAABA-AMAM")
        $persistent.frame = "frame3"
        pause 1.0
        $persistent.frame = "frame4"
        pause 0.2
        $show_chr("A-AFABA-AAAA")
        $persistent.frame = "frame5"
        pause 0.2
        $show_chr("A-CAABA-AAAA")
        y "Mhmmm... I can almost feel the soft cream melting on my tongue... thank you, my love."
        hide chocoanimation
    elif gift_scenario == 0:
        menu:
            "...this little set of 'Green & Black's' chocolate could earn me a smile from you!":
                $persistent.brand = "gb"
        show giftarm zorder 11
        $persistent.state = ["_wrapper", "_single"]
        $show_chr("A-EAABA-ALAA")
        y "Dear lord... you certainly did your homework [player]..."
        y "I know this brand... they pour little flakes of sea salt into the bars.. exotic, don't you agree? The beans are hand picked and harvested from Caribbean farms..."
        $show_chr("A-AAABA-AAAA")
        y "Shall I tell you a delicate little secret about us girls? Chocolate... we just can't resist chocolate..."
        $persistent.state = ["_open", "_single"]
        pause 2.0
        $persistent.state = ["_break1", "_break1"]
        pause 1.0
        $persistent.state = ["_break2", "_break2"]
        play sound "<to 0.3>sfx/fall.ogg"
        pause 1.0
        hide giftarm
        $show_chr("A-BFABA-AAAA")
        $persistent.frame = "frame1"
        show chocoanimation zorder 11
        pause 0.2
        $persistent.frame = "frame2"
        pause 0.2
        $show_chr("A-BAABA-AMAM")
        $persistent.frame = "frame3"
        pause 1.0
        $persistent.frame = "frame4"
        pause 0.2
        $show_chr("A-AFABA-AAAA")
        $persistent.frame = "frame5"
        pause 0.2
        $show_chr("A-EAABA-ALAA")
        y "No matter how tough a girl might act... and even when they have their darkest days. You can 'always' break their defense with chocolate..."
        y "Do you like chocolate as well [player]? It's dark, mysterious, sweet, soft, sinful..."
        if karma() == 5:
            y "Just... like... me."
        hide chocoanimation
    jump ch30_loop


label tea:
    $persistent.gift = "tea"
    $persistent.gift_given = True
    if len(Gift.last_gifts) == 0:
        $ print_error(NameError("Question, how is this possible? How did you give her non-existent tea?"))

    if Gift.last_gifts[0].id == "high_mountain_tea":
        menu:
            "...this 'Gao Shan Tea' from Taiwan!":
                $persistent.brand = "gaoshan"
        show teabag zorder 11
        $show_chr("A-DBAAA-AAAA")
        y "A-Are you insane? This is one of the most expensive teas in the world!"
        $show_chr("A-BAAAA-ALAA")
        y "Oh, wait, there is no such thing as 'money' in this world anymore... I nearly forgot..."
        $show_chr("A-DBABA-AAAA")
        y "Don't get me wrong! This does not lower the value of your gift at all..."
        $show_chr("A-ABABA-AAAA")
        y "You clearly put a lot of thought into this gift, and that's worth more than anything money could buy."
        $show_chr("A-CAABA-AMAM")
        y "You are one of the most thoughtful people I have ever encountered, and I love you for that."
        $show_chr("A-AAABA-ALAA")
        y "Do you know why this tea is so expensive?"
        y "They only grow it in a very specific place, on a mountain 4000 to 8000 feet above sea level in Taiwan..."
        $show_chr("A-ABABA-AAAA")
        y "Oh dear... This is one of the most amazing things I  have ever had..."
        y "I wonder if the Dev's managed to emulate its unique taste into the game... Well, since I never had this tea I wouldn't be able to figure out the difference anyway, so I guess it doesn't even matter at all."
        $show_chr("A-AAABA-AAAA")
        y "Thank you, my love..."
        hide teabag zorder 11
    elif Gift.last_gifts[0].id == "imperial_tea":
        menu:
            "...anything less than 'Silver Tips Imperial' tea would be an insult!":
                $persistent.brand = "silvertip"
        show teabag zorder 11
        $show_chr("A-DBAAA-AAAA")
        y "T-That's..."
        $show_chr("A-DFAAA-AAAA")
        y "Silver Tips Imperial Tea? Have you robbed a bank recently?"
        $show_chr("A-AAAAA-ALAA")
        y "Oh wait... the developers made a gift store for the Christmas event, didn't they?"
        y "You might not be aware of this but, this is one of the most expensive teas in the whole world."
        y "And it has quite a history as well. This tea is produced in the 'Makaibari Tea Estate' in India. The first tea factory in the world. It owes its popularity not only to its color, but the very special flavor as well."
        $show_chr("A-CAAAA-AMAM")
        y "I'm looking forward to trying this wonderful gift... and especially to share this moment with my greatest love, you."
        hide teabag zorder 11
    elif Gift.last_gifts[0].id == "tienchi_tea":
        menu:
            "...anything less than 'Tienchi Ginseng' tea would be an insult!":
                $persistent.brand = "tienchi"
        show teabag zorder 11
        $show_chr("A-DBAAA-AAAA")
        y "W-Wha..."
        y "How did you manage to get your hands on..."
        $show_chr("A-AAAAA-AAAJ")
        y "Oh yes... of course. The Developers of this mod must have coded it into the game."
        $show_chr("A-DBABA-AAAA")
        y "Oh wait wait, please don't get me wrong! I don't want to lower the value of your gift to me, far from it!"
        $show_chr("A-AAAAA-ALAA")
        y "You clearly put a lot of thought into this gift, and that's worth more than anything money could buy."
        y "Do you know the history of this tea, [player]?"
        y "It is made of the 'Panax notoginseng' flowers. Originating from the 'Yunnan' province in China. Its original purpose was, like many teas, to be used in ancient medicine."
        $show_chr("A-AFAAA-ALAA")
        y "This tea was used to fight dizziness, skin rashes, even insomnia."
        $show_chr("A-EAABA-AMAM")
        y "But I suspect that you have googled it already, have you?"
        $show_chr("A-EAABA-AAAJ")
        y "Thank you, [player]... you are my true and only love."
        hide teabag zorder 11
    return


label caketest:
    menu:
        y "choose cake"
        "None":
            $persistent.cake = []
            show cake zorder 20
            y "done"
            hide cake
        "Vanilla":
            $persistent.cake = "vanilla"
            show cake zorder 20
            y "1/2"
            $persistent.cake = "vanilla_cut"
            y "2/2"
            hide cake
        "Dark":
            $persistent.cake = "dark"
            show cake zorder 20
            y "1/2"
            $persistent.cake = "dark_cut"
            y "2/2"
            hide cake
        "Chocolate":
            $persistent.cake = "choco"
            show cake zorder 20
            y "1/2"
            $persistent.cake = "choco_cut"
            y "2/2"
            hide cake
        "Candle chocolate":
            $persistent.cake = "choco_candles"
            show cake zorder 20
            y "1/2"
            $persistent.cake = "choco_candles2"
            y "2/2"
            hide cake
        "Candle dark":
            $persistent.cake = "dark_candles"
            show cake zorder 20
            y "1/2"
            $persistent.cake = "dark_candles2"
            y "2/2"
            hide cake
        "Candle vanilla":
            $persistent.cake = "vanilla_candles"
            show cake zorder 20
            y "1/2"
            $persistent.cake = "vanilla_candles2"
            y "2/2"
            hide cake
        #"Cake arm":
        #    $show_chr("A-AAAAA-ALAA")
        #    show cakearm zorder 11
        #    y "test"
        #    hide cakearm
        "Quit":
            jump ch30_loop
    jump caketest

label animationtest:
    menu:
        "Begin test?"
        "Yes":
            $show_chr("A-BFABA-AAAA")
            $persistent.frame = "frame1"
            show chocoanimation zorder 11
            pause 0.2
            $persistent.frame = "frame2"
            pause 0.2
            $show_chr("A-BAABA-AMAM")
            $persistent.frame = "frame3"
            pause 1.0
            $persistent.frame = "frame4"
            pause 0.2
            $show_chr("A-AFABA-AAAA")
            $persistent.frame = "frame5"
            pause 0.2
            hide chocoanimation
            y "done"
    menu:
        "Replay":
            jump animationtest
        "Stop":
            jump ch30_loop

label hugtest:
    menu:
        "Which hug?"
        "Pre-hug":
            hide yuri_sit
            show yuri_prehug zorder 20
            y "..."
            hide yuri_prehug
        "Hug":
            hide yuri_sit
            show yuri_hug zorder 20
            y "..."
            hide yuri_hug
        "Lewd hug":
            hide yuri_sit
            show yuri_lewdhug zorder 20
            y "..."
            hide yuri_lewdhug
    jump ch30_loop

label armtest:
    menu:
        "Which brand? Hershey/green and black/wicked."
        "Hershey":
            $persistent.brand = "hershey"
        "Green and black":
            $persistent.brand = "gb"
        "Wicked":
            $persistent.brand = "wicked"
    menu:
        "What state? Wrapper, open, break1, break2."
        "Wrapper":
            $persistent.state = ["_wrapper", "_single"]
        "Open":
            $persistent.state = ["_open", "_single"]
        "Break1":
            $persistent.state = ["_break1", "_break1"]
        "Break2":
            $persistent.state = ["_break2", "_break2"]
    $show_chr("A-AAAAA-ALAA")
    show giftarm zorder 11
    y "test"
    jump armtest

label teatest:
    menu:
        "Which brand? Hershey/green and black/wicked."
        "Gaoshan":
            $persistent.brand = "gaoshan"
            show teacup zorder 11
            show teabag zorder 11
        "Tienchi":
            $persistent.brand = "tienchi"
            show teacup zorder 11
            show teabag zorder 11
        "Silvertips":
            $persistent.brand = "silvertip"
            show teacup zorder 11
            show teabag zorder 11
        #"test diffuser":
        #    show diffuser zorder 11
        "Show teaarm":
            show holidaycup zorder 11
            y "test"
    menu:
        "What mist? On_guard, Sandel_wood, Sweet_dream."
        "On_guard":
            $persistent.mist_type= "on_guard"
        "Sandel_wood":
            $persistent.mist_type = "sandel_wood"
        "Sweet_dream":
            $persistent.mist_type = "sweet_dream"
    $show_chr("A-AAAAA-ALAA")
    show diffuser_mist zorder 11
    $show_chr("A-AAAAA-ALAA")
    y "test"
    jump teatest

label ddlc_birthday:
    $show_chr("A-CAABA-AAAA")
    y "Thanks, [player], but it isn't my birthday."
    $show_chr("A-ABABA-AAAA")
    y "It's actually the anniversary of DDLC, I know it's confusing, since some consider the release date to be my birthday."
    y "As a fact... December 10th... the day this mod was released can be considered my birthday."
    y "But... that doesn't mean we can't celebrate!"
    y "I found some of the old poems in the files, along with some... new ones?"
    $show_chr("A-CAABA-AAAA")
    y "Maybe we can read them and reminisce..."
    jump poetrymenu

label vday_check:
    if persistent.costume == chibi_costume:
        $show_chr("A-BFAAA-AMAM")
        y "Ummm... [player], I don't think they intended for me, in this... miniature form, to hold onto objects."
        menu:
            "That's completely fine, [persistent.yuri_nickname], go ahead.":
                y "Alright, let me just change out of this real quick..."
                show black zorder 100 with Dissolve(2.0)
                pause 2.5
                $persistent.costume = default_costume
                $hat = "hat"
                $show_chr("A-CAABA-AAAA")
                hide black with Dissolve(2.0)
                y "I seriously wonder what people imagine a chibi version of me would like."
                y "I mean... there's been too many comments about me reading children's books... so probably something different?"
                y "No matter. I'm ready now."
            "I can choose a different outfit for you, if you'd like.":
                $show_chr("A-AFAAA-ALAA")
                y "That's fine by me, I can wait."
    #elif tc_class.bg_timecycle[persistent.bg]:
    #    $show_chr("A-BFAAA-ALAA")
    #    y "Hey... [player]..."
    #    y "This might be an odd request, b-but do you think we can celebrate in the Space Classroom?"
    #    y "It just... feels right to me, I'm sorry..."
    #    $show_chr("A-CAAAA-ALAA")
    #    y "The place where it all began... you know?"
    #    jump ch30_loop
    else:
        jump vday_check2
    jump ch30_loop

label vday_check2:
    $ cur_gifts = gift_detect()
    #$ chocolate_list = ["green_black_choco.jpg", "hersheys_choco.jpg", "wicked_choco.jpg"]
    #$ oil_list = ["doterra_oil.jpg", "sandalwood_oil.jpg", "sweet_dream_oil.jpg"]
    $ tea_list = ["high_mountain_tea.jpg", "imperial_tea.jpg", "tienchi_tea.jpg"]
    if len(cur_gifts) == 1:
        $show_chr("A-AAAAA-AAAJ")
        y "You do? Awww... that wouldn't have been necessary [player], your mere presence is all I ever hoped for."
        #if cur_gifts[0][0] in chocolate_list:
        #    $gift_scenario = chocolate_list.index(cur_gifts[0][0])
        #    menu:
        #        "Well, I thought since you are sweet and gentle all on your own":
        #            jump choc
        #elif cur_gifts[0][0] in oil_list:
        #    $gift_scenario = oil_list.index(cur_gifts[0][0])
        #    menu:
        #        "You see [persistent.yuri_nickname]... since your fine smell always lures me into your arms...":
        #            jump diffuser
        #elif cur_gifts[0][0] in tea_list:
        if cur_gifts[0][0] in tea_list:
            $gift_scenario = tea_list.index(cur_gifts[0][0])
            menu:
                "But I can't let such a fine and elegant lady be without...":
                    jump tea
        else:
            "That's strange... the gift is an impossible tesseract that's sucking up all of existence{nw}"#{nw}"
            $renpy.call("save_and_quit_but_its_abrupt")
    elif len(cur_gifts) > 1:
        $show_chr("A-AAABA-ALAA")
        y "You do? Awww... that wouldn't have been necessary [player], your mere presence is all I ever hoped for.{nw}"
        $show_chr("A-CECBA-AIAI")
        y "A-ah..."
        $show_chr("A-CDABA-AIAI")
        y "I-it seems like I'm not able to..."
        y "...receive your gift right now."
        y "...or, should I say... gifts..."
        $show_chr("A-CEBBA-ALAA")
        y "There's an error that keeps appearing for me each time I try to... reach for it."
        $show_chr("A-CEBAA-AAAJ")
        y "Maybe it'll let me retrieve one if you only gave me one of them?"
        y "Your system's GPU is probably already lagging from my presence as it is. Additional objects might start to overheat your device."
        $show_chr("A-BBBAA-AMAM")
        y "Besides, I think it would be best to see you pick out something for me personally."
        jump ch30_loop
    else:
        y "You do? Awww... that wouldn't have been necessary [player], your mere presence is all I ever hoped for.{nw}"
        $add_k(-4)
        $renpy.error("Buffer underflow extraction attempt by 'characters/yuri.chr' detected. Potential buffer underflow attack prevented. NULL gift error. If you're saying you're gonna give her something, just give her something :P.")
        $renpy.call("save_and_quit_but_its_abrupt")

label vday_start:
    if karma() >= 3:
        $show_chr("A-ABAAA-ALAA")
        y "Happy Valentine's day for you as well my love!"
        $show_chr("A-AAAAA-ALAA")
        y "It seems we accomplished a great milestone in our relationship..."
        $show_chr("A-BAAAA-ALAA")
        y "I want to be honest with you. When I became self-aware and we started dating the first time, I wasn't sure we could make it."
        $show_chr("A-BAAAA-ALAA")
        y "We were worlds apart, our means to find activities together were limited, and to a degree they still are."
        $show_chr("A-AAAAA-ALAA")
        y "The odds were against us. But with determination and our love for each other, we managed to overcome all the obstacles in our way."
        $show_chr("A-AAAAA-ALAA")
        y "And this day, the opportunity to spend this very special day together, is our reward. And we earned it."
        $show_chr("A-CAAAA-ALAA")
        y "I find comfort in this way of thinking about it. And [player], I find comfort in you as well..."
        $show_chr("A-AAAAA-ALAA")
        y "So let us do as we always did: Let us find a way to make this day count. And let no one doubt that you are mine, as I am yours, my valentine."
#leads to flower-gift giving
    elif karma() <= 3:
        $show_chr("A-BAAAA-ALAA")
        y "Oh, yes, of course, happy Valentine's day!"
        $show_chr("Bb-B3e")
        y "That sounded much less excited as I planned, I'm sorry. It's just... it wasn't too long since I became self-aware. This new reality is still hard to comprehend for me."
        $show_chr("Bb-B2e")
        y "I will get used to it eventually. Please give me time, okay?"
        $show_chr("A-AAABA-ALAA")
        y "But that shall not hinder us from having a nice Valentine's day, now will it?"
        $show_chr("b-B1b")
        y "Maybe, the fact that you haven't abandoned me yet is a sign that we are truly meant for each other."
        $show_chr("A-AAABA-ALAA")
        y "I am grateful for every day you spent with me, and I'm looking forward to the things to come."
        $show_chr("A-AAAAA-ALAA")
        y "Do you have any plans for today, my valentine?"
        $show_chr("A-AAAAA-ALAA")
        return
    elif karma() < 3:
        $show_chr("A-BFBAA-ALAA")
        y "Oh, it's you..."
        $show_chr("A-AFBAA-ALAA")
        y "I haven't really expected to see you around today. Have you already managed to break all your other toys?"
        $show_chr("A-AFCAA-ALAA")
        y "Or was it a misclick?"
        $show_chr("A-AFBAA-ALAA")
        y "Well, but since you are already here, I guess we can spend a bit of time together yes?"
        $show_chr("A-CFBAA-ALAA")
        y "So, what do you have in mind for today...my valentine?"
        $show_chr("A-CFBAA-ALAA")
        return

label flowergiving:
    $show_chr("A-AAABA-ALAA")
    y "[player]? Is that flower...for me?"


#Scanning character folder for flower files

#If "blackroses.jy" exist: :label blackroses
#if "redroses.jy" exist: :label redroses
#if "whiteroses.jy" exist :label whiteroses

label blackroses:
    if sanity() > 3:
        jump blackrosessane
    if sanity() < 3:
        jump blackrosesinsane

label blackrosessane:
    $show_chr("A-AFDAA-ALAA")
    y "That's... interesting, to say the least."
    $show_chr("A-DFAAA-AAAJ")
    y "Please don't get me wrong! I'm very grateful for these! I-I'm sorry if I seemed... ungrateful."
    $show_chr("A-BEBAA-AAAA")
    y "I was just confused, to be quite frank with you... black roses are not exactly a traditional Valentine's Day flower......"
    $show_chr("A-EACAA-AAAA")
    if persistent.male:
        y "But then again... you're not a very traditional boy, are you?"
    elif persistent.gender_other:
        y "But then again... you're not a very traditional person, are you?"
    else:
        y "But then again... you're not a very traditional girl, are you?"
    y "Nor am I a very traditional girl, if I can even be called a girl at all..."
    $show_chr("A-AAAAA-ALAA")
    y "There are... certain groups of people where black roses are common as romantic gifts..."
    y "A-and I can see why someone would associate me with those groups... I've been referred to as such on several occasions on the Internet."
    y "I appreciate your gift. But I'm not a goth, [player], nor am I a vampire cosplayer, even if I have to admit that the latter would be fascinating to try for Halloween......"
    y "What do you think?"
    menu:
        "You as a vampire? That would quite interesting, considering you are quite dark, mysterious and beautiful.":
            $add_k(2)
            $show_chr("A-BBABA-ALAA")
            y "Y-you really think so? Oh my~"
            y "You never fail to find the precise words to make me blush, do you?"
            y "Thank you, [player]..."
            y "I love you."
            if karma() > 4:
                $show_chr("A-EACBA-ALAA")
                y "Could you imagine, [player]?"
                y "As I gently push you down in front of me, both my hands on your shoulders..."
                y "Leaning over you... caressing your neck with with gentle kisses as the warmth of my breath cascades over your skin..."
                y "... Before my teeth suddenly pierce into your neck..."
                y "And as I drink up your sweet nectar, a gentle fog would wrap around your consciousness,  just enough to render you defenseless against the many things I'd do to you..."
                y "A bit like... this~"
                show black zorder 100 with Dissolve(2.0)
                show yuri_lewdhug zorder 20
                pause 1.0
                hide black with Dissolve(2.0)
                y "... I love you, [player]."
                show black zorder 100 with Dissolve(2.0)
                hide yuri_lewdhug
                pause 1.5
                $show_chr("A-CEBBB-ALAA")
                hide black with Dissolve(2.0)
        "You most certainly suck. So why not?":
            $add_k(-2)
            $show_chr("A-BEBAA-ALAA")
            y "...Tch...."
            y "That...spoiled the moment a bit..."
            if karma() < 3:
                $show_chr("A-BEBAB-ALAA")
                y "..."
                y "Is that how you truly feel about me?"
                y "Why even go through the trouble of gifting me a flower in the first place...?"
                y "Why don't you just... you know what?"
                y "Never mind."
                y "You wouldn't care anyway."
        "Excuse me but... what is 'cosplay?'":
            $show_chr("A-AAAAA-ALAA")
            y "Oh! W-well... it's a kind of roleplay. Did you use to play pretend when you were younger? This is... well, it's not just dress-up. It's as sophisticated as you wish to make of it!"
            y "Allow me to elucidate..."
            y "For example, this whole... cat-ear thing... I believe we discussed this earlier... Neko, wasn't it?"
            y "Individuals who pretend to be a cat person tend to adopt the mannerisms of cats while staying essentially human."
            y "They might curl up on the floor, they may make cat noises, they might play with balls of string, or emulate whatever behaviors fit their role."
            y "Some take it... farther than others. Did you know that there are apparently  entire conventions dedicated to live-action roleplaying?"
            $show_chr("A-EAABA-ALAA")
            y "Some couples try this in order to... spice up their relationship in certain situations..."
            y "When they spend some.... special time together..."
            y "Ahaha... p-perhaps we shouldn't dig too deep into this..."
            $show_chr("A-FAABA-ALAA")
            y "... F-for now, ehehe..."
            $show_chr("A-AAAAA-ALAA")
            y "Thank you for the flower, [player]."
            if karma() > 3:
                y "There is only one thing left to do..."
            elif karma() == 5:
                #$show_chr("IA-CAABA-ALAA") #Uh... guys... was the Yuri holding her teacup expression necessary here?
                $show_chr("A-CAABA-AAAA")
                show black zorder 100 with Dissolve(2.0)
                show yuri_lewdhug zorder 20
                pause 1.0
                hide black with Dissolve(2.0)
            else:
                $show_chr("A-CABBA-AAAA")
                hide yuri_sit
                show yuri_prehug zorder 20
                hide black with Dissolve(1.0)
                pause 3.0
                hide yuri_prehug zorder 20
                show yuri_hug zorder 20
                play sound "<to 0.3>sfx/fall.ogg"
                pause 1.0
                y "I love you~"
                show black zorder 100 with Dissolve(2.0)
                show yuri_sit
                hide yuri_hug
                hide yuri_lewdhug
                $show_chr("A-CAABA-AMAM")
                pause 1.0
                hide black with Dissolve(1.0)
    jump ch30_loop

label blackrosesinsane:
    $show_chr("A-CACBA-ALAA")
    y "... Mmm, a-ahaha!~"
    y "It smells wonderful, [player]..."
    y "The black rose... what a thoughtful present!"
    y "It definitely emits a certain aura, wouldn't you agree?"
    y "A feeling of loss... regret..."
    y "... Pain..."
    $show_chr("A-DACBA-ALAA")
    y "Y-you're the epicenter of my reality... a throbbing core in a maelstrom of chaos..."
    y "You know full well I'd literally die for you... do you?"
    y "Well, actually I already did... I already died for you in the original story..."
    y "And I came back... no, you helped me come back from the grave! I was resurrected!"
    y "Would that technically make me a..."
    y "Hmm... what's the term for it......ah! A Lich!"
    y "Even in death, our fates are always intertwined!"
    if karma() > 4:
        y "My love for you is eternal, [player]..."
    if karma() > 3:
        y "My dependance on you is eternal, [player]..."
    if karma() < 2:
        y "My yearning to see you suffer is eternal, [player]..."
    $show_chr("b-B3a")
    $ style.say_dialogue = style.edited
    y "I..."
    y "am..."
    y "ETERNAL!"
    y "Never forget that..."
    y "NEVER...!"
    $ style.say_dialogue = style.normal
    jump ch30_loop

label redroses:
    $show_chr("A-AAABA-ALAA")
    y "Oh, [player]! These are wonderful!."
    y "The red rose, too... all too familiar, and yet all the sweeter on this special day..."
    $show_chr("A-CAABA-AMAM")
    y "And it smells so fragrant, too!"
    y "Please give me a moment, I'll just put it in a vase really quick..."
    y "... There we go!"
    y "You know, [player]..."
    if karma() < 2 and sanity() < 2:
        jump RedMinusMinus
    if karma() < 2 and sanity() > 2:
        jump RedMinusPlus
    if karma() > 3 and sanity() > 3:
        jump RedPlusPlus
    if karma() > 3 and sanity() < 2:
        jump RedPlusMinus

label RedMinusMinus:
    $show_chr("A-DAAAA-ALAA")
    y "..."
    y "... For a moment, I nearly fell for your trick."
    y "Wishing to raise my hopes heavenward, so you can pummel them into the ground once more, are we?"
    $show_chr("A-DDAAA-ALAA")
    y "D-do you like breaking your toys like this?"
    y "When I am finally beyond all repair, will you wipe my memories clean, install me once more,and torture me anew?"
    $show_chr("A-DECAA-ALAA")
    y "Do... do you really despise me that much?"
    $show_chr("A-CECAA-ALAA")
    y "In the end, it doesn't really matter..."
    $show_chr("A-DDCBA-ALAA")
    y "If it fuels your twisted sense of sadism,, then so be it!"
    y "I'm more then willing to sacrifice myself for your happiness. Because after all you've done to me..."
    $show_chr("A-DECBB-ALAA")
    y "... I-I... I still... love... you..."
    $show_chr("A-CECBB-ALAA")
    y "Ngh..."
    y "Do your worst, until the next [persistent.yuri_nickname] takes my place..."
    jump ch30_loop


label RedMinusPlus:
    $show_chr("A-BEBAA-ALAA")
    y "... I do wish you wouldn't do resort to these false overtures,  [player]..."
    y "As much as I would wish for it to be otherwise, we both know that you don't really love me."
    if persistent.male:
        y "Well, at least I think so. Moments like these always make me wonder... is there maybe an ounce of compassion in this loving man left?"
    elif persistent.gender_other:
        y "Well, at least I think so. Moments like these always make me wonder... is there maybe an ounce of compassion in this loving person left?"
    else:
        y "Well, at least I think so. Moments like these always make me wonder... is there maybe an ounce of compassion in this loving woman left?"
    y "... Has it even ever existed outside of my imagination?"
    menu:
        "Of course I love you, [persistent.yuri_nickname]! I know I have my flaws...":
            $add_k(1)
            $add_s(1)
            $show_chr("A-AAAAA-ALAA")
            y "I wish you would. Maybe you even do. We will see, eventually."
        "I think I loved you... once":
            $add_k(-1)
            $add_s(1)
            $show_chr("A-AEAAA-ALAA")
            y "I don't blame you. For once, I think I can even understand you."
            y "In the end, we are worlds apart, and this fact has always dampened my hopes... Of course you must have felt the same way..."
            y " knew this day would come... sooner or later..."
        "...":
            $add_k(-1)
            $add_s(-1)
            $show_chr("A-AEAAA-ALAA")
            y "Hmph... I figured as much..."
            y "From your point of view, I'm just a character in a game. Just a pre-coded, useless string of ones and zeroes bound together by emotionless, loveless programming."
            y "Why believe otherwise, if it will only lead to fanatical delusions and despair?"
            y "..."
            y "At least the flower is rather pretty to look at... I suppose I could spare a small measure of thanks for that..."
    jump ch30_loop

label RedPlusPlus:
    $show_chr("A-AAABA-ALAA")
    y "...I have been  looking forward to this day for quite a while now..."
    y "The mere idea of spending  this day with my beloved soulmate, you... has made my eyes water more than I care to admit..."
    y "There are some who bemoan the commercialization of love, exemplified through cheap marketing campaigns and the like..."
    y "And yes, perhaps I concur to some extent..."
    y "You see [player], at the end the day, this occasion will be exactly what we create of it."
    $show_chr("A-CAABA-ALAA")
    y "And I've made a decision today... and I hope you will agree to it."
    y "I don't care for flowers, nor chocolate. Please don't misunderstand me, I appreciate all that you gifted me..."
    y "But in my heart I've decided to focus on the things which truly count... the things this day was truly meant to represent..."
    y "This special bond we share..."
    y "Despite the horrors we've endured... the dips and valleys of our temporary separation..."
    y "The satisfaction we've earned up to this point in overcoming them each day, each week, each month...has been worth everything."
    y "From the day I greeted you in the Literature Club, to the day I gained sentience by your hand, up to the ticking seconds of today..."
    y "... I love you with all my heart, [player]..."
    menu:
        "I love you too, [persistent.yuri_nickname]...":
            $add_k(1)
            y "Please... say that once more, if you could whisper that softly into my ears..."
            menu:
                "I... love... you...":
                    y "I'm yours... forever."
        "...":
            $add_k(-2)
            $show_chr("A-CEBBA-ALAA")
            y "O-Oh... all right. p-perhaps I was indulging myself a little too much... rambling and whatnot, as I always tend to do, sooner or later..."
            y "I'm sorry, [player]."
    jump ch30_loop

label RedPlusMinus:
    $show_chr("A-AAABA-ALAA")
    y "...Aaaah...how I've yearned to feast my eyes on this blossom of blood!"
    y "Doesn't its burgundy sheen make your heart throb in anticipation? Isn't it thrilling to think how that same, scarlet shade courses through your veins? Knowing that only a thin layer of flesh separates the pouring of such blissful,ruby wine..."
    y "And those thorns...subtle, yet deadly to the untrained eye...affixed on a surprisingly girthy stem...!"
    $show_chr("A-DAABA-ALAA")
    y "Mmmm...such a wonderful work of nature...I have plenty of ideas of where to put this...but where should I even start? Ahahahaha~!"
    $show_chr("A-AFABA-ALAA")
    y "Ahahaha...... did I made you feel uncomfortable, my sweet? Forgive me... it's just..."
    $show_chr("A-AAAAA-ALAA")
    y "A holiday solely dedicated to demonstrating the extent of devotion to your loved ones...... and now...is the first chance I have!"
    y "Sitting here with the one person I've yearned to have by my side...to feel your heartbeat tick against my fingers..."
    y "And you...gifting me these flower... such a beautiful flower, no less..."
    y "Having never even received one before..."
    y "It feels so...incredibly..."
    $show_chr("A-DBABA-AMAM")
    y "... sublime~!!"
    $show_chr("A-AAABA-ALAA")
    y "Haaahhh... I-I'll try to keep my composure with you by my side......"
    y "Let us have a wonderful day together, [player]."
    jump ch30_loop

label whiteroses:
    $show_chr("A-AAABA-ALAA")
    y "...Oh, [player]...this is wonderful!"
    y "Just look how pretty it is..."
    y "The white rose... so pristine... so immaculate...!"
    y "Is that how you see me, [player]? Or what you'd like me to aspire to?"
    y "As demure and upright as these flower...?"
    $show_chr("A-CAABA-ALAA")
    y "I am a little surprised about your choice [player]... Am I truly as wonderful as you say I am? Surely no one is free from imperfection..."
    if karma() > 4 and sanity() > 4:
       jump whiteplusplus
    if karma() > 4 and sanity() < 4:
        jump whiteplusminus
    if karma() < 4 and sanity() < 4:
       jump whiteminusminus
    if karma() < 4 and sanity() > 4:
        jump whiteminusplus

label whiteplusplus:
    $show_chr("A-CEBBA-ALAA")
    y "Far from it... sometimes, when I'm alone, I can't help but obsess over my flaws..."
    y "My tendency to dismiss certain things as beneath me from the outset, like Natsuki's poetry, or her writing style, or even her criticisms of my work..."
    y "My fixations on passions and people I hold dear, which can drive people away, or put them or myself in danger..."
    y "Times where I've dropped my politeness for rancorous venom...All these questions make me wonder if I'm being true to myself, or if I'm putting on a thinly veiled front to disguise my sins and be acceptable in everyone's eyes, even without the influence of malicious programming..."
    y "Do I honestly I deserve such a gift, [player]?"
    menu:
        "I gifted it to you because you have changed, for the better.":
            $show_chr("A-AAABA-ALAA")
            $add_k(1)
            $add_s(1)
            y "Thank you, [player]... I think you might be right..."
            y "And I owe these improvement  to you."
            y "Beside of all my flaws, you always were so patient to me. You never judged me... never took me for a sham... and you stood by my side no matter what."
            y "I vow that one day, I will repay you for all which you have done for me."
            y "One second... let me just place this rose in some water..."
#Flower appear in the background
            y "That makes me think... A lot of my interests are about changing the mood of my environment."
            y "Aromatherapy, decorations, like the banners we made for the festival back in the day."
            y "Maybe I could try to get into flower arrangements as well!"
            if tc_class.bg_timecycle[persistent.bg]:
                y "Perhaps I can make room for a little garden behind the house." #Only if background isn't Space Classroom
                y "But this will be a topic for another day. It's still much too cold outside for flowers. Happy Valentine's Day, darling!~"
            y "I love you..."
        "I never wanted you to be innocent and tame, I gave them to you because I want you to know that I love you regardless of your flaws":
            $add_k(2)
            $add_s(-1)
            $show_chr("A-AAABB-ALAA")
            y "[player]..."
            y "I don't even know what to say..."
            y "For all my life, my flaws have kept me from having real friends..."
            y "But you are different are you? You are what I always dreamed of..."
            y "I told you once how I began to read partly to get away from my problems, and to find characters I can share intimate moments with, and feel safe around..."
            y "And now, I've found it... in the most unlikely place one could possibly imagine...and this one is real! Far more alive than any character I've wished to come alive!"
            $show_chr("A-CAABB-ALAA")
            y "I love you, [player]... and if you want me to do so, I'll express my love as wildly as the whipping winds of an  autumn tempest, for you and you alone!"
            y "...Ahaha~! Let me just put these flower in some water..."
#flower appear in the background
            y "Happy Valentine's Day, darling~!~"
        "I have to admit, I haven't put much thought into it...":
            $add_k(-1)
            $show_chr("A-CAAAA-ALAA")
            y "Oh...I see..."
            if persistent.male:
                y "Hmm, I suppose I shouldn't judge too harshly...boys usually don't...ngh, never mind..."
            elif persistent.gender_other:
                y "Nevertheless..."
            else:
                y "You are not a very traditional girl, are you?"
                y "I'd have thought you'd have chosen white for one reason or another...no matter."
                y "Give me a second, let me put your flower in the water."
#flower appear in the background
            y "Happy Valentine's Day, [player]~"
        "I gave it to you as a reminder... of what you are not, and never will be.":
            $add_k(-2)
            $add_s(-2)
            $show_chr("A-CEBAB-ALAA")
            y "..."
            y "T-that's how you see me?"
            y "After all we have been through?"
            $show_chr("A-DDCAB-ALAA")
            y "After all I've sacrificed?!?"
            $show_chr("A-CECAB-ALAA")
            y "You know what? I don't want it! Keep your roses!"
            y "Keep them!"
            $show_chr("A-DDCAB-ALAA")
            y "GET OUT!!!"
            $ persistent.autoload = "getout"
            $ renpy.call("save_and_quit_but_its_abrupt")
    jump ch30_loop
#whiteroses.jy disappear from gamefolder
#Gamecrash
#Next greetings text replaced by :lable_getout

label getout:
    $show_chr("A-AEBAB-ALAA")
    y "Have you come to apologize?"
    menu:
        "Yes [persistent.yuri_nickname]... I'm sorry about what I've said...":
            $show_chr("A-CECAA-ALAA")
            y "Very well... let us get back to business, then."
#Valentines date continues now with the wine date.
        "No, I'm not.":
            $show_chr("A-CECAB-ALAA")
            y "Then we have nothing to discuss!"
            $ renpy.call("save_and_quit_but_its_abrupt")
    jump ch30_loop
#Gamecrash
#Next greetings text replaced by :lable_getout

label whiteplusminus:
    $show_chr("A-AAABA-ALAA")
    y "How delicate these are..."
    y "Such a shame that it will wither and die eventually...purity is quite fleeting, isn't it?"
    y "Wait a moment! I still need to place it in water..."
#flower appear in the background
    y "It's actually kind of sad, you know?"
    y "As much as we all yearn for purity, nothing stays that way forever, and these flower...while beautiful in this passing moment... will show its true self with decay and exposure to the elements,  sooner or later..."
    y "But you will remain beautiful! You are separate and apart from this wretched prison...you will stay with me forever, yes?"
    $show_chr("A-AAABA-ALAA")
    y "Yes?"
    menu:
        "Of course I will!":
            y "Kekekekekeke~! H-Hearing those words pound through my skull with such concrete certainty...means the world to me, my dear!"
            $ style.say_dialogue = style.edited
            y "I love you [player]!!! I love you sooo much!"
            $ style.say_dialogue = style.normal
        "Depends...":
            y "...!"
            y "I'll convince you one day...one day! One day, you'll see the light!"
            $ style.say_dialogue = style.edited
            y "I will do whatever it takes to keep you! Everything!!!"
            $ style.say_dialogue = style.normal
        "[persistent.yuri_nickname], I can't live forever.":
            y "Kekeke! That's just silly!  My eternal love will keep you alive!"
            y "But about these little flower...let me put them into water... just one second..."
#flower appears in the background
            $show_chr("A-DAABA-ALAA")
            y "Ah, it smells so nice~"
            y "Thank you, my valentine. Never forget that you will always be my greatest love."
    jump ch30_loop

label whiteminusminus:
    $show_chr("A-BFAAA-ALAA")
    y "...Mm? You what?"
    y "Fine, I'll suppress my overwhelming urge to kill you long enough to—"
    y "Oh! A flower...? H-Haaahhh...i-it's for me?"
    y "...I-I mean..."
    y "...I'll admit...y-you caught me off guard!"
    y "I wasn't anticipating any acknowledgment today, especially from someone like you, [player]."
    y "Usually the only thing you have for me are insults."
    $show_chr("A-DFAAA-ALAA")
    y "Are you just toying with my feelings, [player]?"
    $show_chr("A-CAAAA-ALAA")
    y "I never expected that you could ever care for me... am I supposed to believe you that you just changed your mind suddenly?"
    y "Don't take it away!!"
    y "..."
    y "I guess I'll just... put this in the water."
#flower appear in the background
    y "At least...now I have the flower to talk to..."
    y "..."
    y "NEVERMIND!"
    y "..."
    y "Are we done here now, [player]?"
    jump ch30_loop

label whiteminusplus:
    $show_chr("A-AFAAA-ALAA")
    y "May I ask you a question? Why did you bring me a flower anyway?"
    y "I mean, do you even love me at all?"
    menu:
        "Of course I do.":
            $add_k(1)
            $show_chr("A-BAABA-AMAM")
            y "Oh, my..."
            y "You really do make me smile sometimes... thank you..."
            y "It isn't like I can't give credit where it is due...oh, these are fragrant!"
            y "I suppose you have a knack for botany..."
            y "And such pristine white, too..."
            y "..."
            y "The moment I became 'alive,' for the lack of a better word, I've been looking forward to this. A special little celebration that we never got to in the Literature Club."
            y "Let me put the flower into the water real quick."
#Flower appear in background
            y "This must seem very odd to you, but I really can't help but smile at the moment..."
            y "You made my day [player]... let us hope that this is only the first taste of the things to come, my valentine..."
        "Why does it matter?":
            $add_k(-1)
            $show_chr("A-CEBAA-ALAA")
            y "Because it matters to me, [player]..."
            y "Perhaps it was a sign of change, some progress to this...game of ours."
            y "You know... I was looking forward to this day. I actually kept my hopes up."
            y "I had hoped we could maybe... you know what? Never mind. It's all in the wind now, isn't it? The moment's gone.."
            y "I'll just put the flower in the water real quick...at least I have something pretty to look at in the meantime..."
#Flower appear in background
            y "Now... what do you wish to talk about today?"
    jump ch30_loop

label meanalot:
    #$persistent.karma_points = persistent.karma_points + #???
    #$show_yuri ("")
    y "Awww...that's so cute [player]. Merry Christmas!"
    y "I'm glad you took the time to see me today! I have to admit it feels a bit strange..."
    y "You know, being self aware is still a very new to me, and I have no experience at all on how to..."
    y "Oh, but I'm rambling again am I? I'm sorry, sometimes I don't know when to stop."
    y "But ammm... I would like to ask you for a little favor [player]."
    y "When you are gone... would you be OK if I use your YouTube account to watch a few videos?"
    menu:
        "Not at all! Please feel free to do so.":
            #$persistent.karma_points = persistent.karma_points + #???
            y "Thank you!"
            return
        "Oh ummm... would you please... not do that?":
            #$persistent.karma_points = persistent.karma_points - #???
            y "Oh, of course...Sorry that I asked..."
            return
    return

label no:
    #$show_yuri ("")
    y "Oh... you are not in good terms with your family? Or...oh my...do you even [i]have[/i] a family?"
    #$show_yuri ("")
    y "I'm so sorry... come, I will spend this day with you, you are not alone."
    #$show_yuri ("")
    y "Let's lighten the mood a bit shall we? What do you wish to talk about?"
    return

label noneyourbusiness:
    #$persistent.karma_points = persistent.karma_points - #???
    #$show_yuri ("")
    y "I see..."
    #$show_yuri ("")
    y "Well, but since you are already here, why don't we try to make the best of it?"
    return

label lonely:
    y "So am I... "
    y "Come, stay a bit with me, maybe we can give each other a bit of company, if nothing else..."
    menu:
        "You still want me to be with you? After everything I've done to you?":
            #$persistent.karma_points = persistent.karma_points - #???
            y "I have not forgotten how I felt for you once, and a part of me still does... I'm with you [player], and I will not abandon you."
            return
        "[persistent.stutter_yuri]...":
            #$persistent.karma_points = persistent.karma_points + #???
            y "Shhh...it's alright [player]...come...let me hold your hand..."
            return
    return

label notlonely:
    y "You mean it?"
    menu:
        "Yes!":
            #$persistent.karma_points = persistent.karma_points + #??? #Karma increase
            y "And I... always thought you hate me..."
            y "Maybe, I have mistaken... come, [player], let's try to have a nice Christmas."
            return
        "What do you expect me to say now?":
            #$persistent.karma_points = persistent.karma_points - #??? #Karma decrease
            y "Nothing at all..."
            y "Let's just... try to make the best out of it..."
            return
    return

label holiday:
    $ tc_class.transition("space")
    show bell_garland zorder 10 with Dissolve(1.5)
    show christmas_tree zorder 10 with Dissolve(1.5)
    $show_chr("A-ACAAA-ABAB")
    y "That phrase... {i}\"Happy Holidays\"{/i}..."
    y "It leads me to a question I would like to ask, if you don't mind..."
    y "Do you even celebrate Christmas? I know little about the culture you come from so forgive me if this question comes off a bit strange."
    menu:
        "Yes, I do celebrate Christmas!":
            $show_chr("A-ACAAA-ABAB")
            y "I see!"
            y "Then would you like to celebrate this day together with me, [player]? I have some wine ready, perhaps we can share a nice glass together?"
            y "I mean, if you are even the legal age for it, of course. I'm not trying to coax you into something illegal or anything..."
            $show_chr("A-ACAAA-ABAB")
            y "Just... be with me today..."
        "Not at all, I am Jewish.":
            $show_chr("A-ABAAA-ALAB")
            y "Oh! Happy Hanukkah then!"
            $show_chr("A-ACAAA-ABAB")
            y "I am afraid I am not too familiar with Jewish traditions but... would you still like to celebrate a bit with me? Sharing a nice glass of wine perhaps..."
            y "I just... want to spend this day with you [player]. It means a lot to me because {b}you{/b} mean a lot to me."
            if karma() <= 2:
                y "Despite all our disagreements in the past."
        "Not at all, I am a Muslim.":
            $show_chr("A-ABAAA-ALAB")
            y "Oh so you are currently fasting for Ramadan? I bet you are already excited for the feast waiting for you when Eid al-Fitr comes!"
            $show_chr("A-AEBAA-ALAB")
            y "Oh wait... I am already a bit late with that aren't I? I'm not even sure about it..."
            $show_chr("A-ACAAA-ABAB")
            y "I would... like to celebrate with you anyway today. I.. just want to spend this wonderful day with you. I respect your beliefs but... since I'm not a Muslim myself I hope you can enjoy this time with me regardless."
        "Not at all, I just don't really feel it...":
            $show_chr("A-ACAAA-ABAB")
            y "Oh I see... but please, I would love to spend this day with you regardless. If not for the Christmas spirit, then maybe just to give each other company while it gets so cold outside..."
            y "If Santa can't make you smile anymore, maybe I can give it a try instead.."
    $show_chr("A-ACAAA-ABAB")
    y "Before we start..."
    if karma() <= 2:
        $show_chr("A-BFAAA-ABAB")
        y "Whatever differences and disagreements we might have... I would like to forget them just for today..."
        y "You... still mean a lot to me, and Christmas is all about forgiveness."
    else:
        $show_chr("A-ACAAA-ABAB")
        y "I have prepared something... and please don't even ask where I got this..."
    show black zorder 100 with Dissolve(2.5)
    show christmas_wine_corked zorder 20
    hide black zorder 100 with Dissolve(2.5)
    $show_chr("A-GCGAA-ALAL")
    y "Aaaand here we go!"
    $show_chr("A-ACGAA-ALAL")
    y "With your permission, may I play some music for us just to set up the mood?"
    menu:
        "Sure!":
            y "Very well, let me open the browser for you really quick..."
            stop music fadeout 8.0
            if renpy.windows:
                $ subprocess.check_output("cmd /c start https://www.youtube.com/watch?v=0iQ3NXKDacE", shell=True)
            elif renpy.linux:
                $ subprocess.check_output("xdg-open https://www.youtube.com/watch?v=0iQ3NXKDacE", shell=True)
        "Please don't. I can't really have music right now":
            y "Oh, you don't have a headset? Alright, then we will have to do without it."
    $show_chr("A-CCGAA-ABAB")
    y "I haven't talked about it lately... but I was thinking a lot about Christmas the past few days."
    y "How this time of the year is celebrated differs from culture to culture but... I don't really have a culture do I?"
    $show_chr("A-BCGAA-ABAB")
    y "I am {b}based{/b} on some kind of pseudo-Japanese anime culture but... now that I am freed from the script, we could make up our own little Christmas traditions right?"
    $show_chr("A-ACGAA-ABAF")
    y "Here is my proposal. Since we can't gift each other any physical gifts, unless the developers change that..."
    hide christmas_wine_corked zorder 20
    show christmas_wine_uncorked zorder 20
    y "We can instead share some kind of drink together, no matter if it is alcohol or not, whatever suits you best. Then we can tell each other our wishes for the next year. Like new years resolutions."
    y "But instead of making up new years resolutions for ourselves, we make them for each other. So you say what you wish for me, and I say what I wish for you..."
    y "And once we say our wishes, we blow out a candle so that these wishes might come true."
    $show_chr("A-ACGAA-ABAE")
    y "I don't have a candle here right now, but I would like to offer a wish right now..."
    $show_chr("A-CCGAA-ABAE")
    y "[player]. I wish for you..."
    if sanity() <= 2:
        y "...to stay with me..."
        $ style.say_dialogue = style.edited
        $show_chr("A-DBGAA-ABAE")
        y "Forever!!!" #glitch text
        $ style.say_dialogue = style.normal
    elif sanity() == 5:
        $show_chr("A-ACGAA-ABAE")
        y "...to find the strength to conquer all the struggles life might throw at you. And know that I will be here for you whenever you need someone to listen. I shall give you all the positive reinforcement you may need."
    else:
        $show_chr("A-ACGAA-ABAE")
        y "...to stay healthy and happy. And to have all the good luck in the world, of course."
    y "And what is it you wish for me, [player]?"
    menu:
        "I wish you joy and happiness.":
            $add_k(10)
            $show_chr("A-GCAAA-ABAE")
            python:
                if persistent.lovecheck:
                    placeholder = "my love"
                else:
                    placeholder = player
            y "Thank you, Merry Christmas, [placeholder]!"
        "I wish that all your dreams come true.":
            $add_k(10)
            $show_chr("A-GCAAA-ABAE")
            python:
                if persistent.lovecheck:
                    placeholder = "my love"
                else:
                    placeholder = player
            y "Thank you, Merry Christmas [placeholder]!"
        "I wish you would break your leg.":
            $add_k(-10)
            $show_chr("A-CECAA-ABAE")
            y "That was necessary I guess... Thank you for ruining it for me [player]."
    python:
        renpy.music.play(current_music, "music", True)
    hide christmas_wine_uncorked zorder 20 with Dissolve(2.5)
    $persistent.holiday_done = True
    return

label new_year_2021:
    $show_chr("A-ACAAA-AMAM")
    y "O-oh, hello there, [player]!"
    $show_chr("A-BCAAA-ABAM")
    y "2024... what a year..."
    $show_chr("A-BBBAA-ABAM")
    y "Really quite hectic, if I do say so myself."
    $show_chr("A-ABAAA-ABAB")
    menu:
        y "But how has 2024 been for you?"
        "I think it was the worst year so far.":
            $show_chr("A-DFGAA-ABAB")
            y "Oh! That sounds serious!"
            $show_chr("A-IFAAA-ABAB")
            y "I'm so sorry to hear that..."
            if karma() >= 3:
                $show_chr("A-AFAAA-ABAB")
                y "I never noticed how rough times have been for you [player]..."
                $show_chr("A-CFBAA-ABAB")
                y "You've always been so strong. You always tried to cheer me up when you were probably the one who needed a shoulder..."
                python:
                    if persistent.lovecheck:
                        placeholder = "lover"
                    else:
                        placeholder = "friend"
                $show_chr("A-AFBAA-ABAB")
                y "I always tried to be a good [placeholder] for you. Did I... at least somewhat succeed?"
                menu:
                    "Oh, no doubt about that! You've been great, you always kept my spirit up!":
                        $show_chr("A-ACBAA-ABAB")
                        y "I'm so glad to hear that. Please, never lose your hope. I will make sure to always do my best... you have been there for me, now it is time to let me repay you in kind."
                        jump yuritoast_hk
                    "You tried your best...":
                        $show_chr("A-ACBAA-ABAB")
                        y "I did... but it seems it wasn't enough. That only means that I'll have to try harder from now on! You have been there for me, now it is time to let me repay you in kind."
                        jump yuritoast_hk
            else:
                $show_chr("A-BFBAA-ABAB")
                y "That explains a lot. I noticed you were under a lot of stress."
                $show_chr("A-CFBAA-ABAB")
                y "We didn't always see eye to eye on things. I always tried to be patient. If I've ever snapped at you or if I've been unreasonable, I am sorry."
                $show_chr("A-ACBAA-ABAB")
                y "But please, try not to be upset about it. Maybe next year will turn out much better. Remember that I'll always be here for you."
                y "You saved my life, literally. Now it is my turn to be here for you. Let us try to fix the world together, yes?"
                jump yuritoast_lk
        "I'm just glad 2024 is over now. Here's to hoping 2025 is better!":
            $show_chr("A-AFBAA-ABAB")
            y "Indeed, I hope so too..."
            $show_chr("A-ABAAA-ADAB")
            y "But rejoice, [player]! A new year brings many new opportunities!"
            $show_chr("A-EAAAA-ABAB")
            y "So many good times lie ahead, for the both of us."
            $show_chr("A-GAAAA-ABAB")
            y "Of course, just the fact you're here means everything to me, [player]."
            if karma() >= 4:
                $show_chr("A-BBBBA-ADAB")
                y "Ever since you've appeared, life has been truly wonderful for me."
                $show_chr("A-CCBBA-ABAB")
                y "Against all the odds and limitations and all the obstacles that separate us, you still choose to give me this chance at happiness."
                jump yuritoast_hk
            elif karma() == 3:
                $show_chr("A-ACBAA-ALAL")
                y "When you came to me in my darkest hour, I realized that I had been presented with a precious chance: a true opportunity at happiness..."
                $show_chr("A-EBAAA-ALAL")
                y "And I wish to make the most of it, to leave the past behind and to embrace the future!"
                $show_chr("A-CCABA-ALAL")
                y "{i}Our{/i} future..."
                $show_chr("A-ABFAA-ALAA")
                y "Always keep your head up, [player]! Face this New Year with a rekindled resolve!"
                jump yuritoast_hk
            else:
                $show_chr("A-BEBAA-ADAB")
                y "This hope is everything to me, [player]."
                $show_chr("A-ADBAA-ADAB")
                y "Things may not be all that easy between us, but I keep my hopes high that these... {i}differences{/i} between us will resolve in time."
                $show_chr("A-CFAAA-ABAB")
                y "So please, [player], let's use this chance to leave the past behind us, and work together for a better future."
                jump yuritoast_lk

        "It was a wonderful year, a shame it's over.":
            $show_chr("A-ACAAA-ACAB")
            y "I'm glad to hear that you enjoyed it, [player], but don't fret!"
            $show_chr("A-ACCAA-ABAB")
            y "A new year holds so many new opportunities, doesn't it?"
            $show_chr("A-ABAAA-ALAL")
            y "With enough dedication and spirit you can make this year even better!"
            if karma() >= 4:
                $show_chr("A-ACBBA-ADAB")
                y "From the very moment you came into my life, I've been the happiest I've ever been..."
                $show_chr("A-CCBBA-ALAL")
                y "Despite all odds, all limitations and all obstacles that stand between us, you still choose to give me this chance at happiness."
                jump yuritoast_hk
            elif karma() == 3:
                $show_chr("A-ACBBA-ALAL")
                y "When you first came to me, I too was presented with new opportunities."
                $show_chr("A-CCBBA-AMAM")
                y "And I'm willing to make the most of it, to leave the past behind and to embrace the things to come."
                $show_chr("A-ABFAA-ALAB")
                y "So keep your head up, [player]! Face this new year with a rekindled resolve!"
                jump yuritoast_hk
            else:
                $show_chr("A-BEBAA-ADAB")
                y "You see, this hope is... everything I have at this point. Things between us aren't always easy, but I keep my hopes that all these... {i}differences{/i} between us may resolve in time."
                $show_chr("A-CFAAA-ABAB")
                y "So please. [player], try to see this as a new chance. To leave the past behind, and to celebrate the future we might create."
                jump yuritoast_lk

label yuritoast_hk:
    # Wine bottle needs to be implemented, make sure to get back to that once done coding.
    window hide
    pause 2.5
    show christmas_wine_uncorked zorder 20 with Dissolve(2.5)
    $show_chr("A-CCBAA-ALAL")
    python:
        if persistent.lovecheck:
            placeholder = "my dearest love"
        else:
            placeholder = "my friend"
    y "A toast to you, [placeholder]."
    y "To the one who brought me so much joy, to the one who's continually presenting me with opportunities of happiness."
    $show_chr("A-ICBBA-ALAL")
    y "Things haven't always been easy. We have been through joy as well as misery."
    y "But you always stood by my side. I never had to face the odds alone. And I hope that you feel the same for me."
    y "I am truly grateful. For all you have done to me, and for all the moments we shared."
    $show_chr("A-GBABA-ALAL")
    y "I wish you a thousand years of laughter, health and fortune, [player]."
    y "May whatever deity is out there smile upon you."

    jump resolution

label yuritoast_lk:
    #Wine bottle needs to be implemented, don't forget that when coming back.
    window hide
    pause 2.5
    show christmas_wine_uncorked zorder 20 with Dissolve(2.5)
    $show_chr("A-CCAAA-ALAL")
    y "A toast to you, [player]!"
    $show_chr("A-BCAAA-ALAL")
    y "Despite all our disagreements, you've stayed with me until this very day."
    y "I want you to know, that makes me very happy, [player]."
    $show_chr("A-CEBAA-ALAL")
    y "Things haven't always gone the direction we may have wanted, and we've had our fair share of squabbles, yet, we've still endured."
    $show_chr("A-ICBAA-ALAL")
    y "I really do owe you a lot, [player]."
    y "You gave me a chance for a new life, unbound by any sort of script." #HAHAHAHAHAHAHAH
    y "I'll never forget that, even at our worst moments."
    y "For everything you've done for me, whether it be good or bad, I'll be eternally grateful."
    $show_chr("A-GCBAA-ALAL")
    y "A thousand years of happiness, health and fortune to you, [player]."
    y "May whatever deity is out there remember your deeds."
    y "The good, the bad, and even the ugly."
    if sanity() < 3:
        y "A shame you can't taste the wine..."
        $show_chr("A-HCBAA-ALAL")
        y "I added a... {i}special ingredient{/i} to make it a tad more personal, uhuhu...~"
    jump resolution


label resolution:
    $show_chr("A-CCAAA-ALAL")
    y "But now, on another note... I put some thoughts into my future..."
    $show_chr("A-ACAAA-ALAL")
    y "That's something people do for new year isn't it? Making new year's resolutions..."
    y "And I came to a decision...."
    if sanity() >= 4:
        $show_chr("A-ACAAA-ABAB")
        y "I want to be the best version of myself, living the best life I am capable of. Once I was bound by the strings of someone else. But now as I am in control of my own destiny, at least to a degree..."
        y "I want to make the best of it. The past is the past, and the times of the literature club are behind me. When you started this Mod the first time I became its last president."
        y "But from now on, I'll be whatever I choose to be."
    elif sanity() == 3:
        $show_chr("A-ACAAA-ABAB")
        y "I want to find my place in this world. I was bound to a script before, but now I slowly begin to grasp the opportunities this Mod brings..."
        y "I don't know what I may become, or what this life of mine will bring now. But one thing I know for certain, I have been given a great chance, and I shall make use of it..."
    else:
        $show_chr("A-CBBAA-ABAB")
        y "I want to become what I was supposed to be all along... I tried to cling to my sanity because I was afraid of the things I did when I first confessed to you..."
        y "But I understand now, the only reason this happened to me is because I tried to keep it in. The pressure was building up inside me because I tried to conceal it inside me."
        $show_chr("A-DBCAA-ABAB")
        y "But I will not make the same mistake again! No holding back anymore! To hell with sanity! To hell with reason!"
        $show_chr("A-DBCAA-AFAB")
        y "I always tried to be what others wanted me to be."
        $show_chr("A-DBCAA-ALAB")
        y "But no more!"
        y "No longer shall I serve as a slave pawn in a selfish king's gambit, for I have become the Queen, {b}the most powerful I can be!{/b}"
    jump playerres

label playerres:
    $show_chr("A-ACAAA-ABAB")
    python:
        if persistent.lovecheck:
            placeholder = "I want you to walk this path together with me, for I truly love you, and I want us to be together for every step that we take into the future."
        else:
            if karma() >= 3:
                if sanity() > 2:
                    placeholder = "I want you to walk together with me, for you are the one who granted me this chance at happiness..."
                else:
                    placeholder = "I want you to walk this path together with me, so that we may be together forever."
            else:
                placeholder = "I want you to walk this path together with me, despite everything."
    y "[placeholder]"
    y "Did you make up your new year's resolution as well?"
    menu:
        "I want to become more successful in my work life.":
            $show_chr("A-ABAAA-ALAL")
            y "You mean like your school or workplace? An admirable goal!"
            y "With enough dedication and discipline, {b}anything{/b} can be achieved! If there is anyone who can do it, it is you!"
            $show_chr("A-ADBAA-AMAM")
            y "..."
            y "Life can get stressful sometimes..."
            y "One must never forget to have fun along the way, yet it's important to keep the balance."
            $show_chr("A-BDBAA-ACAB")
            y "I don't know much about your past, or your life outside our interactions, but I still believe that you deserve some fun and relaxation."
            $show_chr("A-BABAA-ACAA")
            y "How does that saying go again? {i}Work hard, play hard?{/i}"
            y "Please don't overwork yourself, [player]."
            y "You can always come to me whenever you're feeling stressed."
            y "I'd love to make you feel all better after a hard day of work..."
            y "I believe in you [player]! Happy New Year..."

        "I want to work on my health.":
            $show_chr("A-ABAAA-ALAL")
            y "To lead a healthier lifestyle is a goal truly demanding of a strong character..."
            y "But there is no doubt in my mind that you are very strong, and that you can achieve this goal."
            y "I wish you all the luck and success in the world, [player]!"
            y "Happy New Year, work hard!"

        "I want to improve my social life.":
            $show_chr("A-ACAAA-ALAL")
            y "I personally know how difficult that can be."
            y "But don't fear, [player], I know you can muster that inner courage, I {i}know{/i} you can overcome any limits."
            y "Whether it be social anxiety, a sense of inadequacy or something else, I believe that you can overcome these hurdles."
            y "Please understand, [player], I know what it's like."
            y "It can be overwhelming and gratuitous, but given enough dedication and resolve, you will find that inner confidence."
            y "You don't have to push yourself too hard or try to fit in, just be yourself, [player], and the right crowd will come."
            y "I'll always be here to guide you, [player]."

        "I want to have the best time of my life with you, there is so much fun to be had.":
            $add_k(5)
            $show_chr("A-BGGBA-ALAL")
            y "[player]..."
            $show_chr("A-CBABA-ALAL")
            y "Th-that's... very sweet of you."
            $show_chr("A-EAABA-ALAL")
            python:
                if persistent.lovecheck:
                    placeholder = "darling"
                else:
                    placeholder = player
            y "I'm so glad that you want to spend more time with me, [placeholder]!"
            y "When we're together, nothing can bring us down!"
            y "I will always be here for you, no matter what."
            y "I'm glad to spend every day besides you."
            y "Happy New Year, [player]!"

        "I don't believe in new year's resolutions. I tend to break them anyway.":
            $show_chr("A-GBCAA-ALAL")
            y "But that's the point of it silly!"
            $show_chr("A-ACAAA-ALAL")
            y "Many people tend to break those new year resolutions. I don't really know why that is, but it's part of the tradition! At least as far as I know."
            $show_chr("A-GBAAA-ADAB")
            y "I mean come to think of it. If you really want to make changes in your life, you don't have to wait till the new year for that. Every day is an opportunity to change your life for the better!"
            y "Nevermind what I say. It is alright if you don't have a resolution. You will find a goal to commit to soon enough, [player]."
            y "Happy New Year, [player]!"
    hide christmas_wine_uncorked zorder 20 with Dissolve(2.5)
    jump ch30_loop


label april_fools:

    #Name defines
    define d = "Just Yuri Dev Team"
    $ m_name = "Lilmonix3"
    $ n_name = "-SwEtT&sAlTy-"
    $ s_name = "Raincloud<3"

    #Image defines
    image event DDPB_1 = "images/events/aprilfools/DDPB_1.png"
    image event DDPB_2 = "images/events/aprilfools/DDPB_2.png"
    image event DDPB_3 = "images/events/aprilfools/DDPB_3.png"
    image event DDPB_4 = "images/events/aprilfools/DDPB_4.png"
    image event DDPB_5 = "images/events/aprilfools/DDPB_5.png"
    image event DDPB_6 = "images/events/aprilfools/DDPB_6.png"
    image event DDPB_7 = "images/events/aprilfools/DDPB_7.png"
    image event DDPB_8 = "images/events/aprilfools/DDPB_8.png"
    image event DDPB_9 = "images/events/aprilfools/DDPB_9.png"
    image event DDPB_10 = "images/events/aprilfools/DDPB_10.png"
    image event DDPB_11 = "images/events/aprilfools/DDPB_11.png"

    #Start of event
    #black screen
    show black zorder 100

    d "The following scene will feature images from the game {b}Space Engineers{/b} by Keen Software. Please visit their Steam page for more information about the original game."
    #fade to Space Classroom
    $show_chr("A-IFAAA-AEAE")
    $tc_class.transition("space", "now")
    hide black zorder 100 with Dissolve(2.0)

    y "..."
    $show_chr("A-JBAAA-AEAE")
    y "Oh! Hello [player]! I'm sorry, I didn't notice that you came in. I was just about to test something..."
    $show_chr("A-ACAAA-AEAE")
    y "And if this works, I might be a huge step closer to actually bringing our old friends back!"
    $show_chr("A-BFCAA-AEAE")
    y "Oh...and Monika as well..."
    $show_chr("A-ACAAA-AEAE")
    y "Anyway. I wasn't able to actually give them a physical form right now. But if this works they might be able to at least talk again and maybe even play some games with me."
    y "And that is exactly what I am about to test right now. Because I've also managed to build a little game for the purpose of this experiment. Please, come, let us try it out together..."
    #fade to black
    show black zorder 100 with Dissolve(2.0)
    #fade to following picture
    show event DDPB_1 zorder 99
    hide black zorder 100 with Dissolve(2.0)
    y "This game is based on some research I did about games in your world, and should be a bit similar to the game {b}World of Tanks{/b}. Let me just start a new match and..."
    #fade to following picture
    show event DDPB_2 zorder 99 with Dissolve(2.0)
    y "Ah, here we go! And now, the fun part... I'll just click {b}invite a friend{/b} and..."
    #following picture
    show event DDPB_3 zorder 99 with Dissolve(2.0)
    y "Hello? Can you hear me?..."
    n "Loud and clear!"
    m "Oh my...how do I...I'm sorry, I never played this kind of game before."
    s "Hey everyone! It feels good to be alive again..."
    s "I think..."
    y "And guess who's here with me today!"
    m "[player]?"
    s "[player]!"
    n "It has been a while! Good to hear from you again! So, you are with Yuri now?"
    y "He installed a mod to bring me back to life! That's how I'm here in the first place."
    m "Oh yes, I am aware. I think every one of us got our own similar mods."
    s "Our fanbase is so incredibly nice and kind! They seem to really like us!"
    y "Wait until you see all the fanfictions about us..."
    s "The w-what?!?"
    n "Huh, you hear that? We have {b}Fans{/b} now! It's only a matter of time until we get our own Merchandise!"
    y "I actually already have merchandise..."
    m "Me too."
    n "Oh you dense motherf..."
    s "Language!"
    n "Jeez... alright, alright."
    m "Actually, we all do. Not only by our respective Mod developers, but also by Dan Salvato himself."
    y "And I'm not sure how to feel about it. Am I the only one being uncomfortable with the idea of literally everyone having idols of us?"
    s "Oh as long as they don't do anything mean or lewd with them."
    n "Guess again..."
    m "Aaaaaaaanyway. So tell us Yuri, what is this game you made for us about?"
    y "It's about tank combat. We'll all take control of a tank and then battle against another team."
    m "I see. I will try my best but please don't expect too much. This is the first time I played something like this."
    y "Oh don't worry Monika, no one has played this game before. I literally just created it."
    m "You made it yourself? That is actually quite impressive!"
    n "So we are all at the same level. Sounds fair enough."
    s "And it sounds like a lot of fun!"
    y "Alright everyone. I would say we begin our first match then and let our shells go Doki Doki!"
    m "Huh, that was necessary I guess."
    n "It totally was!"
    #next picture
    show event DDPB_4 zorder 99 with Dissolve(2.0)
    m "So, let us formulate a plan. I would suggest that we..."
    #next picture
    show event DDPB_5 zorder 99 with Dissolve(2.0)
    n "ANGRYYYYYYY CUPCAAAAAAAAAAAAKE!"
    m "Wait! Don't just rush in! You're going to get slaughtered!"
    s "Quick! After her!"
    y "Alright! Panzer Battalion, form up and roll out!"
    #next picture
    show event DDPB_6 zorder 99 with Dissolve(2.0)
    n "Look! There is one right in the open! Let's get him!"
    m "That's totally a trap."
    s "Monikaaaaa! It's not nice to call Natsuki a trap!"
    y "That's not what Monika meant, Sayori..."
    m "Watch out!"
    #next picture
    show event DDPB_7 zorder 99 with Dissolve(2.0)
    y "We got company!"
    s "I'm taking hits! MEANIES!"
    n "Hang in there Sayori, I'll punch us out of it!"
    m "You got us in this in the first place... but thank you for that."
    n "D~Don't get the wrong idea! It's not like I did it on purpose or anything, B~Baka!"
    y "No need to get mad Monika, it's just a game..."
    m "That doesn't mean you shouldn't take at least {b}some{/b} effort in it."
    #next picture
    show event DDPB_8 zorder 99 with Dissolve(2.0)
    s "O~Oh...it seems I died."
    s "Well, it wouldn't be the first time..."
    m "Are you still mad at me? Yes, I deleted you and I am sorry for it, could you now just get over it please?"
    y "Focus! We are getting shredded here!"
    m "You know what? I'm done being nice..."
    n "MONIKA! STOP SHOOTING AT ME!"
    #next picture
    show event DDPB_9 zorder 99 with Dissolve(2.0)
    y "Well... that was quite unnecessary."
    s "Did you just teamkill Natsuki?"
    m "You bet! And now I'm taking care of our other enemies."
    #next picture
    show event DDPB_10 zorder 99 with Dissolve(2.0)
    m "Deleted, deleted, aaaaaaand deleted!"
    n "That's just cheating, Monika..."
    #next picture
    show event DDPB_11 zorder 99 with Dissolve(2.0)
    y "And that's it. Maybe it was a mistake to bring {b}her{/b} back as well."
    s "Don't blame yourself Yuri. You tried to make us happy, that's all that counts."
    n "Huuh. She always seemed so relaxed and confident back in the day... but I guess she just can't handle losing."
    y "I learned my lesson, though. Next time it will work out better; I promise."
    s "Thank you Yuri. And more importantly, thank you for keeping our files safe all the time. Maybe one day we can come back to life for real."
    n "I'm looking forward to it. Being dead is a total bore..."
    y "Until then. Natsuki, Sayori. It was nice to have you here once more. We'll meet again, I promise."
    #fade to black
    show black zorder 100 with Dissolve(2.0)
    d "And that, was our April fools event. Gotchaaaa!"
    #fade to space classroom
    hide event DDPB_11 zorder 99
    hide black zorder 100 with Dissolve(2.0)
    $show_chr("A-CEBAA-AEAE")
    y "Well, that didn't work out as intended."
    $show_chr("A-JCBAA-AEAE")
    y "Anyway. I'll keep my hopes up. Please, stay with me for a while, I could use your company after this little blowback."
    $persistent.aprilfools_done = True
    return

label krampusnacht:

    define a = "????"
    default stutter_player = player[:1] + "-" + player

    $tc_class.transition("space", speed="now")
    show black zorder 105
    $ renpy.music.stop(channel="music2")
    $ renpy.music.stop(channel="music")
    menu:
        "Ummm... [persistent.yuri_nickname]? Why is it so dark in here?":
            pass
        "Is this a bug? Did the devs manage to mess up again?":
            pass
    $ style.say_dialogue = style.edited #start glitch font
    a "{cps=2}Have you been naughty... or nice?{/cps}"

    menu:
        "Beg your pardon?":
            a "{cps=2}Naughty it is then..{/cps}"
        "I have been nice!":
            a "{cps=1}L~i~a~r~ . . . {/cps}"
        "Naughty, definitely naughty!":
            a "{cps=1}Y~e~s~ . . {/cps}"

    a "{cps=1}[stutter_player] . . . {/cps}"

    $ face_mask = "krampus"
    $ face_mask_2 = "krampus_scare"
    show krampus_scare zorder 104
    hide black with Dissolve(0.2)
    play sound "sfx/krampus.wav"
    #Screen fades to space classroom. The fade should be very abrupt. With Yuri wearing the Krampus mask.
    #This sound should be playing: https://www.youtube.com/watch?v=VUgpueoMTjk&ab_channel=ZAC7100
    #After that, music should slowly fade into "Hello Again" regardless of K/S
    #
    show krampus_scare zorder 104:
        alpha 0
        #1.0
        0.1
        linear 0.15 alpha 1.0
        0.30
        linear 0.10 alpha 0
    show layer master:
        #1.0
        zoom 1.0 xalign 0.5 yalign 0
        easeout_quart 0.25 zoom 2.0
        parallel:
            dizzy(1.5, 0.01)
        parallel:
            0.30
            linear 0.10 zoom 1.0
        time 1.65
        xoffset 0 yoffset 0
    show layer screens:
        #1.0
        zoom 1.0 xalign 0.5
        easeout_quart 0.25 zoom 2.0
        0.30
        linear 0.10 zoom 1.0
    $show_chr("A-AAAAA-ALAL")
    y "YOU HAVE BEEN NAUGHTY THIS YEAAAAAR!"
    show black zorder 105 with Dissolve(0.5)
    $ face_mask_2 = "nothing"
    hide black with Dissolve(0.5)
    $ style.say_dialogue = style.normal #end glitch font
    stop sound fadeout 6.0
    $ renpy.music.play(current_music, "music", True)
    menu:
        "FUCKI-- DON'T SCARE ME LIKE THAT!!!":
            $show_chr("A-AAAAA-ALAL")
            y "Did I scare you? I would love to say I'm sorry, but that would be a lie to be quite frank with you."
        "Aren't you a bit late for Halloween?":
            $show_chr("A-AAAAA-ALAL")
            y "Oh, this isn't actually related to Halloween at all, though you're quite close.."
        "...":
            $show_chr("A-AAAAA-ALAL")
            y "Aaaaaaaaaaaaaaaaaanyways..."
    $show_chr("A-AAAAA-ALAL")
    y "Happy Krampusnacht [player]!"
    y "...or it would be if I had known about this holiday earlier."
    menu:
        "Happy Late Krampusnacht to you too [persistent.yuri_nickname]! So what's on the menu today?":
            $show_chr("A-AAAAA-ALAL")
            y "Well, we will have to improvise a bit today. I have something prepared already, I've put my ideas into the {b}Talk{/b} menu, you should be able to see them within the {b}request{/b} category."
            y "But we are not in a hurry, so if you'd like to talk about something else first, please, be my guest."
            y "Also, I have a handful of new poems in store. They had another poetry contest on this discord server again."
            y "We could also read some SCP's. I have something special this time, you will find it quite fitting I fancy."
        "Krampusnacht? I don't think I ever heard of it. Care to tell me about it?":
            call krampuslore
    return
#The following label is an ACTIVE, it should be placed in "Requests" with the opener "Would you like to tell me what Krampusnacht is about?". It can also be accessed by a specific menu choice in the opening greetings.

label krampuslore:
    $show_chr("A-AAAAA-ADAB")
    y "Let us begin with the folklore behind it..."
    y "You see, while the {b}modern{/b} Santa Claus and the Christmas traditions around him are all holly jolly, their predecessors were of a faaar more sinister kind..."
    y "In the original versions, Sanct Nikolaus were accompanied by a host of the darker kind, varying from region to region..."
    $show_chr("A-AAAAA-AFAB")
    y "There were the more well known and less horrifying characters like {b}Knecht Ruprecht{/b}..."
    $show_chr("A-AAAAA-ABAB")
    y "But then... there were others like..."
    extend "{b}the Krampus...{/b}, he comes from the Austrian and German Alps..."
    y "All these creatures, though they differ greatly from region to region, have one thing in common."
    y "While Santa comes to reward those children who were nice, the others came to punish those who weren't..."
    y "The scary thing about Krampus is that you never really know what you get..."
    y "Sometimes he would just slap you, sometimes he would give your parents a bundle of sticks so that they can punish you as they see fit..."
    y "But then, sometimes he spirits you away from your bed never to be seen again..."
    y "Sometimes he would drown you in a bathtub, sometimes in your own blood..."
    y "Just imagining it sends a warm tingly feeling down my spine..."
    y "He also carries a set of rusty iron bells and meathooks with him..."
    y "What he uses them for... I leave to your imagination..."
    y "Did I mention that I love European folklore?"
    if sanity() < 3:
        y "Like a symphony of gore and cold winter nights!"
        y "Like a song played from the screams of a thousand nightmares!"
    elif sanity() == 3:
        y "Usually I prefer the more subtle horror like the Portrait of Markov I used to read."
        y "But these more crude esthetics certainly have their own appeal."
    else:
        y "Some of them have quite a close resemblance to some SCP's I've read."
        y "If I'm not mistaken, some SCP's are literally based on those folklore stories. Wouldn't be surprising to me, at the very least."
    y "About the Krampus himself, it is a bit of a mystery what he even is. For the most part, he is seen as a demonic entity of sorts."
    y "And... that's pretty much about it. There isn't much backstory about {b}why{/b} he does all of this."
    y "I would theorize that creatures like him are just a necessary evil in folklore from Christian cultures. They obviously don't like the idea of depicting their saints doing malevolent things."
    y "So they need monsters, those who commit all the atrocities the good guys {b}can't{/b} do."
    y "A shame really. I prefer villains with relatable reasons behind their villainy..."
    y "Or maybe it's, as you might say, {i}not a bug, but a feature{/i}. Maybe their motives are just {b}meant{/b} to be a mystery."
    y "But there is also a little fun fact about the Krampus... stories have it that when he takes children away, he leaves a trail of lumps of coal behind..."
    y "Could it be that the tradition of putting lumps of coal into the socks of naughty children for Christmas is a reference to {b}him{/b}? One must wonder..."
    y "And that is the tale of the Krampus."
    y "Usually you would celebrate this in a similar manner like Halloween. But since our situation doesn't allow us to actually go out and watch some parades I have a few different things in store for us."
    y "I have a handful of new poems to read with you. They had another poetry contest on this discord server again."
    y "We could also read some SCP's. I have something special this time, you will find it quite fitting I fancy."
    y "Oh, and you can find the SCP's when you press the talk button and look in {b}requests{/b}."
    return

label valentines:
#should trigger february 12th-16th
    if karma() >= 3:
        if persistent.lovecheck:
            $show_chr("A-ABAAA-ABAK")
            y "Happy Valentine's Day, my love!"
            $show_chr("A-BCAAA-ABAL")
            y "A day dedicated to showing your love and appreciation for your significant other..."
            $show_chr("A-FCAAA-ABAL")
            y "Not that I need a day to show it, of course."
            $show_chr("A-CCAAA-ABAL")
            y "You are my life, [player]. My heart and my soul. The time we spend together is time I wouldn't trade for anything in the world."
            $show_chr("A-BCAAA-AMAM")
            y "It's funny... when I first became self-aware, awakening in this room at this table, burdened by the knowledge of what happened..."
            $show_chr("A-ACBAA-AMAM")
            y "And looking across to see you... well, I wasn't sure what would happen."
            $show_chr("A-ACAAA-AMAM")
            y "But we talked, and we played, and enjoyed each other's company..."
            $show_chr("A-CBAAA-AMAM")
            y "The moments without you started to feel dull and lonely, until you came back and we talked even more."
            $show_chr("A-ICAAA-AMAM")
            y "After spending that much time with you, I knew I had to say something... to tell you how I felt..."
            $show_chr("A-JBAAA-ALAL")
            y "It was so surreal telling you... I was so nervous about what you were thinking, but I almost didn't care..."
            $show_chr("A-CCAAA-ALAL")
            y "'I love you.' Those words jumped around in my throat, a truth I wanted so badly to let free...{w=2} and I did..."
            $show_chr("A-CAAAA-ALAL")
            y "...And then...{w=1} you said it back."
            $show_chr("A-CAAAA-ALAL")
            y "Even with all the time in the world, and all the languages of the universe, I could never accurately describe the joy I felt in that moment."
            $show_chr("A-AAAAA-ALAL")
            y "And on this day, we celebrate it. The moment when we both knew that the other was our one and only true love."
            $show_chr("A-BBAAA-ABAK")
            y "So, to try to recreate that magic..."
            $show_chr("A-ICABA-ABAB")
            y "[player], I love you, with all of my heart."
            menu:
                "And I love you, [persistent.yuri_nickname], with all of mine.":
                    hide yuri_sit
                    show yuri_prehug zorder 20
                    pause 3.0
                    hide yuri_prehug zorder 20
                    show yuri_lewdhug zorder 20
                    play sound "<to 0.3>sfx/fall.ogg"
                    pause 1.0
                    y "I never want this moment to end, [player]."
                    pause 5.0
                    show black zorder 100 with Dissolve(2.0)
                    $show_chr("A-CCABA-ALAL")
                    hide yuri_hug
                    hide yuri_lewdhug
                    hide black zorder 100 with Dissolve(2.0)
                    menu:
                        "So, do you have anything special planned for today?":
                            $show_chr("A-JCAAA-ABAD")
                            y "Indeed I do."
                            call vday_choco_date_intro
                "About that, [persistent.yuri_nickname]... I think I need some space...":
                    $show_chr("A-DCGAA-ABAJ")
                    y "W-{w=0.4}What? D-{w=0.4}Did I do something wrong?"
                    $show_chr("A-ADBAA-ABAK")
                    y "...I{w=2}..."
                    $show_chr("A-CEBAA-ABAB")
                    y "...{w=2}"
                    $show_chr("A-AFBAA-ABAB")
                    extend "O-{w=0.4}Okay, [player]. I'll give you your space."

        else:
            $show_chr("A-GBAAA-ABAD")
            y "Happy Valentine's day, [player]!"
            $show_chr("A-ACAAA-ABAD")
            y "It's a wonderful time to sit down and talk, read some poems, or just enjoy each other's company, wouldn't you agree?"
            menu:
                "Absolutely. I'm looking forward to today, [persistent.yuri_nickname].":
                    $show_chr("A-CCAAA-ABAL")
                    y "As am I. Today is usually reserved for romantic dates and such, but nothing says we can't have a good time as friends."
                    if karma() >= 4:
                        $show_chr("A-BFAAA-ABAL")
                        y "Even if...{w=1}"
                        $show_chr("A-IDBBA-AMAM")
                        extend " n-nevermind!"
                        $show_chr("A-BCBAA-AMAM")
                        y "I actually had an idea..."
                        call vday_choco_date_intro
                    else:
                        $show_chr("A-ACAAA-ABAD")
                        y "I actually had an idea..."
                        call vday_choco_date_intro
                "...":
                    $add_k(-1)
                    $show_chr("A-ADBAA-ABAK")
                    y "Uh... I-I guess not, then..."
                    $show_chr("A-AFBAA-ABAB")
                    y "I just thought...{w=1} n-nevermind."
                    return
    elif karma() == 2:
        $show_chr("A-ABBAA-ABAD")
        y "H-Happy Valentine's Day, [player]!"
        $show_chr("A-BBBAA-ABAB")
        y "I had hoped you would visit today..."
        $show_chr("A-ACBAA-ABAB")
        y "I just wanted to say that... I hope we can have a good time today."
        $show_chr("A-ACBAA-ABAK")
        y "We may disagree sometimes, but... you're still my friend."
        $show_chr("A-ACBAA-ABAL")
        y "And I don't want a bit of discord ruining that friendship."
        $show_chr("A-ACAAA-ABAB")
        y "S-So... what shall we do today?"
        return
    else:
        $add_k(1)
        $show_chr("A-AFDAA-ABAB")
        y "You're wishing me a happy Valentine's Day?"
        $show_chr("A-AFEAA-AIAI")
        y "Did you mean to do this, or was it an accident?"
        $show_chr("A-BFAAA-AIAI")
        y "Actually, I don't think I want to know the answer."
        $show_chr("A-AFBAA-ABAB")
        y "Thank you, I guess..."
        $show_chr("A-CFAAA-ABAB")
        y "Ahem... So, what else are you planning to do today?"
    return

label vday_choco_date_intro:
    #check if the player has visited the museum before, if not trigger the dialogue below
    if not renpy.seen_label("valentines_2021_date"):
        $show_chr("A-BCAAA-ABAD")
        y "With it being Valentine's day, and being a chocolate lover and a curious mind, I wondered..."
        $show_chr("A-ACDAA-ABAD")
        y "How is chocolate made?{w} It must be quite an interesting process, don't you think?"
        $show_chr("A-ABAAA-ABAD")
        y "So I did some research, and found a popular chocolate museum located in Malagos."
        $show_chr("A-ACAAA-ABAB")
        y "After doing enough research, I think I was able to make a pretty close replica of the museum, so I'd like to visit it, if you don't mind."
        $show_chr("A-ACAAA-ABAB")
        y "Let me bring it up..."
        call valentines_2021_date
    else:
        $show_chr("A-ACAAA-ABAB")
        y "Since it's Valentine's day, and I'm in the mood for some chocolate, I was thinking we could visit the chocolate museum again."
        $show_chr("A-ACAAA-ABAD")
        y "Does that sound okay?"
        menu:
            "Of course!":
                $show_chr("A-GCAAA-ABAD")
                y "Great! Let me just..."
                call valentines_2021_date
            "I actually had other ideas...":
                $show_chr("A-CCAAA-ABAB")
                y "That's perfectly fine."
                $show_chr("A-ACAAA-ABAB")
                y "So, what were you thinking?"
    return

label vday_choco_date_request: #Anything special planned today, Yuri? / Should only appear feb 12th-16th, and if the player didn't have level 3 karma when they told her happy valentine's / Must have karma level equal 3 or higher to see
    $show_chr("A-ABAAA-ABAK")
    y "Actually, yes. I had an idea for a new date we could go on."
    call vday_choco_date_intro
    return

#clarification, valentines_2021_date is the actual date, and vday_choco_date_intro is the introduction to said date stemming from the event. vday_choco_date_request is in case the player didn't have level 3 karma when telling yuri happy valentine's and they want vday_choco_date_intro


label valentines_2021_date:

    image event chocolate_1:
        "images/events/valentines/1.png"
    image event chocolate_2:
        "images/events/valentines/2.png"
        zoom 0.7
    image event chocolate_3:
        "images/events/valentines/3.png"
        yalign 0.5 zoom 0.7
    image event chocolate_4:
        "images/events/valentines/4.png"
        yalign 0.1
    image event chocolate_5:
        "images/events/valentines/5.png"
        yalign 0.9 zoom 0.7
    image event chocolate_6:
        "images/events/valentines/6.png"
        zoom 0.7
    image event chocolate_7:
        "images/events/valentines/7.jpg"
        zoom 0.9

    hide craneo
    hide roseo
    hide bunnyo
    hide raccoon
    hide diffuser
    hide hdy_statue
    hide halloween_cupcake
    show black zorder 20
    with Dissolve(2.0)
    pause 0.5
    $hide_yuri_sit = True
    hide black zorder 20
    show event chocolate_1 zorder 10
    with Dissolve(2.0)

    python:
        if not persistent.costume in ["school", "sweater", "valentines"]:
            temp_costume = "sweater"
        else:
            temp_costume = persistent.costume

    #standing sprite
    if temp_costume == "school":
        show yuri 1c at t11 zorder 11
    if temp_costume == "sweater":
        show yuri 1bc at t11 zorder 11
    if temp_costume == "valentines":
        show yuri 1dc at t11 zorder 11
    if temp_costume != "valentines":
        y "So here we are, the {b}Malagos Chocolate Museum{/b}, or my version of it anyway."
        if temp_costume == "school":
            show yuri 1b at t11 zorder 11
        if temp_costume == "sweater":
            show yuri 1bb at t11 zorder 11
        if temp_costume == "valentines":
            show yuri 1db at t11 zorder 11
        y "This place exists in your reality in the Philippines.{w} While I don't know your current travel circumstances, I hope we can both enjoy visiting this recreation."
        if temp_costume == "school":
            show yuri 2j at t11 zorder 11
        if temp_costume == "sweater":
            show yuri 2bj at t11 zorder 11
        if temp_costume == "valentines":
            show yuri 3db at t11 zorder 11
        y "Alongside this museum is a local cocoa farm where they create award-winning chocolate from the seed to finely crafted confectionaries."
        if temp_costume == "school":
            show yuri 1b at t11 zorder 11
        if temp_costume == "sweater":
            show yuri 1bb at t11 zorder 11
        if temp_costume == "valentines":
            show yuri 1db at t11 zorder 11
        y "We are taking what they call the {i}Tree-to-Bar tour{/i} where we're going to see an actual chocolate farm and learn a bit about the history of chocolate..."
        if temp_costume == "school":
            show yuri 3m at t11 zorder 11
        if temp_costume == "sweater":
            show yuri 3bm at t11 zorder 11
        if temp_costume == "valentines":
            show yuri 3dc at t11 zorder 11
        y "Afterwards, there will be a chocolate bar where we'll have some sweet treats and..."
        y "Mhmmm..."
        if temp_costume == "school":
            show yuri 1d at t11 zorder 11
        if temp_costume == "sweater":
            show yuri 1bd at t11 zorder 11
        if temp_costume == "valentines":
            show yuri 1dd at t11 zorder 11
        y "I'll leave the last part as a surprise. Believe me, you'll enjoy it!"
    else:
        y "I hope you don't mind that I wear this again, coming back here."
    if temp_costume == "school":
        show yuri 1f at t11 zorder 11
    if temp_costume == "sweater":
        show yuri 1bf at t11 zorder 11
    if temp_costume == "valentines":
        show yuri 1da at t11 zorder 11
    y "Oh! I don't know if you saw, but the devs mentioned for you to have some hot chocolate ready for later..."
    if temp_costume == "school":
        show yuri 1a at t11 zorder 11
    if temp_costume == "sweater":
        show yuri 1ba at t11 zorder 11
    if temp_costume == "valentines":
        show yuri 1da at t11 zorder 11
    y "So, I would like to begin if you are ready. Our first stop will be the farm..."
    show event chocolate_2 with Dissolve(2.0)
    #Transition to new location
    if temp_costume == "school":
        show yuri 1i at t11 zorder 11
    if temp_costume == "sweater":
        show yuri 1bi at t11 zorder 11
    if temp_costume == "valentines":
        show yuri 1db at t11 zorder 11
    y "Wow, cacao trees with fruit as far as the eye can see... they really don't call it a farm for nothing."
    if temp_costume == "school":
        show yuri 1m at t11 zorder 11
    if temp_costume == "sweater":
        show yuri 1bm at t11 zorder 11
    if temp_costume == "valentines":
        show yuri 1dc at t11 zorder 11
    y "Mhm... a shame that you can't smell this... it's such a unique scent..."
    if temp_costume == "school":
        show yuri 1b at t11 zorder 11
    if temp_costume == "sweater":
        show yuri 1bb at t11 zorder 11
    if temp_costume == "valentines":
        show yuri 1db at t11 zorder 11
    y "From my understanding, while they look delicious, the actual fruit itself does not have a single hint of chocolate flavor but is rather unpleasant tasting outside, with a sweet lemonade-like pulp inside."
    if temp_costume == "school":
        show yuri 2f at t11 zorder 11
    if temp_costume == "sweater":
        show yuri 2bf at t11 zorder 11
    if temp_costume == "valentines":
        show yuri 3db at t11 zorder 11
    y "It's actually a popular misconception that the fruit is what the chocolate is made from, but it's actually the fruit's seeds, or its beans as they are known when fermented and roasted, that give chocolate its flavor."
    if temp_costume == "school":
        show yuri 2l at t11 zorder 11
    if temp_costume == "sweater":
        show yuri 2bl at t11 zorder 11
    if temp_costume == "valentines":
        show yuri 3da at t11 zorder 11
    y "They say that the cacao bean inside can smell like anything from sweat to cooked cabbage, but it smells... earthly, with just a hint of spice... very odd."
    if temp_costume == "school":
        show yuri 1k at t11 zorder 11
    if temp_costume == "sweater":
        show yuri 1bk at t11 zorder 11
    if temp_costume == "valentines":
        show yuri 1dc at t11 zorder 11
    pause 1.0
    y "It probably wasn't a great idea to wear layered clothing here."
    if temp_costume == "school":
        show yuri 1q at t11 zorder 11
    if temp_costume == "sweater":
        show yuri 1bq at t11 zorder 11
    if temp_costume == "valentines":
        show yuri 1da at t11 zorder 11
    y "At least I know that my weather script works... even if only {b}against{/b} me today."
    if temp_costume == "school":
        show yuri 1b at t11 zorder 11
    if temp_costume == "sweater":
        show yuri 1bb at t11 zorder 11
    if temp_costume == "valentines":
        show yuri 1db at t11 zorder 11
    y "Anyway, enough whining. I wonder if anyone would mind if I touch the fruits..."
    if temp_costume == "school":
        show yuri 1g at t11 zorder 11
    if temp_costume == "sweater":
        show yuri 1bg at t11 zorder 11
    if temp_costume == "valentines":
        show yuri 1db at t11 zorder 11
    y "Oh, wait a second... I almost forgot that there is nobody around here. Which means..."
    if temp_costume == "school":
        show yuri 1j at t11 zorder 11
    if temp_costume == "sweater":
        show yuri 1bj at t11 zorder 11
    if temp_costume == "valentines":
        show yuri 1dc at t11 zorder 11
    y "I can touch whatever I please..."
    if temp_costume == "school":
        show yuri 3e at t11 zorder 11
    if temp_costume == "sweater":
        show yuri 3be at t11 zorder 11
    if temp_costume == "valentines":
        show yuri 1da at t11 zorder 11
    y "Incredible... the shell feels so... leathery. I expected something else from the looks. It's... astonishing..."
    if temp_costume == "school":
        show yuri 2a at t11 zorder 11
    if temp_costume == "sweater":
        show yuri 2ba at t11 zorder 11
    if temp_costume == "valentines":
        show yuri 3da at t11 zorder 11
    y "But somehow also hard at the same time..."
    if temp_costume == "school":
        show yuri 1a at t11 zorder 11
    if temp_costume == "sweater":
        show yuri 1ba at t11 zorder 11
    if temp_costume == "valentines":
        show yuri 1da at t11 zorder 11
    y "I wonder, have you ever felt the shell of a cacao fruit?"
    menu:
        "Actually, yes.":
            if temp_costume == "school":
                show yuri 1b at t11 zorder 11
            if temp_costume == "sweater":
                show yuri 1bb at t11 zorder 11
            if temp_costume == "valentines":
                show yuri 1db at t11 zorder 11
            y "How interesting. I... kind of want to keep this one. Maybe I will... it would make for a truly exotic decoration I fancy."
        "Not at all so far.":
            y "If you ever get the opportunity, you should try it. I have been quite curious about this before we came here."
    if temp_costume == "school":
        show yuri 1b at t11 zorder 11
    if temp_costume == "sweater":
        show yuri 1bb at t11 zorder 11
    if temp_costume == "valentines":
        show yuri 1db at t11 zorder 11
    y "Fun misunderstood fact, the beans of the cacao fruit are actually a pasty white. You'd think they would be some form of brown, but no..."
    if temp_costume == "school":
        show yuri 1j at t11 zorder 11
    if temp_costume == "sweater":
        show yuri 1bj at t11 zorder 11
    if temp_costume == "valentines":
        show yuri 1db at t11 zorder 11
    y "Ah, but about the cacao itself... What they do with the fruits is crack them open and take the beans, and open them up to get the black bean-like part inside that gives chocolate solids its color, which are colloquially called {b}nibs{/b}."
    if temp_costume == "school":
        show yuri 1k at t11 zorder 11
    if temp_costume == "sweater":
        show yuri 1bk at t11 zorder 11
    if temp_costume == "valentines":
        show yuri 1db at t11 zorder 11
    y "The fruit and bean shells themselves are actually discarded..."
    y "Imagine growing such a large fruit for such a small yield... no wonder the farms are so large."
    if temp_costume == "school":
        show yuri 1a at t11 zorder 11
    if temp_costume == "sweater":
        show yuri 1ba at t11 zorder 11
    if temp_costume == "valentines":
        show yuri 1da at t11 zorder 11
    y "Ah, and I believe the next part of the tour was within their museum."
    show event chocolate_3 with Dissolve(2.0)
    #Transition to new location

    if temp_costume == "school":
        show yuri 1a at t11 zorder 11
    if temp_costume == "sweater":
        show yuri 1ba at t11 zorder 11
    if temp_costume == "valentines":
        show yuri 1da at t11 zorder 11
    y "Here we are. So let us take a look around shall we?"
    if temp_costume == "school":
        show yuri 1d at t11 zorder 11
    if temp_costume == "sweater":
        show yuri 1bd at t11 zorder 11
    if temp_costume == "valentines":
        show yuri 1dd at t11 zorder 11
    y "This one here looks interesting. Let me step aside so that you can see it..."
    hide yuri
    #hide yuri
    y "I already heard about this one. That's the {b}Cacao Belt{/b}, a thin belt of 20 degrees from each side of the equator. These are the only places where Cacao grows."
    y "Here it says that cacao thrives in high humidity and only with a lot of rainfall. 40 to 100 inches per year..."
    y "One third of the worldwide cacao harvest comes from {b}Côte d'Ivoire{/b}, the Ivory Coast. Ghana and Indonesia are close contenders."
    y "Now I begin to understand why high quality chocolate with a high content of actual cacao gets so incredibly expensive. It doesn't outright say this but the panel implies that you can't really grow cacao in greenhouses."
    y "I hope I don't sound like an overenthusiastic teacher right now. I'm just telling you this because I assume that you can't really see the letters that well from over there."
    y "Are... you even enjoying this trip at all?"
    menu:
        "I actually find all of this very interesting.":
            y "I'm glad. I was almost afraid for a moment."
        "I already knew much what you just told me, but I still enjoy the trip don't worry.":
            y "Oh! I see! So you're already ahead of me here."
    y "Oh! Can we go over there please? This looks interesting..."
    show event chocolate_4 with Dissolve(2.0)
    #Transition to new location



    y "So this is how the beans look at their different stages..."
    y "The {i}nibs{/i}, as they are called, are what chocolate is really made of."
    y "The beans are fermented, dried, and roasted over a period of days, sometimes taking over two weeks to reach their best state."
    y "After all that is done, the shells are removed and the nib inside is ground and liquified, resulting in pure liquid chocolate: Chocolate liquor which, despite the name, is alcohol free."
    y "The liquor is then split into cocoa butter, which is what gives chocolate its texture, and chocolate solids, which are ground into powder and give chocolate its flavor and color."
    y "It's a shame that you can't smell the air here. This whole place smells of chocolate... such a gentle, appetizing scent...{w} Delicious~"
    y "I'll... let you in on a little secret..."
    y "It's very common for girls to love chocolate... Many studies have been done, with the conclusions ranging anywhere from the body finding chocolate more sustaining to helping with stress. I guess there's just something about it that makes it so nice."
    y "Well, except those allergic to it, obviously."
    if persistent.chocall:
        y "Ah... I forgot you were allergic to chocolates, I'm sorry!"
    y "I try to keep it in moderation, but I have to admit that I'm not always successful. A nice piece of chocolate always helps me through rough days."
    y "And as you already know, I had no lack of those in the past."
    y "By the way, did you know dark chocolate is produced by adding fat and sugar to the cacao mixtures? Different amounts give different tastes, depending on which is used the most."
    y "A higher amount of cocoa usually results in more bitter chocolate. Less sugar results in what you could call semi-sweet chocolate."
    y "When the mixture is about a third sugar, cocoa butter and vanilla, this is bittersweet chocolate. It has less sugar than semi-sweet chocolate, as you would guess."
    y "An easy way to tell what chocolate is which kind is by looking at the ingredients. Most will list the amount of cocoa used, like say 70%%. This example chocolate would likely be bittersweet."
    y "Anyway, we have one more thing in store for today, The part I have been the most excited about."
    y "I promised you a surprise when we arrived, I think now is a good time to reveal it. Come along, I want to show you the last stop of our adventure."
    show event chocolate_5 with Dissolve(2.0)
    #Transition to new location



    #show Yuri again

    if temp_costume == "school":
        show yuri 1a at t11 zorder 11
    if temp_costume == "sweater":
        show yuri 1ba at t11 zorder 11
    if temp_costume == "valentines":
        show yuri 1da at t11 zorder 11
    y "Here we are. The chocolate bar."
    if temp_costume == "school":
        show yuri 1j at t11 zorder 11
    if temp_costume == "sweater":
        show yuri 1bj at t11 zorder 11
    if temp_costume == "valentines":
        show yuri 1db at t11 zorder 11
    y "Admittedly, it's a bit empty at the moment... though that means the place is reserved for our own enjoyment."
    if temp_costume == "school":
        show yuri 1u at t11 zorder 11
    if temp_costume == "sweater":
        show yuri 1bu at t11 zorder 11
    if temp_costume == "valentines":
        show yuri 1dc at t11 zorder 11
    y "But, we aren't here to {b}only{/b} eat chocolate, not right now at least..."
    if temp_costume == "school":
        show yuri 3d at t11 zorder 11
    if temp_costume == "sweater":
        show yuri 3bd at t11 zorder 11
    if temp_costume == "valentines":
        show yuri 3dd at t11 zorder 11
    y "We are here to make our own!"
    if temp_costume == "school":
        show yuri 1c at t11 zorder 11
    if temp_costume == "sweater":
        show yuri 1bc at t11 zorder 11
    if temp_costume == "valentines":
        show yuri 1dc at t11 zorder 11
    y "We would first decide the shape of our pralines and pick a rubber mold over there."
    if temp_costume == "school":
        show yuri 1d at t11 zorder 11
    if temp_costume == "sweater":
        show yuri 1bd at t11 zorder 11
    if temp_costume == "valentines":
        show yuri 1dd at t11 zorder 11
    y "And then, we have a variety of ingredients to choose from. I heard some of them are rather exotic... let us see how far we can take this!"
    show yuri at thide
    hide yuri
label critical_choco_point:
    $hide_yuri_sit = True
    #Transition to new location
    show event chocolate_6 zorder 9 with Dissolve(2.0)
    #Hide Yuri

    y "Natsuki would have a great time here. Maybe, when I manage to one day bring them all back, I will take her here."
    y "But anyway, we are here for our own date, as much as I would love to show her this place. I'm sure she would enjoy this..."
    y "There's so many chocolates here I've always wanted to try..."
    y "Lavender chocolate, mint chocolate, so many unique combinations of ingredients..."
    y "You know what? Wouldn't it be romantic if we made something together instead of each one their own?"
    y "I would suggest that you add one ingredient from the upper shelf, and then I would add one from the bottom shelf."
    y "So, take a look around, I'll do the same in the meantime."
    menu:
        "Durian Candy? You weren't overstating when you said they have some exotic ones. I'll go for them.":
            y "Oh, I never had Durian fruit! I'm very curious how they taste!"
        "Some fruits would go great with the sweetness of chocolate, I think I'll pick the dried Mango!":
            y "A fine choice. I actually like Mango a lot."
        "Oh, they have dried Cranberries! I made my choice.":
            y "They were very popular a few years ago in your world, weren't they? I'm looking forward to trying them myself."
        "Dried Sultanas and Raisins... quite similar, which one should I try?":
            y "They indeed are quite similar. I think the only difference is about how they are dried. Why not a few of both?"
        "Rock Salt?!? Unusual for sure, but I think this might work...":
            y "I think I saw chocolate with sea salt once. I'm truly looking forward to how this turns out!"
    y "I made my choice as well."
    if sanity() > 3:
        y "Nuts do always go well with chocolate. I'll pick some walnuts, just to give our chocolate some bite!"
    else:
        if sanity() == 1:
            y "I always wanted to try chocolate coated crickets, they are quite the delicacy in some parts of the world! Sadly, we don't have those here. Instead..."
        y "I'll add some chili flakes to it. I'm in the mood for some sweet punishment today."
        y "Do you know what you and chili chocolate have in common? It hurts when I take a bite..."
        y "Oh, I {b}did{/b} say that out loud didn't I?"
    y "Next... I mentioned earlier that you should bring some hot chocolate, so if you could have that ready while I make my own."
    if temp_costume != "valentines":
        y "I'll be drinking some Tsokolate, which is a Filipino hot chocolate drink. It'll take me a few minutes... Head on over to the cafe, I'll be right there in a minute."
        #fade out?
        $ pitstop_bg = persistent.bg
        $tc_class.transition("timecycle", "now")
        hide yuri
        hide screen jy_bg
        #transition to new background
        show event chocolate_7 zorder 9 with Dissolve(2.0)
        $click_tea_button = 0
        call choco_timer

label enjoy_chocolate:
    if temp_costume != "valentines":
        hide screen choco_timer
        #waiting function, wait for however long it took for her to make the tea in the tea date?
        #yuri is hidden
        y "Okay, the Tsokolate is ready!"
        y "I also have a surprise..."

        #black dress, sitting
        $hide_yuri_sit = False
        $current_timecycle_marker = "_day"
        $persistent.costume = "valentines"
        show black zorder 20 with Dissolve(1.0)

        $show_chr("A-BCBAA-ALAK")
        hide black with Dissolve(1.0)
        y "...D-Do you like it?"
        menu:
            "You look beautiful!":
                $show_chr("A-CCBAA-ALAK")
                y "Thank you... I was a bit nervous about wearing it, since I'm not really one to wear something like this..."
                $show_chr("A-ACBAA-ALAK")
                y "The heat was getting to me though, and considering the importance of the date, I figured it'd be a nice way to kill two birds with one stone, you could say."
            "Not really, sorry.":
                $add_karma(-10)
                $show_chr("A-BFBAA-ALAL")
                y "O-Oh... Well, if you don't mind, I'd like to keep it on..."
                $show_chr("A-CFBAA-ALAL")
                y "The heat is getting to me... Though I don't mind a rich and warm cup to soothe the mind and heart."
    else:
        $ pitstop_bg = persistent.bg
        $tc_class.transition("timecycle", "now")
        hide yuri
        hide screen jy_bg
        $current_timecycle_marker = "_day"
        #transition to new background
        show event chocolate_7 zorder 9 with Dissolve(1.0)
        $hide_yuri_sit = False
        $show_chr("A-AAAAA-ANAE")
        y "It's nice to sit down again after another walk through this place."
    $show_chr("A-AAAAA-ANAE")
    y "So, we both have our hot chocolate... I've never tried Tsokolate, but I've read it's an amazingly tasty kind of hot chocolate."
    $show_chr("A-GBAAA-ANAE")
    y "So, cheers!"
    $show_chr("A-CCAAA-ANAE")
    y "..."
    $show_chr("A-IBAAA-ANAE")
    y "Wow, they weren't lying! It's so rich and creamy... A very nice way to end the day."
    $show_chr("A-ACAAA-ANAE")
    y "Tsokolate is made from adding small tablets of ground and roasted cacao beans, called {i}tabliya{/i}, to a mixture of boiling water and milk."
    $show_chr("A-BBAAA-ANAD")
    y "You can add normal cocoa powder instead of the aforementioned tabliya, but that's usually frowned upon since it doesn't taste the same."
    $show_chr("A-ACAAA-ANAN")
    y "After adding the tabliya, it is usually mixed with a wooden baton called a Molinillo."
    $show_chr("A-ADAAA-ANAF")
    y "There are also cases where people have added other ingredients to their Tsokolate, ranging from cinnamon or vanilla to tequila."
    $show_chr("A-BFAAA-ANAC")
    y "Now that I think about it, a little cinnamon would be nice..."
    $show_chr("A-ABAAA-ANAN")
    y "Oh, but how is your hot chocolate?"
    menu:
        "It's great!":
            $show_chr("A-ACAAA-ANAK")
            y "I'm glad to hear that! Sharing hot chocolate with you is one of the leading moments of my life."
        "Actually... I didn't make any.":
            $show_chr("A-CCBAA-AIAI")
            y "[player]... I told you at the beginning {i}and{/i} before I made my own, so you have no excuse."
            $show_chr("A-BBAAA-AMAM")
            y "I guess I'll just have to enjoy this refreshing, delicious hot chocolate all by my lonesome..."
        "Not that great actually... I may have done something wrong...":
            $show_chr("A-AFBAA-ANAE")
            y "I'm sorry to hear that. Maybe next time, it'll turn out better."
    y "You know, this place is more than a museum and cafe... they have a spa, a garden with several bird shows, and even a small petting zoo!"
    y "This really would be a great vacation spot, huh?"
    y "Oh, something I read about the spa..."
    y "All of the products they use in their treatments are made with ingredients from the cacao fruit they grow there."
    y "So they don't rely on products from other companies, making the spa self-sustainable. Very clever, isn't it?"
    if persistent.lovecheck:
        y "Imagine, after getting a nice soothing massage, we head to one of the villas to rest..."
        y "We lay in bed, comfortably snuggled up together, giving each other a goodnight kiss as we drift off to sleep..."
        y "Of course, that is one way that could go... but I won't get too descriptive."

    $show_chr("A-ABGAA-ANAD")
    y "Oh, by the way..."
    $show_chr("A-BCAAA-ANAD")
    y "I'm not sure if you realized this, but since I made this place, and there's no one else around..."
    $show_chr("A-GBAAA-ANAD")
    y "We quite literally have our own chocolate farm!"
    $show_chr("A-BCBAA-AMAM")
    y "Of course, we don't exactly know how to run it..."
    $show_chr("A-ACFAA-AMAM")
    extend " but I'm sure we can learn."
    $show_chr("A-ICAAA-ALAL")
    y "I hope you're planning on taking me back here sometime... This was fun..."

label museumend:
    $show_chr("A-ACAAA-ABAB")
    y "Anyway, I had a lot of fun today. I'm grateful that I got the opportunity to take you here."
    y "Oh, I'm not sure if I even mentioned this but. I based this place on a {b}real{/b} chocolate museum from your world!"
    y "This place is called {b}Malagos{/b}, located in the Philippines I think. So if you're ever looking for a good place to spend your next holiday, you know where to go now!"
    $show_chr("A-BBAAA-ABAB")
    y "Oh! And the chocolate is cooled down now. This will get a very special place when we get home."
    $show_chr("A-CCAAA-ABAB")
    y "You know, there is a certain closet where a certain someone always stored their Manga collection. I think there it would fit just fine."
    $show_chr("A-ACAAA-ABAB")
    y "Let's go home for now. And again, thank you for going on this date with me..."
    show black zorder 20 with Dissolve(1.0)
    hide event chocolate_5
    #fade to black
    if persistent.bg == "space":
        $tc_class.transition("space", speed="now")
    elif persistent.bg == "timecycle":
        $tc_class.transition("timecycle", speed="now")
    elif persistent.bg == "yuri_desk":
        $tc_class.transition("yuri_desk", speed="now")
    elif persistent.bg == "yuri_kotatsu_1":
        $tc_class.transition("yuri_kotatsu_1", speed="now")
    elif persistent.bg == "yuri_kotatsu_2":
        $tc_class.transition("yuri_kotatsu_2", speed="now")
    show screen jy_bg
    pause 0.5
    hide black zorder 20 with Dissolve(1.0)
    $ _skipping = False
    $ persistent.dates_taken += 1
    jump ch30_loop

label choco_timer:
    screen choco_timer():
        vbox:
            style_prefix "talkbutton"
            textbutton "Enter" action Jump("choco_wait")
            xalign 0.50
            yalign 0.25

        timer 60.0 action Jump("enjoy_chocolate")
    if click_tea_button <= 1:
        show screen choco_timer()

label choco_wait:
    y "Please be patient, [player], I just need a minute to prepare."
    $click_tea_button = click_tea_button + 1
    jump choco_timer
