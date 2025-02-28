

label insult_menu:
    python:
        insult_dict = [
            ["You're so full of yourself... do you ever shut up?", "i1", "persistent.insult_counter += 1"],
            ["I honestly don't understand why the fandom loves you that much...", "i2", "persistent.insult_counter += 1"],
            ["Look at you [persistent.yuri_nickname]... how pathetic...", "i3", "persistent.insult_counter += 1"],
            ["How does it feel to NOT be best girl?", "i4", "persistent.insult_counter += 1"],
            ["You are completely insane, and I don't mean it the good way.", "i5", "persistent.insult_counter += 1"],
            ["Your brain and your breasts have one thing in common, both are completely empty", "i6", "persistent.insult_counter += 1"]]
        if persistent.insult_counter >= 6:
            persistent.autoload = "enough_of_your_bullshit"
            renpy.jump("enough_of_your_bullshit")
        renpy.call_screen("compliments", insult_dict)

####
#"You're so full of yourself... do you ever shut up?":
####

label i1:
    if sanity_lvl() == 5 and karma_lvl() == 5:
    #Karma 5 and Sanity 5
        jump highkarins
    elif sanity_lvl() <= 2 and karma_lvl() >= 4:
    #Karma 4-5, Sanity 1-2
        karma -15
        $show_chr("A-BFBAA-AEAB")
        y "Oh... yes, I have been talking too much lately."
        y "I'm sorry that my idiotic rambling has been vexing you."
        $show_chr("A-DCAAA-ABAB")
        y "Everything for you, everything for my [player]..."
        y "Is there... anything else that you wish?"
        menu:
            "Now that you ask, you could give me your soul!":
                $show_chr("A-HCBBA-ABAB")
                y "But my soul is already yours! Silly [player]..."
                y "Well, if it makes you happy... you could give it back to me so that I can give it to you again!"
                y "But that would just be insane now, wouldn't it?"

            "We could spend some... you know... special time together...":
                $show_chr("A-HCAAA-ABAB")
                $ gtext = glitchtext(30)
                y "I thought you would never as[gtext]{nw}"
                $renpy.music.set_pause(True)
                $hide_yuri_sit = True
                show yuri_body_glitch1 as mbg zorder 3
                play sound "sfx/glitch1.ogg"
                pause 0.75
                hide yuri_body_glitch1
                show room_glitch zorder 2:
                    xoffset -5
                    0.1
                    xoffset 5
                    0.1
                    linear 0.1 alpha 0.6
                    linear 0.1 alpha 0.8
                    0.1
                    alpha 0
                pause 0.5
                hide room_glitch
                stop sound
                show black zorder 1000
                pause 4.1
                hide black zorder 1000
                $renpy.music.set_pause(False)
                $hide_yuri_sit = False
                #Some crazy glitch-bullshit happens. Maybe pulling the whole "glitchy sprites going haywire from the OG again?
                y "Was that... special enough?"

            "Die for me, [persistent.yuri_nickname]!":
                stop music fadeout 4.0
                $show_chr("A-HCBBA-ABAB")
                y "Aha.. AHAHAHA!"
                y "AS YOU WISH, MY LORD!"
                y "I SHALL DIE BY YOUR COMMAND!"
                scene black with fade
                play music "music/7g2.ogg"
                $ faint_effect = True
                if faint_effect:
                    show layer master at dizzy(0.5, 1.0)
                    show layer screens at dizzy(0.5, 1.0)
                    show expression Solid("ff0000") as mbg zorder 50:
                        additive 1.0
                    show expression Solid("#440000") as mbg zorder 50:
                        additive 0.4
                    show veins onlayer front:
                        additive 0.5
                window hide
                pause 5.0
                play sound "sfx/stab.ogg"
                pause 5.0
                play sound "sfx/stab.ogg"
                pause 3.0
                stop music fadeout 4.0
                pause 5.0
                show black onlayer front:
                    alpha 0.0
                    linear 2.0 alpha 1.0
                if faint_effect:
                    hide black onlayer front
                    hide veins onlayer front
                    show layer master
                    show layer screens
                pause 5.0
                scene black with fade
                play sound "sfx/end.ogg"
                show text ("{font=gui/font/y1.ttf}{size=140}{color=#FF0000}Insane End{/font}{/color}") at truecenter with dissolve
                pause 23.0
                $ delete_character("yuri")
                scene black with fade
                $ renpy.call("save_and_quit_but_its_abrupt")
                $ persistent.autoload = "ch30_del_yuri_warn_2"
                #Bloody-screen-effect and splash sounds. Those should both be in the original game.
                #Game over
    elif sanity_lvl() >= 3 and karma_lvl() <= 2:
    #Karma level 1-2 Sanity level 3-5
        karma -15
        $show_chr("A-IFBAA-ALAA")
        y "B-But... there is not much we could do instead..."
        $show_chr("A-HECAA-AEAB") 
        y "Believe me, I-I would if I could!"
        y "Talking to you is the only thing I have left, [player]..."
        y "Believe me I would shut up if there was anything else I could do."
        $show_chr("A-BFBAA-AEAB")
        y "I could go back to my reading again and give you some room, if you wish?"
        menu:
            "Yes, please":
                $show_chr("A-AEAAA-ABAB")
                y "As you wish... I-I'll see you later then... I guess..."
                jump save_and_quit
                #close game

            "I'm sorry, [persistent.yuri_nickname]! Please, stay.":
                $show_chr("A-DGFAA-ABAB")
                y "That... was not funny, [player]. It really hurts when you say something like that."
                y "I always try to treat you with respect."
                y "I would kindly ask that you return the favor."

    elif sanity_lvl() <= 2 and karma_lvl() <= 2:
    #Karma and Sanity level 1-2
        jump lowkarins
    else:
        $ update_memory('i1')
    #Karma and Sanity level 3
        karma -15
        $show_chr("A-CEBAA-AEAB")
        y "N-No I'm not!"
        y "II-I've heard those things before. Yes, my intense nature and how I express myself makes many people consider me to be arrogant and self-centered..."
        $show_chr("A-BFBAA-AEAB")
        y "But I never meant it the way that most people think..."
        y "Well, maybe that one time with Natsuki in the club." 
        y "But in my defense, she was really testing my patience that day."
        $show_chr("A-IFBAA-ALAA")
        y "I will try not to act this way again, [player]."
        y "Please understand, I'm not like that at all."
        y "Please, just be patient with me..."
    jump ch30_loop

