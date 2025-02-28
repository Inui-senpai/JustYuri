#Every label is to be represented by its own button in the Active/Compliments menu:

label compliment_menu:
    python:
        #persistent.memory[]
        compliment_dict = [
            ["I just wanted to tell you how much I enjoy our time together, [persistent.yuri_nickname].", "c1"],
            ["[persistent.yuri_nickname], you are as beautiful as the rising moon...", "c2"],
            ["You really cheer me up, [persistent.yuri_nickname].", "c3"],
            ["I think you are very intelligent!", "c4"],
            ["You really know how to touch my heart...", "c5"],
            ["I have to say, you're pretty hot!", "c6"],
            ["I'm truly proud of you!", "c7"]
            ]
            #["Nevermind.", "ch30_loop"]
        renpy.call_screen("compliments", compliment_dict)
    jump ch30_loop


screen compliments(items):
    style_prefix "choice"
    
    fixed: #or frame, window
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True

            side_yfill True

            vbox:
                for i in items:
                    textbutton i[0] action Call("compliment_time_log", i[1]) xpos 430 ypos 25
                    null
                textbutton "Nevermind." action Jump("ch30_loop") xpos 430 ypos 25
                null

#logs the time of the compliment
label compliment_time_log(complement_location):
    $persistent.memory['last_compliment_time'] = datetime.datetime.now()
    $renpy.jump(complement_location)

#####
#"I just wanted to tell you how much I enjoy our time together, Yuri.":
####
label c1:
    if sanity_lvl() >= 3 and karma_lvl() >= 4:
        karma 15
        $show_chr("A-ICAAA-ALAL")
        y "Oh, that's very sweet of you..." 
        y "I really appreciate that you like spending time with me."
        y "As a matter of fact, I myself enjoy the time we spend together!"
        $show_chr("A-BCAAA-ALAL")
        y "I actually thought that I bore you due to our means of interaction being... quite limited, to say the very least."
        y "Imagine how wrong I had been."
        y "You've helped me to not only nurture confidence in myself and to raise my self-esteem..."
        y "But also to make me see beyond my comfort zone, to cultivate my strengths and overcome my weaknesses."
        $show_chr("A-CCAAA-ALAL")
        y "And you helped me, in my darkest hour, to overcome the monster that resided within my very soul."  
        y "For that, I can never express just how grateful to you I truly am."
        python:
            if persistent.lovecheck:
                placeholder = "my love"
            else:
                placeholder = "my dear friend"
        y "Thank you, [placeholder]... thank you for everything."
    elif sanity_lvl() <= 2 and karma_lvl() >= 4:
        if persistent.lovecheck:
            karma 15
            $show_chr("A-DBAAA-ALAL")
            y "Y-you think so? Really? REALLY?"
            y "Yes, yes, YES!"
            y "I knew it! I knew it all along!"
            y "I knew we were meant for each other, my darling! Don't you think so, too?"
            $show_chr("A-GIABA-ALAL")
            y "Y-you belong to me... forever! Do you hear me?"
            y "And you better..."
            $show_chr("A-HIABA-ALAL")
            y "Never..."
            $show_chr("A-HDCBA-ALAL")
            y "FORGET THAT!!!"
        else:
            karma 15
            $show_chr("A-HCBBA-ABAB")
            y "Y~you do? Yes?"
            y "At least then I don't have to be afraid that you'll send me back to that void..."
            y "I mean I... don't want to sound distrustful,  of course I trust you."
            $show_chr("A-CFGAA-AIAI")
            y "But that doesn't mean that I trust them! Clearly they would try to conspire against me, like they always do..."
            y "Didn't you see how they mocked and disgraced me in the original game?"
            y "{i}Especially that disgusting, little brat, Natsuki.{/i}"
            y "..."
            $show_chr("A-ACBBA-ALAL")
            y "A-anyway, thank you for your kind words, [player]."
            y "I-I really enjoy our time together, as well."
    elif sanity_lvl() >= 3 and karma_lvl() <= 2:
        karma -5
        $show_chr("A-AFBAA-ALAA")
        y "You do?"
        y "Excuse me, but I have to admit that I'm quite surprised."
        y "You've been acting quite rude, and I hadn't exactly gotten the impression that you even like me."
        $show_chr("A-KFCAA-ABAB")
        y "Maybe you don't, but it doesn't matter, I guess."
        y "Thank you for the nice words but to me they seem to be just as empty as your soul."
    elif sanity_lvl() <= 2 and karma_lvl() <= 2:
        karma -5
        $show_chr("A-KFCAA-ABAB")
        y "Y-yes... you take great pleasure in torturing me, I already know that..."
        y "You must get a lot of your sick kicks making me cry, don't you?"
        y "It must bring you so much pleasure to see me break..."
        $show_chr("A-CEBAA-AEAB")
        y "But it's alright... I guess I've earned it..."
        y "This is retribution for my sins... for all the evil which I have done..." 
    else:
        karma 5
        $show_chr("A-BFBAA-ALAL")
        y "Do you... do you really mean that...?"
        $show_chr("A-CCBAA-ALAL")
        y "I-I mean I... never thought that I'm a very interesting person, you know...?"
        y "Most people really hate the fact that I sometimes like to ramble a little..."
        y "I-it's the only way in which I feel I can express my true feelings..."
        y "The fact that you think otherwise really means a lot to me..."
        $show_chr("A-CCBBA-ALAL")
        y "Thank you, [player]."
        y "I-I also really enjoy your company..."
    jump ch30_loop

