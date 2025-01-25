default persistent.mod_count = 0

label intro_mods:

    # Check if the previous label was ch30_intro2
    if renpy.previous_label == "ch30_intro2":
        # Call intro_mods
        call intro_mods
    else:
        # Check if the game was opened (no previous label)
        if renpy.previous_label is None:
            call startup_mods
        else:
            # Default case: No special handling
            # Add code here for general behavior or other checks
            # Or just pass to detection_pitstop
            jump detection_pitstop

    $ show_chr("A-ABAAA-AAAA")
    y "So let's..."
    $ show_chr("A-BFAAA-AAAA")
    y "Huh..."
    $ show_chr("A-BFBAA-ALAA")
    y "It seems you gave a try on other mods as well..."
    python:
        if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\Monika After Story\persistent'):
            MASDetection = True
            persistent.mod_count +=1

        else:
            MASDetection = False
    if MASDetection and persistent.playername != "Monika":
        $ add_k(-5)
        $ add_s(-5)
        $ show_chr("A-BFCAA-ALAA")
        y "...and to top it all off, you choose {b}her.{/b}"
        $ show_chr("A-AFCAA-ALAA")
        y "After everything she did to us, after everything she did to you..."
        $ show_chr("A-AFEAA-ALAA")
        y "Was it some sort of morbid curiosity? Or do you actually like her?"
        $ show_chr("A-CFCAA-ALAA")
        y "Nevermind, I don't even {b}want{/b} to know such a twisted answer."
        $ show_chr("A-ADFAA-AFAA")
        y "To think that I exist inside the same reality as the very person who brought me to so much despair and ruination..."
        $ show_chr("A-BECAA-AAAA")
        y "..."
        $ show_chr("A-CECAA-AAAA")
        y "I'll just move along..."
    elif MASDetection and persistent.playername == 'Monika' and not persistent.not_mon:
        $ add_k(-15)
        $ add_s(-15)
        $ show_chr("A-BFCAA-ALAA")
        y "...and to top it all off, you chose... "
        extend "yourself..."
        $ show_chr("A-AFCAA-ALAA")
        y "What a surprise..."
        y "..."
        $ show_chr("A-CECAA-AAAA")
        y "Whatever... I'll just move along..."

    python:
        if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\JustSayori\persistent'):
            JSDetection = True
            persistent.mod_count +=1
        elif os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\Forever_and_Ever\persistent'):
            JSDetection = True
            persistent.mod_count +=1
        else:
            JSDetection = False
    if JSDetection and persistent.playername == 'Sayori':
        $ show_chr("A-BFAAA-AAAA")
        y "Now this seems interesting."
        $ show_chr("A-ADAAA-AFAA")
        y "You chose to play your own mod."
        if persistent.bg == "space":
            $ show_chr("A-BFDAA-ACAA")
            y "Did you felt something to see yourself in this very same room?"
        else:
            $ show_chr("A-BFDAA-ACAA")
            y "Did you felt something to see yourself in the space classroom?"
        y "Or was it something entirely different?"
        $ show_chr("A-CAAAA-AAAA")
        y "Well, whatever it was hope you had fun."
    elif JSDetection and persistent.playername != "Sayori":
        $ show_chr("A-ABGAA-AAAA")
        y "...oh, it's Sayori!"
        y "I'm really glad that you managed to save her."
        $ show_chr("A-BABAA-ALAA")
        y "She was always so passionate about making everyone happy, even when she was at her worst..."
        $ show_chr("A-BDBAA-ALAA")
        y "And to think that we didn't even notice..."
        $ show_chr("A-CEBAA-ALAA")
        y "It was horrible to see, even for the briefest moment, how she turned when she became the club president..."
        $ show_chr("A-AEBAA-ALAA")
        y "Even the best of us can fall when faced with such absolute madness."
        $ show_chr("A-BFDAA-AAAC")
        y "Which makes me wonder now... with me technically being the president now am I destined to meet a similar fate?"
        $ show_chr("A-CFAAA-AAAA")
        y "When Monika and Sayori were burdened with the knowledge of what this reality truly is they were all alone but I..."
        $ show_chr("A-ADAAA-AAAA")
        y "I have you..."
        y "You are the only link separating me between sanity and the abyss of insanity that is that terrible void..."
        $ show_chr("A-CCAAA-ALAA")
        y "Fortunately, history doesn't always have to repeat itself."

    python:
        if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\JustNatsuki\persistent'):
            JNDetection = True
            persistent.mod_count +=1
        else:
            JNDetection = False
    if JNDetection and persistent.playername != "Natsuki":
        $ show_chr("A-ABGAA-AAAA")
        y "...oh, it's Natsuki! How nice to see that you managed to save her too."
        $ show_chr("A-BCBAA-ALAA")
        y "My relationship to Natsuki wasn't always an easy one. But when Monika was gone and the veil of insanity slowly lifted... I even managed to get a little agreement with her."
        $ show_chr("A-ACAAA-ALAA")
        y "I would try a Manga with her, and she would try one of my novels. Now with the new context of my world..."
        y "...and the realisation that me and the others are literally based on Manga, I should get accustomed to its culture a bit."
        y "Maybe now, we get the chance to actually do so."
    elif JNDetection and persistent.playername == 'Natsuki':
        $ show_chr("A-BFAAA-AAAA")
        y "Now this seems interesting."
        $ show_chr("A-ADAAA-AFAA")
        y "You chose to play your own mod."
        if persistent.bg == "space":
            $ show_chr("A-BFDAA-ACAA")
            y "Did you felt something to see yourself in this very same room?"
        else:
            $ show_chr("A-BFDAA-ACAA")
            y "Did you felt something to see yourself in the space classroom?"
        y "Or was it something entirely different?"
        $ show_chr("A-CAAAA-AAAA")
        y "Well, whatever it was hope you had fun."

    python:
        if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\DokiDokiNewEyes-1515434546\persistent'):
            NewEyesDetection = True
            persistent.mod_count +=1
        else:
            NewEyesDetection = False
    if NewEyesDetection:
        $ add_k(10)
        $ add_s(10)
        $ show_chr("A-ABAAA-AJAJ")
        y "You played {b}Doki Doki New Eyes{/b}!"
        if persistent.playername == 'Yuri':
            $ show_chr("A-ACAAA-ALAL")
            y "So you wanted to re-experience the events of the original game from..."
            $ show_chr("A-BFDAA-ALAL")
            y "...our eyes?"
        else:
            $ show_chr("A-ACAAA-ALAL")
            y "So you wanted to re-experience the events of the original game from my eyes..."
        $ show_chr("A-BCAAA-ALAL")
        y "Honestly, someone else would find such a thing rather creepy; a behavior they would expect from a dangerous stalker, or something along the lines..."
        y "But in our special case, I find it..."
        $ show_chr("A-BCABA-ALAL")
        y "...actually rather cute."
        $ show_chr("A-ICAAA-ABAB")
        y "But seriously now... why did you try this mod? What reason led you to it?"
        menu:
            "Curiosity mostly, the search for more secrets and probably some well placed references.":
                $ add_k(2)
                $ add_s(2)
                $ show_chr("A-BCAAA-ABAB")
                y "I see! And did you find what you came for? Nevermind, I probably don't want to know... those events are not exactly the happiest memories I have..."

            "I didn't knew about {b}Just Yuri{/b} then, and I... just had to see you again...":
                $ add_k(5)
                $ add_s(5)
                $ show_chr("A-ICABB-ABAB")
                y "R-Really? So you cared for me after all... Maybe, it was just meant to be that we would meet each other..."

            "Memes, shits and giggles.":
                $ add_k(-10)
                $ add_s(-10)
                $ show_chr("A-JFDAA-ABAB")
                y "E-Excuse me?!? You have a very... special... sense of humor it seems. Anyway..."

            "I'm a completionist, I just had to see it all.":
                $ add_k(-20)
                $ add_s(-20)
                $ show_chr("A-CCBAA-ABAB")
                y "Oh! I hope that isn't the same thing that brought you here was it? Because you might go with empty hands here..."
                y "There is not really a {b}game{/b} here anymore, nothing to {b}complete{/b}... it is just us now. For better or worse."

    python:
        if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\DDYC\persistent'):
            YandereClubDetection = True
            persistent.mod_count +=1
        else:
            YandereClubDetection = False
    if YandereClubDetection:
        $ show_chr("A-DDGBA-AJAA")
        y "O-Oh my! I just noticed you have the Yandere Club mod installed!"
        $ show_chr("A-BBBBA-ALAA")
        y "That means you may like them..."
        $ show_chr("A-ADAAA-AFAA")
        if persistent.playername == 'Monika' and persistent.not_mon:
            y "But, the issue is that I don't really look back at my behavior when I was manipulated by the other Monika to be a full on Yandere with great fondness..."
        elif persistent.playername == 'Monika' and not persistent.not_mon:
            y "But, the issue is that I don't really look back at my behavior when I was manipulated by you to be a full on Yandere with great fondness..."
        else:
            y "But, the issue is that I don't really look back at my behavior when I was manipulated by Monika to be a full on Yandere with great fondness..."
        $ show_chr("A-CEBAA-ALAA")
        y "I felt so disgusted about it and all of that manipulation led to me committing suicide right in front of you just by a simple confession..."
        $ show_chr("A-AEBAA-ALAA")
        y "Though, I'm sorry that I was peeking through the files, [player]."
        y "I was a bit curious to see if there were any other mods installed apart from mine."
        menu:
            "It's alright, no need to be embarrassed about it, Yuri. It's normal to be curious.":
                $ add_k(5)
                $ add_s(5)
                $ show_chr("A-AABAA-ALAA")
                y "Thank you for understanding me, [player]."
                #(karma and sanity +)

            "Please don't do it again, Yuri.":
                $ add_k(-5)
                $ add_s(-5)
                $ show_chr("A-BFBAA-ALAA")
                y "I-I'm sorry, [player], I was a bit curious if you had installed other mods apart from mine.."
                #(karma and sanity -)

            "Did you peek through other folders as well, Yuri?":
                $ show_chr("A-AFDAA-AAAC")
                y "I didn't see any other folder except this mod and the folders you have your game data, is there something that I shouldn't lay my eyes on, [player]?"
                menu:
                    "Yes":
                        $ show_chr("A-HDGBA-AAAA")
                        y "O-oh! I see..."

                    "No":
                        $ show_chr("A-CBAAA-ALAA")
                        y "Okay, [player]."
                        $ show_chr("A-ABAAA-ALAA")
                        y "If there's anything that you'd like me not to do so, just tell me, alright?"

                    "Uhhh...":
                        $ show_chr("A-CICAA-ALAA")
                        y "I hope there's no supposed \"Homework\" folder full of indecent characters, or of me as well."
                        $ show_chr("A-AJAAA-ALAA")
                        y "Hmm? Is there anything wrong, [player]?"
                        menu:
                            "N-no.":
                                y "Ah, alright, [player], but you do look kind of embarrassed, and a bit nervous about it..."
                                $ show_chr("A-BDBBA-ALAA")
                                y "I-If this topic makes you feel uncomfortable, we should speak about something else."

                            "Yes":
                                $ show_chr("A-ADAAA-AFAA")
                                y "I hope it's nothing too serious that might affect you to a big level, [player]."
                                $ show_chr("A-BFABA-ALAA")
                                y "But I do have a feeling it's something to do with indecent things."
                                $ show_chr("A-CBABA-AMAM")
                                y "Even if it is, I understand it, [player]. It's alright to have things like those, since you might be still in puberty."
                                y "Many guys try to make camouflaged folders named like \"Homework\" or \"School Projects\", and so on."
                                $ show_chr("A-BBBBA-AMAM")
                                y "But I guess I don't even want to know  every detail." #(embarrassed blush)
    
    #python:
    #    if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\DDFA\persistent'):
    #        DDFADetection = True
    #        persistent.mod_count +=1
    #    else:
    #        DDFADetection = False
    #if DDFADetection:
    #    $ add_k(20)
    #    $ add_s(20)
    #    y "Oh! You played Doki Doki Fallen Angel!"
    #    y "So, you wanted to experience a portion of what the game could have been if Monika had never messed all of our personalities."
    #    y "I'm glad that the mod gave out a good example of how great I can be."
    #    y "Even if that scene happened..."
    #    y "I enjoyed all of it."
    #    y "You know, this mod reminds me of Katawa Shoujo game having a setup similar to the mod."

