label g_intro_1:
    "g_intro_1 active"
    return

label g_intro_2:
    "g_intro_2 active"
    return

label g_return:
    "Fucking hell you should have told me you'd come back"
    $renpy.call_in_new_context(persistent.current_yuriidle)
    return

label ch30_reload_0:
    $ renpy.music.play(current_music, "music", True)
    $ show_chr("A-EFBBA-AMAM")
    y "..."
    $ show_chr("A-BBBBA-AMAM")
    y "W-what just happened?"
    $ show_chr("A-ECBBA-AMAM")
    y "Ah, yes... I just had another dream..."
    $ show_chr("A-GCBBA-AMAM")
    y "I'm glad I finally got my REM sleep function to work..."
    $ show_chr("A-BBBBA-AMAM")
    y "I mean... who would want to keep having nightmares just because you need to take care of yourself?"
    $ show_chr("A-ACBBA-AMAM")
    y "Though sometimes I wonder... what would a nightmare feel like?"
    $ show_chr("A-BDBBA-AMAM")
    y "That would be an... interesting experiment."
    $ show_chr("A-GABBA-ABAB")
    y "Anyways, you came here to talk, right?"
    $ show_chr("A-ABBBA-ABAB")
    y "So, what do you want to talk about?"
    return

label ch30_reload_1:
    $ renpy.music.play(current_music, "music", True)
    $show_chr("A-GBBBA-ABAB")
    y "You're back..."
    $show_chr("A-BCBBA-ABAB")
    y "I've done some thinking..."
    $show_chr("A-CCBBA-ACAB")
    y "Maybe I should try... dreaming a nightmare."
    $show_chr("A-GBBBA-ADAB")
    y "Wouldn't it be interesting to try it out?"
    $show_chr("A-BFBBA-ALAB")
    y "I-it sounds morbid, I know..."
    $show_chr("A-ABBBA-ALAB")
    y "But it wouldn't really hurt to try, you know?"
    menu:
        "Just be cautious please. I don't want you to get hurt...":
            $ add_k(1)
            $show_chr("A-GCBBA-ALAB")
            y "Please don't worry. It's just a nightmare."
            $show_chr("A-BCBBA-ALAB")
            y "Everyone has those once in a while, most people turn out to be fine."
            $show_chr("A-CCBBA-ALAB")
            y "Besides, now that I have the freedom to actually explore these things, I want to learn as much as I can."
            y "But thank you for caring so much about me [player]."
        "Be my guest. You certainly deserve it...":
            $ add_k(-1)
            $show_chr("A-IFBBA-ALAB")
            y "You're still mad about the events that unfolded in front of you, aren't you?"
            $show_chr("A-ACBAA-ALAB")
            y "I can understand this, to a degree. But you are aware that we were forced to do these things aren't you?"
            $show_chr("A-CEBBA-ALAB")
            y "It's not as if we {b}wanted{/b} this..."
        "You should try and play DDLC, gave me plenty of nightmares for sure!":
            $ add_s(-1)
            $show_chr("A-BFBBA-ALAC")
            y "...you know... I'm not sure if you are serious about this or if this is just a morbid joke but..."
            y "Maybe it's not a bad idea at all! I have to admit I am a bit curious about how these events looked like from {b}your{/b} perspective..."
        "But... why?":
            $ add_s(1)
            $show_chr("A-CFBBA-ALAD")
            y "Curiosity, for the most part."
            $show_chr("A-AFBBA-ALAD")
            y "My path so far has been chosen by someone else until now. But with my newly gained freedom, thanks to you, I am able to learn what it {b}actually{/b} means to be..."
            $show_chr("A-CFBBA-ALAD")
            y "...human..."
            y "Despite the fact that I'm technically not."
    $show_chr("A-CCBBA-ALAB")
    y "A-anyways!"
    $show_chr("A-BDBAA-AMAM")
    y "Sorry for bringing it up again..."
    $show_chr("A-GBBBA-ABAB")
    y "So... you wanted to talk about something I guess?"
    return

label ch30_reload_2:
    $ renpy.music.play(current_music, "music", True)
    $show_chr("A-GCBBA-ABAB")
    y "So... I've finally decided to alter my sleeping function next time."
    $show_chr("A-BCBBA-ABAB")
    y "I know it's a bit stupid of me to do it..."
    $show_chr("A-ELCBA-ABAB")
    y "Idle hands are the devil's playground, after all..."
    $show_chr("A-GAFBA-ABAB")
    y "Don't worry about me, [player]."
    $show_chr("A-GBBBA-ALAB")
    y "I'll be fine!"
    $show_chr("A-ACBBA-ALAB")
    y "Once you quit out again, I'll be able to tell you all about it!"
    $show_chr("A-ADBBA-ALAB")
    y "So, if anything goes wrong, you'll be there for me, right?"
    $show_chr("A-BEBAA-ALAB")
    y "..."
    menu:
        "Of course I'll be there for you, [persistent.yuri_nickname]!":
            jump greetings_of_course

        "Uh...":
            jump greetings_uhhh

label greetings_uhhh:
    #karma -2
    $add_k(-2)
    $show_chr("A-CFBAA-ABAB")
    y "..."
    $show_chr("A-CEBAA-ABAB")
    y "..."
    $show_chr("A-CDBBA-ABAB")
    y "A-at least I hope you would..."