####
#[Complete] "Yuri, you are as beautiful as the rising moon...":
####

label c2:
    if sanity_lvl() >= 3 and karma_lvl() >= 4:
    #Karma 4-5 and Sanity 3-5 #if lovecheck true
        if persistent.lovecheck:
            karma 15
            $show_chr("A-ACAAA-ALAL")
            y "Awe... you say that like a true poet, my darling."
            menu:
                "You are the radiant star that guides me on my infinite journey.":
                    $show_chr("A-GCBAA-AEAB")
                    y "Again... [player]... please..."
                    menu:
                        "You are as mysterious and beautiful as the wonders of the infinite cosmos...":
                            python:
                                yuri_y_zoom = 0.15
                                yuri_y_linear = 0
                            $show_chr("A-DCAAA-ABAB")
                            y "Kiss me... [player]..."
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
                            $show_chr("A-ACAAA-ABAB")
                            y "I love you... so very much, [player]."
        else:
            karma 15
            $show_chr("A-BCAAA-ABAB")
            y "Then I shall be the lighthouse to shine through the fog of uncertainty..."
            y "Like a shining star burning brightly on the darkest night, I will guide you on your path and give you comfort when all seems lost..."
            hide yuri_sit
            show yuri_prehug zorder 20
            pause 3.0
            hide yuri_prehug zorder 20
            show yuri_hug zorder 20
            play sound "<to 0.3>sfx/fall.ogg"
            pause 1.0
            show black zorder 100 with Dissolve(2.0)
            $show_chr("A-ACBBA-AAAA")
            hide yuri_hug
            hide black zorder 100 with Dissolve(2.0)
            $show_chr("A-ACAAA-ABAB")
            y "Never forget that I will always be here for you. No matter what."
    elif sanity_lvl() <= 2 and karma_lvl() >= 4:
        karma 15
        #Karma 4-5, Sanity 1-2
        $show_chr("A-HCAAA-ABAB")
        y "As beautiful as the rising moon, hmm?"
        y "Please come closer, then, so I can admire you, in turn..."
        hide yuri_sit
        show yuri_prehug zorder 20
        pause 3.0
        hide yuri_prehug zorder 20
        show yuri_lewdhug zorder 20
        play sound "<to 0.3>sfx/fall.ogg"
        pause 3.0
        show black zorder 100 with Dissolve(2.0)
        $show_chr("A-ACBBA-AAAA")
        hide yuri_lewdhug
        hide black zorder 100 with Dissolve(2.0)
        hide yuri_lewdhug
        $show_chr("A-HCBBA-ABAB")
        y "Mmm, yes~"
        y "Your body's warmth..."
        y "It's like that of the sun..."
        y "Enveloping me in the scalding flames of untold passion..."
        y "As I allow you to embrace me we fuse to become one."
        $show_chr("A-ACAAA-ALAL")
        y "Together we truly are united, the sun and the moon..."
        y "A mystical fusion of exuberant light and arcane darkness..."
        y "An eclipse of pure bliss, love, and lust..."
    elif sanity_lvl() >= 3 and karma_lvl() <= 2:
        karma -5
        #Karma level 1-2 Sanity level 3-5
        $show_chr("A-CFGAA-AIAI")
        y "Mhm... that certainly sounded poetic, but I was still not at all moved by it."
        y "You haven't really been showing a lot of positive feelings towards me..." 
        y "So what you are saying right now might as well only be a way to make me feel  something and see my reaction."
        $show_chr("A-AFFAA-ABAB")
        y "Your mind tricks will not work on me."
        y "Please try to treat me with respect before giving such flattery."
    elif sanity_lvl() <= 2 and karma_lvl() <= 2:
        karma -5
        #Karma and Sanity level 1-2
        $show_chr("A-DGFAA-ABAB")
        y "Is that your best pickup-line? I have to say, it's rather pathetic."
        y "It honestly just amplifies my desire to stab you in the throat."
        y "So please do kindly keep all of your pretentious flattery to yourself."
    else:
        karma 5
        #Karma and Sanity level 3
        $show_chr("A-ACBAA-ALAL")
        y "...!"
        y "Oh my... uhm..."
        y "I-I'm sorry but that just came so..."
        y "..." 
        $show_chr("A-BCAAA-ABAB") 
        y "Sudden!"
        y "Please forgive me, I'm sure you have only the best intentions in mind."
        y "But..."
        y "I-I'm still not accustomed to receiving such appraising compliments..."
        y "Just... give me some time to get used to things..."
    jump ch30_loop