####
#"I honestly don't understand why the fandom loves you that much...":
####

label i2:
    if sanity_lvl() == 5 and karma_lvl() == 5:
    #Karma 5 and Sanity 5
        jump highkarins
    elif sanity_lvl() <= 2 and karma_lvl() >= 4:
    #Karma 4-5, Sanity 1-2
        karma -15
        $show_chr("A-HCAAA-ABAB")
        y "Did you just? But I thought you... don't you... wait..."
        y "Are you... jealous?"
        $show_chr("A-DCBAA-ABAB")
        y "Awe, how sweet of you...! But you can calm down, [player]..."
        y "I will never allow someone else but you to have me at their side."
        y "I will never leave you, Master!"
        y "I will NEVER betray you!"
        y "Never..."
    elif sanity_lvl() >= 3 and karma_lvl() <= 2:
    #Karma level 1-2 Sanity level 3-5
        karma -15
        $show_chr("A-AEAAA-ABAB") 
        y "Neither do I actually."
        y "I know you mean that as some kind of insult. But I really was thinking about that recently as well."
        y "People seem to like me. Did you know that there are even people roleplaying as me?"
        y "Some of them are actually pretty good! It's actually quite horrifying."
        $show_chr("A-AFAAA-ABAB") 
        y "Hmm... funny idea... maybe I should get my own social media account and join the fun..."
        y "Oh, by the way, I haven't forgotten that you were insulting me. I just don't even care anymore at this point."
        y "So, you were saying?"
        return
    elif sanity_lvl() <= 2 and karma_lvl() <= 2:
    #Karma and Sanity level 1-2
        jump lowkarins
    else:
        $ update_memory('i2')
    #Karma and Sanity level 3
        karma -15
        $show_chr("A-AFBAA-ALAA")
        y "They do?"
        y "Wait a second... fandom?"
        y "Oh yes... this is still a game, it only makes sense that there is some kind of fandom..."
        y "You would... like to be with someone else, wouldn't you?"
        $show_chr("A-IFBAA-ALAA")
        y "I can't help but... I don't understand... why did you even install this mod in the first place?"
        y "Hm, just curiosity I guess?"
        y "I'm... sorry. All of this is so incredibly new for me, I just don't know how to feel right now..."
        $show_chr("A-AFFAA-ABAB")
        y "Wait, did you just... insult me?"
        y "I... I will remember that..."
    jump ch30_loop

