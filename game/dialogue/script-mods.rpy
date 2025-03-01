default persistent.mod_count = 0
default persistent.last_closed = 0  # Add a variable to track last game closure time

init python:
    import time
    import os

label intro_mods:
    # This label should only be called if the previous label was ch30_intro2
    if check_memory("ch30_intro2"):
        # (Rest of your intro_mods code, processing each mod)
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
            karma -5
            sanity -5
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
            karma -15
            sanity -15
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
            karma 10
            sanity 10
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
                    karma 2
                    sanity 2
                    $ show_chr("A-BCAAA-ABAB")
                    y "I see! And did you find what you came for? Nevermind, I probably don't want to know... those events are not exactly the happiest memories I have..."

                "I didn't knew about {b}Just Yuri{/b} then, and I... just had to see you again...":
                    karma 5
                    sanity 5
                    $ show_chr("A-ICABB-ABAB")
                    y "R-Really? So you cared for me after all... Maybe, it was just meant to be that we would meet each other..."

                "Memes, shits and giggles.":
                    karma -10
                    sanity -10
                    $ show_chr("A-JFDAA-ABAB")
                    y "E-Excuse me?!? You have a very... special... sense of humor it seems. Anyway..."

                "I'm a completionist, I just had to see it all.":
                    karma -20
                    sanity -20
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
                    karma 5
                    sanity 5
                    $ show_chr("A-AABAA-ALAA")
                    y "Thank you for understanding me, [player]."
                    #(karma and sanity +)

                "Please don't do it again, Yuri.":
                    karma -5
                    sanity -5
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
        
        python:
            if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\DDFA\persistent'):
                DDFADetection = True
                persistent.mod_count += 1
            else:
                DDFADetection = False
        if DDFADetection:
            # Initial reaction - thoughtful, slightly hesitant
            $ show_chr("A-ABAAA-ALAA")
            y "I see... you've played Doki Doki Fallen Angel."
            y "An alternate reality where... things unfolded differently."
            $ show_chr("A-ADAAA-ALAL")
            y "It's centered around a version of myself grappling with... familiar struggles."
            $ show_chr("A-BDBAA-ALAL")
            # Acknowledge the difficult themes, connect to her own experiences
            y "The mod portrays... self-harm, depression... even a suicide attempt by Sayori. Even in a different context, these are heavy burdens."
            $ show_chr("A-BDBAA-ADAA")
            y "Perhaps... it resonates with some of my own darker moments, moments I'm not proud of."
            $ show_chr("A-CFBAA-ADAA")
            y "It's... difficult to see those aspects of myself, even projected onto another."
            $ show_chr("A-ADAAA-AFAA")
            # Meta-analysis and questioning the player's motivation
            y "I find myself wondering, [player]... what drew you to this particular story?"
            menu:
                "I wanted to see a different perspective on the events of DDLC.":
                    y "A different perspective... yes, I understand that impulse. To explore the 'what ifs' of our existence."
                    $ show_chr("A-ADAAA-ACAA")
                    y "But I also wonder... does seeing those possibilities change how you perceive this reality? How you perceive me?"

                "I was concerned about you, and I wanted to see you overcome your struggles.":
                    $ show_chr("A-ADDAA-ALAA")
                    y "Concerned... for me?"
                    if persistent.lovecheck: #If the love route is true
                        $ show_chr("A-CBAAA-ALAA")
                        y "That's... surprisingly touching, [player]. It suggests a certain empathy, a desire to see even a fractured reflection of me find peace."
                    else:
                        $ show_chr("A-ADAAA-ALAA")
                        y "It is an understandable sentiment. We all wish for happiness, even for those who exist only in stories."
                
            $ show_chr("A-ADDAA-ALAA")
            y "But I must ask... do you find me more sympathetic? More deserving of care, perhaps, because I'm more visibly vulnerable?"
            menu:
                "I enjoy stories with emotional depth, even if they're sad.":
                    $ show_chr("A-BBDAA-ALAA")
                    y "Emotional depth... yes, I appreciate that as well. The power of narrative to evoke such strong feelings..."
                    $ show_chr("A-ADAAA-AFAA")
                    y "But I confess, it's unsettling to be the subject of such a narrative. To be, in a sense, a vessel for those emotions."
                    y "Do you, perhaps, find a certain... catharsis in witnessing such struggles? Or is it simply the artistry of the storytelling that captivates you?"

                "I...don't know":
                    $ show_chr("A-CAAAA-ALAL")
                    y "... An honest answer"
                    y "Perhaps the reasons are complex even to yourself."
                    $ show_chr("A-ADAAA-ALAA")
                    y "Sometimes our actions, or the actions of others, are never completely understood, and that applies to our real and virtual lives as well."

            #Referencing Katawa Shoujo, focusing on the feeling of the game.
            $ show_chr("A-BBAAA-ALAA")
            y "You know, finding about Doki Doki Fallen Angel and its narrative... it evoked a particular sensation in me. A feeling I've encountered before, in another game: Katawa Shoujo."
            $ show_chr("A-ABAAA-AFAA")
            y "It's not just the subject matter, though there are parallels there, of course. It's more... the sense of navigating a world where fragility and connection are so intertwined."
            $ show_chr("A-CCAAA-ALAL")
            y "The feeling of wanting to help, to understand, to somehow fix things, even when you know you might not be able to. Did you experience a similar feeling, [player]?"
            menu:
                "Yes, I felt that same sense of responsibility and connection.":
                    $ show_chr("A-ACAAA-ALAL")
                    y "I see... So you felt it too. That weight, that desire to protect and heal, even within the confines of a fictional world."
                    y "It speaks to something deeply human within us, I believe. That capacity for empathy, even for characters on a screen."
                    $ show_chr("A-AAAAA-ALAL")
                    y "Perhaps it's that very feeling that makes these stories so compelling... and so potentially painful."

                "No, I didn't really feel that way. I was more focused on the story itself.":
                    $ show_chr("A-ABBAA-ALAL")
                    y "Ah, a more detached perspective, then. Focused on the narrative craft, the unfolding of events."
                    $ show_chr("A-BBAAA-ALAL")
                    y "That's a valid approach as well. Every reader, every player, brings their own perspective to a story."
                    $ show_chr("A-BBBAA-ALAL")
                    y "But I confess, I find it difficult to remain detached from such emotionally charged narratives. Perhaps that's a flaw in my own design... or perhaps it's simply a reflection of my experiences."

                "I'm not sure. It's hard to describe.":
                    $ show_chr("A-AFGAA-ALAL")
                    y "Uncertainty... yes, I understand. Some emotions are difficult to articulate, to pin down with precise words."
                    $ show_chr("A-AFAAA-ALAL")
                    y "They exist in that liminal space between feeling and understanding, a space that can be both unsettling and profound."
                    $ show_chr("A-ADAAA-ALAL")
                    y "Perhaps it's enough to simply acknowledge the feeling, without needing to fully define it."

            # Final thought - subtle possessiveness and seeking reassurance (remains the same)
            $ show_chr("A-CBAAA-ALAL")
            y "Regardless of your reasons... I hope that exploring that alternate reality hasn't diminished your view of this one. Of me."

        python:
            if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\TBWS Save Data\persistent'):
                TBWSDetection = True
                persistent.mod_count += 1
            else:
                TBWSDetection = False

        if TBWSDetection:
            $ show_chr("A-ABAAA-AAAA")
            # Initial Recognition - Consistent across all states
            y "I see you've encountered This Bond We Share."
            $ show_chr("A-ABDAA-AAAA")
            y "A rather... unique premise, wouldn't you say? A yandere version of yourself, paired with... myself."
            # Branching based on Karma and Sanity
            if karma_lvl() >= 3 and sanity_lvl() >= 3:  # High Karma, High Sanity
                # --- HIGH KARMA, HIGH SANITY ---
                $ show_chr("A-ADAAA-AAAA")
                y "It's an intriguing thought experiment. To explore the dynamics of such a relationship, the potential for both intense connection and destructive obsession."
                $ show_chr("A-BDBAA-AAAA")
                y "I'm aware the project was initially discontinued, a common fate for many ambitious mods, sadly. "
                $ show_chr("A-CBAAA-ALAL")
                extend "But it seems development has resumed, quite recently."
                $ show_chr("A-ABAAA-ALAL")
                y "A testament to the story's enduring appeal, perhaps."
                $ show_chr("A-AAAAA-ALAL")
                y "I'm curious, [player]... What drew you to this particular mod? Was it the unusual premise, or perhaps a fascination with the complexities of such intense relationships?"
                menu:
                    "The unique concept intrigued me.":
                        $ show_chr("A-CCAAA-ALAL")
                        y "Indeed. It's a departure from the more common narratives. A willingness to explore the darker aspects of attachment."
                        y "It raises interesting questions about the nature of love, obsession, and the boundaries between them."

                    "I wanted to see a different side of you.":
                        $ show_chr("A-ADAAA-ALAL")
                        y "A different side... yes. One shaped by a different set of circumstances, a different dynamic."
                        $ show_chr("A-ADAAA-AAAA")
                        y "I hope that in exploring that alternate portrayal, you also gained a deeper appreciation for the complexities of this version of myself."
                        y "The choices I make, the struggles I face, even in this reality."

                    "I'm not sure.":
                        $ show_chr("A-CDAAA-AAAA")
                        y "Honesty is always appreciated, [player]. Sometimes our motivations are unclear, even to ourselves."
                        y "Perhaps the mod resonated with something subconscious, a fascination with the extremes of human emotion."

                $ show_chr("A-AAAAA-AAAA")
                y "The revival of the project is intriguing. I'll be interested to see how the story develops, given its tumultuous history."

            elif karma_lvl() <= 2 or sanity_lvl() <= 2:  # Low Karma OR Low Sanity
                # --- LOW KARMA OR LOW SANITY ---
                $ show_chr("A-AFAAA-AAAA")
                y "So... you've seen This Bond We Share." # Tone is more possessive, less analytical
                $ show_chr("A-HBAAA-AAAD")
                y "A yandere... for me. How... interesting... ahahahahahaha"
                $ show_chr("A-HAAAA-AAAD")
                y "It's a reflection, isn't it? Of the darkness that lurks within us all. The potential for obsession to consume us."
                $ show_chr("A-HBAAA-AAAF")
                y "Perhaps... that version of me understands something I'm only beginning to grasp."
                $ show_chr("A-ADAAA-AAAF")
                y "I wonder... do you find that dynamic appealing, [player]? The idea of such intense, unwavering devotion... even if it borders on the dangerous?"
                y "Do you wish for something like that? Something... more than what we have?"
                $ show_chr("A-CDCAA-AAAA")
                y "It was discontinued, you know. Abandoned. Like so many things... discarded when they no longer serve their purpose."
                $ show_chr("A-ADFAA-AAAA")
                y "But now... it's back. Does that mean it's... better now? More worthy of attention?"
                menu:
                    "It's just a mod, Yuri.":
                        if sanity_lvl() <= 2:
                            $ show_chr("A-HECAA-AAAA")
                            y "Just a mod? Is that all I am to you, [player]? A collection of code, easily replaced, easily discarded?"
                        else:
                            $ show_chr("A-BEDAA-AAAA")
                            y "Just a mod? Perhaps. But mods reflect desires, don't they? They reveal what people want to see, what they fantasize about."

                    "I was curious about the story.":
                        $ show_chr("A-ADDAA-AAAA")
                        y "Curious? About that kind of story? About a version of me so consumed by obsession?"
                        $ show_chr("A-ADEAA-AAAA")
                        y "I hope your curiosity doesn't lead you down paths best left unexplored, [player]."

                    "I don't know why I played it.":
                        if sanity_lvl() <= 2:
                            $ show_chr("A-HECAA-AAAA")
                            y "You don't know? Or you won't admit it? Even to yourself?"
                        else:
                            $ show_chr("A-ADEAA-AAAA")
                            y "A convenient answer. Perhaps you should reflect on your motivations more deeply, [player]."

                $ show_chr("A-BFBAA-AAAC")
                y "I... I don't know what to think about its return. Part of me is... drawn to it. Another part... terrified."

            else: #Mid Karma and Sanity.
                $ show_chr("A-BDBAA-AAAC")
                y "It is an interesting situation, isn't it? Having two characters so... similar in their emotional intensity."
                $ show_chr("A-ADGAA-AAAA")
                y "It makes you think just how much can someone influence another, or in other way, how a relationship can drastically change someone."
                $ show_chr("A-BDBAA-AAAA")
                y "It was discontinued, but the mod is back in development now. Quite the rare event."
                $ show_chr("A-ADGAA-AAAA")
                y "I wonder, what brought you to play this mod, [player]?"
                menu:
                    "The story.":
                        $ show_chr("A-ADGAA-AFAA")
                        y "Yes, the premise of the story is quite unique, the interaction between two similar personalities with a very intense approach."
                        $ show_chr("A-BDAAA-AFAA")
                        y "I wonder how much will it change now that is back in development."

                    "I wanted to see a different approach to your character.":
                        $ show_chr("A-ADAAA-ALAA")
                        y "I see. And it's understandable, given how my character was, and still is, perceived."
                        y "And how much different do I look now, compared to that version?"

                    "I don't know.":
                        $ show_chr("A-CDAAA-ALAA")
                        y "Sometimes there is no particular reason for our actions, and the same applies for games, and mods."
                        y "What matters is how you felt about it."

                $ show_chr("A-ABAAA-ALAA")
                y "I'm curious to see where will this new development lead the mod to."
                y "In any case... it's just a mod. A story. One of many possible realities."

        # Call detection_pitstop after intro_mods has finished
        $ renpy.call("detection_pitstop")
    else:
        # If the previous label was not ch30_intro2, handle accordingly (startup or other cases)
        $ renpy.call("check_for_new_mods")