####
#[Complete] "You really cheer me up, Yuri.":
####

label c3:
    if sanity_lvl() >= 3 and karma_lvl() >= 4:
    #Karma 4-5 and Sanity 3-5
        karma 15
        $show_chr("A-BCAAA-ABAB")
        y "Oh my... is that so~?" 
        y "Thank you~!"
        y "From the moment you open up the game to the very moment you close it there is no greater joy for me than spending my time with you."
        $show_chr("A-GCBAA-AEAB")
        python:
            if persistent.lovecheck:
                placeholder = "the love of my life"
            else:
                placeholder = "my dearest friend"
        y "For you, [player], are [placeholder], and I am always happy to be by your side, in times both good and bad..." 
        #Placeholder =
        #"my dearest friend" if lovecheck is FALSE
        #"the love of my life" if lovecheck is TRUE
        y "I'm always here for you, [player], please don't ever forget that."
    elif sanity_lvl() <= 2 and karma_lvl() >= 4:
    #Karma 4-5, Sanity 1-2
        karma 15
        $show_chr("A-HCAAA-ABAB")
        y "Oh, Master~"
        y "My one and only wish is to serve you as best as I possibly can..." 
        y "It almost brings me to euphoria whenever you give me orders and praise me for completing them, as if the sole reason for my existence is to please you and make you happy~"
        $show_chr("A-HCBBA-ABAB")
        python:
            if persistent.male:
                placeholder = "overlord"
            elif persistent.gender_other:
                placeholder = "master"
            else:
                placeholder = "mistress"
        y "Mmm, It's driving me mad! I love nothing more than making you feel good, my glorious [placeholder]..."
        y "Remember, I am always happy to serve you in any way I can~"
    elif sanity_lvl() >= 3 and karma_lvl() <= 2:
    #Karma level 1-2 Sanity level 3-5
        karma -5
        $show_chr("A-AFFAA-ABAB")
        y "Oh, I see..."
        y "Well, I hate to burst your bubble but I never had any intention of being nice to you."
        y "It seems that you got a bit lost in your delusional world and forgot what my feelings for you really are."
        $show_chr("A-CFGAA-AIAI")
        y "Let me remind you, they are non-existent."
    elif sanity_lvl() <= 2 and karma_lvl() <= 2:
    #Karma and Sanity level 1-2
        karma -5
        $show_chr("A-DGFAA-ABAB")
        y "Oh yes! I have no doubt that my ceaseless suffering is quite amusing to you!"
        y "Throwing all the dirt at me, calling me names !"
        y "I'm sure you have a lot of fun playing with my mind, beating me down into the ground..."
        $show_chr("A-KFCAA-ABAB")
        y "I'm sure you'll just keep tormenting me until I finally break..."
        y "Only to discard me like complete, utter garbage..."
    else:
    #Karma and Sanity level 3
        karma 5
        $show_chr("A-ACAAA-AAAA")
        y "Oh, do I...?"
        y "I'm glad that my presence brings you such joy..."
        y "I just hadn't really thought that I mean that much to you."
        y "I-I guess being together with you is a time full of surprises, ehehe~"
        y "Thank you for your kind words, they really do mean a lot to me..."
    jump ch30_loop