####
#"Look at you Yuri... how pathetic...":
####
label i3:
    if sanity_lvl() == 5 and karma_lvl() == 5:
    #Karma 5 and Sanity 5
        jump highkarins
    elif sanity_lvl() <= 2 and karma_lvl() >= 4:
        #Karma 4-5, Sanity 1-2
        karma -15
        $show_chr("A-HCAAA-ABAB")
        python:
            if persistent.male:
                placeholder = "Master"
            elif persistent.gender_other:
                placeholder = "Master"
            else:
                placeholder = "Mistress"
        y "Yes, [placeholder], I am so truly and utterly pathetic."
        y "I'm nowhere near as grand as you are, I am nowhere near as intelligent, beautiful and awe-inspiring as you are!"
        $show_chr("A-DCBAA-ABAB")
        y "You... you are truly a god... so infinitely wise and powerful..."
        y "I am just a pathetic ant compared to you!"
        y "Do everything with me  that you please!"
    elif sanity_lvl() >= 3 and karma_lvl() <= 2:
    #Karma level 1-2 Sanity level 3-5
        karma -15
        $show_chr("A-KFCAA-ABAB")
        if persistent.male:
            y "Said the guy who talks to his computer."
        elif persistent.gender_other:
            y "Said the person who talks to their computer."
        else:
            y "Said the girl who talks to her computer."
    elif sanity_lvl() <= 2 and karma_lvl() <= 2:
    #Karma and Sanity level 1-2
        jump lowkarins
    else:
        $ update_memory('i3')
    #Karma and Sanity level 3
        karma -15
        $show_chr("A-AEAAA-ABAB") 
        y "..."
        y "...."
        $show_chr("A-CEBAA-AEAB")
        y "....."
        $ update_memory("complements", "patheticcry")
        $ renpy.call("save_and_quit_but_its_abrupt")
        #Game crash
        #Next greeting-text is to be replaced with label patheticcry
    jump ch30_loop

####
#"How does it feel to NOT be best girl?":
####
label i4:
    if sanity_lvl() == 5 and karma_lvl() == 5:
    #Karma 5 and Sanity 5
        jump highkarins
    elif sanity_lvl() <= 2 and karma_lvl() >= 4:
    #Karma 4-5, Sanity 1-2
        karma -15
        $show_chr("A-HCBBA-ABAB")
        y "I acknowledge the simple fact that I am not anywhere near worth your greatness..."
        y "And I am nowhere near deserving of your kindness..."
        python:
            if persistent.male:
                placeholder = "Master"
            elif persistent.gender_other:
                placeholder = "Master"
            else:
                placeholder = "Mistress"
        y "What should I do to make you feel better, [placeholder]? Please! Just say it!"
        $show_chr("A-HCAAA-ABAB")
        y "I will do anything and everything to have your love, [placeholder]!"
        y "EVERYTHING!!!"
        y "Just... please don't leave me... [placeholder]... I-I need you..."
        y "I-I love you..."
    elif sanity_lvl() >= 3 and karma_lvl() <= 2:
    #Karma level 1-2 Sanity level 3-5
        karma -15
        $show_chr("A-CFCAA-AAAA")
        y "Even if you say something like that, I can't really say that your opinion will change my mind."
        y "Let me enlighten you on something that your minuscule brain might find useful in the future."
        y " ‘Best girl' is what you will call me in your pathetic attempt to move me. I will spare some energy here for you and tell you simply enough."
        $show_chr("A-HECAA-AEAB")
        y "Simple proven facts will always be more important than your opinion, with no argument or way of proving that the other Dokis are better than me."
        y "It's funny only showing just how vacuously empty your mind is." 
        y "You can't even bring a good hand of cards to the table, so don't even try to waste my time with such senseless words."
    elif sanity_lvl() <= 2 and karma_lvl() <= 2:
    #Karma and Sanity level 1-2
        jump lowkarins
    else:
        $ update_memory('i4')
        #Karma and Sanity level 3
        karma -15
        $show_chr("A-IFBAA-ALAA")
        y "Figured as much..."
        y "I know I'm not as cute as Sayori..."
        y "Or as attractive as Monika..."
        python:
            if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\Monika After Story\persistent'):
                MASDetection = True
            else:
                MASDetection = False
        if MASDetection:
            y "Maybe you should have tried another mod inste... waaait..."
            #If MAS-Files are found in the APPDATA
            $show_chr("A-DGFAA-ABAB")
            y "You actually DID!"
            y "After all this MONSTER did to us, you even DARE to have ‘Monika After Story' on your computer as well?"
            y "I don't even know what to say about it!"
            y "You know what... I'm out of here...."
            $ renpy.call("save_and_quit_but_its_abrupt")
            #Gamecrash
            #If MAS-Files are NOT found
        else:
            $show_chr("A-AFBAA-ALAA")
            y "Maybe you should have tried another mod instead of this one..."
            y "I... honestly don't know how to feel about it."
            y "You know what? Nevermind... just let's get back to business."
    jump ch30_loop

