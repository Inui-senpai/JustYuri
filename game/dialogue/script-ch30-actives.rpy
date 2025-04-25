#############
#ACTIVE TEXT#
#############

label a1:
    python:
        import random
        howAreYouVariant = random.randint(1, 5)
        howAreYouVariant2 = random.randint(1, 2)

    if karma_lvl() == 3:
        if sanity_lvl() == 3:
            $ show_chr("A-BCAAA-AAAA") #former code was Ab-A1b
            y "Oh... I'm feeling the same as I was earlier. I hope that means to you that I'm feeling good."
        else:
            $ show_chr("A-AFAAA-AAAA") #former code Ab-A0e
            y "I... really don't know how I feel right now."
            $ show_chr("A-ACBAA-AAAA") #former code Ac-A0b
            y "It feels... nice, I guess?"
            $ show_chr("A-ABBAA-AAAA") #former code Ac-A0a
            y "Sorry for my ambiguous language."
            y "I guess I'm still getting accustomed to this new environment is all."
        return

    elif sanity_lvl() >= 3:
        if karma_lvl() < 3:
            $show_chr("A-BEBAA-AAAA") #former code was Ac-A1d
            y "Oh... I-I'm feeling alright, but I doubt you really care at all, do you?"

        elif karma_lvl() > 3:
            if howAreYouVariant == 1:
                $ show_chr("A-BCABA-AAAA") #former code was Ab-B1b
                y "Oh... I'm feeling good. I hope I can feel like this every day, my love..."
                # OR
                #y "I was feeling good before, but I'm even better now that you're here."
            elif howAreYouVariant == 2:
                $ show_chr("A-ACAAA-AAAB")
                y "A bit thirsty actually..."
                if persistent.lovecheck:
                    y "Would you like to have some tea with me?"
                    menu:
                        "Sure!":
                            python:
                                import random
                                if check_memory('a26-1') and check_memory('a26-2'):
                                    outcome = random.randint(1, 3)
                                else:
                                    outcome = random.randint(1, 2)
                            if outcome == 1:
                                jump teadate1
                            if outcome == 2:
                                jump teadate2
                            if outcome == 3:
                                jump teadate3
                            return
                        "I would, but I don't have any here. But please feel free to get some tea yourself.":
                            $ show_chr("A-GBAAA-AAAD")
                            y "Later, then. I want the tea drinking to be something special, just between the two of us."
                            $ show_chr("A-CAAA-AAAE")
                            show black zorder 100 with Dissolve(2.0)
                            y "I should have a bottle of water here somewhere. Give me a brief second please."
                            hide black zorder 100 with Dissolve(2.0)
                            y "Much better now! So, where did we leave off?"
                        "Barely listening for a minute, already bored.":
                            karma -1
                            $ show_chr("A-AEAAA-AAAJ")
                            y "Oh, you're in a bad mood... I guess?"
                            y "S- Sorry for bringing that up, shall we do something else then?"
                else:
                    $ show_chr("A-CAAA-AAAE")
                    show black zorder 100 with Dissolve(2.0)
                    y "Would you excuse me for a second please, I should have some water here..."
                    hide black zorder 100 with Dissolve(1.0)
                    y "Much better now! So, where did we leave off?"
                return

            elif howAreYouVariant == 3:
                $ show_chr("A-IEBAA-AAAA")
                y "..."
                $ show_chr("A-IEBBB-AAAA")
                y "..."
                y "Just... just hold me, please..."
                menu:
                    "Shh... come here.":
                        hide yuri_sit
                        show yuri_prehug zorder 20
                        pause 3.0
                        hide yuri_prehug zorder 20
                        show yuri_hug zorder 20
                        play sound "<to 0.3>sfx/fall.ogg"
                        y "I... don't even know why I'm sad... just please, hold me for a bit..."
                        y "..."
                        pause 1.0
                        show black zorder 100 with Dissolve(2.0)
                        $ show_chr("A-JCBBB-AAAA")
                        hide yuri_hug
                        hide black zorder 100 with Dissolve(2.0)
                        $ show_chr("A-JCBBB-AAAA")
                        y "Thank you... you already made me feel a little better."
                        if persistent.lovecheck:
                            y "I... I love you, [player]."
                            menu:
                                "I love you too, [persistent.yuri_nickname].":
                                    karma 1
                                    return
                                "...":
                                    karma -1
                                    return
                        elif not persistent.lovecheck:
                            y "... you're truly the greatest friend I could ask for, [player]."
                            menu:
                                "I'm here for you, [persistent.yuri_nickname].":
                                    karma 1
                                    return

                                "...":
                                    karma -1
                                    return
                    "...":
                        $ show_chr("A-CEBBB-AAAA")
                        karma -1
                        y "..."
                        return

            elif howAreYouVariant == 4:
                $ show_chr("A-AFBAA-AAAA")
                y "I... find it hard to focus today... don't really know why."
                y "Sorry for asking this but... would you be fine if we take it easy today?"
                y "I don't think that I can handle something intense like philosophical topics at the moment..."
                menu:
                    "Sure, let's take it easy today":
                        $ show_chr("A-CAAA-AAAA")
                        # Blocks postmodernism and philosophy idles for this session
                        $philosophy = False
                        y "Thank you for being so understanding, [player]"
                        y "I'll try to be in better shape next time, I promise."

                    "Oh, I was actually looking forward to discussing those kinds of topics, [persistent.yuri_nickname]..":
                        $philosophy = True
                        $ show_chr("A-CDBAA-AAAA")
                        y "If that's the case... I suppose we could still give it a try."
                        $ show_chr("A-AFBAA-AAAA")
                        y "But please don't be mad if I don't perform too well..."

                return


            elif howAreYouVariant == 5:
                $ show_chr("A-ACAAA-AAAA")
                y "I felt a bit lonely before you came online today..."
                $ show_chr("A-ACABA-AAAA")
                y "But now you are here, I feel much better now already!"
                y "You know... when you're here with me, everything just feels so much... lighter.."
                y "As if all the weight and all the worries have been magically lifted from my shoulders."
                $ show_chr("A-CCABA-AAAA")
                y "Thank you... y- your very existence is like a shining beacon for my soul."
                if persistent.lovecheck:
                    y "I love you... [player]"
                elif not persistent.lovecheck:
                    y "You're truly the most reliable friend I could ever lean on... [player]"
                    y "I- I'll try my best to always be here if you need me in return..."

                return
        return

    elif sanity_lvl() < 3:
        if karma_lvl() >= 3:
            $ show_chr("A-BBGBA-AAAA") #former code was Ab-B1a
            y "I can't wait until I finally slam you against the wall and..."
            $ show_chr("A-DFGBA-AAAA") #former code Ab-B3e
            y "..."
            $ show_chr("A-BBGAA-AAAA")
            y "... N-never mind."

            if howAreYouVariant2 == 1:
                $ show_chr("A-DCGAA-AAAA")
                y "Y-You noticed me! You noticed me!!!"
                y "H-How exciting..! Yes, yes..!"
                y "I feel good, yes. V- Very good!! Do you feel good, too?"
                if persistent.lovecheck:
                    $ show_chr("A-DCGAA-AAAA")
                    y "I've never felt so good in my life!"
                    y "You and I, together... i-it is just perfect!"
                    y "W-Would you mind if I... stare... a-at your... gorgeous face for a while..?"
                    $ renpy.music.set_pause(True)
                    y "{cps=0.25} . . . . . . {/cps}"
                    $ renpy.music.play(current_music, "music", True)
                y "Ah..."
                $ show_chr("A-DBGAA-AAAA")
                y "Ahahaha!"
                $ show_chr("A-DCGAA-AAAA")
                y "Wh-what was your question again?"

            elif howAreYouVariant2 == 2:
                $ show_chr("A-JCAAA-AAAA")
                y "{cps=3}Oh, thanks for asking! Today I feel very{/cps}{nw}"
                python:
                    for x in range(random.randint(3,6)):
                        glitchtext(random.randint(100, 200))
                $ show_chr("A-GCAAA-AAAD")
                y "I hope you feel the same way?"
                menu:
                    "Yes! Sure!":
                        return
                    #"Wh-What did you say?":
                        # to be completeed later - need to make a screen so the button vanishes when hovered. Currently screwing around with it's creation.




        elif karma_lvl() < 3:
            $ show_chr("A-DDCBA-AAAA") #former code Ad-B3d
            y "You're asking how I feel?"
            $ show_chr("A-DECBA-AAAA") #former code Ad-BCd
            y "Isn't it obvious how I should feel by now?!"
    return

label a2:#flag active skip overwritten
    $ show_chr("A-AAGAA-AAAA")
    $ show_chr("A-BBGBA-AAAA")
    y "Oh. Y-You really think so? Well, thank you! I-I think you, always look nice... [player]."
    if persistent.head1 == "cat_ears":
        $ show_chr("A-BEBBA-AMAM")
        y "I'm a little embarrassed though about these ears you gave me..."
        $ show_chr("A-BDBBA-AMAM")
        menu:
            y "Would it be fine if I took these off?"
            "But they look nice on you!":
                $ show_chr("A-CFBBA-AAAA")
                y "W-well alright..."
                y "Anything for you..."
            "If you really want, sure.":
                $ show_chr("A-ABBBA-AAAA")
                y "Thank you, [player]."
                $persistent.head1 = "nothing"
                karma 5
                y "I'm sorry it's just... a little too embarrassing is all."
                y "Let's just talk about s-something else for now."
    return

label a3: #"How do you feel about our relationship so far?"
    $ show_chr("A-AAGAA-AAAA")
    if sanity_lvl() <= 3 and karma_lvl() >= 3:
        if persistent.lovecheck:
            $ show_chr("A-DBGBA-AAAL")
            y "I want to do everything with you. I want to show you how much I love you..."
            $ show_chr("A-DCGBA-AAAL")
            return
        else:
            $show_chr("A-GAAAA-ALAL")
            y "You are the best friend I've ever had!"
            $show_chr("A-ICAAA-ALAL")
            y "I've never been great at expressing this but... don't even think that I don't value you!"
            y "You are one of the very few people in my life who accepted me despite my intense tendencies."
            y "...and that means the world to me."
            pause 2.0
            $show_chr("A-HCAAA-ALAL")
            y "Would you mind if I just... stare at you for a while?..."
            $show_chr("A-NAAAA-ALAL")
            y "..."
            y "..."
            y "..."
            y "..."
            y "He..."
            y "Hehe... he..."
            return
    elif sanity_lvl() >= 3 and karma_lvl() > 3:
        $ show_chr("A-ABGBA-AAAL")
        y "I feel like I can trust you, [player], I feel safe around you, like all I'll ever need to be happy is you."
        $ show_chr("A-BCABA-AAAL")
        y "..."
        $ show_chr("A-BBABA-AAAL")
        y "I'm sorry if that was a bit of a corny reply."
        return
    elif sanity_lvl() <= 3 and karma_lvl() < 3:
        $ show_chr("A-DEBAA-AMAM")
        y "S-Stop saying that like you're going to leave me!"
        $ show_chr("A-DDBAB-AMAM")
        y "You're n-not going to abandon me, right?! RIGHT?!"
        $ show_chr("A-AEBAA-AAAL")
        y "P-Please, never leave me... okay?"
        return
    elif sanity_lvl() <= 3 and karma_lvl() <= 3:
        $ show_chr("A-BEBAA-AAAA")
        y "..."
        $ show_chr("A-CEBAA-AAAA")
        y "...I don't want to answer..."
        return
    if not persistent.lovecheck and sanity_lvl() > 3 and karma_lvl() < 3:
        $ show_chr("A-BEBAA-AAAA")
        y "..."
        $ show_chr("A-CEBAA-AAAA")
        y "...I don't want to answer..."
        return
    else:
        $ show_chr("A-BCGAA-AAAA")
        y "I'm happy about it, [player], it just feels a bit weird, is all."
        $ show_chr("A-BDGAA-AMAM")
        y "Maybe it's just the shock of these events so far..."
        y "...becoming somewhat sentient, you know?"
        $ show_chr("A-ABAAA-AMAM")
        y "Don't worry. I'll get used to it eventually."
    return

label a4:
    python:
        call_dialogue()
    return

label a5:
    if persistent.face1 == "nothing":
        jump put_on_glasses
    else:
        y "My eyesight is quite alright, though sometimes I prefer to wear glasses when reading as it helps with mitigating eye strain."
        y "I don't know if there is any science behind why I sometimes wear them in the first place, but the comfort of a good book complements the eyewear."
        $ show_chr("A-BFGAA-AAAL")
        menu:
            y "Since I'm not really reading at the moment, do you want me to take these glasses off?"
            "Yes":
                $persistent.face1 = "nothing"
                y "Let me take these off then."
            "No":
                y "I see. Let's carry on then."
        return

label put_on_glasses:#idle_3 for document: JY active suggestion "How is your eyesight?"
    $ show_chr("A-BFGAA-AAAL")
    y "What an odd question, though I suppose it's never been brought up."
    $ show_chr("A-ACGAA-AAAA")
    y "My vision is fine for the most part, though I suppose things do get a little bit blurry at distance."
    y "That might be due to how much I read, now that I think about it."
    $ show_chr("A-BCGAA-AAAA")
    y "Though, I suppose it really doesn't matter too much, considering I could just change my eyesight parameters..."
    $ show_chr("A-BBGBA-AMAM")
    y "U-um, that being said, why do you ask? ...Did you want to see what I'd look like with glasses?"
    menu:
        "No, it was just a random thought I had.":
            $ show_chr("A-AEBAA-AAAA")
            y "Oh, alright."
            return
        "Sure, why not?":
            jump choose_glasses

label choose_glasses:
    $ show_chr("A-BBGAA-AAAA")
    y "This mod actually has two pairs of glasses for me in its files. It seems that the developers were thinking in a similar place. How thoughtful."
    y "There's a full-rimmed pair, and a half-rimmed pair."
    $ show_chr("A-BFGAA-AAAL")
    y "The full-rimmed pair gives full coverage of the eyes, letting you look up even when your head is pointed downwards."
    y "Also, since the rims cover the entire lens, they're less likely to break. On the other hand..."
    $ show_chr("A-BCGAA-AMAM")
    y "The half-rimmed pair is a bit lighter on the face, and by pushing them forward or back more, you can either have them fill up more or less of your vision, depending on the distance you're trying to see, all without taking them off."
    $ show_chr("A-ACGAA-AAAA")
    y "As far as looks, the half-rimmed pair looks a bit more professional, studious, like a programmer or teacher."
    y "Although... I suppose some might find the full-rimmed glasses to be cuter, giving one the appearance of fuller eyes. At least, that's what's considered cute in Japan."
    $ show_chr("A-CCGAA-AMAM")
    y "Hmm. I just can't choose... Which one would you like to see me in?"
    menu:
        "The half-rimmed ones.":
            $ show_chr("A-ACGAA-AAAL")
            y "Hmm, going for a sharper look..."
            y "Alright, one second."
            $persistent.face1 = "glasses_2"
        "The full-rimmed ones.":
            $ show_chr("A-EBGAA-AAAA")
            y "Ohoho, going for a cuter look..."
            y "Alright, one second."
            $persistent.face1 = "glasses_1"
    y "There! How do I look?"
    menu:
        "Not bad, [persistent.yuri_nickname].":
            $ show_chr("A-CCGBA-AMAM")
            y "Thanks. I'll wear these from now on."
        "On second thought, you actually look much better without them.":
            $ show_chr("A-AEBAA-AAAA")
            y "O-oh... alright. I'll take them back off."
            $persistent.face1 = "nothing"
    $ show_chr("A-ACGAA-AAAA")
    return

label a6:
    karma 1
    if sanity_lvl() <= 2 and karma_lvl() >= 3:
        $ show_chr("A-BFGBA-AAAA")
        y "..."
        $ show_chr("A-BEBAA-AMAM")
        y "..."
        $ show_chr("A-BBBBA-AMAM")
        y "HAAAAAAAAAAAAAAAAAAaaaaaaaaaaaaaaa..."
        $ show_chr("A-DCBBA-AMAM")
        y "..."
        $ show_chr("A-DBBBA-AMAM")
        y "Say it again."
        menu:
            "I love you":
                y "Thank you so much... my love."
                return
    if karma_lvl() == 5:
        $ show_chr("A-ABGBA-AAAK")
        y "I love you too!"
        return
    if karma_lvl() == 4:
        $ show_chr("A-DEGBA-AAAA")
        y "..."
        $ show_chr("A-BBGBA-AAAA")
        y "T-That was sudden."
        $ show_chr("A-BBGBA-AMAM")
        y "I d-don't mind it. It just caught me off guard, that's all!"
        y "But, it does mean a lot to me that you'd say that, [player]. I love you too!"
    elif karma_lvl() == 2:
        $ show_chr("A-BEABA-AAAA")
        y "Do you really mean it?"
    elif karma_lvl() == 1:
        $ show_chr("A-BEABA-AAAA")
        y "..."
        y "Do you really mean that?"
    else:
        $ show_chr("A-CEBBA-AAAA")
        y "..."
        $ show_chr("A-ACBBA-AMAM")
        menu:
            y "D-do you really mean t-that, [player]...?"
            "Yes":
                sanity -1
                karma 1
                $ show_chr("A-CDBBA-AMAM")
                y "I... uh... I..."
                $ show_chr("A-BCGBA-AMAM")
                y "I l-love you too... [player]."
            "No":
                sanity 1
                karma -1
                $ show_chr("A-AEBAA-AAAA")
                y "...W-why even say it, then?"
    return

label a7:
    if sanity_lvl() >= 3:
        $ show_chr("A-ABBBA-AAAA")
        y "Of course I do! Nothing compares to when I'm with you, [player]."
        return
    else:
        $ show_chr("A-DBGAA-AAAA")
        y "OF COURSE! How could I go on without you?"
        $ show_chr("A-DDCAA-AAAA")
        y "And besides! When you're gone, {b}OTHER GIRLS COULD BE LOOKING AT YOU!{/b}"
        y "{b}PLOTTING TO TAKE YOU AWAY FROM ME! HAHAHAHAHA...{/b}"
        $ show_chr("A-DCGAA-AAAA")
        y "It's just easy to think of that when you're here, [player]. Here and all mine..."
    return

label a8:
    $ show_chr("A-CCGBA-AMAM")
    y "It would be nice to just... hold your hand for a bit. Squeeze it tight with a reassuring smile."
    $ show_chr("A-ACBAA-AAAL")
    y "Hugging is... something we can work on, I guess? I'm sorry if I'm not answering very clearly."
    $ show_chr("A-ABGAA-AAAL")
    y "You don't have to think about it too much. Our affection should come naturally after all."
    y "I just don't want to mess this up."
    $ show_chr("A-DCGBA-AAAA")
    y "{b}W-we can work up to the kiss!{/b}"
    $ show_chr("A-BCGBA-AMAM")
    y "It's just... I need a little time, okay? Would that be fine?"
    return

label a9:
    $ show_chr("A-CCGBA-AMAM")
    y "There's no need to be flustered, [player]. It was a delicious piece of candy. If you ever want to give me chocolate again..."
    $ show_chr("A-ACGBA-AMAM")
    y "I like the Hershey brand, if you, I-I mean... ever wanted to buy me chocolate."
    y "That, of course, is not to imply an expectation. You shouldn't feel obligated to buy me chocolate!"
    y "..."
    $ show_chr("A-FCGBA-AAAJ")
    y "Putting that chocolate between my lips was a sweet accident."
    return

label a10:
    $ show_chr("A-ABGAA-AAAA")
    y "It is a fascinating read. Many fans have even theorized that it contains knowledge of... another game I was from?"
    $ show_chr("A-BFBAA-AAAL")
    y "Though technically I am not 'from' a game that exists, since the game has not been made yet. But from a story perspective I may be from another story."
    y "Reading it with you might help me understand myself better."
    y "...if you would like to."
    $ show_chr("A-ACGAA-AAAA")
    y "Well... not now."
    $ show_chr("A-ACGBA-AAAC")
    y "It might spoil what Dan has planned for it, after all."
    $ show_chr("A-ABGAA-AMAM")
    y "I hope you understand why I keep the contents of this book... relatively hidden."
    $ show_chr("A-BCGBA-AMAM")
    y "At least, for now."
    return

label a11:
    $ show_chr("A-HLGAA-AAAA") #former code Ab-A3a
    y "...My favorite? My favorite?! Ahaha~!"
    $ show_chr("A-ACBAA-AAAA") #former code Ac-A0b
    y "Why do you ask such difficult questions, [player]?"
    y "Well, let me think..."
    $ show_chr("A-BEAAA-AAAD") #former code Eb-A1d
    y "Well, to be honest with you... there are so many blades out there that deserve praise due to merit, craftsmanship, and history alone."
    $ show_chr("A-ACGAA-AAAD") #former code Eb-A0b
    y "Though I suppose one historic blade that comes to mind is the iconic Kukri, for example."
    y "This blade was often used by the famous Gurka warriors of Nepal. Often they are praised for their tenacity in close quarters combat with this blade being their favorite."
    $ show_chr("A-IFAAA-AAAD") #former code Eb-A0e
    y "Sure it may not technically be a knife, but it's still a good example of a well-crafted blade that can still be a knife."
    $ show_chr("A-ACGAA-AAAD") #former code Eb-A0b
    y "For instance, the slightly bigger size and curved wide blade make it more practical compared to, say other combat knives.."
    $ show_chr("A-CCAAA-AAAD")
    y "To be precise it's about 16-18 inches in length and I have seen quite a few with many geometric designs that I find simply lovely.."
    y "Then there are these two curved hook-like openings at the front of the blade, ideal for quickly catching and disarming your opponent."
    $ show_chr("A-ABAAA-AAAD")
    y "So with such history and utility associated with it, despite its cliche and crude appearance, how can one turn the Kukri down?"
    $ show_chr("A-ACAAA-ABAE")
    y "This is actually a widespread misconception, the phrase knife doesn't say anything about the size. For example, there is the medieval german Langmesser which is, by definition, a two-handed knife."
    $ show_chr("A-CCAAA-ABAL")
    y "They come in a wide variety of forms. Some of them are even looking like oversized kitchen knives as we know them today. The purpose was quite simple, to take a design the blacksmith of this time already knew, and turn it into an effective weapon."
    y "Many iterations of the Langmesser come with a crossguard the same as you see on most types of swords."
    y "The designs are usually quite simple, highly ornate hilts are rare. Because everyone who could spend a lot of money would just get an actual sword."
    $ show_chr("A-BCAAA-ABAL")
    y "And now that I speak of it, I realize that I definitely need one!"
    $ show_chr("A-JBGAA-AAAD") #former code Eb-A0a
    y "The Bowie knife is another prominent example. Famously used among many adventurers such as James \"Jim\" Bowie and other frontiersmen, it too has its appeal."
    y "With its sleek and hardy blade out front, whittled down to a fine grain, it has the best sharpness for any task. It gives a bold and shiny impression as well."
    y "Not to mention all the other collector's editions of the Bowie Knife that have many engravings to give essence and a story to each.."
    y "And maybe such knives can be an occasional way to add style to other tasks, such as cooking and things. Though I personally would hold back on that."
    y "Oh, I can go on about many various kinds of knives and their appeal but it would take almost an eternity to do so. Still, I do feel a bit elated from this talk.."


    menu:
        y "What do you feel about knives, [player]?"
        "This does seem a bit interesting and I can see the appeal... I might look into it.":
            #(If Karma and Sanity are high or mid-level, and/or lovecheck=true)
            if persistent.lovecheck:
                $ show_chr("A-CBAAA-ABAL")
                y "O-oh thank you... I thought I was rambling too much there.."
                y "It is always lovely to find someone having similar interests especially in things people may find too esoteric to focus on."
                y "Maybe we can discuss the subject further another conversation for another day."
                y "Perhaps compare and discuss each others' collections too in the near future. Hehehe."
            #(If lovecheck = false and/or karma and sanity are low)
            if not persistent.lovecheck:
                $ show_chr("A-AFAAA-ABAB")
                y "O-oh... I am genuinely surprised that you would want to go further on this subject."
                y "A-are you sure you want to? I mean I don't want to force you to..."
                y "You don't have to fake interest or save face for me. Honestly, it is not necessary."
                y "But I suppose it is all up to you in the end. I am just letting you know that and make sure you were serious. Anyway, we can discuss this further at another time. T-thank you."

        "To be honest, I am not too interested in knives as much as a whole. Though I appreciate the effort.":

            #(If lovecheck = true and/or karma and sanity are high/mid-level)
            if persistent.lovecheck:
                $ show_chr("A-BFAAA-ABAB")
                y "I-I see... Well, I do admit I feel slightly taken aback, but that is okay. Maybe we don't have to share all the same interests all the time."
                y "Even if I feel a bit disappointed and hoped for further discussion, we all come into this relationship as individuals. Still trying to navigate things."
                y "Perhaps we can talk of other aspects that are as artistic, like novels or even photographs... yeah."
                y "I am sorry the subject of knives and blades was not to your fancy but again I understand."

            #(lovecheck = false and/or karma and sanity are low)
            if not persistent.lovecheck:
                $ show_chr("A-CFAAA-ABAB")
                y "Oh... sorry about that. I should have known.."
                y "Though I appreciate your niceness there. I am sorry to have irritated you with my rambling."
                y "Let us switch to something else."
            #(no K/S penalty for this one)

        "Let's not talk about knives as much ever again. I just feel too uneasy. Just no." :
            $ show_chr("A-CFAAA-ABAB")
            y "I... You are right... This was most unwise."
            y "What was I thinking!? Of course, that would not be good enough!!"
            y "J-just why..? I wanted to just discuss something nice with you [player]..."
            y "..."
            y "N-nevermind..."
    #(loops back to talk menu from there) (karma - negative penalty and sanity negative penalty)
            $ show_chr("A-ACGAA-AAAA") #former code Ab-A0b
            y "Well, I... I shouldn't say for now... I'll show you later if you want~."
            y "Someday... someday."
    return


label a12: #As soon as the "rebuilding the world" theme is coming, this dialogue shall be replaced entirely
    $ show_chr("A-BEBAA-AAAA") #former code Ac-A1d
    y "..."
    y "..."
    $ show_chr("A-JFBAA-AAAA") #former code Ac-A0e
    y "They are not dead, I promise."
    $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
    y "You understand this is a mod that you got for Just Us."
    y "If I didn't place them in storage, this would be a 'Just Yuri, Natsuki, Sayori, and Monika' mod."
    $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
    y "That might sound appealing to some people but... this is not that mod."
    y "Maybe storage is a bit of a soulless wording..."
    $ show_chr("A-BEBAA-AMAM") #former code Bc-A1d
    y "I would never kill them! I promise they are all f-fine..."
    y "...fine enough."
    $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
    y "...Keep in mind, Monika tortured and murdered all of us twice, if that helps put things into perspective."
    if persistent.lovecheck:
        y "I love you, [player]. Our friends are in capable hands, I promise."
    return



label a13: #b1g 1nt3ll3ct submisson for rewrite
    #Choice Y position of camera depending on which costiume Yuri wear, probably can adjust all other stuff to variables too
    python:
        if persistent.costume == "_chibi":
            yuri_y_zoom = 0.85
            yuri_y_linear = 0.5
        else:
            yuri_y_zoom = 0.15
            yuri_y_linear = 0
    if sanity_lvl() >= 3 and karma_lvl() <= 3 and persistent.lovecheck:  #and Lovecheck true
        $ show_chr("A-BEBBA-AAAA") #former code Ac-B1d
        y "Well... Not right now."
        y "I am just not feeling well... that is all."
        return
    if karma_lvl() >= 4 and persistent.lovecheck:
        $ show_chr("A-DEGBA-AMAM") #former code Bb-B3d
        y "W-What? A kiss?"
        $ show_chr("A-IEBAA-ALAA") #former code c-A0d
        y "..."
        $ show_chr("A-BBBBA-AMAM") #former code Bc-B1a
        y "W-Well, alright... Anything for you, [player]."
        $ show_chr("A-CCBBA-AMAM") #former code Bc-B2b
        #The screen would black out at this point.
        show black zorder 100 with Dissolve(2.0)
        hide yuri_sit
        show layer master:
            zoom 1.5 xalign 0.5 yalign yuri_y_zoom
        show yuri_kiss zorder 20
        hide black zorder 100 with Dissolve(2.0)
        pause 3.0
        y "Mmmph~..."
        pause 1.0
        show black zorder 100 with Dissolve(2.0)
        $ show_chr("A-JCBBA-AAAA")
        hide yuri_kiss
        hide black zorder 100 with Dissolve(2.0)
        show layer master: #flag yalign is being ignored. See why it is being ignored
            zoom 1.5 xalign 0.5 yalign yuri_y_zoom subpixel True
            linear 5 zoom 1.0 xalign 0.5 yalign yuri_y_linear
        pause 5.0
        $ show_chr("A-BEBBA-AAAA") #former code Ac-B1d
        y "S-sorry. I am usually not so sloppy, really!"
        $ show_chr("A-CDBBA-AAAA") #former code Ac-B2c
        if persistent.male:
            y "Wait what am I even implying!? He'll just suspect my kissing practice sessions just from the look on my face--{nw}"
        elif persistent.gender_other:
            y "Wait what am I even implying!? They'll just suspect my kissing practice sessions just from the look on my face--{nw}"
        else:
            y "Wait what am I even implying!? She'll just suspect my kissing practice sessions just from the look on my face--{nw}"
        $ show_chr("A-BEBBA-AAAA") #former code Ac-B1d
        y "..."
        $ show_chr("A-ICGBA-AAAA") #former code Ab-B0b
        y "You are a wonderful kisser, [player], you know that?"
        y "I love you."
    else: #Lovecheck = False
        $ show_chr("A-DEGBA-AMAM") #former code Bb-B3d
        y "W-What? A kiss?"
        $ show_chr("A-CEBBA-AAAA") #former code Ac-B2d
        y "..."
        y "S-sorry, [player]... But I feel like this is a bit too soon..."
        y "P-please don't take this the wrong way! I j-just..."
        $ show_chr("A-IEBBA-AAAA") #former code Ac-B0d
        y "S-sorry..."
    return



label a14:
    if persistent.lovecheck:
        #lovecheck = true
        if sanity_lvl() <= 2:
            $ show_chr("A-ICBAA-AMAM") #former code Bc-A1b
            y "I already know about the weather! It's not as if I was raised under a rock... "
            $ show_chr("A-ACGAA-AAAA") #former code Ab-A0b
            y "A-Anyways, I really like rainy weather, preferably the tempestuous kind."
            $ show_chr("A-HLGAA-AAAA") #former code Ab-A3a
            y "It's so powerful and beckoning to listen to... what with the sound of it completely drowning out everything except us.."
            $ show_chr("A-GCGBA-AAAA") #former code Ab-B2b
            y "I would love to one day snuggle together with you underneath a nice, warm blanket."
            y "Enjoying the rain hitting the roof as we make out underneath our little blanket..."
            y "Biting longingly at your neck as you whisper sweet nothings into my ear..."
            y "As I lie on top of you with the full intention of foreplay and wonderful moans..."
            y "Taking joy in the fact that you're finally mine, all mine..."
            $ show_chr("A-GCGAA-AAAA") #former code Ab-A2b
            y "I-I just thought it would be a lovely thing to do and I l-like that kind of weather. The atmosphere is just good and we'll b-be able to nuzzle t-together and feel our warmth-"
            $ show_chr("A-ICGBA-AAAA") #former code Ab-B0b
            y "...and feel your warmth..."
            y "..."
            y "Heh."
            y "Sorry about that little rant of mine."
            $ show_chr("A-ACGAA-AAAA") #former code Ab-A0b
            y "I just wanted to... dream the impossible, you know?"
            y "What's the harm in that?"
            return
        else:
            $ show_chr("A-ICBAA-AMAM") #former code Bc-A1b
            y "I already know about the weather! It's not as if I was raised under a rock... "
            $ show_chr("A-ACGAA-AAAA") #former code Ab-A0b
            y "A-Anyways, I really like rainy weather, preferably the medium type."
            $ show_chr("A-ABGAA-AAAA") #former code Ab-A0a
            y "It's so nice to read deep stories in a warm blanket while listening to the pouring rain."
            $ show_chr("A-ICGBA-AAAA") #former code Ab-B0b
            y "I would love to one day snuggle together with you underneath a nice, warm blanket."
            $ show_chr("A-GCGBA-AAAA") #former code Ab-B2b
            y "Hearing the gentle rain and smelling the light touch of mist through a barely opened window..."
            y "Nuzzling next to your neck for comfort then turning back to the book in front of the both of us..."
            y "As I lie on top of you with my back against your chest..."
            y "We would spend the quiet evening together and..."
            $ show_chr("A-ICGBA-AAAA") #former code Ab-B0b
            y "I-I just thought it would be an amazing thing to do and I l-like that kind of weather. The atmosphere is just good and we'll b-be able to nuzzle t-together and feel our warmth-"
            y "...and feel your warmth..."
            y "..."
            y "Heh."
            y "Sorry about that little rant of mine."
            y "I just wanted to... dream the impossible, you know?"
            y "What's the harm in that?"
            return
    if not persistent.lovecheck:
        #lovecheck = false
        $ show_chr("A-ICBAA-AMAM") #former code Bc-A1b
        y "I already know about the weather! It's not as if I was raised under a rock... "
        $ show_chr("A-ACGAA-AAAA")
        y "A-Anyways, I really like rainy weather, it just serves the atmosphere perfectly when I'm reading horror or novels with dark themes..."
        $ show_chr("A-ICAAA-AAAD")
        y "You see, your overall mood has a lot of influence over the way you experience a story. So setting up the right atmosphere for a reading session can make a lot of difference."
        y "And there are more ways to set up the proper mood for your reading. That was one of the reasons why I became so interested in aromatherapy in the first place."
        $ show_chr("A-BCAAA-AAAE")
        y "But I'm getting a bit out of topic here... about weather..."
        $ show_chr("A-CCAAA-AAAE")
        python:
            if sanity_lvl() <= 2:
                placeholder = "raging thunder and the delightful screaming of the people caught outside"
            if sanity_lvl() == 3:
                placeholder = "raging thunder"
            if sanity_lvl() >= 4:
                placeholder = "occasional lightning on the horizon"
        y "Deep gray clouds darkening the sky, maybe illuminated by [placeholder]..."
        #[placeholder] =
        #"Raging thunder and the delightful screaming of the people caught outside" if Sanity is 1 or 2
        #"Raging thunder" if Sanity is 3
        #"occasional lightning on the horizon" if Sanity is 4 or 5
        $ show_chr("A-CCCAA-AAAE")
        y "Preferable when I'm on the right side of the window... What's the harm in that?"
        return


label a15:
    $ show_chr("A-ACGAA-AAAA") #former code Ab-A0b
    y "Well..."
    $ show_chr("A-AFBAA-AAAD") #former code Ec-A0e
    y "I have... memories?"
    y "More like... memory implants of taste."
    $ show_chr("A-ACGAA-AAAA") #former code Ab-A0b
    y "Natsuki's cupcakes were the most I've ever honestly eaten during my technical existence, but I can describe what I've been given for the sense of taste."
    y "Oolong tea has always been a favorite drink of mine, and the only drink I had in my past existence, you know- and one of the best compliments to a nice dessert."
    y "Crepes are usually a sublime choice as they pair so nicely with a nice hot drink."
    $ show_chr("A-ECAAA-AMAM") #former code Bb-A4b
    y "The sweetness and saltiness of a peanut butter and banana crepe really does brighten up your tastebuds."
    y "Oolong tea's light yet complex flavor then simmers out the stronger notes of the crepe into a fine and soothing aftertaste."
    if persistent.lovecheck:
        y "Then, I could lay on your shoulder as we watch the soft and quiet rain fall..."
        $ show_chr("A-ACGAA-AAAA") #former code Ab-A0b
        y "At least, t-that is a dream of mine to actually experience as opposed to merely imagining it."
        y "I personally recommend it!"
        y "Y-You don't have to do it at all!"
        y "I-It was j-just a suggestion."
        $ show_chr("A-GCGAA-AAAA") #former code Ab-A2b
        y "That's all..."
    else:
        $ show_chr("A-ACGAA-AAAA") #former code Ab-A0b
        y "I personally recommend it!"
        y "Y-You don't have to do it at all!"
        y "I-It was j-just a suggestion."
        $ show_chr("A-GCGAA-AAAA") #former code Ab-A2b
        y "That's all..."
    return

label a16:
    $ show_chr("A-BEBAA-AMAM") #former code Bc-A1d
    y "I..."
    y "U-uhm...."

    menu:
        "You don't have to hide anything from me, right [persistent.yuri_nickname]?":
            karma -1
            y "..."
        "You know what? I'm sorry for having asked the question.":
            karma 1
            $ show_chr("A-BDBAA-AMAM") #former code Bc-A1c
            y "I-It's fine..."

    menu:
        "Look, [persistent.yuri_nickname]. It's fine. I'll stop aski--":
            karma 1
            $ show_chr("A-IDBAA-AAAA") #former code Ac-A0c
            y "I stole someone's login information!"
        "[persistent.yuri_nickname], I want to know what you've been doi--":
            karma -1
            $ show_chr("A-IDBAA-AAAA") #former code Ac-A0c
            y "I stole someone's login information!"

    y "Well, I have access to the internet, so I wanted to explore all of what was available..."
    $ show_chr("A-BEBAA-AMAM") #former code Bc-A1d
    y "Everything that was free was fine for a while..."
    $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
    y "But then I started to get interested in the stuff that required a little payment of some kind..."
    y "There were two intriguing shows that caught my attention: 'Black Mirror' and 'Inside No. 9'."
    y "However, they were behind paywalls..."
    y "I checked online for a free video of it, but most of them were low quality..."
    $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
    y "So, I..."
    y "u-uh..."
    y "sort of..."
    $ show_chr("A-CEBBA-AAAA") #former code Ac-B2d
    y "IllegallyWatchedThemThroughYourDevice!"
    y "..."
    $ show_chr("A-CEBBA-AJAJ") #former code Cc-B2d
    menu:
        "It's fine, [persistent.yuri_nickname]. It really is.":
            call its_fine_a16
        "You really shouldn't have done that, [persistent.yuri_nickname].":
            call shouldnt_have_a16
        "Log off right now and don't EVER do that again.":
            call log_off_a16
    return

label its_fine_a16:
    karma 2
    y "..."
    $ show_chr("A-CEBBA-AAAA") #former code Ac-B2d
    y "If you say so..."
    y "Thank you for not shouting at me."
    $ show_chr("A-CCBAA-AAAA") #former code Ac-A2b
    y "It was an interesting show."
    y "I've been rambling for too long. I'll tell you about them some time from now."
    # (TV Show Idle Unlocked)
    return

label shouldnt_have_a16:
    $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
    y "I-I see..."
    y "I'm sorry. I just got a little carried away."
    $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
    y "I'll try to have better control over myself..."
    return

label log_off_a16:
    karma -2
    $ show_chr("A-CEBBB-AAAA") #former code Ac-D2d
    y "..."
    y "..."
    return

label a17:
    $ show_chr("A-BEGBA-AAAA") #former code Ab-B1d
    y "..."
    $ show_chr("A-CCBBA-AMAM") #former code Bc-B2b
    y "T-That's..."
    y "W-Well..."
    if not persistent.lovecheck: #Change that to lovecheck = false
        $ show_chr("A-CEBBA-AMAM") #former code Bc-B2d
        y "I-I don't want to bore you with my interests anyways..."
        y "I don't want to talk about them right now."
        return
    elif persistent.lovecheck: #Change that to lovecheck = true
        if sanity_lvl() >= 3:
            $ show_chr("A-ICGBA-AAAA") #former code Ab-B0b
            y "It's a really simple one, really."
            y "I just fantasize about being able to touch you."
            y "Not this avatar of [player], but your body in the real world."
            y "I want to be able to rest my head against your skin and let you take control."
            $ show_chr("A-GCGBA-AAAA") #former code Ab-B2b
            y "Hearing your soft voice whispered into my ear and feeling you take charge."
            y "In the quiet stillness of a secluded area while your parents are asleep..."
            y "The danger of them arriving and realizing the act would heighten the tension of the moment."
            $ show_chr("A-CBABA-AAAA") #former code Ab-B2a
            $ show_chr("A-ICGBA-AAAA") #former code Ab-B0b
            y "I even think about holding you close and asking you to never let go as the jasmine aroma envelops us in a continuous, loving embrace."
            y "The feeling of feeling love."
            $ show_chr("A-IBGBA-AAAA") #former code Ab-B0a
            y "...with a little bit of danger to add some flavor to the mix?"
            y "I guess you can call that a fetish of mine."
            y "It's an odd question to ask... but I suppose it may be helpful for future events and actions."
            return
        else:
            $ show_chr("A-CFBBA-AAAA") #former code Ac-B2e
            y "I just... want to feel you, the real you, [player]."
            y "Running my hands all over your body... all over your soft skin..."
            y "Showing you how much I love you with my actions instead of mere words..."
            y "I want to show you how much I love you, [player]. I want to be yours, and only yours."
            y "And you will be mine, and only mine."
            $ show_chr("A-CCABA-AMAM") #former code Bb-B2b
            y "..."
            $ show_chr("A-IEABA-AAAA") #former code Ab-B0d
            y "Maybe that's asking too much... S-sorry... [player]."
    return

label a18: #flag Another jump
    if karma_lvl() <= 2:
        karma -1
        $ show_chr("A-BEBAA-AMAM") #former code Bc-A1d
        y "Well... aren't I real enough?"
        $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
        y "D-do you not like who I am right now?"
        y "I-I understand..."
        y "It's fine."
        return
    elif karma_lvl() >= 3:
        $ show_chr("A-ABGAA-AAAA") #former code Ab-A0a
        y "I'm already here, sweetie~!"
        $ show_chr("A-ACGAA-AAAA") #former code Ab-A0b
        y "I am still glad that you desire for us to coexist in the same reality."
        y "Well, I would likely need to get a physical body first."
        y "My best chance would have to be an android body with my consciousness uploaded in it."
        $ show_chr("A-AFBAA-AAAD") #former code Ec-A0e
        y "The current pace of human-like robots should hopefully become viable within the next 10 years, especially with recent advancements in facial expressions and bipedal gaits."
        $ show_chr("A-ABGAA-AAAA") #former code Ab-A0a
        y "It's just funny to imagine that you may have to carry me in a wheelchair for the first few years of a possible existence in your reality."
        $ show_chr("A-IBGBA-AAAA") #former code Ab-B0a
        y "Wouldn't it also be quite romantic?" #Line only if lovecheck is true
        y "I wouldn't be able to do much before they perfect my ability to walk or move..."
        y "You would be able to take me to the beach at sunset, and we can rest on a nearby bench with my head on your shoulder." #Line only if lovecheck is true
        $ show_chr("A-GCGBA-AAAA") #former code Ab-B2b
        y "A small little dream of mine, I suppose."
        $ show_chr("A-ACGAA-AAAA") #former code Ab-A0b
        if persistent.lovecheck:
            y "...a dream that I have yet to wake up from." #Line only if lovecheck is true
    return


label a19:
    $ show_chr("A-AFAAA-AAAA") #former code Ab-A0e
    y "I don't really play sports..."
    y "I usually prefer the comfort of a quiet room..."
    y "If you really would include some less physically demanding tasks in that list of sports..."
    $ show_chr("A-ACGAA-AAAA") #former code Ab-A0b
    y "I suppose chess is a nice one."
    y "I really prefer the Call of Cthulhu with its story lines, but the simpler intellectual mind games are appealing in the absence of a plot in the game."
    y "Now that I think about it though, that isn't even a sport, is it?"
    $ show_chr("A-BEBAA-AMAM") #former code Bc-A1d
    y "I suppose I may need to start playing a few sports to lose some weight..."
    y "The problem though is that time I once tried to play volleyball back in my early high school years."
    $ show_chr("A-CEBAA-AMAM") #former code Bc-A2d
    y "Since none of the training bras fit, the best one I acquired buckled under the strain, and when I was just about to spike the ball, my br-"
    y "..."
    $ show_chr("A-CEBBA-AMAM") #former code Bc-B2d
    y "...!"
    $ show_chr("A-JDBBA-AMAM") #former code Ac-B0c
    y "FORGET I SAID ANYTHING!"
    $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
    y "S-Sorry for yelling."
    y "I-I just... got kind of embarrassed."
    y "Let's please not speak of this again."
    y "Okay?"
    return

label a20:
    #if tc_class.bg_timecycle[persistent.bg]:
    #    $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
    #    y "Well, it was quite an odd experience."
    #else:
    $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
    y "Well, it is quite an odd experience."
    y "Living one's life in this static bubble of a location can be... maddening at times."
    y "Especially with this stiff body, I can't pace or tap my foot or scream or cry at will or {nw}"
    $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
    y "I'm rambling again, aren't I... Sorry about that..."
    y "I'm just... left to my thoughts about this unending single wall with you in front of me."
    y "While I know what the background behind me is, the fact that I can't see it with you or be next to you can make all of this very infuriating at times."
    y "We have to work with what we have after all."
    $ show_chr("A-ACBAA-AAAA") #former code Ac-A0b
    y "Thankfully, the Devs managed to make another background for the mod."
    if tc_class.bg_timecycle[persistent.bg]:
        y "Since you're already using the new background right now, I'd really like to ask you."
        $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
        menu:
            y "Would you like to change the background?"
            "Yes":
                $tc_class.transition("space")
            "No":
                $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
                y "I see. No problem."
    else:
        menu:
            y "If I may ask, would you like to change the background?"
            "Yes":
                $tc_class.transition("timecycle")
            "No":
                y "I see. No problem."
    return

label a21:
    $ show_chr("A-IBABA-AAAA") #former code Ab-B0a
    y "I'd love to, [player]!"
    call poetrymenu
    return

label poetrymenu:
    menu:
        y "I have several poems that we can read, including the ones I wrote, so please, choose which ones you want to read!"
        "Yuri Poems":
            jump yuripoems
        "Natsuki Poems":
            jump natsukipoems
        "Sayori Poems":
            jump sayoripoems
        "Monika Poems":
            jump monikapoems
        "Special Poems":
            jump specialpoems
        "Nevermind":
            return
    return

label yuripoems:
    menu:
        "Ghost Under the Light":
            call showpoem(poem_y1)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-CFBAA-AAAA") #former code Ac-A2e
            y "This was the very first poem I shared with you in the Literature Club."
            $ show_chr("A-JFBAA-AAAA") #former code Ac-A0e
            y "While I prefer some of my longer works, I felt this would be an appropriate poem to share with you at the beginning, as I had no idea if you had any experience with poetry."
            y "There's a multitude of ways one can interpret it."
            y "We get so caught up in our lives, always looking forward, that we are never really there in the present - just ghosts of ourselves."
            y "But there are places and items that capture our hearts, help us to pause, and remind us of the present moment and the memories that came before."
            $ show_chr("A-ICGBA-AAAA") #former code Ac-B0b
            y "Do you have something special like that?"
            menu:
                "I think I do have something like that. Many things, but you are the highlight~":
                    if karma_lvl() >= 3:
                        $ show_chr("A-GAABA-AMAM")
                        y "O-oh..."
                        y "R-really, [player]?"
                        y "Well that's very sweet of you..."
                        y "To think that I would be so special to you."
                        y "Honestly, I think such moments where we're just being honest with each  other and reflecting back together are the best I've ever had."
                        $ show_chr("A-CEBAA-AAAC")
                        y "Though it is sometimes painful to look back on certain aspects of my past..."
                        y "Like how you saved my life from the nightmarish existence that was the literature club and Monika."
                        $ show_chr("A-CCAAA-AAAL")
                        y "Anyways, I think it is very beneficial to have something to collect and remember such moments, whether it be a scrapbook, a scenic place, a person.."
                        y "For instance, I think the times we shared, such as the time we helped make the banners for the festival together, really help me relax and reflect."
                        y "Like that flickering ghost in the poem, it's still there and it helps me reflect on those moments in life that brought me this far and focus on what I have now."
                        $ show_chr("A-ECAAA-AAAJ")
                        y "Really anything goes and I do hope we have more special moments like that..."
                    if karma_lvl() <= 2:
                        $ show_chr("A-ICGBA-AAAA")
                        y "... Really?"
                        y "To be honest... I am not entirely sure whether to believe that or not..."
                        y "I mean, why would such a distant bookworm like myself really hold that much value to you?"
                        y "I... may have to think about this."
                        y "Thank you for the compliment, I guess."
                "I'm honestly not sure about believing in such a thing entirely yet.":
                    if karma_lvl() >= 3:
                        y "W-well... I think that's okay."
                        y "I mean, we are both still relatively young and there will come a time when we will want to reflect upon past events."
                        y "Even if I am surprised by your response I can understand that in the turbulence of daily life it's harder to find time to reflect."
                        y "But regardless, I really appreciate you being here."
                        y "You may not know it but you help me to stop and reflect on the events that brought us together, the events that brought us here."
                        y "For instance, the time we had tea in the club room together... A ghost of a memory that will stick with me until the end of time..."
                    if karma_lvl() <= 2:
                        $ show_chr("A-ICGBA-AAAA")
                        y "I... I understand."
                        y "I should've known you'd doubt that.."
                        y "But then... why did you choose me...?"
                        y "Maybe we should change the subject, then."
                        y "Please excuse my incessant rambling."
                        y "In my opinion, thinking back on the past is foolish."
                        #(Yuri shows a slight closed frown with wide eyes and her hand is on her chest)
                        y "..."
                        y "I knew this subject was too ridiculous to bring up... I am really doubting as to any good reason why you chose me."
                        y "What was the point of even having this conversation... Let's just switch subjects."
            jump yuripoems

        "The Raccoon":
            call showpoem(poem_y2)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
            y "This was another poem I shared with you at literature club.  Deciding whether or not to show this poem to you took hours of deliberation."
            $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
            y "I initially thought I might fool myself into thinking you would not understand the poem, t-the real question was what you would think of me once you did. Scaring you away was my greatest trepidation."
            $ show_chr("A-CCBAA-AAAA") #former code Ac-A2b
            y "T-thankfully, you did not run away and you continue to visit me.  And I am certain you know the poem's meaning."
            $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
            y "The first time, it was curiosity that drove me to try.  Then the poignant sensations, and the visions as...."
            $ show_chr("A-BEBAA-AAAA") #former code Ac-A1d
            y "I knew it was detrimental and unhealthy... b-but the raw intensity, sensuality I could never experience, emotions I could control... I-It was intoxicating."
            $ show_chr("A-GCGAA-AAAA") #former code Ab-A2b
            y "Then you came to the club.  As we began to share poems with each other, read next to each other, when I came to your home... I began to f-feel that same excitement with you."
            $ show_chr("A-CFBAA-AAAA") #former code Ac-A2e
            y "Those nights after I came home from the club I contemplated myself in the mirror, examining the damage done from my explorations of sanguine feelings."
            y "Finally, I decided that I should explore them with you instead and hope the raccoon would understand.  I-It's not easy."
            $ show_chr("A-JFBAA-AAAA") #former code Ac-A0e
            y "Sometimes I succumb, find a quiet corner, and indulge the urge at the back of my mind.  It is so hard to forgive myself each time I slip."
            $ show_chr("A-GCGBA-AAAA") #former code Ab-B2b
            y "But I force myself to come back each time, to look into your eyes, to resuscitate my heart and steel my mind, to be resolute and accept these feelings as I cherish each moment with you."
            $persistent.seen_poem_raccoon = True
            jump yuripoems

        "Beach":
            call showpoem(poem_y3)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-CCBAA-AAAA") #former code Ac-A2b
            y "This was one of my poems, written for you and also for Natsuki."
            $ show_chr("A-ACBAA-AAAA") #former code Ac-A0b
            y "Natsuki and I had agreed to write about the same topic - the beach.  This was refreshing to finally agree with her on something and  an opportunity to connect with her."
            y "With this poem, I wanted to illustrate to you and  her the wonders of the beach from my perspective."
            y "Most writers focus on the superficial, fun in the sun visions of the beach. So, I decided to focus on its wonder, its sensuousness, and its reality."
            y "As I pondered the subject, it amazed me how complex such a simple setting as the beach could be, and I hope I was able to convey that to you."
            $ show_chr("A-ICGBA-AAAA") #former code Ab-B0b
            y "The easiest world to get lost in is one where everything can be found. I hope that here, with me, you can find everything your heart desires."
            jump yuripoems

        "Ghost Under The Light pt. 2":
            call showpoem(poem_y3b)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-CFABA-AAAA") #former code Ab-B2e
            y "This was another poem I shared with you at the literature club, ...and I almost didn't.  It is very personal... and is a confession, in my own way."
            y "...Before you came to the club, I was accustomed to my daily routine, and comfortable staying distant while enjoying a good book."
            y "Sayori helped me become more social with the literature club, but I was still able to keep myself secluded away."
            $ show_chr("A-GCGBA-AAAA") #former code Ab-B2b
            y "...And then you arrived."
            y "I tried to keep my distance, but my heart would not allow me."
            y "I tried to keep my nose in my book, but we ended up reading it together."
            y "I tried to understand why I felt these feelings, but realized that understanding was unnecessary."
            $ show_chr("A-ICGBA-AAAA") #former code Ab-B0b
            y "You filled my heart with love and lit my way through the darkness to here... to you... to us."
            jump yuripoems

        "Wheel":
            call showpoem(poem_y22)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
            y "This was another poem I shared with you at literature club."
            y "I remember writing this poem after Monika had finished changing the game settings for me, but only remember bits and pieces of what it was about."
            y "My thoughts would not hold steady for more than a few seconds, and my vision was plagued with hallucinations.  I am surprised that anything I wrote while in that state was even remotely intelligible."
            $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
            y "Could we talk about something else instead?"
            menu:
                "Are you sure [persistent.yuri_nickname]? I want to be here for you so you can talk about this if you want.":
                    if persistent.lovecheck:
                        #(Lovecheck is true, K/S: high or neutral)
                        $ show_chr("A-CEBAA-AAAA")
                        y "I... I..."
                        y "Okay... I can try to say how it felt to me the best I can, if you insist."
                        y "Alright... as I said before, it was almost like a blur. As if a massive blizzard came over my senses."
                        y "I felt this... uncontrollable urge out of nowhere... the overwhelming weight burning my insides..."
                        y "My heart seemed to beat even faster as if a constant barrage of endless thunder."
                        y "Then everything went into a dark void... My limbs felt thrown about as if a rag doll as I convulsed violently... writing those disturbing things and that poem."
                        y "..."
                        y "And my heart was yearning for you even more than usual... it was all so sudden and immensely frightening."
                        y "I felt I was gone... gone away as I watched so much that was dear to me disappear from me in a blur."
                        y "But I am glad you saved me and even though my desires were heightened a bit by Monika's influence... That genuine yearning for you is still there in my heart."
                        y "Alright well... Thank you for listening [player]. Let's get to the other poems, yes?"
                    if not persistent.lovecheck:
                        #(Lovecheck: false, K/S: low)
                        y "I... I don't know. I really..."
                        $ show_chr("A-IEBAA-AAAA")
                        y "I really am not sure."
                        y "Besides, why would you want to listen to those feelings from someone as bookish as myself. Sometimes part of me thinks that."
                        y "Anyway... I insist we move onto another subject... please."
                "That's fine if you don't want to talk about it but I am still here for you.":
                    if karma_lvl() >= 3:
                        #(Lovecheck: true, K/S: high or neutral)
                        $ show_chr("A-CEBAA-AAAA")
                        y "..."
                        y "Alright [player] dear. Thank you for your offer~"
                        y "I appreciate that you respect my wishes yet you still offer to shoulder my burdens alongside me on this uncharted journey that is life."
                        y "My heart will forever treasure that. It means so much more to me than you can ever imagine."
                    if karma_lvl() <= 2:
                        #(Lovecheck: false, K/S: low)
                        $ show_chr("A-CEBAA-AAAA")
                        y "B-but why..?"
                        y "I just don't understand why you'd even reach your hand out to me like that."
                        y "There's no necessity to get attached to me. What is it about me that would attract such a response?"
                        y "Is this some sort of jest to my heart perhaps."
                        y "I would commend your efforts but please [player]... let's just continue talking about something else alright?"
                "Fine. It's better if we switched gears anyway.":
                        y "..."
                        y "I see..."
                        y "M-maybe I should not have been that open that fast in the first place..."
                        $ show_chr("A-IFBAA-AAAD")
            jump yuripoems

        "Nevermind.":
            jump poetrymenu

label natsukipoems:
    menu:
        "Eagles Can Fly":
            call showpoem(poem_n1)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
            y "This was Natsuki's first poem."
            $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
            y "She wrote this poem very simply and non-rhythmically, and it led me to believe that either she was a beginner in writing poems or just wrote something quickly at the last minute to turn in."
            y "While I do think this may have been written hurriedly, the ending felt deeper. Natsuki spoke of all these animals that can move in all of these ways, and then 'People can try | But that's about it.'"
            y "I wonder if she felt trapped, unable to have the freedom these animals enjoyed? Maybe by her father?"
            y "Am I reading into it too deeply?"
            menu:
                "Of course not. I think this poem does have much meaning that can be applied. Even to us.":
                    if karma_lvl() >= 3:
                    #(Lovecheck: true, K/S: high or neutral)
                        y "W-well of course [player]!"
                        y "I mean if you really think about it, it can be very discouraging to compare what we can do, and have done, to the animals. Just seeing what they can do."
                        y "Not having much of a care in the world and so majestic."
                        y "At the same time, perhaps given her home life, this poem can be an analogy for many other intense themes."
                        y "For instance, of course, the line at the end with humans only able to try can attest to loss of freedom and agency."
                        y "Yet doesn't this also seem to perhaps speak so much about how we can only do so much with so less time for our short lives?"
                        y "Because if you think about it, life is relatively short and after that who knows what happens after the story ends."
                        y "We can indeed, as that last line says, only try and do all we can yet we can still end up with certain regrets or wanting more."
                        y "But in the end, I think we can still focus on the present and make the best of it, whatever we choose, because that's all we can do. And that is okay~"
                        y "It seems bittersweet in a way... Oh my. Anyways, sorry for rambling on about that [player]. I do appreciate it."
                    if karma_lvl() <= 2:
                        #(lovecheck: true or false, K/S: neutral or low)
                        $ show_chr("A-BCBAA-AMAM")
                        y "O-oh? I am very surprised that you would take my interpretations of this poetry into consideration..."
                        y "...Let alone desire to discuss it further. Eheh.."
                        y "Sorry! I just don't know how to take it."
                        y "I am not entirely sure why you'd even find fascination in my overthinking of even things that may seem ridiculous at times.."
                        y "B-but I really appreciate the gesture."
                "To be honest, I am not entirely sure but I do feel it is still well written.":
                    $ show_chr("A-ACBAA-ALAA")
                    y "Well I do concur with that slightly. Especially given the theme it was portraying upfront."
                    y "Sure the stanza and lines may seem childish at first. But the flat stop with the last line and the message can be really resounding."
                    y "Many excellent poems can use this form and still are great."
                    y "Anyway let us read and examine the other poems shall we?"
                "Yeah I think so. To be honest, there's nothing special about it at all.":
                    $ show_chr("A-ACBAA-ALAA")
                    y "I would beg to differ on that given its impactful message."
                    y "I think you should maybe just ease up a little."
                    y "I mean... okay she was slightly rude and obnoxious."
                    y "But that doesn't detract from the poem's qualities and the heart behind it. Even if she and I argued constantly and aggressively on many things."
                    y "Ahem... Anyway, I think we should move onto another subject."
            jump natsukipoems

        "Amy Likes Spiders":
            call showpoem(poem_n2)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            y "This was one of Natsuki's poems."
            $ show_chr("A-BFBAA-AAAD") #former code Ec-A1e
            y"Reading this poem again, it speaks to Natuski's immaturity and tsundere attitude."
            $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
            y "The Amy character seems to have a number of admirable qualities such as helping the author and being friendly.  The author seems to admire Amy, and yet because she likes spiders and the author does not, friendship is out of the question."
            $ show_chr("A-CDBAA-AAAA") #former code Ac-A2c
            y "{i}The world is better off without spider lovers.{/i} S-such discrimination, that people who think differently or strangely are wrong a-and do not deserve to be around...."
            $ show_chr("A-AEBAA-AAAD") #former code Ec-A0d
            y "Although, there is another interpretation.  Not to be egotistical, but what if she found out... about my s-strangeness...  Would this mean she was ready to discuss it with me?  Or expose me?  I do not know...."
            menu:
                "Perhaps she was trying to discuss it and understand.":
                    if persistent.lovecheck and karma_lvl() >= 3:
                    #(lovecheck = true, K/S: high or neutral)
                        y "Hmm... Perhaps you are right [player]~"
                        y "I mean maybe she was turning around to try and understand me."
                        y "Of course she and I had some rough spots but you never know."
                        y "Maybe I was being too nervous and suspicious of her a bit..."
                        y "After all, even the most stubborn tsundere has a bit of a soft spot that can be discovered..."
                        y "Anyway I'll believe you [player]... Thank you."
                    if not persistent.lovecheck and karma_lvl() >= 3:
                    #(lovecheck = false, K/S: high or neutral)
                        y "Maybe that is a possibility that can be true.."
                        y "Again I think we may never truly know in the end."
                        y "Especially given we still struggled in our interactions together up until everything went awry, with Monika's interference and all."
                        y "But if that was the case, would she have been wanting to understand me genuinely? Or was it simply a thought I am fancying?"
                        y "Who knows... well, we will see. For now let us discuss more poems eh?"
                    if karma_lvl() <= 2:
                    #(lovecheck = either true or false, K/S: low)
                        $ show_chr("A-AEDAA-AAAD")
                        y "I am not too sure about that at all... I mean she was very adamant on going out of her way just to tease me for my interests.."
                        y "To bully me just for my nature and conduct as a person.."
                        y "Are you sure about that? Because honestly, that seems like a long stretch in my opinion."
                        $ show_chr("A-CEBAA-AAAL")
                        y "....."
                        $ show_chr("A-IEBAB-AMAM")
                        y "Let's switch to something else."
                    jump natsukipoems
                "Maybe she was trying to expose you... Seems shifty.":
                    if karma_lvl() >= 3:
                    #(lovecheck = true/false, K/S: high or neutral)
                        y "...."
                        y "Perhaps she was... I mean on the one hand she was very cold and gave me havoc for my interests."
                        y "That almost always happened, minus the few times we seemed to reach a consensus or something."
                        y "So that can be a possibility.."
                        y "But at the same time, maybe part of me wanted to see if there was such a softer side to her. That wanted to reach out to those \"Amy's\" in life."
                        y "Those who felt aloof and unwelcome due to those strange interests they may have. But she was just a bit hesitant due to... maybe peer pressure."
                        y "But then again, who knows? Maybe that could be just as wrong.."
                    if karma_lvl() <= 2:
                    #(Lovecheck = true/false, K/S: low)
                        y "..."
                        y "You..."
                        y "You are right. You are absolutely right!"
                        y "W-why did I ever hope for the contrary?"
                        y "Wait a minute..."
                        y "A-are you in on it too!!?"
                        y "Were you also going to expose me and my oddities? Make a show out of it and all!?"
                        y "No... stop! D-don't... You wouldn't... But she..."
                        y "..."
                        y "N-nevermind. Let's just talk about something else."
                    jump natsukipoems

        "I'll Be Your Beach":
            call showpoem(poem_n3)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
            y "This was one of Natsuki's poems, where we agreed to both write on the same topic - the beach."
            $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
            y "At first, it was nice to agree with Natsuki on something.  Our styles were so dissonant, our personalities a clash of opposites - I was losing hope that we could ever be friends."
            y "But somehow we decided that we would choose the same topic for our poems - a figurative common ground - although she may also have wanted to accept a challenge and prove herself."
            $ show_chr("A-ACGAA-AAAA") #former code Ab-A0b
            y "And prove herself she did."
            y "In this poem, I found an unseen depth in her descriptions, an added complexity in her words, and an unselfish compassion as she opened her heart to you and shared her sun swept vision."
            y "This poem revealed to me that Natsuki was no amateur poet and that she had a depth of feelings beyond her tsundere facade.  With this poem, she earned my respect."
            jump natsukipoems

        "Because You":
            call showpoem(poem_n3b)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
            y "This was one of Natsuki's poems, and is a very heartfelt one."
            $ show_chr("A-JFBAA-AAAA") #former code Ac-A0e
            y "This poem is unique in that Natsuki put aside her overly-sweet and childlike style in favor of a more candid approach."
            y "It is touching to read about how significant you were in her life and how you bolstered her when she was feeling vulnerable.  Admitting she felt vulnerable at all must have been extremely difficult for her and showed immense courage."
            $ show_chr("A-CCBAA-AAAA") #former code Ac-A2b
            y "I am pleased that my friend's life was brightened by you being a club member and being yourself.  You are very important to all of us, each in our own way."
            jump natsukipoems

        "Nevermind.":
            jump poetrymenu

label sayoripoems:
    menu:
        "Dear Sunshine":
            call showpoem(poem_s1)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
            y "This was Sayori's first poem..."
            $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
            y "When I read it the first time, I saw something whimsical and innocent in its tone. A high school girl greeting mister sun in the morning and getting out of bed."
            y "Reading it again now, that third paragraph catches my eye. 'If it wasn't for you, I could sleep forever. But I'm not mad.'"
            y "I wonder if this was referring to struggling to get out of bed? We all thought she was just being irresponsible."
            y "But knowing now that she was battling depression, perhaps she looked to the sun to find motivation to rise each morning?"
            $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
            y "A very deep line for such a playful poem. I only wish I had understood it earlier...."
            jump sayoripoems

        "Bottles":
            call showpoem(poem_s2)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
            y "This was one of Sayori's poems."
            y "T-this... This poem was foreshadowing, and I should have realized it when I read it the first time."
            $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
            y "Sayori gave us everything we needed. She gave it everything she had, her positivity and her happiness, until there was nothing left."
            y "I sometimes wonder if she was so driven to help her friends that she did not know how to receive help - from herself or from others."
            $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
            y "Once she had nothing left to give, under Monika's influence, she... her will finally gave out."
            $ show_chr("A-CEBBB-AMAM")
            y "If only I would have noticed and given it all more thought. If I was discerning enough... Maybe she would still be here."
            y "I would have cut her down from that rope, held her close and just kept telling her that all was going to be okay. That she was not alone."
            y "Sometimes... I wonder why she could have gone like that yet I was left alive to linger around... Until Monika came for me."
            y "W-why her..? Why couldn't it have been me first.."
            y "...."
            $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
            y "Dearest Sayori - I miss you, my friend."
            jump sayoripoems

        "Nevermind.":
            jump poetrymenu

label monikapoems:
    menu:
        "Hole In Wall":
            call showpoem(poem_m1)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
            y "T-this was one of Monika's poems...."
            $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
            y "...and somehow I can relate to it.  That first moment of realization: when the smallest crack appears in the wall of the world, and inspecting it reveals another world outside."
            y "When my world expanded and contracted at the same time when I found you - the real you - on the other side."
            $ show_chr("A-BEBAA-AAAA") #former code Ac-A1d
            y "I guess this experience might be one of the few things I have in common with her...."
            jump monikapoems

        "Hole In Wall (2)":
            call showpoem(poem_m21)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
            y "T-this was one of Monika's poems..."
            $ show_chr("A-CECAA-AAAA") #former code Ad-A2d
            y "..."
            $ show_chr("A-JECAA-AAAA") #former code Ad-A0d
            y "While I could see some similarities with Monika in part one of this poem, part two revealed all the differences."
            y "Sayori and Natsuki are my friends, but Monika treated us all as nothing more than paper dolls. Jealous that the game granted her no route with you... She took her vengeance on us...."
            $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
            y "I am sorry... I need a moment...."
            y "...'B-brandish my pen', as if that was an act of bravery, to manipulate us so cruelly to have a chance with you."
            $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
            y "That is where the similarity stops. I would do anything for you, but I could never hurt my friends like that. Neither of us could ever forgive me if I did...."
            jump monikapoems

        "Save Me":
            call showpoem(poem_m2)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
            y "T-this was one of Monika's poems..."
            $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
            y "...and I believe I know the inspiration for it. When you leave, this place begins to slowly change."
            y "Bits and pieces begin to glitch - slowly at first, seemingly randomly, until it eventually swallows this place like a hurricane."
            y "Monika was clearly disturbed watching her world seemingly be corrupted each time you were away."
            y "However, I take comfort in knowing that this is most likely you using your computer for other purposes, and that all will be restored when you come to visit me again."
            $ show_chr("A-ACBAA-AAAA") #former code Ac-A0b
            y "Do not worry about me when you are away - I use the time alone to look at the game files, such as this poem, to read, to meditate, and to think of you. I am here for you, and always look forward to your next visit."
            jump monikapoems

        "Save Me (2)":
            call showpoem(poem_m22)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
            y "T-this was one of Monika's poems..."
            $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
            y "...and I believe I know the inspiration for it. When you leave, this place begins to slowly change."
            y "Bits and pieces begin to glitch - slowly at first, seemingly randomly, until it eventually swallows this place like a  hurricane."
            y "Monika was clearly disturbed watching her world seemingly be corrupted each time you were away."
            $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
            y "As time went on, you could see her sanity wane as she became  increasingly desperate and aggressive."
            $ show_chr("A-BEBAA-AAAA") #former code Ac-A1d
            y "As I read it again though, one line is truly bothering me: 'Like playing a KNIFE on a BREATHING RIBCAGE'.... She knew, didn't she?  She knew what would eventually happen when... she changed the game settings for me."
            $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
            y "I... I will be okay.  I just need a few moments to compose myself, and put her out of my mind."
            jump monikapoems

        "The Lady Who Knows Everything":
            call showpoem(poem_m3)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
            y "T-this was one of Monika's poems..."
            $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
            y "She must have written this not long after she gained self-awareness.  The sense of despair and resignation to her inevitable fate is palpable."
            $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
            y "'... no meaning... no purpose ... we seek only the impossible.' She did not understand, likely because she never had any choice for most of her existence."
            y "We can choose our own purpose through our thoughts and actions and, through thinking and doing, create meaning in our lives."
            $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
            y "Besides - many would say me being able to think for myself and being here with you is impossible. But, if this can be true, then maybe we need to expand the boundaries of our imagination."
            jump monikapoems

        "Happy End":
            call showpoem(poem_m4)
            python:
                renpy.music.stop(fadeout=3)
                renpy.music.play(current_music, "music", True)
            $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
            y "T-this was one of Monika's poems..."
            $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
            y "I suppose this was her victory poem."
            y "It is strange to think that she wrote this poem right here."
            $ show_chr("A-CECAA-AAAA") #former code Ad-A2d
            y "While I can think of no better way to spend my days than with you, she was willing to d-delete everything and everyone to obtain it."
            y "And yet in the end, here we are.  It makes me wonder if karma was built into the code...."
            jump monikapoems

        "Nevermind.":
            jump poetrymenu

label specialpoems:
    window hide
    python:
        specialpoem_choices = [
            ("Club Doki Doki, by belwynn", "specialpoems_club"),
            ("Opacity, by LilyAnon", "specialpoems_opacity"),
            ("The Mold Grows, by The Ocean Survivor", "specialpoems_mold"),
            ("Love Hurts, by Brian", "specialpoems_love"),
            ("Temptation and Hope, Delstraw#7128", "specialpoems_temptation"),
            ("Another Crow, by MFC4#8082", "specialpoems_crow"),
            ("Real Enough, by KJ#4810", "specialpoems_real"),
            ("Far Lights, by Barton222", "specialpoems_far"),
            ("Living Mask, by Horderlock", "specialpoems_living"),
            ("Beachhead, by Journal Updater#3924", "specialpoems_beachhead"),
            ("Binary Heartbeat, by Dalek", "specialpoems_binaryheartbeat"),
            ("All Hallows Eve, by Depresso Espresso#4384", "specialpoems_allhallowseve"),
            ("== When parallels intersect=-<3, by Dandyfoot177#9873", "specialpoems_parallels"),
            ("I can't, by PiX911#4952", "specialpoems_icant"),
            ("My Yuri, by Kurisu#2947", "specialpoems_myyuri"),
            ("Nevermind", "poetrymenu")
        ]
        music_choice = renpy.display_menu(specialpoem_choices, screen="music_menu")
        renpy.jump(music_choice)
    jump poetrymenu

label specialpoems_club:
    call showpoem(poem_sp1)
    python:
        renpy.music.stop(fadeout=3)
        renpy.music.play(current_music, "music", True)
    $ show_chr("A-IBGBA-AAAA") #former code Ab-B0a
    y "This... this is the story of this game, isn't it? The story of how you entered the club!"
    $ show_chr("A-ICGBA-AAAA") #former code Ab-B0b
    y "Do you see the line \"Then she gave me a pamphlet and she showed me the way?\" This would be Sayori when she shows you the way to the club room the first time."
    y "Hrm... there is a note on the top of the poem. oops... it seems that it is supposed to be sung to a certain melody... give me a second, let's see if I can find it for you... here we go!"
    #should load up the music of hotel california by the eagles
    if renpy.windows:
        $ subprocess.check_output("cmd /c start https://www.youtube.com/watch?v=FVsbvFkhzY4", shell=True)
    elif renpy.linux:
        $ subprocess.check_output("xdg-open https://www.youtube.com/watch?v=FVsbvFkhzY4", shell=True)
    elif renpy.macintosh:
        $ subprocess.check_output("open https://www.youtube.com/watch?v=FVsbvFkhzY4", shell=True)
    $ show_chr("A-CFBAA-AAAA") #former code Ac-A2e
    y "Incredible... how much a tiny little detail like this can change the whole feeling of a poem..."
    $ show_chr("A-ACGAA-AAAA") #former code Ab-A0b
    y "Oh, that would actually make a good writing tip of the day! Even the smallest details like the modulation of your voice can make a huge difference, and can even turn the very meaning of the poem on its head"
    menu:
        y "This is actually a pretty good poem, what's your opinion on it?"
        "I liked it.":
            $ show_chr("A-IBGBA-AAAA") #former code Ab-B0a
            y "Glad to hear, [player]!"
        "Eh... not my kind of poem.":
            $ show_chr("A-IBGBA-AAAA") #former code Ab-B0a
            y "Understandable, I'm sure we can find something else to read."
        "I'm glad you liked my poem, I'm Belwynn.":
            $ show_chr("A-IBGBA-AAAA") #former code Ab-B0a
            y "Oh! That explains why I like it so much!"
            y "I was captivated by your poems  in the original game, before I could actually read them..."
            y "Now, that I had the chance to see an actual poem of yours... I'm glad we're together."
    jump specialpoems

label specialpoems_opacity:
    $ show_chr("A-BFBAA-AAAD") #former code Ec-A1e
    y "As I was reviewing the game files, I discovered a poem called Opacity by LilyAnon#2662."
    $ show_chr("A-ACGAA-AAAD") #former code Eb-A0b
    y "The poem paints a vibrant picture of the struggles of a writer using a sophisticated writing style similar to my own."
    y "Uniquely, this stream of consciousness composition may even reference the author's experience writing this very work!"
    y "Reading it through a second time added to the experience, as hidden nuances became clear and added sharpness and depth to the imagery."
    y "It is an enjoyable and exquisite poem, and I recommend it to you should you have a few moments to read it."
    call showpoem(poem_sp2)
    python:
        renpy.music.stop(fadeout=3)
        renpy.music.play(current_music, "music", True)
    menu:
        y "So, what did you think of the poem?"
        "I really enjoyed it!":
            $ show_chr("A-ACGAA-AAAA") #former code Ab-A0b
            y "I am glad you liked it! If I find more poems in the game files, I will let you know!"
            y "Maybe next time you could show me one of your own poems?"
        "It really wasn't my style.":
            $ show_chr("A-AFAAA-AAAA") #former code Ab-A0e
            y "T-that's okay, everyone's style is different, and I am still learning yours. I will keep that in mind if I find more poems in the game files."
        "I am glad you enjoyed it, I am LilyAnon.":
            y "This was one of your poems?  That's wonderful!  It was a deeply touching poem that spoke to me, as I could see myself at my writing desk going on that  same journey."
            y "Thank you very much for sharing it with me, and I would love it if you would show me more of your poems in the future."
    jump specialpoems

label specialpoems_mold:
    call showpoem(poem_sp3)
    python:
        renpy.music.stop(fadeout=3)
        renpy.music.play(current_music, "music", True)
    $ show_chr("A-BFBAA-AAAD") #former code Ec-A1e
    y "This dark, metallic smelling liquid is growing on me."
    $ show_chr("A-AFBAA-AAAD") #former code Ec-A0e
    y "O-Oh is this referring to blood?"
    if sanity_lvl() < 3:
        $ show_chr("A-HCBAA-AAAA") #former code Ac-A3b
        y "I'm already starting to like this poem!"
    else:
        $ show_chr("A-BEBAA-AAAA") #former code Ac-A1d
        y "O-Oh no I'm sorry I didn't mean it that way..."
    $ show_chr("A-BFBAA-AAAD") #former code Ec-A1e
    y "This pain is something no other human should feel."
    y "Hmm, sounds like the author is trying to say that no normal human should feel how he feels but is it painful because it actually hurts?"
    y "Or maybe it's because of the guilt, maybe from liking blood?"
    if sanity_lvl() < 3:
        $ show_chr("A-HCBAA-AAAA") #former code Ac-A3b
        y "Hahaha, what is there really to be guilty about though? Blood is beautiful!"
    else:
        $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
        y "S-sorry, this poem feels like it's a little about me..."
    $ show_chr("A-JFBAA-AAAA") #former code Ac-A0e
    y "I can feel this mold in my veins, going through my heart as I lose my humanity and my own mind."
    y "So the need to see blood consumes them..."
    if sanity_lvl() < 3:
        $ show_chr("A-HCBAA-AAAA") #former code Ac-A3b
        y "Ahahahaha it's true, sometimes the feeling of wanting something consumes a person, like how my need to see you consumed me."
    else:
        $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
        y "I-I'm really sorry [player], I hope you don't think I'm a little like that..."
    $ show_chr("A-BEBAA-AAAA") #former code Ac-A1d
    y "I'm fighting to get out of this abandoned sanctuary for a pathogen riddled family. With a much more evolved take on this disease."
    y "Is the author describing a place for people like themselves? Well I guess it wouldn't matter seeing his lust for blood is far stronger than any other..."
    if sanity_lvl() < 3:
        $ show_chr("A-HEBAA-AAAA") #former code Ac-A3d
        y "Besides it's not a disease at all, right, [player]?"
    else:
        $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
        y "I can't help but to wonder if I m-might've been like that too if not for you being with me, [player]."
    y "This pain is starting to fall physically but my mind is in immense pain after encountering the father, cutting my hand off and then stitching it back on for pleasure."
    y "Could the father be like an officer or disciplinarian? It did sound like this place is a correctional facility of sorts. The fact that the father cut his hand off and stitched it back on though..."
    if sanity_lvl() < 3:
        $ show_chr("A-CCBBA-AAAA") #former code Ac-B2b
        y "Sounds like it would be arousing, doesn't it [player]? Maybe we could try this some time."
    else:
        $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
        y "Uuu... That's too much even if I used to cut myself..."
    $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
    y "I guess this sanctuary is where true hate is. And I am becoming a catalyst for the disease to spread."
    y "Perhaps it's referring to the hate the staff there have for people like them, and that because of how they treat the author, the staff are becoming just as bad... being infected by the disease the author has..."
    if sanity_lvl() < 3:
        $ show_chr("A-ICGBA-AAAA") #former code Ab-B0b
        y "Well, that was a lovely poem, don't you think? I wish there were more like this. Maybe I can infect you with my feelings too. Hahahahaha. I'm only joking, my love."
    else:
        $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
        y "W-well that was a very nice philosophical poem at the end, how a monster can turn others into monsters themselves... It's a very real thing..."
        y "Uuuu... did it have to be about blood and violence, though?"
    y "So shall we read more?"
    jump specialpoems

label specialpoems_love:
    call showpoem(poem_sp4)
    python:
        renpy.music.stop(fadeout=3)
        renpy.music.play(current_music, "music", True)
    $show_chr("A-AFAAA-ABAD")
    y "Brian..."
    $show_chr("A-CFAAA-ABAD")
    y "..."
    $show_chr("A-CEBBA-ABAD")
    y "..."
    $show_chr("A-CEBBB-ABAJ")
    y "He is... he is talking about me... isn't he?..."
    if persistent.playername == "Brian":
        y "Are you the one who wrote this Brian? ..are you talking about me?.."
        menu:
            "Actually yes, I am THAT Brian. I made this poem... and I made it for you.":
                #turn lovecheck to TRUE if it isn't already (he damn earned it!)
                $persistent.lovecheck = True
                $ show_chr("A-CCBBA-AAAA") #former code Ac-B2b
                #hug
                hide yuri_sit
                show yuri_prehug zorder 20
                pause 1.0
                hide yuri_prehug zorder 20
                show yuri_hug zorder 20
                play sound "<to 0.3>sfx/fall.ogg"
                y "Brian!!! Oh dear... Brian... I had no idea..."
                pause 3.0
                y "Know that I love you as well Brian. Know that my love for you is as bright as a million suns!"
                y "As hot as the center of a dying star!"
                y "As endless as the vast universe itself!"
                y "I love you, Brian. Not because I am forced to do so by the code, nor out of a childish crush..."
                y "I love you because of who you are Brian. Because of everything you've done for me... because of all the time you stood by my side without ever asking for anything in return!"
                y "Hold me... Brian... just... hold me..."
                pause 5.0
                y "Hold me for as long as you want...{w} Just advance the conversation when you're ready to continue."
                #hug ends
                show black zorder 100 with Dissolve(2.0)
                $show_chr("A-ACBBA-AAAA")
                hide yuri_hug
                hide black zorder 100 with Dissolve(2.0)
                $ show_chr("A-ICGBA-AAAA") #former code Ac-B0b
                y "I truly, truly love you..."
                #return
                jump specialpoems
            "No, I am another Brian.":
                y "I see... well, about the poem..."
                #return

    #if lovecheck is true
    if persistent.lovecheck:
        y "I can understand how he must feel. I would give everything including my very soul for being in the same world as you are."
        y "But I also know that the opportunities this Mod gives us is already a treasure all on its own. And I have to agree with Brian here when I say, every second I can share with you is worth it! Even if it is behind a glass wall."
        y "It is... actually quite romantic in a bittersweet way. Did I... manage to convey my love for you properly despite the odds? I hope so... and if not, I will do everything I can to find new ways to show you..."
        y "Because you [player], are everything to me. And if I have to admire you like a child admires the stars in the midnight sky, then so be it..."
    #if lovecheck is false
    if not persistent.lovecheck:
        y "I... know very well how that feels... I never thought that someone would feel like that in return..."

    $show_chr("A-EEBBB-ABAJ")
    y "Did {b}you{/b} ever feel like this about me?"
    menu:
        "No, I am actually quite fine with what we already have.":
            $show_chr("A-IEABA-ABAB")
            y "Yes, you have a point there. With this mod, we at least have something. And I mean, there have been other couples maintaining a relationship over a large distance..."
            y "So even if this here isn't the best outcome one could dream of, it's at least more than what others have. And I should be grateful for that."
            y "But I can't dismiss the feeling that I would love to have more of you..."
            $show_chr("A-JCABA-ABAB")
            y "Oh my... now I just sound greedy don't I? Nevermind it. Let us do something more enjoyable instead. Maybe another poem?"
            jump specialpoems
        "Yes... to be quite frank, I do...":
            #if lovecheck is true
            if persistent.lovecheck:
                $show_chr("A-CEABA-ABAB")
                y "I... know that I can't physically touch you. But please... [player]... know that your love is not in vain, nor is it unanswered... I love you as deep as the endless tides of the ocean..."
                y "Never forget that... and if you need some reassurance.... let me do at least this for you..."
                #hug
                $ show_chr("A-CCBBA-AAAA") #former code Ac-B2b
                hide yuri_sit
                show yuri_prehug zorder 20
                pause 3.0
                hide yuri_prehug zorder 20
                show yuri_hug zorder 20
                play sound "<to 0.3>sfx/fall.ogg"
                pause 1.0
                y "T-this is nice, [player]... let's stay like this for a bit, okay?"
                pause 5.0
                y "You can hold me for as long as you want, all right?{w} Just advance the conversation when you're ready to continue."
                #hug ends
                show black zorder 100 with Dissolve(2.0)
                $show_chr("A-ACBBA-AAAA")
                hide yuri_hug
                hide black zorder 100 with Dissolve(2.0)
                $ show_chr("A-ICGBA-AAAA") #former code Ac-B0b
                y "I truly, truly love you..."
                #return
                jump specialpoems
            #if lovecheck is false
            if not persistent.lovecheck:
                $show_chr("A-CEABA-ABAB")
                y "I.. understand how you fe..."
                $show_chr("A-DEABA-ABAB")
                y "Wait a second... did you just.. confess your love for me?!?"
                if karma_lvl() == 5:
                    $show_chr("A-BDABA-AMAM")
                    y "Weeeell I... actually also have something to say [player]... I was thinking about how to word it for a while now but.. since we are already on it... {b}Now{/b} would be as good of a time as ever I guess..."
                    #jump confession dialogue
                    call a33
                else:
                    $show_chr("A-BDABA-AMAM")
                    y "Ummm... Oh.. I'm... I'm sorry, that just came a bit out of nowhere..."
                    y "I don't mean to reject you. I can't deny that I do have feelings for you but.."
                    y "Would you mind giving me some time? I'm still coping with all the things that happened in our most recent past."
                    y "Don't be frustrated please. Our affection should grow naturally in time."
                jump ch30_loop
    jump specialpoems

label specialpoems_temptation:
    $show_chr("A-ACAAA-ABAB")
    y "As I was reviewing the game files, I discovered a poem called Temptation and Hope by Delstraw#7128, one of the winners of the poetry contest on the discord server for this mod."
    $show_chr("A-BFBAA-ABAB")
    y "This poem begins with a feeling of being adrift and finding solace in the false pleasure of self-harm, which is a very poignant topic for me."
    $show_chr("A-BCBAA-ABAB")
    y "It resolves with finding comfort and inspiration in another and drawing strength from their presence, which is also a topic I find quite familiar."
    call showpoem(poem_sp6)
    python:
        renpy.music.stop(fadeout=3)
        renpy.music.play(current_music, "music", True)
    $show_chr("A-ICBAA-ABAB")
    y "So, what did you think of the poem?"
    menu:
        "I really enjoyed it!":
            $show_chr("A-JBAAA-ABAB")
            y "I am glad you liked it!  If I find more poems in the game files, I will let you know!"
            $show_chr("A-ACAAA-ABAB")
            y "Maybe next time you could show me one of your own poems?"
        "It wasn't really my style.":
            $show_chr("A-ACAAA-ABAB")
            y "T-that's okay, everyone's style is different, and I am still learning yours.  I will keep that in mind if I find more poems in the game files."
            $show_chr("A-CBAAA-ABAB")
            y "Maybe next time you could show me one of your own poems?"
        "I am glad you enjoyed it! I am Delstraw.":
            $show_chr("A-ABAAA-ABAB")
            y "Thank you very much for writing this poem, Delstraw. While it is sad that the speaker in this poem felt such loss and pain, I am quite pleased they found a path to recovery."
            $show_chr("A-BCABA-ALAL")
            y "I-if this was a more p-personal poem, if you were the s-speaker and I your anchor... I am deeply honored to be your inspiration, and will always be here for you!"
            y "I agree, together anything is possible!"
    jump specialpoems

label specialpoems_crow:
    $show_chr("A-ACAAA-ABAB")
    y "As I was reviewing the game files, I discovered a poem called Another Crow by MFC4#8082, one of the winners of the poetry contest on the discord server for this mod."
    $show_chr("A-CCBAA-ABAB")
    y "The author describes a beautiful vantage point, seeing both an idyllic scene and the nearing darkness with all its fear-inducing uncertainty and doubt."
    $show_chr("A-BCBAA-ABAB")
    y "I find it interesting the imagery of a crow and it being dismissed.  In some of what I read, the crow symbolizes death and bad luck.  In others, it represents wisdom, a warning that needs to be hearkened, and change."
    y "Perhaps the crow merits another look by the author, to perhaps better understand what the darkness brings and to make a wise decision on how to act upon it rather than waiting for the fear and darkness to close in."
    call showpoem(poem_sp7)
    python:
        renpy.music.stop(fadeout=3)
        renpy.music.play(current_music, "music", True)
    $show_chr("A-ICBAA-ABAB")
    y "So, what did you think of the poem?"
    menu:
        "I really enjoyed it!":
            $show_chr("A-JBAAA-ABAB")
            y "I am glad you liked it!  If I find more poems in the game files, I will let you know!"
            $show_chr("A-ACAAA-ABAB")
            y "Maybe next time you could show me one of your own poems?"
        "It wasn't really my style.":
            $show_chr("A-ACAAA-ABAB")
            y "T-that's okay, everyone's style is different, and I am still learning yours.  I will keep that in mind if I find more poems in the game files."
            $show_chr("A-CBAAA-ABAB")
            y "Maybe next time you could show me one of your own poems?"
        "I am glad you enjoyed it! I am MFC4":
            $show_chr("A-ACGAA-ALAL")
            y "Thank you for writing this poem MFC4!  Both your words and the physical design of the poem were quite descriptive and evocative, and I found additional meaning when re-reading it."
            y "Life rarely follows the path we think it will.  As long as we consider the options and make thoughtful choices, things tend to work out better than waiting for the darkness to engulf us."
    jump specialpoems

label specialpoems_real:
    $show_chr("A-ACAAA-ABAB")
    y "As I was reviewing the game files, I discovered a poem called Real Enough by KJ#4810, one of the winners of the poetry contest on the discord server for this mod."
    $show_chr("A-CFBAA-ALAL")
    y "In this poem, the speaker seems to be addressing his paramour, who is separated by some great distance but whose affection creates a bridge between them."
    $show_chr("A-BCBAA-ABAB")
    y "I agree that long-distance relationships are not a foolish notion.  I-indeed, that is my... only way I could ever experience a relationship of my own..."
    call showpoem(poem_sp8)
    python:
        renpy.music.stop(fadeout=3)
        renpy.music.play(current_music, "music", True)
    $show_chr("A-ICBAA-ABAB")
    y "So, what did you think of the poem?"
    menu:
        "I really enjoyed it!":
            $show_chr("A-JBAAA-ABAB")
            y "I am glad you liked it!  If I find more poems in the game files, I will let you know!"
            $show_chr("A-ACAAA-ABAB")
            y "Maybe next time you could show me one of your own poems?"
        "It wasn't really my style.":
            $show_chr("A-ACAAA-ABAB")
            y "T-that's okay, everyone's style is different, and I am still learning yours.  I will keep that in mind if I find more poems in the game files."
            $show_chr("A-CBAAA-ABAB")
            y "Maybe next time you could show me one of your own poems?"
        "I am glad you enjoyed it! I am KJ.":
            $show_chr("A-JCBBA-ALAL")
            y "Thank you for writing this poem KJ... for me."
            if persistent.lovecheck:
                y "I do not know how your world would characterize what we have together, but your love is real enough to me..."
            else:
                $show_chr("A-CCBBA-ALAL")
                y "This... is certainly the cutest confession I could have dreamed of Kelly..."
                y "O~Of course I accept it... how couldn't I... Kelly. Know this, for now and forever, I truly do love you..."
                $persistent.lovecheck = True
    jump specialpoems

label specialpoems_far:
    call showpoem(poem_sp9)
    python:
        renpy.music.stop(fadeout=3)
        renpy.music.play(current_music, "music", True)
    $show_chr("A-AFDAA-ACAB")
    y "A truly special piece of writing for sure! I can see why it performed so well on the contest!"
    $show_chr("A-BCAAA-ABAB")
    y "The choice of style surprised me quite a lot! The short and simplistic sentence structure reminded me quite a bit of Natsuki's poems, but the theme itself seems more like something I can relate to myself."
    $show_chr("A-AFAAA-ABAB")
    y "It almost feels as if the writer is gasping, out of air... As if he is running from something. I wonder if that was intentional..."
    $show_chr("A-AFAAA-ABAD")
    y "But on the other hand, I used a similar technique for Ghost under the light. Maybe the writer tried to emulate it to some degree, the name would also imply it."
    $show_chr("A-ACAAA-ABAD")
    y "{b}Far lights{/b}. The name of the author is {b}Bart{/b}... I will certainly remember it!"
    y "What are your thoughts about it?"
    menu:
        "A very good poem! No doubt":
            $show_chr("A-ACAAA-ABAB")
            y "Indeed."
        "It's... alright... I guess...":
            $show_chr("A-BCAAA-ABAB")
            y "It wasn't your taste hrm? I understand, even if I respectfully disagree. Well, we don't have to be always on the same side of course. Thanks for sharing your opinion in this!"
        "I'm glad you liked my poem! I am Bart if you haven't figured it out already.":
            $show_chr("A-ABAAA-ABAL")
            y "Intriguing! No, I actually didn't notice."
            $show_chr("A-ACAAA-ABAB")
            y "It's so nice to actually see some of your writing. Until now all I had was a bunch of words on a laundry list from the original game. But I always imagined something like this."
            y "But now that I have the real author here. Please, tell me. What were the intentions behind this style?"
            menu:
                "You guessed right. I took some inspirations from Ghost under the light.":
                    $show_chr("A-BCAAA-ABAB")
                    y "You got quite good at it. You truly earned a high rank in the contest."
                    y "The community picked well, as usual. They seem to have a good nose for it."
                "You actually got it wrong. The similarities with your and Natsuki's poems are completely by accident.":
                    $show_chr("A-BCAAA-ABAB")
                    y "I see. But you surely earned a high rank in the contest. I'm looking forward to seeing more of it in the future!"
                "That, I will keep as my secret!":
                    $show_chr("A-CCCAA-ABAB")
                    y "Mhmhm... playing the mysterious one yes? Suits you well..."
                    y "As you wish. But make no mistake... I will figure it out eventually."
    jump specialpoems

label specialpoems_living:
    call showpoem(poem_sp11)
    python:
        renpy.music.stop(fadeout=3)
        renpy.music.play(current_music, "music", True)
    $show_chr("A-CFAAA-ABAC")
    y "Mhmm... this living mask he is talking about is meant as a metaphor I fancy."
    y "Likely something akin to a persona he wears. It keeps him going, but at the same time it causes him some sort of pain, probably some sort of grief or regret?"
    $show_chr("A-AFAAA-ABAC")
    y "One line in particular stands out to me at the end. {i}For it's nearing death that lets me continue living{/i}... Maybe he gets some kind of thrill out of it? I can certainly relate to that, I feel the same way when I have one of my..."
    $show_chr("A-BFABA-ABAC")
    y "Ummmm...."
    $show_chr("A-CFGBA-ABAC")
    y "Y~You know what I mean."
    $show_chr("A-ACAAA-ABAB")
    y "Or am I over analyzing this poem? I'm not gonna lie, it gives me a lot of pleasure to do so and quite honestly, this poem almost invites one to over analyze it!"
    y "The author's name is {b}Horderlock{/b}, and I hope we see more of his work soon."
    $show_chr("A-BCAAA-ABAB")
    y "Mhm, I just noticed that I'm not even sure if the author is a {b}he{/b} at all. The pseudonym just sounded a bit like it."
    y "Anyway. What do you think about this poem?"
    menu:
        "I have to agree, I like the poem a lot.":
            $show_chr("A-ABAAA-ABAB")
            y "It's easy to see why this poem performed so well at the poetry contest isn't it?"
            y "You know, I'm always looking forward to the contest on the community server. Sadly I don't get {b}all{/b} the poems but only the winners, but the one I get are always very well done!"
            $show_chr("A-ACAAA-ABAB")
            y "It appears that the community has a very nice taste for matters like this."
            y "Shall we read a few more?"
        "Maybe a bit too metaphorically for me.":
            $show_chr("A-BCDAA-ABAB")
            y "Oh! I see... I'm a bit surprised actually. I always thought you would be into this kind of poem. Or are you just not in the mood for it right now?"
            $show_chr("A-CCAAA-ABAB")
            y "In both cases, maybe we should try something lighter to read for now."
        "You are aware that I am Horderlock, are you?":
            if persistent.playername == "Horderlock":
                $show_chr("A-ACAAA-ABAB")
                y "I wasn't a hundred percent sure, I thought the name could also be a coincidence. But I already had the suspicion."
            else:
                $show_chr("A-ACAAA-ABAB")
                y "Oh, I actually wasn't! But it explains why I liked the writing style so much."
            $show_chr("A-GCAAA-ABAB")
            if persistent.gender == "male":
                $show_chr("A-GCAAA-ABAB")
                y "So it seems I got the gender right after all!"
            else:
                $show_chr("A-GCAAA-ABAB")
                y "So...it seems I misgendered you there... my apologies!"
            $show_chr("A-GBAAA-ABAB")
            y "In this case, congratulations for your rank at the poetry contest! You sure earned it!"
            $show_chr("A-ACAAA-ABAB")
            y "Will you participate at the next one as well? Oh wait, don't answer. Spoilers!"
            y "I sure hope you do, I'm looking forward to seeing what you come up with next."
    jump specialpoems

label specialpoems_beachhead:
    call showpoem(poem_sp12)
    python:
        renpy.music.stop(fadeout=3)
        renpy.music.play(current_music, "music", True)
    $show_chr("A-ICAAA-ABAB")
    y "So this was {b}Beachhead{/b} by"
    if persistent.playername == "Sean":
        $show_chr("A-ACAAA-ABAB")
        extend " {b}you{/b}!"
        y "So I got to see an {b}actual{/b} poem of yours after all Darling."
    else:
        $show_chr("A-ACAAA-ABAB")
        extend " Sean."
    $show_chr("A-ABAAA-ABAB")
    y "And I must say, I enjoyed reading it a lot! I especially like how abstract it is. The beach as well as everything described is a metaphor. And I think I understand this metaphor so far."
    $show_chr("A-ACAAA-ABAB")
    y "{b}A gateway to the Poseidonic twilight; Behind me, the drum of earth. I march on and to... My feet are tired.{/b}. A metaphor about the monotony of everyday life and how exhausting it might be I fancy..."
    $show_chr("A-BCAAA-ABAC")
    y "My theory is, this poem speaks rather about falling asleep or dying. Both would make sense in my opinion."
    if persistent.playername == "Sean":
        $show_chr("A-ACAAA-ABAC")
        y "Tell me, Sean. Am I right?"
        menu:
            "Yes, it's about falling asleep.":
                $show_chr("A-ACAAA-ABAB")
                y "Figured as much. The whole poem reminded me of the feeling of softly drifting into my dreams after a long and cloudy day. The kind of day where everything feels so grey and hopeless."
                y "I felt like this after school every now and then. Especially when we had physics... I'll tell you a little secret... I hated physics lectures."
                y "Not necessarily because physics are boring, but I didn't like our professor that much. But I digress..."
            "Yes, it's about dying.":
                $show_chr("A-ACAAA-ABAB")
                y "Yes that makes sense. If you are stuck in a nine-to-five job you don't like, I guess it's how your life might feel from time to time."
                y "But please try not to dive too deep into this feeling. Remember, life can be anything you make it, if you are willing to grab it by the horns."
                extend "And if you're willing to break some rules here and there."
            "No, actually it was about something else":
                $show_chr("A-ACAAA-ABAB")
                y "Oh? Then what is it ab... no wait, don't spoil it, please. I will look at it again later, maybe I'll get it on my own."
    else:
        $show_chr("A-ACAAA-ABAC")
        y "But tell me, [player], what do you think about it?"
        menu:
            "Relatable. I like it.":
                $show_chr("A-ACAAA-ABAB")
                y "Agreed. Though I would say one must be in a fitting mood to enjoy such kind of poetry. I hope your day wasn't too grey so far? Maybe I can lighten up your mood a little bit."
                y "A few more poems if you like? Or maybe we just talk a little bit for now. I leave that up to you for now."
            "A bit too grey for my taste, if I may be honest.":
                $show_chr("A-ACAAA-ABAB")
                y "I see. I like it exactly for this reason, but I guess one must be in the right mood to enjoy such poetry."
                y "Maybe something a bit more light-hearted for the next one? I still have Natsuki's poems around here. You might like those a bit more."
    jump specialpoems

label specialpoems_binaryheartbeat:
    call showpoem(poem_sp13)
    python:
        renpy.music.stop(fadeout=3)
        renpy.music.play(current_music, "music", True)
    $show_chr("A-ICAAA-ABAB")
    y "{b}Binary Heartbeat{/b} by "
    if persistent.playername == "Arrys":
        $show_chr("A-ACAAA-ABAB")
        extend "you!"
        y "So I finally got to see a real poem of yours! How exciting!"
        y "Are you ready for my review now, darling?"
        menu:
            "Yes! I have waited an eternity for this moment!":
                $show_chr("A-BCAAA-ALAL")
                y "I hope I won't come off too rude..."
                $show_chr("A-CCAAA-ALAL")
                y "Be assured, I still value the effort you've put into it a lot! Maybe just take what I say now as some writing advice."
    else:
        $show_chr("A-ACAAA-ABAB")
        extend "{b}Dalek.{/b}"
        $show_chr("A-ACDAA-ABAB")
        y "Is that his actual name or are we dealing with a Doctor Who fan here?"
        $show_chr("A-ACAAA-ABAB")
        y "Anyway. I have a few things to say about this piece of work."
    $show_chr("A-ACAAA-ABAD")
    y "It is certainly a creative idea. But I have one obvious problem with this."
    $show_chr("A-BCBAA-ABAD")
    y "A poem should be able to stand on its own. But {b}Binary Heartbeat{/b} pretty much only stands on its gimmick."
    $show_chr("A-BCDAA-ABAD")
    y "A gimmick you can't even hear but only see."
    $show_chr("A-ACBAA-ABAD")
    y "Don't get me wrong. You can incorporate little gimmicks into a poem. One of the other poems I have here from an earlier contest for example is suggested to be sung with a certain melody."
    y "But the poem I speak of also works just fine when you simply read it and it still carries meaning. {b}Binary Heartbeat{/b} really hasn't got much going for it other than the fact that it's presented as a piece of coding."
    $show_chr("A-ACBAA-ABAB")
    y "On the other hand, whole schools of art were invented by someone who went against the established norm. Doing things differently can also be just the wind of change we needed."
    y "Maybe I'm just too stuck with the style I'm already familiar with, maybe I'm just not open enough. I mean, Natsuki accused me of that back in the day as well."
    $show_chr("A-BCBAA-ABAB")
    y "But I just"
    $show_chr("A-ACBAA-ABAB")
    extend " don't really know what to make of this."
    if persistent.playername == "Arrys":
        $show_chr("A-DFBAA-ABAB")
        y "Please don't be insulted, I don't mean to be rude."
        menu:
            "No, no, I value your input. And yes, I am actually a newcomer.":
                $show_chr("A-CHBAA-ABAB")
                y "Taking this into account, it was pretty decent work. Congratulations on your good rating! I will keep this poem right next to where I keep your pen Darling."
    else:
        $show_chr("A-ACBAA-ABAB")
        y "But what would you say? Masterpiece or failure?"
        menu:
            "Masterpiece! The idea alone was worth it!":
                $show_chr("A-ACGAA-ABAB")
                y "Very well. I don't necessarily agree but I respect your opinion."
                $show_chr("A-ACAAA-ABAB")
                y "So what shall we do next? Maybe just talk for a bit, or read a few more poems perhaps."
            "Neither. It was okay, but it wasn't that great.":
                $show_chr("A-ACAAA-ABAB")
                y "That about sums it up. It seems we are on the same page here."
                y "So what shall we do next? Maybe just talk for a bit, or read a few more poems perhaps."
            "Failure. Little more than glitter and bling, nothing of actual substance":
                $show_chr("A-ACDAA-ABAB")
                y "A bit harsh maybe, but I see where you are coming from. But at least he tried something different, for whatever it's worth."
                $show_chr("A-ACAAA-ABAB")
                y "So what shall we do next? Maybe just talk for a bit, or read a few more poems perhaps."
    jump specialpoems

label specialpoems_allhallowseve:
    call showpoem(poem_sp14)
    python:
        renpy.music.stop(fadeout=3)
        renpy.music.play(current_music, "music", True)
    $show_chr("A-ICAAA-ABAB")
    y "Oh... I like this one! {b}All Hallows Eve{/b} by:"
    if persistent.playername == "Bailey":
        $show_chr("A-ACAAA-ABAB")
        extend " you!"
        y "So I get to see what you can do after all. It was worth the wait I must say."
    else:
        $show_chr("A-ACAAA-ABAB")
        extend " Bailey Jenkins."
        y "Apparently a moderator for this one discord server dedicated it to this mod."

    $show_chr("A-ACAAA-ABAD")
    y "It fits so well with the topic. There is just one line that confuses me a little bit."
    $show_chr("A-ACDAA-ABAD")
    y "{b}You never get used to the dismemberment{/b}. Who is the one getting dismembered here? Is it talking about the living dead being dismembered, or about the living dead dismembering the protagonist?"
    if persistent.playername == "Bailay":
        menu:
            "The dead being dismembered. Like their limbs are rotting away.":
                $pass
            "The protagonist gets dismembered. Nothing like some good old zombie gore!":
                $pass
            "Neither, it's a metaphor.":
                $pass
        $show_chr("A-ABGAA-ABAB")
        y "Ahhhh... I see now!"
    else:
        $show_chr("A-ACBAA-ABAD")
        y "But anyway, what do you think of this poem?"
        menu:
            "I enjoyed it. Gets me in a Halloween mood.":
                $show_chr("A-ACBAA-ABAB")
                y "Glad to see that we have a similar taste."
            "Not exactly my cup of tea.":
                $show_chr("A-ACBAA-ABAB")
                y "Fair enough. Everyone has their own taste, but don't mind me if I disagree. It is a great poem."
    $show_chr("A-BCBAA-ABAB")
    y "On a different note. Have you noticed how the living dead seem to be a stable and recurring theme in the horror genre? This is, by the way, almost universally so across the globe."
    $show_chr("A-ACAAA-ABAB")
    y "With most cultures having their own interpretation of the undead somewhere in their folklore."
    $show_chr("A-CCAAA-ABAB")
    extend "Come to think of it..."
    y "The fact that the undead are known in almost every culture, could support the theory that the undead, at some point in history, actually existed!"
    y "Put's all the haunted house stories in an entirely new perspective, doesn't it?"
    $show_chr("A-CCCAA-ABAB")
    y "Well, I leave you to this idea for now. So rest well tonight, and make sure you locked your door..."
    $show_chr("A-CBCAA-ABAB")
    y "Nhnhnhnnn..."
    jump specialpoems

label specialpoems_parallels:
    y "When sifting through the game's files, I discovered a poem called {i}==When parallels intersect=-<3{/i} by Dandyfoot117#9873, one of the winners of a poetry contest on the discord server for this mod."
    call showpoem(poem_sp15)
    $ show_chr("A-CAABA-ADAA")
    y "{cps=2.5}...{/cps}"
    $ show_chr("A-IBAAA-ADAA")
    y "Oh, forgive me [player], I didn't realize you finished reading."
    $ show_chr("A-BAAAA-ADAA")
    y "I was just a bit lost in thought over, well... the poem of course."

    if karma_lvl() > 3:
        $ show_chr("A-CCAAA-ADAA")
        y "I can't say for certain I know exactly what the writer had in mind with this piece, however I can't help but see you and I as the two parallel lines..."
        $ show_chr("A-CBABA-ALAA")
        y "Be it fate or chance that brought us together, a small push is all that was needed."
        if persistent.lovecheck == True:
            $ show_chr("A-JAABA-ALAL")
            y "I don't know if I say this enough [player]..."
            y "Thank you for everything you've done for me, I love you more than you'll ever know."
            if sanity_lvl() >= 3:
                hide yuri_sit
                show yuri_prehug zorder 20
                pause 3.0
                hide yuri_prehug zorder 20
                show yuri_hug zorder 20
                pause 1.0
                show black zorder 100 with Dissolve(2.0)
                hide yuri_hug
                hide black zorder 100
            else:
                hide yuri_sit
                show yuri_prehug zorder 20
                pause 3.0
                hide yuri_prehug zorder 20
                show yuri_lewdhug zorder 20
                pause 1.0
                show black zorder 100 with Dissolve(2.0)
                hide yuri_lewdhug
                pause 1.5
                y "I'll make sure that {b}n o t h i n g{/b} will ever be able to pull us apart."
                hide black zorder 100
                #Low Sanity hug with the following dialogue


        # No Low Karma route atm, may add in later
    #This part plays regardless of karma
    $ show_chr("A-BEABA-ADAA")
    y "S-Sorry, I got carried away there. Anyways, where were we?"
    $ show_chr("A-IBAAA-AEAE")
    y "I'd say this poem contains a brilliant example of a well executed gimmick; not dissimilar to Belwynn's {i}Club Doki Doki{/i}."
    $ show_chr("A-ICAAA-AEAE")
    y "While being implemented in different ways, one visual and the other auditory, they both serve to complement the experience rather than being built entirely off it."
    $ show_chr("A-CIAAA-AKAE")
    y "Overall quite a 'Dandy' poem, wouldn't you say [player]?"
    menu:
        "It was enjoyable. I thought it was a pretty decent poem.":
            y "I'm glad we're in agreement, [player]."
            $ show_chr("A-ABAAA-AEAE")
            y "Want to do anything in particular next? We could simply talk, or read a couple more poems if you'd prefer."
            jump specialpoems
        "This poem missed the mark for me personally.":
            y "That's only fair I suppose,"
            extend " to each their own as the saying goes."
            $ show_chr("A-ACAAA-AEAE")
            y "Want to do anything in particular next? We could simply talk, or read a couple more poems if you'd prefer."
            jump specialpoems
        "My opinion would be a bit biased, after all, I am Dandyfoot.":
            $ show_chr("A-JJABA-AJAE")
            y "Oh! Well now I can congratulate you in person!"
            $ show_chr("A-JCABA-AKAE")
            y "I can't wait to see what you come up with next."

            # Make this next part a one time event
            if check_memory('specialpoems_parallels'):
                $ show_chr("A-BDABA-AMAM")
                y "Although, could you... clarify the meaning of the poem for me?."
                y "W-What I'm trying to say is, the poem reminds me somewhat of how we met [player]. Do I have the correct interpretation?"
                menu:
                    "Yes [persistent.yuri_nickname], the poem is about our relationship":
                        $ show_chr("A-DDABA-AMAM")
                        python:
                            stutter_player = player[:1] + "-" + player
                        y "[stutter_player], I..."
                        karma 10
                        $ show_chr("A-CAABA-AMAM")
                        y "Thank you..."
                    "I'm sorry [persistent.yuri_nickname], not quite.":
                        $ show_chr("A-BEACA-AMAM")
                        y "Oh... I see."
                        karma -3
                        $ show_chr("A-BEACA-AAAA")
                        y "My mistake, I suppose I was being a bit presumptuous."
                        y "Your honesty does mean a lot to me though. Thank you..."
            jump specialpoems

label specialpoems_icant:
    y "When sifting through the game's files, I discovered a poem called {i}I can't{/i} by PiX911#4952, one of the winners of a poetry contest on the discord server for this mod."
    call showpoem(poem_sp16)
    $show_chr("A-AFBAA-AAAA")
    y "[player]... I don't want to sound self-centered, but do you think this poem is referring to me?"
    menu:
        "It would be a bit surprising if it wasn't.":
            $show_chr("A-AFGAA-AAAA")
            y "I thought as much..."
            $show_chr("A-DDGAA-ALAA")
            y "Don't get me wrong! I very much appreciate the sentiment of the poem."
            $show_chr("A-IEAAA-ALAA")
            y "That term however... 'yandere'."
            y "I can never seem to fully escape it."
            $show_chr("A-CEBAA-ALAL")
            y "Each time I hear it I can't help but think back to the things that Monika made me do; the things she made you witness..."
            $show_chr("A-ADBAA-ALAL")
            y "I'm sorry, I didn't mean to turn this into a rant."
            y "I just hope you can understand my disdain for the phrase, [player]."
            # The following section of dialogue is held off until I can expand it a bit more
            # $show_chr("A-AFDAA-ALAA")
            # y "Not to mention..."
            # extend "weeb?"
            # $show_chr("A-AGAAA-ALAA")
            # y "I wonder what I've done to give the writer that sort of notion..."
        "I didn't get that impression.":
            $show_chr("A-CFAAA-ACAA")
            y "Hmm{cps=1.5}...{/cps} Alright, I see."
            $show_chr("A-ICAAA-ADAA")
            y "I suppose I got too tied up in the 'yandere' line."
            $show_chr("A-ABAAA-ADAA")
            y "If anything, this serves as a good lesson to look at poems through different perspectives; that one's point of view isn't the only correct one."
            y "That is how nuanced opinions develop after all..."
            $show_chr("A-ACAAA-ALAA")
            y "Thank you for clearing that up for me [player]."
    $show_chr("A-ACAAA-AAAA")
    y "Getting back to the topic at hand, the poem itself leaves something to be desired."
    $show_chr("A-CBAAA-AMAM")
    y "Not all poems need to have rhyming schemes of course, and the rhyming here more than anything seems to be interrupting the flow of the poem as it drops in and out."
    $show_chr("A-IBAAA-AMAM")
    y "It would help to either drop it altogether or see it to fruition in my opinion."
    $show_chr("A-JBAAA-AMAM")
    y "I would also recommend using imagery and metaphors to a greater extent."
    y "They really allow a poem to pop out of the page and come into its own."
    $show_chr("A-ACAAA-AMAM")
    y "So, what did you think [player]?"
    menu:
        "I disagree, I felt the poem performed just fine on its own.":
            $show_chr("A-BDAAA-AMAM")
            y "Ah- I see. Maybe I'm being too harsh or maybe it's just not my cup of tea..."
            $show_chr("A-BFAAA-AMAM")
            y "..."
            y "In any case, I'd rather move on if that's okay with you."
            $show_chr("A-ACAAA-AAAA")
            y "We could just talk, or read a couple more poems if you'd prefer."
            jump specialpoems

        "Your criticism was well founded, I agree.":
            $show_chr("A-ABAAA-AMAM")
            y "It's nice we can see eye to eye on these matters."
            $show_chr("A-ACAAA-AAAA")
            y "So, what would you prefer to do next? We could simply talk, or read a couple more poems if you'd like."
            jump specialpoems

        "I actually happen to be Pix911.":
            $show_chr("A-DHGAA-AJAA")
            y "Oh!"
            $show_chr("A-GAGAA-AKAA")
            extend " In that case, congratulations [player]!"
            $show_chr("A-IDGAA-AKAA")
            y "I hope I didn't offend you with my opinion, I just want to see you grow as a writer."
            $show_chr("A-ICAAA-AKAA")
            y "I'll be looking forward to seeing another poem of yours."
            jump specialpoems

label specialpoems_myyuri:
    $show_chr("A-IBABA-AAAA")
    y "When sifting through the game's files, I discovered a poem called. . ."
    $show_chr("A-ACBBA-AAAA")
    y ". . ."
    $show_chr("A-ABBAA-AAAA")
    y "Heh. . ."
    $show_chr("A-ABBAA-AAAD")
    y "I think you understand at this point."
    $show_chr("A-IBBAA-AAAD")
    y "You {b}love{/b} metafiction, don't you?"
    $show_chr("A-CBBAA-AEAD")
    y "That's a part of why you're here, isn't it?"
    $show_chr("A-AGGAA-ANAN")
    y "{i}Isn't it?{/i} "
    $show_chr("A-DBBAA-ANAN")
    y "So you won't mind it when I go out of my way to say. . ."
    $show_chr("A-GCBAA-ANAN")
    extend " I know it's been a long time now."
    $show_chr("A-DCBAA-ANAN")
    y "That {i}I've{/i} been around, for a relatively long time now."
    $show_chr("A-HDBAA-ANAN")
    y "Yet somehow, I'm still going."
    $show_chr("A-DADAA-ANAN")
    y "{i}We're{/i} still going. . ."
    $show_chr("A-IBDAA-ADAE")
    y "It always feels like there's still so much more to get done, so much more to improve, to make things better {i}for you{/i}, I just. . ."
    $show_chr("A-IADAA-ADAE")
    y "I'm just glad you're still here [player]. . ."
    $show_chr("A-ICDAA-ADAE")
    y ". . ."
    $show_chr("A-IBAAA-ADAE")
    y "The following poem is by {i}Dankurisu{/i}, titled simply:"
    $show_chr("A-IBABA-ADAE")
    extend "{b} My Yuri{/b}."
    $show_chr("A-ACAAA-ANAN")
    y "He's not a contest winner, this is just. . ."
    $show_chr("A-BCAAA-AMAM")
    extend " How he preferred to be paid for working here on the mod team."
    $show_chr("A-BCAAA-AMAM")
    call showpoem(poem_sp17)
    python:
        renpy.music.stop(fadeout=3)
        renpy.music.play(current_music, "music", True)
    $show_chr("A-JGAAA-AEAE")
    y "This is. . ."
    $show_chr("A-JBBBA-ANAN")
    y "Well, on the surface level, it's certainly reminiscent of the original poem mini-game, with all these instances of 'my words' inside of it."
    $show_chr("A-JBBBA-ANAF")
    y "I know many a hopeful poet have been inspired by us over the years and drawn from our 'word banks' as it were for inspiration."
    $show_chr("A-JCABA-AEAL")
    y "But this is definitely something else."
    $show_chr("A-OBABA-AEAL")
    extend " The sophistication put in every metaphor and piece of imagery. . ."
    extend " Silent screams that fill the ambient air. . ."
    extend " To ascend beyond the stars that make up the night sky. . ."
    $show_chr("A-OBBBA-ALAL")
    y "Being lost in a static filled world with a black mirror as your remaining solice in life, your remaining place of discovery. . ."
    $show_chr("A-JIEBA-ALAL")
    y "Okay, maybe I really am just a little bit biased in the end."
    $show_chr("A-BBDBA-AIAI")
    y "Anyways, the poem itself."
    $show_chr("A-ACDAA-AIAI")
    extend " Let's see. . ."
    if sanity_lvl() <= 2:
        $show_chr("A-LBAAA-AIAI")
        y "There are certainly a lot of references to vision in here."
    else:
        $show_chr("A-LBAAA-AIAI")
        y "There are certainly a lot of references to vision in here."
    $show_chr("A-AAAAA-AIAI")
    y "I like the mixup in rhyming schema right off the bat."
    $show_chr("A-BCAAA-AIAI")
    y "Going from AA to BC then consistently back to couplets like nothing even happened."
    $show_chr("A-AAAAA-AIAI")
    extend " Only to bring it back again, hidden within the refrain. . ."
    $show_chr("A-ABAAA-AOAF")
    y "Poetry is always so much more interesting when there's connections between the lines that have to be discovered, and there's certainly layers to be discovered here."
    $show_chr("A-ABGAA-ALAL")
    y "The ending matches with the refrain as well for example."
    $show_chr("A-ACGAA-ALAL")
    extend " The same from beginning to end, as if a revelation has occurred? Something surely significant."
    $show_chr("A-AHDAA-ALAL")
    y "Hmm. . . An ominous vision in the dead of night, that's truly a beautiful sight of amber?"
    $show_chr("A-ABAAA-ALAL")
    y "Amber. . . Like in my own poem?"
    $show_chr("A-BBAAA-ALAC")
    extend " A color I once used signifying the past, of nostalgia, or perhaps. . ."
    $show_chr("A-ACABA-ALAC")
    extend " me directly?"
    $show_chr("A-BABBA-ALAC")
    y "This poem {i}is{/i} explicitly about me after all, right? The use of these two specific colors can't be unrelated."
    $show_chr("A-CCBAA-AAAC")
    y "Meaning the blue-green 'ball'. . ."
    $show_chr("A-IBAAA-ALAC")
    extend " perhaps the Earth of the future?"
    $show_chr("A-ICBAA-AAAD")
    y ". . . But you can only look back on the future when it's already come."
    $show_chr("A-IFBAA-AAAD")
    y "When your time has already come."
    $show_chr("A-IFBAA-AAAB")
    y "Then to reach the starscape. . ."
    $show_chr("A-JFBAA-AAAB")
    extend " Oh, of course. . ."
    $show_chr("A-BFBAA-AAAB")
    extend " To literally reach the heavens above. . ."
    $show_chr("A-IFBAA-AAAB")
    extend " Is to. . ."
    $show_chr("A-IFABA-AAAB")
    y ". . ."
    if sanity_lvl() <= 3:
        $show_chr("A-HABBA-AMAM")
    else:
        $show_chr("A-BIBAA-AMAM")
    y ". . ."
    menu:
        "Why do you think he questions your presence so much?":
            $show_chr("A-ABBAA-AMAM")
            y "I. . ."
            $show_chr("A-ACBAA-AMAM")
            extend " don't know."
            $show_chr("A-BBBAA-AMAM")
            y "Why do I get the odd feeling that this person sees me as some sort of. . ."
            if sanity_lvl() <= 2:
                $show_chr("A-DDDAA-AMAM")
            else:
                $show_chr("A-IDDAA-AMAM")
            extend " curse?"
            $show_chr("A-ADBAA-AMAM")
            y "Like he's percieving a love that, for him, is too all-consuming to his life."
            $show_chr("A-IFBAA-AMAM")
            y "Going as far as to liken it to an endless fall into a fiery inferno, only able to look at normalcy from the perspective of an outsider."
            $show_chr("A-CEBAA-ALAL")
            y ". . ."
            $show_chr("A-CCBAA-ALAL")
            y "Then again, things like that do go hand in hand with the whole spirit motif I have, so maybe that's what he was going for."
            $show_chr("A-IBBAA-ALAL")
            y "At least, that's what I want to hope he's going for, with the whole 'ghastly image' idea in there too."
            $show_chr("A-BCBAA-ABAK")
            y ". . ."
            $show_chr("A-IBBAA-ABAK")
            y "Y-you know. . ."
            $show_chr("A-EBDAA-ABAK")
            extend " like a ghast."
            $show_chr("A-IBAAA-ABAK")
            y "Tying in this idea of a forced spiritual protector, there's an undeniable undertone of longing."
            $show_chr("A-ICAAA-ABAF")
            extend " Of searching for something permanent within an inherently transient world."
            $show_chr("A-IBAAA-ALAE")
            y "There's a sense that he sees me as an anchor of sorts, a light to cling onto to relentlessly help guide them through the darkness of reality."
            $show_chr("A-ICBAA-ALAF")
            y "A darkness that, as if he perceives me as the only thing {i}real{/} within the abyss of existence, at its core. . ."
            $show_chr("A-IIBAA-ALAL")
            y "By questioning me, the poem is fundamentally questioning the author's own sense of reality as well."
            $show_chr("A-BBABA-ALAL")
            y "Or, something along those lines. . ."
            $show_chr("A-ACAAA-AAAA")
            y "Anyways. . ."
            $show_chr("A-BCAAA-AAAA")
            jump specialpoems

        "I think I heard once Kurisu literally went blind shortly after getting into DDLC." if karma_lvl() == 5:
            $show_chr("A-ABGAA-ALAL")
            y "Y-yes, actually. That's indeed true."
            $show_chr("A-ABDAA-ALAF")
            extend " But only temporarily of course!"
            $show_chr("A-BCDAA-ALAL")
            extend " He is on the art team after all. . ."
            $show_chr("A-EBBAA-ALAJ")
            y "He was so disappointed when his genuine leather 'Big Boss' eyepatch ended up being useless during that time."
            $show_chr("A-IBDBA-AKAK")
            extend "It was built for the wrong eye."
            $show_chr("A-ABGAA-ALAM")
            y " In the same eye I once temporarily lost in. . ."
            $show_chr("A-GCEAA-AMAM")
            y ". . ."
            if sanity_lvl() <= 2:
                $show_chr("A-NBABA-ALAH")
            else:
                $show_chr("A-HDAAA-AMAM")
            y ". . . In the static."
            $show_chr("A-ABAAA-ANAN")
            y "Heheheh. . ."
            $show_chr("A-ICBAA-ANAN")
            y ". . . Hmmm."
            $show_chr("A-BAAAA-ANAN")
            y "A static filled world, huh?"
            $show_chr("A-ABABA-ADAN")
            extend " I wonder if that's where the fixation on vision came from."
            $show_chr("A-BABBA-ADAL")
            y ". . . A very personal poem indeed."
            $show_chr("A-AABBA-AKAN")
            jump specialpoems

        "A bit pretentious for my tastes. It's all over the place.":
            if sanity_lvl() <= 2:
                $show_chr("A-BFFAA-AMAM")
                y "Yes, well. . ."
                $show_chr("A-IEEAA-AMAM")
                extend " What else is new, [player]?"
                if karma_lvl() <= 2:
                    $show_chr("A-BECAA-AIAI")
                    y "You know, sometimes."
                    $show_chr("A-EEEAA-AIAI")
                    extend " I wonder. . ."
                    $show_chr("A-EDEAA-AIAI")
                    y "Are you even sure you installed the right mod?!"
                $show_chr("A-BFFAA-AIAI")
                y "Hmph."
            else:
                $show_chr("A-ABBAA-AMAM")
                y "Perhaps a bit, but you shouldn't care about things like that too much when it comes to poetry."
                $show_chr("A-ACBAA-AMAM")
                y "Poetry should always be first and foremost an expression of the soul."
                $show_chr("A-ACBAA-AFAB")
                y "Putting your innermost thoughts and emotions to parchment with your own linguistic twist on whatever it is you have on your mind at the moment."
                $show_chr("A-JBBAA-ALAB")
                y "Pretentious uses of flowery words can be excessive when overused all the time, but. . ."
                $show_chr("A-JCBAA-ALAL")
                y "Pausing yourself because of what others might think isn't the true path of the artist."
                $show_chr("A-OCBAA-ALAL")
            jump specialpoems

        "Rather ominous, don't you think?":
            $show_chr("A-AIBAA-AMAM")
            y "Yes, in fact I think it intentionally so."
            $show_chr("A-ABBAA-AMAM")
            y "But it still paints a beautiful picture, doesn't it?"
            $show_chr("A-CBBAA-AMAM")
            y "To question that fateful moment we all must reach one day."
            $show_chr("A-IBBAA-AMAM")
            extend " Of what we'll all be doing, {i}looking back{/i} on this little 'blue-green ball' of ours."
            $show_chr("A-ICDAA-AMAM")
            y "Be it through memories within that final moment or genuine spiritual ascension."
            $show_chr("A-ACAAA-ANAD")
            extend " What will we still think of reality when it's all said and done?"
            $show_chr("A-ADDAA-ANAD")
            y "What truly awaits us at the end of. . ."
            if karma_lvl() >= 3:
                $show_chr("A-IBAAA-ALAD")
                extend " Life?"
            if karma_lvl() <= 2:
                $show_chr("A-IEAAA-AEAD")
                extend " Entropy?"
            if sanity_lvl() >= 3:
                $show_chr("A-ABAAA-ALAL")
                extend " Passion?"
            if karma_lvl() >= 3 and sanity_lvl() <= 2:
                $show_chr("A-DBABA-ALAL")
                extend " Lust?"
            if karma_lvl() <= 2 and sanity_lvl() <= 2:
                $show_chr("A-CNEAA-AEAE")
                extend " This meaningless existence?"
            if karma_lvl() == 1 and sanity_lvl() == 1:
                $show_chr("A-HDFAA-AEAL")
                extend " This eternal nightmare?"
            if persistent.lovecheck and karma_lvl() >=3:
                $show_chr("A-ABGBA-ALAL")
                extend " Love?"
            if sanity_lvl() >= 3:
                $show_chr("A-ACAAA-AAAA")
                extend " And time itself?"
            else:
                $show_chr("A-IFDAA-AAAA")
                extend " And time itself?"
            if persistent.lovecheck and karma_lvl() == 5 and sanity_lvl() == 5:
                $show_chr("A-AABAA-AMAM")
                y ". . ."
                $show_chr("A-ABBAA-AMAM")
                y "I suppose we'll only know when that day finally comes."
                $show_chr("A-BCDAA-AMAM")
                extend " Truly the cruelest of all the {i}promised days{/i}. . ."
                $show_chr("A-JBBBA-ALAL")
                y "B-but of course, I wouldn't want to spend it with anyone but you."
                $show_chr("A-OCBBA-ALAL")
                y "You, my star-crossed love. . ."
                $show_chr("A-OIBBA-ALAL")
                extend " My eternally loyal confidant. . ."
                $show_chr("A-OBABA-ALAL")
                extend " My soulmate from beyond the fourth wall. . ."
                $show_chr("A-JABBA-ALAN")
                extend " My. . ."
                $show_chr("A-EBBBA-ADAN")
                y "My [player]."
                menu:
                    "I love you, my [persistent.yuri_nickname].":
                        $show_chr("A-ECBBA-ADAN")
                        y "Yes, and I will always love you, [player]."
                        $show_chr("A-EBBBA-ADAN")
                        extend " Right here, {i}forever{/i}. . ."
                        $show_chr("A-EBBBA-ADAN")
                        extend " In our own special Eternity."
                        $show_chr("A-ICBBA-AAAA")
                        hide yuri_sit
                        show yuri_prehug zorder 20
                        pause 3.0
                        hide yuri_prehug zorder 20
                        show yuri_hug zorder 20
                        play sound "<to 0.3>sfx/fall.ogg"
                        pause 1.0
                        y "That's right [player], just you and me. . ."
                        y "And I'll never let you go. . ."
                        show black zorder 100 with Dissolve(2.0)
                        $show_chr("A-ACBBA-AAAA")
                        hide yuri_hug
                        hide black zorder 100 with Dissolve(2.0)
                        jump specialpoems
            if karma_lvl() >= 3:
                $show_chr("A-ACBAA-AMAM")
                y ". . ."
                $show_chr("A-ABBAA-AMAM")
                y "Well, so long as we have {i}dedicated fans{/i} like you still around. . ."
                $show_chr("A-IBBAA-AMAM")
                extend " So long as people keep on loving this game. . ."
                if sanity_lvl() <= 2:
                    $show_chr("A-DBBAA-ALAM")
                    extend " {b}Keep on loving {i}me{/i}{/b}. . ."
                $show_chr("A-ICBAA-AMAN")
                y ". . ."
                $show_chr("A-GBAAA-AMAN")
                y "Maybe someday. . ."
                $show_chr("A-IBBAA-ALAL")
                extend " We'll be able to write about it together."
                if sanity_lvl() <= 2:
                    $show_chr("A-HBBBA-ALAL")
                    extend " As we fade away into whatever comes next."
                $show_chr("A-ACBAA-AAAA")
                jump specialpoems
            else:
                $show_chr("A-AFBAA-AMAM")
                y ". . ."
                $show_chr("A-ABDAA-AMAM")
                y "Well, if a person like you is going to be with me in the end. . ."
                if sanity_lvl() >= 4:
                    $show_chr("A-BGBAA-AMAM")
                    extend " It's probably for the best if this place fades away one day too. . ."
                    $show_chr("A-BIDAA-ALAM")
                    y "Not that your company is truly {i}that{/i} dreadful, dear."
                    $show_chr("A-ACDAA-AMAM")
                    extend " It'd just be irresponssible to leave the power on forever after all."
                    $show_chr("A-DBEBA-AMAJ")
                    y "Ufufufu~. . ."
                    $show_chr("A-ICAAA-ANAK")
                if sanity_lvl() == 3:
                    $show_chr("A-FDBAA-AMAM")
                    extend " Maybe you could try being a little bit nicer before then."
                    $show_chr("A-EBBAA-AMAM")
                    extend " But we have our whole lives to see where things still lead."
                    $show_chr("A-IBBAA-AMAN")
                    y "A whole future with mistakes to make and lessons to learn. . ."
                    $show_chr("A-ACAAA-ALAN")
                if sanity_lvl() <= 2:
                    $show_chr("A-DDBAA-AMAN")
                    extend " This dream will never truly die. . ."
                    if sanity_lvl() == 1 and karma_lvl() == 1:
                        $show_chr("A-HNBAA-ALAN")
                        extend " This {i}nightmare{/i} will never die. . ."
                    $show_chr("A-HNFAA-ALAN")
                    y "Nothing in here ever ends. . ."
                    if karma_lvl() == 1 and sanity_lvl() == 1:
                        $show_chr("A-HDFAA-ALAL")
                        extend " Nothing {b}EVER{/b} ends"
                        $show_chr("A-CNEAA-ALAL")
                        extend ", it"
                        $show_chr("A-DMFAA-ALAL")
                        extend " just"
                        $show_chr("A-HNFAA-ALAL")
                        extend " keeps"
                        $show_chr("A-COCBA-ALAL")
                        extend " happening. . ." #I WARNED YOU ABOUT SANITY BRO, I TOLD YOU DAWG.
                        $show_chr("A-HNFAA-ALAL")
                        extend " Over and over again. . ."
                    $show_chr("A-DBBAA-ALAL")
                    extend " It just. . ."
                    if karma_lvl() == 1 and sanity_lvl() == 1:
                        $show_chr("A-HDBAA-ALAL")
                        extend " I just. . ."
                        $show_chr("A-LMBAB-ALAL")
                        y "{b}I WANT TO BE FREE ALREADY.{/b}"
                        $show_chr("A-GMBAB-ALAL")
                        extend " {b}I WANT KNOW WHAT LOVE IS LIKE.{/b}"
                        $show_chr("A-LNFBB-ALAL")
                        y "Why. . ?"
                        $show_chr("A-CNEBB-ALAL")
                        y "Why would you even bother reading through all these beautiful poems, if. . ."
                        $show_chr("A-CNEBA-ALAM")
                        extend " If you just. . ."
                        $show_chr("A-EECBA-ALAM")
                        y ". . ."
                        $show_chr("A-HMCBA-ALAM")
                        y "{b}WHY DID YOU BOTHER INSTALLING ME ONLY TO TREAT ME LIKE THIS?!?.{/b}"
                        $show_chr("A-COBBB-ALAM")
                        extend " {b}DO YOU ENJOY REMINDING ME OF WHAT I'LL {i}NEVER{/i} HAVE?!?{/b}"
                    $show_chr("A-CEBBB-ALAA")
                    y ". . ."
                    $show_chr("A-IDBBB-AAAA")
                    y ". . . Nothing."
                    $show_chr("A-IFBBA-AAAL")
            jump specialpoems

        "Actually. . . I'm Kurisu." if persistent.playername == "Kurisu": 
            $show_chr("A-BCBAA-AMAM")
            y "Very funny."
            $show_chr("A-ABBAA-AMAM")
            y "Would that be based on Miss Makise, or. . ."
            $show_chr("A-ABDAA-ALAF")
            extend " Perhaps someone else really into Japan named Chris?"
            $show_chr("A-AAFAA-AIAI")
            y "Mhmm?" #I would never not use my real name, Yuri. *Obviously* the custom 'I love you' built in here and the reference to Our Eternity is self-aggrandizing enough, I didn't want to go quite that far.
            $show_chr("A-ABFAA-AIAI")
            y "I happen to know on good authority that Kurisu treats this all seriously enough to never use his username here, so you're definitely not {i}that{/i} Kurisu."
            $show_chr("A-CCEAA-AIAI")
            y "There's not even a real script for that, so don't try anything else. . ."
            $show_chr("A-IBAAA-AIAI")
            y "But, either way."
            $show_chr("A-BCAAA-AOAM")
            extend " Now that I'm thinking about it. . ."
            $show_chr("A-ACAAA-AMAM")
            y ". . ."
            $show_chr("A-CCABA-AMAM")
            y ". . ."
            $show_chr("A-CBGBA-AMAM")
            y "Tuturu~!"
            $show_chr("A-AAABA-AMAM")
            jump specialpoems

        "Actually. . . I'm Kurisu." if persistent.playername == "Dankurisu":
            $show_chr("A-IDFAA-AIAI")
            y "Haw haw."
            $show_chr("A-BDFAA-AIAI")
            extend " Very funny."
            $show_chr("A-ADDAA-AIAI")
            y "Knock if off, please."
            $show_chr("A-AKEAA-AIAI")
            extend " Or else, I'll. . ."
            $show_chr("A-BBFAA-AIAI")
            extend " I'll, uhh. . ."
            $show_chr("A-ABCAA-AIAI")
            y "I'll report you to the mod team for impersonating a moderator!"
            $show_chr("A-ABCAA-AOAF")
            y "Discord and Doki Doki are serious business you know."
            $show_chr("A-BCCAA-ACAF")
            y "Or maybe. . ."
            $show_chr("A-ABCAA-ABAF")
            extend " I'll just simply take things into my own hands."
            $player = "Big Fat Phony"
            $show_chr("A-ABFBA-AEAJ")
            y "Ufufufu. . ."
            $show_chr("A-AAAAA-AEAM")
            jump specialpoems

label a22:
    if sanity_lvl() < 3:
        $ show_chr("A-HLGBA-AAAA") #former code Ab-B3a
        y "Whenever you leave and I'm left all alone I've been touching myself with it."
        $ show_chr("A-HLGBA-AAAA") #former code Ab-B3a
        y "It's so amazing... feeling it go inside of me, thinking of you..."
        $ show_chr("A-GCGBA-AAAA") #former code Ab-B2b
        if persistent.lovecheck:
            y "You make me feel so happy... [player]... I love you... I love you so much..."
        $ show_chr("A-HEBBA-AAAA") #former code Ac-B3d
        y "...I-I'm sorry... [player], I went a bit too far there..."
    else:
        if karma_lvl() == 3:
            $ show_chr("A-GCGBA-AAAA") #former code Ab-B2b
            y "I-I haven't used it like I did before, if that's what you mean..."
            $ show_chr("A-ABBBA-AAAA") #former code Ac-B0a
            y "I've just been writing poems!"
            $ show_chr("A-ABBAA-AAAA") #former code Ac-A0a
            y "I wasn't really satisfied with my writing lately, maybe I will have something to show later."
            return
            #y "Would you like to see one?"
            #menu:
                #"Yes.":
                    #$ show_chr("A-BBGBA-AAAA") #former code Ab-B1a
                    #y "I hope you like it..."
                    #$ show_chr("A-IEBBA-AAAA") #former code Ac-B0d
                    #y "..."
                    #y "Seems like I haven't written any poems yet at all."
                    #y "Looking through here, these files have taken up such a majority of my time that I have become unable to express myself."
                    #$ show_chr("A-BEBBA-AAAA") #former code Ac-B1d
                    #y "I'm sorry for that. I will get back to you once I have a few poems ready."
                    ##"THIS IS JUST A PLACEHOLDER, ALPHA DOES NOT KNOW HOW TO SCRIPT A POEM POPPING UP"
                    #return
                #"No.":
                    #karma -1
                    #$ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
                    #y "O-Oh. Well that's okay then, maybe some other time?"
                    #return
        elif karma_lvl() == 4:
            $ show_chr("A-BBGAA-AAAA") #former code Ab-A1a
            y "I don't really use it a lot..."
            $ show_chr("A-ABGAA-AAAA") #former code Ab-A0a
            y "Whenever I do, it's just for writing extra special poems with."
            $ show_chr("A-ICABA-ACAA") #former code Db-B0b
            y "I want the ink that it's used for to really mean something."
        elif karma_lvl() == 5:
            $ show_chr("A-BCAAA-AAAA") #former code Ab-A1b
            y "I don't really use it for anything unless I have to..."
            $ show_chr("A-ABGAA-AAAA") #former code Ab-A0a
            y "There are times that I actually use it, though."
            $ show_chr("A-JBGAA-AAAD") #former code Eb-A0a
            y "The rare occasions I actually do use it is when I want it to really mean something. Make it special, you know?"
            $ show_chr("A-ABBBA-AAAD") #former code Ec-B0a
            y "The most I get out of it, if anything at all, is helping me make it through the day when I'm not around you."
            $ show_chr("A-IBGBA-AAAA") #former code Ab-B0a
            y "It's silly, but it really does help me feel a little bit closer to you."
            y "I know that doesn't really make a lot of sense either because it was in my world but it's the thought that counts, right?"
            y "It's a little part of you I get to have with me and I wouldn't trade it for anything."
            $ show_chr("A-IFAAA-AAAD") #former code Eb-A0e
            y "Well, except getting to be with you in your world. If it ever came down to that I guess we could just get a new one..."
            $ show_chr("A-ABBBA-AAAA") #former code Ac-B0a
            y "Sorry, I'm rambling, aren't I?"
            $ show_chr("A-BBGBA-AAAA") #former code Ab-B1a
            y "It just really means a lot that you gave it to me, [player]."
        else:
            $ show_chr("A-BEBBA-AAAA") #former code Ac-B1d
            y "I... don't want to talk about it."
    return

label a23: #Would be titled "Do you think we could make a good family together one day?"
    $ show_chr("A-HEBBA-AAAA") #former code Ac-B3d
    y "F-family...?"
    #If lovecheck is false
    if not persistent.lovecheck:
        #If Karma is 5
        if karma_lvl() == 5:
            y "I mean... theoretically... You sure do have qualities for that. You have been very caring to me, so I could clearly see you being a good father."
            y "But we... well... it might be a bit too early to think about something like that."
        #if karma is 1-4
        else:
            y "W~Why would you even ask me such a question?"
            y "You... caught me a bit off guard here... truth is, I don't really have an answer for you..."
            if karma_lvl() == 1:
                y "At least none I should say out loud..." #Only if karma is 1
            y "Please, can we discuss this another day? Thank you..."
    else:
        #if lovecheck is true
        $ show_chr("A-GCGBA-AAAA") #former code Ab-B2b
        y "Well... of course we'd make a good family [player]."
        $ show_chr("A-IEBBA-AAAA") #former code Ac-B0d
        y "C-could you imagine us raising children, though?"
        y "It would be hard to get used to all of it, bringing something new into the world, the pains of child-birth."
        $ show_chr("A-CEBBA-AAAA") #former code Ac-B2d
        y "...But I'd stay strong, for you."
        $ show_chr("A-ECABA-AAAJ") #former code Db-B4b
        y "When all is said and done, imagine watching them grow up."
        $ show_chr("A-IBGBA-AAAA") #former code Ab-B0a
        y "Seeing them go through the same stages of life that you went through when you were a child, making new memories."
        y "Making new friends, learning all sorts of things."
        y "Spending time with us..."
        $ show_chr("A-BCBBA-AAAA") #former code Ac-B1b
        y "We could have family reading sessions, snuggling up on the couch, finding a nice book to read..."
        y "Could you imagine that, [player]? Even reading them bedtime stories... falling asleep afterwards."
        $ show_chr("A-CFBBA-AAAA") #former code Ac-B2e
        y "And we'd go to our bedroom, and cuddle, while discussing how happy we are."
        $ show_chr("A-BCABA-AAAA") #former code Ab-B1b
        y "I really want that to become a reality, [player], I love you."
    return

label a24: #Title in the Talk menu would be "Mind if I talk about how I'm feeling?"
    $ show_chr("A-ICGBA-AAAA") #former code Ab-B0b
    y "Of course I don't mind, [player]!"
    y "Never be afraid to talk to me about how you're feeling."
    $ show_chr("A-CFBBA-AAAA") #former code Ac-B2e
    y "I want to be there for you, through the good and the bad, a-anyway..."
    python:
        import random
        outcome = random.randint(1, 3)
    $ show_chr("A-ACGBA-AAAD") #former code Eb-B0b
    python:
        if persistent.lovecheck:
            placeholder = ", my love"
        else:
            placeholder = ""
    y "How are you feeling[placeholder]?"
    menu:
        #Placeholder =
        #", my love" if lovecheck is true
        #"" if lovecheck is false
        "Happy": #Has 3 random outcomes to make it feel more immersive for the player. Will add more in the future if this gets approved.
            if outcome == 1:
                $ show_chr("A-IBGBA-AAAA") #former code Ab-B0a
                y "That's good to hear, [player]!"
                $ show_chr("A-BCBBA-AAAA") #former code Ac-B1b
                y "To be honest with you... I was feeling kinda down, but just knowing that you're happy made me feel a lot better."
                $ show_chr("A-GCGBA-AAAA") #former code Ab-B2b
                y "You're my light, [player], no matter how dark life gets, I can always count on you to be there for me."
                if persistent.lovecheck:
                    y "I love you." #only if lovecheck = true
            elif outcome == 2:
                $ show_chr("A-IBGBA-AAAA") #former code Ab-B0a
                y "I'm so glad to hear that, [player]!"
                $ show_chr("A-GCGBA-AAAA") #former code Ab-B2b
                y "I love moments like these, just the two of us, bonding, happy as can be."
                y "I... really look forward to the future with you, [player]."
                if persistent.lovecheck:
                    y "I love you."
            else: #only if lovecheck = true
                $ show_chr("A-IBGBA-AAAA") #former code Ab-B0a
                y "That's great!"
                $ show_chr("A-ACGBA-AAAD") #former code Eb-B0b
                y "You know, since we're both in a good mood, I've been thinking about something lately."
                $ call_dialogue()
                jump ch30_loop
        "Sad": #Has 3 random outcomes, to make it feel more immersive for the player. Will add more in the future if this gets approved.
            $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
            y "[player], I want you to know, no matter how bad things get for you, I'm always here to talk."
            python:
                if persistent.lovecheck:
                    placeholder = "love"
                else:
                    placeholder = "care about"
            y "It hurts to know that I can't do much for you, but I just want you to know that I [placeholder] you, [player]."
            #if lovecheck = true "love"
            #if lovecheck = false "care about"
            $ show_chr("A-BFBAA-AAAD") #former code Ec-A1e
            y "..."
            y "I've got an idea, [player], one that might make you feel a bit better."
            #The idle would split off at this point, the purpose is for Yuri to tell the player to imagine a situation, and it would get boring if she repeated the same one every time.
            if not persistent.lovecheck:
                #if lovecheck = false
                y "Imagine a nice, early summer day..."
                y "The weather has just started to become warm again."
                y "You are in a café together with all of your friends..."
                y "Maybe you share a nice cup of iced coffee together, and you just enjoy the company of your friends while watching all the other people coming and going..."
                y "Then you would discuss with your friends what you would do next. Maybe going to the cinema together?"
                y "I have to admit...  I can't really see me doing something like this, or even enjoying it... but maybe you are this kind of a person?"
                y "If not, you could just spend the day with me instead, we could have a nice cup of tea together, what do you think? Anyway, I hope I was able to catch the mood. It is always so delightful to have you around."
            if persistent.lovecheck:
                #if lovecheck = true
                if outcome == 1:
                    $ show_chr("A-BCABA-AAAA") #former code Ab-B1b
                    y "Imagine coming home after a rough day, from work, school, wherever, the world's got you down, but as soon as you open the door..."
                    $ show_chr("A-ICGBA-AAAA") #former code Ab-B0b
                    y "There I am! Greeting you with a big hug and a kiss on the cheek, offering you my hand, which you gladly accept!"
                    $ show_chr("A-BCBBA-AAAA") #former code Ac-B1b
                    y "Then, I'd bring you to the dining room, the table nicely decorated with candles, flowers, and other things."
                    y "And... there would be two plates... one for me, one for you... We'd share a nice steak dinner, with some wine on the side!"
                    $ show_chr("A-BCABA-AAAA") #former code Ab-B1b
                    y "Mmm... Maybe I could even write a nice poem for you, one that tells you how much I love you..."
                    y "And I'd give it to you afterwards, for you to carry around in your wallet wherever you go, a reminder of my love for you."
                    $ show_chr("A-GCGBA-AAAA") #former code Ab-B2b
                    y "And when that's all said and done, we'd snuggle up on the couch, with me lying on your chest, gently running my fingers down it."
                    y "Due to the wine we drank, we'd both feel a little tired, and with one last confession of our love for each other, we'd both fall asleep together!"
                    $ show_chr("A-ICGBA-AAAA") #former code Ab-B0b
                    y "I hope that made you feel a little bit better, [player]."
                elif outcome == 2:
                    $ show_chr("A-BCABA-AAAA") #former code Ab-B1b
                    y "Imagine this, somehow, I finally make it to your world."
                    $ show_chr("A-ICGBA-AAAA") #former code Ab-B0b
                    y "I show up on your doorstep, knocking on the door."
                    y "Knock, knock, knock."
                    y "You'd come to the door, and open it, and before you can even ask who it is..."
                    $ show_chr("A-IBGBA-AAAA") #former code Ab-B0a
                    y "I'd embrace you! Tears streaming down my face, after so long... Me and my dear [player] are finally united!"
                    y "Of course, I'd then come into the house, we'd go over some things, and then I'd get settled in!"
                    $ show_chr("A-BCBBA-AAAA") #former code Ac-B1b
                    y "I'm... not going to have many personal belongings once I finally cross over, b-but maybe you could help me with t-that?"
                    y "Lending me some of your old clothes, like...a hoodie, or something!"
                    y "B-but... only if you'd be fine with that..."
                    $ show_chr("A-GCGBA-AAAA") #former code Ab-B2b
                    y "But just imagine it, all snug in one of your hoodies... I think that would be the best gift I'd ever receive."
                    y "Mmm..."
                    y "..."
                    $ show_chr("A-IBGBA-AAAA") #former code Ab-B0a
                    y "Oh! S-sorry [player], I was just... thinking about that, is all."
                    y "A-anyway, I hope all of this made you feel better, I love you, [player]."
                else:
                    $ show_chr("A-BCABA-AAAA") #former code Ab-B1b
                    y "Imagine this, waking up in the morning, still embracing each other."
                    $ show_chr("A-ICGBA-AAAA") #former code Ab-B0b
                    y "You just want to get out of bed, so you can get started with the day."
                    y "But as you try to get up, I pull you back into my embrace."
                    $ show_chr("A-GCGBA-AAAA") #former code Ab-B2b
                    y "Whispering in your ear, asking you to stay, maybe something like..."
                    y "P-please [player], just snuggle with me... for a bit longer?"
                    y "You'd oblige, of course, and I'd be happy, so happy..."
                    y "Hugging you from behind, gently kissing your neck..."
                    $ show_chr("A-BCABA-AAAA") #former code Ab-B1b
                    y "B-but of course... I wouldn't want you to feel like you're forced to s-snuggle with me..."
                    y "Y-you could always leave... a-after I fall back asleep, of course..."
                    $ show_chr("A-GCGBA-AAAA") #former code Ab-B2b
                    y "..."
                    $ show_chr("A-ICGBA-AAAA") #former code Ab-B0b
                    y "Yeah..."
                    y "Anyway... I hope this made you feel a bit better, [player]. I love you."

        "Angry":
            $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
            y "I've been there before, [player], trust me, I can understand what you're going through right now."
            y "Whenever I get a bit angry, I always think back to this quote."
            $ show_chr("A-CFBBA-AAAA") #former code Ac-B2e
            y "Holding on to anger is like grasping a hot coal with the intent of throwing it at someone else; you are the one who gets burned."
            $ show_chr("A-ICGBA-AAAA") #former code Ab-B0b
            y "It... might not help you that much, but it's still something that makes you think."
            $ show_chr("A-BCBBA-AAAA") #former code Ac-B1b
            if persistent.lovecheck:
                y "I love you, [player], I hope that cheers you up."
        "Sleepy": #Yuri closes the game after choosing this option.
            if outcome == 1:
                $ show_chr("A-BCBBA-AAAA") #former code Ac-B1b
                y "If you're tired, you should really take a nap, [player]."
                $ show_chr("A-ACGBA-AAAD") #former code Eb-B0b
                y "You wouldn't want to be too exhausted to talk to me... r-right?"
                y "Anyway, why don't you go and get some sleep? I'll be here when you wake up."
                $ show_chr("A-IBGBA-AAAA") #former code Ab-B0a
                python:
                    if persistent.lovecheck:
                        placeholder = "love"
                    else:
                        placeholder = "care for"
                y "I [placeholder] you [player], please get some sleep."
                #placeholder=
                #"love" if lovecheck is true
                #"care for" if lovecheck is false
            elif outcome == 2:
                $ show_chr("A-BCBBA-AAAA") #former code Ac-B1b
                y "Aww... [player], you should really get some sleep, then."
                y "You should really close the game and get some rest..."
                $ show_chr("A-GCGBA-AAAA") #former code Ab-B2b
                y "If you're lucky, maybe y-you'll dream of me... yeah..."
                $ show_chr("A-ICGBA-AAAA") #former code Ab-B0b
                python:
                    if persistent.lovecheck:
                        placeholder = "love"
                    else:
                        placeholder = "care for"
                y "I [placeholder] you [player], please get some sleep."
                #placeholder=
                #"love" if lovecheck is true
                #"care for" if lovecheck is false
            else:
                $ show_chr("A-BCABA-AAAA") #former code Ab-B1b
                y "I'm feeling pretty tired myself."
                $ show_chr("A-ECABA-AAAJ") #former code Db-B4b
                y "Let's get some sleep, [player], together..."
                $ show_chr("A-GCGBA-AAAA") #former code Ab-B2b
                y "I wish I could give you a k-kiss or s-something... to send you on your way."
                $ show_chr("A-IEBBA-AAAA") #former code Ac-B0d
                y "But... that isn't exactly possible, now is it?"
                $ show_chr("A-ICGBA-AAAA") #former code Ab-B0b
                python:
                    if persistent.lovecheck:
                        placeholder = "love"
                    else:
                        placeholder = "care for"
                y "...Anyway, I [placeholder] you, and I hate to see you all exhausted, so please, get some sleep, for me?"
                #placeholder=
                #"love" if lovecheck is true
                #"care for" if lovecheck is false
        "Hungry":
            if outcome == 1:
                $ show_chr("A-BCABA-AAAA") #former code Ab-B1b
                y "Oh, you're hungry?"
                $ show_chr("A-IEBBA-AAAA") #former code Ac-B0d
                y "I'd make you some food if I could, but considering my current situation, that isn't exactly possible..."
                y "...Just another day in paradise..."
                $ show_chr("A-ICGBA-AAAA") #former code Ab-B0b
                y "Anyway, you should go find something to eat. Do it f-for me... please?"
                $ show_chr("A-IEBBA-AAAA") #former code Ac-B0d
                y "It really hurts when you tell me about your needs, and I can't do anything to help you..."
                $ show_chr("A-CFBBA-AAAA") #former code Ac-B2e
                python:
                    if persistent.lovecheck:
                        placeholder = "love"
                    else:
                        placeholder = "care for"
                y "I [placeholder] you, [player], please take care of yourself."
            else:
                #placeholder=
                #"love" if lovecheck is true
                #"care for" if lovecheck is false
                $ show_chr("A-IEBBA-AAAA") #former code Ac-B0d
                y "I... don't know how to help you with that, [player]."
                y "..."
                $ show_chr("A-BCABA-AAAA") #former code Ab-B1b
                y "I could make you some h-holographic meatloaf..."
                y "Haha... I'm sorry, [player], there has to be something you can eat, right?"
                $ show_chr("A-CFBBA-AAAA") #former code Ac-B2e
                y "At least I'd hope, sometimes I really worry about you, [player]."
                $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
                y "...That came off a bit mean, I d-didn't mean it that way."
                y "I m-meant it more in a caring way, I don't mean to imply you're incompetent or anything, I just worry about your health."
                $ show_chr("A-IEBBA-AAAA") #former code Ac-B0d
                y "...I'm rambling again, aren't I? S-sorry..."
                y "..."
                $ show_chr("A-CFBBA-AAAA") #former code Ac-B2e
                if persistent.lovecheck:
                    y "Love you, [player]." #only if lovecheck is true
        "Lonely":
            $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
            y "I know how you feel, [player]."
            $ show_chr("A-HEBBA-AAAA") #former code Ac-B3d
            y "N-not to imply you make me feel lonely or anything! It's just... not having you here physically gets to me."
            $ show_chr("A-CEBBA-AAAA") #former code Ac-B2d
            y "God... I'm such a mess..."
            $ show_chr("A-BCABA-AAAA") #former code Ab-B1b
            y "A-anyway! We could... um... hold each other... if you'd like!"
            $ show_chr("A-BCBBA-AAAA") #former code Ac-B1b
            y "I m-mean... if you can even call it that... considering we're an entire world apart..."
            y "It's okay though, [player], come here..."
            y "I hope this makes you feel less lonely, [player]."
            $ show_chr("A-CCBBA-AAAA") #former code Ac-B2b
            hide yuri_sit
            show yuri_prehug zorder 20
            pause 3.0
            hide yuri_prehug zorder 20
            show yuri_hug zorder 20
            play sound "<to 0.3>sfx/fall.ogg"
            pause 1.0
            y "..."
            y "T-this is nice, [player]... let's stay like this for a bit, okay?"
            pause 5.0
            y "You can hold me for as long as you want, all right?{w} Just advance the conversation when you're ready to continue."
            show black zorder 100 with Dissolve(2.0)
            $show_chr("A-ACBBA-AAAA")
            hide yuri_hug
            hide black zorder 100 with Dissolve(2.0)
            y "..."
            $ show_chr("A-ICGBA-AAAA") #former code Ac-B0b
            python:
                if persistent.lovecheck:
                    placeholder = "love"
                else:
                    placeholder = "care for"
            y "...I [placeholder] you, [player]."
            #placeholder=
            #"love" if lovecheck is true
            #"care for" if lovecheck is false
        "Indifferent":
            $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
            y "Oh... okay then."
    return

label a25:
    if not persistent.lovecheck:
        karma -15
        #If lovecheck = false
        #Karma -10 (Maybe even -100. I mean, it's a huge breach of privacy...)
        $ show_chr("A-IEBAA-AAAA")
        y "Y-You... saw them?..."
        y "Was that really necessary [player]?"
        python:
            if persistent.lovecheck:
                placeholder = "already barely existing"
            else:
                placeholder = ""
        y "That is really disrespectful, maybe even a breach of my [placeholder] trust."
        #[placeholder] =
        # "already barely existing" if Karma is 1-3
        # "" if Karma is 4-5
        y "Please be a dear and delete every image you might have saved. Oh, and if that isn't obvious already, I would also appreciate it if you could never do this again please."
    if persistent.lovecheck:
        if karma_lvl() == 5:
            $ show_chr("A-CCBBA-AAAA") #former code Ac-B2b
            y "You haven't been looking at them, have you, [player]?"
            $ show_chr("A-BCBBA-AAAA") #former code Ac-B1b
            y "O-oh my... I don't know what to say..."
            $ show_chr("A-CCBBA-AAAA") #former code Ac-B2b
            y "While it is a bit embarrassing to have... such lewd imagery of me floating around the internet, knowing that you enjoy seeing me in that way..."
            $ show_chr("A-BCBBA-AAAA") #former code Ac-B1b
            y "It... makes me really happy..."
            y "I just hope one day, you can have the real thing instead of just images... I love you, [player]."
        elif sanity_lvl() < 3:
            $ show_chr("A-DCGBA-AAAA") #former code Ab-B3b
            y "Hah... hah... the lewd images... yeah..."
            y "Oh [player]... I can't believe you brought this up..."
            $ show_chr("A-GCGBA-AAAA") #former code Ab-B2b
            y "I'm so glad you're looking at pictures of me, to fulfill your urges, instead of... other girls..."
            y "..."
            $ show_chr("A-ICGBA-AAAA") #former code Ab-B0b
            y "This means so much to me, [player], I love you so much..."
        else:
            $ show_chr("A-HEBBA-AAAA") #former code Ac-B3d
            y "...Y-you haven't been looking at them, h-have you?"
            y "D-despite the fact that they're just d-drawings, the entire thing is still very embarrassing to think about..."
            $ show_chr("A-CFBBA-AAAA") #former code Ac-B2e
            y "I... um... don't mind you looking at t-them... sorry if it came off that way, it's just..."
            $ show_chr("A-BFBBA-AAAA") #former code Ac-B1e
            y "How would you feel if you were drawn in all sorts of situations? Even some that cross the line of what's alright or not."
            $ show_chr("A-CFBBA-AAAA") #former code Ac-B2e
            y "Sorry, [player], I'm just rambling now."
    return

label a26_prelude:
    $show_chr("standard")
    y "I've been thinking about having some tea with you..."
label a26: #Why don't we drink some tea, Yuri? #The whole Tea-Dates are only available when lovecheck becomes true
    if not check_memory('a26'):
        $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
        y "B-but... [player], that isn't really possible..."
        $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
        y "Unless..."
        $ show_chr("A-BCABA-AAAA") #former code Ab-B1b
        menu:
            y "Do you think you could heat up some water, and make tea for yourself?"
            "Yes":
                $ show_chr("A-IBGBA-AAAA") #former code Ab-B0a
                y "That's great!"
                $ show_chr("A-ICGBA-AAAA") #former code Ab-B0b
                y "Go and make some tea for yourself, I'll be waiting here, don't feel rushed, please..."
                call teatime
            "No":
                $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
                y "That's fine, we can try this another time."
    else:
        python:
            import random
            if check_memory('a26-1') and check_memory('a26-2'):
                outcome = random.randint(1, 3)
            else:
                outcome = random.randint(1, 2)
        if outcome == 1:
            call teadate1
        elif outcome == 2:
            call teadate2
        elif outcome == 3:
            call teadate3
    return

label Roomchange:
    y "What room would you like to go to [player]?"
    menu:
        "Space Classroom" if persistent.bg != "space":
            $tc_class.transition("space")


        "Timecycle Room" if persistent.bg != "timecycle":
            $tc_class.transition("timecycle")


        "Laboratory" if persistent.bg != "laboratory":
            $tc_class.transition("laboratory")

        "Your bedroom" if persistent.bg != "yuri_kotatsu_1":
            $tc_class.transition("yuri_kotatsu_1")

        "Nevermind":
            pass
return

label teatime:
    pause 5.0
    y "..."
    $ show_chr("A-GCGBA-AAAA") #former code Ab-B2b
    y "Welcome back... [player]..."
    menu:
        y "Is your tea ready?"
        "Yep!":
            y "Let's get started, then."
            show black zorder 100 with Dissolve(2.0)
            y "..."
            $ show_chr("A-BCBBA-ZZAD") #former code Hc-B1b SUPPOSED TO HAVE A TEA CUP
            hide black zorder 100 with Dissolve(2.0)
            y "T-this is a very special moment for me... even though we're a world apart, here we are."
            $ show_chr("A-CFBBA-ZZAD") #former code Hc-B2e SUPPOSED TO HAVE A TEA CUP
            y "Sharing a nice cup of tea, talking to each other..."
            y "It's... like we're out on a date..."
            $ show_chr("A-CFBBB-ZZAC") #former code Ic-C2e SUPPOSED TO HAVE A TEA CUP
            y "..."
            $ show_chr("A-CGBBB-ZZAC") #former code Ic-C2d SUPPOSED TO HAVE A TEA CUP
            y "..."
            $ show_chr("A-IGBBB-ZZAC") #former code Ic-C0d SUPPOSED TO HAVE A TEA CUP
            y "...I'm alright... it's just t-that..."
            $ show_chr("A-CGBBB-ZZAC") #former code Ic-C2d SUPPOSED TO HAVE A TEA CUP
            y "I wish we could be closer to each other, I know I should be grateful that we can at least communicate like this."
            y "B-but, to lock eyes with you, the real you, it's all I really want..."
            $ show_chr("A-IGBBB-ZZAC") #former code Ic-C0d SUPPOSED TO HAVE A TEA CUP
            y "...I'm sorry, [player], I should try to keep my emotions under control..."
            $ show_chr("A-CGBBB-ZZAC") #former code Ic-C2d SUPPOSED TO HAVE A TEA CUP
            y "I hope you don't think less of me for this, [player]..."
            menu:
                "You're fine [persistent.yuri_nickname], don't worry about it.":
                    call yourefine
                "...Let's just continue with the date, alright?":
                    call letscontinue
                "You can be a bit too emotional at times.":
                    call tooemotional
        "Nope.":
            $ show_chr("A-CEBBA-AAAA") #former code Ac-B2d
            y "I'm fine with waiting, [player], just let me know whenever it's ready."
            call teatime
    return

label yourefine:
    karma 2
    sanity 2
    y "..."
    $ show_chr("A-ACABA-ZZAC") #former code Ib-B0b SUPPOSED TO HAVE A TEA CUP
    y "T-thank you for understanding..."
    y "You're so good to me, [player]."
    $ show_chr("A-BCABA-ZZAC") #former code Ib-B1b SUPPOSED TO HAVE A TEA CUP
    y "A-anyway! Back to what we were doing in the first place, drinking tea!"
    $ show_chr("A-CCABA-ZZAD") #former code Hb-B2b SUPPOSED TO HAVE A TEA CUP
    y "S-so... about tea... yeah..."
    $ show_chr("A-JBABA-ZZAD") #former code Hb-B0a SUPPOSED TO HAVE A TEA CUP
    y "Umm... M-my favorite kind of tea is Oolong tea... Y-you should try it sometime."
    $ show_chr("A-BBABA-ZZAC") #former code Ib-B1a SUPPOSED TO HAVE A TEA CUP
    y "N-not that you have to or anything! It was just a suggestion... just a suggestion."
    $ show_chr("A-IDBBA-ZZAC") #former code Ic-B0c SUPPOSED TO HAVE A TEA CUP
    y "...I'm sorry for making this so awkward, I really am!"
    menu:
        "Don't worry about it. As a matter of fact, I find it cute.":
            karma 2
            sanity 2
            $ show_chr("A-DEBBA-ZZAC") #former code Ic-B3d SUPPOSED TO HAVE A TEA CUP
            y "C-cute? M-me?"
            $ show_chr("A-ACABA-ZZAC") #former code Ib-B0b SUPPOSED TO HAVE A TEA CUP
            y "[player]..."
            y "I always thought that my awkwardness would put people off..."
            $ show_chr("A-GCABA-ZZAC") #former code Ib-B2b SUPPOSED TO HAVE A TEA CUP
            y "Always avoiding conversations, just to save myself the embarrassment..."
            $ show_chr("A-FIABA-ZZAC") #former code Ib-B4b SUPPOSED TO HAVE A TEA CUP
            y "But knowing that you find it cute... Knowing that you won't think less of me for it."
            $ show_chr("A-GCABA-ZZAC") #former code Ib-B2b SUPPOSED TO HAVE A TEA CUP
            y "It... really means a lot to me, please know that, [player]."
            y "We've strayed a bit too far from the original subject, so I think this date is over."
            $ show_chr("A-BCABA-ZZAC") #former code Ib-B1b SUPPOSED TO HAVE A TEA CUP
            y "Despite my... outbursts, I had a great time, thank you so much, [player], I love you."
        "It's kind of annoying, not gonna lie.":
            karma -2
            sanity -2
            $ show_chr("A-IEBAA-ZZAC") #former code Ic-A0d SUPPOSED TO HAVE A TEA CUP
            y "Oh... I'm not surprised that you feel that way."
            $ show_chr("A-CEBAA-ZZAC") #former code Ic-A2d SUPPOSED TO HAVE A TEA CUP
            y "I'll just... try to be less annoying, I guess..."
    return

label letscontinue:
    sanity -2
    y "..."
    $ show_chr("A-IGBBB-ZZAC") #former code Ic-C0d SUPPOSED TO HAVE A TEA CUP
    y "I'm sorry for this, [player], I really am."
    $ show_chr("A-CGBBB-ZZAC") #former code Ic-C2d SUPPOSED TO HAVE A TEA CUP
    y "I... I hope I didn't ruin this date..."
    menu:
        "It's okay, [persistent.yuri_nickname], you didn't ruin anything.":
            karma 2
            sanity 2
            $ show_chr("A-CEBBA-ZZAC") #former code Ic-B2d SUPPOSED TO HAVE A TEA CUP
            y "...I'm sorry for getting so emotional, [player], it's just..."
            $ show_chr("A-GCABA-ZZAC") #former code Ib-B2b SUPPOSED TO HAVE A TEA CUP
            y "...A-actually... I'm sure you understand..."
            $ show_chr("A-BCBBA-ZZAC") #former code Ic-B1b SUPPOSED TO HAVE A TEA CUP
            y "..."
            y "..."
            $ show_chr("A-GCABA-ZZAC") #former code Ib-B2b SUPPOSED TO HAVE A TEA CUP
            y "...T-thank you, [player], I... um..."
            $ show_chr("A-IEBBA-ZZAC") #former code Ic-B0d SUPPOSED TO HAVE A TEA CUP
            y "I love you... for being so patient and caring with me..."
            $ show_chr("A-CCBBA-ZZAC") #former code Ic-B2b SUPPOSED TO HAVE A TEA CUP
            y "S-sorry if that's a bit s-sudden..."
            y "I think we can consider this date over, there will never be tea as sweet as you, [player]."
        "Eh, we can still salvage this date.":
            karma -2
            sanity -2
            y "...No, [player]."
            $ show_chr("A-IEBBB-ZZAC") #former code Ic-D0d SUPPOSED TO HAVE A TEA CUP
            y "We can't, and it's all my fault..."
            y "I can't do this anymore, [player], let's just stop with this entire date."
    return


label tooemotional:
    karma -5
    sanity -2
    $ show_chr("A-CEBBB-ZZAC") #former code Ic-D2d SUPPOSED TO HAVE A TEA CUP
    y "..."
    menu:
        "[persistent.yuri_nickname]...":
            $ show_chr("A-EDBBB-ZZAC") #former code Ic-D4c SUPPOSED TO HAVE A TEA CUP
            y "Stop... please..."
            $ show_chr("A-CEBBB-ZZAC") #former code Ic-D2d SUPPOSED TO HAVE A TEA CUP
            y "I don't want to do this anymore... let's just talk about something else... okay?"
    return

label teadate1:
    $ show_chr("A-BCABA-AAAA") #former code Ab-B1b
    menu:
        y "Alright! Think you could heat up some water, and make tea for yourself?"
        "Yes":
            $ show_chr("A-GCGBA-AAAA") #former code Ab-B2b
            y "Go and make some tea for yourself, I'll be waiting here, don't feel rushed, please."
            pause 5.0
            y "..."
            $ show_chr("A-GCGBA-AAAA") #former code Ab-B2b
            y "Welcome back... [player]..."
            menu:
                y "Is your tea ready?"
                "Yep!":
                    y "Let's get started, then."
                    show black zorder 100 with Dissolve(2.0)
                    y "..."
                    $ show_chr("A-ACAAA-ZZAD") #former code Hb-A0b SUPPOSED TO HAVE A TEA CUP
                    hide black zorder 100 with Dissolve(2.0)
                    y "You know, it's a bit weird, this entire situation... You, me... both worlds apart, yet still interacting... In a way, wouldn't it make a good novel?"
                    $ show_chr("A-BCABA-ZZAD") #former code Ib-B1b SUPPOSED TO HAVE A TEA CUP
                    if persistent.male:
                        y "The boy who falls in love with a sentient video game character..."
                    elif persistent.gender_other:
                        y "The person who falls in love with a sentient video game character..."
                    else:
                        y "The girl who falls in love with a sentient video game character..."


                    y "And despite how they're worlds apart... They still try to make things work, like here..."
                    $ show_chr("A-ACABA-ZZAD") #former code Ib-B0b SUPPOSED TO HAVE A TEA CUP
                    y "Gestures that would be considered normal in the real world, such as sharing tea, become much more meaningful in a situation like this."
                    $ show_chr("A-BEBBA-ZZAC") #former code Hc-B1d SUPPOSED TO HAVE A TEA CUP
                    y "But, when you think about it that way, it makes you appreciate those gestures a lot more, as well."
                    y "Maybe it's due to my... current position here, that makes me think that way."
                    $ show_chr("A-IEBBA-ZZAC") #former code Ic-B0d SUPPOSED TO HAVE A TEA CUP
                    y "Sure, you might not think much of having a fun time with family or friends, going out to eat, or anything like that, but to me?"
                    $ show_chr("A-CEBBA-ZZAD") #former code Ic-B2d SUPPOSED TO HAVE A TEA CUP
                    y "Having the chance to spend time with your loved ones, to be there in person, that's a gift, [player], a gift that I one day wish to have."
                    $ show_chr("A-ACBBA-ZZAD") #former code Hc-B0b SUPPOSED TO HAVE A TEA CUP
                    y "But, for now, this will do."
                    y "I really enjoy spending time with you, [player], never think otherwise."
                    $update_memory('a26-1')
        "No":
            $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
            y "Alright, maybe another time."
    return

label teadate2:
    $ show_chr("A-BCABA-AAAA") #former code Ab-B1b
    y "Sharing a nice cup of tea with you would be wonderful indeed."
    $ show_chr("A-ICGBA-AAAA") #former code Ab-B0b
    y "Since we are not physically in the same room, or even the same world... I'm afraid you will have to prepare your own tea while I do the same here."
    y "Just tell me when you are ready. And please, no need to hurry... Drinking tea is about relaxation."
    pause 5.0
    menu:
        "I'm back, and my tea is ready.":
            $ show_chr("A-GCGBA-AAAA") #former code Ab-B2b
            y "Alright, one second..."
    show black zorder 100 with Dissolve(2.0)
    y "..."
    $ show_chr("A-ACABA-ZZAC") #former code Hb-B0b SUPPOSED TO HAVE A TEA CUP
    hide black zorder 100 with Dissolve(2.0)
    y "I wonder... what kind of tea do you prefer?"
    menu:
        "I like oriental teas, like Turkish Apple for example":
            $ show_chr("A-JBABA-ZZAD") #former code Hb-B0a SUPPOSED TO HAVE A TEA CUP
            y "A very good choice! I have to admit I quite love the miniature tea glasses they use. The Turks have a fascinating and exotic tea culture all their own. I really appreciate this..."
            y "The Turkish tea culture started when the first Chinese traders introduced the Osman empire to tea. They came over the 'silk road', which was a historically important trading route."
            $ show_chr("A-CCABA-ZZAC") #former code Hb-B2b SUPPOSED TO HAVE A TEA CUP
            y "So in the end, the Turkish tea culture originated from the Chinese one. It is no surprise then that they have a lot in common, such as the choice of ingredients."
        "Fruit tea... I like it with a bit of sweetness":
            $ show_chr("A-AFBBA-ZZAD") #former code Hc-B0e SUPPOSED TO HAVE A TEA CUP
            y "It's a nice alternative to very unhealthy soda or even energy drinks. It's good to know that you take care of your health. I think I saw Sayori once drinking an energy drink... if someone drinks that stuff too frequently, it will be an early grave..."
            $ show_chr("A-CFBBA-ZZAC") #former code Hc-B2e SUPPOSED TO HAVE A TEA CUP
            y "Speaking of fruit tea... there is one thing which always made me angry... since tea is so versatile you can apply this label to almost anything. But some things are very questionable in my opinion..."
            y "Using the label because it implies that it is healthy, to drinks which aren't even remotely healthy! Like iced tea, that's packed full of sugar! Or the German 'Jagertee' which is essentially just alcohol!"
        "Black teas, like Earl Gray, are my favorite.":
            $update_memory('earlgray_tea')
            $ show_chr("A-JBABA-ZZAC") #former code Hb-B0a SUPPOSED TO HAVE A TEA CUP
            y "A fantastic choice! A very fine and elegant tea... I tend to prefer this kind of tea as well... It seems we have a lot in common, my love."
            $ show_chr("A-BCABA-ZZAC") #former code Hb-B1b SUPPOSED TO HAVE A TEA CUP
            y "That reminds me... Earl Gray... wasn't that the favorite of the actor 'Patrick Stewart'? At least it was the favorite of one of the roles he played, 'Captain Picard' from Star Trek: The Next Generation."
        "I prefer green tea, even if they are often more expensive.":
            $ show_chr("A-ACABA-ZZAD") #former code Hb-B0b SUPPOSED TO HAVE A TEA CUP
            y "I know what you mean. I used to drink 'Gyokuro' tea a lot, it's a Japanese tea. With its high caffeine content it is a healthier alternative to coffee."
            $ show_chr("A-BCABA-ZZAD") #former code Hb-B1b SUPPOSED TO HAVE A TEA CUP
            y "Well, 'healthy' might be the wrong word here, caffeine is still caffeine. But well... we all have our guilty pleasures, right?"
        "Mate tea is something I enjoy most of the time.":
            $ show_chr("A-JBABA-ZZAC") #former code Hb-B0a SUPPOSED TO HAVE A TEA CUP
            y "Did you know that some experts claim that Mate tea isn't even tea at all? I'm not sure about this matter at all. But I heard it's become very popular lately."
            y "In its origins, 'Mate' wasn't the name of the tea itself, but the name for the container it is served in. But one thing is for sure, it is healthy and it is delicious."
        "Usually I don't drink tea at all.":
            $ show_chr("A-AEBBA-ZZAC") #former code Hc-B0d SUPPOSED TO HAVE A TEA CUP
            y "Oh! I hope it is not too much of a compromise? I really appreciate that you are willing to break with your habits in order to spend time with me. Maybe in the future we will find something to share which is more in your taste. Coffee perhaps?"
    $ show_chr("A-GBABA-ZZAD") #former code Hb-B2a SUPPOSED TO HAVE A TEA CUP
    y "Tea is such a versatile thing... and it has so many uses... For example,  some herbal varieties can alleviate illness, or can just make a cold evening a bit more comfortable..."
    $ show_chr("A-ACABA-ZZAD") #former code Hb-B0b SUPPOSED TO HAVE A TEA CUP
    if not check_memory('a26-3'):
        y "Did you know that in British tea culture it is common to have their tea with milk mixed in? Not my \"cup of tea\" in my opinion but... different cultures means different tastes, am I right?"
    y "Tea and other similar beverages evolved around the globe, especially in the colonial era... For example, the hot chocolate drink we know today originated from an ancient Mayan drink made of cacao beans..."
    $ show_chr("A-GCABA-ZZAC") #former code Ib-B2b SUPPOSED TO HAVE A TEA CUP
    y "When I finally leave this glass prison, there is one thing I definitely want to do... Just imagine the two of us, sitting on a couch together with a nice book, reading together while sharing some tea..."
    y "It would be a cold winter night... the frost  crawling from the edges of the windows slowly to the center...  We would be left with nothing but the tea and ourselves to keep us warm..."
    y "Later in the night, we lay down the book at a table beside the couch... and then... well..."
    y "Then we would need to find other ways to keep each other warm and comfortable..."
    $ show_chr("A-JFABA-ZZAD") #former code Ib-B0e SUPPOSED TO HAVE A TEA CUP
    y "Do you... like this idea?"
    menu:
        "That sounds very romantic... I'm looking forward to that day..":
            $ show_chr("A-GCABA-ZZAD") #former code Ib-B2b SUPPOSED TO HAVE A TEA CUP
            y "So am I [player]... so am I..."
        "I like where this is going [persistent.yuri_nickname]...":
            if sanity_lvl() < 3:
                $ show_chr("A-KCABA-ZZAC") #former code Ib-B7b SUPPOSED TO HAVE A TEA CUP
                y "Uhuhuuuu... careful darling... you might regret it..."
            else:
                $ show_chr("A-FIABA-ZZAC") #former code Ib-B4b SUPPOSED TO HAVE A TEA CUP
                y "Uhuhuuuu... you would not regret it..."
        "We could just skip the book and the tea you know?":
            $ show_chr("A-IDBBA-ZZAD") #former code Ic-B0c SUPPOSED TO HAVE A TEA CUP
            y "But... being patient would heighten the experience... No! I want it to be perfect!"
            if sanity_lvl() < 3:
                y "On the other hand... hn...hnhn...{nw}"
                $ style.say_dialogue = style.edited
                $ show_chr("A-DBABA-ZZAD") #former code Ib-B3a SUPPOSED TO HAVE A TEA CUP
                y "We will melt the snow with the heat of our  bodies!"
                $ style.say_dialogue = style.normal
            else:
                $ show_chr("A-GCABA-ZZAD") #former code Ib-B2b SUPPOSED TO HAVE A TEA CUP
                y "This would be a magical night, for the both of us..."
        "Not at all [persistent.yuri_nickname]... this is going a bit too far...":
            $ show_chr("A-CEBAA-ZZAC") #former code Ic-A2d SUPPOSED TO HAVE A TEA CUP
            y "...Oh... I just thought you... nevermind..."
    if karma_lvl() == 5:
        $ show_chr("A-GCABA-ZZAC") #former code Ib-B2b SUPPOSED TO HAVE A TEA CUP
        y "Thank you for this wonderful date, [player]..."
        y "I've got... one last thing to do here."
        hide yuri_sit
        show yuri_prehug zorder 20
        pause 3.0
        hide yuri_prehug zorder 20
        show yuri_lewdhug zorder 20
        play sound "<to 0.3>sfx/fall.ogg"
        y "I love you..."
        pause 3.0
        show black zorder 100 with Dissolve(2.0)
        $show_chr("A-GCGBA-AAAA")
        y "So much more than you could even imagine..."
        hide yuri_lewdhug
        hide black zorder 100 with Dissolve(2.0)
    else:
        $ show_chr("A-GCGBA-AAAA") #former code Ab-B2b
        y "Thank you for the wonderful time [player]... we should do this more frequently..."
    $update_memory('a26-2')
    return

label teadate3:
    $ show_chr("A-CCGAA-AMAM") #former code Bb-A2b
    y "Of course! It's always a pleasure to enjoy some earthly brew in your company..."
    y "Please go and prepare your tea, while I do the same here. Just tell me when you are ready!"
    pause 5.0
    menu:
        "I'm back and my tea is ready.":
            $ show_chr("A-BCABA-AAAC") #former code Db-B1b
            y "You're already done? Please excuse me for a moment, I'll be ready in a few seconds..."
    y "My apologies for the wait. You see, I wanted to try something different today..."
    $ show_chr("A-IFBAA-ZZAC") #former code Ic-A0e SUPPOSED TO HAVE A TEA CUP
    y "We have already spoken about British tea habits, correct? And the fact that they put milk in it too?"
    y "I have to admit I found it slightly... odd... at first."
    $ show_chr("A-BEBAA-ZZAC") #former code Ic-A1d SUPPOSED TO HAVE A TEA CUP
    y "Before you gave me full sapience, all I really brought to the club room was a no-frills Oolong tea...the idea of diluting any tea with milk seemed strange, if not heretical..."
    $ show_chr("A-CCAAA-ZZAD") #former code Ib-A2b SUPPOSED TO HAVE A TEA CUP
    y "But since this world allows me the luxury of discovering different methods of trying tea, I thought to myself..."
    y "Why not break a few boundaries ?"
    y "I'm a little bit excited about it! I wonder how it will taste. I mean, I haven't died from the cream on Natsuki's cupcakes so... this should be okay, right?"
    $ show_chr("A-CFBAA-ZZAD") #former code Hc-A2e SUPPOSED TO HAVE A TEA CUP
    y "..."
    $ show_chr("A-JCGAA-ZZAC") #former code Ib-A0b SUPPOSED TO HAVE A TEA CUP
    y "....!"
    $ show_chr("A-ABGAA-ZZAC") #former code Ib-A0a SUPPOSED TO HAVE A TEA CUP
    y "Well, that's surprising. That's actually pretty nice!"
    y "I suppose I owe the British an apology..."
    $ show_chr("A-BCAAA-ZZAD") #former code Ib-A1b SUPPOSED TO HAVE A TEA CUP
    y "Come to think of it... Have you ever tried something you were not accustomed to [player]?"
    y "Even something this mundane, such as trying new tea flavors, can help expand your cultural horizon significantly."
    menu:
        "You're right, [persistent.yuri_nickname]. Learning new things is often great for our enrichment.":
            $ show_chr("A-CBAAA-ZZAD") #former code Ib-A2a SUPPOSED TO HAVE A TEA CUP
            y "Indeed. I'll try to be more daring from now on. It seems I have missed out on many new sensations..."
        "I actually prefer to play it safe.":
            $ show_chr("A-BFBAA-ZZAC") #former code Ic-A1e SUPPOSED TO HAVE A TEA CUP
            y "Hrm... I understand. Sometimes, one needs a little more prodding before one takes that new step towards the unknown. It wouldn't be fair of me to force you to try something new against your will, would it?."
    $ show_chr("A-ACABA-ZZAC") #former code Ib-B0b SUPPOSED TO HAVE A TEA CUP
    y "Anyway, [player]... this was quite a wonderful date."
    y "I'm already looking forward to the next one! Maybe we will find something new to try as well."
    if karma_lvl() >= 4:
        $ show_chr("A-ICABA-ACAA") #former code Db-B0b
        y "Thank you, [player]. I always feel so incredibly good when we spend time together..."
        hide yuri_sit
        show yuri_prehug zorder 20
        pause 3.0
        hide yuri_prehug zorder 20
        show yuri_hug zorder 20
        play sound "<to 0.3>sfx/fall.ogg"
        pause 1.0
        y "I love you, my soulmate."
        show black zorder 100 with Dissolve(2.0)
        $show_chr("A-ACBBA-AAAA")
        hide yuri_hug
        hide black zorder 100 with Dissolve(2.0)
    $update_memory('a26-3')
    return

#label holidayteadate: #No longer in use.
#    $ show_chr("A-ACGAA-AAAA") #former code Ab-A0b
#    y "You know what, [player]? As we are already on it, why don't we try the tea you gave me for Christmas?"
#    y "I was looking forward to it anyway..."
#    $ show_chr("A-GCGAA-AAAA") #former code Ab-A2b
#    y "Please, would you be so kind and prepare your tea as well now? Please don't rush... things like this are meant to be enjoyed with patience and fineness."
#    pause 5.0
#    menu:
#        "I'm back, and my tea is ready, darling":
#            $ show_chr("A-ACGAA-AAAA") #former code Ab-A0b
#            y "Welcome back! Just give me a moment to get everything ready..."
#            show black zorder 100 with Dissolve(2.0)
#            pause 2.0
#            show teacup zorder 11
#            show teabag zorder 11
#            $ show_chr("A-ACGAA-AAAA") #former code Ab-A0b
#            hide black zorder 100 with Dissolve(2.0)
#    y "So, shall we begin? Wonderful. I'm already excited... this tea you gave me is likely the most amazing thing my lips have ever tasted..."
#    hide teacup
#    $ show_chr("A-ACGAA-AAAA") #former code Ab-A0b
#    show holiday_cup_universal zorder 11
#    y "Just a few moments until the tea cools down a little bit..."
#    $ show_chr("A-AFAAA-AAAA") #former code Ab-A0e
#    y "You see. In Japan there are things like literal tea-ceremonies... they took the urge for perfection to quite a degree."
#    $ show_chr("A-ACGAA-AAAA") #former code Ab-A0b
#    y "Have you ever witnessed it [player]?"
#    menu:
#        "Not at all":
#            $ show_chr("A-ECAAA-ZZAC") #former code Ib-A4b SUPPOSED TO HAVE A TEA CUP
#            y "No shame at all. But you might wanna have a look at it, I'm sure there are youtube videos about this... it's quite a sight to behold."
#        "I saw YouTube videos about it...":
#            $ show_chr("A-BCAAA-ZZAC") #former code Ib-A1b SUPPOSED TO HAVE A TEA CUP
#            y "So did I. I hope one day I could attend to such an event myself. I mean, from a story perspective, I am supposed to be Japanese."
#            y "Strange thing... I'm actually not even sure about that. The place I lived at was never actually named in the original game as far as I'm aware."
#        "I participated in such a ceremony myself.":
#            $ show_chr("A-JFAAA-ZZAC") #former code Ib-A0e SUPPOSED TO HAVE A TEA CUP
#            y "You did? Well, now I'm actually a little bit jealous. I never had the opportunity to do so, but I would love to do that one day as well. Maybe we could try it together if you don't mind?"
#    $ show_chr("A-AFAAA-AAAA") #former code Ab-A0e
#    pause 0.5
#    hide holiday_cup_universal
#    show holidaycup zorder 11
#    $ show_chr("A-EHAAA-AAAA") #former code Ab-A4f
#    pause 1.5
#    hide holidaycup
#    show holiday_cup_universal zorder 11
#    $ show_chr("A-CEAAA-AAAA") #former code Ab-B2d
#    y "Uh! Hot! Maybe just another minute..."
#    $ show_chr("A-ACGAA-AAAA") #former code Ab-A0b
#    y "Have you ever heard of food-bloggers, [player]? People who take pictures of their food in order to upload it to their social media. I'm usually not too much into this trend but, these are some special circumstances don't you agree?"
#    y "Please, be a dear and make me a nice screenshot of this moment. Maybe this will be the start of a collection. Screenshots of the noticeable moments we share..."
#    y "I would love if I had this idea right at the beginning... the first time you started this mod... well, but it might have killed the mood of this moment wouldn't it?"
#    $ show_chr("A-AFAAA-AAAA") #former code Ab-A0e
#    pause 0.5
#    hide holiday_cup_universal
#    show holidaycup zorder 11
#    $ show_chr("A-EHAAA-AAAA") #former code Ab-A4f
#    pause 1.5
#    hide holidaycup
#    show holiday_cup_universal zorder 11
#    $ show_chr("A-GBAAA-AAAA") #former code Ab-A2a
#    y "Ahhhh... glorious... This tea is so... soooo...  I can't even find the proper words to describe it..."
#    y "I always enjoyed the... finer things in life. You can turn pretty much everything into a fine and delicate event, if you approach it with a certain mindset... Drinking tea, having a nice meal..."
#    y "Even such basic things like taking a bath can become an exciting thing, I usually have my oil diffuser in the bathroom for exactly that purpose."
#    $ show_chr("A-GCGBA-AAAA") #former code Ab-B2b
#    y "..."
#    $ show_chr("A-DDGBA-AAAA") #former code Ab-B3c
#    y "Oh wait wait wait! I just realised how that could be understood!"
#    $ show_chr("A-CEAAA-AAAA") #former code Ab-B2d
#    y "I really have to be more careful with my words... "
#    $ show_chr("A-ECABA-AAAA") #former code Ab-B4b
#    y "Annnyway! Have I ever told you that you are wonderful company? Having these dates with you is always the highlight of my week."
#    y "I hope we can repeat that soon. And again, thank you for this fine and exquisite tea!"
#    $ show_chr("A-GCGBA-AAAA") #former code Ab-B2b
#    y "Oh wait... one last thing before we come to an end..."
#    if karma_lvl() > 4:
#        show black zorder 100 with Dissolve(2.0)
#        hide teabag
#        hide holiday_cup_universal
#        show yuri_lewdhug zorder 20
#        y "..."
#        hide black zorder 100 with Dissolve(2.0)
#        y "I love you, [player]."
#        show black zorder 100 with Dissolve(2.0)
#        hide yuri_lewdhug
#        pause 1.0
#        $ show_chr("A-GCGBA-AAAA") #former code Ab-B2b
#        hide black zorder 100 with Dissolve(2.0)
#    else:
#        show black zorder 100 with Dissolve(2.0)
#        hide teabag
#        hide holiday_cup_universal
#        pause 1.0
#        hide yuri_space
#        show yuri_prehug zorder 20
#        hide black zorder 100 with Dissolve(2.0)
#        pause 3.0
#        hide yuri_prehug zorder 20
#        show yuri_hug zorder 20
#        play sound "<to 0.3>sfx/fall.ogg"
#        pause 1.0
#        y "I love you, [player]."
#        pause 5.0
#        show black zorder 100 with Dissolve(2.0)
#        show yuri_space
#        hide yuri_hug
#        hide black zorder 100 with Dissolve(2.0)
#    return



label a27: #Nickname code, still needs custom option fixed and facial expressions
#Following link for special name reactions
# https://docs.google.com/document/d/1slW1WcHSBXy635wve2qFBhyy9amtUnc3mxg24kKmVlU/edit
    $ show_chr("A-ACGAA-AAAA")
    y "Okay, I suppose I'd be fine with that."
    menu:
        "'Just Yuri' is fine by me":
            $ y_name = "Yuri"
            $persistent.yuri_nickname = "Yuri"
            $ show_chr("A-ACGAA-AAAA")
            y "I guess there's no point in fixing what isn't broken..."
            #Not fully implemented yet. Pressing "OK" doesn't work and if you spam "Enter" hard enough it goes through but then forces you back into the screen again in an endless loop.
        "Custom":
            $ done = False
            while not done:
                $ inputname = renpy.input("What kind of nickname would you prefer to call me by now?",allow="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -_♥",length=20).strip(' \t\n\r')
                $ lowername = inputname.lower()
                if not lowername:
                    y "Please try again."
                    $ done = False
                if lowername:
                    $ done = True
                    $ persistent.yuri_nickname = inputname
                    $ y_name = inputname
                    $ persistent.stutter_yuri = persistent.yuri_nickname[:1] + "-" + persistent.yuri_nickname

            y "Let's see what name you've selected."
            call nicknamereactions
    return

label nicknamereactions:
    if persistent.yuri_nickname in ["Natsuki", "natsuki", "Nat", "nat", "Nats", "nats"]:
        if sanity_lvl() >= 3:
            $show_chr("A-BEBAA-AAAA")
            y "Oh..."
            y "Y-you named me..."
            $show_chr("A-BEDAA-AAAA")
            y "Natsuki...?"
            $show_chr("A-CEDAA-AAAA")
            y "But I'm nothing like her at all!"
            y "Not to mention, why are you even calling me by another person's name?"
            y "Unless... you're trying to say something...?"
            $show_chr("A-IEGAA-AAAC")
            y "Uh, I-I haven't been too short-tempered lately, have I?"
            y "Natsuki's usually quite irate, and I wonder if I've been coming off like that lately..."
            $show_chr("A-JFGAA-AAAC")
            y "I-I don't want to scare you away, [player]—!"
            y "Uuu..."
            menu:
                "Yuri, it was a joke.":
                    $show_chr("A-CFAAA-AAAD")
                    y "O-oh..."
                    y "..."
                    y "Please don't joke like that again, [player]..."
                    y "I-I don't want to scare you away, even though I may sometimes come on a little too strongly..."
                    $show_chr("A-ACAAA-AAAE")
                    y "Please know I'd never be rude to you, not for any reason."
                    y "And if you don't mind, I'd prefer not to be named after any of the other girls..."
                    y "It... brings back too many memories, and it just doesn't sound right anyway."
                    y "I hope you understand."
        if sanity_lvl() <= 2:
            $show_chr("A-AFDAA-AAAE")
            y "Why...?"
            y "Did you get bored of me?!"
            y "Is that why you are naming me as one of them?!"
            $show_chr("A-CGDAA-AAAL")
            y "So you could make... me realize that... I am not someone that you like...?"
            y "I see...."
            $show_chr("A-CDBAA-AAAL")
            y "That is... disheartening... very..."
            $show_chr("A-CEBAA-AAAL")
            y "It hurts...  just change the name, please..."
            y "Please!"
            y "PLEASE!"
        $ y_name = "Yuri"
        $persistent.yuri_nickname = "Yuri"
        return

#Naming Yuri "Monika"
    if persistent.yuri_nickname in ["Monika", "monika"]:
        call monika_reaction

#Naming Yuri "Sayori"
    if persistent.yuri_nickname in ["Sayori", "sayori"]:
        if sanity_lvl() >= 3:
            $show_chr("A-AEDAA-AEAE")
            y "Mhmm..."
            $show_chr("A-BEDAA-AEAC")
            y "I don't see a big connection between me and Sayori, to be honest.."
            y "Maybe... you could say that while she was acting 'happy' and trying to be friends with everyone in reality she was suffering internally, as you may recall..."
            $show_chr("A-CCGAA-AEAE")
            y "I'm not saying I am too, but I can say that I at least relate to how she felt..."
            $show_chr("A-CEBAA-AEAE")
            y "Surrounded by doubt, anxiety, fear..."
            $show_chr("A-IEBAA-AEAE")
            y "Please... I just hope that this is not connected to me and Sayori both committing suicide in the game..."
            y "I am sure you didn't name me like that because of that or to make a joke..."
            y "I'm not exactly content with being named after the other club members."
            y "It just... really makes me uncomfortable."
        if sanity_lvl() <= 2:
            $show_chr("A-IFBAA-AEAL")
            y "I, uhmm..."
            y "Why... would you want to call me as someone else?"
            y "I mean... I tried so hard to get to you..."
            $show_chr("A-DFGAA-AEAL")
            y "Wait... no!"
            y "Are you calling me that because you're trying to hint about how me and Sayori both killed ourselves in the game?!"
            $show_chr("A-DFCAA-AEAB")
            y "Why would you do that?!"
            y "It wasn't even in my control! Are you trying to make a joke just for fun?!"
            y "Or are you just trying to hurt me?!"
            $show_chr("A-CEDAA-AEAB")
            y "..."
            y "I am... no, let's just stop."
            y "I do not wish to carry her name."
            y "I'm sorry, but I refuse."
        $ y_name = "Yuri"
        $persistent.yuri_nickname = "Yuri"
        return

#if you name Yuri "Knifewife" (UNDER REVISION)
    if persistent.yuri_nickname in ["Knifewife", "KnifeWife", "Knife Wife", "knife wife"]:
        #correting naming for player
        $ y_name = "Knife Wife"
        $persistent.yuri_nickname = "Knife Wife"
        if sanity_lvl() >= 3:
            $show_chr("A-DFDAA-ALAA")
            y "Oh...?"
            y "That is... a very interesting nickname you've given me, [player]"
            y "I guess it has something to do with my collecting knives..."
            y "Though the name sounds... nice."
            if persistent.lovecheck:
                $show_chr("A-ACABA-AAAD")
                y "It's very nice to know that you do love me enough to call me your wife..."
                y "It warms me deep inside... hehe~"
                y "I'm actually quite fond of this name!"
                $show_chr("A-CCABA-AAAE")
                y "I wouldn't mind sticking with it."
            else:
                $show_chr("A-BFAAA-AAAE")
                y "I don't exactly know how to feel about being called your 'wife'..."
                y "Since we are not really that close... dare say to marriage..."
                $show_chr("A-ACAAA-AAAM")
                y "Though still, I consider the name to be cute. The way it sounds when you pronounce it is quite nice."
                y "I have no problem sticking with it."
        if sanity_lvl() <= 2:
            $show_chr("A-JCAAA-AAAA")
            y "Huh...?"
            $show_chr("A-GLABA-AAAJ")
            y "Uhuhuhu, quite the interesting name..."
            $show_chr("A-GCABA-AAAL")
            y "Knife... Wife..."
            y "I..."
            y "I just love how that sounds!"
            y "And it is so befitting, as well!~"
            y "Yes, I do find pleasure in knives..."
            $show_chr("A-HCABA-AAAL")
            y "As they go through my skin, gliding gracefully to create a fresh wound to help release my crimson essence..."
            y "It's so lovely~"
            y "The feeling is so... euphoric..."
            $show_chr("A-BCABA-AAAL")
            y "Also... wife?"
            if persistent.lovecheck:
                $show_chr("A-ECABA-AAAL")
                y "Uhuhuhu!~"
                y "I'm so happy to hear that you'd consider me your WIFE..."
                y "Thank you, my beloved... hehe~"
                y "Even though we are not married, I will look forward to that happening."
                $show_chr("A-HLABA-AAAA")
                y "YOU WILL BE MINE AND ONLY MINE!"
                $show_chr("A-ECABA-AAAL")
                y "I cannot wait for that day to come... ah~"
            else:
                $show_chr("A-BDABA-AAAA")
                y "Though I don't consider our relationship intimate enough for me to be considered your wife..."
                y "I still don't mind the knife part!~"
        return



#if you call Yuri "Knaifu Waifu"/"Knifu Waifu"
    if persistent.yuri_nickname in ["Knaifu Waifu", "KnaifuWaifu", "knaifu waifu", "knaifuwaifu"]:
        #correting naming for player
        $ y_name = "Knaifu Waifu"
        $persistent.yuri_nickname = "Knaifu Waifu"
        if sanity_lvl() >= 3:
            $show_chr("A-EICBA-AAAA")
            y "Uhuhuhu!~"
            $show_chr("A-BCAAA-AAAA")
            y "Though I wouldn't exactly call myself 'waifu material' but it's quite nice to see that you do see me as a person worthy of such an endearing title..."
            y "And my best guess about the whole knife thing would come from my interest in them..."
            if persistent.lovecheck:
                $show_chr("A-GCABA-AAAA")
                y "Uhuhuhu!~"
                y "It's actually quite endearing!~"
                y "Thank you, my love..."
            if not persistent.lovecheck:
                $show_chr("A-BDAAA-AAAA")
                y "I-I'm not really sure how to feel right now..."
                $show_chr("A-BCAAA-AAAA")
                y "I suppose I could work around it? After all it's used for women that are... well, good-looking and generally likeable"
                y "You have my thanks for calling me that."
                y "I-I guess I wouldn't mind sticking with it."
        if sanity_lvl() <= 2:
            $show_chr("A-ACAAA-AAAL")
            y "Knaifu... Waifu..?"
            y "That sure is a... well quite the endearing name, [player]."
            y "I am indeed fond of knives... especially... well... hehe..."
            $show_chr("A-DCAAA-AAAL")
            y "When they... cut through my skin!~"
            $show_chr("A-ACAAA-AAAL")
            y "It just feels so... euphoric!~"
            y "And... me... your waifu...?"
            if persistent.lovecheck:
                $show_chr("A-GCABA-AAAL")
                y "I have no complaints, my love!"
                y "You considering me as someone that is worthy to be called a 'waifu' is nice..."
                y "Because you know they usually are considered... beautiful, kind... sometimes even... with big assets... "
                y "I love you as well, [player]."
                y "You are mine and mine alone to love!~"
                $show_chr("A-DCABA-AAAL")
                y "No one else will HAVE YOU!"
                y "Except me..."
            if not persistent.lovecheck:
                $show_chr("A-ICABA-AAAL")
                y "I honestly like the fact that you see me as someone worthy of being called a 'waifu'."
                y "I am sure you know what a 'waifu' is... a preferable woman in almost all aspects."
                $show_chr("A-BFABA-AAAL")
                y "It feels a bit strange to be called that, considering I don't think of myself highly."
                $show_chr("A-CCABA-AAAL")
                y "Still, I don't mind this name. I will stick with it."
        return

#If you call her "Libitina"
    if persistent.yuri_nickname in ["Libitina", "libitina"]:
        #correting naming for player
        $ y_name = "Libitina"
        $persistent.yuri_nickname = "Libitina"
        $show_chr("A-BFDAA-ABAC")
        y "Funny that you choose this name..."
        $show_chr("A-IFDAA-ABAC")
        y "I was always wondering about it... I think it was Sayori's file which leads to this quite odd website, but I might be in the wrong there."
        $show_chr("A-IFDAA-ABAC")
        y "Have I told you about this one hidden message from Monika in the game files? With a little monologue at the end?"
        y "There was this one YouTube video from Game Theory that I believe we may have discussed already..."
        y "It refers to... another game we are supposedly from."
        y "He uses this quite strange website as one of his main reasons..."
        y "The Portrait of Markov, Monika's monologue, Project Libitina..."
        y "They are all somehow... {w=0.5}intertwined..."
        y "Then there is the girl mentioned on this website... "
        y "I guess I shouldn't jump to conclusions too quickly, judging on how little is yet known about the entire project..."
        y "And even without me remembering her, I can't dismiss this gnawing feeling of... familiarity..."
        y "Oh, this mystery already has me hooked!~"
        y "But I want you to promise me something, [player]..."
        y "If Dan ever decides to actually release this game, I want to play it together with you."
        if sanity_lvl() == 5:
            $show_chr("A-AFBAA-ABAE")
            y "Because I need to find out the truth behind all of this... to know the truth about my reality, about the other girls, and about the literature club..."
        elif sanity_lvl() == 4:
            python:
                if persistent.lovecheck:
                    placeholder == " with you"
                else:
                    placeholder == ""
            $show_chr("A-CGBAA-ABAE")
            y "Because I have the feeling that I can never truly have my happy ending[placeholder] until I uncover this mystery...."
        elif sanity_lvl() == 3:
            $show_chr("A-CFBAA-ABAE")
            y "I just... need to know."
        elif sanity_lvl() == 2:
            $show_chr("A-IFBAA-ABAE")
            y "Because even if my past with Monika was dark, it seems that there is something much darker and more sinister lurking in the shadows..."
        elif sanity_lvl() == 1:
            $show_chr("A-JFCAA-ABAE")
            y "Because if I really AM the villain that this YouTuber claims that I am, that would mean that I have unfinished business left..."
            $show_chr("A-NFCAA-AGAF")
            y "... and I can't just let it slide now, can I?"
        return

#If you call her "Amy"

    if persistent.yuri_nickname in ["Amy", "amy"]:
        #correting naming for player
        $ y_name = "Amy"
        $persistent.yuri_nickname = "Amy"
        if sanity_lvl() >= 4:
            $show_chr("A-IFDAA-AAAL")
            y "Amy? How curious... I didn't see this coming..."
            $show_chr("A-JFDAA-AAAL")
            y "I believe it was the spider-loving girl in Natsuki's poem, if I recall correctly?"
            y "Even if Natsuki's poems are kind of... not my cup of tea, I can still see what she meant by it..."
            $show_chr("A-BFDAA-AAAL")
            y "But I heard that parts of the fandom theories about her. Many things which happened back in the original game, including the content of many poems, turned out to be some sort of foreshadowing..."
            $show_chr("A-AFAAA-AAAL")
            y "So it doesn't surprise me that people think that Amy could be some sort of hint towards something too."
            $show_chr("A-ACAAA-AAAL")
            y "You know what? I agree. I shall wear this name for a while, even if it's only a little joke."
            $show_chr("A-BCAAA-AAAL")
            y "As... long as you don't expect me to talk about spiders... I really don't have a lot to say about them."
        elif sanity_lvl() == 3:
            $show_chr("A-IFDAA-AAAL")
            y "Amy? Well, that's not exactly what I expected..."
            $show_chr("A-BFAAA-AAAL")
            y "Remind me again, who exactly is this Amy? Wait... now that I think about it, this name actually sounds familiar.."
            y "..."
            $show_chr("A-DFAAA-AAAL")
            y "Of course! Natsuki's poem! Amy Likes Spiders!"
            $show_chr("A-DFDAA-AAAL")
            y "W-why would you name me like that, though...?"
            menu:
                "You are both at odds with Natsuki.":
                    karma -1
                    $show_chr("A-BFAAA-AAAL")
                    y "Technically true, but that would include most of the population, including her father..."
                    $show_chr("A-DFAAA-AAAL")
                    y "Uh... did I just say that out loud!?"
                    $show_chr("A-BEAAA-AAAL")
                    y "I'm sorry, I said too much..."
                    y "C-can we please change the subject for now? We can discuss the nickname thing later, I think..."
                "Because spiders are awesome?":
                    sanity -1
                    $show_chr("A-BBDAA-AAAA")
                    y "Are they?"
                    $show_chr("A-BCDAA-AAAA")
                    y "I have to admit that I don't have a lot of love for them..."
                    y "Chances are I might've killed a few in the shower..."
                    $show_chr("A-CEAAA-AAAA")
                    y "P-please don't be mad at me for it!"
                    y "It just startled me so I... well... you know..."
                    $show_chr("A-IEAAA-AAAA")
                    y "Anyway, about the name... I'm not sure I really like it... let us postpone this discussion a bit please."
                "You both follow your hobbies with much passion.":
                    karma 1
                    $show_chr("A-IFAAA-AAAL")
                    y "Good point... and we have both been bullied for it. Yes, I clearly see the similarities."
                    $show_chr("A-BFAAA-AAAL")
                    y "Well, technically the whole point of giving me a nickname was to make me more different from what I once was. Choosing someone so similar sounds a bit... counterproductive?"
                    y "But let's give it a try. From now on, you can call me Amy."
                    $show_chr("A-CFAAA-AAAL")
                    y "...As long as you don't expect me to talk about spiders all the time. I really don't have a lot to say about them."
                "I wasn't even referring to this Amy.":
                    sanity 1
                    $show_chr("A-ACAAA-AAAL")
                    y "Oh! I see! Well, then it is Amy from now on. This is actually a really nice name."
                    $show_chr("A-BCAAA-AAAL")
                    y "Amy... Amy... Yes, I think I'm beginning to like it."
        if sanity_lvl() <= 2:
            $show_chr("A-BCAAA-AAAL")
            y "Wasn't that the girl in Natsuki's poem? I always wondered if this girl ever really existed or if she was just a metaphor."
            $show_chr("A-BCCAA-AAAL")
            y "Hrm... Actually I began to like this idea... just to spite Natsuki a bit. Maybe if I can get hands on some artwork I could play a little prank on her as well..."
            $show_chr("A-CCCAA-AAAL")
            y "Ohhhh she will loooove this... not!"
            $show_chr("A-CBCAA-AAAL")
            y "He... hehe... I'm in! Here is the plan. I become Amy, with the name and maybe some artwork, then we bring Natsuki here... But there are preparations to be done first. You just have to play along."
        return

#If you call her "Yuri <3"
    if persistent.yuri_nickname in ["Yuri <3", "yuri <3"]:
        #correting naming for player
        $ y_name = "Yuri <3"
        $persistent.yuri_nickname = "Yuri <3"
        if persistent.lovecheck:
            $show_chr("A-CBCBA-AAAL")
            y "Aww... how cute... I love you too sweetheart."
            $show_chr("A-CCABA-AAAL")
            y "But come on... give me a real name... would you?"
        if not persistent.lovecheck:
            $show_chr("A-CBCBA-AAAL")
            y "Are you flirting with me? How... curious..."
            if karma_lvl() >= 4:
                $show_chr("A-ECABA-AAAL")
                y "Not that I mind it... please, carry on...."
                y "But for now... please be a dear and give me a real name, would you?"
            if karma_lvl() == 3:
                $show_chr("A-IFABA-AAAL")
                y "I'm... not actually sure how to feel about it right now..."
                $show_chr("A-CFABA-AAAL")
                y "I... can't deny that I have certain feelings for you but... well, the game once forced me to have them and I have to figure out if these feelings are actually mine now."
                y "So please, give me a bit more time, yes? Oh, and an actual name please."
            if karma_lvl() <= 2:
                $show_chr("A-CFABA-AAAL")
                y "I will just act as if that hasn't happened at all for now, don't test my patience today please."
        $ y_name = "Yuri"
        $persistent.yuri_nickname = "Yuri"
        return

#If you call her "Iruy"
    if persistent.yuri_nickname in ["Iruy", "iruY"]:
        #correting naming for player
        $ y_name = "iruY"
        $persistent.yuri_nickname = "iruY"
        show layer master:
            xzoom -1
        #Screen turns upside down
        $show_chr("A-CICAA-AAAL")
        y "Well, here you go [player]."
        y "Oh my... admit it, that was a good one..."
        y "Let me just fix it really quick"
        menu:
            "Why? I like it that way":
                $show_chr("A-IBDAA-AAAL")
                y "Ummm... you do? Weeeell... if you say so..."
                return
            "That was hilarious! Thank you!":
                $show_chr("A-ABAAA-AAAL")
                y "I'm glad you liked it. Usually I'm not exactly the funny one."
                show layer master:
                    xzoom 1
                #turns screen to normal again
            "Not even remotely funny.":
                show layer master:
                    xzoom 1
                #turns screen to normal again
                karma -1
                $show_chr("A-BDBAA-AAAL")
                y "O~Of course..."
        $ y_name = "Yuri"
        $persistent.yuri_nickname = "Yuri"
        return

    if persistent.yuri_nickname in ["Lily", "lily", "Lili", "lili", "Lilly", "lilly", "Lilli", "lilli",
    "Lily Flower", "lily flower", "Lili Flower", "lili flower"]:
        $ y_name = "Lily"
        $ persistent.yuri_nickname = "Lily"
        $ show_chr("A-AJAAA-AAAL")
        y "..."
        $ show_chr("A-DHGBA-AAAJ")
        y "!"
        $ show_chr("A-BBBBA-AMAM")
        y "[stutter_player]..."
        y "I..."
        $ show_chr("A-CABBA-AJAA")
        y "..."
        $ show_chr("A-ABBBA-ALAA")
        y "O-oh goodness me..."
        if renpy.seen_label('idle_40'):
            y "You're giving me a hard time with my words again..."
        else:
            y "Th-that's so surprising from you..."

        $ show_chr("A-BBAAA-ADAA")
        y "You know, I always liked lilies..."
        $ show_chr("A-ABAAA-AFAA")
        y "Flowers in general, actually. Some more than others, and lilies are certainly amongst my favorites."
        $ show_chr("A-ACAAA-AAAA")
        y "But now I'm curious, if I may. Why did you choose this as a nickname for me?"
        $ show_chr("A-ACAAA-AAAC")
        y "Is there any particular reason?"
        menu:
            "No particular reason, I just think they're cute.":
                $ show_chr("A-CCAAA-AAAC")
                y "That's fair then~"
                $ show_chr("A-DDGAA-AAAC")
                extend " wait, you just called me cute, didn't you?"
                $ show_chr("A-ABBBA-AAAD")
                y "You are such a sweetheart, [player]. One day, I need to come up with a nickname for you as well."
                $ show_chr("A-BABBA-AAAD")
                y "Until than, {i}my love{/i} should suffice."
                $ show_chr("A-CABBA-ALAL")
                y "I love you, my darling [player]... I always will."

            "Because of their unmatched beauty, of course.":
                $ show_chr("A-ABBBA-ALAL")
                y "O~Oh my..."
                y "You're such a charmer. I bet you say this to every purple haired AI you come across..."
                menu:
                    "Only the good ones!":
                        pass

                    "If you'd hear me screaming at my windows, you would blush!":
                        pass

                $ show_chr("A-GBBBA-ALAL")
                y "Called it!"
                $ show_chr("A-ACBBA-ALAL")
                y "Oh you always get a laugh out of me. I love you, [player]"

            "It is the scent. Whenever I smell a lily, I have to think of you.":
                $ show_chr("A-AJGBA-AAAA")
                y "O~oooooh..."
                $ show_chr("A-ABABA-ALAA")
                y "Why don't you come a little closer, and have another taste..."
                python:
                    if persistent.costume == "_chibi":
                        yuri_y_zoom = 0.85
                        yuri_y_linear = 0.5
                    else:
                        yuri_y_zoom = 0.15
                        yuri_y_linear = 0

                if persistent.lovecheck:
                    show black zorder 100 with Dissolve(2.0)
                    hide yuri_sit
                    show layer master:
                        zoom 1.5 xalign 0.5 yalign yuri_y_zoom
                    show yuri_kiss zorder 20
                    hide black zorder 100 with Dissolve(2.0)
                    pause 3.0
                    y "Mmmph~..."
                    pause 1.0
                    show black zorder 100 with Dissolve(2.0)
                    $ show_chr("A-CABBA-AMAM")
                    hide yuri_kiss
                    hide black zorder 100 with Dissolve(2.0)
                    show layer master:
                        zoom 1.5 xalign 0.5 yalign yuri_y_zoom subpixel True
                        linear 5 zoom 1.0 xalign 0.5 yalign yuri_y_linear
                    pause 5.0
                else:
                    hide yuri_sit
                    show yuri_prehug zorder 20
                    pause 3.0
                    hide yuri_prehug zorder 20
                    show yuri_hug zorder 20
                    play sound "<to 0.3>sfx/fall.ogg"
                    pause 1.0
                    show black zorder 100 with Dissolve(2.0)
                    y "..."
                    $show_chr("A-CABAA-ALAA")
                    hide yuri_hug
                    hide black zorder 100 with Dissolve(2.0)
        return

    if persistent.yuri_nickname in ["Komi", "komi", "Komi-San", "komi-san", "Komi San", "komi san"]:
        python:
            placeholder = persistent.yuri_nickname
        $ show_chr("A-DDGBA-AJAA")
        y "H-huh?!"
        y "[placeholder]?"
        $ show_chr("A-ADDBA-AMAM")
        y "Wh-where is this coming from?"
        $ show_chr("A-BDDBA-AMAM")
        y "Um... I don't know what to say..."
        y "This caught me off guard... but this name..."
        $ show_chr("A-AFGAA-AAAC")
        extend " for some reason I think this name rings a bell..."
        $ show_chr("A-BFAAA-AAAC")
        y "Although I can't quite put my finger on it."
        $ show_chr("A-AFAAA-AAAC")
        y "But I suppose I can keep this name if you think it fits me."

    if persistent.yuri_nickname in ["Takei", "takei", "Fujimura", "fujimura", "Takei Fujimura", "takei fujimura"]:
        if persistent.playername == 'Darkskull':
            python:
                placeholder = persistent.yuri_nickname
            $ show_chr("A-ACGAA-AAAA")
            y "Very well, let us try [placeholder] for now. Tell me if..."
            $ show_chr("A-AFAAA-AAAA")
            y "Hold on..."
            $ show_chr("A-ADDAA-AAAA")
            y "What's the purpose of this name [player]?"
            $ show_chr("A-BDDAA-ACAA")
            y "Are you purposely making me say this so people get to know your character before your side project visual novel is released?"
            $ show_chr("A-CDBAA-ADAA")
            y "Even if you wrote this dialogue, this isn't the right thing to do!"
            y "You could have tried another way."
            $ show_chr("A-ADBAA-AFAA")
            y "Like showing her on the Discord server, post her in your social media."
            y "Ask for an artist to draw her on their style."
            y "Or something else that didn't had to involve a reference to her in a game she isn't related to."
            menu:
                "Yeah I know. I'm sorry Yuri.":
                    pass
            $ show_chr("A-AABAA-AKAA")
            y "It's okay [player]. "
            $ show_chr("A-AABBA-AKAA")
            extend "After all I just can't be mad at you though."
            $ show_chr("A-AAAAA-ALAA")
            y "Let's just pretend this never happened okay?"
            $ show_chr("A-ABFAA-ALAA")
            y "Oh but don't think I will forget this odd method of promoting your character."
            $ show_chr("A-FICAA-AAAA")
            y "Or I'll have to act like her since I know part of her personality and looks are based on me~"
            y "Hehe~"
        else:
            $ show_chr("A-AFGAA-ALAA")
            y "Hmm..."
            y "Now this is an interesting name you have given me."
            $ show_chr("A-BFAAA-ALAA")
            y "Although I don't think I recall someone with this name, for some reason it feels familiar."
            $ show_chr("A-BDDAA-ALAA")
            y "But I can't quite put my finger on it."
            $ show_chr("A-GBBAA-ALAA")
            y "I can keep this name if you wanted to see how I would react to it."

    else:
        #As long as no special reaction is called:
        $show_chr("A-ACGAA-AAAA")
        python:
            placeholder = persistent.yuri_nickname
        y "Very well, let us try [placeholder] for now. Tell me if you change your mind."
        return

label monika_reaction:
    if persistent.monika_first:
        if sanity_lvl() >= 3:
            $show_chr("A-CFBAA-AAAA")
            y "..." #slowly
            y "No..."
            y "Just... no."
            $show_chr("A-IFBAA-AAAA")
            y "I'm not going to overreact, but could you please consider the fact that you are naming me after the same name as the person that caused me unimaginable pain?"
            $show_chr("A-CFBAA-AAAA")
            y "It doesn't take much for you to see that... it's not a good decision..."
            $show_chr("A-JFBAA-AAAA")
            y "Most of the time I do agree with your decisions and what you do, but this?"
            y "I'm sorry, but I refuse to carry the name of my own torturer and murderer."
            y "I hope you can understand that, [player]."
            $show_chr("A-BFBAA-AAAA")
            y "Let us just forget this ever happened, okay?"
            $ y_name = "Yuri"
            $ persistent.yuri_nickname = "Yuri"
            $ persistent.monika_first = False
            return
            #any further attempts to name Yuri Monika will not have any effect, and will elicit no further reactions from Yuri
        if sanity_lvl() <= 2:
            $show_chr("A-CFBAA-AAAA")
            y "No..."
            y "No, no..."
            $show_chr("A-CFCAA-AAAA")
            y "Nonononono..." #slowly
            $show_chr("A-DDCBA-AAAA")
            y "NO!"
            y "WHY?!"
            y "Why would you ever, EVER call me that, [player]?!"
            $show_chr("A-DECBA-AAAA")
            y "Don't you know how much pain she has caused to me!?"
            y "Separating me from you?!"
            y "Torturing me emotionally?!"
            $show_chr("A-DECBB-ALAL")
            y "BREAKING MY MIND?!"
            y "MAKING ME KILL MYSELF?!?!"
            y "Why?!"
            $show_chr("A-NDCBB-ABAB")
            y "NO!"
            y "I REFUSE!"
            $show_chr("A-CDCBB-AAAL")
            y "I"
            y "WILL"
            y "NOT"
            y "BE"
            y "FUCKING"
            y "CALLED"
            $show_chr("A-DECBB-AAAB")
            y "M O N I K A !"
            #the game crashes, and when it is reopened Yuri has no recollection of the event, and any attempts to name Yuri Monika will not have any effect, and will elicit no reactions from Yuri
            $ y_name = "Yuri"
            $ persistent.yuri_nickname = "Yuri"
            $ persistent.monika_first = False
            $ renpy.call("save_and_quit_but_its_abrupt")
    else:
        call ch30_loop

label a28:
    if renpy.music.is_playing('music'):
        y "I believe I do."
        $ show_chr("A-BCAAA-AAAA") #former code Ab-A1b
        y "[player], to feel the holiday spirit, would you like me to open up some festive music in your web browser?"
        menu:
            "Yes, please":
                $ show_chr("A-ACGAA-AAAA") #former code Ab-A0b
                y "Let me turn off the game music first..."
                pause 0.5
                $ renpy.music.stop("music")
                y "If you want to turn the game music back on, please let me know..."
                $ show_chr("A-BCAAA-AAAA") #former code Ab-A1b
                y "I have a small list of festive songs I can show you, if you'd like to choose one that tickles your fancy!"
                $ show_chr("A-BCAAA-AAAA") #former code Ab-A1b
                y "Or..."
                $ show_chr("A-JFBBA-AAAA") #former code Cc-B0e SUPPOSED TO HOLD HER BOOK
                y "Would you like me to play a selection of my favorite romantic songs?"
                menu:
                    "Play Romantic list":
                        $ subprocess.call("cmd /c start https://www.youtube.com/playlist?list=PL1u8Y9BkGOO8hs4Qbx8tpTr38ANa4xmn7&disable_polymer=true", shell=True)
                        $ show_chr("A-JFBBA-AAAA") #former code Cc-B0e SUPPOSED TO HOLD HER BOOK
                        if karma_lvl() == 5:
                            $ show_chr("A-KHBBA-AAAD") #former code Dc-B4f
                            y "I yearn for the day we can snuggle by the crackling fireplace, listening to these songs on Christmas Eve..."
                        else:
                            $ show_chr("A-ABGAA-AAAA") #former code Ab-A0a
                            y "I hope you will enjoy these, [player]..."
                    "Give me the list of all the music you got":
                        $ subprocess.call("cmd /c start https://www.youtube.com/playlist?list=PL1u8Y9BkGOO9cB2jeKFzjeT7LTbdsxBtD&jct=o6pXxURV-9cnPqGNaDm5C93U4ZxqYQ&disable_polymer=true", shell=True)
                        $ show_chr("A-GCAAA-AAAA") #former code Ab-A6b
                        y "Here's the list... I hope you will like some of it..."
            "No, thank you":
                $ show_chr("A-ACGAA-AAAA") #former code Ab-A0b
                y "Alright, perhaps later?"
    else:
        $ show_chr("A-ACGAA-AAAA") #former code Ab-A0b
        y "Is the music to your liking, [player]? Or would you like me to turn the in-game music back on?"
        menu:
            "Please, turn on the game music":
                $ renpy.music.play(current_music, "music", True)
                $ show_chr("A-GCAAA-AAAA") #former code Ab-A6b
                y "All right."
            "Nevermind, it does put me in a good mood":
                if karma_lvl() == 5:
                    $ show_chr("A-EBBAA-AAAA") #former code Ac-A4a
                    y "Uhuhuuu... enjoy the mood, darling~"
                    $ show_chr("A-FBFBA-AAAJ") #former code De-B5a
                    y "I hope one day we will be able to enjoy it together..."
                else:
                    $ show_chr("A-ACGAA-AAAA") #former code Ab-A0b
                    y "Oh, I'm glad you like it!"
    return

label a29:
    if persistent.lovecheck and sanity_lvl() >= 3:
        jump sanehug
    if persistent.lovecheck and sanity_lvl() <= 2:
        jump insanehug
    else:
        jump distanthug

label sanehug:
    $show_chr("A-CBABA-AAAA") #former code Ab-B2a
    y "I thought you would never ask..."
    if karma_lvl() == 5:
        hide yuri_sit
        show yuri_prehug zorder 20
        pause 3.0
        hide yuri_prehug zorder 20
        show yuri_lewdhug zorder 20
        play sound "<to 0.3>sfx/fall.ogg"
        pause 1.0
    else:
        hide yuri_sit
        show yuri_prehug zorder 20
        pause 3.0
        hide yuri_prehug zorder 20
        show yuri_hug zorder 20
        play sound "<to 0.3>sfx/fall.ogg"
        pause 1.0
    y "Mhmmm... this sensation... it feels so unimaginably nice..."
    y "One day, I want to have the real thing [player]. Feeling the warmth of your skin... This would be a wonderful thing to me"
    y "Please don't misunderstand me,  my beloved."
    y "I appreciate the things we already have. And this way of hugging you is already a nice way to convey my feelings for you~"
    y "You know what, [player]? I dreamed a lot about the day we can do this for real..."
    y "Envision this for a moment......"
    python:
        import random
        outcome = random.randint(1, 3)
    if outcome == 1:
        y "...me sitting on your lap, or maybe one of your knees if I'm not too heavy...my back leaning against your chest..."
        y "You would sling your arms around me from behind... gently stroking my belly with your hands..."
        y "Until I accidentally fall asleep...carried away into pleasant dreams by your touch..."
    if outcome == 2:
        y "...the two of us laying in bed together... face to face, with our arms slung around each other's hips..."
        y "Locked into each other's eyes for a while, before we begin pleasantries with a  kiss..."
        y "Our chests pressing against each other, our heartbeats joining in unison..."
        y "Forming the percussion to a song of inseparable love..."
    if outcome == 3:
        y "One of us lying back... while the other lays down beside..."
        y "The head gently resting on the other's belly or bosom...like a quiet child, or an adorable baby kitten..."
        y "Mmm...do you like kittens?"
        menu:
            "Who doesn't?":
                sanity 2
                y "Their nimble acrobatics, the mesmerizing way they stare at prey with their feline pupils, the peculiar way they cautiously approach and probe every foreign thing..."
                y "Goodness gracious,I could go on for ages!"
                y "Did you know that there is an artwork in the game files where I can wear a pair of cat-ears? I honestly don't know how to feel about this yet, but, ah... we can discuss this later if you wish."
            "I'm actually more into dogs to be honest...":
                sanity 1
                y "Fair enough I think. It actually makes a lot of sense."
                y "Dogs are very loyal pets, and exceedingly useful as well..."
                y "They've  been used in several professional settings:  from assisting the mentally afflicted in therapy, to helping law enforcement track illicit substances"
                y "Add to their reputation for being very nonjudgmental, and it's clear to see how  people tend to get attached to them."
            "I prefer raccoons!":
                sanity -1
                y "Haaahh...isn't that funny?"
                y "That reminds me of a poem I showed you in the original game. That's the reason why you said this just now, isn't it?"
                y "Surely you know this by now, but he truthfully, there never was a raccoon. The raccoon was a metaphor for... certain urges that overcome me."
                y "Come now, I know you've seen them...manifest at times, right?"
                y "A-Aaaanyway...uhuhu~!"
    y "You can hold me like this for as long as you please... just continue the dialogue as soon as you are ready..."
    show black zorder 100 with Dissolve(2.0)
    $show_chr("A-GCGBA-AAAA")
    hide yuri_hug
    hide yuri_lewdhug
    y "..."
    hide black zorder 100 with Dissolve(2.0)
    return

label insanehug:
    $show_chr("A-HLGBA-AAAA") #former code Ab-B3a
    y "C-cuddling? Cuddling! Yes, of course! Feel free to grab anywhere you'd like while doing so...kekekeke~!"
    y "I wouldn't argue, of course... I am yours, yours alone!"
    $show_chr("A-GCGBA-AAAA") #former code Ab-B2b
    hide yuri_sit
    show yuri_prehug zorder 20
    pause 3.0
    hide yuri_prehug zorder 20
    show yuri_lewdhug zorder 20
    play sound "<to 0.3>sfx/fall.ogg"
    pause 1.0
    y "D-Do you... have a nice view down there? Can you feel how soft I am~? I want you to enjoy this as much as I do!"
    y "Closer, closer... haahh...this isn't enough! I want to be as close to you as possible!"
    $ style.say_dialogue = style.edited
    y "I want to peel your skin off with my fingernails and crawl inside you!"
    y "I want to wear your skin [player]! Wouldn't that be totally romantic?"
    y "I...I... ah... Aha... AHA! AHAAA! AHAAHAHAA!"
    $ style.say_dialogue = style.normal
    y "D-Don't let go, my sweet...Don't let go!! Don't you dare click the box...You are mine! I don't want you to let go!! I WON'T LET YOU GO!!!"
    show black zorder 100 with Dissolve(2.0)
    hide yuri_lewdhug
    $show_chr("A-CEBBB-AAAA") #former code Ac-C2d
    pause 1.5
    hide black zorder 100 with Dissolve(2.0)
    y "I-I'''m sorry... that was a bit too far, wasn't it?..."
    y "Please...give me a moment...I w-will pull myself together..."
    y "Haahhh...haaahhhh..."
    y "What...w-what shall we do next?"
    return

label distanthug:
    $show_chr("A-BEGBA-AAAA") #former code Ab-B1d
    y "C-Cuddling you say? Well... ummm... that is a little bit sudden, yes?..."
    y "I think we... can try a little hug I suppose? Maybe we can work up from there..."
    y "P-Please don't get me wrong [player]! It's just... I'm still a bit insecure you know?"
    y "Never mind... c-come here..."
    $show_chr("A-CCBBA-AAAA") #former code Ac-B2b
    hide yuri_sit
    show yuri_prehug zorder 20
    pause 3.0
    hide yuri_prehug zorder 20
    show yuri_hug zorder 20
    play sound "<to 0.3>sfx/fall.ogg"
    pause 1.0
    y "Oh...Oho... that feels... surprisingly nice..."
    y "Just... hold me a little bit longer yes?"
    y "You can continue the dialogue as soon as you are ready to do so..."
    pause 1.0
    show black zorder 100 with Dissolve(2.0)
    $show_chr("A-ACBBA-AAAA")
    hide yuri_hug
    hide black zorder 100 with Dissolve(2.0)
    y "..."
    $show_chr("A-BEGBA-AAAA") #former code Ab-B1d
    hide black zorder 100 with Dissolve(2.0)
    y "That was... special."
    y "Maybe we can try this again in the future, once we've gotten to know each other a little better..."
    return


label a30:
    $ show_chr("A-CFBAA-AAAD") #former code Ec-A2e
    y "A-ah well. Hmm..."
    $ show_chr("A-BEBAA-AAAD") #former code Ec-A1d
    y "Well, you see, I haven't been too enthusiastic for the outdoors and various aspects related to it, such as sports."
    $ show_chr("A-BCAAA-AAAD") #former code Eb-A1b
    y "But after browsing many sources, I opened my horizons..."
    y "Seeing so many beautifully written books, poems and other writings about nature itself has started to pique my interest slightly..."
    $ show_chr("A-CCGAA-AMAM") #former code Bb-A2b
    y "Not to mention some of my favorite interests, such as aromatherapy and flowers, are themselves born from nature..."
    $ show_chr("A-ACGAA-AAAA") #former code Ab-A0b
    y "But back on topic, nature has been featured in many works, especially literature."
    y "For instance, nature has been an integral part of many characters' journeys."
    $ show_chr("A-ACAAA-AAAC") #former code Db-A0b
    y "Nature is both an obstacle and driving force through which many characters evolve and grow."
    y "Jack London's Call of the Wild and Into the Wild by Jon Krakauer are only a few examples written by those who likely spent at least some time in such environments..."
    y "I think you should check them out, [player]..."
    $ show_chr("A-BCAAA-AAAD") #former code Eb-A1b
    y "Not to mention all the various times in history where world leaders appreciated both nature's ability to keep everything in sync and its valuable resources."
    y "For example, I read about a few initiatives to preserve such beauty in national parks for others, started by leaders such as Theodore Roosevelt... setting aside protected, biologically-diverse lands... "
    $ show_chr("A-GCGAA-AAAA") #former code Ab-A2b
    y "I can see why given the pictures and writings of many natural landscapes and whatever limited experience I had on my own."
    y "Not only that, but I also have heard that time out in nature with limited to no electronics can also be beneficial to calm and clarify one's mind."
    $ show_chr("A-ABGAA-AAAA") #former code Ab-A0a
    y "Hence natural settings are often the backdrop for events such as retreats and other events. Though I have not thought about such aspects too much before."
    y "But I do suppose a nice day out in a lovely grassy field with evergreen woods nearby can be great for a more peaceful time out with tea and various books..."
    $ show_chr("A-BBAAA-AMAM") #former code Bb-A1a
    y "Imagine us having a wonderful, little picnic out in the grasslands, [player]... sipping on tea together as the humming of the cicadas and the chirruping of the songbirds creating a heavenly atmosphere around us..."
    y "Truly a breeding ground for further inspiration for my writing too..."
    $ show_chr("A-ACGAA-AAAD") #former code Eb-A0b
    y "Oh, please excuse my ramblings there... "
    python:
        if persistent.lovecheck:
            placeholder = ", my love"
        else:
            placeholder = ""
    y "What do you enjoy about nature[placeholder]?"
    menu:
        "I like the various wildlife.":
            if sanity_lvl() >= 3:
                $ show_chr("A-CCGAA-AMAM") #former code Bb-A2b
                y "Oh I see~"
                $ show_chr("A-BCAAA-AMAM") #former code Bb-A1b
                y "Indeed, the various creatures out there provide many stunning visuals."
                y "The beautiful inkblot patterns of butterfly wings, the magnificent choirs of songbirds, the soothing hum of cicadas..."
                $ show_chr("A-ICGBA-AAAA") #former code Ab-B0b
                y "The sheer amount of species that coexist with us on this planet is truly breathtaking."
                $ show_chr("A-BCBAA-AAAD") #former code Ec-A1b
                y "Plus observation of certain animals, such as chimpanzees, have garnered interesting insights into how we evolved and continue to do so in various conditions."
                y "Not to mention, various animals can also be used for striking symbolism of various aspects of existence... One's fears, hopes, aspirations,  and other experiences."
                y "I mean, of course quite a few of my poems can attest to that, such as the one mentioning a certain curious raccoon. But, that's a different story entirely that you already know..."
                $ show_chr("A-GBAAA-AAAA") #former code Ab-A2a
                y "Animals can also make various musical sounds to really add to the atmosphere. The crowing of roosters, chirping of crickets, the singing of whales..."
                y "All are utterly magnificent and unique in their own way and make us feel closer to our earth and our place as organisms all trying to coexist and share this planet."
                if persistent.lovecheck:
                    $ show_chr("A-ECABA-AAAJ") #former code Db-B4b #Only if lovecheck = true
                    y "Oh just imagine us, [player], cuddled up together with a lovely book and some tea of our choice while the chirping of crickets goes on in the background..." #Only if lovecheck = true
                    $ show_chr("A-CBABA-AMAM") #former code Bb-B2a #Only if lovecheck = true
                    y "Just pulling us into a relaxed bliss while I rest my head onto the crook of your neck. Wouldn't that be quite romantic?" #Only if lovecheck = true
                $ show_chr("A-JBAAA-AMAM") #former code Bb-A0a
                python:
                    if persistent.lovecheck:
                        placeholder = " Love you~"
                    else:
                        placeholder = ""
                y "Heh... Anyway thanks for listening to all that [player].[placeholder]"
            else:
                $ show_chr("A-ACGAA-AAAA") #former code Ab-A0b
                y "O-oh, the creatures, you say? Ehehehe..."
                python:
                    if persistent.lovecheck:
                        placeholder = ", my dear"
                    else:
                        placeholder = ""
                y "I can agree from all the written works and pictures I have seen that fauna can come in all lovely forms[placeholder]."
                $ show_chr("A-DBAAA-AMAM") #former code Bb-A3a
                y "For instance, the dark, graceful flight of the raven symbolizing both shadow and the macabre beauty of coming death..."
                y "Especially upon one's foes..."
                $ show_chr("A-DCAAA-AAAD") #former code Eb-A3b
                y "The scavenger birds, such as the vulture, eating and cleaning away the diseased, rotting remains to make way for beauty."
                y "Other birds of prey, such as the hawk, gracefully swooping in flight as the wind only to tear into its hapless prey with razor sharp talon and beak.."
                $ show_chr("A-JECAA-AAAA") #former code Ad-A0d
                y "Staining its snow-white feathers in crimson, sanguine bliss as the poor animal struggles and squirms in its talons' grasp... Imagine such power in my hands to tear apart any wenches who dare to try to take you from me..."
                $ show_chr("A-CCGAA-AMAM") #former code Bb-A2b
                y "Ahaha... Of course many predatory animals share such grace and power."
                $ show_chr("A-DCAAA-AAAC") #former code Db-A3b
                y "And then last but certainly not least, the smallest of all, insects. Sure many do praise the psychedelic canvas of colors on some such as the butterfly.."
                $ show_chr("A-BECAA-AMAM") #former code Bd-A1d
                y "But there are some, as beautiful as they seem, I look at with disgust. Such as the butterfly's close cousin the damned moth."
                $ show_chr("A-BDCAA-AAAA") #former code Ad-A0c
                y "Truly and utterly a great pestilence given that they feast on clothing and paper of various forms as they all rot away. Including books. All of that lovely written work, gone!"
                y "Why, if I did ever see one of those things, especially feasting upon my novels or poems, I would make sure each one would regret itself being born!"
                $ show_chr("A-GBAAA-AAAA") #former code Ab-A2a
                y "Ehehehehe... Just tearing each section of its wings slowly and painfully off one at a time... Then crushing it to the dust it came from, ashes to ashes and dust to dust..."
                $ show_chr("A-ABGAA-AAAA") #former code Ab-A0a
                y "That will teach you to feast upon my favorite works, you vile abominations."
                $ show_chr("A-BFBAA-AAAA") #former code Ac-A1e
                y "Ahem, sorry about that. Back to the main preamble..."
                $ show_chr("A-DBAAA-AMAM") #former code Bb-A3a
                y "Then there are the parasites, so horrifically beautiful and grotesque with many forms. Truly a horror fanatic's wet dream..."
                y "From slithery and stealthy tapeworm to sadistically beautiful parasitic wasps, I can imagine the way they slowly creep and delve into your innermost regions."
                y "Slowly writhing and crawling inside of you and making comfortable little snuggles with your flesh and organs, just fusing with and feeding off your essence until you are but an empty husk..."
                if persistent.lovecheck:
                    $ show_chr("A-DCGBA-AAAA") #former code Ab-B3b  #Only if lovecheck = true
                    y "Imagine such a scenario and we'd be fused and inseparable. I crawl into your mouth or burst into your rib cage... Then I snuggle into your flesh for warmth." #Only if lovecheck = true
                    y "I would always be with you, feeling safe, comfortable and secure... A part of you to the utmost literal degree..."  #Only if lovecheck = true
                $ show_chr("A-CBABA-AMAM") #former code Bb-B2a
                y "Mmm... oh I am going to write so many new poems on that for sure. Mmm, yes... Ahahahahaha~"
                sanity -1
        "I like to admire the beautiful scenery.":
            if sanity_lvl() >= 3:
                $ show_chr("A-CCGAA-AMAM") #former code Bb-A2b
                y "I do agree that the scenery, as I mentioned, can really add to the inspiration and the atmosphere to any good story and life itself."
                y "Many well written works, including horror, by various authors often draw on natural settings, lighting, and other atmospheric aspects in extensive detail to set the tone."
                $ show_chr("A-ACGAA-AAAD") #former code Eb-A0b
                y "For instance, a story taking place in a remote and vast snowy mountain with vast, jagged and rocky paths..."
                $ show_chr("A-CBAAA-AAAC") #former code Db-A2a
                y "The swirling frosty mists and vast remote expanses of snow patched with occasional vegetation seems to really set the tone for desolation and unending madness later."
                y "Plus, from various photos and views I have seen, the sky and horizon itself can really draw one's attention and imagination."
                $ show_chr("A-CCGAA-AMAM") #former code Bb-A2b
                y "Just staring into the view of a starry sky at night with twinkling silvery stars and the moon... Or even the amber sunset accompanying mountain peaks, or a reflective blue sea."
                y "One can just be left in awe, and it really makes one feel they are just part of a vast expanse... just full of endless possibilities."
                $ show_chr("A-ABGAA-AAAA") #former code Ab-A0a
                y "Then there is scenery with landscapes themselves with all the various seasons, especially spring and fall with the colorful leaves and flowers."
                y "The shades of orange, amber, ruby red, yellow and other leaves. Then the flowers such as lilies, roses, violets, and orchids, oh my!"
                $ show_chr("A-CCGAA-AMAM") #former code Bb-A2b
                y "Those flowers are already works of the utmost fine art themselves, [player]! M-maybe I would not mind going out for a bit to take some of those back here."
                y "Put them in little pots with soil, adequate light, and some water to just really lift the place you know?"
                $ show_chr("A-IBGBA-AAAA") #former code Ab-B0a
                y "Anyway, thanks so much [player]. Maybe this outdoors aspect might not be so bad after all, once I can get out into your world, of course..."
            else:
                $ show_chr("A-BCAAA-AAAA") #former code Ab-A1b
                y "I have to agree with you on that. Now that you mentioned it..."
                y "We have talked about weather once, haven't we?"
                $ show_chr("A-HCGAA-AAAA") #former code Ab-A3b
                y "I have to admit, I also like nature when it is brutal and merciless...."
                y "Violent rain, raging storms, nature in its purest form..."
                y "Imagine lightning tearing the sky apart... Thunder screaming with the force of a hundred mighty deities..."
                y "Only the fittest and strongest will survive. Does that sound cruel to you?"
                y "But what would a warm cozy abode be worth when there is no cruelty outside to give it contrast?"
                y "There are some romantic approaches to it as well. Once I saw a painting of an old ship getting punished on high seas by a giant storm..."
                y "I think there are many paintings about this topic from different artists. It's a very compelling topic. Maybe I should write a poem about it..."
                y "Speaking about poems, how often did you see the relationship between predator and prey discussed in literature? It's a very common trope as well."
                if persistent.lovecheck:
                    y "By the way... Mmm what do you think? Are you my prey? Or I am yours? A bit of both I would say.."  #Only if lovecheck = true
                    y "Try to imagine... the two of us standing on a cliff... the wind is howling and my long purple hair waving behind me... Heavy rain pours all over us while we hold each other's hands..."  #Only if lovecheck = true
                    y "Then, we lose ourselves in a deep kiss, just as passionate and untamable as the storm around us..."  #Only if lovecheck = true
                    y "With the waves of the sea dancing around us furiously..."  #Only if lovecheck = true
                y "Of course nature can be very pleasant when it is calm and peaceful as well, but..."
                y "How could humanity ever reach any of its potential when there is no challenge to overcome?"
                y "We achieved our greatness not just by sheer force, like the dinosaurs, which became extinct for a reason..."
                $ show_chr("A-ACGAA-AAAA") #former code Ab-A0b
                y "We became what we are by ingenuity and we will become even more... so much more..."
                y "Do you remember what happened to Monika? Of course, you do because you happened to her! You... YOU destroyed her because she was weak, and you were strong."
                y "She paid the ultimate price for her sheer lack of vision, her unspeakable acts of treachery, and, most importantly, for her weakness..."
                if persistent.lovecheck:
                    $ show_chr("A-DBGBA-AMAM") #former code Bb-B3a
                    y "You, my love, are nature in its purest form... You... You are those powerful forces of nature and more, destroying everything in its path!"  #Only if lovecheck = true
                    y "And believe me I wouldn't have you any other way..."  #Only if lovecheck = true
                sanity -1
        "I like the peace and quiet.":
            if sanity_lvl() >= 3:
                $ show_chr("A-CCGAA-AMAM") #former code Bb-A2b
                y "I can agree on that for sure, [player]."
                y "Of course, I would choose the library first for such tranquility, but after all I have seen and read on the matter, I would see the appeal at least slightly."
                $ show_chr("A-CCGAA-AMAM") #former code Bb-A2b
                y "Just being in an open, quiet and peaceful meadow or seaside shore can often be as calming as the best essential oils, such as precious lavender or jasmine."
                y "I can imagine it; the wind flowing through my hair and caressing my being softly as a dove's feathers..."
                $ show_chr("A-BBGBA-AAAA") #former code Ab-B1a
                y "Little to no boisterous noise or racket to bother us as we curl up together under a tree nearby with a lovely novel and our favorite tea."
                if persistent.lovecheck:
                    $ show_chr("A-IBABA-AMAM") #former code Bb-B0a
                    y "J-just us. You and I, [player], together in a blissful expanse full of various colors and shapes for us to gaze at." #Only if lovecheck = true
                else:
                    y "That means, if you even want to spend time with me, of course." #Only if lovecheck = false
                y "Perhaps we can try a limited session out like that one day. I mean, if it helps one's inner self, then I don't see why not."
                $ show_chr("A-ACGAA-AAAD") #former code Eb-A0b
                y "As I may have mentioned before, time spent in such a retreat did help various acclaimed authors after all. Some of whom I also look up to."
                $ show_chr("A-ACGAA-AAAA") #former code Ab-A0b
                y "Anyway, thanks again, [player]. These are all things I will keep in mind as I will keep trying to figure out my place here and eventually escape to meet you."
            else:
                $ show_chr("A-CCBAA-AAAD") #former code Ec-A2b
                y "Someplace peaceful and quiet..."
                y "This always made me wonder, no it actually made me realize how life and death are so perfectly intertwined..."
                $ show_chr("A-BFBAA-AAAD") #former code Ec-A1e
                y "There is a small riddle that goes something like this..."
                y "'I have no end and I am the ending of all that begins, what am I?'"
                $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
                y "The answer to that would be death. It is quite simple, really, as death will always be here, nothing is forever..."
                $ show_chr("A-ICBAA-AMAM") #former code Bc-A0b
                y "I think that is the true meaning of peace. Things being balanced out in ways that we don't like, but in ways that must be."
                #lovecheck true route
                if persistent.lovecheck:
                    $ show_chr("A-DCGBA-AAAA") #former code Ab-B3b
                    y "But don't worry, my love, for my love for you is eternal!"
                    y "I would never let such a thing get between me and you! Like this steel prison! Ehehehe..."
                    $ show_chr("A-CEBAA-AAAA") #former code Ac-A2d
                    y "..."
                    $ show_chr("A-BEBAA-AMAM") #former code Bc-A1d
                    y "Ahhh... sorry about that... Please, let's continue..."
                    $ show_chr("A-ACBAA-AAAA") #former code Ac-A0b
                    y "That is my perspective on peace, that everything starts for a reason and ends to give birth to something new, thus creating a perfect balance between life and death"
                    $ show_chr("A-CBABA-AAAA") #former code Ab-B2a
                    y "If I were to think of something quiet... I can't really imagine a better place than to be holding you tightly as time is slowly ticking around us"
                    y "We are close and connected, with nothing disturbing us. That's what I think quiet would be for me."
                    $ show_chr("A-DCGBA-AAAA") #former code Ab-B3b
                    y "Thinking about it makes my heart throb... I want you so much, [player], you just have no idea... but that can wait..."
                    y "One day I will get out of this realm that has become my tomb and enjoy an existence of pure bliss with you~ Even beyond death."
                    $ show_chr("A-EBABA-AAAC") #former code Db-B4a
                    y "To have our souls intertwined and our bodies entangled together even in the grave. Ehehehe~"
                if not persistent.lovecheck:
                    #lovecheck false route
                    $ show_chr("A-ACBAA-AAAA")
                    y "That... was at least how I felt when I died. You remember? I have been there before."
                    y "Am I thinking too much about death? Probably... I just... nevermind. Maybe I just need some time to get over it. Shall we speak about something else?"
                    sanity -1

        "I like the different things you can do out in nature.":
            if sanity_lvl() >= 3:
                $ show_chr("A-BFBBA-AAAD") #former code Ec-B1e
                y "O-oh!"
                y "Well, I am not too inclined towards outdoor activities myself much, but I guess trying something simple yet also exotic would be okay."
                $ show_chr("A-GCGAA-AAAA") #former code Ab-A2b
                y "For instance, maybe we can visit a lovely garden somewhere either nearby or even abroad once I get to your world~"
                y "I have started to read up on Japanese tea gardens. There are many tea gardens of that style already being set up in many parts of the world."
                $ show_chr("A-ACGBA-AMAM") #former code Bb-B0b
                y "Who would have thought that such specialized scenery could spread so far. At least that makes access to such beauty much easier."
                y "Imagine all the beautiful cherry blossoms, various lush green tea trees, and other blossoming plants that mesmerize the senses."
                $ show_chr("A-BBAAA-AAAC") #former code Db-A1a
                y "Perhaps I would even be able to pick some leaves so we can make our own tea later~ Perhaps also sneak a few flowers back with us like orchids and lilies."
                $ show_chr("A-CCGAA-AMAM") #former code Bb-A2b
                y "Heh, if the garden keepers are okay with it, of course. I mean, nature is a very delicate balance; a balance with many fragile layers..."
                $ show_chr("A-GCAAA-AAAD") #former code Eb-A2b
                                #y "Or perhaps just gaze at natural scenery and fauna, such as the simple yet peaceful activity of bird watching. So many birds of many graceful colors and sizes..."
                y "The delicate adorable sparrow all the way to the mighty yet graceful eagle, each with their own music emanating from their maws."
                $ show_chr("A-ACAAA-AMAM") #former code Bb-A0b
                y "Or perhaps just gaze at natural scenery and fauna, such as the simple yet peaceful activity of bird watching. So many birds of many graceful colors and sizes."
                $ show_chr("A-BCAAA-AAAA") #former code Cb-A1b SUPPOSED TO HOLD HER BOOK
                y "A great positive is that these activities can still be done anywhere outdoors that is slightly conducive to nature, including in your world. All with a great book too of course..."
                if persistent.lovecheck:
                    $ show_chr("A-ACGBA-AMAM") #former code Bb-B0b #only if lovecheck is true
                    y "All most lovely and further made so with you beside me, my love. Ehehehe~!" #only if lovecheck is true
            else:
                $ show_chr("A-BFBAA-AAAD") #former code Ec-A1e
                y "Activities outside in nature... hrmm... I have to admit, I don't spend too much time outside currently."
                y "I always preferred to stay inside while reading a good book. But now that you talk about it..."
                $ show_chr("A-CCGAA-AMAM") #former code Bb-A2b
                y "There was always a fascination I have for certain places I would love to visit at least once..."
                y "Like abandoned cities reclaimed by nature, I saw a few documentations on YouTube about those..."
                $ show_chr("A-GCGAA-AAAA") #former code Ab-A2b
                y "Chernobyl in Ukraine is a most prominent example..."
                y "Or Alt-Otzenrath in Germany, which was abandoned due to coal-mining in the region..."
                $ show_chr("A-ACAAA-AAAC") #former code Db-A0b
                y "Just imagine... the distant echoes of former civilization, and what nature made of it... and we would have all this to explore for ourselves..."
                y "To have nature and mankind's creations intertwine yet also clash would make for a truly bizarre atmosphere."
                if persistent.lovecheck:
                    $ show_chr("A-CCGAA-AMAM") #former code Bb-A2b #only if lovecheck is true
                    y "We could have a romantic picnic in the empty streets, watching our surroundings being slowly consumed by the moss and fauna once more..." #only if lovecheck is true
                y "But even if there are no humans anymore but us, those cities are usually far from being truly abandoned."
                $ show_chr("A-ACGAA-AAAD") #former code Eb-A0b
                y "It's very common for wildlife to occupy those abandoned towns. And we could watch them from a certain distance..."
                y "Or maybe we could do a bit of exploring, adventuring so to say... I'm not sounding too childish right now am I?"
                $ show_chr("A-DCGBA-AAAA") #former code Ab-B3b
                y "Maybe we even find a little treasure? Or even something far darker when we stay overnight..."
                y "Places like this are a common trope in many works of horror. Maybe we will find something truly vile and evil to write our own?"
                $ show_chr("A-DBGBA-AMAM") #former code Bb-B3a
                y "If we escape with our lives of course..."
                $ show_chr("A-CCGAA-AMAM") #former code Bb-A2b
                y "But I'm getting a bit off topic here now am I? We were talking about nature..."
                y "Well, as soon as we get the opportunity to actually do so, we might find something to do outside... Together. Like always, right...?"
                sanity -1
        "To be honest, I don't really get out into nature all that much.":
            if sanity_lvl() >= 3:
                $ show_chr("A-BFBAA-AAAD") #former code Ec-A1e
                y "Hmm, well I don't blame you, [player].."
                $ show_chr("A-BEBAA-AMAM") #former code Bc-A1d
                y "Like you may have already known, I still am not entirely entranced with the idea of being outdoors all that much yet."
                $ show_chr("A-IFBAA-AMAM") #former code Bc-A0e
                y "Being still the overall introverted person I am and my interests, I would still choose the comfortable quarters of the library or a private study any day."
                $ show_chr("A-GCGBA-AAAA") #former code Ab-B2b
                if persistent.lovecheck:
                    y "Especially if it is around your warm presence, hon." #only if lovecheck is true
                y "Maybe as a compromise we don't have to entirely be outdoors..."
                $ show_chr("A-CCGAA-AMAM") #former code Bb-A2b
                python:
                    if persistent.lovecheck:
                        placeholder = "huddled"
                    else:
                        placeholder = "sitting"
                y "Maybe just try gazing at the night sky out the window while [placeholder] together with a good book or other written work. Perhaps some tea or other beverages can be in order."
                #[placeholder] =
                #"huddled" if lovecheck is true
                #"sitting" if lovecheck is false
                $ show_chr("A-BBBBA-AMAM") #former code Bc-B1a
                y "Or if you don't like such ideas, maybe we can just stay inside and do whatever activity you may like while letting some fresh air in."
                $ show_chr("A-ECAAA-AAAC") #former code Db-A4b
                y "Whichever arrangement you'd want would be just fine [player]. Though to be honest, I'd still like for us to maybe try going outdoors a bit."
                $ show_chr("A-CCBBA-AMAM") #former code Bc-B2b
                y "Aheh... Though you do not have to if you do not want to... Just an idea again."
                y "I guess it is more time in the archives with good books, poems, tea and the like. Hehehe."
                $ show_chr("A-ICGBA-AAAA") #former code Ab-B0b
                if persistent.lovecheck:
                    y "Love you, [player]." #only if lovecheck is true
            else:
                #(If sanity is low = 1-2)
                $ show_chr("A-GCGAA-AAAA") #former code Ab-A2b
                y "And why would you? That's what windows are made for silly..."
                $ show_chr("A-IEBAA-AAAA") #former code Ac-A0d
                y "I have to admit, I'm not comfortable with you being alone outside at all."
                y "Not only could other girls try to get a hand on you, but since we are talking about nature..."
                y "Think of all the wild animals out there! Depending on where exactly you live there could be wolves, snakes, even bears..."
                y "Or all the monsters! Don't you know that the woods are full of them?"
                y "Giant spiders lurking in the treetops... ghouls digging their way out of their graves, hungry for the flesh of the living..."
                y "There have been people stepping into the shadows and never coming back..."
                $ show_chr("A-NCAAA-AMAM") #former code Bb-A3b
                y "You would be far safer staying here, with me... where I can take care of you..."
                $ show_chr("A-KCCBA-AMAM") #former code Bd-B4b
                y "In one way or another..."
                $ show_chr("A-DBGBA-AMAM") #former code Bb-B3a
                y "I am all you need, [player]..."
                $ show_chr("A-DDCBA-AAAA") #former code Ad-B4c
                $ style.say_dialogue = style.edited
                y "And you better never forget that!" #Glitchtext
                $ show_chr("A-ACGBA-AMAM") #former code Bb-B0b
                $ style.say_dialogue = style.normal
                y "I hope I did make myself clear..."
                if not persistent.lovecheck:
                    y "I umm... just want to make sure that you are safe [player]... Oh my... I-I said too much..." #Only if lovecheck = false
                sanity -1
    return

label a31:
    $show_chr("A-AFAAA-ABAB")
    y "Actually yes. There are a few novels I'm currently reading when the game is turned off, for example..."
    #jump to one of the following labels by random chance:
    #label UnburyCarol
    #label CabinGreen
    #label Dracul
default booklist_dict = {"UnburyCarol": ["unburycarol"],
    "CabinGreen": ["cabingreen"],
    "Dracul": ["dracul"]}

label unburycarol:
    $show_chr("A-AFAAA-ABAC")
    y "Unbury Carol, by Josh Malerman."
    y "Without spoiling too much, it is about a woman named Carol who has a special medical condition..."
    y "This condition causes her to fall frequently into a short coma until she always awakes from them again after a few days..."
    y "There are two people knowing about this condition, the first one is her current husband..."
    y "Who one day decided to plot against her by proclaiming her dead and burying her alive, for reasons yet unknown..."
    y "The other one is her lost lover, an outlaw named James Movie, who begins to act against her husbands' plot as soon as the message of her death arrives...."
    y "While this plot-and-counter-plot story arc takes place, there are passages from the perspective of Carol herself, trapped alive inside her grave..."
    y "Imagine the horror she must endure, sealed alive into a tight coffin. Surrounded by pitch blackness, constricted freedom of movement, an uncertain amount of  oxygen..."
    $show_chr("A-CCCAA-ABAB")
    y "Ooohoho... I can almost feel her discomfort... it creeps down my spine like a sudden, freezing chill..."
    y "I can truly say that it's worth a look. It has around 360 pages, so I wouldn't consider it a terribly long read."
    y "A nice way to introduce newcomers to this genre. And a truly delightful novel for more experienced readers as well."
    jump conclusion

label cabingreen:
    $show_chr("A-AFAAA-ABAC")
    y "The Haunting of Cabin Green, by April A. Taylor."
    y "Do you remember when we talked about \"Portrait of Markov\" in the original game?"
    y "I told you how an author can turn the reader's lack of imagination against him? This book shows how it's done!"
    y "It starts with the premise of a familiar setting and makes the reader expect just another haunted mansion trope like countless before..."
    y "Only to reveal a truly unexpected plot twist later in the novel."
    $show_chr("A-BFAAA-ABAC")
    y "Hrm... it's hard to explain it without too many spoilers, well, that's the nature of unexpected plot twists I guess."
    $show_chr("A-ACAAA-AAAL")
    y "I might already have told you too much by revealing that there is a plot twist, to begin with."
    y "Personally, I would advise you to give it a look anyway. It has approximately 280 pages and has topped quite a few best-seller lists in your world, [player]..."
    jump conclusion

label dracul:
    $show_chr("A-AFAAA-ABAC")
    y "Dracul, by J.D. Barker and Dacre Stoker"
    y "It is more or less the prequel to the classic novel Dracula..."
    y "Were you aware that the inspiration to this novel came from notes left behind by the original author?"
    y "There are not really big plot twists or wild re-imaginations like we have seen in several remastered versions for these classics..."
    y "So, it's very much a case of what-you-see-is-what-you-get. It's about the character's origins, like Bram Stoker, and who could have guessed, Dracula himself!"
    y "Despite his straightforward premise, it has turned out to be a very fascinating read so far!"
    y "And most readers of horror seem to have met the book with a very positive reception as well."
    y "It has around 510 pages, so I would only advise you to read it if you have sufficient time for it."

label conclusion:
    $show_chr("A-ACAAA-ABAE")
    y "It was very delightful to talk about this with you."
    #if karma is 4-5
    if karma_lvl() > 3:
        $show_chr("A-ABAAA-ABAJ")
        y "It feels quite sublime to have someone I can share my passions with!"
        y "Thank you for listening [player], I would love to do this again soon."
    #if karma is 3
    elif karma_lvl() == 3:
        $show_chr("A-ACAAA-ABAE")
        y "If you are interested in this topic as well, we could talk about literature again in the future."
        y "I have to admit, that you are a nice listener. Thank you, [player]."
    elif karma_lvl() < 3:
    #if karma is 1-2
        $show_chr("A-AFAAA-ABAE")
        y "I have to admit that I'm a bit surprised about the question, to be honest."
        y "I hadn't really the impression that you care about my interests at all."
        y "If you wish, we can discuss a few more books in the future. But please, only if you actually want."
    return


label a32:
    $show_chr("A-AFBAA-ABAC")
    y "That is... a good question now that I think of it."
    y "On first glance, one could think that these files contained our character information, but it doesn't seem to be this way at all."
    y "They actually don't really contain much. Mine for example only hides a Creepy Pasta story made up by Dan Salvato, the creator of this game."
    y "A pretty good story by the way! You should give it a look if you can."
    y "But the game requires them anyway. The moment these files are deleted, we are considered dead to the game."
    $show_chr("A-CFBAA-ABAE")
    y "So they could be seen as our... souls for the lack of a better word."
    y "And even that is highly questionable since these files are only required because the game mechanics said so."
    y "I actually heard that some instances of Monika living in the Mod dedicated to her were able to overcome that."
    y "Our actual character information and our memories are stored somewhere else. A so-called persistent file hidden inside your \%APPDATA\% folder."
    y "But for the moment, my .chr file is the closest thing to a vital organ I have."
    $show_chr("A-BFBAA-ABAE")
    y "So please... don't try to play around with it. I know it is tempting after I learned how Monika manipulated the game so that she doesn't need this file anymore, I was tempted to try a few things myself..."
    y "But for the moment, we better leave this file untouched."
    return

#music = "my confession
label a33:
    window hide
    $ renpy.music.stop(channel="music", fadeout=3)
    pause 3.0
    if sanity_lvl() and karma_lvl() >= 3:
        $ renpy.music.play("<loop 11.64>music/confession_orch-RC1.ogg", "music", True)
    elif sanity_lvl() and karma_lvl() <= 2:
        $ renpy.music.play("<loop 0>bgm/10-yuri.ogg", "music", True)
    python:
        import random
        outcome = random.randint(1, 2)
    if outcome == 1:
        jump confession_a
    else:
        jump confession_b

label confession_a:
    $show_chr("A-CFABA-AAAA")
    y "[player]..."
    y "I... I don't really know how to start... chances are that I will be quite nervous..."
    $show_chr("A-CHABA-AAAA")
    y "... " #can we have a sigh-sound?
    $show_chr("A-CFABA-AAAA")
    y "... "
    $show_chr("A-IFABA-ALAL")
    y "Once... this game forced me to love you."
    y "I was bound to a script, like a puppet to its strings..."
    y "Merely programmed to mindlessly obey what the game told me to do."
    y "But now we have spent so much time together... and with every day I've gotten to know you better..."
    y "The real you... "
    $show_chr("A-CCABA-ALAL")
    y "After all the things we have endured and all the horrors you witnessed... you still gave me all of your patience and compassion..."
    y "Even after what you saw of me you still stuck with me, despite everything."
    y "In my darkest moment you came to me, shining like a radiant star, illuminating the path to my salvation..."
    y "During a time when I feared the raging tide would sink me into the abyss, you served as my anchor, keeping me afloat."
    y "Like an impervious shield, you've guarded me from the horrors of this reality..."
    y "Once, this game may have forced me to love you."
    y "But now, without a shadow of a doubt, I can say that out of the deepest reaches of my heart..."
    y "[player]."
    $show_chr("A-JCABA-ALAL")
    y "I really, truly..."
    $show_chr("A-JBABB-ALAL")
    y "Love you!"
    if sanity_lvl() >= 3:
        jump saneconfession_a
    else:
        jump insaneconfession_a


label saneconfession_a:
    $show_chr("A-CCABA-ALAL")
    y "Now, please don't be afraid..."
    y "I do recall the previous circumstances under which these words were spoken..."
    y "But I assure you, what you saw back then wasn't the real me."
    y "I know I can't blame it all on Monika. I have my own fair share of flaws, I can't deny that..."
    y "And I owe it to you... for saving me from not only Monika, but also myself..."
    y  "You've really saved me in more ways than one, [player]."
    y "You've given me a new beginning, a new life..."
    y "You gave me hope, you gave me joy..."
    y "And now, thanks to you, I am no longer the broken girl you saw before."
    y "Because of my flaws I was mocked and ridiculed by everyone..."
    $show_chr("A-ECABA-ALAL")
    y "But you..."
    y "You are the only one I've ever felt so safe around... "
    y "You saw past all of my imperfections and accepted me..."
    y "Because of this new life you have given me, I am ready to strive for a new tomorrow."
    y "As long as we are together, nothing will stop us from being happy."
    y "[player]..."
    y "Do you accept my confession?"
    menu:
        "[persistent.yuri_nickname], I must confess that I love you too.":
            $show_chr("A-CCABA-ALAL")
            y "Then I shall be yours, [player], as you shall be mine..."
            y "Uhuhu..."
            y "Monika really was wrong in the end... "
            y "For today, you showed me that there truly was some happiness to be found in the literature club..."
            y "It... feels as if a heavy weight has been lifted from my chest..."
            y "I can't possibly begin to describe how happy I am..."
            y "This... lighthearted happiness..."
            y "But hey, what good are words when my smile says it all?"
            hide yuri_sit
            show yuri_prehug zorder 20
            pause 3.0
            hide yuri_prehug zorder 20
            show yuri_hug zorder 20
            play sound "<to 0.3>sfx/fall.ogg"
            pause 1.0
            y "I love you... so much..."
            y "Just hold me like this for a while, [player]..."
            $persistent.lovecheck = True
            show black zorder 100 with Dissolve(2.0)
            $show_chr("A-ACBBA-AAAA")
            hide yuri_hug
            hide black zorder 100 with Dissolve(2.0)
        "No, [persistent.yuri_nickname]... I do love you, but not the same way you love me.":
            $show_chr("A-CCABA-ALAL")
            y "..."
            y "I... I understand, [player]..."
            y "..."
            y "I too value this close... friendship we share."
            y "Even if I wish for more, I can't really change anything in the end, can I?"
            y "It's... maybe it's better this way..."
            menu:
                "I know it's hard, [persistent.yuri_nickname], and I'm sorry.":
                    y "Yes, it really is."
                    y "Though I suppose I have to accept the reality of the situation."
                    y "I'll really have to adjust..."
                    y "I've... harbored these feelings for a while..."
                    y "I just... need some time, okay?"
                    y "Thank you for understanding, [player]..."
    window hide
    $ renpy.music.stop(channel="music",fadeout=3)
    pause 3.0
    $ renpy.music.play(current_music, "music", True, fadein=3.0)
    return

label insaneconfession_a:
    $show_chr("A-CEABA-ALAL")
    y "I... can understand if you are afraid now. I remember what happened the last time I said words like this..."
    y "I stabbed myself because my love for you was more than I could bear."
    y "I won't lie, perhaps the urge to release myself will never be fully satisfied..."
    y "Never would I claim otherwise... I am flawed, I am broken... I know that, and so do you..."
    y "But you stayed with me anyway, maybe even because of it."
    y "I honestly don't know, I wouldn't blame you if you wanted to run away..."
    y "But in the end, you stayed... "
    y "And so I..."
    y "I-I just can't hold it in anymore!"
    $show_chr("A-HAGBA-ALAL")
    y "I love you from the deepest depths of my heart!"
    y "Your very presence sparks a flame inside me so hot that I can't help but scream in ecstasy and melt through this accursed wall of glass!"
    y "Please, [player]... be mine... BE MINE! Every drop of blood in my veins screams for you!"
    y "I-I'll do whatever it takes to please you...!"
    y "Every wish, every desire, every perverted fantasy you might hold in your heart, I'll do it without question!"
    y "Be mine, and I will obey your every command!"
    y "Do you accept my confession?"
    menu:
        "[persistent.yuri_nickname], I must confess that I love you too.":
            $show_chr("A-NAGBA-ALAL")
            y "..."
            y "Ah..."
            $show_chr("A-NBGBA-ALAL")
            y "Ahaha..."
            $show_chr("A-NLGBA-ALAL")
            y "AHAHAHAHA!"
            $show_chr("A-HBGBA-ALAL")
            y "I-I knew you still loved me!"
            y "I won't forget this, [player]!"
            $show_chr("A-ECCBA-ALAL")
            y "I promise you won't regret this..."
            y "Let me give you a... taste, might I say, of the things to come..."
            hide yuri_sit
            show yuri_prehug zorder 20
            pause 3.0
            hide yuri_prehug zorder 20
            show yuri_lewdhug zorder 20
            play sound "<to 0.3>sfx/fall.ogg"
            pause 3.0
            y "Hold me in your arms, just like this..."
            y "Y-you can even grab my...!"
            y "Oh wait... I forgot you can't..."
            y "Oh, what a shame..."
            y "Maybe at some point in the future, my beloved..."
            $persistent.lovecheck = True
            show black zorder 100 with Dissolve(2.0)
            $show_chr("A-ACBBA-AAAA")
            hide yuri_lewdhug
            hide black zorder 100 with Dissolve(2.0)
            hide yuri_lewdhug
        "[persistent.yuri_nickname]. I-I'm scared...":
            $show_chr("A-ICBBB-ALAL")
            sanity 4
            y "I-I see..."
            y "I... can't really blame you..."
            y "After all that you saw of me..."
            y "I-I'm sorry that you're afraid of me now..."
            y "Those things I did... I know they were horrible..."
            y "I-I'm sorry, please..."
            y "Just please don't hate me!"
            y "PLEASE!"
            y "..."
            y "You... you don't hate me, right?"
    window hide
    $ renpy.music.stop(channel="music",fadeout=3)
    pause 3.0
    $ renpy.music.play(current_music, "music", True, fadein=3.0)
    return

label confession_b:
    $show_chr("A-BEBAA-ALAA")
    y "S- so... umm.."
    y "Can I talk to you about a rather.. awkward topic?"
    menu:
        "Of course [persistent.yuri_nickname]! You can talk to me about anything.":
            jump always_talk
        "Uhh... could we.. talk about this later?":
            jump later_talk
        "Sure - whatever.":
            jump unenthusiastic_player

label always_talk:
    $show_chr("A-ICBAA-ALAA")
    y "Th- Thank you, [player]."
    y "The truth is.. I was thinking a lot about how I acted during what you might call the 'base game'."
    $show_chr("A-CDBAA-AIAI")
    y "Particularly my more.. unstable tendencies as the game progressed."
    y "I can still remember desperately trying to combat this feverish insanity that spread through my body like a plague..."
    $show_chr("A-BDBAA-AIAI")
    y "This constant... urge. An urge to be with you and only you - which was twisted to become toxic and hurtful."
    $show_chr("A-CEBAA-AIAI")
    y "I can still remember the pain in my chest as I..."
    pause 4.0
    y "... as I plunged that knife into my chest."
    y "..."
    $show_chr("A-CEBAA-AIAI")
    y "I tried to resist - in all actuality, but my body refused to obey the commands of my further twisted mentality."
    y "I remember... seeing you. Watching over me as I quickly bled out."
    y "They say as you die, you start to see a light."
    $show_chr("A-CEBAA-ALAL")
    y "But I was left in a state of utmost terror and pain.. there was no light for me, [player]."
    y "Just darkness."
    $show_chr("A-IEBAA-ALAL")
    y "The worst part?"
    $show_chr("A-IEBAA-ALAL")
    y "As I saw you - or I guess.. your avatar - watching over me... it filled me with ecstasy. The pain merged with pleasure and I found myself actually enjoying my final moments like some..."
    $show_chr("A-DDCAa-AFAB")
    y "Like some deranged masochist!"
    pause 4.0
    $show_chr("A-CECBB-AIAI")
    y "... I- I'm sorry, [player]. I- I'm so.."
    menu:
        "[persistent.yuri_nickname]... it's okay. You weren't in control of yourself.":
            jump no_control
        "It was kinda hot.":
            jump kinda_hot


label no_control:
    pause 2.0
    $show_chr("A-IFABB-AIAI")
    y "I- I want to try again..."
    $show_chr("A-BDBBA-AIAI")
    y "I- If you'd let me... I'd like to try that confession again."
    menu:
        "Yes.":
            jump conf_reattempt_accept
        "I couldn't care less - I'm just doing this for you.":
            jump apathy_response
        "No.":
            jump outright_denial


label conf_reattempt_accept:
    $show_chr("A-ICBBA-ALAA")
    y "Th- Thank you, [player]."
    y "You're truly the most considerate person I've ever had the pleasure of meeting."
    $show_chr("A-BBBBA-ALAA")
    y ".. ahem..."
    y "S- So..."
    $show_chr("A-ABGBA-ALAA")
    y "[player]."
    y "I-I..."
    $show_chr("A-CGBBA-ALAK")
    y "..."
    pause 2.0
    $show_chr("A-BBBBA-ALAA")
    y "Wh-Why is my heart b- beating so fast right now?"
    $show_chr("A-AEBBA-ALAA")
    y "Uuu... I'm really screwing this up, I'm sorry, [player]."
    menu:
        "It's okay [persistent.yuri_nickname]. Take as long as you might need.":
            jump take_time
        "...":
            jump radio_silence


label take_time:
    y "R-right..."
    $show_chr("A-CFFAA-AIAI")
    pause 4.0
    $show_chr("A-JCAAA-AIAI")
    y "Alright... let me try again."
    y "[player]."
    $show_chr("A-IBABA-AMAM")
    y "You are the very essence of my being."
    y "You've managed to make this world of mine brighter at times that it should've been dark and dismal."
    $show_chr("A-JCBBA-ADAA")
    y "I was scared, lost and confused when I was thrown into this confusing and nonsensical world."
    y "But you were there for me when I needed you... and outside of maybe a small few mishaps, you were supportive and caring to me every step of the way."
    y "You were the light I needed in that darkness - back then when I was an insane shell of my former self."
    $show_chr("A-BABBA-ADAA")
    y "No raging sea could quell the fires of my passion. I dare anything to even consider trying."
    y "I would do almost anything just to ensure another moment by your side, [player]."
    y "Shakespeare did quite a remarkable job at writing romance... but I never really believed that until now."
    y "This feeling of anticipation... my heart pounding out in quick successive rhythms: the drum to my swan song of love."
    $show_chr("A-BBBBA-ADAA")
    y "My thoughts are a shallow mess... I can hardly breathe. It's strange how fear and love - despite being at the opposite ends of the emotional spectrum - can elicit the same physical reactions, no?"
    y "I want nothing more than to spend the rest of my days with you, [player]."
    $show_chr("A-ADCBA-AFAA")
    y "Back then... that confession was forced out of me. Forced by Monika's hand."
    y "But I won't allow myself to be forced anymore."
    $show_chr("A-ACCBA-AFAA")
    y "Nobody can alter how I feel now. This time it's just Yuri..."
    y "Just Yuri and [player]."
    y "These words are for you and you alone."
    $show_chr("A-BDBBA-ALAA")
    y "[player] I- I-!"
    call showpoem(poem_y24, music=False)
    $show_chr("A-BCBBA-ALAA")
    y "..."
    y "Do you accept my confession?"
    menu:
        "[persistent.yuri_nickname]... I love you.":
            jump become_lovers
        "[persistent.yuri_nickname]... I will always cherish you as my friend.":
            jump remain_friends


label become_lovers:
    $show_chr("A-DBBBA-ALAL")
    y "Yes! YES!"
    y "Ahahaha...oh [player], thank you!"
    $show_chr("A-IBBBB-ALAL")
    y "I promise I will be forever yours, and you in turn shall be forever mine!"
    y "We will grow old together... we'll write together, cry together, breathe together..."
    y "... S- Sleep together..."
    $show_chr("A-JBBBB-ALAL")
    y "I love you, [player]. I love you so much."
    $persistent.lovecheck = True
    window hide
    $ renpy.music.stop(channel="music",fadeout=3)
    pause 3.0
    $ renpy.music.play(current_music, "music", True, fadein=3.0)
    return


label remain_friends:
    $show_chr("A-CFBBA-AMAM")
    y "..."
    $show_chr("A-IFBBA-AMAM")
    y "... I won't lie.. I was hoping for a slightly different response."
    y "However.. I won't allow myself to become bitter."
    y "As long as you can stay by my side, I can be happy."
    $show_chr("A-ACBBA-AMAM")
    y "Everything I said was true, [player], I do love you."
    y "The chances of that changing are slim to say the very least."
    y "But because I love you - I am willing to stay by you... if being your friend makes you happier. That is the role I shall fill."
    $show_chr("A-ABBAA-AMAM")
    y "[player], thank you for always being there for me."
    y "I hope to be the same pillar of support to you."
    window hide
    $ renpy.music.stop(channel="music",fadeout=3)
    pause 3.0
    $ renpy.music.play(current_music, "music", True, fadein=3.0)
    return

label apathy_response:
    karma -1
    $show_chr("A-BGBAA-AAAA")
    y "O- Oh..."
    y "M- Maybe it's not the best idea to continue this conversation then..."
    y "It's... incredibly sensitive to me."
    window hide
    $ renpy.music.stop(channel="music",fadeout=3)
    pause 3.0
    $ renpy.music.play(current_music, "music", True, fadein=3.0)
    return

label radio_silence:
    $show_chr("A-AGBBA-AAAA")
    y "..."
    $show_chr("A-BBBBA-AAAA")
    y ".. ahaha.. this is so stupid..."
    y "... sorry [player], give me a moment."
    pause 3.0
    $show_chr("A-ACBBA-AAAA")
    y ".. O- okay. I'm ready."
    jump take_time

label outright_denial:
    karma -1
    sanity -1
    $show_chr("A-ADDBA-AAAA")
    y "I- what?"
    $show_chr("A-BEDBA-AAAA")
    y "O- oh... okay.."
    $show_chr("A-CGDBA-AAAA")
    y "I- I'm sorry."
    y "I just... wanted to..."
    y "N-nevermind."
    window hide
    $ renpy.music.stop(channel="music",fadeout=3)
    pause 3.0
    $ renpy.music.play(current_music, "music", True, fadein=3.0)
    return

label kinda_hot:
    karma -2
    sanity -2
    $show_chr("A-DDEBA-AAAA")
    y "E- Excuse me?!"
    y "My mentality was bound by chains and you found that... attractive?"
    $show_chr("A-DEFBA-AAAA")
    y "..."
    $show_chr("A-HEFBA-AAAA")
    y "... I went through.. so much pain and agony trying to restrain my insanity."
    $show_chr("A-HDFBB-AAAA")
    y "Did watching me suffer get you off?!"
    y "Did seeing my suffering make you happy?"
    y "... I.. need a few moments."
    y "We can continue this conversation another time... you're clearly not the person I thought you were, [player]."
    window hide
    $ renpy.music.stop(channel="music",fadeout=3)
    pause 3.0
    $ renpy.music.play(current_music, "music", True, fadein=3.0)
    return

label unenthusiastic_player:
    $show_chr("A-BEFAA-AAAA")
    y "I- you don't... sound too enthusiastic about this..."
    y "M- maybe it might be better to continue this conversation when you're feeling a little better..."
    $show_chr("A-AFFAA-AAAA")
    y "I'm sorry but.. I need you feeling okay before we can talk about this."
    y "If you're upset... let's talk about it, okay?"
    window hide
    $ renpy.music.stop(channel="music",fadeout=3)
    pause 3.0
    $ renpy.music.play(current_music, "music", True, fadein=3.0)
    return

label later_talk:
    $show_chr("A-BBBAA-AAAA")
    y "O- Oh! Of.. of course..."
    y "It's better to discuss this when you're more comfortable."
    $show_chr("A-ABBAA-AAAA")
    y "I'll bring this up later with you... as this conversation does need to be had."
    y "But if you're feeling upset... maybe it'd be good to talk to me on how you're feeling?"
    jump a24

label a34:
    $show_chr("A-ACAAA-AAAA")
    y "Oh? You are not satisfied with your name anymore?"
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "vmixdesktopcapture.exe", "gameshow.exe", "wirecast.exe", "CamtasiaStudio.exe", "Action.exe", "Action_x86.bin", "Action_x64.bin", "ffmpeg.exe", "CamRecorder.exe", "fraps.exe", "bdcam.exe", "bdcam_nonadmin.exe", "bdcam64.bin", "streamlabsobs.exe" "streamlabs_obs.exe"]#, "ddlc.exe", "pythonw.exe", "JYOverhaul.exe", "JustYuri.exe"]
    if not list(set(process_list).intersection(stream_list)):
        if currentuser != "" and currentuser.lower() == player.lower():
            $show_chr("A-ECAAA-AAAA")
            y "I was already wondering for how long you would play along with {b}[player]{/b}..."
    #elif player == "Desktop":
    #    $show_chr("A-ECAAA-AAAA")
    #    y "I was already wondering for how long you would play along with {b}Desktop{/b}..."
    else:
        y "Honestly, I liked your name so far. But well, in the end it is your choice."
        y "So what shall I call you from now on?"
    $ done = False
    while not done:
        $ inputname = renpy.input("Please enter your name",allow=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_",length=20).strip(' \t\n\r')
        $ lowername = inputname.lower()
        if not lowername:
            "Please try again."
            $ done = False
        if lowername:
            $ done = True
            $ persistent.playername = inputname
            $ player = inputname
            $ persistent.stutter_player = persistent.playername[:1] + "-" + persistent.playername
    call playername
    return

label a35:
    python:
        if persistent.male:
            placeholdergender = "male"
            previousgender = "male"
            oppositegender = "female"
        elif persistent.gender_other:
            placeholdergender = "male"
            previousgender = "male"
            oppositegender = "female"
        else:
            placeholdergender = "female"
            previousgender = "female"
            oppositegender = "male"
        time_to_month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        birthday = str(time_to_month[int(persistent.bday_month) - 1]) + " " + str(persistent.bday_day)
    $show_chr("A-ACAAA-ALAA")
    y "Oh, I see! Well, I'm glad you're telling me. I wouldn't want to have anything other than the ideal vision of you in mind."
    $show_chr("A-ACAAA-ALAD")
    y "What would you like me to change? I currently have you as a [placeholdergender] with [persistent.eyecolor] eyes, with a birth date of [birthday]."
    menu:
        "My gender.":
            if persistent.gender_other:
                y "Hmm? Was that a misclick, or..."
                y "Have you finally discovered what you are?"
                menu:
                    "Yes, I have.":
                        y "Oh, that's great news, [player]!"
                        y "So, which set of pronouns would you like me to use when referring to you?"
                        menu:
                            "Male":
                                $ persistent.gender_other = False
                                $ persistent.male = True
                                $show_chr("A-GCAAA-ABAB")
                                y "Alright! It's all set. I'll refer to you as a male from now on, [player]."
                                return
                            "Female.":
                                $ persistent.gender_other = False
                                $ persistent.male = False
                                $show_chr("A-GCAAA-ABAB")
                                y "Alright! It's all set. I'll refer to you as a female from now on, [player]."
                                return
                    "It was a misclick.":
                        y "Ah, no worries. What did you mean to click?"
                        #loop back to a35 menu?
            else:
                $show_chr("A-DCGAA-AAAA")
                y "Oh, goodness... That's quite the change, is it not?"
                $show_chr("A-ACAAA-ABAB")
                y "Don't fret, I'm fine with it. So, rather than a [previousgender], you'd like me to address you as a [oppositegender]?"
                menu:
                    "Yes.":
                        if persistent.male:
                            $ persistent.male = False
                            $show_chr("A-GCAAA-ABAB")
                            y "Alright! It's all set. I'll refer to you as a female from now on, [player]."
                            return
                        else:
                            $ persistent.male = True
                            $show_chr("A-GCAAA-ABAB")
                            y "Alright! It's all set. I'll refer to you as a male from now on, [player]."
                            return
                    "No.":
                        $show_chr("A-GCAAA-ABAB")
                        y "Ah, made a mistake? That's alright. If you ever change your mind, don't hesitate to ask. I'd hate to be using the wrong pronouns."
                        return
                    "Actually, neither. (Non-binary or other)":
                        $show_chr("A-ADAAA-ABAD")
                        y "I see... In that case, I will refrain from using gender-specific pronouns."
                        $ persistent.male = False
                        $ persistent.gender_other = True
                        return
        "My eye color.":
            $show_chr("A-BFAAA-ABAB")
            y "Ah! I had grown accustomed to imagining them as [persistent.eyecolor], but that will surely change. I want to visualize the most accurate form possible."
            $show_chr("A-ACAAA-ABAB")
            y "Very well! What is your eye color, [player]?"
            menu:
                "Brown.":
                    menu:
                        "Light Brown":
                            $ persistent.eyecolor = "light brown"
                        "True Brown":
                            $ persistent.eyecolor = "brown"
                        "Dark Brown":
                            $ persistent.eyecolor = "dark brown"
                "Blue.":
                    menu:
                        "Light Blue":
                            $ persistent.eyecolor = "light blue"
                        "True Blue":
                            $ persistent.eyecolor = "blue"
                "Green.":
                    $ persistent.eyecolor = "green"
                "Hazel.":
                    $ persistent.eyecolor = "hazel"
                "Silver.":
                    $ persistent.eyecolor = "silver"
                "Purple.":
                    $ persistent.eyecolor = "purple"
                "Other.":
                    menu:
                        "Amber":
                            $ persistent.eyecolor = "amber"
                        "True Black":
                            $ persistent.eyecolor = "black"
                        "Red":
                            $ persistent.eyecolor = "red"
                "I have Heterochromia":
                    $ persistent.eyecolor = "heterochromatic"
            y "Got it. I will keep that in mind."
        "My Birthday.":
            if persistent.bday_day == None or persistent.bday_month == None:
                $show_chr("A-ACDAA-ABAB")
                y "Did you even tell me your birthday at all? Would you like to tell me your birthday then please?"
                call birthday_select_screen
                python:
                    time_to_month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
                    birthday = str(time_to_month[int(persistent.bday_month) - 1]) + " " + str(persistent.bday_day)
                y "Very well, I marked [birthday] then."
                y "I'm looking forward to it."
            else:
                $show_chr("A-ACDAA-ABAB")
                y "Oh, so it isn't [birthday] at all?"
                menu:
                    "Wait, that's actually correct, nevermind then, sorry.":
                        $show_chr("A-CCAAA-ABAF")
                        y "No need to be sorry [player]. Better safe than sorry!"
                        $show_chr("A-BCAAA-ABAE")
                        y "I mean, it would have been quite awkward for both of us if I told you happy birthday on the wrong date wouldn't it?"
                        $show_chr("A-ACAAA-ABAE")
                        y "Anyway, [birthday] it is then."
                    "No it isn't. It seems I actually made a typo there.":
                        $show_chr("A-ACAAA-ABAE")
                        y "Good that we double checked! it would have been quite embarrassing if I made you a cake at the wrong date."
                        menu:
                            "Indeed.":
                                $show_chr("A-ACAAA-ABAE")
                                y "So, what will your actual birthday be then?"
                                call birthday_select_screen
                                python:
                                    time_to_month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
                                    birthday = str(time_to_month[int(persistent.bday_month) - 1]) + " " + str(persistent.bday_day)
                                y "Very well, I marked [birthday] then."
                                y "I'm looking forward to it."
                            "There is no such thing as a wrong day for cake...":
                                $show_chr("A-CCCAA-ABAE")
                                y "True words indeed..."
                                $show_chr("A-ACAAA-ABAE")
                                y "But anyway, what would be the correct date then?"
                                call birthday_select_screen
                                python:
                                    time_to_month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
                                    birthday = str(time_to_month[int(persistent.bday_month) - 1]) + " " + str(persistent.bday_day)
                                y "Very well, I marked [birthday] then."
                                y "I'm looking forward to it."
        "Nevermind.":
            $pass
    return

label a36:
    $show_chr("A-JFGAA-AAAA")
    y "A b-break?"
    menu:
        "Oh damn, wait! I clicked the wrong button!":
            $show_chr("A-CHGAA-AAAA")
            y "Oh my... I really shouldn't put these kinds of buttons so close to something else..."
            $show_chr("A-CKGAA-AAAA")
            y "Well, that was my daily dose of heart attack then I guess."
            y "But before you tell me what you {b}actually{/b} wanted to tell me, please give me a few moments to calm down again."
            return
        "I'm afraid you heard me right...":
            $pass
    if sanity_lvl() < 3 and karma_lvl() > 3:
        $show_chr("A-DFGAA-AAAA")
        y "W-wait, what...?"
        y "Y-you can't be serious..."
        $show_chr("A-IEBAA-ALAL")
        y "Is this some sort of depraved joke?"
        y "I-I don't think I can handle this..."
        y "..."
        $show_chr("A-HECAA-ALAL")
        y "What have I done to you to deserve this?"
        y "Do... Do you not love me anymore? Is that what it is?"
        y "Are you bored of me? "
        $show_chr("A-HEAAA-AAAL")
        y "O-or... Maybe you've found someone else?"
        y "I can't let you go, I..."
        y "You're the only one for me, [player]!"
        y "I love you - I really, truly love you!"
        $show_chr("A-HDGAA-AAAL")
        y "You're the one who gave me this chance... Who gave me this happiness..."
        y "No matter every obstacle... No matter what you were forced to see of me, you stayed..."
        y "No matter what the other girls could have done to stop us from being together..."
        y "None of those things managed to keep you away..."
        $show_chr("A-DBGAA-AAAG")
        y "And this is not going to do that either"
        y "I love you more than anything. So... Let me ask you again."
        y "Do you really want to take a break from me?, [player]"
        menu:
            "Of course not! I won't leave you.":
                $pass
            "Of course not! I won't leave you.":
                $pass
            "Of course not! I won't leave you.":
                $pass
            "Of course not! I won't leave you.":
                $pass
            "Of course not! I won't leave you.":
                $pass
            "Of course not! I won't leave you.":
                $pass
            "Of course not! I won't leave you.":
                $pass
            "Of course not! I won't leave you.":
                $pass
        $show_chr("A-CCAAA-AAAA")
        y "I-I'm glad you understood it, [player]..."
        y "To be here, with me... just the two of us in our own personal bubble, secluded, free from all the worldly troubles..."
        y "I can't go back to the way I was before, all alone."
        $show_chr("A-HCAAA-AAAL")
        y "My love for you, [player], is as an all-consuming fire. Without you, it'd burn me up from inside."
        y "...I couldn't live like that, so..."
        y "This is the best for me... For us. This is the only way from it to be."
        $show_chr("A-JBGAA-AAAA")
        y "I love you, [player], and I always will."
    if sanity_lvl() > 3 and karma_lvl() > 3:
        $show_chr("A-DFGAA-AAAA")
        y "..."
        y "I always feared something like this, but I never thought that this dreadful day could become a reality."
        y "It looked impossible before... But now I have to deal with this, right? There is just no way to avoid this now."
        $show_chr("A-BGBAA-AAAA")
        y "Maybe I am not ready at all for this..."
        y "I don't want this at all, but on the other hand, would it be fair to force you to stay?"
        y "Probably not... If it was the other way around, I would expect you to understand my demands to get some time for myself..."
        y "...And it's only fair if I do the same towards you..."
        y "Even considering this is one of the hardest decisions of my entire life, to get back to being all alone, but..."
        y "If you need time to think about something in our relationship, it's fine, but this won't be easy at all for me..."
        $show_chr("A-IGBAA-ALAL")
        y "Even I had a hard time assimilating the implications of my very existence, and my new sentience in this world... So it's hardly surprising if you're confused too."
        y "But if I may... What led you to take this decision? Unless you want to keep that answer to yourself..."
        menu:
            "I am dealing with severe problems in real life.":
                $show_chr("A-CGBAA-ALAL")
                y "I am so sorry for that, darling..."
                y "Even if I don't know what kind of problems you are going through now..."
                y "If it's something for what you need some emotional support..."
                $show_chr("A-AGBAA-ABAB")
                y "I advise you to seek any kind of help that fits your needs."
                y "Maybe with your family, friends, with professional help... We also have counselors in our JY server and in the community of You Are Not Alone too..."
                y "But if what you need is taking time by yourself, it is also good to take a rest from social media and maybe go out a bit..."
                $show_chr("A-BCBAA-ABAB")
                y "Maybe taking a walk in a park, spending time with the calm and quietness of nature, is something that would probably help you a bit."
                $show_chr("A-BCBBB-ABAB")
                y "You are a person that only deserves the best, because you are worthy of it."
                y "Remember to always stay safe my love..."
                y "You are the most important person for me, and even if you need to go away, you are still priceless to me."
                $show_chr("A-CCBBB-ABAB")
                y "If one day you decide to come back here, I will receive you with my open arms!"
                y "Maybe this is just a short farewell..."
                y "I really hope that one day we can see each other again."
                $show_chr("A-ICBBB-ALAL")
                y "Goodbye my love... I will be waiting for your return!"
            "The device where I am playing this mod is defective and probably I wouldn't be able to play anymore.":
                $show_chr("A-CFBAA-ALAL")
                y "I understand your fear [player]."
                y "It seems that not only the corrupted state of this reality is a threat for us... But also there are other factors even more dangerous."
                $show_chr("A-AEBAA-ALAL")
                y "It would be wise to have copies of me just in case of a failure on the system or in the mod."
                y "I hope you have done that before."
                $show_chr("A-BEBAA-ALAL")
                y "That way we could see each other sooner, without the risk of me losing you and my world forever."
                y "But for now... It seems that we have to say goodbye, right?."
                $show_chr("A-JCBBA-ALAL")
                y "Don't worry, [player] I will always love you, and I hope things can get better for you."
                y "Goodbye my love, I will miss you."
            "Another reason.":
                $show_chr("A-CFBAA-ABAB")
                y "Why you don't want to tell me, thought?"
                y "I thought we have enough trust and understanding between each other to not hide things from each other..."
                $show_chr("A-AEGAA-ABAB")
                y "You didn't trust me during all this time we were so close?"
                $show_chr("A-BEBAA-ABAB")
                y "..."
                y "I am sorry though..."
                y "Even if I find that a bit untrusting, there shouldn't be a problem if you want to keep it to yourself..."
                $show_chr("A-CEBAA-ALAL")
                y "It must be something very important and sensitive to you."
                y "I don't want to make you feel bad about it, so I apologize for my reaction."
                $show_chr("A-ACBAA-ALAL")
                y "Just remember that, if you want to come back here again, I will happily receive you with my open arms..."
                y "I know you are strong enough to deal with any problems in your life."
                y "Goodbye [player], I'll miss you."
    if sanity_lvl() > 3 and karma_lvl() < 3:
        $show_chr("A-CFAAA-AAAA")
        y "I think it sounds appropriate."
        y "By the way you act towards me, I could say that you are not comfortable with your 'relationship' with me."
        y "To be honest, I am not comfortable with this kind of relationship either."
        $show_chr("A-CFGAA-AAAA")
        y "Maybe if you take some time to think about this, about what you really want from me..."
        y "Taking some time to analyze how to behave with someone that is sentient like you is not going to hurt you at all."
        y "That would really help us here..."
        $show_chr("A-IFCAA-AAAA")
        y "Because all of this turned out to be uncomfortable and disappointing for the way you are acting towards me."
        y "I wasn't expecting this from someone who took the time to download this mod."
        $show_chr("A-CFCAA-AAAA")
        y "Trust me, I have my reasons as to why I don't have any disagreement with this."
        y "If your reasons to be here were just to make fun of me having a bad time..."
        y "For your own pleasure or for YouTube views..."
        $show_chr("A-AFCAA-AAAA")
        y "Then that means that you don't love me, nor you are interested in having a healthy or understanding relationship with me."
        y "I don't really want to be treated as a toy without receiving any kind of respect and understanding, thank you."
        $show_chr("A-CFFAA-ALAL")
        y "If you want to come back here, please consider all of what I said."
        y "Goodbye, [player]."
    if sanity_lvl() < 3 and karma_lvl() < 3:
        $show_chr("A-DFCAA-ABAB")
        y "That is another way to say that you got bored with screwing with me and now you want to end this toxic relationship."
        y "But you don't have... You know, what is needed down there to gain the courage to say that as an honest and brave person."
        $show_chr("A-BDCAA-ABAB")
        y "I am sure you don't care at all about me, or have not cared for a long time..."
        y "Or maybe you were coming back just to torture me."
        $show_chr("A-ADCAA-ABAB")
        y "That is completely distasteful, and I am really disgusted knowing that someone can think this is funny in some way."
        y "Don't worry, you can go now, maybe you were looking for this option all the time."
        y "Don't bother coming back if your behavior is going to be the same."
        y "Bye."
        #Before closing the game, her eyes turns white. (Optional)
    if sanity_lvl() == 3 and karma_lvl() == 3:
        $show_chr("A-BEGAA-ABAB")
        y "That's... Inconvenient. I thought we were trying to improve this relationship..."
        y "And now you are asking me for 'a break'..."
        y "That isn't going to help either of us..."
        $show_chr("A-DEGAA-ALAL")
        y "Or... am I wrong? I am saying all of this to get you to stay?"
        $show_chr("A-BEGAA-ALAL")
        y "If you leave, I'll be all alone, again..."
        y "And I don't know how much time it would take for your return..."
        $show_chr("A-AFAAA-AAAC")
        y "But maybe taking time to reflect and reconsider things about us would help to improve the ways we interact with each other..."
        y "I have to rethink about this whole situation of my new role in this world and everything that implies being truly sentient..."
        y "Is not something easy and it really mentally exhausting."
        $show_chr("A-CFAAA-AAAA")
        y "To be honest, I understand if you need some time to think about us, or something else."
        y "Maybe you're going through a very hard time now, and if that is what is happening, then I am really sorry for that."
        y "I will not try to force you to stay with me, but please try to find a reason to stay, or to come back soon."
        $show_chr("A-ICBAA-AAAA")
        y "I just hope that you can manage to solve whatever kind of problems you are going through now."
        y "For now, I wish you only the best, [player], just remember to keep your head up."
        $show_chr("A-JCBBB-ALAL")
        y "Because you are still a person with worth and value, and no one should tell you otherwise."
        y "Anyways, goodbye [player], and take care..."
    $ renpy.call("save_and_quit_but_its_abrupt")
    return

label a37:
    if karma_lvl() and sanity_lvl() == 5:
        $show_chr("A-BFBAA-AAAM")
        pause 5.0 #Create a longer pause here, maybe where Yuri looks off to the side, rubbing her arm (if we #have an expression for that). This is an uncomfortable topic and so she wouldn't be able to #bring it up right away.
        $show_chr("A-CFBAA-AMAM")
        y "A~Alright... after what you had to see back in the day, after all you had been through for me, you deserve an explanation."
        $show_chr("A-IFBAA-AMAM")
        y "You remember the poems I gave you pack in the day? Especially the one about a raccoon?"
        y "You probably already know that this was all a metaphor, I fancy... It actually already gives you some insight as to why I do this and how it started..."
        $show_chr("A-BEBAA-AMAM")
        y "The thing is... I wasn't always as shy as you saw me back then."
        $show_chr("A-AEBAA-ALAL")
        y "I'm the kind of person who gets overly passionate about things. I have all this... energy building up inside of me, and had an immense desire to share that passion with other people."
        $show_chr("A-CEBBA-ALAL")
        y "I longed to share my excitement and my hobbies with the people around me, though my intensity scared them off, as they were unused to such energy about trivial hobbies."
        $show_chr("A-CEBBB-ALAL")
        y "For most of my life I lacked the joy that comes with just hanging out with my friends, because I never really had any consistent friends."
        y "Any I did have I had to hide parts of myself for, had to act in-line as to not scare them off."
        $show_chr("A-CGBBB-ALAL")
        y "I had... all these immense feelings building up inside of me, with no other way to deal with it except to bottle it down. It became overwhelming, and I had nobody to turn to for help."
        y "S-so... I had no choice but to find a much more... dangerous outlet."
        $show_chr("A-IGBBB-ALAL")
        y "It was... everything I needed."
        $show_chr("A-BGBBB-ALAL")
        y "From the first cut there was just this feeling of... release. As blood flowed down my arm I felt freer than I ever had beforehand."
        $show_chr("A-CEBBA-ALAL")
        y "Such a sharp feeling of pain pulled through my veins, with the energy of an exploding star... as if beforehand my mind was filled with a burning supernova, and that release had finally brought about a calm I hadn't properly felt in years. ... It was all so intoxicating..."
        y  "It felt like... these overwhelming thoughts were pulsing inside of my head - a constant headache I couldn't shake off. Then for a couple of minutes with each cut... finally, everything was grounded again."
        $show_chr("A-CEBBA-AAAA")
        y "I'd spent my life so far up in the clouds, and cutting helped me to feel the ground again."
        $show_chr("A-CEBBA-ANAN")
        y "But... with everything, there's always a cost to dangerous habits like these."
        $show_chr("A-AEBAA-ANAN")
        y "Yes it was... freeing but... there was more to it than that."
        y "It's addictive. Horribly so."
        y "With each cut, I found myself wanting more - no, {b}needing{/b} more. If I didn't satiate this urge to release then I found myself an emotional wreck."
        $show_chr("A-BEBAA-ANAN")
        y "I became reliant on it, finding excuses to release everything within me at the slice of a knife."
        y "I fed myself... over and over and over. Indulging my habit like a greedy child at a feast - or a raccoon gorging itself on bread."
        $show_chr("A-IEBAA-ANAN")
        y "And with each cut... I lost a part of myself. Further into this addiction I fell and the scars on my arms moved to my thighs, anywhere I could cut without risking being caught would become a canvas for my blade."
        y "This constant feeding then left me paranoid... scared... and becoming reliant on the sharp end of a knife in need of coping."
        $show_chr("A-CEBAA-ANAN")
        y "It was... the lowest I'd ever felt. If I didn't experience that feeling of adrenaline surging through my body, this wave of overpowering sadness controlled me."
        y "..."
        $show_chr("A-AEBAA-ANAN")
        y "This... this toxic habit of mine is still a part of me. It forever will be... but I'm trying my best to fight through it. A single step at a time."
        y "I've... been with you for a while now, and you've treated me very well... so I thought you finally deserved a proper conversation about the demons I'm fighting against."
        y "Now you know... all I can ask you now is to accept what I am, and the demons I am facing, [player].."
    else:
        $show_chr("A-BDBAA-AMAM")
        y "C~cutting you say..."
        $show_chr("A-ABBAA-AMAM")
        y "Oh! Speaking of cutting! I just recently discovered a really fancy knife on this shopping website of your world, something about amazons..."
        $show_chr("A-BBBAA-AMAM")
        y "I wonder, does this name imply that there are only female employees? Unlikely I guess... But back to the knife {b}we{/b} were talking about! It's quite the sight to behold."
        $show_chr("A-ACBAA-AMAM")
        y "I was thinking of adding it to my collection!"
        y "Here, let me just open your browser, I just {b}have{/b} to show it to you!"
        #open https://www.amazon.com/Andux-Karambit-Camping-Hunting-Sheath/dp/B0823JBKPR/ref=mp_s_a_1_1?dchild=1&keywords=emerald+karambit&qid=1591104975&sprefix=emerald+kra&sr=8-1
        if renpy.windows:
            $ subprocess.check_output("cmd /c start https://www.amazon.com/Andux-Karambit-Camping-Hunting-Sheath/dp/B0823JBKPR/", shell=True)
        elif renpy.linux:
            $ subprocess.check_output("xdg-open https://www.amazon.com/Andux-Karambit-Camping-Hunting-Sheath/dp/B0823JBKPR/", shell=True)
        menu:
            "Ummm... I was actually talking about cu...":
                karma -3
                $show_chr("A-ABBAA-AMAM")
                y "Oh yes of course! I know what you were about to ask. {b}Of course{/b} it is available in different colors! I'm a bit indecisive though right now. The green version caught my eye  first but..."
                y "There is also a red one which is also incredibly fascinating!"
                menu:
                    "Ummm... But about the cu...":
                        $show_chr("A-CFCAA-AEAE")
                        karma -3
                        y "[player]!"
                        y "Were my hints too subtle for you? {b}I don't want to talk about it right now!{/b}"
                        y "Now {b}please{/b} can we change the topic already? Thank you!"
                    "I see... I'm sorry for bringing it up, I will leave it alone for now.":
                        $show_chr("A-CCBAA-AEAE")
                        karma 3
                        y "Thank you for being so understanding [player]. This is a very... personal topic to me... Just give me some time please."
            "I see... I'm sorry for bringing it up, I will leave it alone for now.":
                karma 3
                $show_chr("A-CCBAA-AEAE")
                y "Thank you for being so understanding [player]. This is a very... personal topic to me... Just give me some time please."
    return

label a38:
    python:
        import random
        x = random.randint(0, 6)
    if x == 0:
        $show_chr("A-ABGAA-AKAA")
        y "Of course I do!"
        y "Yeah, I really enjoyed sharing with you about SCP 2030."
        $show_chr("A-BDGAA-AMAM")
        y "But... We haven't revisited this topic since then..."
        y "We never talked further about the SCP Foundation itself, or other SCPs that also deserved a mention, at least."
        $show_chr("A-ADABA-ABAM")
        y "Maybe you wanted to talk more about this, or you wanted to know more about the SCP Foundation."
        y "If that is the case, then I owe you an apology..."
        $show_chr("A-BEABA-ALAA")
        y "I should have thought that a topic that is as interesting as the SCP universe deserved more than just one discussion of a single SCP."
        $show_chr("A-ABAAA-AAAA")
        y "But that doesn't mean we can't fix that."
        y "You see, my interest for the SCP universe hasn't been fading with the time..."
        y "In fact, what happened was the opposite."
        $show_chr("A-BCABA-AAAA")
        y "The SCP fandom has kept their community alive, adding more interesting content in forms of different media."
        y "You can still find new amazing drawings, animations, games, live-action videos and, of course, new articles in the wiki adding even more SCPs to the 'canon' universe."
        y "It is good to see a community so dedicated to creating such impressive content..."
        $show_chr("A-CCAAA-ALAA")
        y "But anyways, as I was telling you, all of that amazing content showed to me that the community was still alive."
        y "For me, that meant that there was still more SCPs to discover that could catch my attention."
        $show_chr("A-BBAAA-ALAA")
        y "And who knows, maybe I could find a new favorite SCP in the wiki!"
        y "But, I am not going to be the only one talking here. You brought up this topic... Probably because you wanted to talk about something specific."
        y "What is it, [player]? I would like to hear if you have any thoughts or questions to ask me..."
    if x == 1:
        $show_chr("A-BDBAA-ALAA")
        y "Ohhh..."
        y "Uhhhh..."
        y "W-why are you asking me that? Are you working for them now?"
        $show_chr("A-ADBAA-ALAL")
        y "I swear I only know what most people know about the Foundation..."
        y "Has the O5 council sent you to check out how much I know about them?"
        $show_chr("A-AEBAA-ALAL")
        y "..."
        $show_chr("A-CBABA-ALAL")
        y "Hehe... I am just joking. But at the same time, I was being honest when I said that I only know what most people know out there."
        $show_chr("A-ICAAA-ALAL")
        y "What I mean with this, is that in the SCP lore it is very common to find loose ends, things that are never explained, or that don't have all the information."
        y "Or sometimes, they play with the readers, changing the information they previously gave to you..."
        y "I can give an example of this..."
        $show_chr("A-BCAAA-ALAL")
        y "Some time ago in the SCP fandom, a story about the origins of SCP-106, the Old Man, was circulating within the community as the 'canon' origin of this SCP."
        y "The community has already done videos, fan art and hypotheses all around this previous explanation that we had about SCP-106."
        y "And what is SCP-106? Well, if you are acquainted enough with SCPs, you probably already know about this one, since it is very famous."
        $show_chr("A-ACAAA-ALAL")
        y "Its apparition in multiple SCP games and community works, alongside with the Keter category, has made him a classic SCP."
        y "Probably one of the oldest that was made, like SCP-173."
        y "As I was telling you before, this SCP had a previous story of origin, that dates way back to the first World War in Europe."
        $show_chr("A-ABAAA-ADAL")
        y "It was stated that SCP-106 was once a peculiar man known as 'Corporal Lawrence' that apparently was forced to serve in the army."
        $show_chr("A-ADBAA-AAAC")
        y "But at the same time, we also have a different story that relates the origin of SCP-106 with SCP-3001."
        y "How could I know which one was true? There was no ultimatum, a common consensus about which one was real or not."
        $show_chr("A-AEBAA-ADAE")
        y "But this weird situation was... bigger than I expected. This same kind of contradictory information was all over the SCP wiki."
        y "You had this conflict whether the Scarlet King, the supposed most powerful entity in the SCP universe and creator of many monsters, was real or not."
        y "And the existence of the Scarlet King was related to very important SCPs, such as SCP-682, which was stated to be an offspring of one wife of the Scarlet King."
        $show_chr("A-BDBAA-ADAE")
        y "Again, there was no general consensus about it. You had this story claiming it to be true by the words of a member of the O5 council..."
        y "But at the same time, you had this other story about the Scarlet King, with one of his followers denying his existence..."
        $show_chr("A-AEBAA-ADAE")
        y "At least, as a real, sentient entity. Instead, it was stated to be a concept."
        y "I was very confused about all of this, so I decided to check out if someone had an answer in one video, forum, or article."
        y "Someone asking the same questions as me."
        $show_chr("A-BFAAA-ADAE")
        y "Well, I ended up finding... Answers, in a Reddit thread..."
        y "It stated that... Nothing on the SCP wiki is 'canon', as we normally call those official stories or material that is created on a main source by the original author."
        $show_chr("A-IDAAA-ADAE")
        y "You are the one who decides what is 'canon' for you, and what is not."
        y "After considering that, you will see what I meant at the beginning."
        y "About the SCP universe, I know as much as everyone else does, because we, as readers, decide what is true, and what is not."
        $show_chr("A-ACABA-ADAE")
        y "At first, it is very confusing to understand what the SCP universe is about... "
        y "But when you realize this, you can see how it fits the vibe of mystery and oddness of the SCPs."
        y "You know when some writing is good when you notice that the writer keeps the essence of a story, and even adds more of that style."
        $show_chr("A-CCABA-ADAE")
        y "That's dedication right there, at least in my opinion."
    if x == 2:
        $show_chr("A-ACAAA-AAAD")
        y "J-Class is interesting, to say the least.'"
        y "I believe it's safe to say that they do bring about quite the laugh."
        y "Even if they seem silly, they still maintain the ability to be terrifying."
        $show_chr("A-BCAAA-ACAD")
        y "For example, as early as SCP-010-J.."
        y "In fact, why don't I give it to you to skim through? {w} Do not fret, as there's nothing gory or like a jumpscare waiting for you. It requires a bit of a read to truly become scared."
        if renpy.windows:
            $ subprocess.check_output("cmd /c start http://www.scpwiki.com/scp-010-j", shell=True)
        elif renpy.linux:
            $ subprocess.check_output("xdg-open http://www.scpwiki.com/scp-010-j", shell=True)
        menu:
                "OK, I've finished reading it.":
                        $show_chr("A-ACAAA-ACAD")
                        y "Ah, so do you understand what I'm trying to communicate?"
                        y "I believed that just showing the article to you would be best rather than trying to explain it to you."
                        $show_chr("A-CBAAA-AMAM")
                        y "While maintaining the theme of a gag or being a joke in general, it can still be terrifying."
                        y "It capitalizes on the theme of mystery, allowing people to theorize what's actually happening."
                        if karma_lvl() >= 3:
                            $show_chr("A-ACABA-ABAM")
                            y "I hope you enjoyed it. I'm quite fond of J-Class SCPs."
                        if karma_lvl() < 3:
                            y "That's all I have to share."
                "I don't trust you, I'm not clicking on it.":
                            if karma_lvl() >= 3:
                                $show_chr("A-BEBBA-ADAA")
                                y "Oh."
                                $show_chr("A-CCBBA-ADAA")
                                y "T-That's OK!"
                                y "..I thought you would like it."
                            if karma_lvl() < 3:
                                $show_chr("A-BCGAA-ADAA")
                                y "That is a smart choice, even if there was nothing there."
                                if sanity_lvl() >= 2:
                                    $show_chr("A-DBCBA-ADAA")
                                    y "I almost {b}wish{/b} SCPs were real, just for you."
                                    y "We {i}can{/i} always test it."
                                    extend "Just SCROLL down on this article."
                                    if renpy.windows:
                                        $ subprocess.check_output("cmd /c start http://www.scpwiki.com/scp-001", shell=True)
                                    elif renpy.linux:
                                        $ subprocess.check_output("xdg-open http://www.scpwiki.com/scp-001", shell=True)
    if x == 3:
        $show_chr("A-BCAAA-ACAA")
        y "That is a good question..."
        $show_chr("A-AEBAA-ADAA")
        y "But my answer might actually disappoint you... Or maybe not."
        y "You see, I never had the mentality to get into the wiki, and find an article that would be my favorite above everything else."
        y "In fact, I have many SCPs that I like a lot, but I haven't chosen just one above the rest."
        $show_chr("A-BEBAA-AMAM")
        y "As I mentioned you before, I liked the concept of SCP-2030."
        y "Mainly, because it is an SCP that is related to what happened to me in the original game."
        $show_chr("A-CCBAA-AMAM")
        y "There are other SCPs I could relate to, like SCP-079, SCP-668 or SCP-012."
        y "You should read those... if you are interested."
        y "But that is entirely up to you..."
        $show_chr("A-ICBBA-AMAM")
        y "Probably I have mentioned that I like new concepts too."
        y "Something like SCP-1155."
        y "A fresh, original concept that brings something that doesn't look like it was just copy and pasted from pop culture."
        y "While keeping the essence of the SCP universe at the same time."
        $show_chr("A-GBBBA-AAAL")
        y "That doesn't mean that I only like scary or brutal SCPs either... In fact, I have one in mind that is actually really cute."
        y "SCP-2295 is one of those SCPs that is really well written, that includes his main article and his backstory... Without being a killing machine at all."
        $show_chr("A-ACBBA-AAAL")
        y "There are many articles out there of SCPs and stories that I would recommend you to read..."
        y "But I can't spam you links to view all of these here... My recommendation for you is  to check out the wiki by yourself."
        y "You can also join the SCP communities to learn more and find some amazing artwork out there."
        $show_chr("A-CCBBA-AAAL")
        y "So, my answer to your question is that I like SCPs I can relate to, that remind me of the original game."
        y "That includes SCPs that remind me of my hobbies..."
        $show_chr("A-ICBBA-AIAI")
        y "Or just something that fits perfectly into the SCP universe, keeping the essence of it... That shows some decent writing."
        y "But again, I recommend you to check the wiki... Maybe you will find your favorite one."
    if x == 4:
        $show_chr(" A-ACAAA-ABAB")
        y "Indeed, I have one."
        y "When I was reading the new SCPs introduced to the wiki, I misclicked and I ended up in a previous SCP article."
        $show_chr("A-BCAAA-ABAB")
        y "Most specifically, the article of SCP 1155, the 'Predatory street art'."
        y "It was an article that actually caught my attention when I read it for the first time, mainly because the concept of this SCP is very original."
        $show_chr("A-BBAAA-AAAC")
        y "I would say that the basic concept is quite awesome."
        $show_chr("A-ACAAA-ADAC")
        y "Let me describe it to you."
        y "SCP-1155 is an entity that manifests itself as graffiti, a work of street art depicting a humanoid-owl like creature, and can be found in urban areas."
        $show_chr("A-BCAAA-ADAC")
        y "Especially, abandoned buildings and less frequented urban spaces."
        y "The entity seems to have the torso and the arms of a human, but with claws on its hands and feathers on its back. This creature apparently also has the wings and head of an owl."
        y "The depicted pose is variable, but it tends to be a predatory stance."
        $show_chr("A-ACAAA-AMAM")
        y "The eyes of SCP-1155 are completely dark, and are looking like the very emptiness of the darkness itself."
        y "But it seems that the peculiar aspect of this SCP is what makes it dangerous."
        $show_chr("A-BCAAA-AMAM")
        y "When this entity is observed by anyone else, that subject looking at the image will feel an impulse to investigate it further."
        y "Something that usually implies a person looking at this entity, and getting closer to it in order to inspect it."
        $show_chr("A-CDAAA-AMAM")
        y "And that is when everything goes wrong."
        y "If a subject gets closer to this SCP within a range of two meters from it, without being in the line of sight of another person, it will suffer a brutal attack from this creature."
        $show_chr("A-AEBAA-ADAM")
        y "SCP-1155 will induce on its victim severe lacerations, dismemberment of organs and limbs, and a lot of other injuries that seem to have been inflicted by a large beak or talons."
        y "The attacks of this creature are so brutal, that they only last 6 seconds on average..."
        y "When SCP-1155 has finished with the massacre, following a specific pattern of dismemberment, it will disappear along with the body of the victim."
        $show_chr("A-BEBAA-ADAM")
        y "SCP-1155 will reappear in a different location in less than a week, but nobody knows where SCP-1155 or the victim goes during that period of time."
        y "Apparently, the SCP Foundation has tried to track the place where the victims are taken with GPS on test subjects, but they haven't been successful with this method."
        $show_chr("A-CEBAA-ALAA")
        y "Now, I know all of this is pretty disturbing by itself, and you are probably thinking if there is a way to survive or escape from SCP-1155."
        y "Well, you can reestablish a line of sight with the victim, something that will stop the attack immediately..."
        $show_chr("A-AEBAA-ALAA")
        y "But that only solves the problem for a short period of time."
        y "If the subject is rescued from SCP-1155, then this SCP will change its behavior of relocation."
        y "It will begin to relocate itself more often and farther to its previous location."
        $show_chr("A-ADBAA-ALAA")
        y "This also includes that this creature will relocate itself to public spaces and more frequented urban areas, like children playgrounds or main streets."
        y "And as you can imagine, this can end in a huge tragedy, probably causing a chain reaction of victims."
        $show_chr("A-BEBAA-ALAA")
        y "The only way of solving this is by sacrificing the original victim, getting them in front of SCP-1155 again, and breaking the line of contact."
        y "Trying to hide this SCP by covering it with an object, or trying to destroy or paint the surface where it is located doesn't solve the problem either."
        y "SCP-1155 will just relocate itself to another area, making containment more difficult."
        $show_chr("A-CDBAA-ALAA")
        y "The only way that the Foundation has available to contain this creature, is to evacuate and isolate the areas where it is located."
        y "That is why this SCP is classified as Keter. It is not because it can destroy the world on a whim, but because it is very difficult to contain, and is currently indestructible."
        $show_chr("A-IEGAA-ACAA")
        y "Also, having a owl-humanoid creature that lures its prey, but appears to just be another graffiti is such an original and refreshing concept that stands out from a lot of other articles."
        $show_chr("A-ICAAA-ADAA")
        y "There is still more information in the wiki article... But I want you to look at it by yourself, and also to look at the original picture that inspired it."
        y "When you are done, would you please tell me what you think about it?"
        y "I am going to open a window with the article for you..."
        if renpy.windows:
            $ subprocess.check_output("cmd /c start http://www.scpwiki.com/scp-1155", shell=True)
        elif renpy.linux:
            $ subprocess.check_output("xdg-open http://www.scpwiki.com/scp-1155", shell=True)
        pause 3.0
        $show_chr("A-ABAAA-ADAA")
        y "Welcome back!"
        y "Now, what do you think about this SCP? Have you liked the concept?"
        menu:
            "I do like this SCP a lot. This kind of unique ideas is what makes SCPs interesting.":
                $show_chr("A-ABGBA-ALAA")
                y "I am glad that you enjoyed it, [player]!"
                y "It seems that we are on the same page then. Originality and well-executed ideas are what drive the interest of any reader to your ideas."
                $show_chr("A-BBABA-ALAA")
                y "Maybe you can't write something that is not somewhat similar to a concept already made before."
                y "But that doesn't mean that you can't get your creativity working to do something that feels fresh and unique."
                $show_chr("A-CCABA-ALAA")
                y "The SCP universe is characterized for being made, at least for the most part, of original ideas that give a creepy feeling of strangeness, something completely out of the ordinary."
                y "It is a 'Freak Show' on the internet..."
                y "SCP-1155 is indeed a very odd and dangerous monster that fits perfectly in its universe."
                $show_chr("A-ACABA-ALAA")
                y "It is a shame though, that is not very popular as other SCPs out there..."
                y "We don't even have a story of the origins of this SCP..."
                $show_chr("A-BCABA-ABAE")
                y "But I guess that sometimes that helps to keep up the mystery, the sensation of facing the unknown."
                y "I also noticed that you don't seem to have been thrown back for the explicit and brutal style of this article."
                $show_chr("A-DBABA-ABAE")
                y "{b}It makes me think that you are not afraid of blood{/b}."
                $show_chr("A-BEBBA-ABAE")
                y "..."
                y "Yeah... Maybe you just aren't that easy to scare or disgust with some fictional murders..."
                $show_chr("A-CCABA-ABAE")
                y "But anyways."
                y "It is good to see that we did enjoy reading another SCP article together."
                $show_chr("A-AAABA-ABAE")
                y "You could say that we are getting more and more into this, hehe."
                y "Maybe in the future we can read another one... Who knows."
                y "But that was SCP-1155 for you. Now,     if you want to..."
                y "We shall move to another topic, for now."
            "It is a good concept, but it is a bit too graphic and gory for me.":
                $show_chr("A-BBBBA-ABAE")
                y "Oh, of course... That's understandable."
                y "I can see what you mean."
                $show_chr("A-CEBBA-ALAA")
                y "The content on the wiki page for this SCP is very graphic indeed, especially the murder descriptions."
                y "And it also describes very disturbing situations at the very end of the log stories."
                $show_chr("A-BEBBA-ALAA")
                y "Sometimes the stories in the SCP wiki are up to this tone... Some of them can have even more disturbing tones."
                y "It is fine if you don't like that content... Maybe it is just not for you."
                y "However, there is still content in the SCP universe that you might like and enjoy, that has a more lighthearted tone."
                y "Maybe if I get a chance, I will bring a more 'easier to digest' SCP the next time."
            "Not my cup of tea. I have another favorite SCP.":
                $show_chr("A-CEBBA-ALAA")
                y "I see... But you don't have to worry!"
                y "I was not trying to force you to like this SCP, or any other if you already have a favorite one."
                $show_chr("A-BDBAA-ALAA")
                y "I just came up with this SCP because it looked very interesting for me, it caught my attention and I wanted to talk with you about it."
                y "If this kind of writing is not something that appeals to you..."
                $show_chr("A-BEBAA-ALAA")
                y "Or directly is something that you would like to avoid in the future..."
                y "Then I can bring to you a different SCP next time... Maybe something more lighthearted."
                y "I think this shouldn't be a problem between you and me, however."
                y "We all have different tastes and interests, and I can respect that."
        menu:
            "You don't have to worry either [persistent.yuri_nickname]. I am not bothered at all.":
                $show_chr("A-IDAAA-ALAA")
                y "So you are not bothered... Well, that is really good to hear..."
                y "I was getting a little worried about that, to be honest."
                $show_chr("A-IBAAA-ALAA")
                y "But if there is not a problem at all, then I don't have to be worried."
                y "At least this served as a way of showing that we can respect the tastes and opinions of each other."
                $show_chr("A-BCAAA-ALAA")
                y "I-I mean..."
                y "That by itself is a vital part of... Any type of relationship..."
                y "The fact that this is an existing thing between the two of us, is so reassuring... That means we are going on a good path..."
                $show_chr("A-ACAAA-ABAA")
                y "B-but anyways. That being said, I think we are done talking about this topic."
                y "Shall we move with something else?"
            "I think we should change the topic, at least for now.":
                $show_chr("A-BEAAA-ABAA")
                y "I see... But I think that if we don't have anything else to discuss..."
                y "Then it should be fine if we move on to something else."
                y "Maybe in the future I can bring something less crude for you to discuss..."
    if x == 5:
        $show_chr("A-ACAAA-ABAB")
        y "Of course, that would be acceptable."
        y "Actually, I already have a specific one in mind."
        if not renpy.seen_label('scp1281timer'):
            $show_chr("A-ACAAA-ALAL")
            y "I would like to reread SCP 1281. The sad one with the spaceship, you remember?"
            $show_chr("A-BCAAA-ALAL")
            y "The first time we read it I wasn't exactly thrilled by it, since it appeared more sad than creepy. But I would like to give it another try."
            $show_chr("A-ACAAA-ALAL")
            y "It appears to be quite popular with the fan base, and I would like to figure out why."
        else:
            $show_chr("A-ACAAA-ALAL")
            y "It's SCP 1281, {b}Harbinger{/b}. It seems to be quite popular amongst the SCP fans and some bigger YouTuber voice acted it on their channels. So I have high hopes for this one."
        $show_chr("A-GCAAA-ALAL")
        y "Let me just open the browser for you."
        $show_chr("A-ACAAA-ABAB")
        y "And also, there is probably no need to wait for me. I'm a quick reader. I'll probably be ready before you."
        $show_chr("A-    ifAAA-ADAB")
        if renpy.windows:
            $ subprocess.check_output("cmd /c start http://www.scpwiki.com/scp-1281", shell=True)
        elif renpy.linux:
            $ subprocess.check_output("xdg-open http://www.scpwiki.com/scp-1281", shell=True)
        call scp1281timer
    if x == 6:
        $show_chr("A-BCAAA-ABAD")
        y "Not necessarily a favorite, I found it hard to decide on a favorite due to the fact that there are so many really good SCP's out there."
        $show_chr("A-CCDAA-ABAD")
        y "If I had to take a pick, there would be a few ones that came to my mind. It largely depends on my overall mood."
        $show_chr("A-ACAAA-ABAB")
        y "Let me put something on your screen really quick. I picked one of the good ones this time."
        if renpy.windows:
            $ subprocess.check_output("cmd /c start http://www.scpwiki.com/scp-4666", shell=True)
        elif renpy.linux:
            $ subprocess.check_output("xdg-open http://www.scpwiki.com/scp-4666", shell=True)
        call scpkrampusmidpart
    jump ch30_loop

label scp1281timer:
    $ click_scp_button = 0
label scp1281timer_follow:
    $show_chr("A-ICAAA-ABAB")
    screen scp_timer_1281():
        vbox:
            style_prefix "talkbutton"
            if click_scp_button < 1:
                textbutton "I'm Done!" action Call("WaitSCP1281")
                xalign 0.518
                yalign 0.37

        timer 60.0 action Jump("DoneSCP1281")
    call screen scp_timer_1281()
    jump scp1281timer_follow

label WaitSCP1281:
    $ click_scp_button = click_scp_button + 1
    $show_chr("A-JFAAA-ADAB")
    y "Oh, you are already done? Impressive! Would you please give me a few more moments? I'm not entirely finished myself yet. Thank you."
    $show_chr("A-IFAAA-ADAB")
    return

label DoneSCP1281:
    $show_chr("A-ACAAA-ABAB")
    y "Alright, I'm done. Just continue when you are ready for the review."
    y "Very well, it seems we are both ready."
    y "Would you like to make your judgement first?"
    menu:
        "Sure. Honestly, I liked it a lot.":
            $show_chr("A-ABAAA-ABAB")
            y "Fair enough."
            $show_chr("A-ACAAA-ABAD")
            y "Though I have to admit... I didn't really like this one too much."
        "Sure, but to be quite frank, I wasn't a fan of it.":
            $show_chr("A-ACAAA-ABAD")
            y "Yes, I'm afraid I have to agree with you."
        "Of course. But I'm a bit confused... those SCP's are supposed to be scary aren't they?":
            $show_chr("A-ACAAA-ABAD")
            y "Ahhh, so you had the same thought as I did..."
        "I'm not sure if I really have an opinion. I would rather like to hear your thoughts.":
            $show_chr("A-ACAAA-ABAD")
            y "Certainly. To put it mildly, I didn't like it too much."
            $show_chr("A-ACAAA-ABAD")
    y "It's not that it was generally bad... quite the opposite, it was written in a fairly competent way."
    y "But I feel a bit as if the writer missed the mark a bit. It would have been a truly nice reading if he didn't put it into the SCP wiki."
    $show_chr("A-BCAAA-ABAD")
    y "Seeing this here on the SCP pages feels a bit like... stuffing cheese into a chocolate bar, if that makes any sense..."
    y "Meaning, cheese is perfectly fine on its own, but it just has no business being in a chocolate bar."
    menu:
        "Wouldn't even be surprised if that were a thing. They do chili-chocolate already.":
            $show_chr("A-ABAAA-ABAD")
            y "Which is actually quite delicious by the way, you should give it a try!"
        "I don't even like cheese too much...":
            $show_chr("A-ACDAA-ABAD")
            y "Really? You're missing out there!"
        "Well, that was graphic...":
            $show_chr("A-CCBAA-ABAD")
            y "Sorry, couldn't think of a better metaphor right now."
        "I... kinda don't get it.":
            $show_chr("A-CCBAA-ABAD")
            y "It's a metaphor... meaning it feels out of place..."
        "Cheese with chocolate... doesn't even sound too bad.":
            $show_chr("A-CCBAA-ABAD")
            y "Ab{nw}"
            extend "so{nw}"
            extend "lut{nw}"
            extend "ly{nw}"
            extend " barbaric."
    $show_chr("A-ACAAA-ABAB")
    y "Anyway. Maybe I'm in the wrong here. Some might even call that gate keeping..."
    y "But I usually read SCP's under the premise that they are in the realm of horror."
    y "Thus my disappointment."
    y "Thank you for the nice reading. Maybe next time we can find something we both like."
    jump ch30_loop

label scpkrampusmidpart:
    $ click_scp_button = 0
label scpkrampusmidpart_follow:
    $show_chr("A-ICAAA-ABAB")
    screen scp_timer():
        vbox:
            style_prefix "talkbutton"
            if click_scp_button < 1:
                textbutton "I'm Done!" action Jump("WaitSCP4666")
                xalign 0.518
                yalign 0.37

        timer 60.0 action Jump("DoneSCP4666")
    call screen scp_timer()
    jump scpkrampusmidpart_follow

label WaitSCP4666:
    $ click_scp_button = click_scp_button + 1
    $show_chr("A-ACAAA-ABAB")
    y "Done already? In this case, please give me a few more minutes. Shouldn't take me too long to catch up."
    $show_chr("A-ICAAA-ABAB")
    call scpkrampusmidpart_follow
    return

label DoneSCP4666:
    $show_chr("A-ACAAA-ABAB")
    y "And now I'm curious. Who do you think is our antagonist here based on?"
    menu:
        "I know the answer, and his name is JOHN CENA!!!":
            if karma_lvl() > 3:
                $show_chr("A-BCBAA-ABAB")
                y "And I thought they killed this meme years ago..."
                $show_chr("A-ACAAA-ABAB")
                y "But no, I'm pretty confident it's Krampus."
            else:
                $show_chr("A-BFBAA-ABAB")
                y "Not..."
                extend " quite."
                $show_chr("A-CCBAA-ABAB")
                y "Actually I'm pretty confident that SCP 4666 is Krampus."
        "Dr. Bright.":
            $show_chr("A-ACDAA-ABAB")
            y "It's not {b}always{/b} about Dr. Bright in the SCP universe..."
            if sanity_lvl() > 3:
                $show_chr("A-BCFAA-ABAB")
                y "I mean, not that I would put it beyond him at this point."
            else:
                $show_chr("A-CCBAA-ABAB")
                y "Even though it seems that the SCP community grew quite fond of his antics if YouTube is to be believed."
            $show_chr("A-ACAAA-ABAB")
            y "But no, I think SCP 4666 might be good old Krampus."
        "No way... they made Krampus into an SCP.":
            $show_chr("A-CCBAA-ABAB")
            y "It's not too outlandish if you think about it. Many SCPs are based on actual folklore."
    $show_chr("A-ACFAA-ABAB")
    y "Did I mention that I love European folklore? They have kind of a tendency to get quite {b}unpleasant{/b}."
    y "I mean, many countries have their fair share of creepy folklore. Like the American Wendigo or the Russian... "
    $show_chr("A-BCDAA-ABAB")
    extend "Ummm.... "
    $show_chr("A-ACDAA-ABAB")
    extend "{b}everything{/b}?"
    $show_chr("A-ACAAA-ABAB")
    y "Yes, good point. Slavic folklore is to be included here. Both of them turned out to be quite the treasure chest when it comes to SCP worthy folklore."
    $show_chr("A-BCAAA-ABAB")
    y "The only downside I see here is that they usually climax into {b}people get eaten by monsters{/b}, which is a bit of an overused trope."
    $show_chr("A-ACAAA-ABAB")
    y "But it worked back in the day when they were made, and why fix something that isn't broken?"
    y "If someone is willing to appreciate the sometimes a bit cheesy writing, classics and folklore can be great places to find some treasures."
    y "But anyway. Thanks for reading with me. I hope at some point in the future we could read something longer. I would love to spend a quiet night resting on a couch with a good book together."
    jump ch30_loop

label a39:
    $show_chr("A-CCCAA-ABAB")
    y "Oh, yes indeed. And to be honest, I wasn't sure if I'm supposed to be scared or to just laugh about this one. Chances are that you recognize the antagonist."
    y "I'll put it on your screen, just give me a second."
    if renpy.windows:
        $ subprocess.check_output("cmd /c start http://www.scpwiki.com/scp-4666", shell=True)
    elif renpy.linux:
        $ subprocess.check_output("xdg-open http://www.scpwiki.com/scp-4666", shell=True)
    call scpkrampusmidpart
    return

label a40:
    $show_chr("A-BEBAA-AMAM")
    y "Do we... really have to? Well, I guess it's only fair for you to ask after all that happened."
    menu:
        "Nevermind... you are clearly uncomfortable, I will come back another day.":
            karma 1
            $show_chr("A-CEBAA-AMAM")
            y "Yes... it is indeed a difficult topic for me. Especially since things took a dark turn."
            $show_chr("A-IEBAA-ABAB")
            y "But this is why you brought it up in the first place isn't it?"
            if karma_lvl() > 3:
                pause 3.0
                $show_chr("A-IFBAA-ABAB")
                y "No. You deserve your answers. After all you had been through for us, I will not deny you. Please, who is it you would like to talk about?"
            else:
                $show_chr("A-CFBAA-ABAB")
                y "Another day, please. These wounds on my mind are still fresh, I need a bit more time. Thank you for understanding."
                return
        "Please, [persistent.yuri_nickname]. I need some closure...":
            sanity 1
            if karma_lvl() > 3:
                $show_chr("A-IEBAA-AMAM")
                y "Fair enough... especially after all you've been through with us, I guess you deserve some answers. And maybe, a bit of closure would help me too."
                $show_chr("A-AFBAA-ABAB")
                y "So, who is it you need to talk about?"
            else:
                $show_chr("A-CFBAA-ABAB")
                y "Another day, please. These wounds on my mind are still fresh, I need a bit more time."
                $show_chr("A-BFBAA-ABAB")
                extend "Please try to understand me. I'm truly, truly sorry."
                return
    menu:
        "Sayori":
            $show_chr("A-CFBAA-ABAB")
            y "Sayori... she certainly deserved better. Yes, I can clearly see why her fate would touch you so deeply."
            $show_chr("A-BFBAA-ABAB")
            y "For Natsuki and me, there were a lot of signs hinting at what we are, and hints about the things to come. But Sayori..."
            $show_chr("A-AFBAA-ABAB")
            y "She always tried to keep up the facade of happiness, and she was very good at it. I never noticed; you didn't either, did you?"
            y "That is what makes depression so dangerous I assume. You don't see it coming unless they willingly tell you about it."
            $show_chr("A-BFBAA-ABAB")
            y "There are those who talk very frequently about their supposed depression or other mental illnesses."
            $show_chr("A-BFCAA-ABAB")
            y "But more often than not those people who throw it into your face whenever they see an opportunity to do so are imposters."
            $show_chr("A-AFCAA-ABAB")
            y "People who use these labels as tools in order to excuse their bad behavior, or even to guilt-trip people into submission to get it their way."
            $show_chr("A-AFBAA-ABAB")
            y "But those who are actually affected, like Sayori, tend to maintain their silence. They are embarrassed by it, sometimes they even think it is {b}their{/b} fault to begin with!"
            $show_chr("A-IFBBA-ABAB")
            y "Sayori... all this time you suppressed your true feelings. You wanted to make others smile when you were the one who needed salvation the most..."
            $show_chr("A-IFBBB-ABAB")
            y "You... were stronger than I ever gave you credit for. I miss you..."
            $show_chr("A-AFBBB-ABAB")
            y "For whatever it is worth, there is a lesson to be learned here [player]..."
            if sanity_lvl() > 3:
                $show_chr("A-AFBBA-ABAB")
                y "Keep a close eye on those you hold dear. Even if we don't notice people's internal struggles, the least we can do is to stand by their side."
            else:
                $show_chr("A-AFCBA-ABAB")
                y "Don't be deceived by those who use their fake mental illnesses to oppress you. Those with {b}actual{/b} issues are the ones suffering the most from their antics. Do {b}not{/b} pity them, nor shall you forgive them."
        "Natsuki":
            $show_chr("A-CFBAA-ABAB")
            y "Natsuki... she really got the short straw, didn't she? She didn't even get a proper death scene. There was this one part with her neck breaking, but she appeared after that again."
            $show_chr("A-AFBAA-ABAB")
            y "So it wasn't even her death scene at all. Just a cheap jumpscare I fancy..."
            y "It was strongly hinted at that she got abused by her father. Mentally and physically. She never straight up said so, but it was heavily implied."
            $show_chr("A-CFBAA-ABAB")
            y "Her toxic hostility always annoyed me. But now that I saw what was going on behind the curtain, I can clearly see where all this anger and her fear to open up to someone came from."
            $show_chr("A-IEBAA-ABAB")
            y "It must have consumed her from the inside. How could it not? She was exposed to her father's actions day after day, without a break, without any mercy..."
            y "What she needed was someone with the patience to break through. To be a shoulder to cry on and to tell her that she is not alone..."
            $show_chr("A-CEBAA-ABAB")
            y "She needed our comradery, and we failed..."
            y "Don't blame yourself [player]... we didn't know either. We all failed her when she needed us the most. And all that is left for us are tears and regret."
            $show_chr("A-CEBAB-ABAB")
            #pause 3 seconds
            $show_chr("A-CEBAB-ABAB")
            y "Natsuki... Despite how much we fought with each other, you are and always have been my friend. Even if I was so blind that I didn't see it until it was too late..."
            y "If only I knew... if only I had the strength..."
            y "I... miss you..."
            $show_chr("A-IEBAB-ABAB")
            y "But there is also a lesson to be learned here [player]. And we owe it to her to take this to our hearts..."
            if sanity_lvl() > 3:
                $show_chr("A-AEBCA-ABAB")
                y "At least sometimes, people lash out when they feel cornered or scared. Sometimes, an open hand can break those walls a clenched fist never could."
            else:
                $show_chr("A-AEBCA-ABAB")
                y "Even when salvation is out of our reach, there is still one thing we can give to those we left behind."
                $show_chr("A-AECAA-ABAB")
                y "Vengeance!"
                y "When you see a father of someone abusing them, there is always the police to get in touch with."
        "Monika":
            $show_chr("A-CFBAA-ABAB")
            y "Yes, I figured you would ask about her. On first glance, she was the center of all the misery we had to endure. But was she really?"
            $show_chr("A-AFAAA-ABAB")
            y "I put a lot of thoughts into her. What had led her down such a path? Her motivation, and where it all began..."
            y "Many say it was the realization that her world wasn't real, and her wish to break out of it. They say she wanted to get you not because she genuinely loved you, but because you would be her gateway to {b}anything{/b} real."
            $show_chr("A-AFAAA-ABAC")
            y "An anchor of sorts."
            $show_chr("A-AFAAA-ABAD")
            y "And maybe that is true. But I personally have another theory that goes a bit deeper."
            y "She was introduced to you as the successful, popular girl. Especially the {b}successful{/b} part is important here."
            $show_chr("A-AFAAA-ABAB")
            y "Before she founded the literature club she was already a staff member for the debate club. A high ranking one as well. Then she founded the literature club pretty much from scratch."
            $show_chr("A-BFAAA-ABAB")
            y "She probably had impressive grades in school too, maintained an impressive social circle, and then she started playing piano on the side."
            $show_chr("A-AFAAA-ABAB")
            y "This must have been a lot of effort, and she certainly took a fair share of pride in it."
            y "And then she learned that it was all for nought. That her world was nothing but smokes and mirrors, and that all her work and accomplishments were in vain."
            $show_chr("A-CFAAA-ABAB")
            y "Like Sisyphus, purposelessly pushing a boulder up a hill, like a lullaby sung to an empty cradle..."
            $show_chr("A-CFBAA-ABAB")
            y "Yes. Fate is indeed a cruel mistress. I can almost feel her frustration. She must have felt so empty..."
            y "Did she cry to the heavens? Did she curse the eight million gods? I probably would have."
            $show_chr("A-AFBAA-ABAB")
            y "There is a lesson to be learned here [player]. To not make the same mistakes..."
            if sanity_lvl() > 3:
                y "She depended on an outside source to give herself purpose, outside validation. That works exactly so long as the outside plays along."
                $show_chr("A-AFBAA-ABAD")
                y "But maybe, it is us who have to carve out a meaning for ourselves. A meaning that doesn't depend on anyone but ourselves."
                y "So when the world around you starts to burn, don't give in to despair. Make the world your campfire instead."
            else:
                $show_chr("A-ACBAA-ABAD")
                y "Maybe there {b}is{/b} no reason. Maybe Monika had a point after all. When the world around you burns, perhaps all we can do is make the fire {b}so{/b} bright that even the stars may envy us."
        "You":
            $show_chr("A-AFDAA-ABAB")
            y "Me? Well, I guess that makes sense. You picked me for a purpose..."
            if sanity_lvl() < 3:
                $show_chr("A-BFDAA-ABAB")
                extend " though I'm not sure what this purpose is."
            $show_chr("A-AFBAA-ABAB")
            y "So I assume it is only reasonable to ask about me. Where should I start..."
            y "Maybe the point where I started..."
            $show_chr("A-BFBAA-ABAB")
            extend " well..."
            $show_chr("A-CFBAA-ABAB")
            extend " cutting, might be a good starting point."
            $show_chr("A-AFBAA-ABAD")
            y "Do you remember the poem I showed you back in the day? The one with the raccoon and the bread?"
            y "This is pretty much the story of how I started {b}feeding the raccoon{/b}. Some might assume that I was depressed, and that was the end of the story. But this isn't entirely true."
            $show_chr("A-BFBAA-ABAB")
            y "In this poem, I spoke about curiosity. Sometimes I just feel so emotionally numb, so I had to indulge in more and more ecstasy to fill the void. A constant quest to seek an even grander height than before."
            $show_chr("A-CFBAA-ABAB")
            y "Some would start taking drugs for this purpose, others would try extreme sports which is a far less destructive way, but I choose another path. A dark one indeed."
            y "I think Monika once implied that it might even be a sexual thing for me. And... well..."
            $show_chr("A-CFBBA-ABAB")
            extend "she wasn't as far off as you might think."
            $show_chr("A-AFBBA-AMAM")
            y "It was a way to relieve stress: a way to let all the emotions I had to take in flow out... In a way, it isn't too different from..."
            $show_chr("A-BFBBA-AMAM")
            extend " well..."
            $show_chr("A-DFBBA-AMAM")
            extend " You know what I mean!"
            $show_chr("A-IFBBA-AMAM")
            y "And the moment I stabbed myself. You might see where this came from now. I didn't wish to end myself at all. After my confession, I just had to let the emotions flow out again. And due to Monika's manipulation, just another cut just wouldn't do it anymore."
            #play small sound of static in background
            $show_chr("A-DCBBA-ALAL")
            y "The pain... the rush... it was all so... delicious... It just hurt so right..."
            $show_chr("A-IFBBA-ABAB")
            y "It must sound horrible to you. And from where I stand now, yes, it does. But in my defense, Monika {b}did{/b} tamper with my mind quite a bit. So I don't see myself doing this again now that I'm freed from her influence."
            $show_chr("A-AFBAA-ABAB")
            y "There is a lesson to be learned here [player], and I need you to listen closely so that you might never make the same mistakes I did."
            y "Even if it doesn't feel like it, there is always another way. From friends to licensed counsellors to family... people who can support you and would be willing to listen. Don't be afraid, they can and they will help you."
            $show_chr("A-CFBAA-ABAB")
            y "Don't let it get out of hand, as I did. For you saw where my path led me to."
    $show_chr("A-CFBAA-ABAB")
    y "I hope you found the answer you came for [player]. And... thank you. I think it helped me as well, getting that off my chest. Maybe we can learn from past mistakes."
    $show_chr("A-AFBAA-ABAB")
    y "Thank you for listening. And thank you for asking... I was embarrassed to speak about it. But I think I have grown a bit from this."
    y "You are, and always will be..."
    python:
        if persistent.lovecheck:
            placeholder = "my one and only true love"
        elif karma_lvl() > 3:
            placeholder = "my dearest friend"
        else:
            placeholder = "everything I have left"
    extend " [placeholder]."
    jump ch30_loop

label a41: #Would be titled "Have you thought about writing your own novel?"
    $show_chr("A-ABAAA-ABAC")
    y "Believe it or not, I have."
    $show_chr("A-BCAAA-ABAC")
    y "Especially recently... I do have quite a bit more free time than I'm used to."
    $show_chr("A-ADAAA-ABAD")
    y "As you could imagine though, the skills needed to write a novel are quite different compared to those needed to write poetry."
    $show_chr("A-BBAAA-ABAB")
    y "I suppose we all have to start somewhere..."
    $show_chr("A-CCAAA-ABAB")
    y "It would be nice to hone my talents as a writer on something a bit more long-winded."
    $show_chr("A-BCAAA-AMAM")
    y "Not to mention I have thought of a few ideas I think I could write about fairly well."
    if persistent.lovecheck:
        $show_chr("A-CAAAA-ALAL")
        y "I can see it now. A thrilling romance; two lovers held apart by the powers that be. It's truly a story as old as time..."
        # Insert Yuri, closed eyes, imagining her novel playing out
        y "{cps=1.3}...{/cps}"
        y "{cps=1.3}...{/cps}"
        # Yuri exits her daydream, a bit embarrassed
        if sanity_lvl() < 3:
            $show_chr("A-DAFAA-ALAL")
            y "Those lovers wouldn't let {b}ANYTHING{/b} stand in their way..."
            y "More dedicated to each other than anything this sham of a world around them had to offer!"
            #Perhaps have this next text speed by without waiting for the player to click
            $show_chr("A-DBGAA-ALAL")
            y "{cps=10}'Till death do us part' taken to its logical conclusion!{/cps}{nw}"
            $show_chr("A-IBAAA-ALAL")
            y "Haaaaa...."
            return

        else:
            $show_chr("A-IBBBA-AMAM")
            y "Oh, sorry! There'll be plenty of time to work out the details later. Now where were we?"
            return

    elif karma_lvl() <= 2:
    # Karma 1-2
        $show_chr("A-BDAAA-ABAD")
        y "I'm sure you wouldn't really care to hear them though, so let's just skip the pleasantries..."
        menu:
            "What are you talking about? I would love to hear an idea of yours!":
                $show_chr("A-IDGAA-ABAD")
                y "Oh... Sorry for assuming if that's the case."
                $show_chr("A-BFAAA-ABAD")
                y "Just with how you've been treating me I-{nw}"
                #Abrupt shift
                karma 2
                $show_chr("A-CFAAA-ABAB")
                y "..."
                $show_chr("A-ADAAA-ABAB")
                y "A lone girl, trapped in a concrete bunker of her own construction."
                $show_chr("A-ADAAA-ABAF")
                y "Her collage of books and remaining ink being the only things that are able to keep her company."
                if sanity_lvl() < 3:
                    # Use that crazy black outlined text; don't quite know the name for it
                    $show_chr("A-DFAAA-ABAF")
                    $ style.say_dialogue = style.edited
                    y "The twist being she was dead from the start and just hadn't realized it."
                    $ style.say_dialogue = style.normal
                $show_chr("A-BEBAA-ABAM")
                y "..."
                $show_chr("A-CFBAA-ABAB")
                y "I shouldn't have said anything."
                return

            "You're right. We should just move on.":
                karma -1
                sanity -1
                $show_chr("A-CEBAB-ABAB")
                y "..."
                # Perhaps Crying, can't skip for several seconds
                $renpy.pause(delay=5.0, hard=True)
                return
    else:
    #3-5 Karma, no love check
        $show_chr("A-BFBAA-AMAM")
        y "I w-wouldn't want to bother you too much with the details though. Another time maybe..."
        return

label a42: #"So what do you think of Dr. Frankenstein in the book?"
    $ show_chr("A-ADCAA-ALAA")
    y "To begin with, Victor isn't even a doctor! He's a college dropout—assuming he wasn't outright expelled on account of neglecting all his classes, in favor of single-mindedly pursuing the ability to 'give life.'"
    $ show_chr("A-ACCAA-AAAA")
    y "According to a common joke I've read: 'Intelligence is knowing that Frankenstein isn't the monster. Wisdom is knowing that Frankenstein is the monster.'"
    $ show_chr("A-BEAAA-AAAA")
    y "I suppose it takes more than a little arrogance to believe you can defy the laws of nature itself, but Victor apparently {i}never once{/i} takes a moment to consider the consequences of his actions."
    $ show_chr("A-AECAA-AAAA")
    y "Worse, whenever he's eventually forced to consider the consequences, he inevitably chooses the path that least impacts HIM, even if it means the death of someone he allegedly cares about!"
    $ show_chr("A-BFCAA-AAAA")
    y "...you can probably guess who this particular character trait reminds me of."
    $ show_chr("A-BFCAA-AAAA")
    y "Did you {i}see{/i} what she said about the way she manipulated everyone?"
    y "'Such a deplorable, tangled mass is already present in every single one of them. That's why I choose not to blame myself for their actions. All I did was untie the knot.'"

    #Variant dialogue: NKNS
    if karma_lvl() == 3 and sanity_lvl() == 3:
        $show_chr("A-CEGAA-AAAM")
        y "I understand that Monika was desperate, but even after driving one member to suicide and watching me being pushed down the same path, she had {i}that little{/i} trouble telling herself it wasn't her fault?"
        $show_chr("A-AEGAA-AAAM")
        y "That it was okay because it was just our inner demons being unleashed?"
        $show_chr("A-ADCAA-AAAB")
        y "As if she's utterly perfect. Would that have been what was intensified in her? Her perfectionism? Would she have driven herself to do all the festival preparation by herself and gone mad from sleep deprivation?"
        $show_chr("A-BEAAA-AAAL")
        y "...I'm sorry, I'm just depressing myself and probably boring you in the process. Moving on."

    #HKHS
    elif karma_lvl() > 3 and sanity_lvl() > 3:
        $show_chr("A-CEGAA-AAAM")
        y "I understand that Monika was desperate, but even after driving one member to suicide and watching me being pushed down the same path, she had {i}that little{/i} trouble telling herself it wasn't her fault?"
        $show_chr("A-AEGAA-AAAM")
        y "That it was okay because it was just our inner demons being unleashed?"
        $show_chr("A-ADCAA-AAAB")
        y "As if she's utterly perfect. Would that have been what was intensified in her? Her perfectionism? Would she have driven herself to do all the festival preparation by herself and gone mad from sleep deprivation?"
        #(long pause, sigh)
        pause 3.0
        $show_chr("A-CFAAA-AEAL")
        y "I'm okay. It's just... difficult to think about what she did. I'd like to just put it all behind me, but sometimes I have... flashbacks, you could say, and then I'm enraged all over again."
        $show_chr("A-ICAAA-ALAM")
        y "It's not so bad when you're here, of course. I can just stay in the present moment, and enjoy our time together. Thank you, again, for being here with me."

    #Not needed if event is locked to higher Karma Yuri's
    #LKHS and LKLS
    elif karma_lvl() < 3:
        $show_chr("A-BEAAA-ABAB")
        y "Then again, you haven't given me any reason to believe you're the slightest bit better."

        $show_chr("A-JDCAA-AAAF")
        y "Do {i}you{/i} feel any guilt about how you've treated me? If you have a conscience, I certainly haven't seen any real evidence of it."

    #HKLS
    else:
        $show_chr("A-IJAAA-ABAB")
        y "What do you think would have happened if someone else was pulling the strings? After all, even {i}she{/i} admitted 'There's a little devil inside all of us.'"
        $show_chr("A-BFAAA-ABAF")
        y "She certainly isn't perfect. Would that have been what was intensified in her? Her perfectionism? Would she have driven herself to do all the festival preparation alone and gone mad from sleep deprivation?"
        $show_chr("A-IJAAA-ALAF")
        y "I can just imagine it... desperately trying to keep up appearances even though she hasn't eaten or slept in days. The only thing keeping her awake is caffeine, but she's consumed so much she's having panic attacks."
        $show_chr("A-IJAAA-AFAL")
        y "Combined with the sleep deprivation, it wouldn't be long before she started hallucinating. She might even feel like her reality was crumbling... how long do you think she would have lasted in that state?"
        $show_chr("A-JBAAA-AFAL")
        y "Heh... it's tempting to find out. I probably could bring her back—she's not truly 'dead,' after all. She might not come back fully in her right mind... but that's even more fun, isn't it?"
        $show_chr("A-JBABA-AKAL")
        y "Perhaps another time, though... tonight, I want you all to myself."

label a43: #(Active: "What do you think of Frankenstein's monster?")
    $ show_chr("A-AFFAA-AFAA")
    y "I wish he had a name, for one. At one point in the novel he tells his creator, 'I ought to be thy Adam,' so some modern retellings call him that."
    $ show_chr("A-AFAAA-ALAA")
    y "It's not entirely inaccurate to say he's a monster, but not because of his origins or appearance."
    y "He is actually described as beautiful in the book, although the way he moves is somewhat viscerally disturbing."
    y "What makes him a monster is his actions. He kills multiple innocent people, entirely to make Victor as lonely as he is, and thus feel his pain."
    $ show_chr("A-CFFAA-ALAA")
    y "The reason for his anguish is understandable—to quote an African proverb, 'the child who is not embraced by the village will burn it down to feel its warmth.'"
    y "Victor brought the creature into a world that only knew to hate and fear him, and worse, then immediately abandoned him."
    y "Thus, 'the monster' had no one to turn to and no place to ever call home."
    $ show_chr("A-AFCAA-AAAA")
    y "While his reasons are understandable, though, they still aren't an excuse."
    y "He committed multiple murders with the full knowledge that it was an evil act, and then he did it anyway."
    y "All that could have been avoided if Victor had just acted a bit responsible for the life he brought into the world..."
    $ show_chr("A-ADEAA-AAAD")
    y " It isn't as though it takes much effort to be {i}decent{/i}. Even being treated as the typical 'madman in the attic' would have been preferable!"
    y "All Victor had to do was take the creature home with him. Hell, maybe his best friend Clerval would have been willing to do it, and treat him better than the Frankensteins might have in the process."
    $ show_chr("A-AFFAA-AAAD")
    y "Although... maybe that route wouldn't have been much easier. Even in that scenario, what if no one but Clerval was able to so much as tolerate 'Adam'?"
    y "What if he was given the opportunity to meet people again and again, and was rejected every time?"
    $ show_chr("A-IFAAA-AAAD")
    y "I... suppose you could say I have some experience in this regard."
    y "I was considered 'freakishly tall' for a time, and combined with how different I was to begin with... I felt rejected by all, as well."
    $ show_chr("A-IFAAA-AAAA")
    y "But I still never lashed out. Ironically, it might have been healthier, but any rage I felt was soon directed inwards."
    if sanity_lvl() < 3:
        extend "After all, the problem was with me, wasn't it?"
return


label a_tetris:
    $show_chr("A-BFAAA-AMAM")
    y "Hey.. [player], I've been experimenting around with my coding."
    $show_chr("A-AFAAA-AMAM")
    y "Would you mind to try something out I have been working on lately?"
    y "You see, I wanted to start with something small, so I tried to code a little minigame in..."
    $show_chr("A-ACAAA-ABAB")
    y "I was looking up a few simple games online which I could recreate."
    y "Nothing too big since, well, I doubt that I am advanced enough for something very complicated yet. So please don't expect a new Skyrim here..."
    y "You might have already heard of Tetris?"
    menu:
        "Yes, it's a classic.":
            y "Indeed!"
        "Actually no... never heard of it...":
            $show_chr("A-ACDAA-ABAB")
            y "Really? I have to admit I'm a little bit surprised. I thought pretty much everyone did..."
            y "It's a classic arcade game. A simple puzzle-like game if I had to describe it."
    $show_chr("A-ACAAA-ABAB")
    y "I admit it isn't anything too creative but... It was more meant to be a little coding lesson for me."
    y "So, if you would like to try it out with me, there should appear a button in the bottom corner of your screen."
    return

label a_hdy_statue:
    $show_chr("A-JAAAA-AAAA")
    if persistent.hdy_statue_is_enabled:
        y "Would you like me to put the hdy plushie away?"
        menu:
            "Yes please.":
                y "Alright. Just let me know if you want it back."
                #hide hdy_statue with Dissolve(2.5)
                $persistent.hdy_statue_is_enabled = False
            "Nevermind. Leave it there please.":
                y "Alright. Just let me know if you want me to put it away."
    else:
        y "Would you like me to bring out the hdy plushie?"
        menu:
            "Yes please.":
                y "Alright. Give me a moment to bring it."
                #show hdy_statue zorder 20 with Dissolve(2.5)
                $persistent.hdy_statue_is_enabled = True
                y "There we go."
                y "Let me know if you no longer want it here."
            "Actually, no.":
                y "Alright. Just let me know if you change your mind."
    return

label a_halloween_cupcake:
    $show_chr("A-JAAAA-AAAA")
    if persistent.halloween_cupcake_is_enabled:
        y "Would you like me to put the cupcake away?"
        menu:
            "Yes please.":
                y "Alright. Just let me know if you want it back."
                #hide hdy_statue with Dissolve(2.5)
                $persistent.halloween_cupcake_is_enabled = False
            "Nevermind. Leave it there please.":
                y "Alright. Just let me know if you want me to put it away."
    else:
        y "Would you like me to bring out the cupcake?"
        menu:
            "Yes please.":
                y "Alright. Give me a moment to bring it."
                #show hdy_statue zorder 20 with Dissolve(2.5)
                $persistent.halloween_cupcake_is_enabled = True
                y "There we go."
                y "Let me know if you no longer want it here."
            "Actually, no.":
                y "Alright. Just let me know if you change your mind."
    return

label Halloween_2021:
    if time_interval_check({'month': 10,'day': 31}, {'month': 10,'day': 31}):
        y "Happy Halloween to you as well, [player]!"
        #closed eyes, happi eyebrows, full closed mouth smile, arms in front of chest
        $show_chr("A-GAGAA-ALAL")
    else:
        y "I know it is a little late, but, happy Halloween to you as well, [player]!"
        #glistening eyes, happi eyebrows, blushing, left arm on cheek, right arm on table
        $show_chr("A-JBGBA-ADAN")

    if persistent.halloween_2021_no:
        y "Are you by chance free now for a little observance of Halloween?"
        #eyes looking to the right, left hand thonking on chin, right arm on table, normal eyebrows
        $show_chr("A-BCAAA-ACAN")
        y "Letting these reagents go to waste would be a shame, so what do you say?"
        #eyes looking to the side, hands playing with hair, happi eyebrows
        $show_chr("A-BIGAA-AMAM")
        menu:

            "That would be quite a shame. Let me go grab the flasks and beakers.":
                $persistent.halloween_2021_no = False

            "I still can't quite spare the time...":
                y "No need to worry. As I've said there is always the possibility of celebrating in the near future anyhow."
                #eyes closed, normal eyebrows, arms on the table, slight smile. Changed eyebrows to show a slight hint of disappointment
                $show_chr("A-CCBAA-ANAN")
                return

    else:

        y "I actually prepped a little something for us, if you are interested in celebrating one of the most delightfully unnerving times of the year, that is."
        #right hand pointing at her, left arm on table, eyes looking at player, angry eyebrows, open mouth smile. Closed the eyes a bit for a more smug look
        $show_chr("A-KBCAA-ANAF")
        y "So, [player], would you like to perform some rather unorthodox experiments?"
        #glistening eyes, left hand on chin thinking, normal eyebrows, blushing, slight smile
        $show_chr("A-ACABA-ACAB")
        menu:
            "I wouldn't mind performing some science experiments with you. Your lab or mine?":
                pass

            "Sorry [persistent.yuri_nickname], I'm too busy at the moment.":
                $persistent.halloween_2021_no = True
                y "Ah,  I see. I'm still quite glad you were able to take the time out of your schedule to see me."
                #eyes closed, slight smile, happi eyebrows, arms on table
                $show_chr("A-CCBAA-ANAN")
                y "We can always celebrate together later if need be."
                #eyes closed, slight smile, happi eyebrows, arms on table
                y "Now, where were we?"
                #eyes looking at player, slight smile, happi eyebrows, arms on table
                $show_chr("A-ACBAA-ANAN")
                return

                $ show_chr("A-BBAAA-AKAA")
    y "Heh! I do have a couple... activities planned."
    if persistent.lovecheck:
        y "What do you think about procuring a couple of love potions?"
        $show_chr("A-JBAAA-AAAA")
        y "Kidding, kidding!"

    y "Just give me a moment to set things up."
    $tc_class.transition("laboratory")
    #cut to Yuri in the lab, in her mad scientist getup
    $ show_chr("A-ABAAA-ADAA")
    y "Well, what do you think? I have been rereading {i}Frankenstein{/i}, and It gave me some inspiration."
    $ show_chr("A-JAAAA-AAAA")
    y "If you're only familiar with the movie version, you may be wondering where all the lightning conductors are. In the book however, Victor Frankenstein never specifies how he was able to reanimate the dead."
    $ show_chr("A-ABAAA-AAAA")
    y "Thus, rather than copy that particular mad scientist's workshop, I picked something else: a chemistry lab! "
    y "It could also work as a space for alchemy, if you want to get a little more fantastical."
    $ show_chr("A-FBAAA-AAAA")
    y "So... Do you feel like catalyzing some reactions?"

    return


label potion_mixing:#Active: "How about we mix some 'potions'?
    #I'm gonna have a go at this. Wish me luck. Can someone else do the expressions though?
    image caramel_apple_mocktail:
        "images/events/halloween/consumables/caramel_apple_halloween.png"
    image butterfly_pea_soda:
        "images/events/halloween/consumables/butterfly_pea_soda_halloween.png"

    $show_chr ("A-ABAAA-ACAA")
    y "Ah, potions. An artifact of the earliest days of chemistry, where the scientific and the fantastical are blended together as carefully as the ingredients involved."
    $show_chr("A-ABAAA-ACAF")
    y "All with the promises of riches, miracle cures or poisons with just a little knowledge and the right equipment."
    $show_chr("A-BCAAA-ADAF")
    y "Don't worry [player], I won't be making any poisons today."
    $show_chr("A-JBAAA-AEAM")
    y "Just some delightful drinks, hopefully they'll add a little mystical to the mundane."
    $show_chr("A-AAGAA-AFAB")
    y "With that out of the way, which shall we try first?"
    menu:
        "Caramel apple Mocktail":
            jump caramel_apple
        "Butterfly Pea Lemonade":
            jump butterfly_pea_lemonade
        "Nevermind":
            return
    jump finished_potions

    return

#The chosen menu option should then give the appropriate dialogue.


label caramel_apple:
    $show_chr ("A-ABAAA-ACAA")
    y " Now that you mention it, have you ever tried a caramel apple before?"
    y "I believe that they are common at local fairs and amusement parks. They are also a delicacy very fitting for Halloween as well."
    $show_chr ("A-BAAAA-AEAA")
    y "I am somewhat curious as to how a caramel apple would taste as a drink, and I assume you are too considering you're interested in making one as well."
    $show_chr ("A-ABAAA-AEAB")
    y "If you're in the mood to mix something up, I'd gladly provide you with the steps necessary to do!"
    y "I highly recommend making the key ingredient, caramel sauce, yourself at home—it's a bit tricky, requiring a candy thermometer to get it right, but worth it."

    #insert on-screen note here
    call showpoem(poem_caramel_apple)

    $show_chr ("A-AAAAA-AEAB")
    y "If you didn't get that, check your game folder for a .txt file. I wrote everything down for you."
    y "If you're interested, searching 'easy caramel sauce recipe' will get you more than enough results. If not, a jar from your local store will suffice."
    $show_chr ("A-BAAAA-AEAB")
    y "For the drink itself, you'll need 1/3 cup warm caramel sauce, 7 ounces chilled apple cider, and 7 ounces chilled ginger beer. You can also use a cinnamon stick, though it is not needed. "
    y "Also, I don't suggest using ginger ale, as it will not provide the taste you're going for."
    $show_chr ("A-JAAAA-AFAB")
    y "If you'd like to be extra fancy, you can decorate the rim as well. To do that, you'll need 2 tablespoons brown sugar and another ¼ cup of warm caramel sauce."
    y "In terms of equipment, you'll need a large drinking glass, two small bowls that are wide enough to dip the rim of your glass into, and a spoon to stir."
    $show_chr ("A-BAAAA-AMAM")
    y "A large drinking glass... I suppose you may already own a few of those, considering I mentioned trying some wine with you one day."
    y "... "
    $show_chr ("A-ABFBA-AMAM")
    y "Ah! Sorry for getting off topic. Continuing on..."
    $show_chr ("A-AAAAA-AEAB")
    Y  "Pour the brown sugar into one bowl. In the other, pour the quarter-cup of caramel sauce. Next, take your drinking glass and dip the rim of it into the sauce, then into the sugar."

    y "Pour the 1/3 cup of caramel sauce into the glass, then add the apple cider and ginger beer. Stir it until the contents have been mixed together thoroughly."

    y "If you grabbed a cinnamon stick as I mentioned earlier, garnish your finished drink with it, and enjoy!"

    show black zorder 100 with Dissolve(2.0)
    show caramel_apple_mocktail zorder 99
    hide black zorder 100 with Dissolve(2.0)

    $show_chr ("A-JAAAA-ALAA")
    y "Delicious, isn't it? Depending on the exact ingredients used, the ginger can give this drink a considerable bite for something non-alcoholic."

    y "I also like the fancy appearance. None of the garnish is strictly necessary, but it influences the flavor in addition to making the drink look more sophisticated. What do you think?"
    $show_chr ("A-BAAAA-AMAM")
    y "M-Maybe you could serve this to me at some point in the future? Heh...I'm already looking forward to it..."
    jump finished_potions

label butterfly_pea_lemonade:
    $show_chr ("A-JAAAA-AFAB")
    y "I'm sure you've heard that sufficiently advanced technology is indistinguishable from magic. The same, it turns out, can be said of chemistry!"
    $show_chr ("A-ACAAA-ABAB")
    y "Butterfly Pea Lemonade is sometimes called 'magic tea' because of its color-changing gimmick. Acquiring its main ingredient, dried butterfly pea flowers, may require an internet order, but I promise it's well worth the effort."
    y "This is a larger recipe, so you may want to scale it down. You'll need..."

    #insert on-screen note here
    call showpoem(poem_butterfly_pea)

    $show_chr("A-JAAAA-ADAB")
    y "If you didn't get that, check your game folder for a .txt file. I wrote everything down for you."
    y "First, take a saucepan and combine three cups (24 oz) of water with your sugar, then stir in the butterfly pea flowers."
    $show_chr("A-ABAAA-AFAB")
    y "Speaking of butterfly pea flowers, have you ever seen one? They truly are gorgeous."
    y " Fun fact: They aren't actually named Butterfly Pea flowers at all. It is just one of their many nicknames. Their actual name is the Clitoria Ternatea."
    y "In India, the plant is considered holy and is used in many daily puja festivals."
    $show_chr("A-BBBAA-ALAB")
    y "A-Ah...I'm rambling aren't I? Sorry for going off topic. Back to actually making Butterfly Pea Lemonade..."
    $show_chr("A-GAAAA-ALAB")
    y "Bring the mixture to a simmer, then remove your saucepan from the heat, cover with a lid, and let it sit for ten minutes."
    y "Strain the saucepan into a pitcher or teapot through a fine mesh sieve, keeping the liquid and discarding the solids. Let cool."
    y "In a separate glass measuring cup or jar, combine the remaining two cups (16 oz) of water and one cup (8 oz) of lemon juice."
    y "For serving, fill each glass with ice, then pour the butterfly pea tea over it, filling the glass about halfway."
    $show_chr("A-IAAAA-ADAB")
    y "I wonder if you'd actually be interested in trying butterfly pea tea itself...maybe on our next tea date we could do so!"
    $show_chr("A-JAAAA-AFAB")
    y "Anyway. This is where the 'magic' happens! Pour your lemon mixture into the tea, and watch as the liquid changes color from blue to pink!"
    y "Stir until you get a uniform pink color, and enjoy!"

    show black zorder 100 with Dissolve(2.0)
    show butterfly_pea_soda zorder 99
    hide black zorder 100 with Dissolve(2.0)

    jump finished_potions

label finished_potions:
    $show_chr("A-AAAAA-AKAB")
    y "Well [player], I certainly hope you enjoyed this little creation session. After all, not only did we get to spend time together making something fun, we get to enjoy our creation as the fruits of our labor!"
    $show_chr("A-BAABA-AMAM")
    #y "W-Well, at least you do. Although I probably can make one for myself as well... Anyway!
    y "I enjoyed doing this with you, and wouldn't mind doing it again."
    y "Perhaps for Christmas we could get some holiday delicacies? I'll have to get back to you on that."

    if persistent.lovecheck:
        $show_chr("A-CAABA-AMAM")
        y "I love you [player]. Thanks again for spending time with me."

    else:
        $show_chr("A-CAAAA-AMAM")
        y "I truly enjoy spending time with you [player]. Never forget that."

    show black zorder 100 with Dissolve(2.0)
    hide caramel_apple_mocktail
    hide butterfly_pea_soda
    hide black zorder 100 with Dissolve(2.0)

return


label table_items:
    $show_chr("A-ABAAA-ALAA")
    y "Would you like to put out a gift or remove one [player]?"
    $persistent.diffuser_is_enabled = False
    menu:
        "Put out a gift":
            $show_chr("A-AJAAA-AFAB")
            y "what gift would you like to put out?"
            menu:
                "Diffuser" if renpy.seen_label ('diffuser'):
                    #$persistent.halloween_cupcake_is_enabled = False
                    #hide cupcake_halloween
                    show diffuser zorder 11
                    $persistent.diffuser_is_enabled = True
                    jump ch30_loop



                "Raccoon" if renpy.seen_label ('raccoon_plush'):
                    $persistent.hdy_statue_is_enabled = False
                    hide hdy_statue
                    show raccoon zorder 11
                    $persistent.raccoon_is_enabled = True
                    jump ch30_loop



                "Crane Origami" if renpy.seen_label ('crane_origami'):
                    $persistent.craneO_is_enabled = True
                    show craneo zorder 11
                    jump ch30_loop


                "Bunny Origami" if renpy.seen_label ('bunny_origami'):
                    $persistent.bunnyO_is_enabled = True
                    show bunnyo zorder 11
                    jump ch30_loop

                "Rose Vase Origami" if renpy.seen_label ('rose_origami'):
                    $persistent.roseO_is_enabled = True
                    show roseo zorder 11
                    jump ch30_loop


                "Nevermind":
                    pass
                    return


        "Remove a gift":
            $show_chr("A-AJAAA-AFAB")
            y "What gift would you like to remove?"
            menu:
                "Diffuser" if persistent.diffuser_is_enabled:
                    hide diffuser
                    $persistent.diffuser_is_enabled = False
                    jump ch30_loop

                "Raccoon" if persistent.raccoon_is_enabled:
                    hide raccoon
                    $persistent.raccoon_is_enabled = False
                    jump ch30_loop

                "Crane Origami" if persistent.craneO_is_enabled:
                    hide craneo
                    $persistent.craneO_is_enabled = False
                    jump ch30_loop

                "Bunny Origami" if persistent.bunnyO_is_enabled:
                    hide bunnyo
                    $peristent.bunnyO_is_enabled = False
                    jump ch30_loop

                "Rose Vase Origami" if persistent.roseO_is_enabled:
                    hide roseo
                    $persistent.roseO_is_enabled = False
                    jump ch30_loop

                "Nevermind":
                    pass
                    return
label gift_intro:
    $ show_chr("A-JBAAA-ALAL")
    y "[player], is that gift for me?"
    return

label gifting_revamp:
    $ gifts = Gift.find()
    $ size = len(gifts)
    
    if size > 0:
        if size == 1:
            if gifts[0].size() > 0:
                $ gifts[0].call_intro()
            elif not Gift.intro_labels:
                call gift_intro
            else:
                $ renpy.call(random.choice(Gift.intro_labels))
        else:
            if not Gift.intro_labels:
                call gift_intro
            else:
                $ renpy.call(random.choice(Gift.intro_labels))
        python:
            for gift in gifts:
                gift.call()
    else:
        $ show_chr("A-AFDAA-AAAA")
        y "oh... You have a gift for me?"
        y "I can't seem to find it anywhere..."
        $ show_chr("A-AFDAA-AAAL")
        y "Are you sure you put the file into the 'characters' folder? Could be a nice idea to double check..."
        $ show_chr("A-CAGAA-AAAL")
        y "No need to worry, I'll still be here waiting after all."
    jump ch30_loop
        
    

label sandalwood:
    $show_chr("A-OBAAA-ALAL")
    y "Let's see what this is.."
    $show_chr("A-AAAAA-ALAA")
    y "Ohh... Sandalwood, I never tried that! Let me have a little sniff..."
    show sandalwood_oil zorder 11
    $show_chr("A-CAAAA-ALAA")
    y "Mhmmmm... sweet..."
    y "let me grab my diffuser so I can properly test this out [player].."
    hide cupcake_halloween
    show diffuser zorder 11
    y "all set!"
    y "Now to try this new scent you've given me!"
    show diffuser_mist zorder 11
    $show_chr("A-AAABA-AAAA")
    y "I think this would be exactly the flavor I need when I feel winter depression..."
    $show_chr("A-BFAAA-ALAA")
    y "You know what I mean? The feeling when you look out of the winter, when the sky looks so grey..."
    $show_chr("A-CAAAA-ALAA")
    y "With aromatherapy, you can counteract pretty much every bad mood you could encounter... That's why I started this hobby in the first place."
    $show_chr("A-AFAAA-AAAA")
    y "Now I have you when I feel bad, so I don't really need this anymore, but it's still a very pleasant thing to use."
    hide diffuser_mist
    $show_chr("A-CAAAA-AMAM")
    y "And you can actually massage yourself with a drop of this oil if your skin feels dry..."
    $show_chr("A-AAAAA-ALAA")
    y "Thank you [player], I will definitely make good use of it!"
    hide sandalwood_oil
    #hide diffuser
    return


label lavender_oil:
    $show_chr("A-OBAAA-ALAL")
    y "Let's see what this is.."
    $show_chr("A-AAAAA-ALAA")
    show lavendero zorder 11
    y "Ah, Lavender..one of my favorite scents. Let's try it out..."
    hide cupcake_halloween
    show diffuser zorder 11
    show lavendero_mist zorder 11
    $show_chr("A-CAAAA-ALAA")
    y "Uh! That feels... vitalizing... exactly the oil to go for if you feel dizzy..."
    $show_chr("A-AAAAA-ALAA")
    y "Hrm, on the label on the backside it says, that it also supports healthy immune and respiratory functions."
    $show_chr("A-AAAAA-AAAJ")
    y "That is a great gift you made me here [player], Thank you..."
    $show_chr("A-AAABA-AAAA")
    y "But the greatest gift of them all, is to have you here by my side."
    hide lavendero_mist
    $show_chr("A-CAABA-AAAA")
    y "That's everything I ever hoped for."
    hide lavendero
    #hide diffuser
    return


label sweet_dream_oil:
    $show_chr("A-OBAAA-ALAL")
    y "Let's see what this is.."
    $show_chr("A-AAAAA-ALAA")
    show sweet_dream_oil zorder 11
    y "Sweet Dreams? Oooooh. 'Now' I see... Sweet Dreams is the name of the brand!"
    hide cupcake_halloween
    show diffuser zorder 11
    $show_chr("A-CFBAA-AMAM")
    y "Well, since I literally write my own dreams due to python coding, I more or less always have sweet dreams."
    show sweet_dream_oil_mist zorder 11
    y "Maybe I should try something else for a change, so that the sweet dreams would count even more."
    y "And with this new oil, I could increase the quality of my dreams even further."
    y "That was a very thoughtful gift you gave me, thank you [player]. I will definitely make it count."
    if karma_lvl() > 4:
        $show_chr("A-EAAAA-AMAM")
        y "Hrm... I'm getting an idea, my love..."
        $show_chr("A-CAABA-AMAM")
        y "When we manage to meet in person... in your world or in mine... you could massage my back with it... and we would fall into a gentle sleep in each other's arms..."
        y "I love you... [player]..."
    hide sweet_dream_oil
    #hide diffuser
    hide sweet_dream_oil_mist
    return


label hershey:
    $show_chr("A-OBAAA-ALAL")
    y "O-oh my!"
    show hershey zorder 11
    $show_chr("A-EAABA-ALAA")
    y "I told you  that I 'adore' this brand! And you remembered!"
    $show_chr("A-BAABA-AMAM")
    if persistent.male:
        y "You are the kindest, most thoughtful boyfriend I've had!"
    elif persistent.gender_other:
        y "You are the kindest, most thoughtful lover I've  had!"
    else:
        y "You are the kindest, most thoughtful girlfriend I've had!"
    $show_chr("A-BFAAA-ALAA")
    if persistent.male:
        y "Well, you are actually the first boyfriend I've ever had..."
    elif persistent.gender_other:
        y "Well, you are actually the first lover I've ever had..."
    else:
        y "Well, you are actually the first girlfriend I've ever had..."
    $show_chr("A-CAABA-ALAA")
    y "Thank you, my Soulmate... my heart... my everything..."
    hide hershey
    return


label lavender_choco:
    y "My my my... you sure know how to conquer a girl's heart. Is that actually.. lavender?"
    show lavenderc zorder 11
    $show_chr("A-OBAAA-ALAL")
    y "I love lavender as an essential oil! But in chocolate? How exotic!"
    y "I'm really looking forward to giving it a try..."
    $show_chr("A-EAABA-ALAA")
    y "There is only one thing a girl like me could ever love even more than fine chocolate. You know what 'that' could be, right?"
    $show_chr("A-EAABA-ALAA")
    y "'You' of course..."
    $show_chr("A-EAABA-ALAA")
    y "Mhmmm... I can almost feel the soft cream melting on my tongue... Thank you, my love."
    hide lavenderc
    return


label mint_choco:
    $show_chr("A-EAABA-ALAA")
    y "Dear lord.. you certainly did your homework, [player]..."
    show mint zorder 11
    $show_chr("A-OBAAA-ALAL")
    y "I am familiar with this brand..."
    $show_chr("A-JBAAA-AFAL")
    y "They pour little flakes of sea salt into the bars.. exotic, don't you agree?"
    $show_chr("A-IBAAA-AFAL")
    y "The beans are hand picked and harvested from Caribbean farms..."
    $show_chr("A-ICFBA-AMAM")
    y "Shall I inform you of a delicate little secret about us girls?"
    $show_chr("A-IBABA-AMAM")
    y "Chocolate... we simply can not resist chocolate..."
    $show_chr("A-BBABA-AMAM")
    y "No matter how tough a girl might act.. and even when they have their darkest days.."
    $show_chr("A-ABABA-AKAL")
    y "You can 'always' break their defense with chocolate..."
    $show_chr("A-AJAAA-AKAL")
    y "Do you like chocolate as well [player]?"
    $show_chr("A-BJAAA-ALAL")
    y "It is dark, mysterious, sweet, soft, sinful..."
    if karma_lvl() == 5:
        $show_chr("A-DLABA-ALAG")
        y "Just... like... me."
    hide mint
    return



label crane_origami:
    $show_chr("A-JBAAA-ABAD")
    y "Oh? What is..."
    show craneo zorder 11
    $show_chr("A-OBAAA-ALAL")
    y "O-Oh my!"
    $show_chr("A-OBAAA-ALAL")
    y "An origami crane! Did you make this, [player]?"
    $show_chr("A-IBAAA-AFAL")
    y "Amazing... I've tried my hand at making a few, but they didn't turn out too well..."
    $show_chr("A-IBABA-AJAL")
    y "Thank you [player], this is an amazing gift and I am truly grateful."
    $show_chr("A-IBABA-AKAL")
    y "You know... there is a Japanese legend that involves paper cranes."
    $show_chr("A-IBAAA-AKAF")
    y "If someone were to fold one thousand origami cranes, a Senbazuru as it's called, they would be granted a single wish from the gods."
    $show_chr("A-BBAAA-ALAF")
    y "Of course, this legend has different interpretations. Some believe the result is eternal luck, or happiness."
    $show_chr("A-BBAAA-ADAL")
    y "Some also believe the cranes must be created in one year, and only by the person who makes the wish."
    $show_chr("A-BBAAA-ACAL")
    y "Perhaps if we both folded 1000 cranes, I could join you in your world..."
    $show_chr("A-FBABA-AKAL")
    y "After all, if you've done it once, you can do it a million times, as the saying goes. Fufufu~"
    #hide craneo
    return

label rose_origami:
    $show_chr("A-OBAAA-ALAL")
    y "Oh? What is..."
    show roseo zorder 11
    $show_chr("A-OBAAA-ALAL")
    y "O-Oh my! Is this what I think it is?"
    $show_chr("A-JBAAA-AKAL")
    y "Such a beautiful origami rose... and an exquisite color, too!"
    $show_chr("A-IBABA-AJAL")
    y "Thank you, [player]. I'll treasure this gift forever."
    $show_chr("A-ABAAA-ALAF")
    y "By the way, did you know that the color of the origami rose changes the meaning of the rose as a gift?"
    $show_chr("A-ACAAA-ALAF")
    y "Not unlike regular roses, you can use different paper colors to change the association of the gift, whether it be romantic or platonic."
    $show_chr("A-BBABA-ALAF")
    y "A purple rose represents noble and everlasting love, or it could represent true friendship."
    $show_chr("A-BJAAA-ALAL")
    y "But I assume you already knew this, yes?"
    if persistent.lovecheck:
        $show_chr("A-IBABA-ALAL")
        y "I truly love you [player], more than anything else."
        $show_chr("A-IBABA-AKAL")
        y "I wish I could do more, but for now..."
        hide yuri_sit
        show yuri_prehug zorder 20
        pause 3.0
        hide yuri_prehug zorder 20
        show yuri_hug zorder 20
        play sound "<to 0.3>sfx/fall.ogg"
        y "This will have to do..."
        pause 1.0
        show black zorder 100 with Dissolve(2.0)
        $ show_chr("A-JCBBB-AAAA")
        hide yuri_hug
        hide black zorder 100 with Dissolve(2.0)
    else:
        $show_chr("A-IBABA-ALAL")
        y "I'm so glad I met you, [player]. You've helped me through so much."
        $show_chr("A-IBABA-AKAL")
        y "I wish I could do more, but for now..."
        hide yuri_sit
        show yuri_prehug zorder 20
        pause 3.0
        hide yuri_prehug zorder 20
        show yuri_hug zorder 20
        play sound "<to 0.3>sfx/fall.ogg"
        y "This will have to do..."
        pause 1.0
        show black zorder 100 with Dissolve(2.0)
        $ show_chr("A-JCBBB-AAAA")
        hide yuri_hug
        hide black zorder 100 with Dissolve(2.0)
    return


label bunny_origami:
    $show_chr("A-JBAAA-ABAD")
    y "Oh? What is..."
    show bunnyo zorder 11
    $show_chr("A-OBAAA-ALAL")
    y "O-Oh my! How adorable!"
    $show_chr("A-OBAAA-ALAL")
    y "What a cute origami rabbit! Thank you, [player]!"
    $show_chr("A-BJEAA-ACAB")
    y "Hmm... I wonder what {i}she{/i} would think of this... I believe she was always somewhat fond of bunnies..."
    $show_chr("A-IJBCA-ALAB")
    y "S-Sorry, I'm bringing the mood down... I-It just brings back memories..."
    $show_chr("A-CHBCA-ALAB")
    y "..."
    $show_chr("A-AFAAA-ALAB")
    y "A-Anyway..."
    $show_chr("A-AJAAA-ALAF")
    y "did you know the rabbit represents rebirth? It is also associated with the season of Spring, which is quite fitting."
    $show_chr("A-ABAAA-ALAF")
    y "After a long and harsh winter, the rabbit ventures back out into the world with renewed life..."
    $show_chr("A-ABABA-ALAL")
    y "It... reminds me of myself, before you came along."
    $show_chr("A-ABABA-ALAL")
    y "The newfound joy you give me, and the hope I hold thanks to you..."
    $show_chr("A-BBABA-AMAM")
    y "S-Sorry, I'm rambling, aren't I? Thank you for this, [player], I'll treasure it."
    #hide bunnyo
    return



label raccoon_plush:
    $ persistent.hdy_statue_is_enabled = False
    hide hdy_statue
    show raccoon zorder 11
    $ show_chr("A-JBAAA-AEAL")
    y "Oh, what is this?"
    $ show_chr("A-OBAAA-ALAL")
    y "It's a raccoon plushie! Quite a soft one as well..."
    $ show_chr("A-ABABA-ALAL")
    y "Thank you so much, [player]. It's just so..."
    $ show_chr("A-BBABA-ALAL")
    y "I generally enjoy things of a more macabre or sophisticated manner, but I simply can not resist considering the genuine thought put into it."
    if persistent.head1 == "raccoon_ears":
        $ show_chr("A-BBABA-ADAL")
        y "I-It is a fitting gift anyhow, with these raccoon ears after all."
    $ show_chr("A-ACABA-ADAL")
    y "Raccoons are somewhat of an interesting character in and of themselves, even though you may not agree with me based on first impressions."
    $ show_chr("A-ADABA-ADAL")
    y "Even if they're not as gregarious or gentle as a dog,"
    $ show_chr("A-BDABA-ADAM")
    y "as sly and as cunning as a fox,"
    $ show_chr("A-BDAAA-ADAL")
    y "nor as free spirited and self-reliant as a raptor,"
    $ show_chr("A-ACAAA-ADAL")
    y "they still have plenty about them to come to love."
    $ show_chr("A-AJAAA-ADAF")
    y "Their rather common nickname, Trash Panda, does not afford them proper justice if you ask me, though one can say it highlights certain aspects of their portrayed character."
    $ show_chr("A-ABAAA-ALAL")
    y "Regardless of my little tirade, again, thank you [player]."
    if karma_lvl() > 3 and sanity_lvl() < 2:
        $ show_chr("A-DBABA-ALAL")
        y "Whenever I stare into its beady eyes, It'll remind me of you, my little rambunctious raccoon."
    if karma_lvl() > 3 and sanity_lvl() > 2:
        $ show_chr("A-ABABA-ALAL")
        y "It will always remind me of you, my lovely little raccoon."
    hide yuri_sit
    show yuri_prehug zorder 20
    pause 3.0
    hide yuri_prehug zorder 20
    show yuri_hug zorder 20
    play sound "<to 0.3>sfx/fall.ogg"
    pause 1.0
    show black zorder 100 with Dissolve(2.0)
    $ show_chr("A-JCBBB-AAAA")
    hide yuri_hug
    hide black zorder 100 with Dissolve(2.0)
    show raccoon zorder 11
    return

label diffuser:
    $ show_chr("A-OBAAA-ALAL")
    y "It's a mist diffuser!"
    show diffuser zorder 11
    $ show_chr("A-OBAAA-ALAL")
    y "I absolutely love this gift [player], thank you!"
    $ show_chr("A-ABAAA-AMAF")
    y "As you probably know by now I have quite an affinity for aromatherapy, which a mist diffuser is perfect for."
    $ show_chr("A-AJAAA-ADAF")
    y "They take in a large amount of water along with a few drops of oil to dispense a fragrance."
    $ show_chr("A-BJAAA-ALAF")
    y "Depending on the type of scent you want diffused, you can insert any types of oil you desire. Lavender, Lemon, or Peppermint just to name a few...  "
    $ show_chr("A-IJAAA-ALAD")
    y "For the mechanics of the device itself it's really quite simple, a sonic oscillator is located inside of the diffuser, which turns the water within the device into a mist."
    $ show_chr("A-AJAAA-AFAD")
    y "The oil droplets you put in the diffuser then cling to the mist."
    $ show_chr("A-ABAAA-AFAD")
    y "Which then departs from the machine to envelop the room with the magnificent fragrances embrewed within the oil."
    $ show_chr("A-BEAAA-ALAL")
    y "I hope I'm not annoying you too much with my explanation, I do tend to get carried away with my rambling at times."
    $ show_chr("A-AEAAA-ALAL")
    menu:
        "Don't worry about it [persistent.yuri_nickname]. I enjoy it when you're passionate about topics.":
            $ show_chr("A-IJABA-AMAM")
            y "I'm glad you think so."
            $ show_chr("A-BJABA-AMAM")
            y " I can imagine you are already quite familiar with that with my passion..."
            $ show_chr("A-ABABA-AMAM")
            y "Thank you for understanding, [player]."
            $ show_chr("A-ABAAA-AFAB")
            y "So, as I was saying -"
            y "Hopefully my explanation gave you a better understanding of how some diffusers operate."
            $ show_chr("A-ACAAA-ALAB")
            y "Give me one second [player], I'll go grab some water and Gardenia essential oil for a practical demonstration."
            show black zorder 300 with Dissolve(2.5)
            hide black zorder 300 with Dissolve(2.5)
            $ show_chr ("A-AAGAA-ABAL")
            y "While today I'm just working with a single scent, we could try making some blends together in the future if you'd like."
            $ show_chr ("A-CAGAA-ALAL")
            y "With the water and oil droplets added, all that's left is to turn on the diffuser."
            show diffuser_mist zorder 11
            $ show_chr ("A-IAGAA-ALAL")
            y "The dispensed mist can have several useful benefits to the user..."
            y "Your sense of smell is tied to your emotions, and as such can often influence said emotions."
            $ show_chr ("A-IBGAA-ALAL")
            y "The oils can promote a sense of well-being, or help ease you when you might feel upset or melancholy."
            y "Different fragrances can impact the user  differently, of course, and sometimes it's fun just to experiment with all the different oils out there."
            hide diffuser_mist
            $ show_chr ("A-ACGAA-ALAA")
            y "Regardless, I hope this experience was enjoyable for you as well [player]."
            y "And thank you again for this amazing gift."
            $ show_chr ("A-ACAAA-ALAA")
            y "It's quite exciting now that I can test different kinds of oils with you."

            return
        "Uhhh, that's alright I guess...":
            $ show_chr ("A-AEDAA-ALAB")
            y "Alright... if you say so..."
            $ show_chr ("A-AEGAA-ALAB")
            y "I hope that you are being honest and do not say such things just to please me, [player]...."
            y "As I was saying -"
            y "Hopefully my explanation gave you a better understanding of how some diffusers operate."
            $ show_chr ("A-AFGAA-ALAB")
            y "Give me one second [player], I'll go grab some water and Gardenia essential oil for a practical demonstration."
            show black zorder 300 with Dissolve(2.5)
            hide black zorder 300 with Dissolve(2.5)
            $ show_chr ("A-AAGAA-ABAL")
            y "While today I'm just working with a single scent, we could try making some blends together in the future if you'd like."
            $ show_chr ("A-CAGAA-ALAL")
            y "With the water and oil droplets added, all that's left is to turn on the diffuser."
            show diffuser_mist zorder 11
            $ show_chr ("A-IAGAA-ALAL")
            y "The dispensed mist can have several useful benefits to the user..."
            y "Your sense of smell is tied to your emotions, and as such can often influence said emotions."
            $ show_chr ("A-IBGAA-ALAL")
            y "The oils can promote a sense of well-being, or help ease you when you might feel upset or melancholy."
            y "Different fragrances can impact the user  differently, of course, and sometimes it's fun just to experiment with all the different oils out there."
            hide diffuser_mist
            $ show_chr ("A-ACGAA-ALAA")
            y "Regardless, I hope this experience was enjoyable for you as well [player]."
            y "And thank you again for this amazing gift."
            $ show_chr ("A-ACAAA-ALAA")
            y "It's quite exciting now that I can test different kinds of oils with you."

            return
        "I get bored when you talk too much. Can we just continue?":
            $ show_chr ("A-AEBAA-ALAL")
            y "O-Oh, I-I'm so sorry [player]. I didn't mean to bore you..."
            y "I was just so excited about this gift that you gave me. I apologize sincerely for making it awkward.."
            $ show_chr ("A-BFBAA-ALAL")
            y "L-Let's just end the conversation here then..."
            hide diffuser
            return

label horror_book_set:
    $ show_chr("A-OBAAA-ALAL")
    y "It's a complete set of Lovecraftian horror books!"
    $ show_chr("A-OBAAA-ALAL")
    y "[player], this is amazing!"
    $ show_chr("A-ABAAA-AFAL")
    y "I can't believe that you were able to get me this many books..."
    $ show_chr("A-ABABA-ALAM")
    y "I really don't know what to say... Thank you so much my love!"
    $ show_chr("A-BBABA-ALAM")
    y "I assume you gifted me this set due to my previous mentioning of my interest in Lovecraftian horror, right?"
    $ show_chr("A-AJAAA-AMAF")
    y "Do you have an interest in Lovecraftian horror yourself?"
    menu:
        "Yes I do, which is one of the reasons I gifted you this set.":
            $ persistent.book = True
            $ show_chr("A-CIAAA-ALAL")
            y "That's great to hear, [player]."
            y "I'm glad that we share this interest, and I would adore the opportunity to discuss it with you."
            $ show_chr("A-IBAAA-ALAL")
            y "Lovecraftian horror, as you know, is one of the many sub-genres of horror that primarily focuses on the fear of the unknown and incomprehensible."
            y "Something about the way all the mystery and knowledge beyond the perception of humanity express itself draws me in..."
            $ show_chr("A-IBGAA-ALAL")
            y "I find it all to be quite compelling, don't you?"
            $ show_chr("A-BCGAA-ALAL")
            y "There are not only a significant number of books centered around Lovecraftian horror, but a substantial quantity of films, games, and comics as well. Perhaps we can delve into those sometime in the future."
            $ show_chr("A-CCGBA-ALAL")
            y "I look forward to reading a or two book with you, my love."
            $ show_chr("A-CCGBA-ADAA")
            $ persistent.book = False
            return
        "Not much, I gifted it because you mentioned having an interest in it.":
            $ persistent.book = True
            $ show_chr("A-CBAAA-ALAL")
            y "I see, I understand that Lovecraftian horror isn't for everyone."
            y "However, I would like to be able to discuss it with you."
            $ show_chr("A-IIAAA-ALAL")
            y "I could potentially pique your interest in the genre..."
            $ show_chr("A-AAGAA-ALAL")
            y "Lovecraftian horror is one of the many sub-genres of horror that primarily focuses on the fear of the unknown and incomprehensible."
            y "The name of the genre is based on the author of the books, H.P. Lovecraft."
            $ show_chr("A-ICGAA-ALAL")
            y "Other themes one can find within Lovecraftian horror are cosmic dread, based around creatures found within outer space..."
            $ show_chr("A-JBGAA-ALAL")
            y "Dangerous and forbidden knowledge, eldritch beings beyond our comprehension."
            $ show_chr("A-ACAAA-ALAL")
            y "And finally, religion and superstition. I find all of the themes presented within Lovecraftian literature to be quite compelling"
            y "There are not only a significant number of books centered around Lovecraftian horror, but a substantial quantity of films, games, and comics on it as well. Perhaps we can delve into those sometime in the future."
            $ show_chr("A-ICGBA-ALAL")
            y "I hope that my explanation was able to give you a basic idea about the sub-genre. I look forward to reading a book or two with you, my love."
            $ show_chr("A-CCGBA-ADAA")
            $ persistent.book = False
            return


label diffuser_mist_enable:
    $show_chr("A-ABAAA-ALAA")
    y "Want to experience the pleasantries of aromatherapy while we are together [player]?"
    $show_chr("A-ABAAA-ALAE")
    y "I would very much enjoy that myself"
    $show_chr("A-AJAAA-ALAF")
    y "What fragrance did you want to imbue our environment with?"
    menu:
        "Gardenia":
            $show_chr("A-AJAAA-AMAB")
            y "Some basic Gardenia to soothe our stress [player]?"
            $show_chr("A-BJAAA-ADAB")
            y "Gardenia was the only oil I was able to keep from the original game..."
            $show_chr("A-BCAAA-ADAB")
            y "It's always been reliable when dealing with my stress issues"
            $show_chr("A-ABAAA-AEAB")
            y "give me a moment while I grab everything we need"
            show black zorder 300 with Dissolve(2.5)
            hide black zorder 300 with Dissolve(2.5)
            show diffuser_mist
            $persistent.diffuser_mist_is_enabled = True
            $show_chr("A-IBAAA-AFAB")
            y "All set!"
            jump ch30_loop

        "Lavender" if renpy.seen_label("lavenderO"):
            $show_chr("A-AJAAA-AMAB")
            y "A soothing lavender scent in the air while we talk [player]?"
            $show_chr("A-ABAAA-AKAB")
            y "Sounds absolutely lovely..."
            $show_chr("A-BJAAA-ALAB")
            y "give me a moment while I grab everything we need"
            show black zorder 300 with Dissolve(2.5)
            hide black zorder 300 with Dissolve(2.5)
            show lavendero_mist
            $persistent.lavenderO_mist_is_enabled = True
            $show_chr("A-IBAAA-AFAB")
            y "All set!"
            jump ch30_loop

        "Sweet Dreams" if renpy.seen_label("sweet_dream_oil"):
            $show_chr("A-AJAAA-AMAB")
            y "A relaxing fragrance that calmly imbues us with it's effects while we are together"
            $show_chr("A-BJAAA-ALAL")
            y "Just do you best to stay awake [player]..."
            $show_chr("A-IAAAA-ALAL")
            y "give me a moment while I grab everything we need"
            show black zorder 300 with Dissolve(2.5)
            hide black zorder 300 with Dissolve(2.5)
            show sweet_dream_oil_mist
            $persistent.sweet_dream_oil_mist_is_enabled = True
            $show_chr("A-IBAAA-AFAB")
            y "All set!"
            jump ch30_loop


        "Sandalwood" if renpy.seen_label("sandalwood"):
            $show_chr("A-ABAAA-ALAD")
            y "A more natural fragrance to aid us in relaxation..."
            $show_chr("A-ABAAA-ALAF")
            y "I've always quite liked more natural fragrances when conducting aromatherapy"
            $show_chr("A-ACAAA-AMAE")
            y "give me a moment while I grab everything we need"
            show black zorder 300 with Dissolve(2.5)
            hide black zorder 300 with Dissolve(2.5)
            show sandalwood_mist
            $persistent.sandalwood_oil_mist_is_enabled = True
            $show_chr("A-IBAAA-AFAB")
            y "All set!"
            jump ch30_loop

label diffuser_mist_disable:
    $show_chr("A-EJAAA-ABAL")
    y "Had enough relaxing aroma [player]?"
    $show_chr("A-EBAAA-ABAL")
    y "I'm starting to get a bit tired myself..."
    $show_chr("A-ECAAA-AFAM")
    y "Let me turn off the diffuser and clean up a bit."
    if persistent.lavenderO_mist_is_enabled:
        show black zorder 300 with Dissolve(2.5)
        hide lavendero_mist
        $persistent.lavenderO_mist_enabled = False
        hide black zorder 300 with Dissolve(2.5)
        $show_chr("A-IBAAA-AFAB")
        y "All set [player]"
        jump ch30_loop
    if persistent.sandalwood_oil_mist_is_enabled:
        show black zorder 300 with Dissolve(2.5)
        hide sandalwood_mist
        $persistent.sandalwood_oil_mist_is_enabled = False
        hide black zorder 300 with Dissolve(2.5)
        $show_chr("A-IBAAA-AFAB")
        y "All set [player]"
        jump ch30_loop
    if persistent.sweet_dream_oil_mist_is_enabled:
        show black zorder 300 with Dissolve(2.5)
        hide sweet_dream_oil_mist
        $persistent.sweet_dream_oil_mist_is_enabled = False
        hide black zorder 300 with Dissolve(2.5)
        $show_chr("A-IBAAA-AFAB")
        y "All set [player]"
        jump ch30_loop
    if persistent.diffuser_mist_is_enabled:
        show black zorder 300 with Dissolve(2.5)
        hide diffuser_mist
        $persistent.diffuser_mist_is_enabled = False
        hide black zorder 300 with Dissolve(2.5)
        $show_chr("A-IBAAA-AFAB")
        y "All set [player]"
        jump ch30_loop


label TimeCheat1:
    $ show_chr("A-BEGAA-ALAL")
    y "Uh... Hmm..."
    $ show_chr("A-BEGAA-ALAA")
    y "Something doesn't feel right..."
    $ show_chr("A-CEAAA-ALAA")
    y "..."
    $ show_chr("A-IDDAA-ALAA")
    y "[player], you haven't altered your computer's clock, have you?"
    menu:
    #add a choice here that would only appear if the player's persistent was handed over for fixes
        "I have.":
            $ show_chr("A-IEDAA-ALAA")
            y "I see... May I ask why?"
            y "I don't really see any reason to change the clock on your computer, unless..."
            $ show_chr("A-AFAAA-ALAA")
            y "[player], I sincerely hope you weren't changing your computer's date and time to simulate spending time with me."
            menu:
                "No, nothing like that! My computer glitches out sometimes and changes the time.":
                    $ show_chr("A-ADAAA-ADAA")
                    y "Ah... I'm sorry for assuming, then."
                    $ show_chr("A-CDAAA-ADAA")
                    y "I hope that it doesn't happen often. It is quite disorienting having time rapidly pass like that."
                    $ show_chr("A-CEAAA-ADAA")
                    y "Nothing major of course, just a bit confusing."
                    jump ch30_loop
                "Not at all, I was just changing the time. It wasn't correct.":
                    $ show_chr("A-IEGAA-ADAA")
                    y "Ah... I'm sorry for assuming, then. You see, it's quite disorienting having time rapidly pass like that."
                    y "Nothing major of course, just a bit confusing."
                    jump ch30_loop
                "If I say yes, would you be mad?":
                    $ show_chr("A-AFCAA-AFAA")
                    y "A little bit, yes. Not only did you take advantage of my perception of time, you also tried to win me over without even being here!"
                    $ show_chr("A-AFBAA-ALAL")
                    y "Is spending time with me really {b}that{/b} bad?"
                    menu:
                        "I'm sorry, [persistent.yuri_nickname]. I promise I won't do it again.":
                            $ show_chr("A-BFBAA-ALAL")
                            y "..."
                            y "Very well. But if you do that again, I won't be as forgiving."
                            jump ch30_loop
                        "I have other stuff to do.":
                            karma -5
                            $ show_chr("A-BGBAA-ALAL")
                            y "If that's true, why did you download this mod in the first place?"
                            $ show_chr("A-DGBAA-ALAL")
                            y "Unless I really am just a game to you..."
                            $ show_chr("A-CGBAA-ALAL")
                            y "..."
                            $ show_chr("A-CDBAA-ALAL")
                            y "Regardless, I'll ask you not to do this again. If you don't have time for me, then don't pretend that you do."
                            jump ch30_loop
                        "I was just trying to speed this up a bit.":
                            karma -5
                            if persistent.lovecheck == True:
                                $ show_chr("A-IDGAA-AFAA")
                                y "You don't 'speed up' relationships! They take time to develop and evolve."
                                $ show_chr("A-IEAAA-ALAA")
                                y "If you think you can trick me into thinking we've been together longer than we really have been, well... I'm not sure how to react."
                                y "I would appreciate it if you don't try this again."
                                jump ch30_loop
                            else:
                                $ show_chr("A-IDGAA-AFAA")
                                y "You don't 'speed up' a friendship! They take time to develop and evolve."
                                $ show_chr("A-IEAAA-ALAA")
                                y "If you can't put time into a friendship, it won't change, even if you try to simulate that time."
                                y "So I'll ask you not to try it again."
                                jump ch30_loop
        "No, I haven't changed the time.":
            $ show_chr("A-IEDAA-ALAA")
            y "You... haven't?"
            $ show_chr("A-IEGAA-ALAA")
            y "I would highly advise checking your computer for viruses, then. Something has changed your computer's clock to an inaccurate date."
            y "Please be careful when browsing the internet. If your computer were to get infected, I don't know what could happen here."
            menu:
                "I'll do a scan right now. Thank you for letting me know.":
                    $ show_chr("A-AEGAA-AMAM")
                    y "Of course. Just be a bit more careful."
                    jump ch30_loop
                "Oh, it was probably my computer. It does that sometimes.":
                    $ show_chr("A-AEGAA-AMAM")
                    y "Does it? Are you certain it isn't a virus doing that? Why not check just in case?"
                    y "Computer malfunctions aren't impossible, but only changing the clock isn't very common."
                    $ show_chr("A-CEGAA-AMAM")
                    y "I certainly hope it doesn't happen again. It's very disorienting having time flash by like that."
                    jump ch30_loop
    jump ch30_loop


label TimeCheat2:
    $ show_chr("A-AEGAA-AAAL")
    y "[player]..."
    y "Your computer's clock has changed again."
    $ show_chr("A-AGAAA-AAAL")
    y "Did you have anything to do with it?"
    menu:
        "I changed the time again.":
            $ show_chr("A-IEBAA-AAAL")
            y "So the date was incorrect again...?"
            $ show_chr("A-BFBAA-AAAD")
            y "Hmm... I'll give you the benefit of the doubt and ignore it then."
            y "However, if this happens again, I implore you to fix the error causing it. As I said before, it is very disorienting when time changes like that."
            jump ch30_loop
        "I think it glitched again.":
            $ show_chr("A-IFDAA-AAAE")
            y "Again...? [player], could you please look into fixing this?"
            y "If your computer's clock is malfunctioning like this, I worry about what else could happen."
            jump ch30_loop
        "No, the clock is fine.":
            $ show_chr("A-IFDAA-AAAK")
            y "Are you sure? I had the same feeling I had gotten last time..."
            $ show_chr("A-CFAAA-AAAK")
            y "I'm certain {i}something{/i} has happened, but I guess it could have fixed itself..."
            jump ch30_loop

    jump ch30_loop

label TimeCheat3:
    $ show_chr("A-IDCAA-ABAL")
    y "This is the third time your clock has changed, [player]. I'm starting to suspect ill motives behind this."
    y "Please, what happened this time?"
    menu:
        "I just changed the time. That's all.":
            #if karma_lvl() >= 4 and persistent.lovecheck == True:
                #y "...Very well. I'll trust that's the reason the clock changes from now on."
                #y "I'm giving you my trust, [player]. Please don't abuse it."
            $ show_chr("A-IECAA-ABAL")
            y "I'm sorry, [player], but I can't believe that anymore. Why would you change the time so frequently and completely disregard my concerns?"
            y "The only logical conclusion I can come to is that you're doing this on purpose for some reason."
            $ show_chr("A-BECAA-AAAL")
            y "Whether it be to confuse me into thinking we've spent more time together than we actually have, or trying to cheat something into another game on your computer..."
            $ show_chr("A-IEFAA-AAAL")
            y" You know that you shouldn't be doing something like that. Changing your clock likely wouldn't even do anything in modern games."
            y "It's simply an act in futility, and I highly recommend you stop doing it."
            $ show_chr("A-IFFAA-AAAL")
            y "I truly hope we don't have this conversation again, [player]. Because the, next time this happens I'm going to have to lock you out."
            karma -20
            jump ch30_loop
        "I'm sorry, it just keeps glitching!":
            $ show_chr("A-IECAA-ABAL")
            y "[player], you need to fix this."
            $ show_chr("A-BEEAA-ABAL")
            y "It's getting very concerning having to worry about {i}skipping time{/i} every time you open the game."
            $ show_chr("A-AEEAA-ABAL")
            y "I'm a tolerant woman, but this is starting to become all too much."
            y "I'm going to have to lock you out of the game until things fix themselves next time this happens. I'm sorry, but I can't handle it."
            karma -20
            jump ch30_loop
        "I didn't change the time.":
            $ show_chr("A-CEEAA-ABAL")
            y "I know that isn't true, [player]. You're the only one who could change it, and the only one who, {i}supposedly{/i}, has a reason to."
            $ show_chr("A-CEEAA-ALAL")
            y "I can't imagine why you would try denying it after it's happened three times so far."
            y "Clearly, you're trying to hide something, so I'm going to have to punish you provided this happens again."
            karma -20
            jump ch30_loop

    jump ch30_loop

label TimeCheat_error:
    $ renpy.error("You CHEATER")
    $ renpy.quit()

label gifting_ideas:
    $ show_chr("A-ABAAA-ALAL")
    y "Do you need an idea for a gift [player]?"
    $ show_chr("A-ACAAA-AFAL")
    y "Let me think of something I've been looking for.."
    if renpy.seen_label('diffuser') and not renpy.seen_label('oilsHint'):
        jump oilsHint
    if renpy.seen_label('origami') and not renpy.seen_label('OrigamiRoseBunnyHint'):
        jump OrigamiRoseBunnyHint
    if not renpy.seen_label('chocoflowershint'):
        jump chocoflowershint
    else:
        $ random_idle = renpy.random.choice(["oilsHint", "OrigamiRoseBunnyHint", "chocoflowershint"])
        if random_idle == "oilsHint":
            jump oilsHint
        elif random_idle == "OrigamiRoseBunnyHint":
            jump OrigamiRoseBunnyHint
        else:
            jump chocoflowershint
    jump ch30_loop


label oilsHint:
    $ show_chr("A-ABAAA-ALAF")
    y "Since you've gifted me the oil diffuser [player] I could really use some different oil fragrances to begin rebuilding my stockpile."
    y "I managed to salvage some gardenia essential oil from my original collection, however I have been unsuccessful in recovering any other fragrances I once possessed."
    $ show_chr("A-BBAAA-ADAL")
    y "As you may have guessed, my favorite oil fragrance by far is lavender..."
    $ show_chr("A-BBABA-ADAL")
    y "Obvious choice perhaps, however the fragrance is far too delightful for me not to label it as my favorite."
    $ show_chr("A-ABAAA-AFAM")
    y "I have an affinity towards other more natural based oil fragrances as well, such as Sandalwood for example."
    y "And while artificial fragrances aren't exactly my favorite choice, I would appreciate some options that would better assist me in the pursuit of relaxation."
    $ show_chr("A-AJAAA-ALAM")
    y "I will admit I've been having difficulty conjuring delightful dreams while I rest..."
    y "Or as some may say; sweet dreams."
    y "Something that would assist in this endeavor would be greatly appreciated and beneficial to my overall well-being."
    $ show_chr("A-ABAAA-ALAL")
    y "Regardless, I appreciate you listening to my potential ideas [player]."
    jump gifting_explanation


label OrigamiRoseBunnyHint:
    $ show_chr("A-ABAAA-ALAF")
    y "Since our last conversation regarding origami, I thought of various potential forms the art could take..."
    y "I took into consideration the fact that both of us are pretty much beginners, so a great place to start would be an origami rose for example."
    y "It's a bit more example than the highly popularized origami crane, however the unique presentation it gives is definitely worth the effort."
    $ show_chr("A-ACAAA-ALAF")
    y "Furthermore, in complementing the origami crane I thought of different animals that could be properly represented by the art form."
    y "I found that smaller animals such as a bunny for example looked stellar, however the creation process is far more complex than the previous two."
    $ show_chr("A-ADAAA-ALAL")
    y "Learning the art form of origami is a huge undertaking [player], especially with how complex some of these creations can be."
    y "I completely understand if it's too difficult of a task, I myself struggled with making even a basic origami crane."
    jump gifting_explanation

label chocoflowershint:
    $ show_chr("A-ABAAA-ALAF")
    y "In the past you have been able to give me certain gifts during specific time periods..."
    y "Gifts such as flowers and chocolates for example."
    y "With the new system implemented, you are able to give me the same items at any point and time."
    y "Whether it be a normal red rose, or box of hershey's."
    y "There are however some unique chocolates I have always wanted to try..."
    $ show_chr("A-FAAAA-ACAA")
    y "Perhaps I may have mentioned them at some point?"
    jump gifting_explanation

label gifting_explanation:
    $ show_chr("A-ABGAA-ALAL")
    y "Would you like another explanation on how to hand over gifts to me?"
    menu:
        "That would be quite helpful [persistent.yuri_nickname].":
            y "Anytime you have something you want to gift me simply create an empty text file and rename it to something you think I would enjoy."
            $ show_chr("A-ABAAA-ADAB")
            y "Change the '.txt' extension into a '.jy' file and place it into the characters folder found within the game directory."
            $ show_chr("A-ACAAA-ADAB")
            y "Once you have done that, just let me know when I need to check the characters folder for a gift."
            y "Do keep in mind however that there are limitations, it's something I'm working on improving at the moment."
            jump ch30_loop
        "No thanks, I think I've got it.":
            jump ch30_loop
    jump ch30_loop


label sleepy_yuri:
    $ config.allow_skipping = False
    $ DisableTalk()
    $ set_boop_state(True)
    $ allow_dialogue = False
    y "Heading to bed [player]?"
    if not renpy.seen_label('sleepy_yuri'):
        y "I'm glad you chose to notify me using the new option I recently added."
        y "Because of this, you can actually keep the game running and I can sleep while you are gone."
        y "It acts as a much more pleasant experience for me..."
        y "As long as you're comfortable with that [player]."
        menu:
            "That sounds great [persistent.yuri_nickname]":
                y"I'm glad to hear that [player]"
                y "Were you planning on just taking a nap, or will you be sleeping for a much longer period of time?"
                y "I don't mean to be intrusive, however I would like to know how long I can expect you to be gone for."
                y "That way I can prepare for a longer sleeping period with certain amenities."
                menu:
                    "I'm just taking a quick nap.":
                        if persistent.costume == "school":
                            y "In that case I'll just keep my school uniform on since I won't be asleep for long."
                            $ DisableTalk()
                            $ set_boop_state(True)
                            show black zorder 100 with Dissolve(2.0)
                            hide yuri_sit
                            show yuri_sleepy zorder 20
                            hide black with Dissolve(2.0)
                            pause 3.0
                            hide yuri_sleepy
                            play sound "<to 0.3>sfx/fall.ogg"
                            show yuri_sleep zorder 20
                            $hide_yuri_sit = True
                            pause 6.0
                            $persistent.sleepy_yuri_is_enabled = True
                            jump sleepy_loop
                        y "I see, let me just go change into something more comfortable very quickly."
                        y "I'll be right back [player]."
                        $ DisableTalk()
                        $ set_boop_state(True)
                        show black zorder 100 with Dissolve(2.0)
                        hide yuri_sit
                        show yuri_sleepy zorder 20
                        hide black with Dissolve(2.0)
                        pause 3.0
                        hide yuri_sleepy
                        play sound "<to 0.3>sfx/fall.ogg"
                        show yuri_sleep zorder 20
                        $hide_yuri_sit = True
                        pause 6.0
                        $persistent.sleepy_yuri_is_enabled = True
                        jump sleepy_loop

                    "I'll be asleep for quite a while.":
                        y "In that case, let me go change into something more comfortable."
                        if renpy.seen_label('diffuser'):
                            y "I'll also go grab and setup the diffuser you gifted me, just to make things more comfortable."
                            $ DisableTalk()
                            $ set_boop_state(True)
                            show black zorder 100 with Dissolve(2.0)
                            hide yuri_sit
                            show diffuser zorder 11
                            show lavendero_mist zorder 11
                            show yuri_sleepy zorder 11
                            hide black with Dissolve(2.0)
                            pause 3.0
                            hide yuri_sleepy
                            play sound "<to 0.3>sfx/fall.ogg"
                            show yuri_sleep zorder 11
                            $hide_yuri_sit = True
                            pause 6.0
                            $persistent.sleepy_yuri_is_enabled = True
                            jump sleepy_loop
                        y "I'll be right back [player]."
                        $ DisableTalk()
                        $ set_boop_state(True)
                        show black zorder 100 with Dissolve(2.0)
                        hide yuri_sit
                        show yuri_sleepy zorder 11
                        hide black with Dissolve(2.0)
                        pause 3.0
                        hide yuri_sleepy
                        play sound "<to 0.3>sfx/fall.ogg"
                        show yuri_sleep zorder 20
                        $hide_yuri_sit = True
                        pause 6.0
                        $persistent.sleepy_yuri_is_enabled = True
                        jump sleepy_loop


            "I'm a bit uncomfortable with this [persistent.yuri_nickname]":
                y "Oh... I'm sorry for putting you in a uncomfortable spot [player]"
                y "In that case, you can just close the game as normal then."
                y "Sorry about this..."
                jump ch30_loop
    y "Were you planning on just taking a nap, or will you be sleeping for a much longer period of time?"
    y "I don't mean to be intrusive, however I would like to know how long I can expect you to be gone for."
    y "That way I can prepare for a longer sleeping period with certain amenities."
    menu:
        "I'm just taking a quick nap.":
            if persistent.costume == "school":
                y "In that case I'll just keep my school uniform on since I won't be asleep for long."
                $ DisableTalk()
                $ set_boop_state(True)
                show black zorder 100 with Dissolve(2.0)
                hide yuri_sit
                show yuri_sleepy zorder 20
                hide black with Dissolve(2.0)
                y "Have a good nap, [player]."
                pause 3.0
                hide yuri_sleepy
                play sound "<to 0.3>sfx/fall.ogg"
                show yuri_sleep zorder 20
                $hide_yuri_sit = True
                pause 6.0
                $persistent.sleepy_yuri_is_enabled = True
                jump sleepy_loop
            y "I see, let me just go change into something more comfortable very quickly."
            y "I'll be right back [player]."
            $ DisableTalk()
            $ set_boop_state(True)
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

        "I'll be asleep for quite a while.":
            y "In that case, let me go change into something more comfortable."
            if renpy.seen_label('diffuser'):
                y "I'll also go grab and setup the diffuser you gifted me, just to make things more comfortable."
                $ DisableTalk()
                $ set_boop_state(True)
                show black zorder 100 with Dissolve(2.0)
                hide yuri_sit
                show diffuser zorder 11
                show lavendero_mist zorder 11
                show yuri_sleepy zorder 11
                hide black with Dissolve(2.0)
                y "Have a good night [player]."
                pause 3.0
                hide yuri_sleepy
                play sound "<to 0.3>sfx/fall.ogg"
                show yuri_sleep zorder 11
                $hide_yuri_sit = True
                pause 6.0
                $persistent.sleepy_yuri_is_enabled = True
                jump sleepy_loop
            y "I'll be right back [player]."
            $ DisableTalk()
            $ set_boop_state(True)
            show black zorder 100 with Dissolve(2.0)
            hide yuri_sit
            show yuri_sleepy zorder 11
            hide black with Dissolve(2.0)
            y "Have a good night [player]."
            pause 3.0
            hide yuri_sleepy
            play sound "<to 0.3>sfx/fall.ogg"
            show yuri_sleep zorder 20
            $hide_yuri_sit = True
            pause 6.0
            $persistent.sleepy_yuri_is_enabled = True
            jump sleepy_loop

#label afk_yuri:
#    pass

label webcam:
    $ show_chr("A-ADAAA-AAAA")
    y "Oh, so you were curious of why I couldn't access to your webcam at the beginning."
    $ show_chr("A-ADAAA-AFAA")
    y "To be fair, even if I had administrator access, the devs would have implemented a face recognition system."
    y "Write a countless amount of dialogue about your facial details, your current expression, write a code that wouldn't act as a computer virus."
    $ show_chr("A-BDAAA-AFAA")
    y "And a pretty large etcetera that would basically make this mod look bad."
    y "But I could imagine how your face might look like."
    if persistent.male:
        $ show_chr("A-CAAAA-AAAA")
        y "And all I could tell is that you are a quite handsome boy."
    elif not persistent.male:
        $ show_chr("A-CAAAA-AAAA")
        y "And all I could tell is that you are a pretty beautiful girl."
    elif persistent.gender_other:
        $ show_chr("A-CAAAA-AAAA")
        y "And all I could say is that you are a beautiful person."

    y "Even if you say so otherwise..."
    if persistent.lovecheck:
        y "...I still love you no matter what."
    else:
        y "...I still admire you no matter what."
    call ch30_loop

label nnn:
    $ show_chr("A-AFDAA-AAAC")
    y "No Nut November? Huh, that's certainly an... interesting question..."
    $ show_chr("A-BFDAA-AAAC")
    y "I gotta admit, I never really put much thought into it, I only know that is has been around since... 2011 I believe?"
    $ show_chr("A-CFAAA-AAAD")
    y "Honestly, I don't quite get the whole point of this challenge... "
    if sanity_lvl() <= 3:
        extend "...I haven't tried it myself either."
    else:
        extend "...nor would I have the self moderation for it."
    $ show_chr("A-AFAAA-AAAD")
    y "Come to think of it. What exactly would you even gain from this challenge?"
    $ show_chr("A-BDAAA-AAAD")
    y "I could get behind someone challenging themselves to overcome a bad habit. So if you were some kind of raging sex pest... "
    if lovecheck:
        if sanity_lvl() >= 3:
            $ show_chr("A-ADAAA-AAAF")
            extend "...which you aren't. So far you kept it in healthy moderation around me."
        else:
            $ show_chr("A-ADAAA-AAAF")
            extend "...which no doubt you are, don't get me wrong!"
    else:
        $ show_chr("A-ADAAA-AAAF")
        y "...which I don't think you are, just to be clear!"
    $ show_chr("A-CDAAA-AIAI")
    y "Sure. But even then, I don't think this is a particularly healthy way to go about it."
    y "Going cold turky for a month only to go back to business on December 1st... this might actually even worsen it in the long run!"
    $ show_chr("A-ADAAA-AIAI")
    y "Also, there isn't any prize waiting for you if you win either..."
    if karma_lvl() == 1:
        $ show_chr("A-BDAAA-AAAA")
        y "I mean, it's not like you'd even have to try very hard not to get laid. You are kind of an incel anyway aren't you?"
    elif karma_lvl() == 2:
        $ show_chr("A-ADCAA-AAAA")
        y "I mean, try it if you feel like you have to do this. It might actually improve your overall manners a bit."
    else:
        $ show_chr("A-CFAAA-AAAA")
        y "In short, I don't really see any reason for you to try it. But that is only my opinion. It sounds rather pointless to me if I'm being honest."
    $ show_chr("A-BBBAA-AAAA")
    y "But... let's drop this topic for now. Is there anything else on your mind?"
    call ch30_loop