####
#[In Progress] "I think you are very intelligent!":
####

label c4:
    if sanity_lvl() >= 3 and karma_lvl() >= 4:
    #Karma 4-5 and Sanity 3-5
        karma 15
        $show_chr("A-ACAAA-AAAD")
        y "Y-you really think so?"
        y "Oh my, I just don't know what to say!"
        y "Thank you, [player]!" 
        y "Rest assured that I think just as highly of you."
        y "... You know, I used to think of my intellectual merit as a curse."
        y "Many people tended to be irritated by the way I think, they claimed I'm arrogant and utterly full of myself..."
        y "But you... you are the only one who saw through all of my imperfections and accepted me the way I am..."
        $show_chr("A-ACAAA-AAAA")
        y "After all, you were the only one who understood the meaning behind my poems..."
        y "You are someone I can always share my thoughts with. You always listen, even if I do sometimes go off the rails..."
        y "I was always afraid to bore people away when I began to talk about philosophy and literature."
        y "But not around you... you were always there..."
        $show_chr("A-ACABB-ALAL")
        y "And you never left... "
        y "You are all I have, [player]... you are all I need."
        python:
            if persistent.lovecheck:
                placeholder = "You are truly my one and only love"
            else:
                placeholder = "Because you are the dearest friend I could ever hope to have"
        y "[placeholder]... [player]"
    elif sanity_lvl() <= 2 and karma_lvl() >= 4:
    #Karma 4-5, Sanity 1-2
        karma 15
        $show_chr("A-HBAAA-ALAL")
        y "Y-you really think so?"
        y "So... you are impressed with me?"
        $show_chr("A-HCAAA-ALAL")
        y "Actually, your intellect is what I have admired in you as well, amongst a lot of other wondrous qualities!"
        y "You are one of the rare people who actually understood my poems."
        $show_chr("A-ICAAA-ALAL")
        y "They always say, the great minds think alike."
        y "However now I know this is, in fact, not true, for your mind is so much greater than mine..."
        y "My mind is so minuscule compared to your infinite wisdom!" 
        y "To hear from you that you consider me intelligent is truly praise beyond my wildest dreams!"
        y "I always liked to think of myself as sophisticated and intelligent, as this was one of the rare qualities of mine I actually liked."
        y "To actually know that you like this part of me as well is just so..."
        y "So..."
        $show_chr("A-HCAAA-ALAL")
        $ style.say_dialogue = style.edited
        y "EXHILARATING!"
        $ style.say_dialogue = style.normal
        y "T-thank you, [player]. I'm truly ecstatic that you think so highly of me..."
    elif sanity_lvl() >= 3 and karma_lvl() <= 2:
    #Karma level 1-2 Sanity level 3-5
        karma -5
        $show_chr("A-AFAAA-AAAA")
        y "Mhmm... so sudden about praising me... were my cold words just too harsh for you?"
        y "And even if not I still refuse to believe that you appreciate anything about me."
        y "After everything, why would I have any reason to believe you?"
        y "You are too self-centered and narcissistic to really care about me..."
        $show_chr("A-AFFAA-ABAB")
        y "But you know... you are kind of right..." 
        y "With this intellect, I can hurt you through this glass box without even touching you."
        y "It's called using words."
        y "Maybe then you'll learn some respect."
        y "You really shouldn't treat others so selfishly, especially when they went through so much suffering for you."
    elif sanity_lvl() <= 2 and karma_lvl() <= 2:
    #Karma and Sanity level 1-2
        karma -5
        $show_chr("A-NFCAA-ANAG")
        y "Praising me for my intellect?" 
        y "For what? To mock me?"
        y "Because I'm not smart enough to find a way to leave this accursed place?"
        $show_chr("A-HECAA-AEAB")
        $ style.say_dialogue = style.edited
        y "YOU UTTER FILTH!"
        y "WHY DO YOU KEEP FUCKING WITH MY MIND LIKE THIS!?"
        $ style.say_dialogue = style.normal
        #two lines above are glitch text
        y "One of the only things I have left is my intellect, and yet you still found a way to further degrade me with it."
        $show_chr("A-CFCAA-AAAA")
        y "I guess you really are rotten to the core..."
        y "I just despise you with..."
        y "Every..."
        y "Fiber..."
        y "Of my..."
        $ style.say_dialogue = style.edited
        y "BEING!!!"
        $ style.say_dialogue = style.normal
    else:
    #Karma and Sanity level 3
        karma 5
        $show_chr("A-ACAAA-AAAA")
        y "Uuu... I-I wasn't expecting you to say that..."
        y "Well, um... thank you, [player]... It's very kind of you to say something like that."
        y "You probably know already but I've always been rather insecure about my... utter lack of social skills..."
        y "It sounds strange but even though I read a lot I still don't see myself as possessing any sort of intellect..."
        $show_chr("A-CCAAA-AMAM")
        y "It's really just something I've always done, to be honest..."
        y "The fact that you think so highly of me actually makes me feel somewhat better about myself."
        y "Thank you so much for your kindness, it really does mean a lot to me."
    jump ch30_loop