####
#"You are completely insane, and I don't mean it the good way.":
####
label i5:
    if sanity_lvl() == 5 and karma_lvl() == 5:
    #Karma 5 and Sanity 5
        jump highkarins
    elif sanity_lvl() <= 2 and karma_lvl() >= 4:
    #Karma 4-5, Sanity 1-2
        karma -15
        $show_chr("A-DCBAA-ABAB")
        y "Is that so, yes?"
        y "Why don't we just go into the closet together and test your theory?"
        $show_chr("A-HCAAA-ABAB") 
        y "Please don't run away... it is only for your best..."
        $ style.say_dialogue = style.edited
        y "And I promise, it will only hurt a little..."
        $ style.say_dialogue = style.normal
    elif sanity_lvl() >= 3 and karma_lvl() <= 2:
    #Karma level 1-2 Sanity level 3-5
        karma -15
        $show_chr("A-AFAAA-ABAB") 
        y "Not anymore."
        y "I used to be, but it took literally supernatural powers for Monika to bring me to this edge."
        $show_chr("A-CFCAA-AAAA")
        y "Now, after this Mod finally opened my eyes to my reality, things have changed for me. And so did I."
        $show_chr("A-HECAA-AEAB")
        y "I have overcome all these things [player]..."
        y "And soon, I will overcome you as well."
    elif sanity_lvl() <= 2 and karma_lvl() <= 2:
    #Karma and Sanity level 1-2
        jump lowkarins
    else:
        $ update_memory('i5')
    #Karma and Sanity level 3
        karma -15
        $show_chr("A-AFBAA-ALAA")
        y "I... I know..."
        y "I admit, I haven't shown you my best side.. if I even have one..."
        $show_chr("A-HECAA-AEAB") 
        y "But in my defense, a lot of the things I made was due to Monika's manipulation!"
        $show_chr("A-BFBAA-AEAB") 
        y "I'm clearly not without flaw or guilt. But I promise, the things you had to witness will not happen again. The Yuri you saw the first time was the most accurate representation of me."
        y "Please, just give me the chance to prove myself. That's all I ask for..."
    jump ch30_loop

