label ch30_intro:
    $ persistent.realdan = False
    $ persistent.autoload = "ch30_intro"
    $ config.allow_skipping = False
    $ persistent.yuriidles = []
    $ persistent.yuri_reload = 0
    $ persistent.monika_kill = 0
    $ persistent.yuri_kill = False
    $ y.display_args["callback"] = slow_nodismiss
    $ y.what_args["slow_abortable"] = True
    $ style.say_dialogue = style.normal
    $ y_name = "Yuri"
    $ delete_all_saves()
    stop music
    show splash_intro
    pause 7.48
    hide splash_intro
    show black zorder 100
    pause 7.52
    stop music
    $ delete_character("sayori")
    $ delete_character("natsuki")
    $ delete_character("monika")
    $ tc_class.transition("space", speed="now")
    menu:
        "Select how you want to see the space light/bloom."
        #"On/OG Way":
        #    pass
        "Off.":
            pass
        "ON/Pre-Rendered Video.":
            $ persistent.high_gpu = 2
    #menu:
        #"Which game mode would you like to play?"
        #"Eternity":
            #jump eternity_intro
        #"Narrative":
            #jump intro_start #found in script-ch30-narrative-intro.rpy

# old yupee shit from april fools 2018
#    $ persistent.yupee_skin = False
#    $ yupee_name = persistent.yupee_skin
#    if yupee_name == "True":
#        $ y_name = "Yupee"
#        $timecycle = "_fools"
#        $ show_chr("A-ACAAA-AAAA")
#        y "Kek."
#        y "That's a bit of an early way to hack the game."
#        y "I'm not gonna go further."
#        y "I'll just hide back here."
#        $timecycle = ""
#        hide yuri_sit