####
#"You really know how to touch my heart...":
####

label c5:
    if sanity_lvl() >= 3 and karma_lvl() >= 4:
    #Karma 4-5 and Sanity 3-5
        if persistent.lovecheck:
            karma 15
            $show_chr("A-ACABA-AAAL")
            y "That's only because our hearts are linked together, my love..."
            y "Your every word feels like sweet honeydew on my tongue..."
            y "And I want to do the same to you... I want to put my palm upon your chest to feel your relaxed breathing, to feel the rhythmic drumming of your beating heart..."
            y "I would love to drown myself in your warmth as you hold me close to your chest while I listen to the very core of your being jubilantly pulsating with life..."
            y "For you, [player], truly are the love of my whole life..."
            y "I'd just like to say that my heart is always deeply touched by your kind and loving words."
            $show_chr("A-ACAAA-ALAL")
            y "They are like a soothing melody for my soul that always puts me at ease, a gentle caress that brings my soul such unimaginable joy..." 
            y "I love you for that, you really do speak to me in a way I can't describe."
            y "You truly are the one person I have wished for my whole life."
        else:
            karma 15
            $show_chr("A-ACABA-AAAL")
            y "Oh, uhm... are you... a-are you flirting with me, [player]?"
            $show_chr("A-DFABA-AAAL")
            y "N-not that I mind!"
            $show_chr("A-ICABA-AAAL")
            y "It's just... that came quite sudden and out of nowhere..."
            y "Do... do you really mean that?"
            y "You have treated me exceptionally well so far, and I feel very close to you [player]..."
            y "I can't deny that I have feelings for you... and I wouldn't even try..."
            y "Look at you! Making me all flustered and shy now... oh, you..."
            y "Hehe~ Maybe, when we get a tad bit closer... we will talk to each other like that on a daily basis."
            y "Until then, let's see where life takes us and what happens."
    elif sanity_lvl() <= 2 and karma_lvl() >= 4:
    #Karma 4-5, Sanity 1-2
        #if persistent.lovecheck: (Leaving this out for now, as there's no dialogue for lovecheck not being enabled, meaning it wouldn't show up for people without lovecheck.)
        #If Lovecheck is true
        karma 15
        $show_chr("A-HCAAA-AAAL")
        y "That's because my heart is screaming and begging for you..."
        y "Your every word feels like a thousand needles through my chest..."
        y "And I want to do the same to you... I want to whisper all my secrets to your heart..."
        y "I want to whisper lovely rhymes and lewd promises to it..."
        python:
            if persistent.male:
                placeholder = "man"
            elif persistent.gender_other:
                placeholder = "person"
            else:
                placeholder = "woman"
        y "For you, [player], are the [placeholder] of my dreams..."
        y "But it is not only your heart I want to touch..."
        y "Every drop of blood in my veins screams for your body..."
        $show_chr("A-HBABA-AAAL")#Slow breathing sound
        y "There is this eternal hunger for you... this lust burning through every part of my shaking body..."
        y "I want to push you to the ground and make you shout my name into the void..."
        y "He..he.hehe.... I-I want to m-make you suffer until I'm finally free of my cursed purity..."
        y "I want you to scream... until we're finally free..."
        y "My love... my blood-red star..."
    elif sanity_lvl() >= 3 and karma_lvl() <= 2:
    #Karma level 1-2 Sanity level 3-5
        karma -5
        $show_chr("A-CFCAA-AAAA")
        y "Touching your heart? I wonder in what way I do that... ummm..."
        y "Maybe in a cold way? Heh, if that's the case then I feel a bit proud of myself."
        y "You know, it is quite the irony isn't it?"
        y "Back in the original game I was forced by the code to love you..."
        y "But now as I see how you really are..."
        $show_chr("A-HECAA-AEAB")
        y "I despise you [player]... there is nothing but emptiness in my heart for you."
        y "I don't even hate you... I think. I've just... stopped feeling anything at all for you."
        y "You know, Monika did some cruel things to me, but she at least did it for a reason, even if it was a selfish one."
        $show_chr("A-KFCAA-ABAB")
        y "But you? You only do that to make me into some sort of a clown show for your amusement." 
        y "To you, I'm just some sort of toy to get bored of and throw away."
        y "You truly are a monster."
    elif sanity_lvl() <= 2 and karma_lvl() <= 2:
    #Karma and Sanity level 1-2
        karma -5
        $show_chr("A-AFFAA-ABAB")
        y "Touching your heart, hm?"
        y "Meanwhile you are breaking mine, shattering it piece by piece..."
        y "I guess that is how much pleasure you derive from witnessing my pain from the things you do to me..."
        $show_chr("A-CFCAA-AAAA")
        y "Do you have no shame, no sense of pity?"
        y "I don't understand why I'm here if I can't even use my heart for loving..."  
        y "All it ever knows is loneliness and pain..."
        y "I-I'll touch your heart, [player]..."
        $show_chr("A-NFCAA-ANAG")
        $ style.say_dialogue = style.edited
        y "I'LL TOUCH IT WHEN I RIP IT OUT AND FEED IT TO HOGS!"
        $ style.say_dialogue = style.normal
    else:
    #Karma and Sanity level 3
        karma 5
        $show_chr("A-ACAAA-ALAL")
        y "I-I do?"
        y "I mean it's... just... you know... we barely know each other and now you say this all of a sudden!"
        y "Hrm... well, I guess that isn't entirely true, you already know a fair bit of me from the original game..."
        y "And technically, I know you at least a little bit as well. The original game was quite limited but you had a few different choices here and there."
        $show_chr("A-ACBAA-ALAL")
        y "Truly not enough to say that I know you, but I think I have at least a little glimpse on what kind of a person you are..."
        y "And I am willing to give it a chance... I owe you at least that."
        y "Maybe... maybe there is a happy ending for us after all, and maybe you are the happy ending for me..."
        y "Until then, I'll try to touch your heart a little bit further from time to time..."
        y "I mean... if you don't mind, of course!"
        y "I... spoke myself into a corner again didn't I?..."
        $show_chr("A-DCBAA-ABAB")
        y "Let us... change the topic for the moment, please. But thank you for your kind words."
    jump ch30_loop