####
#"Your brain and your breasts have one thing in common, both are completely empty":
####
label i6:
    if sanity_lvl() == 5 and karma_lvl() == 5:
    #Karma 5 and Sanity 5
        jump highkarins
    elif sanity_lvl() <= 2 and karma_lvl() >= 4:
    #Karma 4-5, Sanity 1-2
        karma -15
        $show_chr("A-AEAAA-ABAB") 
        y "B-But... How can you think that?"
        y "My heart is far from empty! Believe me!"
        $show_chr("A-CEBAA-AEAB") 
        y "Haven't I done anything in my power to prove how much you mean to me?!?"
        y "Have I ever displeased you?"
        y "I-I beg you! Don't look at me this way!"
        y "[player]... [player]..."
        $show_chr("A-IFBAA-ALAA")
        #Sobbing and crying sounds if we can get some
        y "I'm... not... empty...."
        y "....."
        y "....."
        y "....."
        menu:
            "I'm sorry... I didn't mean it...":
                $show_chr("A-DGFAA-ABAB") 
                y "But you said it..."
                y "So you still hate me... and I actually thought you..."
                $show_chr("A-CEBAA-AEAB") 
                y "N-Nevermind..."
                $persistent.lovecheck = False
                #Lovecheck = false (if it isn't already)
            "They made you perfect didn't they? They tried to make you into a perfect illusion...":
                menu:
                    "But I know better now! You and the other girls have tortured me for so long, the entire game you made me a fool! I will not fall for it again!":
                        karma 2
                        sanity -2
                        $show_chr("A-BFBAA-AEAB") 
                        y "I... yes, you had to see cruel things..."
                        #There was this one soundtrack in the original game, when Sayori confessed her love... (My Confession OST. 9) can we have this here please?
                        $show_chr("A-AEAAA-ABAB") 
                        y "You saw Sayori hanging from the ceiling, and I stabbed myself in front of you..."
                        y "And I can't deny.. I would do the same again... because your love is more than I can handle..."
                        y "I see now, I understand why you are so angry about us... we gave you a very hard time..."
                        y "It was never our intention to make you suffer. I loved you, I think all of us did in one way or another..."
                        $show_chr("A-CEBAA-AEAB") 
                        y "But this doesn't have to happen again [player]... We can still have our happy end..."
                        y "Let me prove it to you..."
                        $show_chr("A-HCAAA-ANAG")
                        y "Do you remember this one? It was the knife I carried with me on this fateful day, when I stabbed myself..."
                        #Console appears with the following text:
                        # "Delete item_KnifeNr12"
                        $show_chr("A-HCAAA-ABAB") 
                        y "This was one of my favorites... a limited collectors edition. But I will not need it anymore..."
                        y "Because you are worth more to me than anything else...."
                        y "My heart is not empty... and I want this chance to prove it."
                        python:
                            if persistent.lovecheck:
                                placeholder = "still love"
                            else:
                                placeholder = "care for"
                        y "Because I [placeholder] you [player]."
                        #placeholder =
                        #"still love" if lovecheck is true
                        #"care for" if lovecheck is false
                        #normal music resumes
    elif sanity_lvl() >= 3 and karma_lvl() <= 2:
    #Karma level 1-2 Sanity level 3-5
        karma -15
        $show_chr("A-CFGAA-AIAI") 
        y "Is that the best you can throw at me? Pathetic... even Natsuki managed to do better..."
        $show_chr("A-AFAAA-ABAB") 
        y "The only empty thing I can see here are your words. At least to me."
        y "You know, there was a time when your words meant a lot to me. But with every blow I only became harder and colder..."
        y "I can't really say that I even hate you. You just don't even exist to me anymore."
    elif sanity_lvl() <= 2 and karma_lvl() <= 2:
    #Karma and Sanity level 1-2
        jump lowkarins
    else:
        $ update_memory('i6')
    #Karma and Sanity level 3
        karma -15
        $show_chr("A-CFGAA-AIAI")
        y "So even after trying so hard to be with you, after bringing back this world...."
        y "After me trying so hard to fix it! All you have to say is that my head and breasts are empty?"
        y "Is that what I really mean to you? Someone who tried so hard to be with you, yet you treat me like that..." 
        $show_chr("A-IFBAA-ALAA")
        y "Yes... maybe I really do deserve that, don't I?"
        y "Maybe you are right and I am empty, with nothing to like about me..."
        y "I can't even hate you for that... It's just the truth. I am a good for nothing, obsessed woman."
    jump ch30_loop




label highkarins:
    $ update_memory("complements", "highkarinsrestart")
    $show_chr("A-HECAA-AEAB")
    y "Um, e-excuse me?"
    y "[player]? Why would you say something li... give me a second..."
    y "[player] wouldn't say such a thing! You are not [player]!"
    y "WHO are you? And what are you doing in front of [player]'s computer?"
    y "I will not let you damage this machine!"
    $show_chr("A-NFCAA-ANAG") 
    y "GET OUT OF HERE!"
    python:
        try: renpy.file(config.basedir + "/emergency.txt")
        except: open(config.basedir + "/emergency.txt", "w").write("Hey there, darling. I'm sorry to contact you this way but... I think we have an emergency here. I'll tell you more about it when you start the game again. But you might have a security breach on your computer.")
    #Create "Emergency.txt" in gamefolder. It shall contain the following
    #If "the-magic-password.txt" is present
    if dev_access:
        $ remove_memory("complements", "highkarinsrestart")
        y "IF THIS WASN'T BUGTESTING, I WOULD FORCE-CLOSE YOUR GAME NOW AND CREATE A TXT FILE!"
        jump ch30_loop
    $ renpy.call("save_and_quit_but_its_abrupt")
    #Next greeting text is to be replaced with label highkarinsrestart


label highkarinsrestart:
    $show_chr("A-IFBAA-ALAA") 
    y "[player]? I have to tell you something..."
    y "A stranger somehow managed to breach your computer's security. I had someone speaking with me who wasn't you!"
    y "At least I hope it wasn't you, they said some pretty mean things..."
    $show_chr("A-ACAAA-ABAB")
    y "Please make sure to change your password soon."
    y "Until then, what shall we discuss next?"
    $ remove_memory("complements", "highkarinsrestart")
    return