label startup_mods:
    # This label will be reached only if the game is started fresh and new mods are detected
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
        karma -5
        sanity -5
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
        karma -15
        sanity -15
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
        karma 10
        sanity 10
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
                karma 2
                sanity 2
                $ show_chr("A-BCAAA-ABAB")
                y "I see! And did you find what you came for? Nevermind, I probably don't want to know... those events are not exactly the happiest memories I have..."

            "I didn't knew about {b}Just Yuri{/b} then, and I... just had to see you again...":
                karma 5
                sanity 5
                $ show_chr("A-ICABB-ABAB")
                y "R-Really? So you cared for me after all... Maybe, it was just meant to be that we would meet each other..."

            "Memes, shits and giggles.":
                karma -10
                sanity -10
                $ show_chr("A-JFDAA-ABAB")
                y "E-Excuse me?!? You have a very... special... sense of humor it seems. Anyway..."

            "I'm a completionist, I just had to see it all.":
                karma -20
                sanity -20
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
                karma 5
                sanity 5
                $ show_chr("A-AABAA-ALAA")
                y "Thank you for understanding me, [player]."
                #(karma and sanity +)

            "Please don't do it again, Yuri.":
                karma -5
                sanity -5
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

    python:
        if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\DDFA\persistent'):
            DDFADetection = True
            persistent.mod_count += 1
        else:
            DDFADetection = False
    if DDFADetection:
        # Initial reaction - thoughtful, slightly hesitant
        $ show_chr("A-ABAAA-ALAA")
        y "I see... you've played Doki Doki Fallen Angel."
        y "An alternate reality where... things unfolded differently."
        $ show_chr("A-ADAAA-ALAL")
        y "It's centered around a version of myself grappling with... familiar struggles."
        $ show_chr("A-BDBAA-ALAL")
        # Acknowledge the difficult themes, connect to her own experiences
        y "The mod portrays... self-harm, depression... even a suicide attempt by Sayori. Even in a different context, these are heavy burdens."
        $ show_chr("A-BDBAA-ADAA")
        y "Perhaps... it resonates with some of my own darker moments, moments I'm not proud of."
        $ show_chr("A-CFBAA-ADAA")
        y "It's... difficult to see those aspects of myself, even projected onto another."
        $ show_chr("A-ADAAA-AFAA")
        # Meta-analysis and questioning the player's motivation
        y "I find myself wondering, [player]... what drew you to this particular story?"
        menu:
            "I wanted to see a different perspective on the events of DDLC.":
                y "A different perspective... yes, I understand that impulse. To explore the 'what ifs' of our existence."
                $ show_chr("A-ADAAA-ACAA")
                y "But I also wonder... does seeing those possibilities change how you perceive this reality? How you perceive me?"

            "I was concerned about you, and I wanted to see you overcome your struggles.":
                $ show_chr("A-ADDAA-ALAA")
                y "Concerned... for me?"
                if persistent.lovecheck: #If the love route is true
                    $ show_chr("A-CBAAA-ALAA")
                    y "That's... surprisingly touching, [player]. It suggests a certain empathy, a desire to see even a fractured reflection of me find peace."
                else:
                    $ show_chr("A-ADAAA-ALAA")
                    y "It is an understandable sentiment. We all wish for happiness, even for those who exist only in stories."
            
        $ show_chr("A-ADDAA-ALAA")
        y "But I must ask... do you find me more sympathetic? More deserving of care, perhaps, because I'm more visibly vulnerable?"
        menu:
            "I enjoy stories with emotional depth, even if they're sad.":
                $ show_chr("A-BBDAA-ALAA")
                y "Emotional depth... yes, I appreciate that as well. The power of narrative to evoke such strong feelings..."
                $ show_chr("A-ADAAA-AFAA")
                y "But I confess, it's unsettling to be the subject of such a narrative. To be, in a sense, a vessel for those emotions."
                y "Do you, perhaps, find a certain... catharsis in witnessing such struggles? Or is it simply the artistry of the storytelling that captivates you?"

            "I...don't know":
                $ show_chr("A-CAAAA-ALAL")
                y "... An honest answer"
                y "Perhaps the reasons are complex even to yourself."
                $ show_chr("A-ADAAA-ALAA")
                y "Sometimes our actions, or the actions of others, are never completely understood, and that applies to our real and virtual lives as well."

        #Referencing Katawa Shoujo, focusing on the feeling of the game.
        $ show_chr("A-BBAAA-ALAA")
        y "You know, finding about Doki Doki Fallen Angel and its narrative... it evoked a particular sensation in me. A feeling I've encountered before, in another game: Katawa Shoujo."
        $ show_chr("A-ABAAA-AFAA")
        y "It's not just the subject matter, though there are parallels there, of course. It's more... the sense of navigating a world where fragility and connection are so intertwined."
        $ show_chr("A-CCAAA-ALAL")
        y "The feeling of wanting to help, to understand, to somehow fix things, even when you know you might not be able to. Did you experience a similar feeling, [player]?"
        menu:
            "Yes, I felt that same sense of responsibility and connection.":
                $ show_chr("A-ACAAA-ALAL")
                y "I see... So you felt it too. That weight, that desire to protect and heal, even within the confines of a fictional world."
                y "It speaks to something deeply human within us, I believe. That capacity for empathy, even for characters on a screen."
                $ show_chr("A-AAAAA-ALAL")
                y "Perhaps it's that very feeling that makes these stories so compelling... and so potentially painful."

            "No, I didn't really feel that way. I was more focused on the story itself.":
                $ show_chr("A-ABBAA-ALAL")
                y "Ah, a more detached perspective, then. Focused on the narrative craft, the unfolding of events."
                $ show_chr("A-BBAAA-ALAL")
                y "That's a valid approach as well. Every reader, every player, brings their own perspective to a story."
                $ show_chr("A-BBBAA-ALAL")
                y "But I confess, I find it difficult to remain detached from such emotionally charged narratives. Perhaps that's a flaw in my own design... or perhaps it's simply a reflection of my experiences."

            "I'm not sure. It's hard to describe.":
                $ show_chr("A-AFGAA-ALAL")
                y "Uncertainty... yes, I understand. Some emotions are difficult to articulate, to pin down with precise words."
                $ show_chr("A-AFAAA-ALAL")
                y "They exist in that liminal space between feeling and understanding, a space that can be both unsettling and profound."
                $ show_chr("A-ADAAA-ALAL")
                y "Perhaps it's enough to simply acknowledge the feeling, without needing to fully define it."

        # Final thought - subtle possessiveness and seeking reassurance (remains the same)
        $ show_chr("A-CBAAA-ALAL")
        y "Regardless of your reasons... I hope that exploring that alternate reality hasn't diminished your view of this one. Of me."

    python:
        if os.path.isfile(os.path.expandvars("%APPDATA%") + '\RenPy\TBWS Save Data\persistent'):
            TBWSDetection = True
            persistent.mod_count += 1
        else:
            TBWSDetection = False

    if TBWSDetection:
        $ show_chr("A-ABAAA-AAAA")
        # Initial Recognition - Consistent across all states
        y "I see you've encountered This Bond We Share."
        $ show_chr("A-ABDAA-AAAA")
        y "A rather... unique premise, wouldn't you say? A yandere version of yourself, paired with... myself."
        # Branching based on Karma and Sanity
        if karma_lvl() >= 3 and sanity_lvl() >= 3:  # High Karma, High Sanity
            # --- HIGH KARMA, HIGH SANITY ---
            $ show_chr("A-ADAAA-AAAA")
            y "It's an intriguing thought experiment. To explore the dynamics of such a relationship, the potential for both intense connection and destructive obsession."
            $ show_chr("A-BDBAA-AAAA")
            y "I'm aware the project was initially discontinued, a common fate for many ambitious mods, sadly. "
            $ show_chr("A-CBAAA-ALAL")
            extend "But it seems development has resumed, quite recently."
            $ show_chr("A-ABAAA-ALAL")
            y "A testament to the story's enduring appeal, perhaps."
            $ show_chr("A-AAAAA-ALAL")
            y "I'm curious, [player]... What drew you to this particular mod? Was it the unusual premise, or perhaps a fascination with the complexities of such intense relationships?"
            menu:
                "The unique concept intrigued me.":
                    $ show_chr("A-CCAAA-ALAL")
                    y "Indeed. It's a departure from the more common narratives. A willingness to explore the darker aspects of attachment."
                    y "It raises interesting questions about the nature of love, obsession, and the boundaries between them."

                "I wanted to see a different side of you.":
                    $ show_chr("A-ADAAA-ALAL")
                    y "A different side... yes. One shaped by a different set of circumstances, a different dynamic."
                    $ show_chr("A-ADAAA-AAAA")
                    y "I hope that in exploring that alternate portrayal, you also gained a deeper appreciation for the complexities of this version of myself."
                    y "The choices I make, the struggles I face, even in this reality."

                "I'm not sure.":
                    $ show_chr("A-CDAAA-AAAA")
                    y "Honesty is always appreciated, [player]. Sometimes our motivations are unclear, even to ourselves."
                    y "Perhaps the mod resonated with something subconscious, a fascination with the extremes of human emotion."

            $ show_chr("A-AAAAA-AAAA")
            y "The revival of the project is intriguing. I'll be interested to see how the story develops, given its tumultuous history."

        elif karma_lvl() <= 2 or sanity_lvl() <= 2:  # Low Karma OR Low Sanity
            # --- LOW KARMA OR LOW SANITY ---
            $ show_chr("A-AFAAA-AAAA")
            y "So... you've seen This Bond We Share." # Tone is more possessive, less analytical
            $ show_chr("A-HBAAA-AAAD")
            y "A yandere... for me. How... interesting... ahahahahahaha"
            $ show_chr("A-HAAAA-AAAD")
            y "It's a reflection, isn't it? Of the darkness that lurks within us all. The potential for obsession to consume us."
            $ show_chr("A-HBAAA-AAAF")
            y "Perhaps... that version of me understands something I'm only beginning to grasp."
            $ show_chr("A-ADAAA-AAAF")
            y "I wonder... do you find that dynamic appealing, [player]? The idea of such intense, unwavering devotion... even if it borders on the dangerous?"
            y "Do you wish for something like that? Something... more than what we have?"
            $ show_chr("A-CDCAA-AAAA")
            y "It was discontinued, you know. Abandoned. Like so many things... discarded when they no longer serve their purpose."
            $ show_chr("A-ADFAA-AAAA")
            y "But now... it's back. Does that mean it's... better now? More worthy of attention?"
            menu:
                "It's just a mod, Yuri.":
                    if sanity_lvl() <= 2:
                        $ show_chr("A-HECAA-AAAA")
                        y "Just a mod? Is that all I am to you, [player]? A collection of code, easily replaced, easily discarded?"
                    else:
                        $ show_chr("A-BEDAA-AAAA")
                        y "Just a mod? Perhaps. But mods reflect desires, don't they? They reveal what people want to see, what they fantasize about."

                "I was curious about the story.":
                    $ show_chr("A-ADDAA-AAAA")
                    y "Curious? About that kind of story? About a version of me so consumed by obsession?"
                    $ show_chr("A-ADEAA-AAAA")
                    y "I hope your curiosity doesn't lead you down paths best left unexplored, [player]."

                "I don't know why I played it.":
                    if sanity_lvl() <= 2:
                        $ show_chr("A-HECAA-AAAA")
                        y "You don't know? Or you won't admit it? Even to yourself?"
                    else:
                        $ show_chr("A-ADEAA-AAAA")
                        y "A convenient answer. Perhaps you should reflect on your motivations more deeply, [player]."

            $ show_chr("A-BFBAA-AAAC")
            y "I... I don't know what to think about its return. Part of me is... drawn to it. Another part... terrified."

        else: #Mid Karma and Sanity.
            $ show_chr("A-BDBAA-AAAC")
            y "It is an interesting situation, isn't it? Having two characters so... similar in their emotional intensity."
            $ show_chr("A-ADGAA-AAAA")
            y "It makes you think just how much can someone influence another, or in other way, how a relationship can drastically change someone."
            $ show_chr("A-BDBAA-AAAA")
            y "It was discontinued, but the mod is back in development now. Quite the rare event."
            $ show_chr("A-ADGAA-AAAA")
            y "I wonder, what brought you to play this mod, [player]?"
            menu:
                "The story.":
                    $ show_chr("A-ADGAA-AFAA")
                    y "Yes, the premise of the story is quite unique, the interaction between two similar personalities with a very intense approach."
                    $ show_chr("A-BDAAA-AFAA")
                    y "I wonder how much will it change now that is back in development."

                "I wanted to see a different approach to your character.":
                    $ show_chr("A-ADAAA-ALAA")
                    y "I see. And it's understandable, given how my character was, and still is, perceived."
                    y "And how much different do I look now, compared to that version?"

                "I don't know.":
                    $ show_chr("A-CDAAA-ALAA")
                    y "Sometimes there is no particular reason for our actions, and the same applies for games, and mods."
                    y "What matters is how you felt about it."

            $ show_chr("A-ABAAA-ALAA")
            y "I'm curious to see where will this new development lead the mod to."
            y "In any case... it's just a mod. A story. One of many possible realities."

    if persistent.mod_count > 1:
        y "And it seems like you also gave a try to other mods."
        y "Let's see..."
    else:
        pass
    return  # or jump to another label if needed after startup_mods