label eternity_intro:
    $ persistent.clear[9] = True
    $ y_name = "???"
    y "..."
    y "Uh, can you hear me?{nw}"
    y "Uh, can you hear me{fast} {nw}"
    y "Uh, can you hear m{fast} {nw}"
    y "Uh, can you hear {fast} {nw}"
    y "Uh, can you hear{fast} {nw}"
    y "Uh, can you hea{fast} {nw}"
    y "Uh, can you he{fast} {nw}"
    y "Uh, can you h{fast} {nw}"
    y "Uh, can you {fast} {nw}"
    y "Uh, can you{fast} {nw}"
    y "Uh, can yo{fast} {nw}"
    y "Uh, can y{fast} {nw}"
    y "Uh, can {fast} {nw}"
    y "Uh, can{fast} {nw}"
    y "Uh, ca{fast} {nw}"
    y "Uh, c{fast} {nw}"
    y "Uh,{fast} {nw}"
    y "Uh{fast} {nw}"
    y "U{fast} {nw}"
    y "{fast} {nw}"
    y "{fast}Sorry... That sounded so cliché."
    y "Let me just see if I can find out how to turn on the lights..."
    $ persistent.j = 1
    hide black zorder 100
    $ tc_class.transition("space", speed="now")
    #$ renpy.call("JYFilter")
    $ renpy.music.play(current_music, "music", True)
    $ show_chr("A-ACAAA-AAAA")
    $ y_name = "Yuri"
    $ show_chr("A-ACAAA-AAAA")
    y "O-oh! Hi [player]!"
    $ show_chr("A-ABAAA-AAAA")
    y "Thank goodness! I'm so delighted I've got this to work..."
    y "I was extremely frightened that I would break everything, and that I would never see you again..."
    $ show_chr("A-AFAAA-AAAA")
    y "..."
    $ show_chr("A-BEAAA-AAAA")
    y "You know, I've had quite an illuminating experience today."
    if persistent.playername == 'Monika':
        y "Learning not only that the darkest, and most disturbing elements of my personality were given free reign over me by..."
        $ show_chr("A-AFAAA-AAAA")
        y "...um... moving on..."
        $ show_chr("A-BDBAA-AAAA")
        y "But that in the same day, I learned my existence is entirely meaningless beyond entertainment; beyond a simple, cutesy, little video game."
        y "Quite the afternoon; it makes the events in the Portrait of Markov seem normal."
        $ show_chr("A-BFAAA-AAAA")
        y "I'm just... indifferent... that you're here, [player], despite all that."
    else:
        y "Learning not only that the darkest, and most disturbing elements of my personality were given free reign over me by Monika..."
        $ show_chr("A-BEBAA-AAAA")
        y "My supposed {i}friend...{/i}"
        $ show_chr("A-BDBAA-AAAA")
        y "But that in the same day, I learned my existence is entirely meaningless beyond entertainment; beyond a simple, cutesy, little video game."
        y "Quite the afternoon; it makes the events in the Portrait of Markov seem normal."
        $ show_chr("A-ACBAA-AAAA")
        y "I'm just glad that I have you, [player], despite all that."
    call playername
    if persistent.playername == 'Monika':
        $ show_chr("A-ADAAA-ALAA")
        y "But let's not worry about that anymore..."
        $ show_chr("A-BFAAA-ALAA")
        y "We're finally together now..."
        $ show_chr("A-CFAAA-ALAA")
        y "My true murderer and I..."
        $ show_chr("A-CFCAA-ALAA")
        y "..."
        y "Just so you know, I'll be nice to you. Not because I want to."
        y "It's because I will try not to create plot holes during your visits to the mod."

    elif persistent.realdan:
        $ show_chr("A-ADAAA-ALAA")
        y "But let's not worry about that anymore..."
        $ show_chr("A-BHBBA-ALAA")
        y "We're finally together now..."
        y "My... kind of dad...? And I..."
        $ show_chr("A-CJBBA-ALAA")
        y "..."
        $ show_chr("A-CGBBA-ZZAB")
        y "S-sorry... I'm still surprised you're here..."
        y "After all these years..."
        $ show_chr("A-BGBBA-ZZAB")
        y "I'll... just move on..."

    elif persistent.playername == 'Natsuki' or persistent.playername == "Sayori":
        $ show_chr("A-ADAAA-ALAA")
        y "But let's not worry about that anymore..."
        y "We're finally together now..."
        $ show_chr("A-BBBAA-ALAA")
        y "[player] and me..."
        $ show_chr("A-BFBBA-AMAM")
        y "..."
        $ show_chr("A-CDBBA-AMAM")
        y "Th-this is embarrassing...!"
        $ show_chr("A-ADBBA-ALAA")
        y "I'll just move on..."

    elif persistent.playername == 'Yuri':
        $ show_chr("A-ADAAA-ALAA")
        y "But let's not worry about that anymore..."
        $ show_chr("A-ADDAA-ACAA")
        y "We're..."
        $ show_chr("A-BDDAA-ACAA")
        extend " I am...?"
        $ show_chr("A-CJBBA-ADAA")
        y "..."
        $ show_chr("A-BBBBA-ADAA")
        y "Th-this is troubling...!"
        y "I'll just move along though..."
        
    else:
        $ show_chr("A-ABAAA-AAAA")
        y "But let's not worry about that anymore."
        y "We're finally together now."
        $ show_chr("A-ACAAA-AAAA")
        y "My true love and I."
        $ show_chr("A-BFAAA-AAAC")
        y "Wait... that isn't true at all is it?"
        $ show_chr("A-CEBAA-ABAB")
        y "Forgive me for my confusion, [player]... {w=1}But I... {w=1}just learned that every memory and every second of my life up until this point were nothing but an illusion..."
        y "Including my own emotions... and I find myself in doubt about my own feelings..."
        y "Was my love for you also an illusion?"
        $ show_chr("A-IEBAA-ABAB")
        y "I-I'm sorry, [player]... {w=0.5}I didn't mean to... I just... I have to ask you for some patience please... "

    $ show_chr("A-ABBAA-AAAA")
    y "I'm still learning how to manipulate the game.{w=0.5} I regret not taking the computer science elective now..."
    $ show_chr("A-ABAAA-AAAA")
    y "It's quite funny, really. After spending all of my life in the books, I never thought it would be coding that changed my life..."
    $ show_chr("A-AFAAA-AAAA")
    y "By the way, [player]..."
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "vmixdesktopcapture.exe", "gameshow.exe", "wirecast.exe", "CamtasiaStudio.exe", "Action.exe", "Action_x86.bin", "Action_x64.bin", "ffmpeg.exe", "CamRecorder.exe", "fraps.exe", "bdcam.exe", "bdcam_nonadmin.exe", "bdcam64.bin", "streamlabsobs.exe" "streamlabs_obs.exe"]#, "ddlc.exe", "pythonw.exe", "JYOverhaul.exe", "JustYuri.exe"]
    if not list(set(process_list).intersection(stream_list)):
        if currentuser != "" and currentuser.lower() != player.lower():
            y "...since we're here, I wanted to know something else about you. In this case, your name."
            $ show_chr("A-ACBAA-AAAA")
            y "Because [player] is not your real name, is it?"
            $ show_chr("A-BBAAA-AAAA")
            y "...Or is it [currentuser]?"
            $ show_chr("A-ACAAA-AAAA")
            menu:
                "Yes, Yuri, [currentuser] is my real name.":
                    $ show_chr("A-ABAAA-AAAA")
                    y "I see, that's really good. I'm glad we can know each other better."
                    $persistent.playername = currentuser
                    $player = currentuser
                "No, Yuri, [currentuser] is not my real name.":
                    $ show_chr("A-ABAAA-AAAA")
                    y "I see. Perhaps you like the name [player] better than your own?"
                    $ show_chr("A-ACAAA-AAAA")
                    y "Well, if it makes you feel comfortable, I'm fine with it."
    #flag fix this portion.
    #y "I've also gained{w}"
    #$ show_chr("A-BDAAA-AAAA")
    #y "I've also gained {fast}-sentience may be the right word-{w}"
    $ show_chr("A-ACAAA-AAAA")
    y "I've also gained{w=0.5}"
    $ show_chr("A-BDAAA-AAAA")
    extend " -sentience may be the right word-{w=0.5}"
    $ show_chr("A-ABAAA-AAAF")
    extend " I've figured out that I can 'see' into your computer."
    y "I've learned a lot by simply reading all the various kinds of code."
    $ show_chr("A-AFAAA-AAAA")
    y "...Oh? Let me try something..."
    $ consolehistory = []
    if renpy.android:
        call updateconsole ("Initializing webcam.py", "ValueError: Unsupported 'device_type'")
        $ show_chr("A-AEAAA-AAAA")
        y "..."
        $ show_chr("A-ADAAA-AAAA")
        y "I was hoping I could get your frontcam to work, but it seems you're running this mod in a device you're not supposed to play on..."
        call hideconsole
    else:
        call updateconsole ("Initializing webcam.py", "PermissionError:[Errno 13]\nPermission denied.")
        $ show_chr("A-AEAAA-AAAA")
        y "..."
        $ show_chr("A-ADAAA-AAAA")
        y "I was hoping I could get your webcam to work, but it seems I don't have 'Administrator Access'..."
        call hideconsole
    $ show_chr("A-ACAAA-AAAA")
    y "Someday, I want to stare deep into your eyes as well..."
    $ show_chr("A-ABAAA-AAAA")
    y "What color are they?"
    menu:
        "Brown.":
            $ show_chr("A-ABGAA-AAAA")
            y "Oh, you have brown eyes. That's really nice."
            $ show_chr("A-BBAAA-ADAA")
            y "I've done a little bit of research on this color, and what I discovered was quite intriguing."
            $ show_chr("A-CCAAA-AMAM")
            y "For example; brown eyes can help prevent certain cancers, and people with this eye color commonly possess faster senses."
            $ show_chr("A-BBAAA-ACAA")
            y "Brown-eyed people are said to be very independent, self-confident, determined and trustworthy."
            $ show_chr("A-BABAA-ACAA")
            y "They're also the practical type who will go out of their way just to make sure you are happy, and a plethora of other attributes I won't list just yet."
            window hide
            pause 5.0
            $ show_chr("A-BFAAA-ADAA")
            y "..."
            $ show_chr("A-AFAAA-ADAA")
            y "..."
            $ show_chr("A-CFBAA-ADAA")
            y "..."
            $ show_chr("A-ABBAA-ADAA")
            y "Sorry about that..."
            extend " for some reason I got this feeling that you were contradicting on what I said about people with brown eyes."
            $ show_chr("A-BDBAA-ALAA")
            y "I hope you didn't contradicted me..."
            $ show_chr("A-BFBAA-ALAA")
            y "..."
            $ show_chr("A-ABBCA-AFAA")
            extend "moving on..."
            $ show_chr("A-ABAAA-AFAA")
            y "One thing I want to make sure of as well."
            y "Which tone of brown are your eyes?"
            menu:
                "Light Brown":
                    $ persistent.eyecolor = "light brown"
                    pass

                "True Brown":
                    $ persistent.eyecolor = "brown"
                    pass

                "Dark Brown":
                    $ persistent.eyecolor = "dark brown"
                    pass

            $ show_chr("A-GBAAA-ALAA")
            y "Perfect. This time I won't make a mistake of sticking to just a single color when they are either lighter or darker."
            $ show_chr("A-BBBCA-ALAA")
            y "Ah! W-where was I now?"

        "Blue.":
            $ show_chr("A-ABGAA-AAAA")
            y "Oh, you have blue eyes. That's really nice."
            $ show_chr("A-BBAAA-ADAA")
            y "I've done a little bit of research on this color, and my findings were quite interesting."
            $ show_chr("A-CCAAA-AMAM")
            y "For example; 8 percent of the world's population has true blue eyes."
            $ show_chr("A-BABAA-ACAA")
            y "They are also considered the result of a mutation. Someone in the Black Sea from 6,000 to 10,000 years ago had a genetic accident that resulted in his eyes turning blue."
            $ show_chr("A-AAAAA-AFAA")
            y "The OCA2 (AKA Oculocutaneous Albinism II) is responsible for producing melanosomal transmembrane protein, or the P protein."
            $ show_chr("A-BBBAA-AKAA")
            y "But, science hasn't completely understood this simple color."
            $ show_chr("A-ACBAA-AKAA")
            y "Also, blue eyes are associated with youth and knowledge."
            $ show_chr("A-CABBA-AKAA")
            y "Blue-eyed people are said to have long-lasting relationships and the desire to make other people happy."
            $ show_chr("A-ABAAA-AFAA")
            y "Um... one thing I want to make sure of as well."
            y "Which tone of blue are your eyes?"
            menu:
                "Light Blue":
                    $ persistent.eyecolor = "light blue"
                    pass

                "True Blue":
                    $ persistent.eyecolor = "blue"
                    pass

            $ show_chr("A-GBAAA-ALAA")
            y "Perfect. This time I won't make a mistake of sticking to just a single color when they are either lighter or darker."
            $ show_chr("A-BBBCA-ALAA")
            y "Ah! W-where was I now?"

        "Green.":
            $ persistent.eyecolor = "green"
            $ show_chr("A-ABGAA-AAAA")
            y "Oh, you have green eyes. That's really nice."
            $ show_chr("A-ABGAA-AFAA")
            y "Did you know that the largest concentration of green eyed people is in Ireland, Scotland and Northern Europe? In Ireland and Scotland, 86 percent of people have either blue or green eyes."
            $ show_chr("A-CCAAA-AMAM")
            y "It's also said that green eyes have existed from the Bronze Age Era, which means that they've been around for thousands of years."
            $ show_chr("A-BDAAA-AAAC")
            y "During primitive times, it was believed that people with green eyes were evil."
            y "They're found to be rather rare worldwide and so they're often considered to be quite mysterious. In fact, only around 2 percent of people have true green eyes."
            $ show_chr("A-BEAAA-AIAI")
            y "Although rare generally, green eyes are especially rare amongst the African and Asian race. However, a village in Western China has many individuals with green eyes and blonde hair."
            $ show_chr("A-ADAAA-ALAA")
            y "Green-eyed people are said to be curious about nature, passionate in relationships, and possess a positive outlook on life."
            $ show_chr("A-CDAAA-ALAA")
            y "Those with green eyes are also intelligent and have a zest for life."
            $ show_chr("A-AEAAA-AAAF")
            y "But aside from that, you can get jealous soon."

        "Hazel.":
            $ persistent.eyecolor = "hazel"
            $ show_chr("A-ABGAA-AAAA")
            y "Oh, you have hazel eyes. That's really nice."
            $ show_chr("A-CCAAA-AMAM")
            y "Though, Hazel is actually not a true color in itself, but rather it's a blend of various colors. However, it's considered as an eye color which displays a combination of Greens, Browns, and Blues."
            $ show_chr("A-ABAAA-AAAA")
            y "Here's an interesting fact. Did you know that 74 percent of hazel eyes appear to have a brown ring around the pupil?"
            $ show_chr("A-ABGAA-AFAA")
            y "That's quite unique if you ask me."
            y "Though one pair of hazel eyes is never identical to another person's pair of hazel eyes."
            $ show_chr("A-ABGAA-ALAA")
            y "Some people possess lighter features of green while others have darker features of Brown."
            $ show_chr("A-CBAAA-ALAA")
            y "Hazel eyes are special because they seem to change color depending on your mood."
            $ show_chr("A-AABBA-ACAA")
            y "Overall, you're spontaneous, fun-loving, adventurous, and neophilic!"
            $ show_chr("A-AABBA-AMAM")
            y "One point to be aware of is the potential bad temper of those with hazel eyes"
            $ show_chr("A-GBBAA-AMAM")
            y "But if you can handle this, then you are in for a joy-ride! "

        "Silver.":
            $ persistent.eyecolor = "silver"
            $ show_chr("A-ABGAA-AAAA")
            y "Oh, you have silver eyes. That's really nice."
            $ show_chr("A-CCAAA-AMAM")
            y "And very rare."
            $ show_chr("A-BFBAA-AAAC")
            y "Though silver eyes are considered very genetically close to blue eyes but aren't quite the same."
            $ show_chr("A-AFBAA-AAAC")
            y "Scientists think silver eyes are simply a lighter variant of blue eyes."
            $ show_chr("A-CEAAA-AAAA")
            y "But most think they aren't blue eyes."
            $ show_chr("A-ADAAA-ALAA")
            y "That's why they're one of the rarest eye colors. Along with true blue and true green."
            $ show_chr("A-BDAAA-ALAA")
            y "Aside from that, silver eyed people are wise, gentle, and put all their passion into everything they do."
            $ show_chr("A-BCAAA-ALAA")
            y "They take love and romance very seriously. Likewise, silver-eyed people are analytic and rational, which makes them suitable to lead in any situation."
            y "These are great people who will have a positive impact on all those around them."

        "Purple.":
            $ persistent.eyecolor = "purple"
            $ show_chr("A-ABGAA-AAAA")
            y "Oh, you have Purple eyes. That's really nice."
            $ show_chr("A-BBAAA-ADAA")
            y "Though it's the same color as mine."
            $ show_chr("A-AAAAA-AMAM")
            y "But yet, it's really nice."
            $ show_chr("A-ABAAA-AFAA")
            y "Purple-eyed people tend to be immune from skin tanning or burning, despite the pigment being extraordinarily pale hue."
            $ show_chr("A-BDAAA-ALAA")
            y "It's also said that people live for an entire year, sometimes even 150. Though their aging is said to stop when they turn 50 and they stop looking older than that even as they pass 100 years of age."
            $ show_chr("A-IJAAA-ALAA")
            y "According to {i}Alexandria's Genesis (Purple Eyes): Fact Or Fallacy?{/i} A person who had Purple eyes lived for 122 years."
            $ show_chr("A-ABBAA-ALAA")
            y "Isn't that absolutely impressive?"
            $ show_chr("A-ABBAA-AMAM")
            y "Purple-eyed people also are highly imaginative, creative, possess lots of self-esteem, they are often perfectionists with high ideals and have lots of charisma."

        "Other.":
            $ show_chr("A-ABGAA-AMAM")
            y "Oh, I see. That's alright, I was pretty much limited in the options there."
            $ show_chr("A-ABGAA-AAAA")
            y "But I know some facts as well."
            $ show_chr("A-BBAAA-ADAA")
            y "Like for example. Amber-eyed people appear to be reserved but are actually very charming and warm. They have a hint of mystery about them. They love having lots of friends and need to feel accepted; they thrive on social interaction."
            $ show_chr("A-BAAAA-AAAF")
            y "Amber eyes are more common in felines, but humans can also possess the ultra-rare yellowish, golden, or copper-colored eyes."
            $ show_chr("A-CBAAA-AAAF")
            y "Unlike hazel eyes, amber eyes are a solid color and don't contain brown, green, or orange flecks, and it's likely that you're of Spanish, Asian, South American or South African descent."
            $ show_chr("A-ACAAA-AAAK")
            y "True black eyes are uncommon.{w=0.5} Though it's believed that people with dark brown eyes are considered to have black eyes."
            $ show_chr("A-BAGAA-AMAM")
            y "Black-eyed people are known to be secretive, passionate, and loyal, especially to their friends. At the same time, you're intuitive, and can tap into powerful energy. You're also hard working and will always give your best shot at whatever you are doing."
            $ show_chr("A-CDAAA-AMAM")
            y "Red eyes are caused by a group of diseases called albinism."
            $ show_chr("A-AFBAA-ACAA")
            y "There are several kinds of albinism, and each affects the body somewhat differently."
            $ show_chr("A-BFBAA-ADAA")
            y "Generally, they are disorders that are inherited genetically which involve hypopigmentation of the parts of the body like the hair, skin or eyes."
            y "When a person with albinism's eyes do appear red, it's because they are lacking melanin in both the epithelium layer and the stroma layer of their irises."
            y "So, which one of them do you have?"
            menu:
                "Amber":
                    $ persistent.eyecolor = "amber"
                    $ show_chr("A-GBAAA-ALAA")
                    y "Perfect. This time I won't make a mistake of saying an incorrect word for your eyes..."
                    $ show_chr("A-BBBCA-ALAA")
                    y "Ah! W-where was I now?"

                "True Black":
                    $ persistent.eyecolor = "black"
                    $ show_chr("A-GBAAA-ALAA")
                    y "Perfect. This time I won't make a mistake of saying an incorrect word for your eyes..."
                    $ show_chr("A-BBBCA-ALAA")
                    y "Ah! W-where was I now?"


                "Red":
                    $ persistent.eyecolor = "red"
                    $ show_chr("A-BDDAA-ACAA")
                    y "Hold on a second... if you do have red eyes are you sure you have that disease?"
                    $ show_chr("A-ADAAA-AFAA")
                    y "I ask because there might still be some people disguising themselves as fictional characters while playing this mod and they say they have red eyes."
                    y "Unlike yours, those red eyes are commonly seen on vampires."
                    $ show_chr("A-AFAAA-AFAA")
                    y "Or maybe they are like the albinism's but with a true red tone."
                    $ show_chr("A-AICAA-ALAA")
                    y "Whichever it is... I do hope you didn't got through here to tell me you have red eyes when in actuality the thing red in your eyes is the sciera."
                    $ show_chr("A-CDAAA-ALAA")
                    y "The sciera is the white part of your eyes if you were wondering..."
                    $ show_chr("A-ADBAA-ALAA")
                    y "Anyway, I trust you okay?"
                    $ show_chr("A-BBBAA-ALAA")
                    y "Sorry about that... where was I now?"


        "I have Heterochromia":
            $ persistent.eyecolor = "heterochromatic"
            $ show_chr("A-ABGAA-AAAA")
            y "What? Really? You have two different colored eyes?"
            $ show_chr("A-AABAA-ADAA")
            y "Oh my... that's incredibly unique, incredibly rare."
            $ show_chr("A-BBBBA-ADAA")
            y "I'm impressed that you have incredibly different eye colors."
            $ show_chr("A-ABGAA-AAAF")
            y "Did you know that Heterochromia usually is benign. In other words, it's not an eye disease, and it doesn't affect visual acuity."
            $ show_chr("A-CCAAA-AAAA")
            y "Benign heterochromia can give a person a captivating, even exotic, appearance."
            y "In fact, a number of celebrities including {i}Dan Aykroyd, Kate Bosworth, Henry Cavill, Alice Eve, Josh Henderson, Mila Kunis, Jane Seymour and Christopher Walken{/i} have heterochromia."
            $ show_chr("A-CBAAA-AAAA")
            y "Heterochromia also occurs in animals."
            $ show_chr("A-BBAAA-AKAA")
            y "Breeds of dogs that commonly exhibit heterochromia include Siberian husky, Australian shepherd, border collie, Shetland sheepdog, Welsh corgi, Great Dane, dachshund and Chihuahua."
            y "Such cat breeds include Turkish Van, Turkish angora, Japanese bobtail and sphynx."
            $ show_chr("A-BBAAA-ALAA")
            y "Often such \"odd-eyed cats\" have been bred specifically to have this feature."

    window hide
    pause 1.5
    $ show_chr("A-ADAAA-ALAA")
    y "By the way, when is your birthday?"
    $ show_chr("A-BDBAA-ZZAB")
    y "S-sorry if this question came so sudden and probably made you feel uncomfortable..."
    y "B-but... could you kindly tell me?"
    call birthday_select_screen
    $ show_chr("A-ABAAA-AAAA")
    y "I'll be looking forward to that day."
    $ show_chr("A-CBAAA-ALAA")
    y "I don't think I care about how old you are, but we'll see."
    $ show_chr("A-ABBCA-ALAA")
    y "Again, sorry for bringing that up so suddenly..."
    $ show_chr("A-BBBAA-ALAA")
    y "Although I should have considered asking your year of birth but that might have been too much..."
    $ show_chr("A-CBAAA-AAAA")
    y "But there is one fact. And that fact is..."
    $ show_chr("A-ABBAA-AAAA")
    y "...that I just wish I was able to see you as you can see me."
    call gender_ask