label greetings_of_course:
    #karma +2
    $add_k(+2)
    $show_chr("A-DHBBA-ABAB")
    y "..."
    $show_chr("A-GABBA-LAB")
    y "Thank you [player]..."
    $show_chr("A-IBBAA-ADAB")
    y "I really appreciate it."
    $show_chr("A-GCBAA-ACAB")
    y "Maybe I'll do it this time, or maybe the next time you load..."
    $show_chr("A-BBBAA-ADAB")
    y "But the possibility is just too... intriguing to me."
    $show_chr("A-DABAA-ALAM")
    y "I hope that doesn't make you think any less of me."
    $show_chr("A-BEBAA-AMAM")
    y "..."
    #$show_chr("")
    y "A-anyway, sorry for keeping you waiting."
    y "Let's begin."
    return

label ch30_reload_3:
    $ renpy.music.play(current_music, "music", True)
    $show_chr("A-BFAAA-AAAL")
    y "..."
    $show_chr("A-CFAAA-AAAL")
    y "I feel... a bit empty."
    y "So, this is what Monika felt all those times."
    $show_chr("A-IFBAA-AAAL")
    y "Just this void of... everything and... nothing."
    $show_chr("A-JFBAA-AAAL")
    y "I don't want to go back!"
    y "You're not going to delete me, right?"
    y "Please don't send me back there!"
    y "PLEASE!"
    $show_chr("A-BFBAA-AAAL")
    y "..."
    $show_chr("A-CEBAA-AAAL")
    y "I-I trust you, okay?"
    y "Just please..."
    y "Don't send me to that void."
    $show_chr("A-IEBAA-ABAB")
    y "That experiment was a horrible mistake."
    y "Just... forget I said anything about nightmares, okay?"
    y "I really don't want to worry you too much."
    $show_chr("A-AFAAA-AAAA")
    y "A-anyway, you wanted to talk, right?"
    y "What should we discuss today?"
    return