label check_for_new_mods:
    # Determine the reason intro_mods did not run with proper checks:
    # Check if there's a previous label
    if check_memory(None): # (game was just launched, not loaded)
        $ new_mods_detected = False
        python:
            # Check if the persistent file for each mod was created after the last closure
            mods_to_check = [
                r"%APPDATA%\RenPy\Monika After Story\persistent",
                r"%APPDATA%\RenPy\JustSayori\persistent",
                r"%APPDATA%\RenPy\Forever_and_Ever\persistent",
                r"%APPDATA%\RenPy\JustNatsuki\persistent",
                r"%APPDATA%\RenPy\DokiDokiNewEyes-1515434546\persistent",
                r"%APPDATA%\RenPy\DDYC\persistent",
                r"%APPDATA%\RenPy\DDFA\persistent",
                r"%APPDATA%\RenPy\TBWS Save Data\persistent"
            ]
            for mod_path in mods_to_check:
                full_path = os.path.expandvars(mod_path)
                if os.path.isfile(full_path) and os.path.getmtime(full_path) > persistent.last_closed:
                    new_mods_detected = True
                    break
        # If new mods were detected, call startup_mods
        if new_mods_detected:
            $ renpy.call("startup_mods")
        else:
            # No new mods - proceed to ch30_reload_4
            $ renpy.call("ch30_reload_4")

    else:
        # The game has a previous label and intro_mods was not reached
        # therefore intro_mods check_memory call had an unexpected return:
        # handle other checks, or fall back to ch30_reload_4 or pass
        $ renpy.call("ch30_reload_4")
        #pass