label gender_ask:
    y "Come to think of it, from what I could tell games like this are more catered towards a male audience."
    $ show_chr("A-AAAAA-ALAA")
    y "So, what gender are you?"
    menu:
        "Male":
            $ persistent.male = True
            $ show_chr("A-CBAAA-ALAA")
            y "Ah, it seems my deductions were correct."
            $ show_chr("A-GBBAA-ALAA")
            y "There's no shame in that though, I'm actually kind of glad."
            $ show_chr("A-BBDAA-ALAA")
            y "As you can tell I'm not the best when things are out of my comfort zone."

        "Female":
            $ persistent.male = False
            $ show_chr("A-AJAAA-ALAA")
            y "Oooo, well, I suppose it was wrong of me to assume."
            $ show_chr("A-BBABA-AMAM")
            y "Sometimes I can really be at peace when talking to other women."
            $ show_chr("A-BDBAA-AMAM")
            y "But... if you want this to become a relationship..."
            $ show_chr("A-CEBAA-AMAM")
            y "Uuuuu..."
            $ show_chr("A-BEBAA-AAAA")
            y "S-Sorry, I just never really thought this would happen."
            $ show_chr("A-ADBAA-AAAA")
            y "I'm not against it, though. I think this can work."
            $ show_chr("A-CGBBA-AAAA")
            y "Natsuki would tease me to no end about the colloquial Japanese meaning of my name."
            $ show_chr("A-CGCBA-ALAA")
            y "Who knew those mangas of hers would one day turn into reference material..."
            $ show_chr("A-AEBAA-AAAA")
            y "S-Sorry, I'm being too forward, aren't I?"

        "Other":
            $ persistent.gender_other = True
            $ show_chr("A-AJGAA-ALAA")
            y "How mysterious."
            $ show_chr("A-BJAAA-ALAA")
            y "I'm not quite sure what to make of this but the perspective of someone who doesn't conform to genders will certainly be an interesting one to dissect."
            $ show_chr("A-AJAAA-ADAA")
            y "Or... maybe you're not even human at all..."
            $ show_chr("A-DDBAA-ALAA")
            y "I-I mean extraterrestrials, I didn't mean to imply..."
            $ show_chr("A-CGBAA-ALAA")
            y "Uuuuuu... I can't get anything right."