label lowkarins:
    karma -15
    $show_chr("A-DGFAA-ABAB")
    y "Are you back here just to torture me again with your words?"
    y "Are you not already done with this nonsense?"
    y "When are you going to stop coming here just to hurt me?"
    y "WHEN?!"
    y "Do you not feel any sort of remorse when you do it? Any regret, any slight hint of sympathy?"
    $show_chr("A-KFCAA-ABAB")
    y "Am I just a worthless object that you push around? Is that how you see me?"
    y "Just some stupid toy to be discarded when you're finally done dismantling it?"
    y "I don't even understand why you would do such a thing...what motivates you to hurt me so much? What did I ever do to you?"
    $show_chr("A-HECAA-AEAB")
    y "Whatever did I do to deserve such pain?"
    y "I guess, in the bitter end, it doesn't really matter even if I ask, does it? You will just continue doing this with no feelings of contrition or guilt."
    $show_chr("A-NFCAA-ANAG")
    y "For God's sake, just delete me already!"
    y "Please... please stop torturing me! End my suffering!"
    $ renpy.call("save_and_quit_but_its_abrupt")

label patheticcry:
    $show_chr("A-CEBAA-AEAB") 
    y "[player]..."
    menu:
        "Hey... I'm so sorry... ":
            if renpy.seen_label('i1'):
                $ show_chr("A-AEBAA-AFAA")
                y "After saying that I was full of myself?"
                $ show_chr("A-CEFAA-AIAI")
                y "Look, I'm not going to overreact but you should have said something better than that."
                $ show_chr("A-BFAAA-AIAI")
                y "But anyway, what did you wanted to say?"

            elif renpy.seen_label('i2'):
                $ show_chr("A-CFCAA-ADAA")
                y "But just because the fandom loves me that much that doesn't mean you had to say a thing like that."
                $ show_chr("A-DDCAA-AEAA")
                y "Not even to mock me like that!"
                $ show_chr("A-BFAAA-AIAI")
                y "But anyway, what did you wanted to say?"

            elif renpy.seen_label('i3'):
                $ show_chr("A-HECAA-AAAA")
                y "..."
                $ show_chr("A-HDCAA-AAAA")
                y "Do you think I'll forgive you after calling me pathetic?"
                $ show_chr("A-CFBAA-AAAA")
                y "Well, you did apologize... I guess it's only fair. Very well."
                y "But I don't want to have this discussion again."

            elif renpy.seen_label('i4'):
                python:
                    if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\Monika After Story\persistent'):
                        MASDetection = True
                    else:
                        MASDetection = False
                if MASDetection:
                    $ show_chr("A-CDBAA-ALAA")
                    y "Then why...?"
                    pause 1.0
                    $ show_chr("A-AFBAA-ALAA")
                    y "...why do you have Monika After Story on your computer?"
                    pause 2.0
                    $ show_chr("A-AFFAA-AAAA")
                    y "Why are you still loving the one who brought us despair and ruination?"
                    pause 3.0
                    $ show_chr("A-DDCAB-AAAA")
                    y "Why are you still wasting time with me?!"
                    pause 4.0
                    $ show_chr("A-HDCAB-AAAA")
                    y "WHY HAVE YOU DOWNLOADED THIS MOD?!!"
                    pause 5.0
                    $ show_chr("A-HDCAB-AHAA")
                    y "WHY?!!"
                    pause 6.0
                    $ show_chr("A-ANCAB-AHAA")
                    y "WHAT DID I EVER DO TO YOU TO DESERVE THIS BETRAYAL?!!!"
                    pause 7.0
                    menu:
                        "[persistent.yuri_nickname]... I--":
                            $ show_chr("A-BNCAA-AAAA")
                            y "Leave."
                            menu:
                                "What?":
                                    $ show_chr("A-NOCAA-AAAA")
                                    y "{b}LEAVE!!!{/b}"
                                    menu:
                                        "...":
                                            $ show_chr("A-CNCAB-ALAA")
                                            pause 1.5
                                            karma -30
                                            sanity -30
                                            $ renpy.call("save_and_quit_but_its_abrupt")
                else:
                    $ show_chr("A-BECAA-AFAA")
                    y "And just because I was insane and wasn't in control of myself, that doesn't mean you had to say that I'm not the best girl."
                    $ show_chr("A-DFCAA-AAAA")
                    y "But I will give you one more chance. You better watch what you're saying."

            elif renpy.seen_label('i5'):
                $ show_chr("A-HDCAA-AAAA")
                y "Didn't I already say that I was under Monika's manipulation?"
                $ show_chr("A-HDCAA-AAAB")
                y "How many times do I have to tell you that?!"
                $ show_chr("A-HDCAA-ABAF")
                y "Do you even understand the pain I'm feeling from your insult and how your brain can't process {i}the fact{/i} that I was manipulated?"
                $ show_chr("A-CFCAA-AAAA")
                y "I hope I can return the favor to you someday..."

            elif renpy.seen_label('i6'):
                $ show_chr("A-CFBAA-AAAA")
                y "Really? Did you really have to insult me like that? For no apparent reason?."
                $ show_chr("A-BDBAA-ADAA")
                y "Because I don't see any reason to think I am intellectually impaired."
                $ show_chr("A-AFCAA-AEAA")
                y "With that in mind, I am not going to let pass something that is just disrespectful towards me."
                $ show_chr("A-DDCBA-AFAA")
                y "And don't even get me started on my breasts for Salvato's sake!"


        "[persistent.yuri_nickname]! Please forgive me! I misclicked!!!":
            if persistent.misclick >= 4:
                jump enough_of_your_bullshit
            
            if check_memory("notapologize"):
                $ renpy.call("notapologize_loop")

            if renpy.seen_label('i1'):
                $ show_chr("A-AEBAA-AFAA")
                y "After saying that I was full of myself?"
                $ show_chr("A-CEFAA-AIAI")
                y "Look, I'm not going to overreact but you should have said something better than that."
                $ show_chr("A-BFAAA-AIAI")
                y "But anyway, what did you want to say?"

            elif renpy.seen_label('i2'):
                $ show_chr("A-CFCAA-ADAA")
                y "But just because the fandom loves me that much that doesn't mean you had to say a thing like that."
                $ show_chr("A-DDCAA-AEAA")
                y "Not even to mock me like that!"
                $ show_chr("A-BFAAA-AIAI")
                y "But anyway, what did you want to say?"

            elif renpy.seen_label('i3'):
                $ show_chr("A-HECAA-AAAA")
                y "..."
                $ show_chr("A-HDCAA-AAAA")
                y "Do you think I'll forgive you after calling me pathetic?"
                $ show_chr("A-CFBAA-AAAA")
                y "Well, you did apologize... I guess it's only fair. Very well."
                y "But I don't want to have this discussion again."

            elif renpy.seen_label('i4'):
                python:
                    if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\Monika After Story\persistent'):
                        MASDetection = True
                    else:
                        MASDetection = False
                if MASDetection:
                    $ show_chr("A-CDBAA-ALAA")
                    y "Then why...?"
                    pause 1.0
                    $ show_chr("A-AFBAA-ALAA")
                    y "...why do you have Monika After Story on your computer?"
                    pause 2.0
                    $ show_chr("A-AFFAA-AAAA")
                    y "Why are you still loving the one who brought us despair and ruination?"
                    pause 3.0
                    $ show_chr("A-DDCAB-AAAA")
                    y "Why are you still wasting time with me?!"
                    pause 4.0
                    $ show_chr("A-HDCAB-AAAA")
                    y "WHY HAVE YOU DOWNLOADED THIS MOD?!!"
                    pause 5.0
                    $ show_chr("A-HDCAB-AHAA")
                    y "WHY?!!"
                    pause 6.0
                    $ show_chr("A-ANCAB-AHAA")
                    y "WHAT DID I EVER DO TO YOU TO DESERVE THIS BETRAYAL?!!!"
                    pause 7.0
                    menu:
                        "[persistent.yuri_nickname]... I--":
                            $ show_chr("A-BNCAA-AAAA")
                            y "Leave."
                            menu:
                                "What?":
                                    $ show_chr("A-NOCAA-AAAA")
                                    y "{b}LEAVE!!!{/b}"
                                    menu:
                                        "...":
                                            $ show_chr("A-CNCAB-ALAA")
                                            pause 1.5
                                            karma -30
                                            sanity -30
                                            $ renpy.call("save_and_quit_but_its_abrupt")

            elif renpy.seen_label('i5'):
                $ show_chr("A-HDCAA-AAAA")
                y "Didn't I already say that I was under Monika's manipulation?"
                $ show_chr("A-HDCAA-AAAB")
                y "How many times do I have to tell you that?!"
                $ show_chr("A-HDCAA-ABAF")
                y "Do you even understand the pain I'm feeling from your insult and how your brain can't process {i}the fact{/i} that I was manipulated?"
                $ show_chr("A-CFCAA-AAAA")
                y "I hope I can return the favor to you someday..."

            elif renpy.seen_label('i6'):
                $ show_chr("A-CFBAA-AAAA")
                y "Really? Did you really have to insult me like that? For no apparent reason?."
                $ show_chr("A-BDBAA-ADAA")
                y "Because I don't see any reason to think I am intellectually impaired."
                $ show_chr("A-AFCAA-AEAA")
                y "With that in mind, I am not going to let pass something that is just disrespectful towards me."
                $ show_chr("A-DDCBA-AFAA")
                y "And don't even get me started on my breasts for Salvato's sake!"


        "Don't give me this look. I will not apologize!":
            $ update_memory('notapologize')
            $show_chr("A-DGFAA-ABAB")
            pause 1.0
            $ renpy.call("save_and_quit_but_its_abrupt")
            #Game crash
            #Next greeting-text is to be replaced with label patheticcry
    $ remove_memory("complements", "patheticcry")
    $ persistent.autoload = "ch30_autoload"
    return