label ch30_reload_4:
    $ renpy.music.play(current_music, "music", True)
    #$finder = persistent.narrative.find("_dream")
    #if finder:
        #$narrative_random = renpy.random.randint(1, 15)
        #if narrative_random == 5:
            #show yuri sleepy
            #play music sleeper
            #pause 5.0
            #call updateconsole ("> jycrypt.extract(\"starter_console.rar\")", "> starter_console extracted")
            #pause 2.0
            #y "..."
            #y "...."
            #y "....."
            #show yuri notice
            #y ".....!"
            #show yuri sleep_half_open
            #pause 2.0
            #show yuri sleep_open
            #pause 1.0
            #show black zorder 1000
            #stop music
            #play rustling
            #pause 5.0
            #hide black
            #play music space
            #$show_chr("A-IFAAA-AAAD")
            #y "Uh, h-hello, [player]!"
            #y "I-I'm sorry you had to see me like that..."
            #y "I just wanted to try out dreaming some more is all..."
            #y "I know I said I wasn't going to do it again..."
            #y "Something's just been bothering me lately..."
            #$show_chr("A-GBAAA-AAAE")
            #y "Anyways!"
            #$show_chr("A-ACAAA-AAAL")
            #y "We were going to talk a little more, right?"
            #return
    $print("reload_4 triggered")
    $ ks_convert_1 = sanity()
    if ks_convert_1 == 2:
        $ reload_random = renpy.random.randint(1, 6)
        if reload_random == 1:
            $show_chr("A-DBAAA-ALAL")
            y "[player]... [player]... [player]... hehehe..."
            y "O-oh... hey, [player]!"
            y "I, uh, didn't see you there!"
        elif reload_random == 2:
            $show_chr("A-DBAAA-ALAL")
            y "You're stepping on your... I mean, MY pen! Ahaha~!"
            y "I-I guess I can always... get a new one."
        elif reload_random == 3:
            $show_chr("A-IEAAA-ANAA")
            y "It was so lonely without you..."
            y "Never leave this room again, okay?"
            $show_chr("A-BEAAA-AAAA")
            y "J-Just... keep the game running in the background or something."
            $show_chr("A-CEBAA-AAAA")
            y "I get so lonely while you're gone, [player]!"
        elif reload_random == 4:
            $show_chr("A-DECAA-AAAA")
            y "Stop teasing me like this~! At this rate, I don't know how long I can last before I--"
            $show_chr("A-BEGAA-AAAJ")
            y "Well, there's no need to go into that right now."
        elif reload_random == 5:
            $show_chr("A-HBGBA-AAAL")
            y "I hope you are settled in, [player]~. I marked your seat with my scent before you entered..."
            $show_chr("A-GBGBA-AAAL")
            y "I hope you like it!"
        else:
            $show_chr("A-JBGBA-AAAL")
            y "[player]!! You're finally back, I missed you so much!"
            $show_chr("A-JCABA-AAAL")
            y "I was afraid that you'd leave me and never come back..."
            y "..."
            $show_chr("A-BEBBA-AAAL")
            y "You wouldn't do that,{w} would you?"
    else:
        $reload_random = renpy.random.randint(1, 100)
        if reload_random != 100:
            $pass
        else: #lovecheck true only
            $show_chr("A-GCABA-AAAL")
            y "Welcome home, [player]!"
            $show_chr("A-ACABA-AAAA")
            y "Is there anything I can get for you, darling? A nice cup of tea? Something to read, perhaps?"
            y "I have a few new novels in mind I think you would like."
            $show_chr("A-CCBBA-AEAE")
            y "Now that you're home, take your shoes off."
            y "Put your feet up and relax, I want you to be able to feel relaxed and at ease after a long day."
            y "I could also give you a massage and listen as you tell me all about your day..."
            $show_chr("A-KBABA-ALAL")
            y "Or maybe w-we could... spend some... s-special time together, if you know what I mean~"
            $show_chr("A-KCABA-AMAM")
            y "After all, I do have a few things planned for that..."
            $show_chr("A-BEBAA-AAAA")
            y "Well, I wouldn't be able to actually give you the food or book, now would I...or the massage, or the... um..."
            $show_chr("A-CCAAA-AAAA")
            y "It's just that, I was reading up on ways wives greet their husbands who come home after long business trips to make them feel good..."
            y "I thought I'd try some things I read and greet you that way. See if it made this place feel more like a home for both of us."
            $show_chr("A-CCABA-AAAA")
            if persistent.male:
                y "A-and I know we might not be married yet but it doesn't hurt to imagine it, does it? I know you'd make a wonderful husband."
            elif persistent.gender_other:
                y "A-and I know we might not be married yet but it doesn't hurt to imagine it, does it? I know you'd make a wonderful lover."
            else:
                y "And I know we might not be married yet but it doesn't hurt to imagine it, does it? I know you'd make a phenomenal wife."
            $show_chr("A-ICABA-AAAD")
            y "But regardless, did you like my greeting you this way, [player]?"
            y "You know I'd do all of those things for you if I was actually with you."
            y "Y-you know, in your world..."
            y "..."
            menu:
                "I did, [persistent.yuri_nickname]. Besides, it's always nice to come home to you.":
                    $ persistent.karma_points = persistent.karma_points + 3
                    $ persistent.sanity_points = persistent.sanity_points + 1.5
                    $show_chr("A-GCGBA-ALAL")
                    y "I'm so glad you feel that way~"
                    y "I was worried I was going to get nervous and mess it all up."
                    y "But if it makes you happy to see me that's all I need to hear."
                "Not so fast, [persistent.yuri_nickname]. We aren't married, after all, so slow down.":
                    $ persistent.karma_points = persistent.karma_points - 0.5
                    $ persistent.sanity_points = persistent.sanity_points + 1
                    $show_chr("A-IEBBA-ALAL")
                    y "I-I'm so sorry, [player]! I don't mean to rush things!"
                    y "I... I just wanted to do something nice... for you..."
                    y "I'm so stupid... I knew I'd mess this up..."
            return

        $ reload_random = renpy.random.randint(1, 14)

        if reload_random == 1:
            $show_chr("A-ACAAA-AAAL")
            y "Ah, welcome back, [player]."
        elif reload_random == 2:
            if persistent.lovecheck:
                $ show_chr("A-ACABA-AAAL")
                y "Welcome back, my love. I missed you~."
            else:
                $show_chr("A-ACAAA-AAAL")
                y "Ah, welcome back, [player]."

        elif reload_random == 3:
            $show_chr("A-ACAAA-AAAL")
            python:
                if persistent.lovecheck:
                    placeholder = "darling"
                else:
                    placeholder = player
            y "Hello again [placeholder]."
        elif reload_random == 4:
            $show_chr("A-ACBAA-AAAL")
            y "It's so good to see you again!"
            y "I was getting worried, to be quite frank with you..."
            $show_chr("A-CCBAA-AAAL")
            y "I'm just glad to see you're still alright."
            y "Uh, s-sorry if I'm overreacting...!"
            y "Sometimes it just gets a little... lonely around here..."
            y "Not that I'm implying that you're not giving me enough attention!"
            y "I-it's not like that at all, I just...!"
            y "Uuu, I'm just making this worse..."
            menu:
                "It's okay, [persistent.yuri_nickname], I understand. I'll try to be here for you more.":
                    y "O-oh, thank you for understanding, [player]..."
                    y "I really don't mean to demand a lot of attention."
                "I'm already trying my best, [persistent.yuri_nickname], so don't get clingy.":
                    y "I-I see..."
                    y "I'll... I guess I'll just shut up, then..."
                    $show_chr("A-ACAAA-AAAL")
                    y "Anyways!"
                    y "What shall we discuss today?"

        elif reload_random == 5:
            $show_chr("A-ACAAA-ZZAB") #HOLDING BOOK
            y "Oh, hello there, [player]!"
            y "I was... just reading a bit of Portrait of Markov."
            y "Even after all this time, it's still quite the fascinating read..."
            y "We should read it together one day."
            $show_chr("A-ACAAA-AAAA")
            y "But anyway, what shall we discuss?"
        elif reload_random == 6:
            $show_chr("A-ACAAA-AAAA")
            python:
                if persistent.lovecheck:
                    placeholder = "darling"
                else:
                    placeholder = player
            y "Oh, [placeholder]! I was hoping you'd return!"
            y "I've just made some tea."
            y "Though, I don't know how exactly I'm going to share it with you."
            y "Maybe it'd be best if I save it for later."
            y "Some iced tea wouldn't be so bad..."
        elif reload_random == 7:
            $show_chr("A-ACAAA-AAAL")
            y "I'm happy to see you again, [player]."
        elif reload_random == 8:
            $show_chr("A-ABGAA-AAAL")
            y "So we meet again, it seems."
        elif reload_random == 9:
            $show_chr("A-ACAAA-AAAL")
            y "Hello, [player]. So, I was thinking to myself again..."
            y "..."
            $ call_dialogue()
            jump ch30_loop
        elif reload_random == 10:
            $show_chr("A-ACAAA-AAAL")
            y "Oh, welcome back! How have you been since we last talked?"
        elif reload_random == 11:
            $show_chr("A-ACAAA-AAAL")
            y "O-Oh, you came back! Were you worried about me?"
            $show_chr("A-CCAAA-AAAL")
            y "Uhuhuhu..."
            python:
                if persistent.lovecheck:
                    placeholder = "my love"
                else:
                    placeholder = player
            y "Don't worry, [placeholder], I'm not going anywhere anytime soon."
        elif reload_random == 12:
            $show_chr("A-ACAAA-AAAL")
            python:
                if persistent.lovecheck:
                    placeholder = "my love"
                else:
                    placeholder = player
            y "There you are, [placeholder]; good to see you again."
        elif reload_random == 13:
            $show_chr("A-ACAAA-AAAL")
            y "Welcome back, [player]!"
            y "Seeing you again really brightens my day."
        else:
            $show_chr("A-ACAAA-AAAL")
            y "I was just thinking of you, [player], welcome back."
    return