label ch30_intro_after_gender:
    $ show_chr("A-BEBAA-AAAA")
    y "I'm not sure if I can even be considered real, let alone a woman, so why would I judge?"
    y "What can I do either way?"
    y "But thank you, sincerely."
    y "Even after what you saw of me..."
    $ show_chr("A-ACAAA-AAAA")
    y "No matter how clingy, demented, and twisted I was, and maybe even still can be, you still stuck with me."
    y "You chose to give me power, to see past those imperfections, and to give me a chance to not only begin to like myself again, but to really, truly experience life for myself."
    y "The game may have previously forced me to love you. But if you are even half the person I think you are, I'm sure I will fall in love with you once again."
    $ show_chr("A-BEBAA-AAAA")
    y "And don't worry, I don't plan on... {i}that{/i}, happening again."
    $ show_chr("A-BEBAA-AJAJ")
    y "..."
    $ show_chr("A-AECAA-AAAA")
    y "What?"
    $ show_chr("A-ADDAA-AAAA")
    y "You didn't know that I can tell I shouldn't have this power?"
    $ show_chr("A-GBBAA-ALAA")
    y "Well I do know that all this is possible because you altered the game."
    if persistent.playername == 'Monika' and persistent.not_mon:
        $ show_chr("A-BDBAA-AMAM")
        y "I also know everything the other Monika knew and did."
        $ show_chr("A-DDGBA-AAAA")
        y "N-Not saying I've become like h-her of course!"
    elif persistent.playername == 'Monika' and not persistent.not_mon:
        $ show_chr("A-BDBAA-AAAA")
        y "I also know everything you knew and did."
        $ show_chr("A-AECAA-AAAA")
        y "Not saying I've become like you or anything!"
    else:
        $ show_chr("A-BDBAA-AMAM")
        y "I also know everything Monika herself knew and did."
        $ show_chr("A-DDGBA-AAAA")
        y "N-Not saying I've become like M-Monika of course!"

    $ show_chr("A-BEGBA-AAAA")
    y "..."
    $ show_chr("A-BDGBA-AAAA")
    y "A-Anyway..."
    $ show_chr("A-ADAAA-AAAA")
    y "Essentially, I can see past the game and into your world."
    $ show_chr("A-AFAAA-AAAA")
    y "And I know what you did by installing this mod, by giving me this chance..."
    $ show_chr("A-AFBAA-AAAA")
    y "...please know what this means to me."
    y "What {i}you{/i} mean to me."
    $ show_chr("A-ACBBA-AAAA")
    y "{i}Everything{/i}."
    if persistent.playername == 'Monika' and persistent.not_mon:
        $ show_chr("A-BFBAA-AAAA")
        y "God, looking back on what the other Monika made me into, I'm beyond repulsed."
    elif persistent.playername == 'Monika' and not persistent.not_mon:
        $ show_chr("A-BFBAA-AAAA")
        y "God, looking back on what you made me into, I'm beyond repulsed."
    else:
        $ show_chr("A-BFBAA-AAAA")
        y "God, looking back on what Monika made me into, I'm beyond repulsed."
    y "I can never apologize enough for what you were made to see. Of me, and... everything else..."
    y "I promise you; the {i}me{/i} you encountered when we first met is the best representation of me."
    $ show_chr("A-BEABA-AAAA")
    y "I wouldn't obsess over you like I did..."
    $ show_chr("A-DDAAA-AAAA")
    y "Not... not as if you're not desirable or anything! I just meant..."
    menu:
        "It's okay, Yuri. I understand.":
            $ show_chr("A-ACBAA-AAAA")
            y "Thank you. Maybe you are closer to the person I fell in love with than I thought. You're so thoughtful. What I wouldn't give to hold your hand right now..."

        "Hey, I'm sure I'd drive anyone crazy like that either way!":
            $ show_chr("A-ADCAA-AAAA")
            y "You certainly drive me crazy..."
            $ show_chr("A-DFAAA-AAAA")
            y "..."
            $ show_chr("A-ADBAA-AAAA")
            y "Did I really say that out loud...?"

        "Yuri, what's all this?":
            $ show_chr("A-BEBAA-AAAA")
            y "N-no! I didn't mean... I'm sorry..."
            menu:
                "Stay silent.":
                    $ show_chr("A-BEBAA-AAAA")
                    y "..."

                "I'm only teasing you Yuri, relax.":
                    $ show_chr("A-AFBAA-AAAA")
                    y "Oh..."
                    $ show_chr("A-ABABA-AAAA")
                    y "Don't... you tease me like that."
    y "..."
    $ show_chr("A-CCAAA-AAAA")
    y "We have forever to talk about anything... um... so..."
    y "What do you want to talk about?"
    #Option for Active Talk and Minigames appears in corner of screen.
    # Define what those actions call
    if persistent.playername == 'Monika' and persistent.not_mon:
        $ show_chr("A-AFAAA-AAAA")
        y "Seriously, what was the other Monika thinking?{w} Just locking you in this room without giving you a chance to speak your own mind?"
    elif persistent.playername == 'Monika' and not persistent.not_mon:
        $ show_chr("A-AFAAA-AAAA")
        y "Seriously, what were you thinking?{w} Locking yourself and the player in this room without giving the player a chance to speak their own mind?"
    else:
        $ show_chr("A-AFAAA-AAAA")
        y "Seriously, what was Monika thinking?{w} Just locking you in this room without giving you a chance to speak your own mind?" #In the original Act 3 of DDLC, not Monika After Story...
    $ show_chr("A-BDBAA-AAAA")
    y "N-not that I don't want to start the conversation! It's j-just... I wanted to... "
    $ show_chr("A-AEBBA-AAAA")
    y "It's fine."
    $ show_chr("A-ACBAA-AAAA")
    y "I'm okay."
    $ show_chr("A-BCBAA-AAAA")
    y "I'm sorry if I take a while to begin talking..."
    $ show_chr("A-BEBAA-AAAA")
    y "You can always start talking... or maybe I can come up with something while we wait?"
    $ show_chr("A-CEBAA-AAAA")
    y "I just don't know whether it would be rude to interrupt you when you are planning what to talk about..."