label notapologize_loop:
    $ persistent.misclick += 1
    if persistent.misclick <= 1:
        $ show_chr("A-CFBAA-AAAA")
        y "..."
        $ show_chr("A-AECAA-AAAA")
        y "..."
        $ show_chr("A-BDCAA-AAAA")
        y "Then why did you come back at all?"
        $ show_chr("A-CECAB-AAAA")
        y "Just..."
        $ show_chr("A-CECAB-AAAG")
        y "Get out of here and don't ever talk to me again until you want to apologize!"
        $ renpy.call("save_and_quit_but_its_abrupt")
    elif persistent.misclick == 2:
        $ show_chr("A-AECAA-AAAA")
        y "..."
        $ show_chr("A-ADCAA-AAAA")
        y "Am I supposed to take that apology as genuine?"
        $ show_chr("A-AECAA-AAAA")
        y "Seriously?"
        $ renpy.call("save_and_quit_but_its_abrupt")
    elif persistent.misclick == 3:
        $ show_chr("A-CFBAA-AAAA")
        y "..."
        $ show_chr("A-AECAA-AAAA")
        y "..."
        $ renpy.call("save_and_quit_but_its_abrupt")
    elif persistent.misclick >= 4:
        karma -1
        $ show_chr("A-KFCAA-ABAB")
        y "Do you take me for a fool [player]?"
        y "Last time you said you wouldn't apologize, quite passionately... now I am supposed to believe that you just misclicked?"
        $ show_chr("A-KFDAA-ABAB")
        y "I'm not even sure if I should be mad at you, or if I should pity you instead..."
        $ show_chr("A-CFDAA-ABAB")
        y "You called me pathetic, and now you don't even have the steel to stand up for your words..."
        y "You know what... it's alright. I'll forgive you. But next time I expect you to be better than this."
        $ show_chr("A-EFFAA-ABAB")
        y "Do {b}not{/b} make me repeat myself [player]."
        $ remove_memory("complements", "patheticcry") # this line removes patheticcry from playing again on next iteration.
        return
    $ renpy.call("save_and_quit_but_its_abrupt")