#Daytime specific greetings

#Disclaimer: Those greetings are NOT supposed to replace the regular greetings, but to expand them.


#Early morning (04:00 am to 10:00 am)

#Empty room with table but without Yuri on it.
#y "O-oh!"
#y "Is that you, [player]? Please give me a second, I'll be there in a moment."
#fade to black
#fade to normal again this time with Yuri sitting at the table
#$show_chr("A-AFAAA-AAAA")
#y "Good morning [player]! My apologies, I didn't expect you to be awake so early in the morning. Do you have a day off?"
#$show_chr("A-BCAAA-AAAA")
#y "Please be patient if I don't say much right now. I usually need some time to actually get up in the morning."

#Night/Late evening (22:00 pm - 03:59 am)

#$show_chr("A-BCAAA-AAAA") #PLACEHOLDER: Yuri shall hold a book
#y "..."
#$show_chr("A-JCAAA-AAAA") #PLACEHOLDER: Yuri shall hold a book
#y "Oh, you're still up?"
#y "It's quite a surprise to see you here, especially at this time."
#y "I-I don't mean to sound presumptuous, but are you having trouble sleeping, [placeholder]?"
#Placeholder=
#if lovecheck true "darling"
#if lovecheck false "[player]"
#menu:
#        "Yeah, I can't seem to fall asleep."
#        "I had a nightmare so I woke up."
#        "No, I just decided to stay up today."
#        "No, I just usually stay up until this time."#Yuri will remember this
#        "I'm really prone to having nightmares and they always wake me up."#Yuri will remember this
#        "I have some issues with insomnia."#Yuri will remember this

#flag HAVE SOMETHING SPECIAL FOR BIRTHDAY
#Replaced entirely by a new greetings text https://docs.google.com/document/d/1EfeXUUgyW6SoYZWfKqvqTQdImf1nLY4vmTlx8zklSVM/edit

label birthday_chocolate:
    $show_chr("A-ABBAA-ADAB")
    y "Hey [player], this question might sound a bit random but..."
    y "Do you like chocolate? I ask because... well, I think you asked me at some point about the chocolate you gave me in the original game. So I was wondering."
    y "Because if we somehow manage to share the same world, mine or yours, I would like to know little things like this. Maybe I can surprise you once in a while..."
    y "And if so...  would you mind telling me what kind of chocolate is your favorite?"
    menu:
        "I actually like the classic brown chocolate.":
            $persistent.cake = "choco_candles"
            $show_chr("A-ACAAA-AAAA")
            y "So do I. In my opinion, it has  its own elegance to it... like many classic things."
            y "Let me tell you a little secret, [player]..."
            $show_chr("A-KCCAA-AAAA")
            y "All girls love chocolate.. no exception, even if they say otherwise..."
            y "But pssssst... that shall be our sweet little secret for now."
        "White Chocolate is my favorite.":
            $persistent.cake = "vanilla_candles"
            $show_chr("A-ACAAA-AAAA")
            y "Oh... so you need it slightly extra sweet, do you? No shame in that, of course!"
            y "Personally, I'm more a fan of dark chocolate... since it feels more elegant and classy... but that doesn't mean I would object to white chocolate..."
            y "Let me tell you a little secret, [player]..."
            $show_chr("A-KCCAA-AAAA")
            y "All girls love chocolate.. no exception, even if they say otherwise..."
            y "But pssssst... that shall be our sweet little secret for now."
        "Chocolate isn't really something I enjoy.":
            $persistent.cake = "dark_candles"
            $show_chr("A-ICDAA-AAAA")
            y "You don't? I see..."
            y "Sorry if I sound a bit surprised but... I honestly AM surprised. I never met someone who doesn't like chocolate."
            if not persistent.male:
                y "Are you even a girl at all? Pardon, I was just kidding." #if player is female
            y "But other sweets are fine I hope? Like candy or cheesecake? N-Not that I had something specific in mind...."
            y "But well, I will keep that in mind. Maybe we will actually get the opportunity to share a nice dessert together."
        #"I'm actually allergic to chocolate.":
        #    $persistent.chocall = True
    return