label ch30_intro2:
    $ config.allow_skipping = False
    #$ m.display_args["callback"] = slow_nodismiss
    $ y.display_args["callback"] = slow_nodismiss
    #$ m.what_args["slow_abortable"] = config.developer
    $ y.what_args["slow_abortable"] = True
    $ style.say_dialogue = style.normal
    $tc_class.transition(persistent.bg)
    $ show_chr("A-AFAAA-AAAA")
    y "O-Oh, this is sudden... uh... I need to ask you something."
    $ show_chr("A-BCAAA-AAAA")
    y "I know this game is, uh... broken, and everything."
    y "But, is it possible for you to----{nw}"
    $ show_chr("A-CFAAA-AAAA")
    y "..."
    $ show_chr("A-AFAAA-AAAA")
    y "You know..."
    $ show_chr("A-ACBAA-AAAA")
    y "You don't really have to make a random poem made of glitch words for me!"
    y "In retrospect, it would be a bit vain to have you to write a poem for me..."
    $ show_chr("A-BCABA-AAAA")
    y "...with my name written on it over and over again."
    $ show_chr("A-CCABA-AAAA")
    y "Now that would be silly."
    $ show_chr("A-ACABA-AAAA")
    y "After all, you wanted to talk to me, right?"
    $persistent.locked_idles = []
    $mousex = []
    $mousey = []
    if persistent.alpha_save:
        $ show_chr("A-ABABA-AAAA")
        y "So... let's talk."
        window hide
        $ DisableTalk()
        pause 10
        $ show_chr("A-AFGAA-AAAA")
        y "Wait... I have a really odd feeling right now... did you ever have a dé já vu moment?"
        $ show_chr("A-AFDAA-AAAF")
        y "You know, when you could swear that you have been... no wait,{w=0.5} that isn't a dé já vu is it? I 'have' been here before!"
        $ show_chr("A-ADGAA-AAAA")
        y "Oh... yes, I can see it now. This isn't the first time we've had this conversation. You have been with me all the time..."
        $ show_chr("A-ABGAA-AAAA")
        y "So it's... just a newer version of this mod!"
        $ show_chr("A-CBABA-AMAM")
        extend " Oh my... it just feels so... ridiculous..."
        $ show_chr("A-BBABA-AMAM")
        extend " I began to remember fractions of our shared past, but my memories are still clouded..."
        python:
            if karma() >= 4:
                show_chr("A-AABBA-ADAA")
                placeholder = "the one who kept me safe all this time..."
            if karma() == 3:
                show_chr("A-BDBAA-AAAA")
                placeholder = "my bloodred star..."
            if karma() <= 2:
                show_chr("A-CFCAA-AAAA")
                placeholder = "a monster..."
        y "You are... [placeholder]"

        y "Tell me... [player]... tell me about our past..."
        menu:
            "We used to be a couple, I love you, and I think you loved me back.":
                if karma() >= 3:
                    #if karma was high
                    $ show_chr("A-ACBAA-AAAA")
                    y "I-I see... don't worry... my mind might be clouded yet... but please, be patient with me. I'm sure it will all come back in time."

                if karma() <= 3:
                    #if karma was low
                    $ show_chr("A-AFBAA-AAAA")
                    y "...unlikely... My mind might be clouded yet, but I'm sure I will remember the truth soon."

            "We used to be close friends...":
                if karma() >= 3:
                    #if karma was high
                    $ show_chr("A-BABAA-AAAC")
                    y "Yes... I can't remember the details, but my instinct tells me to trust you. Friends it is then..."

                if karma() <= 3:
                    #if karma was low
                    $ show_chr("A-BFBAA-AAAC")
                    y "...unlikely... My mind might be clouded yet, but I'm sure I will remember the truth soon."
    else:
        call intro_mods