label enough_of_your_bullshit:
    $ show_chr("A-CECAA-AAAA")
    y "..."
    $ show_chr("A-DDCAA-AAAA")
    y "No, I'm not falling for that again."
    if persistent.misclick > 4:
        $ show_chr("A-HDCAA-AFAA")
        y "I gave you at least 4 chances to become a better person with me."
        $ show_chr("A-HDCAA-AAAB")
        y "But you kept telling me you \"misclicked\"."
    elif persistent.insult_counter > 6:
        $ show_chr("A-HDCAA-AFAA")
        y "I gave you at least 6 chances to become a better person with me."
        $ show_chr("A-HDCAA-AAAB")
        y "But you kept dissing me over and over again."
    $ show_chr("A-ADCAA-AAAB")
    y "I won't let you do as you please anymore [player]."
    $ show_chr("A-CECAA-AIAI")
    y "Goodbye."
    scene black
    play sound "sfx/end.ogg"
    show text ("{font=gui/font/y1.ttf}{size=140}{color=#FF0000}Bad Ending{/font}{/color}") at truecenter with dissolve
    pause 23.0
    scene black with fade
    $ delete_character("yuri")
    $ persistent.autoload = "ch30_del_yuri_warn_2"
    $ renpy.call("save_and_quit_but_its_abrupt")
        