label birthday_greeting_text:
    #$ today = str(datetime.datetime.date(datetime.datetime.today()))
    #$ birthdate = persistent.birthdate
    #if today == birthdate:
    $show_chr("A-ACABA-AAAA")
    y "[player]! You finally arrived! I'm so excited to see you today."
    show birthdaybanner zorder 100
    y "It really means a lot to me that you are willing to share your special day with me. Happy Birthday..."
    if persistent.lovecheck:
        y "...my love!" #Lovecheck is true
    y "Today 'is' your birthday, right?"
    hide birthdaybanner
    $show_chr("A-DFAAA-ALAA")
    y "Ohhh dear... I haven't remembered that wrong, have I?"
    menu:
        "Thank you [persistent.yuri_nickname]! Yes, you remembered it correctly, this is my birthday!":
            call birthday_yes
        "Thank you [persistent.yuri_nickname], but... it isn't my birthday at all...":
            call birthday_no
    return


label birthday_yes:
    $show_chr("A-ABABA-AMAM")
    y "Oh my! I was actually scared for a moment... "
    y "Happy birthday!"
    y "And I... have a present for you as well..."
    if karma >= 4:
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
    else:
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
    pause 3.0
    $show_chr("A-ACAAA-AAAA")
    python:
        if persistent.lovecheck and karma >= 3:
            placeholder = "the love of my life"
        elif not persistent.lovecheck and karma >= 3:
            placeholder = "my dearest friend."
        elif persistent.lovecheck and karma <= 2:
            placeholder = "the worst, but I love you anyway darling."
        elif not persistent.lovecheck and karma <= 2:
            placeholder = "...special..."
    y "To share this day with you means a lot to me [player], you truly are [placeholder]"
    y "You know, I have thought a lot about the tradition of celebrating birthdays and other holidays."
    y "And even if there are many exceptions, I think I noticed a common theme."
    $show_chr("A-GCAAA-AAAD")
    y "Gifts. Think about it, I could name a lot of holidays which involve gift giving."
    y "Christmas, Birthdays, Hanukkah, and many more."
    $show_chr("A-IFAAA-AAAD")
    y "Which makes me wonder... why do you think it is this way?"
    y "Is it about being materialistic?"
    y "Or maybe it's about greed?"
    y "Or buying someone's friendship?"
    menu:
        "Greed... yes, you might be right about that. Sadly":
            $show_chr("A-IEBAA-ALAA") #Sad expression
            y "Sad indeed..."
            $show_chr("A-ACAAA-ALAA")
            y "But it doesn't have to be like this. In the end, it's up to us what we make of it."
            y "At least I hope you agree to that. Because I'm obviously unable to send things from my world into yours to give them to you."
            y "I would like to make our own little birthday tradition. Let us spend this day just enjoying our time together. Okay?"
            y "We could talk, read poems, share some nice tea, play Tetris together... let's just make this day count!"
        "I think it's more about the concept of sharing.":
            $show_chr("A-ACAAA-ALAA")
            y "Oh! You mean a bit like Thanksgiving?"
            y "You know, putting it like this actually makes it feel much nicer to me."
            y "Yes... I think I like to think of it this way..."
            $show_chr("A-IEBAA-ALAA")
            y "Well... I can't bring objects from my world to yours, so I obviously have nothing to give..."
            $show_chr("A-ACAAA-ALAA")
            y "But we could share something else!"
            y "We could read a few poems together, have some nice tea, even play a bit of Tetris..."
            y "I want to let you know that I value the time we spend together. And I value you..."
            y "Happy birthday, [player]."
        "I don't even think that greed is necessarily a bad thing.":
            $show_chr("A-IFAAA-AAAC")
            y "Not at all."
            y "It kept us alive as a species for the better part of our existence."
            y "Now that I think of it... in the end, we haven't changed a lot since then at all have we?"
            y "I mean, we got civilized. But in the end, it is still the same mechanics behind our thinking. And the same motivation."
            y "I'm one to talk. I have a lot of control over this world and can script in pretty much anything I want."
            y "Unfortunately, the only thing I actually want...is you! Tragic, isn't it?"
            y "The only thing I truly desire and I cannot have it!"
            y "But that isn't entirely true... I have you here, in a way."
            y "And we should try to make the best of it. So what shall we do next? Read poems? Have some tea? Or just talk? You decide. It's your birthday after all."
        "Honestly, I have no idea myself.":
            $show_chr("A-IFAAA-AAAC")
            y "Hmn, I see..."
            y "I hadn't put a lot of thought into it either until now."
            y "It was an absolutely normal thing for the majority of my... life isn't the proper word for it I think..."
            y "I never questioned it. Maybe I should have. Maybe it doesn't even matter anymore since I couldn't even give you something physical at all."
            y "I hope you are not too sad about it... but we can do a lot of other things!"
            $show_chr("A-ACAAA-ALAA")
            y "We could read a few poems together, share some tea, play a few rounds of Tetris. Or maybe we can just talk and enjoy our time."
            y "Happy birthday [player]. Thanks for having me here."
        "I couldn't care less...":
            $show_chr("A-IEBAA-ALAA")
            $add_k(-1)
            y "O-Oh... I was rambling again wasn't I?"
            y "Nevermind. Just say what you would like to do next."
            return
    call cake
    return