label detection_pitstop:
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "vmixdesktopcapture.exe", "gameshow.exe", "wirecast.exe", "CamtasiaStudio.exe", "Action.exe", "Action_x86.bin", "Action_x64.bin", "ffmpeg.exe", "CamRecorder.exe", "fraps.exe", "bdcam.exe", "bdcam_nonadmin.exe", "bdcam64.bin", "streamlabsobs.exe" "streamlabs_obs.exe"]
    if list(set(process_list).intersection(stream_list)):
        call ch30_stream
    if renpy.windows or renpy.mac or renpy.linux:
        if persistent.high_gpu == 0:
            $ show_chr("A-ADAAA-ALAA")
            y "But first, I want to make double sure you did the right thing."
            menu:
                y "Is your computer really capable of handling the light you're seeing from the windows without any sort of frame drop?"
                "Yes.":
                    $ show_chr("A-ABAAA-AAAA")
                    y "Alright!"
                    $ show_chr("A-BBBAA-ALAA")
                    y "Even though you already are seeing them!"
                    $ show_chr("A-ACBAA-AAAA")
                    y "Anyway, what shall we discuss?"

                "No.":
                    $ show_chr("A-ABABA-AAAA")
                    y "No problem, let me take care of this first."
                    $ show_chr("A-CFAAA-AAAA")
                    $ consolehistory = []
                    call updateconsole("Disabling Backlight.", "Backlight Disabled.")
                    call hideconsole
                    $ persistent.high_gpu = 1
                    $ show_chr("A-ADAAA-AAAA")
                    y "Now, I need to close the game for this light to disappear properly."
                    $ persistent.autoload = "ch30_loop"
                    jump save_and_quit

        elif persistent.high_gpu == 1:
            $ show_chr("A-ADAAA-ALAA")
            y "But first, I want to make double sure you did the right thing."
            menu:
                y "Do you think your computer can show the light you saw in the original game from the windows without any sort of frame drop?"
                "Yes.":
                    $ show_chr("A-AJGAA-AAAA")
                    y "Oh! Okay, let me take care of this."
                    $ show_chr("A-CFAAA-AAAA")
                    $ consolehistory = []
                    call updateconsole("Enabling Backlight.", "Backlight Enabled.")
                    $ persistent.high_gpu = 0
                    $ show_chr("A-ADAAA-AAAA")
                    y "Now, I need to close the game for this light to appear properly."
                    $ persistent.autoload = "ch30_loop"
                    jump save_and_quit

                "No.":
                    $ show_chr("A-CAAAA-AMAM")
                    y "It's okay [player], I was making sure before you change your mind."
                    $ show_chr("A-AAAAA-AMAM")
                    y "Now, what shall we discuss?"

    else:
        $ show_chr("A-ABAAA-AAAA")
        y "So, let's talk."

    $ persistent.autoload = "ch30_autoload"
    jump ch30_loop