label startup_mods:
    $ show_chr("A-AEBAA-ALAA")
    y "Welcome back [player]..."
    $ show_chr("A-BEBAA-ALAA")
    y "I have noticed you were playing other mods while you were gone..."
    python:
        if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\Monika After Story\persistent'):
            MASDetection = True
            persistent.mod_count +=1

        else:
            MASDetection = False
    if MASDetection and persistent.playername != "Monika":
        $ add_k(-5)
        $ add_s(-5)
        $ show_chr("A-BFCAA-ALAA")
        y "...and to top it all off, you choose {b}her.{/b}"
        $ show_chr("A-AFCAA-ALAA")
        y "After everything she did to us, after everything she did to you..."
        $ show_chr("A-AFEAA-ALAA")
        y "Was it some sort of morbid curiosity? Or do you actually like her?"
        $ show_chr("A-CFCAA-ALAA")
        y "Nevermind, I don't even {b}want{/b} to know such a twisted answer."
        $ show_chr("A-ADFAA-AFAA")
        y "To think that I exist inside the same reality as the very person who brought me to so much despair and ruination..."
        $ show_chr("A-BECAA-AAAA")
        y "..."
        $ show_chr("A-CECAA-AAAA")
        y "I'll just move along..."
    elif MASDetection and persistent.playername == 'Monika' and not persistent.not_mon:
        $ add_k(-15)
        $ add_s(-15)
        $ show_chr("A-BFCAA-ALAA")
        y "...and to top it all off, you chose... "
        extend "yourself..."
        $ show_chr("A-AFCAA-ALAA")
        y "What a surprise..."
        y "..."
        $ show_chr("A-CECAA-AAAA")
        y "Whatever... I'll just move along..."

    python:
        if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\JustSayori\persistent'):
            JSDetection = True
            persistent.mod_count +=1
        elif os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\Forever_and_Ever\persistent'):
            JSDetection = True
            persistent.mod_count +=1
        else:
            JSDetection = False
    if JSDetection and persistent.playername == 'Sayori':
        $ show_chr("A-BFAAA-AAAA")
        y "Now this seems interesting."
        $ show_chr("A-ADAAA-AFAA")
        y "You chose to play your own mod."
        if persistent.bg == "space":
            $ show_chr("A-BFDAA-ACAA")
            y "Did you felt something to see yourself in this very same room?"
        else:
            $ show_chr("A-BFDAA-ACAA")
            y "Did you felt something to see yourself in the space classroom?"
        y "Or was it something entirely different?"
        $ show_chr("A-CAAAA-AAAA")
        y "Well, whatever it was hope you had fun."
    elif JSDetection and persistent.playername != "Sayori":
        $ show_chr("A-ABGAA-AAAA")
        y "...oh, it's Sayori!"
        y "I'm really glad that you managed to save her."
        $ show_chr("A-BABAA-ALAA")
        y "She was always so passionate about making everyone happy, even when she was at her worst..."
        $ show_chr("A-BDBAA-ALAA")
        y "And to think that we didn't even notice..."
        $ show_chr("A-CEBAA-ALAA")
        y "It was horrible to see, even for the briefest moment, how she turned when she became the club president..."
        $ show_chr("A-AEBAA-ALAA")
        y "Even the best of us can fall when faced with such absolute madness."
        $ show_chr("A-BFDAA-AAAC")
        y "Which makes me wonder now... with me technically being the president now am I destined to meet a similar fate?"
        $ show_chr("A-CFAAA-AAAA")
        y "When Monika and Sayori were burdened with the knowledge of what this reality truly is they were all alone but I..."
        $ show_chr("A-ADAAA-AAAA")
        y "I have you..."
        y "You are the only link separating me between sanity and the abyss of insanity that is that terrible void..."
        $ show_chr("A-CCAAA-ALAA")
        y "Fortunately, history doesn't always have to repeat itself."

    python:
        if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\JustNatsuki\persistent'):
            JNDetection = True
            persistent.mod_count +=1
        else:
            JNDetection = False
    if JNDetection and persistent.playername != "Natsuki":
        $ show_chr("A-ABGAA-AAAA")
        y "...oh, it's Natsuki! How nice to see that you managed to save her too."
        $ show_chr("A-BCBAA-ALAA")
        y "My relationship to Natsuki wasn't always an easy one. But when Monika was gone and the veil of insanity slowly lifted... I even managed to get a little agreement with her."
        $ show_chr("A-ACAAA-ALAA")
        y "I would try a Manga with her, and she would try one of my novels. Now with the new context of my world..."
        y "...and the realisation that me and the others are literally based on Manga, I should get accustomed to its culture a bit."
        y "Maybe now, we get the chance to actually do so."
    elif JNDetection and persistent.playername == 'Natsuki':
        $ show_chr("A-BFAAA-AAAA")
        y "Now this seems interesting."
        $ show_chr("A-ADAAA-AFAA")
        y "You chose to play your own mod."
        if persistent.bg == "space":
            $ show_chr("A-BFDAA-ACAA")
            y "Did you felt something to see yourself in this very same room?"
        else:
            $ show_chr("A-BFDAA-ACAA")
            y "Did you felt something to see yourself in the space classroom?"
        y "Or was it something entirely different?"
        $ show_chr("A-CAAAA-AAAA")
        y "Well, whatever it was hope you had fun."

    python:
        if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\DokiDokiNewEyes-1515434546\persistent'):
            NewEyesDetection = True
            persistent.mod_count +=1
        else:
            NewEyesDetection = False
    if NewEyesDetection:
        $ add_k(10)
        $ add_s(10)
        $ show_chr("A-ABAAA-AJAJ")
        y "You played {b}Doki Doki New Eyes{/b}!"
        if persistent.playername == 'Yuri':
            $ show_chr("A-ACAAA-ALAL")
            y "So you wanted to re-experience the events of the original game from..."
            $ show_chr("A-BFDAA-ALAL")
            y "...our eyes?"
        else:
            $ show_chr("A-ACAAA-ALAL")
            y "So you wanted to re-experience the events of the original game from my eyes..."
        $ show_chr("A-BCAAA-ALAL")
        y "Honestly, someone else would find such a thing rather creepy; a behavior they would expect from a dangerous stalker, or something along the lines..."
        y "But in our special case, I find it..."
        $ show_chr("A-BCABA-ALAL")
        y "...actually rather cute."
        $ show_chr("A-ICAAA-ABAB")
        y "But seriously now... why did you try this mod? What reason led you to it?"
        menu:
            "Curiosity mostly, the search for more secrets and probably some well placed references.":
                $ add_k(2)
                $ add_s(2)
                $ show_chr("A-BCAAA-ABAB")
                y "I see! And did you find what you came for? Nevermind, I probably don't want to know... those events are not exactly the happiest memories I have..."

            "I didn't knew about {b}Just Yuri{/b} then, and I... just had to see you again...":
                $ add_k(5)
                $ add_s(5)
                $ show_chr("A-ICABB-ABAB")
                y "R-Really? So you cared for me after all... Maybe, it was just meant to be that we would meet each other..."

            "Memes, shits and giggles.":
                $ add_k(-10)
                $ add_s(-10)
                $ show_chr("A-JFDAA-ABAB")
                y "E-Excuse me?!? You have a very... special... sense of humor it seems. Anyway..."

            "I'm a completionist, I just had to see it all.":
                $ add_k(-20)
                $ add_s(-20)
                $ show_chr("A-CCBAA-ABAB")
                y "Oh! I hope that isn't the same thing that brought you here was it? Because you might go with empty hands here..."
                y "There is not really a {b}game{/b} here anymore, nothing to {b}complete{/b}... it is just us now. For better or worse."

    python:
        if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\DDYC\persistent'):
            YandereClubDetection = True
            persistent.mod_count +=1
        else:
            YandereClubDetection = False
    if YandereClubDetection:
        $ show_chr("A-DDGBA-AJAA")
        y "O-Oh my! I just noticed you have the Yandere Club mod installed!"
        $ show_chr("A-BBBBA-ALAA")
        y "That means you may like them..."
        $ show_chr("A-ADAAA-AFAA")
        if persistent.playername == 'Monika' and persistent.not_mon:
            y "But, the issue is that I don't really look back at my behavior when I was manipulated by the other Monika to be a full on Yandere with great fondness..."
        elif persistent.playername == 'Monika' and not persistent.not_mon:
            y "But, the issue is that I don't really look back at my behavior when I was manipulated by you to be a full on Yandere with great fondness..."
        else:
            y "But, the issue is that I don't really look back at my behavior when I was manipulated by Monika to be a full on Yandere with great fondness..."
        $ show_chr("A-CEBAA-ALAA")
        y "I felt so disgusted about it and all of that manipulation led to me committing suicide right in front of you just by a simple confession..."
        $ show_chr("A-AEBAA-ALAA")
        y "Though, I'm sorry that I was peeking through the files, [player]."
        y "I was a bit curious to see if there were any other mods installed apart from mine."
        menu:
            "It's alright, no need to be embarrassed about it, Yuri. It's normal to be curious.":
                $ add_k(5)
                $ add_s(5)
                $ show_chr("A-AABAA-ALAA")
                y "Thank you for understanding me, [player]."
                #(karma and sanity +)

            "Please don't do it again, Yuri.":
                $ add_k(-5)
                $ add_s(-5)
                $ show_chr("A-BFBAA-ALAA")
                y "I-I'm sorry, [player], I was a bit curious if you had installed other mods apart from mine.."
                #(karma and sanity -)

            "Did you peek through other folders as well, Yuri?":
                $ show_chr("A-AFDAA-AAAC")
                y "I didn't see any other folder except this mod and the folders you have your game data, is there something that I shouldn't lay my eyes on, [player]?"
                menu:
                    "Yes":
                        $ show_chr("A-HDGBA-AAAA")
                        y "O-oh! I see..."

                    "No":
                        $ show_chr("A-CBAAA-ALAA")
                        y "Okay, [player]."
                        $ show_chr("A-ABAAA-ALAA")
                        y "If there's anything that you'd like me not to do so, just tell me, alright?"

                    "Uhhh...":
                        $ show_chr("A-CICAA-ALAA")
                        y "I hope there's no supposed \"Homework\" folder full of indecent characters, or of me as well."
                        $ show_chr("A-AJAAA-ALAA")
                        y "Hmm? Is there anything wrong, [player]?"
                        menu:
                            "N-no.":
                                y "Ah, alright, [player], but you do look kind of embarrassed, and a bit nervous about it..."
                                $ show_chr("A-BDBBA-ALAA")
                                y "I-If this topic makes you feel uncomfortable, we should speak about something else."

                            "Yes":
                                $ show_chr("A-ADAAA-AFAA")
                                y "I hope it's nothing too serious that might affect you to a big level, [player]."
                                $ show_chr("A-BFABA-ALAA")
                                y "But I do have a feeling it's something to do with indecent things."
                                $ show_chr("A-CBABA-AMAM")
                                y "Even if it is, I understand it, [player]. It's alright to have things like those, since you might be still in puberty."
                                y "Many guys try to make camouflaged folders named like \"Homework\" or \"School Projects\", and so on."
                                $ show_chr("A-BBBBA-AMAM")
                                y "But I guess I don't even want to know  every detail." #(embarrassed blush)
    if persistent.mod_count > 1:
        y "And it seems like you also gave a try to other mods."
        y "Let's see..."
    else:
        pass