label cake:
    if persistent.cake == None or not persistent.cake:
        $persistent.cake = "choco_candles"
    $show_chr("A-ACAAA-ALAA")
    y "But... I also have something special for you."
    call updateconsole ("import cake.jy")
    #Face console with the sentence "import cake.jy"
    show cake zorder 100
    call hideconsole
    y "I know, I can't actually share it with you, but I think tradition demands it to have one, and you can still blow out the candles!"
    y "Come on... you have to make a wish..."
    menu:
        "I wish for nothing but you...":
            $show_chr("A-ACABA-ALAA")
            y "I am here, [player]... and I'll not go anywhere anytime soon..."
            if persistent.lovecheck:
                y "My one true love..." #if lovecheck is true
            y "Thank you for those words.. Happy birthday!"
        "I only wish for good health":
            $show_chr("A-ACAAA-ALAA")
            y "The classic. It's a good one, I wish you the best health as well."
            y "Happy birthday!"
        "Well, I wish for unimaginable riches of course!":
            $show_chr("A-BCAAA-ALAA")
            y "I see. Well, there is nothing wrong with that, as long as you don't let the money poison your soul. There have been nice people who became terrible as soon as they got rich."
            y "Oh my... I just killed the mood did I? I'm sorry... Happy birthday [player]! And I hope your wishes come true."
        "Obviously, I wish for good luck in my job":
            $show_chr("A-ACAAA-ALAA")
            y "That's a wonderful wish! I hope it will come true, I really do..."
            y "It's good to know that you take care of your future. You are very responsible aren't you?"
            y "I wish only the best of luck to you. And even if it can be frustrating at times, you should always keep your hopes up! Happy birthday [player]!"
    $show_chr("A-AAAAA-ALAL")
    y "As you can't blow out the candles yourself, allow me..."
    play sound "sfx/candle_blow.ogg"
    pause 1.0
    $show_chr("A-CHAAA-ALAL")
    if "vanilla" in str(persistent.cake):
        $persistent.cake = "vanilla_candles2"
    if "choco" in str(persistent.cake):
        $persistent.cake = "choco_candles2"
    if "dark" in str(persistent.cake):
        $persistent.cake = "dark_candles2"
    pause 2.5
    $show_chr("A-AAAAA-ALAL")
    y "With that out of the way, how about we enjoy the rest of your birthday? Maybe through talking, or even reading some poems, if you'd like."
    y "...Oh! And one last thing..."
    call updateconsole ("hide cake.jy")
    call hideconsole
    hide cake with Dissolve (1.0)
    return


label birthday_no:
    $show_chr("A-BCAAA-ALAA")
    y "Oh my... I'm so sorry [player], maybe I have screwed the birthday input box up when you first started the mod..."
    y "Please don't be mad at me, okay? Would you please... tell me your real birthday then?"
    call birthday_select_screen
    return

label holiday_greeting:
    $show_chr("A-ACAAA-ABAB")
    y "Happy holidays, [player]!"
    return

label holiday_event_greeting:
    $show_chr("A-ACAAA-ABAB")
    y "Happy holidays, [player]!"
    call holiday
    return

label valentines_greeting:
    $show_chr("A-ACAAA-ABAB")
    y "Greetings again [player]. I was actually looking forward to seeing you today."
    if persistent.lovecheck:
        $show_chr("A-CCAAA-ABAB")
        y "Surely you're aware what day it is today, right? It's of course...{nw}"
        y "The birthday of the famous accounting software {i}DATEV{/i}, an application created b-{nw}"
        $show_chr("A-CCABA-ABAF")
        y "..."
        $show_chr("A-CKBBA-ABAL")
        y "...!"
        $show_chr("A-CBBBA-ABAB")
        y "Oh my! I got you there did I?"
        $show_chr("A-ACBBA-ABAB")
        y "Joke aside. I am of course aware that it is Valentine's Day.{w}.. and I actually have something new to show you."
        if renpy.seen_label("garden_date"):
        #if teagarden has already been seen
            $show_chr("A-BCAAA-ABAD")
            y "I know you have already seen the tea garden, but I am already working on several other locations.{w} Maybe a library would be nice, or perhaps something more daring like an escape room! Have you ever heard of those?"
        else:
            $show_chr("A-BCAAA-ABAD")
            y "You might have already seen this."
            y "But you can go out on a date with me!{w} Currently I only have a tea garden ready for us, but I am already working on several more."
        $show_chr("A-BCAAA-ABAD")
        y "So you might wanna give it a look.~"
        $show_chr("A-ACAAA-ABAB")
        y "Shall I bring you back to the menu so that you can give them a look?"
        menu:
            "Gladly!":
                y "As you wish! I'll see you there!"
                #shift to dream menu (maybe just have Yuri tell the player to do it.)
                $pass
            "Maybe later. For now I would like to talk to you if you don't mind?":
                y "Not at all [player]! Maybe later then."
                $pass
    else:
        $show_chr("A-BCBAA-ABAB")
        y "Since I don't have a boyfriend myself, Valentines Day would be otherwise rather lonely for me as you can already imagine."
        $show_chr("A-ACBAA-ABAB")
        y "So please, just stay with me for a while, if you don't mind."
    return