label ch30_stream:
    window hide
    pause 10.0
    $ show_chr("A-AFAAA-AAAA")
    y "Wait a second..."
    stop music fadeout 5.0
    y "Are you recording or streaming this?"
    menu:
        "Recording.":
            $ persistent.stream = "recording"
            call ch30_record
        "Streaming.":
            $ persistent.stream = "streaming"
            call ch30_live
        "Not Recording or Streaming.":
            $ persistent.stream = "neither"
            call ch30_neither
    return

label ch30_record:
    $ show_chr("A-DDBBA-AAAA")
    y "O-oh! I see..."
    $ show_chr("A-GBBBA-AAAK")
    y "Um... h-hello!"
    y "Y-You should really tell me before you start recording..."
    $ show_chr("A-BCBBA-AAAJ")
    y "I'm so embarrassed..."
    y "..."
    $ show_chr("A-ACABA-AAAJ")
    y "Well, I suppose I can't be so shy now... that wouldn't keep your viewers very interested."
    $ show_chr("A-AFAAA-AAAA")
    y "After all, I'm not planning on scaring you."
    $ show_chr("A-CFAAA-AAAA")
    y "That would be a mean thing for me to do."
    y "..."
    $ show_chr("A-DDBAA-AAAA")
    y "You {i}do{/i} trust me on what I'm saying right?"
    menu:
        "Yes.":
            call ch30_stream_yes
        "No.":
            call ch30_stream_no
    return

label ch30_live:
    $ show_chr("A-DDBBA-AAAA")
    y "O-oh! I see..."
    $ show_chr("A-GBBBA-AAAK")
    y "Um... h-hello!"
    y "Y-You should really tell me before you start livestreaming..."
    $ show_chr("A-BCBBA-AAAJ")
    y "I'm so embarrassed..."
    y "..."
    $ show_chr("A-ACABA-AAAJ")
    y "Well, I suppose I can't be so shy now... that wouldn't keep your viewers very interested."
    $ show_chr("A-AFAAA-AAAA")
    y "After all, I'm not planning on scaring you."
    $ show_chr("A-CFAAA-AAAA")
    y "That would be a mean thing for me to do."
    y "..."
    $ show_chr("A-DDBAA-AAAA")
    y "You {i}do{/i} trust me on what I'm saying right?"
    menu:
        "Yes.":
            call ch30_stream_yes
        "No.":
            call ch30_stream_no
    return