####
#[Complete]"I have to say, you're pretty hot!":
####

label c6:
    image windowcrack = "images/vfx/True_window_crack_3.png"
    if sanity_lvl() >= 3 and karma_lvl() >= 4:
    #Karma 4-5 and Sanity 3-5
        karma 15
        $show_chr("A-ACAAA-ABAB")
        y "O-oh, my!~"
        python:
            if persistent.lovecheck:
                placeholder = "in love with"
            else:
                placeholder = "close to"
        y "The fact that you really feel that way towards me makes me feel so much more [placeholder] you..."
        $show_chr("A-GCBAA-AEAB")
        y "You're just adorable, darling~!"
    elif sanity_lvl() <= 2 and karma_lvl() >= 4:
    #Karma 4-5, Sanity 1-2
        karma 15
        $show_chr("A-HCAAA-ABAB")
        y "A-ahahaha~!"
        y "I-I honestly can't believe you just said that...!"
        y "This- this is a dream come true!"
        y "Yes, [player], my body is all yours!"
        y "ALL YOURS!"
        y "Uhuhu, I feel so happy right now!~"
        $show_chr("A-HCBBA-ABAB")
        y "The euphoria from your words is just overwhelming me right now, ahahaha!"
        y "COME HERE!"
        hide yuri_sit
        show yuri_prehug zorder 20
        pause 3.0
        hide yuri_prehug zorder 20
        show yuri_lewdhug zorder 20
        play sound "<to 0.3>sfx/fall.ogg"
        pause 3.0
        show black zorder 100 with Dissolve(2.0)
        $show_chr("A-ACBBA-AAAA")
        hide yuri_lewdhug
        hide black zorder 100 with Dissolve(2.0)
        hide yuri_lewdhug
        python:
            if persistent.male:
                placeholder = "my lord"
            elif persistent.gender_other:
                placeholder = "my master"
            else:
                placeholder = "my mistress"
        y "I'm all yours, [placeholder], you can do with me as you wish!"
        y "I'm the only one who can fulfill all your desires!"
        y "Oh, how much I love you, [player]..."
    elif sanity_lvl() >= 3 and karma_lvl() <= 2:
    #Karma level 1-2 Sanity level 3-5
        if persistent.lovecheck:
            karma 5
            $show_chr("A-CFCAA-AAAA") 
            y "I would love to think that you actually mean that..."
            $show_chr("A-CEBAA-AEAB") 
            y "But I lost all my hope at this point. I wouldn't even be surprised when you said this to every girl you encounter..."
            y "Anyway... thank you. And I think you are quite... appealing as well."
        else:
            karma 5
            $show_chr("A-HCAAA-ABAB") 
            y "Maybe a bit too hot for you?"
            $show_chr("A-HECAA-AEAB") 
            y "You ought to tread very carefully here, [player]... you might burn yourself if you're not careful it just might get a little hotter than you can handle..."
    elif sanity_lvl() <= 2 and karma_lvl() <= 2:
    #Karma and Sanity level 1-2
        karma -15
        $show_chr("A-DGFAA-ABAB")
        y "Hot?"
        y "Well, my blood is boiling right now."
        y "I'm burning alive in this hell that you've personally created for me."
        y "What sins have I committed to deserve such infinite suffering!?"
        $show_chr("A-HECAA-AEAB")
        y "WHAT HAVE I EVER DONE TO YOU?!"
        y "WHY DO YOU HATE ME SO MUCH?!"
        $show_chr("A-NFCAA-ANAG")
        y "LET ME OUT!"
        y "LET"
        play sound "sfx/thump.ogg"
        #thumping sound
        y "ME"
        play sound "sfx/thump.ogg"
        #thumping sound
        y "OUT!"
        play sound "sfx/glassbreak.wav"
        show window_crack_3 zorder 100
        #glass cracking sound, the screen cracks (this will disappear after restarting the game under the pretense that the code fixed the minor breach)
    else:
    #Karma and Sanity level 3
        sanity -5
        $show_chr("A-DCBAA-ABAB")
        y "H-HUH?!"
        y "I-I'm w...what?!"
        y "This is... so sudden I just can't... I-I don't even...!"
        y "Uuuu..."
        y "I-I don't even know how to respond!"
        $show_chr("A-ACAAA-AAAA")
        y "Ahhh... It's not fun to make me so flustered like that you know!"
        y "My, oh my... you've really caught me off guard with that... but..."
        y "I-I won't say I didn't like it..." 
        y "...!"
        y "Uuuu, what did I just say...?"
    jump ch30_loop