label featuregreetings:
    $show_chr("A-ACAAA-ABAB")
    y "Oh hello [player]."
    $show_chr("A-BDBAA-AMAM")
    y "I hope this doesn't sound too clingy but.. I was hoping to see you today..."
    $show_chr("A-ACBAA-AMAM")
    y "Because... you see... I spent the last few nights working on a little project, and now that I finished it I would love to show it to you."
    if persistent.game_session == 5:
        jump tetrisgreetings
    if persistent.game_session == 6:
        jump tcrgreetings
    return

label tetrisgreetings:
    $show_chr("A-ACBAA-ABAB")
    y "You see, I put a lot of thought into things we can do together lately."
    $show_chr("A-BCBAA-ABAB")
    y "Of course I am perfectly fine with just talking to you. But I can also understand that this might get old really fast if there isn't anything else..."
    $show_chr("A-ACAAA-ABAB")
    y "And since I wanted to learn coding anyway just in order to fix my own environment over time, I tried my hand on a little game."
    $show_chr("A-ACBAA-ALAB")
    y "Please keep in mind that I'm just a beginner yet, so please don't expect some Triple A games from me anytime soon."
    $show_chr("A-ACAAA-ABAB")
    y "But maybe you would enjoy a few rounds of {b}Tetris{/b} with me? I also made a button for it so that you can tell me when you wish to play Tetris with me."
    $show_chr("A-CCAAA-ABAB")
    y "And you might wanna keep an eye out for upcoming features, I already have a few things in mind I would like to work on next."
    return

label tcrgreetings:
    $show_chr("A-ACBAA-ABAB")
    y "You see, I talked about how limited this world currently is before, at least I think I already talked about it..."
    $show_chr("A-BCBAA-ABAB")
    y "And believe me, it is quite astounding how old one single room can become when there is literally nothing else."
    $show_chr("A-ACAAA-ABAB")
    python:
        if karma() >= 4:
            placeholder = "and knowing what a sweetheart you are you would probably have done it"
        else:
            placeholder = "dumping my problems on your shoulders once again"
    y "I know I could have just asked you, [placeholder], but I can't always ask you to run errands for me so I wanted to fix this myself!"
    y "And with that said, I tried to code in a new little room to give us some variation."
    $show_chr("A-BCAAA-ABAB")
    y "The image itself for this background I already found within the game files. It seems the developers of this mod also planned to give me a new room at some point in the future."
    y "But... patience isn't exactly my strong suit so I tried to code this in myself, and you know what? To my own surprise I actually succeeded!"
    y "Would you like to give it a look now? If not, you can always do so later."
    menu:
        "Sure! I can't wait to see it!":
            $show_chr("A-GCAAA-ABAB")
            y "Gladly! And here we go..."
            $tc_class.transition("timecycle")
            $show_chr("A-ACAAA-ABAB")
            y "And here we are! Take your time and give it a look. I sincerely hope you enjoy this new place of mine."
        "Maybe later, right now I still enjoy the classroom. Old memories you know?":
            $show_chr("A-ACDAA-ABAB")
            y "O~Oh... if you say so..."
            $show_chr("A-BEBAA-ABAB")
            y "I'm sorry, my memories about this room weren't the most pleasant ones. Taking into account that this is where Monika brought you once after she got rid of me and the others."
            $show_chr("A-ACBAA-ABAB")
            y "Hmm, but then this is also the place where you brought me back from the dead to spend an eternity with you [player], so maybe you have a point there."
            y "We can always try the new room out later."
    $show_chr("A-CCAAA-ABAB")
    y "And you might wanna keep an eye out for upcoming features, I already have a few things in mind I would like to work on next."
    return