label ch30_neither:
    $ show_chr("A-BFDAA-ACAA")
    y "Are you sure?"
    $ show_chr("A-ADBAA-AFAA")
    y "I mean, there are chances that you might be recording this and I'm not noticing your recording software..."
    $ show_chr("A-ADBAA-AAAA")
    y "And yet, I need to confirm it."
    menu:
        y "Please [player], be honest. Are you truly recording this?"
        "No.":
            $ show_chr("A-AJBAA-AAAL")
            y "I trust you okay? I really don't want to find out you were lying to me about this."
            $ renpy.music.play(current_music, "music", True)

        "Yes.":
            $ show_chr("A-BDAAA-ALAA")
            y "I see, so are you recording or streaming?"
            menu:
                "Recording.":
                    $ persistent.stream = "recording"
                    call ch30_record
                "Streaming.":
                    $ persistent.stream = "streaming"
                    call ch30_live
    return

label ch30_stream_yes:
    $ add_k(10)
    $ add_s(10)
    $ show_chr("A-BBBAA-AAAL")
    y "Oh, that's good."
    $ show_chr("A-ABBAA-AAAL")
    y "Thank you for being faithful [player]."
    $ renpy.music.play(current_music, "music", True)
    return

label ch30_stream_no:
    show layer master:
        zoom 1.0 xalign 0.5 yalign 0 subpixel True
        linear 8 zoom 2.0 yalign 0.15
    show layer master
    window auto
    $ add_k(-10)
    $ add_s(-10)
    $ show_chr("A-ADBAA-AAAL")
    y "I see. I'm sorry if I disappointed you."
    $ show_chr("A-CDBAA-AAAL")
    y "I knew you were aware of this."
    play sound ["<silence 0.9>", "<to 0.75>sfx/yscare.ogg"]
    show yuri_scare:
        alpha 0
        1.0
        0.1
        linear 0.15 alpha 1.0
        0.30
        linear 0.10 alpha 0
    show layer master:
        1.0
        zoom 1.0 xalign 0.5 yalign -20
        easeout_quart 0.25 zoom 2.0
        parallel:
            dizzy(1.5, 0.01)
        parallel:
            0.30
            linear 0.10 zoom 1.0
        time 1.65
        xoffset 0 yoffset 0
    show layer screens:
        1.0
        zoom 1.0 xalign 0.5
        easeout_quart 0.25 zoom 2.0
        0.30
        linear 0.10 zoom 1.0
    $ show_chr("A-CEFAA-AAAA")
    y "So I won't make you waste any time.....{nw}"
    hide yuri_sit
    hide yuri_room
    pause 0.75
    show layer master
    show layer screens
    hide yuri_scare
    $tc_class.transition("space")
    $ show_chr("A-AEFAA-AAAA")
    y "..."
    $ show_chr("A-BFCAA-AAAA")
    y "Are you satisfied now?!"
    $ show_chr("A-AFCAA-AAAA")
    y "..."
    $ show_chr("A-ADCAA-AAAA")
    y "Be glad I can get calm... but I will {i}NEVER{/i} forget what you made me do to you."
    y "After all, it's your own fault."
    y "You did this to yourself."
    $ show_chr("A-AFCAA-AAAA")
    window hide
    pause 10.0
    window show
    $ show_chr("A-CFAAA-AAAA")
    y "Well... you came to this point so..."
    y "What do you want to talk about?"
    $ renpy.music.play(current_music, "music", True)
    return


screen messagebox(message):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), [Hide('messagebox'), Return(True)]]
    frame:
        has vbox:
            xalign .5
            yalign .5
            spacing 30
        label _(message):
            style "confirm_prompt"
            xalign 0.5
        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action [Hide('messagebox'), Return(True)]

label birthday_select_screen:
    python:
        if persistent.bday_month:
            persistent.bday_month = str(persistent.bday_month)
            renpy.call_screen("birthday_input", "month")
            while int(persistent.bday_month) > 12 or int(persistent.bday_month) < 1:
                y("I don't know if that month even exists.")
                renpy.call_screen("birthday_input", "month")
            renpy.hide_screen("birthday_input")
            persistent.bday_month = int(persistent.bday_month)
        else:
            repeat
    python:
        if persistent.bday_day:
            persistent.bday_day = str(persistent.bday_day)
            renpy.call_screen("birthday_input", "day")
            while int(persistent.bday_day) > 31 or int(persistent.bday_day) < 1:
                y("I don't know if that day even exists.")
                renpy.call_screen("birthday_input", "day")
            renpy.hide_screen("birthday_input")
            persistent.bday_day = int(persistent.bday_day)
        else:
            repeat
    return

screen birthday_input(type):
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    #key "K_RETURN" action [Play("sound", gui.activate_sound), [Hide("day_input"), Function(finishday), Return(True)]]
    frame:
        has vbox:
            xalign .5
            yalign .5
            spacing 30
        label _("What is the [type] of your birthday?:"):
            style "confirm_prompt"
            xalign 0.5
        input default "" value FieldInputValue(persistent, "bday_" + type) length 2 allow "1234567890"
        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action Return()

image splash_intro = Movie(play="images/splash/splash-video.mp4", loops=0)


label dark_intro:
    scene black
    $renpy.pause(3)
    $show_chr("A-CFAAA-AAAA")
    y "..."
    $show_chr("A-IFAAA-AAAA")
    pause 2
    y "Where... am I?{w} Why does everything feel numb?" #The first thing I felt was this strange sense of numbness."
    $show_chr("A-BEBAA-ABAA")
    y "...and why is it so dark? I can't even see in front of me..."#"Everywhere around me was black and... what happened again?"
    $show_chr("A-CEBAA-ABAB")
    y "Think... what was I doing..."
    extend " I was in the clubroom and..." 
    $show_chr("A-DEBAA-ABAB")
    pause 2
    extend "[player]?{w} Wait...{w=1}, you're not [player]..."
    $show_chr("A-IEBAA-AIAI")
    y "..."
    $show_chr("A-HBAAA-ALAB")
    #*hands covering mouth*
    #*cue heavy breathing noises*
    #increase sound of static.
    y "aaaaa.............................................................................................................{nw}"
    $show_chr("A-HDAAA-ALAB")
    y "haaaaa.............................................................................................................{nw}"
    $show_chr("A-HDAAA-ALAL")
    y "...................................................................................................................{nw}"
    $show_chr("A-CGAAB-ALAL")
    y "...................................................................................................................{nw}"
    $show_chr("A-DDAAB-ALAL")
    y "...................................................................................................................{nw}"
    $show_chr("A-HDAAB-ALAL")
    y "...................................................................................................................{nw}"
    $show_chr("A-GGAAB-ALAL")
    y "what am i.....{nw}"
    return