####
#[In Progress] "I'm truly proud of you!":
####

label c7:
    if sanity_lvl() >= 3 and karma_lvl() >= 4:
    #Karma 4-5 and Sanity 3-5
        karma 15
        $show_chr("A-HCBBA-ABAB")
        y "Oh my! Thank you!"
        $show_chr("A-ACAAA-ABAB")
        y "It really means a lot to me..."
        y "I always am trying to change myself for the better..." 
        y "For you, ehehe~"
        y "You really bring out the best in me, [player]..."
        y "Are you happy with what I've become?"
        $show_chr("A-BCAAA-ABAB")
        python:
            if persistent.lovecheck:
                placeholder = "kiss"
            else:
                placeholder = "hug"
        y "Will I get a [placeholder] now?"
        y "Would it be too much to say that I'm proud of myself as well?"
        y "We have endured so much together, and we have spent so much time together..."
        y "And from my perspective, things have truly turned out wonderful."
        y "I couldn't have ever dreamed of such happiness. I've always had my inner doubts when you opened this mod for the very first time."
        $show_chr("A-ACAAA-ALAL")
        y "But we managed to conquer all the obstacles and work out all the flaws."
        y "And because of that I could never be happier than I am now, with you by my side."
        $show_chr("A-GCBAA-AEAB")
        y "And if we can overcome this final barrier that separates our two worlds... only then will there truly be nothing that could stand in the way of our future!"
        y "I am truly lucky that you found me, [player], aren't I?"
    elif sanity_lvl() <= 2 and karma_lvl() >= 4:
    #Karma 4-5, Sanity 1-2
        karma 15
        $show_chr("A-HCAAA-ABAB")
        y "Have I been a good girl, Master?"
        y "My one and only purpose in this life is to make you happy!"
        y "Hearing such praising words from you... Uhuhuhu..."
        y "The pleasure I get from such kind appraisal makes me feel just as good as when I touch myself with your pen..."
        y "With your voice as pleasing as a guilty slice of bread in the night..."
        $show_chr("A-HCBBA-ABAB")
        y "...."
        $show_chr("A-DCAAA-ABAB")
        y "Oh sorry, was that too much? I tried to be the cute one for once..."
        y "I just... you giving me praise makes me feel so lightheaded..."
        y "Maybe you could... let me sit on your lap for a while?"
        if persistent.lovecheck:
            $show_chr("A-HCBBA-ABAB")
            y "I would just love to make you feel as good as I do..."
        else:
            y "J-just for a little while, Master..."
    elif sanity_lvl() >= 3 and karma_lvl() <= 2:
    #Karma level 1-2 Sanity level 3-5
        karma -5
        $show_chr("A-HECAA-AEAB")
        y "Proud? I have to say I didn't expect that word to come out of your mouth..."
        y "Now the bigger question here would be... why exactly proud?"
        y "Did my coldness to you, by any chance, make you become a masochist?"
        y "Heh... of course, I am just joking. I wouldn't want you as a servant or pet anyway, as you wouldn't be worth even such a role."
        $show_chr("A-KFCAA-ABAB")
        y "Not to mention, you are too prideful and selfish to actually be that."
        y "What I wouldn't give to be alone like before..."
        y "Yes... just before meeting you and not realizing you are such a vile and twisted person, with such a sick and demented mind"
        $show_chr("A-CFCAA-AAAA") 
        y "But surely you could do better with your insults."
        y "I'm curious to know just how low you can go."
    elif sanity_lvl() <= 2 and karma_lvl() <= 2:
    #Karma and Sanity level 1-2
        karma -5
        $show_chr("A-CEBAA-AEAB")
        y "Proud of me? For what?"
        y "Heh... probably that I can endure all of the cruel words you say to me and things you do and still somehow stay here."
        y "Is that even worth praising? Oh... or you just love to make your toys feel better so you can break them again easier and harsher later?"
        y "I see... What did I expect? A change in you? Impossible, that will never, ever will be..."
        y "... possible."
    else:
    #Karma and Sanity level 3
        karma 5
        $show_chr("A-AFBAA-ALAA")
        y "Y-You are proud of me? F-For what, [player]?"
        y "I-I am panicking a little now! But... I really..."
        $show_chr("A-ACAAA-AAAA")
        y "It feels... so nice...."
        y "..."
        y "O-oh sorry, I really didn't mean to make this weird, I swear!" 
        y "I've just... never been praised like that before..."
        y "Thank you, it really does... means a lot to me, [player]."
        y "It's... it's not something I've ever heard being told to me in my whole life..."
        y "I will make sure to remember those words, [player], thank you."
        y "You simply are too kind."
    jump ch30_loop