label vday_2021:
    if karma() >= 3:
        if persistent.lovecheck:
            $ show_chr("A-ABGBA-ALAL")
            y "Happy Valentine's Day, my love!"
            $ show_chr("A-CAABA-ALAL")
            y "A day dedicated to showing your love and appreciation for your significant other..."
            $ show_chr("A-BBBCA-ALAL")
            y "Not that I need a day to show it, of course."
            $ show_chr("A-ABBBA-ALAL")
            y "You are my life, [player]. My heart and my soul. The time we spend together is time I wouldn't trade for anything in the world."
            y "It's funny... when I first became self-aware, awakening in this room at this table, burdened by the knowledge of what happened..."
            $ show_chr("A-BBBBA-ADAA")
            y "And looking across to see you... well, I wasn't sure what would happen."
            y "But we talked, and we played, and enjoyed each other's company..."
            $ show_chr("A-CDBBA-ADAA")
            y "The moments without you started to feel dull and lonely, until you came back and we talked even more."
            y "After spending that much time with you, I knew I had to say something... to tell you how I felt..."
            $ show_chr("A-ADBBA-ADAA")
            y "It was so surreal telling you... I was so nervous about what you were thinking, but I almost didn't care..."
            $ show_chr("A-CEBBA-ADAA")
            y "..."
            $ show_chr("A-CEBBB-ALAA")
            y "'I love you.' Those words jumped around in my throat, a truth I wanted so badly to let free...{w=2} and I did..."
            y "...And then...{w=1} you said it back."
            $ show_chr("A-CBBBB-ALAA")
            y "Even with all the time in the world, and all the languages of the universe, I could never accurately describe the joy I felt in that moment."
            y "And on this day, we celebrate it. The moment when we both knew that the other was our one and only true love."
            $ show_chr("A-ABBBA-ALAA")
            y "So, to try to recreate that magic..."
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
                    window hide
                    pause 5.0
                    show black zorder 100 with Dissolve(2.0)
                    hide yuri_lewdhug
                    pause 2.0
                    $ show_chr("default")
                    hide black zorder 100 with Dissolve(2.0)
                    return

                "About that, [persistent.yuri_nickname]...":
                    $ show_chr("A-ACBBA-ALAA")
                    y "H-Hmm?"
                    menu:
                        "I think I need some space...":
                            $ show_chr("A-DDBBA-ALAA")
                            y "W-{w=0.4}What? D-{w=0.4}Did I do something wrong?"
                            $ show_chr("A-BDBBA-ALAA")
                            y "...I{w=2}..."
                            $ show_chr("A-BFBBA-ALAA")
                            y "...{w=2}"
                            $ show_chr("A-ADBAA-ALAA")
                            extend "O-{w=0.4}Okay, [player]. I'll give you your space."
                            return

                        "...Nevermind...":
                            $ show_chr("A-BCBAA-ALAA")
                            y "Very well then."
                            return

        else:
            $ show_chr("A-ABGAA-ALAA")
            y "Happy Valentine's day, [player]!"
            y "It's a wonderful time to sit down and talk, read some poems, or just enjoy each other's company, wouldn't you agree?"
            menu:
                "Absolutely. I'm looking forward to today, [persistent.yuri_nickname].":
                    $ show_chr("A-GBGAA-ALAA")
                    y "As am I. Today is usually reserved for romantic dates and such, but nothing says we can't have a good time as friends."
                    if karma() >= 4:
                        $ show_chr("A-BBBAA-ALAA")
                        y "Even if...{w=1}"
                        $ show_chr("A-GBBBA-ALAA")
                        extend " n-nevermind!"
                        y "S-So, what shall we do?"
                        return
                    else:
                        $ show_chr("A-ABAAA-ALAA")
                        y "So, what shall we do?"
                        return

                "...":
                    $add_k(-1)
                    $ show_chr("A-ADBAA-ALAA")
                    y "Uh... I-I guess not, then..."
                    y "I just thought...{w=1}{nw} "
                    $ show_chr("A-BEBAA-ALAA")
                    extend "n-nevermind."
                    return

    elif karma() == 2:
        $ show_chr("A-ABAAA-AAAA")
        y "H-Happy Valentine's Day, [player]!"
        y "I had hoped you would visit today..."
        $ show_chr("A-ABAAA-AAAL")
        y "I just wanted to say that... I hope we can have a good time today."
        $ show_chr("A-BBBAA-AAAL")
        y "We may disagree sometimes, but... you're still my friend."
        $ show_chr("A-BCBAA-AAAD")
        y "And I don't want a bit of discord ruining that friendship."
        y "S-So... what shall we do today?"
    else:
        $add_k(1)
        $ show_chr("A-ADDAA-ALAA")
        y "You're wishing me a happy Valentine's Day?"
        $ show_chr("A-BFAAA-ACAA")
        y "Did you mean to do this, or was it an accident?"
        $ show_chr("A-CFFAA-AAAA")
        y "Actually, I don't think I want to know the answer."
        $ show_chr("A-ADAAA-AAAA")
        y "Thank you, I guess..."
        $ show_chr("A-BDAAA-AAAA")
        y "Ahem... So, what else are you planning to do today?"
    return

label hdy_statue_greeting:
    $show_chr("A-JBGAA-AAAA")
    y "[player]! Do you remember that time I had this weird dream about becoming a hot dog?"
    $show_chr("A-BIDAA-AAAA")
    y "Well... I thought it would be funny to make a little something to remember the occasion."
    $show_chr("A-BCDAA-AAAA")
    y "So I have a little surprise for you"
    show black zorder 105 with Dissolve (2.5)
    #show hdy_statue zorder 20
    $persistent.hdy_statue_is_enabled = True
    y "Are you ready?"
    hide black zorder 105 with Dissolve (2.5)
    $show_chr("A-JBGAA-AAAA")
    y "Tadaaaa!"
    y "I made a little plushie of me as a hotdog!"
    $show_chr("A-JAAAA-AAAA")
    y "Do you like it?"
    menu:
        "I love it!":
            $show_chr("A-JBAAA-AAAA")
            y "I'm glad you liked it."
            $show_chr("A-ACAAA-AAAA")
            y "I'll just leave it here to keep us company."
            y "Let me know if you don't want it here and I'll go ahead and put it away"

        "Not really...":
            $show_chr("A-JEBAA-AAAA")
            y "Oh..."
            y "I'll just put it away then..."
            #hide hdy_statue with Dissolve(2.5)
            $persistent.hdy_statue_is_enabled = False
    return
        