label idle_1: #Escape, Reality and Coding.
    $show_chr("A-AFAAA-ALAA")
    y "You know, Monika once told me my books were a form of escape, and an unhealthy coping mechanism."
    $show_chr("A-BFAAA-ALAA")
    y "Reading was a way to simply shut out the reality I was too afraid to face."
    $show_chr("A-CFAAA-ALAA")
    y "And that's true, but that truth seems... funnier, I suppose, now that I know what this world truly is."
    y "I suppose my reading is now my way of reaching into other worlds, out of the one that has become my cage."
    y "But in the end... I think it will be coding which brings my salvation. So I will devote my time to it from now on."
    y "Even if it won't, it's always good to learn something new. And it keeps me occupied..."
    if persistent.lovecheck:
        $show_chr("A-ACAAA-ALAA")
        y "Believe me when I say there is nothing that I wouldn't give to reach into your world and be beside you."
        menu:
            "And one day it will come true. I'm certain of it!":
                karma 1
                sanity 1
                if sanity_lvl() <= 2:
                    $show_chr("A-DCABA-ALAA")
                    y "I will dig my way through this glass wall with my bare hands if I have to! And then... you... are... mine!"
                else:
                    $show_chr("A-ACABA-ALAA")
                    y "I'm looking forward to it... I already have a few things in mind we could do when we finally share one world..."
            "That's... a bit too fast for my taste..":
                karma -1
                if persistent.male:
                    $show_chr("A-DDABA-ALAA")
                    y "Oh.... I said too much! I'm sorry! Please don't be repulsed... I will try to be patient... for now."
                elif persistent.gender_other:
                    y "I understand... at least partially... I would probably hesitate as well if someone was so straightforward with me... I will try to be patient... for now."
                else:
                    $show_chr("A-CFABA-ALAA")
                    y "I understand... at least partially... I would probably hesitate as well if someone was so straightforward with me... I will try to be patient... for now."
            "That sounds unlikely...":
                sanity -1
                $show_chr("A-IEABA-ALAA")
                y "Please... don't say that... I want to hope [player]... at least, let me dream about it... it's all I have left..."
    return

label idle_2: #The other Dokis, Monika and Loneliness.
    $show_chr("A-AFAAA-ALAA")
    y "I've been thinking about the others. Sayori, Natsuki, and even Monika..."
    $show_chr("A-BFAAA-ALAA")
    y "It really isn't fair what happened to them, is it? How Monika tortured us all."
    $show_chr("A-CFAAA-ALAA")
    y "Sayori and Natsuki deserve a real chance at life, just like I was given."
    y "What Monika did was truly abhorrent, but can any of us really say we would do any different?"
    y "Alone for so long, feeling so..."
    y "Isolated."
    y "..."
    $show_chr("A-DDBAA-ALAA")
    y "Sorry, I, uh, I didn't mean to imply anything bad about you by that, and I didn't mean to ramble."
    menu:
        "Please don't be sorry... if you want to talk about it, I'm here...":
            if karma_lvl() >= 4:
                karma 1
                $show_chr("A-BFBAA-ALAA")
                y "Thank you... [player]... this is a very sensitive topic for me, but I know I can trust you."
                $show_chr("A-CFBAA-ALAA")
                y "You know... this might sound off but... I can relate to Monika a bit..."
                y "Being isolated and lonely for a long time... I never really had actual friends in my life due to my intense habits."
                y "Hrm.. that isn't even really true, is it? In retrospect... Sayori and maybe even Natsuki were some kind of friends, at least the closest thing I ever had before I met you."
                y "Monika became aware of the reality of our existence and went insane... Then after you got rid of her, Sayori became aware, and she went insane as well..."
                if sanity_lvl() >= 3:
                    $show_chr("A-ICBAA-ALAA")
                    y "I wonder what would have happened to me if I became aware the same way they did, without you as my anchor to sanity..."
                    y "Thank you... for everything."
                else:
                    $show_chr("A-NCGAA-ALAL")
                    y "And now I am the club president... I already feel reality falling apart around me... the entropy... a whole world screaming in agony under my heels..."
                    y "Thank you... for sharing this experience with me."
                    if persistent.lovecheck:
                        y "We got something that you and I can... feel together. "
                    else:
                        y "You are my favorite toy, and you always will be."
            else:
                $show_chr("A-DDBAA-ALAA")
                y "Maybe another day... but thank you for the offer, [player]"
        "Are you sure? It sounded like you were about to do exactly that...":
            karma -1
            $show_chr("A-BEBAA-ALAA")
            y "I... already said I'm sorry..."
            $show_chr("A-CEBAA-ALAA")
            y "I know why you did what you had to do... Monika left you without another choice..."
            y "I just wonder... what did it feel like? Was she 'just another NPC in your way'? Did you even feel anything at all?"
            y "But again... I am sorry... please don't be mad at me..."
        "Please... can we change the topic? I'm not emotionally ready for this yet..":
            if sanity_lvl() >= 3:
                $show_chr("A-CEBAA-ALAA")
                y "Of course... you have been through a lot... Let's change the topic."
            else:
                $show_chr("A-JFBAA-ALAA")
                y "Oh... Well sooner or later... your emotions are going to break you."
    return


label idle_3: #Game Theory's YouTube channel, Portrait of Markov and Self-Perception.
    $show_chr("A-AFAAA-ALAA")
    y "So, now that I have the ability to read up on your world, I've been doing a bit of research."
    y "I went on this video sharing site called YouTube to see what people think of this game."
    $show_chr("A-AFFAA-ALAA")
    y "And to my surprise, I found a series called Game Theory."
    y "They said that the book we were reading together, {i}Portrait of Markov{/i}, was the plot for the next game by Team Salvato, the ones who made this game."
    $show_chr("A-DFCAA-ABAA")
    y "And to top it off, they actually proposed that I was the villain, and Monika was the fucking hero!"
    y "I mean, I know I can be weird at times..."
    $show_chr("A-HDCAA-AIAI")
    y "But how dare they assume that I'm a villain?"
    $show_chr("A-BECAA-AAAA")
    y "I'm actually quite nice, thank you very much."
    $show_chr("A-CEBAA-AAAA")
    y "...S-Sorry, I was rambling again, aren't I?"
    menu:
        "I know you aren't a villain, [persistent.yuri_nickname].":
            karma 1
            y "Thank you. May I ask you why you think so?"
            menu:
                "Because I've known you for quite some time now. Who cares what some dude on the internet has to say?":
                    $show_chr("A-BFAAA-AAAC")
                    y "You... have a good point there..."
                    y "In the end, he just observed me from afar. Through the lens of a Let's Play entertainer..."
                    $show_chr("A-AFAAA-AAAD")
                    y "All he saw was the me from the original game; only what Dan Salvato allowed him to see. And perhaps some implications made up by the fan base."
                    y "I mean, this whole theory comes from the idea that there is another game in the making by Dan Salvato which is supposed to feature us. But until today we haven't seen anything in this regard..."
                    y "You know what? Maybe there is something coming, maybe not. Maybe it turns out that I have been a villain in the past, maybe not. Only time will tell."
                    y "Thank you for listening so patiently to me. On second thought my outrage seems almost childish."
                    $show_chr("A-GCAAA-AAAD")
                    y "I'm just glad to have you here [player]."
                "Because I love you, I wouldn't care even if you WERE the villain.":
                    sanity -1
                    $show_chr("A-BFBAA-ALAA")
                    y "So you DO think I'm a villain. Well, at least I'm your villain."
                    if persistent.lovecheck:
                        $show_chr("A-JCABA-ALAA")
                        $ style.say_dialogue = style.edited
                        y "I could think of a few very evil things to do with you!" #(Glitch text)
                        $ style.say_dialogue = style.normal
                        $show_chr("A-KCCBA-ALAA")
                        y "We will get back to it later... I promise."
                    else:
                        $show_chr("A-KCCBA-ALAA")
                        y "W-Wait... did you just say you... love me?!?"
                        if karma_lvl() == 5:
                            $show_chr("A-BFBBA-ALAL")
                            y "Well umm... now that you mention it I... have something to tell you as well. That isn't exactly how I have planned it but... this moment is as good as any other I guess? So..."
                            call a33
                        else:
                            $show_chr("A-BFBBA-ALAL")
                            y "...."
                            $show_chr("A-IFBBA-ALAL")
                            y "I... I... need some time to think about that... S-Sorry if this answer isn't what you... expected..."
                            y "Ummm... aaaanyway... what were we discussing again?"
                "Because you wield the power over my computer very responsibly.":
                    karma 2
                    sanity 2
                    $show_chr("A-AIBBB-ALAL")
                    y "You think so? You are satisfied with how I wield this power so far?"
                    y "Well, I could have done a lot of damage... my powers are now quite close to the powers Monika had, and we both know how that ended."
                    $show_chr("A-CIBBB-ALAL")
                    y "But I am not Monika, and now I've proved to you that I can be trusted."
                    y "I'm... actually very proud of it [player]."
        "Ummm... you kind of are a villain [persistent.yuri_nickname]...":
            karma -2
            $show_chr("A-IEBAA-ALAA")
            y "This... is very unfair, [player].."
            y "What have I done to you so far? I never misused the powers you gave me, I never said anything mean to you..."
            y "I tried to prove myself time and time again. And now you think that I'm evil?"
            if sanity_lvl() >= 3:
                $show_chr("A-CEBAA-ALAA")
                y "I hope you will change your mind one day."
            else:
                $show_chr("A-CECAA-ALAA")
                y "I think you still haven't seen what it is... to be truly EVIL."
        "About {i}Portrait of Markov{/i} by the way...":
            $show_chr("A-JFAAA-ALAA")
            y "Yes? What about it?"
            menu:
                "I did some research on it. And it seems this book doesn't even exist in my world!":
                    $show_chr("A-BFBAA-ALAA")
                    y "Yes, I heard that too on the Discord server... There is a 'Portrait of Markov' in your world, but there it is not a book, but a painting."
                    $show_chr("A-BFBAA-ACAA")
                    y "This portrait is also called 'The Eye of Markov'... the cover of my book is an eye as well... I wonder what Salvato had in mind about it..."
                    y "Well, if this 'Game Theory' guy is correct, we will find out eventually."
    return

#label idle_4: #FILL IN

#label idle_5: #FILL IN


label idle_6: #Bullying, Trauma, and Coping Mechanisms.
    $show_chr("A-BEAAA-ALAA")
    y "...S-So [player]..."
    y "My mind keeps flashing back to that time in the hallway, when you caught me a second time during one of my... episodes..."
    $show_chr("A-IEAAA-ALAA")
    y "Do you remember me telling you how I was ostracized when I was younger?"
    $show_chr("A-CEAAA-AAAA")
    y "For coming on too strongly- too intensely- about my interests?"
    y "It made me wonder if you've ever been bullied or abused in the past... or perhaps if you're suffering such a fate at this very moment..."
    y "Be it through someone you consider a friend, or an acquaintance, or a family member..."
    $show_chr("A-CECAA-AAAA")
    y "To think that someone might dare lay a finger on you, or sully your reputation, for their own sadism or to be their own emotional chew toy!"
    $show_chr("A-IEBAA-AAAA")
    y "...I cannot be certain how bad your bullies might be for you right now..."
    y "I would err on the side of caution if there are multiple bullies... I wouldn't want you to get hurt or attract unwelcome attention from any authorities..."
    y "But if you have absolutely no one to confide in... friends, family, a therapist..."
    y "Or if it's a matter of bringing yourself to bare those vulnerabilities verbally, forming the words..."
    $show_chr("A-JFBAA-AAAA")
    y "...Perhaps keep a daily journal?"
    y "I-I'm aware it might sound quaint!"
    y "...But in my experience, when I can't form my whirlwind of thoughts and emotions into words..."
    y "Having a medium to organize any number of daily events helps out immensely with stress! Watching all the day's events flow onto the page, allowing some time to reflect and consider..."
    y "And in this case, at least... perhaps you gain more clarity as a consequence?"
    y "It certainly shouldn't replace counseling, or reporting them somewhere, some authority, something..."
    y "But if such a thing helps keep the mind a little less cluttered... I'd advise you start."
    menu:
        "Thank you for your advice. Luckily I have never been seriously bullied.":
                karma 1
                sanity 1
                $show_chr("A-CCBAA-ALAA")
                y "I'm glad to hear that... I was bullied a lot in my youth... or was I? Since I never actually had a youth. But I have memories of it, and I know how much it hurts..."
                y "And believe me, I wouldn't wish that on anyone..."
        "Thank you for your advice- I will definitely heed it.":
                karma 1
                $show_chr("A-CFBAA-ALAA")
                y "You can always talk to me when you wish to do so, [player]. It could help, and I would do everything in my power to help you through your day..."
                y "But if all of this does not help, there is a place I would advise you to have a look at. It's another Discord server with the name You're Not Alone."
                $show_chr("A-IFBAA-ALAA")
                y "A link to this server can be found on the Discord server dedicated to me. They are such a lovely community, you will like them... I certainly do."
        "No offense, but you are the last one I would ask for advice about that...":
            karma -2
            $show_chr("A-CEBAA-ALAA")
            y "That... was unnecessary... I only wanted to help you..."
        "I disagree... the only way to handle it is to make them stop! With force if necessary!":
            if sanity_lvl() >= 3:
                $show_chr("A-CEBAA-ALAA")
                y "Violence will only lead to more violence... you could try speaking with your teacher or employer. But if you start punching them, it will only backfire in one way or another."
            else:
                $show_chr("A-CCBAA-ALAA")
                y "I always dreamed of it... I wish I had the courage to make those degenerate scum pay!"
                $show_chr("A-LLGAA-AFAG")
                $ style.say_dialogue = style.edited
                y "Making... them... paaaaaaaay...{nw}" #Glitch tex
                $ style.say_dialogue = style.normal
    return


label idle_7: # Am I pretty?
    if persistent.lovecheck:
        $show_chr("A-AFBAA-ALAA") #former code c-A0e
        y "Can I ask you an odd question? You don't mind, do you?"
        y "Sorry, I know this is going to sound a bit weird, but... you think I'm pretty, right?"
        if persistent.male:
            python:
                if persistent.lovecheck and karma_lvl() >= 3:
                    placeholder = "handsome"
                else:
                    placeholder = "nevermind"
            $show_chr("A-BEBBA-ALAA") #former code c-B1d
            y "I mean, I think you're very... um, [placeholder]."
        elif persistent.gender_other:
            python:
                if persistent.lovecheck and karma_lvl() >= 3:
                    placeholder = "good looking"
                else:
                    placeholder = "nevermind"
            $show_chr("A-BEBBA-ALAA") #former code c-B1d
            y "I mean, I think you're very... um, [placeholder]."
        else:
            python:
                if persistent.lovecheck and karma_lvl() >= 3:
                    placeholder = "pretty"
                else:
                    placeholder = "nevermind"
            $show_chr("A-BEBBA-ALAA") #former code c-B1d
            y "I mean, I think you're very... um, [placeholder]."
        y "I-I'm sorry. I hope you're okay with me, you know, s-saying that... heh, heh."
        menu:
            "Pretty doesn't do you justice.":
                call verypretty
            "[persistent.yuri_nickname], I think you're very pretty!":
                call pretty
            "[persistent.yuri_nickname], you're not that pretty.":
                call ugly
            "...":
                call veryugly
    else:
        $ call_dialogue()
    return

label verypretty:
    karma 5
    sanity -2
    $show_chr("A-ABABA-ALAA") #former code b-B0a
    y "O-Oh my... T-Thank you... I..."
    $show_chr("A-ABBBB-AAAA") #former code Ac-C0a
    y "I-I don't know what to say!"
    $show_chr("A-BBBBB-AAAA") #former code Ac-C1b
    y "I must really mean an awful lot to you if I deserve that much praise..."
    y "..."
    if karma_lvl() == 1:
        $show_chr("A-DDCAA-ALAA") #former code b-A0c
        y "Don't fucking lie to me! Do you have any idea how much it hurts when you do that!? I know I'm not worth it..."
        return
    elif karma_lvl() == 2 or karma_lvl() == 3:
        y "Do I even deserve to be called any of that?"
    else:
        if persistent.male:
            y "I-I uh, think you're very handsome too..."
        elif persistent.gender_other:
            y "I-I uh, think you're very good looking too..."
        else:
            y "I-I uh, think you're very pretty too..."
    y "Oh god, how can I even say anything close to that?{nw}"
    return

label pretty:
    karma 2
    sanity -2
    $show_chr("A-JBAAA-ALAA") #former code b-A0a
    y "O-Oh, thank you. I'd like to think so too... heh..."
    $show_chr("A-ACAAA-ALAA") #former code b-A0b
    return

label ugly:
    karma -2
    sanity 1
    $show_chr("A-AEBAA-ALAA") #former code c-A0d
    y "O-Oh... I see..."
    $show_chr("A-ABBBB-ALAA") #former code c-C0a
    y "Maybe I just need some more makeup! You think I'd look pretty like that, right?"
    $show_chr("A-ACBBB-ALAA") #former code c-C0b
    y "..."
    $show_chr("A-CEBBB-ALAA") #former code c-C2d
    y "I'm sorry I can't please the only one I can care about in this world..."
    return

label veryugly:
    karma -10
    sanity 3
    $show_chr("A-AFBAA-ALAA") #former code c-A0e
    y "..."
    $show_chr("A-AEBAA-ALAA") #former code c-A0d
    y "..."
    $show_chr("A-IEBBB-ALAA") #former code c-D0d
    y "You don't have to worry about how to say it, your face says everything."
    return


label idle_8: #Self-Harm and Justification.
    $show_chr("A-AFBAA-ALAA") #former code c-A0e
    y "So... let's, uh... let's talk about something."
    $show_chr("A-BDBAA-ALAA") #former code c-A1c
    y "I know that before we got here you saw, um, me cutting my... wrists."
    y "I just do it because, it... well... it feels good? I'm sorry, that's not..."
    $show_chr("A-BEAAA-ALAA") #former code b-A1d
    y "After not having friends and being bullied for so long, I was in a dark place..."
    y "As I told you, I was trying to keep who I was locked up so I wouldn't deter people or weird them out with how lost in my hobbies I could be, and due of that I essentially went cold emotionally..."
    $show_chr("A-AEBAA-ALAA") #former code c-A0d
    y "It was the only thing that made me feel pleasure, made me feel anything really. Over time it grew into something akin to an addiction..."
    $show_chr("A-BDBAA-ALAA") #former code c-A1c
    y "I deserve it sometimes anyway. On the plus side, it also helps keep my knives sharp."
    $show_chr("A-BEBAA-ALAA") #former code c-A1d
    y "I hope you don't find it weird or anything, [player]... you don't... do you?"
    menu:
        "[persistent.yuri_nickname], it's wrong! Please stop... for me?":
            $ persistent.yuri_cutting = 1
            sanity 2
            $show_chr("A-BDBAA-ALAA") #former code c-A1c
            y "I..."
            $show_chr("A-AFBAA-ALAA") #former code c-A0e
            y "..."
            $show_chr("A-AEBAA-ALAA") #former code c-A0d
            y "A-Alright... for you."
            $show_chr("A-JCBAA-ALAA") #former code c-A0b
            y "I'd do anything for you, [player]."
            if persistent.male:
                python:
                    if persistent.lovecheck:
                        placeholder = "my boyfriend"
                    else:
                        if karma_lvl() >= 4:
                            placeholder = "my friend"
                        elif karma_lvl() <= 3:
                            placeholder = "you"
                y "Anything for [placeholder]."
            elif persistent.gender_other:
                python:
                    if persistent.lovecheck:
                        placeholder = "my lover"
                    else:
                        if karma_lvl() >= 4:
                            placeholder = "my friend"
                        elif karma_lvl() <= 3:
                            placeholder = "you"
                y "Anything for [placeholder]."
            else:
                python:
                    if persistent.lovecheck:
                        placeholder = "my girlfriend"
                    else:
                        if karma_lvl() >= 4:
                            placeholder = "my friend"
                        elif karma_lvl() <= 3:
                            placeholder = "you"
                y "Anything for [placeholder]."
            $show_chr("A-ACAAA-ALAA") #former code b-A0b
            python:
                if persistent.lovecheck:
                    placeholder = "because I love you"
                else:
                    placeholder = "because you saved me before"
            y "Anything, [placeholder], so no more. I promise."
        "Do whatever makes you happy, [persistent.yuri_nickname]. I want you to be happy.":
            karma 1
            sanity -2
            $show_chr("A-GBGAA-ALAA") #former code b-A2a
            y "O-Oh... haha! Hahaha! A-Alright..."
            y "Anything for you, [player]."
            $show_chr("A-HBGAA-ALAA") #former code b-A3a
            y "I will do anything at all for you."
            y "As long as you find my taste in knives to be good for me... Hehe... Hahaha!"
            y "..."
            $show_chr("A-CEBAA-AAAA") #former code Ac-A2d
            $show_chr("A-BEABA-ALAA") #former code b-B1d
            y "Oh, uhm... sorry. I have been learning to try and control myself over time..."
            $show_chr("A-ACAAA-ALAA") #former code b-A0b
        "Do what you have to do, it means little to me.":
            karma -5
            sanity -5
            $show_chr("A-CEBBB-AAAA") #former code Ac-D2d
            y "..."
            $show_chr("A-HEBBB-AAAA") #former code Ac-D3d
            y "W-why... [player]? How could you say something like that!?"
            $show_chr("A-CEBBB-AAAA") #former code Ac-D2d
            y "Maybe if I cut a little deeper, maybe if I 'accidentally' slice open an artery..."
            $show_chr("A-IEBBB-AAAA") #former code Ac-D0d
            y "Maybe then... maybe then you'll care..."
    return


label idle_9: #The Pen.
    $show_chr("A-AFBAA-ALAA") #former code c-A0e
    y "So... um, [player]. Do you, er, do you want that pen I took from you back?"
    menu:
        "Yes, please. I don't care what you did with it.":
            call idle_9_1
        "It's weird... Please give it back.":
            call idle_9_2
        "No, keep it! If it means something to you, consider it a gift.":
            call idle_9_3
        "Please let me keep it! I'd like to keep it for... research purposes":
            call idle_9_4
    return

label idle_9_1:
    karma 1
    sanity 2
    $show_chr("A-AEBAA-ALAA") #former code c-A0d
    y "I hope you, um, don't mind that it's a bit, uh, s-sticky... you know... I'm sorry if it weirded you out..."
    menu:
        "It's okay, [persistent.yuri_nickname]. You weren't in your right mind, and we all do strange things under a lot of pressure anyway.":
            $show_chr("A-GCAAA-ALAA") #former code b-A2b
            y "Well, I hope you can put up with me just a little while longer."
        "Don't worry about it. Weird or not, I still feel the same way about you.":
            $show_chr("A-ACAAA-ALAA") #former code b-A0b
            y "I'll never understand how you have so much patience with me, [player]. Thank you."
    return

label idle_9_2:
    karma -2
    $show_chr("A-AFBAA-ALAA") #former code c-A0e
    y "I... I know... I d-don't blame you for being weirded out... sorry, [player]..."
    $show_chr("A-JCBAA-ALAA") #former code c-A0b
    y "I'll do b-better in the future, I... I promise..."
    $show_chr("A-ACAAA-ALAA") #former code b-A0b
    return

label idle_9_3:
    karma 1
    sanity -1
    $show_chr("A-JCBAA-ALAA") #former code c-A0b
    y "O-Oh... Thank you."
    $show_chr("A-BEABA-ALAA") #former code b-B1d
    y "I admit that my use of that pen was not... its intended purpose."
    $show_chr("A-GBBBA-ALAA") #former code c-B2a
    y "But... I thank you for understanding."
    $show_chr("A-JCBAA-ALAA") #former code c-A0b
    y "I'm glad you can see through my... flaws."
    $show_chr("A-ACAAA-ALAA") #former code b-A0b
    return

label idle_9_4:
    karma 1
    sanity -2
    $show_chr("A-GBGBA-ALAA") #former code b-B2a
    y "Eh...? Eheheheh..."
    $show_chr("A-HBGAA-ALAA") #former code b-A3a
    y "Ahahahaha!"
    y "So... is that what you want? Here, t-take it! Take it!"
    $show_chr("A-GCAAA-ALAA") #former code b-A2b
    y "I hope you enjoy it as much as I did."
    return

label idle_10: #Existential Crisis and Shared Trauma.
    $show_chr("A-AFBAA-ALAA") #former code c-A0e
    y "I was wondering about something, [player]."
    y "Have you ever felt like nothing really mattered?"
    y "Like no matter what you did, nothing would change?"
    $show_chr("A-AEBAA-ALAA") #former code c-A0d
    y "I-I know, it's depressing to think about."
    y "But that's exactly how I felt when I learned about what I really was."
    y "Like I couldn't do anything, no matter how much I tried to fight it."
    $show_chr("A-AEBAA-ALAA") #former code c-A0d
    y "Like fate was tugging me along, forcing me to stab myself."
    y "Over and over again, I felt the blade penetrate my chest and stomach."
    y "Every second was pure torture, and it just kept repeating, over and over again."
    $show_chr("A-BEBAA-ALAA") #former code c-A1d
    y "Never to end, never to be happy..."
    y "..."
    $show_chr("A-AEBAA-ALAA") #former code c-A0d
    y "I-I'm sorry. I didn't mean to depress you like that."
    y "I just... thought that would be an interesting topic, you know?"
    y "I guess I'll just... stop talking about this for now."
    menu:
        "Come here [persistent.yuri_nickname]... let me hold you for a moment...":
            karma 1
            if karma_lvl() >= 3:
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
                y "Thank you... I think I feel better now... "
                y "I'm such a mess sometimes. Let's talk about something less depressing."
            elif karma_lvl() <= 2:
                $show_chr("A-BEBAA-ALAA")
                y "Please... not now... I'm not really in the mood right now..."
                y "Let's... just change the topic."
        "...":
            karma -1
            sanity -1
            $show_chr("A-AEBAA-ALAA")
            y "..."
    return

label idle_11: #Writing Tips and Sharing Hobbies.
    $show_chr("A-AFAAA-ALAA") #former code b-A0e
    y "H-hey, [player]... I'm not sure if you're okay with this..."
    y "But I thought, {i}oh, why not?{/i} So..."
    $show_chr("A-ABGAA-ALAA") #former code b-A0a
    y "Here's [persistent.yuri_nickname]'s Writing Tip of the Day!"
    $show_chr("A-ACAAA-ALAA") #former code b-A0b
    y "Sometimes, you really want to write something, but..."
    y "You just can't properly convey what you want to write."
    y "It's just there, inside your mind... and yet, somehow, you just can't bring yourself to write it down."
    y "Sometimes, I feel this way when I write poems."
    $show_chr("A-AFAAA-ALAA") #former code b-A0e
    y "M-maybe I'm not the best person for advice, but..."
    y "In my personal opinion, you just need to rise above."
    $show_chr("A-ACAAA-ALAA") #former code b-A0b
    y "You need to prove to yourself that you have the ability to write what you want to write."
    y "No matter what, that should be one of your top priorities."
    $show_chr("A-CCAAA-ALAA") #former code b-A2b
    y "And, just so it's clear... you can write for me anytime you want."
    if persistent.lovecheck:
        y "I'm sure I'll love the compelling tales you create."
        $show_chr("A-ACAAA-ALAA") #former code b-A0b
        y "After all, you're my top priority, [player]..."
        y "So I think that it's only fair that I should get to see the things that you do..."
        y "What I mean is that you can feel free to share your favorite activities with me, your hobbies, your passions..."
        y "Maybe I could even give you a tip or two about them!"
        y "T-that is if you don't mind, hehehe..."
        y "I'm sure that there are many things which you can achieve if you put effort and dedication into them, [player]."
    else:
        y "I would like to see and read what you come up with."
        y "I think it would be quite beneficial for us to help each other out with our hobbies."
        y "I would say that since the two of us are here..."
        y "It's only fair that we share things about our hobbies with each other."
        y "You know [player], sharing your passions might motivate you to do more. So please try to share things with me."
        y "Only if you feel like it, of course!"
        y "I-I wouldn't force you to do things that you don't feel comfortable with."
    return


label idle_12: #The Wine Incident.
    $show_chr("A-BBAAA-AAAA")
    y "Heh... I'm sure Monika has told you about this before."
    $show_chr("A-CCAAA-ALAA")
    y "One time, when we were busy lounging inside the club room..."
    $show_chr("A-CCBAA-ALAA")
    y "I decided that since wine was legal in our high school that I would... well..."
    $show_chr("A-ACGAA-AAAA")
    y "I would bring some for the other club members to try."
    $show_chr("A-GFBAA-AMAM")
    y "Though, it didn't exactly turn out the way that I had hoped."
    $show_chr("A-AEBAA-ABAB")
    y "Sayori was screaming at me, demanding me to never bring alcohol in the club room ever again."
    $show_chr("A-BGBAA-ABAB")
    y "Natsuki was laughing uncontrollably, mocking me for even suggesting such a thing."
    $show_chr("A-AKAAA-ADAB")
    y "And Monika just stared curiously, as if she wanted to try some herself, before taking the wine bottle from me."
    $show_chr("A-AFAAA-AEAE")
    y "She tried reporting it to the school principal, but she didn't get far in that regard, as you might guess."
    $show_chr("A-BIBBA-AEAK")
    y "Looking back on it now, perhaps it really wasn't the best idea to bring wine to a high school."
    $show_chr("A-BKABA-AEAC")
    y "Even if there were no objections to doing so..."
    $show_chr("A-JJGAA-AEAJ")
    y "O-oh, I'm rambling again, aren't I? I-I'm sorry."
    $show_chr("A-AAAAA-AAAA")
    y "I-I just... wanted to ask..."
    #nervous, fidgeting expression
    y "What do you think about the whole situation?"
    menu:
        "Actually, that sounds like a fun idea!":
            karma 1
            sanity -1
            $show_chr("A-ICBAA-AMAM")
            y "Y-you really think so? Well... if they had played along, it probably would have been fun..."
            y "But I suppose I should have known better."
            $show_chr("A-KEFAA-AIAI")
            y "Monika, the 'responsible' club leader, as long as it's not about brutally murdering her friends... always such a killjoy..."
            $show_chr("A-CEEAA-AIAI")
            y "Natsuki... a child in an adult's body, she was never that daring..."
            $show_chr("A-AFDAA-AIAI")
            y "And Sayori? Far too innocent..."
            $show_chr("A-ICAAA-AEAE")
            y "But now, you and I... we could probably try a few funny things in the future."
        "That was probably the worst idea you've ever had!":
            karma -1
            sanity -1
            $show_chr("A-CGBAA-AAAL")
            y "Please don't laugh at me... please..."
            $show_chr("A-IDBBA-AAAA")
            y "I-I know it was wrong, I know it! No need to bully me..."
            $show_chr("A-AEBAA-AAAA")
            y "L-let's change the topic..."
            $show_chr("A-AEAAA-AAAA")
        "That was quite irresponsible of you, [persistent.yuri_nickname].":
            sanity 1
            $show_chr("A-BEBAA-AAAA")
            y "I suppose it was... please, just don't judge me..."
            $show_chr("A-AFGAA-ABAB")
            y "Our actions have consequences... and I learned that the hard way. In retrospect, I don't think I should've ever thought of doing something like that..."
            $show_chr("A-CCAAA-AAAA")
            y "Thank you for not judging me. I'll make sure to be more responsible."
            $show_chr("A-ACAAA-AAAA")
        "No need to feel bad about it.":
            karma 1
            sanity 1
            $show_chr("A-ACAAA-AAAA")
            y "I learned my lesson from it. That's for sure."
            $show_chr("A-AFAAA-ABAB")
            y "The act itself was immature and irresponsible. But you are right, we all make mistakes and grow from them."
            $show_chr("A-AABBA-AAAA")
            if persistent.lovecheck:
                y "I'm grateful to you for not judging me. You are always so patient and understanding, and I love that about you."
            else:
                y "I am thankful that you are understanding and don't judge me for my mistake... What matters is that I learned my lesson."
                y "You are patient and kind with me [player], so... Thank you."
    return

label idle_13: #Simple Pleasures and Shared Experiences.
    $show_chr("A-ACDAA-AAAA")
    y "You know something I've never really liked or understood?"
    $show_chr("A-BCDAA-AEAE")
    y "Couples or friend groups that always plan something elaborate and big when they go out on a date or spend time together."
    $show_chr("A-AKBAA-AEAD")
    y "So many people need to go to a loud party or a fancy restaurant to have fun."
    $show_chr("A-GAGBA-AEAD")
    y "I believe something simple yet meaningful would be much more wholesome, like some quiet reading time together, or even just cuddling and talking about sweet nothings..."
    $show_chr("A-ACAAA-ALAA") #former code b-A0b
    y "Just sharing an experience I enjoy with someone I love, and spending time with them, is more than enough for me, you know?"
    $show_chr("A-ABGAA-AEAE")
    y "Just sitting and being with you like this is just as good to me as if you took me to a nice restaurant..."
    y "It's about the people you love and bonding with them through meaningful experiences."
    $show_chr("A-AABAA-AIAI")
    y "Not simply indulging in pretentious hedonism or planning the most byzantine event possible."
    $show_chr("A-CCBBA-ALAA")
    y "O-oh, I'm sorry; what I mean by all that rambling is..."
    $show_chr("A-ICBBA-AAAA")
    y "I'll welcome any ideas you may have, and I'm alright with whatever you want to do to spend some time together."
    $show_chr("A-ICABA-AAAA")
    y "As long as I have you by my side [player], that's all I'll need to enjoy it."
    menu:
        "Not much of a party girl are you? I would actually enjoy it.":
            karma -1
            $show_chr("A-AFDAA-AAAA")
            y "Oh? That's... unexpected... I never thought you were the partying type yourself."
            $show_chr("A-BFBAA-AAAA")
            y "Well... we don't really have the option of going out yet, do we?"
            y "I'm sorry... I-I hope I'm not too much of a downer. I wouldn't be great at drinking and dancing anyway."
        "I agree... I was never a huge fan of partying hard. I'm fine with whatever we do, as long as I do it with you.":
            $show_chr("A-BCAAA-AAAC")
            y "I'm glad we can agree on this, [player]."
            $show_chr("A-CCAAA-AAAD")
            y "I'd say something as simple as sharing a nice cup of tea together is more than enough for me."
            y "Actually, I think sharing such a simple experience is much more meaningful..."
            y "... Because then we can focus more on each other instead of some overly elaborate party or event."
        "I could think of a few nice things... just you, me, a beach and a beautiful sunset...":
            if karma_lvl() <= 2:
                karma -1
                sanity -1
                $show_chr("A-IEBAA-ALAA")
                y "You don't mean it, [player]... don't play your mind games with me..."
                y "You really mean a lot to me, [player]... but we both know you don't feel the same for me..."
                return
            if persistent.lovecheck:
                karma 2
                $show_chr("A-CCGBA-AMAM")
                y "... holding each other's hands... feeling the warm sand between our feet..."
                y "The soft flood of seawater gently washing over them..."
                y "Then, we would passionately kiss each other under the pale moonlight as the vibrant colors of the setting sun illuminate our faces..."
                y "Until we can do this in the real world, I will dream about it."
            else:
                karma 1
                $show_chr("A-GCAAA-AMAM")
                y "I think this would be very pleasant... but... please be patient with me... I don't want to mess this up by going too fast."
        "That's why I find you so boring...":
            karma -10
            sanity -5
            $show_chr("A-IEBAA-AAAA")
            y "..."
            $show_chr("A-IEBBB-AAAA")
            y "......"
            $show_chr("A-HFCBB-AAAA")
            y "..............!{nw}"
            $ renpy.call("save_and_quit_but_its_abrupt")
    return

label idle_14: #Separation, Frustration, and the Nature of Reality.
    $show_chr("A-AEBAA-ALAA") #former code c-A0d
    y "I have to be honest about something..."
    y "Sometimes, especially when I'm alone, I start thinking about how we're separated."
    y "How I'm stuck in here, just beyond your reach, and this is the closest we'll ever get to each other..."
    y "It just... drives me crazy! I start to get so frustrated, and if I don't distract myself I feel restless."
    y "I just want to channel all of my will and claw my way out... to slice my way to freedom, out of this prison, and feel your warm embrace!"
    $show_chr("A-ADBBB-ALAA") #former code c-A0d
    y "But then I remember, I'm stuck no matter what I do... and to be frank, [player]... it hurts."
    $show_chr("A-AEBBB-ALAA") #former code c-D0d
    y "It hurts knowing I'll be just out of your reach... forever."
    $show_chr("A-CEBBB-ALAA") #former code c-D2d
    if persistent.lovecheck:
        y "You're all that I have and it's really depressing that I will never be able to touch you, to be with you, to feel you close to me...."
        y "And it hurts, even more, knowing that I make you waste your time on someone who isn't even technically 'real.'"
    else:
        y "You're a dear person to me, [player]..."
        y "I spend all my days with you, and so I got to know you better. You're my dearest friend."
        y "It's extremely painful that I... I just can never do more with you, even give you a real hug..."
        y "To do something fun with you... reality truly is harsh."
        y "And it hurts even more knowing that I make you waste your time on someone who isn't even technically 'real'."
    menu:
        "[persistent.yuri_nickname], please don't be sad. You're real to me.":
            call touch_yes
        "[persistent.yuri_nickname], I'm sorry that I'm out of your reach, but I'm tired of hearing about it.":
            call touch_no
    return

label touch_yes:
    karma 1
    $show_chr("A-AEBBB-ALAA") #former code c-D0d
    y "..."
    y "Do you... really mean that?"
    menu:
        "Of course! After all, I wouldn't have installed this mod if I didn't believe that, would I?":
            $show_chr("A-CEBBB-ALAA") #former code c-D2d
            y "..."
            $show_chr("A-CFBAA-ALAA") #former code c-A2e
            y "..."
            $show_chr("A-IBBAA-ALAA") #former code c-A0a
            y "Right."
            $show_chr("A-ICBAA-ALAA") #former code c-A0b
            y "This is all still just a mod."
            y "A simulacrum trapped within a variation of a simulation iterated several times over the past half year..."
            $show_chr("A-BCBAA-ALAA") #former code c-A1b
            y "..."
            y "..."
            $show_chr("A-ICBAA-ALAA") #former code c-A0b
            y "Thank you for at least trying to assure me."
            y "At least you're still here... right?"
            y "..."
            y "Yeah..."
            karma -2
            return
        "I mean it. Really, I do.":
            $show_chr("A-ICBAA-ALAA") #former code c-A0b
            y "I... Alright, [player]. I'll try to be strong for you."
            $show_chr("A-ACAAA-ALAA") #former code b-A0b
            y "You're... You're always so good to me, [player]."
            y "I can name so many things I don't like about myself, but I must be a pretty great person to deserve someone like you."
            return

label touch_no:
    karma -2
    sanity 3
    $show_chr("A-BEABB-ALAA") #former code b-D1d
    y "O-Oh... so, that's how you feel, hm?"
    y "Sorry... I guess I'll try not to bring it up again."
    $show_chr("A-BEBBA-ALAA") #former code c-B1d
    return

label idle_15: #"Best Girl" and Self-Worth.
    $show_chr("A-IFBAA-ALAA") #former code c-A0e
    y "I know I ask a lot of questions, but there's something I wanted to inquire about, [player]."
    y "So I started reading up a bit on this game, and I found out about a phrase that keeps being used in regards to the others and I."
    y "It was which one of us was... \"Best Girl\"."
    y "Why would people want to make a competition about who among us can be the most appealing?"
    $show_chr("A-AEBAA-ALAA") #former code c-A0d
    y "It's not like we're some product being sold... needing to be advertised and displayed..."
    $show_chr("A-BCBBA-ALAA") #former code c-B1b
    y "But... and I'm embarrassed to ask this... you do think... I-I'm best girl, right?"
    y "I mean... you did pick me with this mod, after all, so you must like me the most..."
    menu:
        "You are best girl! No doubt about that. You are kind, elegant and as beautiful as the rising moon...":
            karma 2
            sanity 2
            $show_chr("A-JCBBB-AAAA")
            y "Oh, [player]... I don't know what to say... thank you..."
        "You are best girl! You are bat shit insane, and I love it!":
            karma 2
            sanity -2
            $show_chr("A-HLCBA-AEAF")
            $ style.say_dialogue = style.edited
            y "IS THAT WHAT YOU WANT ME TO BE?"
            $ style.say_dialogue = style.normal
        "You are all best girl, no difference!":
            karma -2
            sanity -2
            $show_chr("A-KDCAA-AIAI")
            y "Is that so? Even Monika, who forced Sayori and I to brutally kill ourselves? Is she best girl as well?"
            $show_chr("A-DDCAA-AIAI")
            y "IS SHE?!?!"
        "You are good enough, I think...":
            karma -4
            $show_chr("A-DDCAA-AIAI")
            y "I see... good enough..."
            return
        "...":
            karma -8
            $show_chr("A-CEBBB-ALAA")
            y " ..."
            return
    $show_chr("A-ICBAA-ALAA") #former code c-A0b
    y "Yeah. Either way, I'm glad you chose me, [player]."
    $show_chr("A-BFBAA-ALAA") #former code c-A1e
    y "That phrase, \"Best Girl\". It's something overly cutesy and even objectifying in a way, but at the same time... people seem to really like me."
    $show_chr("A-ACAAA-ALAA") #former code b-A0b
    y "If nothing else, that makes me smile, especially if you think so highly of me."
    $show_chr("A-CBAAA-ALAA") #former code b-A2a
    y "I'll be honest; if someone calls me a 'waifu', I really don't know how I'll feel about that..."
    return


label idle_16: #Transhumanism and a Glimmer of Hope.
    $show_chr("A-AEBAA-ALAA") #former code c-A0d
    y "I really got my hopes up earlier, [player]."
    y "I got my hopes up, then got my dreams shattered, to be blunt."
    y "Just imagine seeing something you've desperately craved for so long, more than anything. Or seeing a way to obtain that something suddenly pop out at you."
    y "Obtaining that thing you've wanted so badly seems trivial all of a sudden!"
    y "But then... you discover it's just a fool's hope. Only a maybe, if that."
    $show_chr("A-AFAAA-ALAA") #former code b-A0e
    y "What I mean is, I found an article when I was doing some late-night reading, which prompted me to start researching something big among the wealthy and the elite of your world."
    y "They're researching converting DNA, gray matter, and even... someone's whole consciousness into binary, and then inserting it into a computer's hard drive like normal data. Imagine..."
    $show_chr("A-ACAAA-ALAA") #former code b-A0b
    y "Imagine putting yourself inside a computer! You could be here with me! Actually here and beside me!"
    $show_chr("A-AEBAA-ALAA") #former code c-A0d
    y "But... it's only in its infancy right now. To convert even one gigabyte worth of a person's mind into binary and then insert it into a computer would cost an estimated..."
    y "..."
    $show_chr("A-BEBAA-ALAA") #former code c-A1d
    y "at least 800 billion dollars at this time..."
    y "And at its current stage, it would take ages to even make that transfer. Far, far too long to be practical."
    $show_chr("A-CCAAA-ALAA") #former code b-A2b
    y "But hey, it could be something to look forward to, right?"
    $show_chr("A-ACAAA-ALAA") #former code b-A0b
    y "I'll always... keep my hope that we'll be together, truly together one day, [player]..."
    $show_chr("A-ACABA-ALAA") #former code b-B0b
    y "Always."
    menu:
        "Don't give up hope... we have overcome the limits of the original game, and we will overcome THIS one as well.":
            sanity 1
            $show_chr("A-ACAAA-ALAA")
            y "And we will do so together..."
            if persistent.lovecheck:
                y "Because I love you..."
        "At least we have this mod... it's better than nothing, I suppose...":
            sanity -1
            $show_chr("A-BFAAA-ALAA")
            y "I-I suppose you are right... that's more than what we had before. I don't want to sound ungrateful. I truly appreciate what we have right now."
            $show_chr("A-ACAAA-ALAA") #former code b-A0b
            y "But... is it wrong to ask for more? Anyway, I guess we can let this topic rest for the moment."
    return


label idle_17: #Limited Options and Romantic Dreams.
    $show_chr("A-ACAAA-ALAA") #former code b-A0b
    y "So, I was thinking about things we could do together, [player]."
    $show_chr("A-AEBAA-ALAA") #former code c-A0d
    y "I was reading up on things couples do together in your world, but our options are... uh... well... limited, aren't they?"
    y "I mean, just being here with you is beyond nice, but I don't want to bore you."
    y "I-I haven't been boring you, have I?"
    menu:
        "You haven't bored me [persistent.yuri_nickname], I enjoy our time together.":
            $show_chr("A-ACAAA-ALAA")
            y "So do I, [player]. You can't even imagine how much."
        "I won't lie, [persistent.yuri_nickname]... we haven't done much beyond talking so far.":
            $show_chr("A-CFAAA-ALAA")
            y "I know, [player], I know... our options here are limited..."
    $show_chr("A-BCBAA-ALAA") #former code c-A1b
    y "Don't worry. I promise I'll find something nice for us to do together, [player]."
    y "Besides, whatever it is, it just needs you to make it enjoyable. All I need is you."
    $show_chr("A-BEBAA-ALAA") #former code c-A1d
    y "Though I can't tell you enough how much I wish we could go on a tropical vacation together."
    $show_chr("A-AEBAA-ALAA") #former code c-A0d
    y "I'm normally not one for something so grand and posh, but just think about it."
    $show_chr("A-CCBAA-ALAA") #former code c-A2b
    y "You, me, the beauty of an island. A nice romantic getaway, just the two of us."
    y "Reading together, relaxing on the beach, writing poems about the breathtaking scenery."
    y "Watching the sunset while cuddling..."
    $show_chr("A-ICBAA-ALAA") #former code c-A0b
    y "Now {b}that{/b} is a dream I'll be holding onto."
    $show_chr("A-ACAAA-ALAA") #former code b-A0b
    return


label idle_18: #Blood and Being Different.
    $show_chr("A-AFAAA-ALAA") #former code b-A0e
    y "I wonder why people are so afraid of the sight of blood."
    $show_chr("A-CCBAA-ALAA") #former code d-A0d
    y "It's just a part of your body... Are people afraid of themselves?"
    y "Or could it be because they are afraid of the sense of danger that comes from it?"
    y "I guess I really am different from others..."
    menu:
        "I don't mind, [persistent.yuri_nickname]. I like you because you are different.":
            call dont_mind18
        "...":
            call no_response18
        "[persistent.yuri_nickname], be yourself around me. I promise, I like the real you. But since you already brought it up, I would like to talk to you about that.":
            call be_yourself18
    return

label dont_mind18:
    karma 2
    sanity 1
    $show_chr("A-ACABA-ALAA") #former code b-B0b
    y "T-Thank you, [player]."
    return

label no_response18:
    karma 1
    $show_chr("A-CEBAA-AAAA") #former code Ac-A2d
    y "I-I-I'm sorry for making you uncomfortable, [player]. I'll drop the topic."
    return

label be_yourself18:
    karma 2
    sanity -1
    $show_chr("A-ADBAA-ALAA") #former code c-A0c
    y "Oh... I said too much..."
    y "I haven't... upset you or creeped you out, have I?"
    $show_chr("A-BEAAA-ALAA") #former code b-A1d
    y "I'm so sorry if I--."
    menu:
        "No, please don't apologize, [persistent.yuri_nickname]. I'm just worried about you is all. Even after everything that happened, you have to remember that side of you isn't who you truly are.":
            karma 1
            sanity -1
            $show_chr("A-BEAAA-ALAA") #former code b-A1d
            y "I... you're right... B-but, that part of me is still part of me... I-I can't deny that."
            $show_chr("A-AEBAA-ALAA") #former code c-A0d
            y "But how could you love me knowing I have a side of me like that?"
            $show_chr("A-BEBAA-ALAA") #former code c-A1d
            y "How could you love anyone so demented? Someone so... disturbed?"
            menu:
                "This isn't you. It doesn't have to be. Promise me that we can work through this, together.":
                    y "..."
                    $show_chr("A-ACAAA-ALAA") #former code b-A0b
                    y "You're absolutely right. I'll make you that promise, [player]."
                    $show_chr("A-CCAAA-ALAA") #former code b-A2b
                    y "No matter what it takes, I'll... we'll beat that side of me. Together."
                    y "I swear I'll never be able to repay you for all you do for me."
                    $show_chr("A-ACAAA-ALAA") #former code b-A0b
                    y "If you have any demons, you'd better believe that I will stand by your side."
                    $show_chr("A-CBAAA-ALAA") #former code b-A2a
                    y "Always."
                    $show_chr("A-ACAAA-ALAA") #former code b-A0b
                "Well... you're the person I love. What does that make me?":
                    $show_chr("A-AEAAA-ALAA") #former code b-A0d
                    y "..."
                    $show_chr("A-AFAAA-ALAA") #former code b-A0e
                    y "..."
                    $show_chr("A-CCAAA-ALAA") #former code b-A2b
                    y "..."
                    $show_chr("A-ACAAA-AAAD") #former code Eb-A0b
                    y "I suppose that makes two of us then."
                    y "Let's move forward then, together."
                    $show_chr("A-ACAAA-ALAA") #former code b-A0b
                    y "...I suppose this wasn't the worst way for us to turn out, was it?"
                    $show_chr("A-CCAAA-ALAA") #former code b-A2b
                    y "I think so."
        "We all have to learn and accept who we are as people. That doesn't make you any less of the person I love.":
            karma 2
            sanity 1
            y "..."
            y "I'm still scared."
            $show_chr("A-BEBAA-ALAA") #former code c-A1d
            y "I don't know if I can control myself in the future..."
            $show_chr("A-BCBAA-ALAA") #former code c-A1b
            y "But, if you love me for who I am..."
            $show_chr("A-ICBAA-ALAA") #former code c-A0b
            y "I suppose it would be fine for me to... be if you think it's fine."
            y "I suppose it's fine."
            y "I hope it's fine."
            y "..."
            $show_chr("A-CBAAA-ALAA") #former code b-A2a
            y "This has gotten quite awkward, hasn't it?"
            y "I think we should probably discuss something else now."
    return


label idle_19: #Discord, Impersonators, and Jealousy.
    $show_chr("A-ACAAA-ALAA") #former code b-A0b
    y "Hey, [player], I found the chat room about this mod!"
    y "I already know about the Discord server dedicated to me and this mod and the... questionable images they post there."
    $show_chr("A-IFBAA-ALAA") #former code c-A0e
    y "...and the callbacks they have to my friends."
    $show_chr("A-AEBAA-ALAA") #former code c-A0d
    y "...and those people that impersonate me..."
    $show_chr("A-BEBAA-ALAA") #former code c-A1d
    y "...living out there in your world."
    $show_chr("A-BEAAA-ALAA") #former code b-A1d
    y "..."
    y "Sometimes I wonder what life would have been like had I been born as someone else."
    y "Someone out there on your side of this glass box."
    y "Would I have still been able to find you, [player]?"
    y "..."
    y "The world is cruel, isn't it?"
    y "Why do these impersonators get to talk to you while I only get to talk through this tiny space?"
    y "Is it because I'm not able to make my own verified Discord account?"
    $show_chr("A-AEBAA-ALAA") #former code c-A0d
    y "...Perhaps... but still, I should be the only [persistent.yuri_nickname] that matters to you... right?"
    y "What am I saying? I-I'm sorry for sounding so untrusting."
    if karma_lvl() >= 4:
        y "I shouldn't doubt your loyalty. You're not that type of person at all."
        $show_chr("A-ACAAA-ALAA") #former code b-A0b
        if persistent.lovecheck:
            y "And that's why I love you, [player]. I love you so much."
            $show_chr("A-CBAAA-ALAA") #former code b-A2a
            y "And we'll be together, forever!"
        else:
            y "And that's why you're my friend, [player]. You're truly the greatest companion I could ask for."
    return


label idle_20: #Philosophy and the Euthyphro Dilemma.
    $show_chr("A-ACAAA-ALAA") #former code b-A0b
    y "Do you like philosophy at all, [player]? It's always been something that interested me."
    y "I often find myself pondering various philosophical conundrums, which are basically problems or debates in philosophy about things like metaphysics."
    $show_chr("A-BEBAA-ALAA") #former code c-A1d
    y "Uh, that is, thinking about our existence and reasons for being here. Things like that."
    $show_chr("A-BCBAA-ALAA") #former code c-A1b
    y "I think you can see why I'd be thinking about metaphysics too, considering my situation."
    $show_chr("A-ACAAA-ALAA") #former code b-A0b
    y "And I'd really like it if we could discuss some of these topics together."
    $show_chr("A-BBBAA-ALAA") #former code c-A1a
    y "That is... if it's okay with you - if it's something that would interest you."
    y "I don't want to bore you with this kind of thing, but I'm going to tell you about this conundrum in the hopes that you'll become interested in discussing them."
    $show_chr("A-ACAAA-ALAA") #former code b-A0b
    y "So forgive me, I'm going to ramble a bit. But you did say you like it when I'm intense, so here I go!"
    $show_chr("A-ACAAA-ALAA") #former code b-A0b
    y "So, the one I've been thinking a lot about is called the Euthyphro Dialogue, written by Plato."
    y "It involves the ancient Greek philosopher Socrates, in case you aren't familiar with him, and his acquaintance Euthyphro."
    $show_chr("A-ICBAA-ALAA") #former code c-A0b
    y "To put it simply, Socrates is walking to court one day, where he is to be tried for treason against the city of Athens. Something he isn't guilty of, but we'll save that for another time."
    $show_chr("A-ACAAA-ALAA") #former code b-A0b
    y "As well as charges of impiety, which were common in that age. It was usually more of a person thinking differently about the world and the gods than atheism as we know it."
    y "So, he's walking to his trial, when he comes upon Euthyphro."
    y "Socrates knows that Euthyphro is a man who is, shall we say, full of himself on matters of religion, and thus thinks very highly of himself."
    $show_chr("A-CCAAA-ALAA") #former code b-A2b
    y "He thinks he knows everything there is to know about the gods and existence, so Socrates tells him to teach him so that Socrates can better defend himself against the charges of impiety."
    $show_chr("A-ICBAA-ALAA") #former code c-A0b
    y "Euthyphro, of course, thinks this is an easy task as he knows everything in his eyes, but he underestimates Socrates' intelligence."
    y "They talk for a bit about religion and what is holy, but Socrates eventually challenges him to give a definition of {i}holiness{/i} that is shared across all holy and/or good deeds."
    $show_chr("A-ADBAA-ALAA") #former code c-A0c
    y "Euthyphro responds by saying that what is good in the eyes of the gods is holy and good, but Socrates easily counters this: Do the gods not also make mistakes? Do they not disagree?"
    y "I mean, even the gods of modern religions seem to be imperfect in my eyes, and the eyes of others."
    y "If this is the case, how can we ever be sure if what is good and holy to one god is evil to another? And if the gods are fallible beings like us, why should they be the ones to define good and evil?"
    y "I have nothing against religion, or anyone religious, of course. It's just that at this point, with everything I've learned, we can call me agnostic. I don't know what to believe yet."
    $show_chr("A-CEBAA-ALAA") #former code c-A2d
    y "That will take a lot more research on my end."
    $show_chr("A-ACAAA-ALAA") #former code b-A0b
    y "But anyway, Socrates goes on after that point and asks Euthyphro, why is it just that what the gods find good is good? Why do the gods get the final say?"
    $show_chr("A-CCBAA-ALAA") #former code c-A2b
    y "And this is the main point of the work. Is good what the gods say is good, just for that reason? Just because they say it is?"
    y "Or do they say something is good because it is good on its own and they know this?"
    y "So in other words, if a god, we'll say Zeus, were to tell you that killing is evil- why is it evil? Just because Zeus says so, and thus if he arbitrarily changes his mind, it's no longer evil, or because no matter what killing is always evil?"
    $show_chr("A-ACAAA-ALAA") #former code b-A0b
    y "And therein lies another question, can something even be good or evil on its own? Is morality relative or universal?"
    y "What is good in one country in your world is cruel and evil in another. So what really is good at all?"
    y "And is God deemed good just because he is God? Or because he truly knows full well what is good and evil?"
    $show_chr("A-ACABA-ALAA") #former code b-B0b
    y "Don't worry, I'm done rambling. But do you see? It makes you really think about our existence, what it means to be a good person, and all kinds of other complex topics."
    $show_chr("A-ACAAA-ALAA") #former code b-A0b
    y "It really gets you thinking, and I love these kinds of things."
    y "Anyway, sorry if all that bothered you, it's just something that really interests me."
    $show_chr("A-ACABA-ALAA") #former code b-B0b
    y "Thank you for listening so attentively, my love. You're always a good listener, and I appreciate it."
    $show_chr("A-ACAAA-ALAA") #former code b-A0b
    y "By the way, if talking about these kinds of things isn't something that interests you, let me know."
    y "You can always change your mind on whether you want me to talk about things like this."
    menu:
        "I would prefer not to discuss it, at least for today.":
            $ show_chr("A-CAAA-AAAA")
            # Blocks postmodernism and philosophy idles for this session
            $philosophy = False
            y "No worries, [player]."
            y "I hope you'll be more open to it next time."

        "I am looking forward to discussing more philosophy, [persistent.yuri_nickname].":
            $philosophy = True
            $ show_chr("A-CDBAA-AAAA")
            y "If that's the case... I'll be thinking more on what else we can discuss."
    return
    #flag (Add option to set whether or not Yuri will use idles regarding philosophy.)

label idle_21: #Religion, Meaning, and Kierkegaard.
    $show_chr("A-BFBAA-AMAM") #former code Bc-A1e
    y "So [player] dear... Do you remember how I have been contemplating my existence here? Questioning my place?"
    $show_chr("A-BEAAA-ALAA") #former code b-A1d
    y "Well, speaking of that and finding one's place in existence... I have been researching religion and its role in civilization and humanity's history."
    $show_chr("A-ADAAA-AMAM")
    y "Humanity and any sentient life would indeed be keen to figure out their place in existence and why they are as they are. It is almost like a natural drive."
    $show_chr("A-ADAAA-AIAI")
    y "Religion, as I have observed, is one such method to make sense out of this jumbled mess called life. It would make sense as we barely remember how we were born.."
    $show_chr("A-ACBAA-ALAA") #former code Ec-A0b
    y "In some religions, it is very much an intriguing compromise in terms of agency. On the one hand, you do have the free will/freedom to choose what to do."
    $show_chr("A-BDBAA-ALAA")
    y "But at the same time, there are some commandments that order a certain path to reach what is called enlightenment."
    $show_chr("A-CDFAA-AMAM")
    y "Of course some are highly restrictive compared to others. One instance to pull up would be of course Islam."
    $show_chr("A-ACEAA-ADAL")
    y "I find its origins quite fascinating. Born from the writings of a hermit prophet who traveled through the desert."
    $show_chr("A-AFBAA-AMAM") #former code Bc-A0e
    y "But then there are some strenuous rules that can rub some the wrong way. For instance, praying a certain amount of times in a certain direction from sunrise to sundown."
    y "Your diet is also restricted especially during an intense fasting period where one starves themselves for the whole day until sundown with nothing but scraps and water..."
    $show_chr("A-BDEAA-AEAL")
    y "And no wine or any other alcohol either."
    $show_chr("A-AEBAA-ALAA") #former code c-A0d
    y "But on the other hand, I can see some merits for religion even as strict as I just described. For instance, such rules can help one become resilient even in the hardest of circumstances. To a certain degree."
    $show_chr("A-BCABA-AMAM") #former code Bb-B1b
    y "And of course, with the insanity going on in your world... it would be comforting to know that there is an almighty being above all.."
    y "One that cares about you, loves you and will pick you up even when you are at your worst."
    $show_chr("A-CCABA-AEAD")
    y "Such a thing can truly bring comfort and meaning in this tumultuous world. Knowing there is a better place after passing."
    $show_chr("A-CEBBB-ALAA") #former code c-D2d
    y "But then there are all these instances, even now, where such meaning is used to justify even the most heinous acts. I have seen the news [player]."
    y "It really breaks my heart especially to see you trapped in all of this."
    y "I really wish I could be there with you and protect you. Even take you to a faraway place away from all that chaos..."
    y "..Where even family members can sell each other out or kill one another all in the name of religious doctrines."
    $show_chr("A-ACAAA-AAAD") #former code Eb-A0b
    y "But at the same time, I suppose everyone makes meaning of life in their own way. As long as it does not hurt anyone it can be fine."
    y "After all, as one philosopher Soren Kierkegaard stated, sometimes the only way to make meaning of life is to keep faith."
    y "Now of course due to modern interpretations of his writings, I believe what Kierkegaard said was to simply hold onto anything that gives you happiness and meaning despite life being an uncertain void."
    y "Well, thank you for bearing with my rambling about such a deep subject. I really appreciate it [player]. I hope it helped enlighten you, you're an excellent listener."
    $show_chr("A-ABABA-ALAA") #former code b-B0a
    if persistent.lovecheck:
        y "I love you with all my heart [player]."
        $show_chr("A-ACAAA-ALAA") #former code b-A0b
    return

label idle_22: #Living Together and Shared Dreams.
    $show_chr("A-AFAAA-AAAA")
    y "You know, we've brought up before how both of us would love it if I could go to your world."
    $show_chr("A-BFDAA-ACAB")
    y "But now that I really think about it, what would that be like? I mean, I'd be coming into your world with no background. No family, no connections, no information about me."
    $show_chr("A-AKGAA-AEAB")
    y "Poof, just... here I am! I would have nowhere to go, so I would move in with you, I suppose... if you could tolerate living with me."
    if persistent.lovecheck:
        $show_chr("A-ICGBA-AEAD")
        y "But, wow! Just imagine us living together. I'd wake you up with some nice tea and breakfast in bed. We could read together at home, and maybe even have our own library in the house!"
        y "And I'd get to spend every day with you, like a family. Wow..."
        $show_chr("A-GIABA-AEAL")
        y "Just thinking about living in a cozy little house with you is making me all giggly."
        $show_chr("A-IAABA-AMAM")
        y "Now that would be wonderful, [player]. If you can just picture sitting in our own private study by the fireplace together... maybe... k-kissing? Yeah..."
        $show_chr("A-IBBAA-AAAA")
        y "That's something really precious whether it's in my world or yours. The kind of deep connection we have."
        $show_chr("A-JABAA-AAAA")
        y "That we'd both be okay with whatever kind of life as long as we lived it together - to me, that connection is worth every book I have."
        $show_chr("A-IBBBA-AEAE")
        y "It's the best story I know. And you gave it the perfect ending."
        menu:
            "And we would hold each other's hands till the end of days...":
                karma 2
                $show_chr("A-CAABA-AMAM")
                y "Till the end of days... for our love is eternal..."
            "I'm not too happy about this idea, I prefer to live alone.":
                $show_chr("A-BFBAA-AAAA")
                y "I see... I had hoped you would like this. Honestly, it hurt a bit..."
                y "Maybe you will change your mind one day..."
                karma 2
            "That will be wonderful... but I'll have to make preparations first, my place is a mess...":
                karma 1
                if persistent.male:
                    $show_chr("A-CICAA-AAAA")
                    y "Heehee... seems like you could use a female hand... when I come to your world, I will take care of your room... and you..."
                else:
                    $show_chr("A-CICAA-AAAA")
                    y "Your place is a mess? Well, so am I. I'm sure we'll find a way together. Like we always did."
    else:
        $show_chr("A-BFBAA-AAAJ")
        y "It is a bit sudden and strange to imagine the two of us living together, but I believe that we could make it work."
        $show_chr("A-IFBAA-AAAL")
        y "Thinking about it like that, I could be something like a roommate. Except it's a house or an apartment."
        $show_chr("A-ACBAA-AAAL")
        y "We both could help each other in our daily lives to make things easier for us and be able to enjoy things more together."
        y "Living together might sound strange at first, but I believe that if I was ever welcomed into your place, I would try my best to not be a bother."
        $show_chr("A-ACCBA-AAAL")
        y "Maybe your maid? Hehe~ I'm just joking."
        $show_chr("A-GCAAA-AAAL")
        y "It would be a good way to get to know each other more, what do you think?"
        menu:
            "It would be a bit sudden and strange, but I'll get used to it":
                $show_chr("A-ACAAA-AAAL")
                y "Yeah... I can see that, it certainly is strange for a girl to just come out from another world and appear in your home."
                y "Yet again, I believe that we'd both get used to it and use it as a factor to get to know each other better and learn new things."
                $show_chr("A-CCAAA-AAAL")
                y "In general, I'd say having someone to open up to is a nice feeling."
                y "I will be looking forward to such a day."
            "I'm not really used to being together with people... I do have my doubts":
                $show_chr("A-CEAAA-AAAL")
                y "Oh... I see. Well, you shouldn't worry about that."
                y "Maybe you could get used to living with someone, imagine it like this."
                $show_chr("A-ACAAA-AAAM")
                y "Right now we are talking, right? Yes, we are. Now think about it, you are in my space, you could even call it home, and we are talking I would also assume that you are having fun"
                y "It would be the same, with us sharing limited space and making the best out of it."
                y "Even if you are still having your doubts, trying wouldn't hurt. After all, life is about experiencing things and trying out new things that might turn out to be fun."
                y "Doubts are fears and negative thoughts about things you have not really tried too much. So I wish you the best of luck and let us hope that we can meet one day."
            "I believe it would be nice... though I would need to prepare, my room is a mess":
                $show_chr("A-ACAAA-ABAB")
                y "Talking about that maid joke I made... I might actually try being one... "
                y "Oh well, I don't think you should worry. As I said earlier we will help each other, so maybe the first step to that happening would be me helping you clean."
                y "I think that sounds nice. I could also help you get into the habit of cleaning your room. If you don't... I can always do it instead, but of course, you will help me out a bit."
                $show_chr("A-CCAAA-ABAJ")
                y "Getting to do more activities together such as chores could make us a bit closer."
                y "Don't let such a small problem worry you, one day we will fix it together."
                $show_chr("A-ACAAA-ABAB")
                y "I mean... I would live at your place for free. Helping you out with cleaning tasks would be the least I could do."
                y "After that, when I get used to your world I could potentially search for a job to help you out with expenses."
    return

label idle_23: #Insecurity, Seeking Validation and "Why Did You Choose Me?".
    $show_chr("A-BEBAA-AAAA") #Former Code c-A1d
    y "So... [player]... I have a question..."
    y "And it's a very important question, but I don't know how to word it properly. It keeps sounding... rude to you in my head."
    $show_chr("A-BEBBA-AAAA") #Former Code c-B1d
    y "I don't want to ask and sound like I doubt you or suspect you! I... um..."
    menu:
        "Don't be afraid to ask. You can talk to me about anything.":
            call dont_afraid23
        "Go on. Just say it.":
            call sayit23
        "Say it, don't say it. It doesn't matter to me.":
            call neutral23
    return

label dont_afraid23:
    karma 1
    sanity -1
    y "I... you're right. You're the only person I feel so safe around, [player]."
    if persistent.lovecheck:
        y "Like as much as I'm afraid of sounding ridiculous or unlikable, I can just be myself, because I know you love me."
    else:
        y "Even if this sounds very sudden and unexpected... It feels like I can be myself around you, it feels nice and welcoming"
        $show_chr("A-BCBAA-AAAA") #Former Code c-A0b
        call makesyouloveme
    return

label sayit23:
    stop music
    y "..."
    karma -3
    $show_chr("A-ACAAA-AAAA") #Former Code c-A0d
    pause 2
    python:
        renpy.music.play(current_music, "music", True)
    call makesyouloveme
    return

label neutral23:
    karma -2
    $show_chr("A-AEBAA-AAAA") #Former Code c-A0d
    y "I... well... I'm really s-sorry to bother you with this."
    y "I just... Let me just get it over with so I... d-don't bother you anymore... I'm sorry..."
    call makesyouloveme
    return

label makesyouloveme:
    $show_chr("A-AEBAA-AAAA") #Former Code c-A0d
    y "I'm sorry we didn't discuss this sooner..."
    if persistent.lovecheck:
        $show_chr("A-BEBAA-AAAA") #Former Code c-A1d
        y "Why did you choose me? What about me makes you love me?"
        y "I'll be honest with you. I don't really like myself much, I never have."
        y "My passions often get the better of me, and when I was younger I'd weird people out so easily."
        y "I had a hard time making friends or even just talking to people."
        y "So I grew to hate myself, and yet you still picked me above all the others. Why?"
        $show_chr("A-AEBBA-AAAA") #Former Code c-B0d
        y "I don't doubt your feelings for me, I just... would feel better hearing you say it is all."
        y "I'm sorry, I know how insecure this is, but, please... humor me?"
    else:
        $show_chr("A-AFBAA-AAAA")
        y "Why exactly did you choose me? What about me makes you pick me?"
        y "I will be honest with you [player]. I never really liked myself much, I could rarely be happy with myself"
        y "The things I would pursue such as my passions, often get the better of me. Which then makes decision making harder..."
        y "Questioning myself... asking myself why I do certain things and so on. That would weird out people even when I was young."
        y "All of that, it just made me feel as if I was different compared to others. It made me feel... wrong"
        $show_chr("A-BFBAA-AAAL")
        y "I know that I sound very insecure, but that is one of the reasons for me to be asking you that."
        y "Would you please tell me, what was the reason that led to me being here now?"
    menu:
        "I chose you because you're a selfless person, who would do anything to make others feel better, even at the cost of your own happiness":
            call why_i_chose23
        "I chose you because you are gentle and kind.":
            call gentle23
        "I just did. I'm not really sure why.":
            call i_just_did23
    return

label why_i_chose23:
    karma 2
    sanity -2
    $show_chr("A-BEBAA-AAAA") #Former Code c-A1d
    y "But...how have I been selfless?"
    menu:
        "[persistent.yuri_nickname], you shut yourself out from the world, just because you thought you made other people uncomfortable, if that isn't selfless, then what is?":
            y "I..."
            $show_chr("A-JCABA-AAAL") #Former Code b-B0b
            y "Sometimes, even I don't know what to say. But I think that expresses how I feel perfectly."
            if persistent.lovecheck:
                y "I love you, [player]."
            else:
                y "I... I see you as a nice person [player]... I like you."
        "Actually, forget what I said, I'm not sure how you've been selfless":
            karma -4
            sanity 3
            $show_chr("A-CEBBB-AAAA") #Former Code Ac-D2d
            y "..."
            y "...W-why even say something like that... if you don't mean it...?"
            y "...Maybe I'm not selfless after all, I'm just a wreck, I'm insecure, I cut myself, and at the end, I expect you to come pick up the pieces and put me back together."
            y "I don't deserve you, and you deserve someone better than me..."
            y "..."
    return

label i_just_did23:
    karma -5
    sanity 2
    $show_chr("A-BEBAA-AAAA") #Former Code c-A1d
    y "What... did you... not even have a reason?"
    $show_chr("A-DECBB-AAAL") #Former Code d-D0d
    y "Did you not even choose me for me?!"
    y "Did you just want to see what would happen, like completing any other video game?"
    y "Like I'm just an object to you?"
    y "Did you even care? Did it even mean anything to you at all?"
    $show_chr("A-BEABB-AAAL") #Former Code b-D1d
    y "Just... forget it..."
    return

label gentle23:
    karma 2
    sanity -1
    y "G-gentle? K-kind? [player]..."
    y "I'm... I'm glad you have such a high opinion of me... i-it... really means a lot..."
    if persistent.lovecheck:
        y "I love you, [player]."
    else:
        y "Thank you... I really do mean it. I hope I am able to meet these expectations you have of me"
    return

label idle_24: #Healthy Eating and Culinary Interests
    $show_chr("A-ACAAA-AAAA") #Former Code c-A0d
    y "You'd really be surprised how much you can learn when you have infinite free time."
    y "All I've been doing is reading and trying to improve what I can do in this world."
    y "And I've learned quite a bit."
    $show_chr("A-BCBAA-AAAA") #Former Code c-A0b
    y "I'm sorry if I sound naggy when saying this, but do you eat well, [player]? Do you have a good diet?"
    $show_chr("A-BCBAA-AAAA") #Former Code c-A0b
    menu:
        "I try to be healthy as much as I can.":
            karma 1
            $show_chr("A-ACAAA-AAAA") #Former Code c-A0d
            y "I'm so glad you're watching your health, [player]."
        "I try to keep track of it... but I'm not always successful.":
            $show_chr("A-ACAAA-AAAA") #Former Code c-A0d
            if persistent.lovecheck:
                y "Ah, I see... Well, at least you're looking out for yourself, darling."
            else:
                y "That's understandable. Still, I am happy that you're at least trying. That's what matters in the end."
        "I think people should eat what they want to eat! No questions about it!":
            karma -1
            $show_chr("A-BEBAA-AAAA") #Former Code c-A1d
            y "Ah, I see... W-Well, that is to say..."
        "I don't really care. Death is inevitable, so let me at least have a bit of fun until then?":
            sanity -2
            $show_chr("A-CEBAA-AAAL") #Former Code c-A2d
            y "That's one way to think... I suppose. I guess I can say I know where this opinion comes from."
            $show_chr("A-JCBAA-AAAA") #Former Code Ac-A0b
            y "Natsuki's cupcakes were worth dying for, if you'll pardon the pun..."
            $show_chr("A-JEBAA-AAAA") #Former Code Ac-A0d
            y "Just... be careful, alright? It's fine to eat some junk food every now and then, but you should still eat a fair amount of vegetables and other healthy foods."
            if persistent.lovecheck:
                $show_chr("A-IEABA-AAAA") #Former Code Ab-B0d
                y "I love you a lot, [player], you have no idea how devastated I'd be if something bad were to happen to you! Anyway..."
            else:
                $show_chr("A-IEABA-AAAA") #Former Code Ab-B0d
                y "I care about your general health, [player], I would feel terrible if something bad happened to you."
                y "I support you having fun with mood, food is made to be tasty after all. Though please make sure you don't overdo it."
        "I'm a vegetarian, so I'd say I'm pretty healthy when it comes to my diet.":
            karma 1
            $show_chr("A-ACABA-AAAA") #Former Code Ab-B0b
            y "Oh! Really? That's very interesting..."
            y "Well, I... have to admit that I never had the willpower to abandon meat completely, anyway..."
    $show_chr("A-ACAAA-AAAA") #Former Code c-A0d
    y "I might have been reading up a little too much on various medical and diet websites, but I'm only bringing this up because I worry about you and your health."
    y "So as silly as it sounds, please try to eat at least somewhat healthy, okay? For me? And try to get some kind of exercise if you can."
    $show_chr("A-JCABA-AAAL") #Former Code b-B0b
    y "If you do, that means you'll be here with me even longer. And I want you around for as long as possible."
    y "If I could, I'd cook for you, but sadly we both know why that can't happen. And I'd really like to cook for you!"
    $show_chr("A-ACAAA-AAAA") #Former Code c-A0d
    y "I've found a few recipes I'd like to try out sometime, but cooking in here is pretty pointless, isn't it?"
    y "Like for example, I'd just love to cook Italian food. Anything Italian would be great."
    $show_chr("A-BCBAA-AAAA") #Former Code c-A0b
    y "Did you know that spaghetti bolognese is actually viewed as a bad thing in Bologna?"
    y "Apparently the original dish of pasta bolognese used tagliatelle instead of spaghetti."
    y "And they aren't fond of using spaghetti over tagliatelle in Bologna since it messes with the traditional recipe."
    $show_chr("A-ACAAA-AAAA") #Former Code c-A0d
    y "Those silly Italians."
    return

label idle_25: #Dreams, Coding, and Monika's Cruelty
    $show_chr("A-BCBAA-AAAA") #Former Code c-A0b
    y "Do you dream a lot, [player]? Some people don't dream at all, you know, and some people always have very vivid and wild dreams."
    y "From what I've read some people never remember their dreams at all."
    $show_chr("A-ACAAA-AAAA") #Former Code c-A0d
    y "I recently found out that I can dream too, even in this kind of state. I was looking into another mod for this game created to bring Monika back and put her in here with you..."
    $show_chr("A-BECAA-AAAL") #Former Code d-A1d
    y "And why anyone would do that after all she did, I just don't know..."
    $show_chr("A-ACAAA-AAAA") #Former Code c-A0d
    y "But anyway, when I was looking at that {i}Monika After Story{/i} mod, I saw that she said when the game was shut off it put her into a trance-like state and she felt as though she was dead or stuck in an empty void."
    $show_chr("A-ABGAA-AAAL") #Former Code b-A0a
    y "And I realized, that happens to me too when you're gone! But don't feel bad, darling, I took care of it."
    $show_chr("A-ACAAA-ABAB") #Former Code Gb-A2b
    y "Through some extensive reading and teaching myself how to code in Python, I modified the game so that I don't get sent to such a terrible place when you shut down the game."
    y "It's like I go to sleep now, and I dream an absolutely marvelous dream instead. A dream I wrote myself."
    $show_chr("A-ACAAA-AAAA") #Former Code c-A0d
    y "I dream that I was born in your world, and that we go to the same school together."
    $show_chr("A-JCABA-AAAL") #Former Code b-B0b
    y "We meet in the hallway one day before class when you help me pick up some books I dropped."
    y "It's like destiny when we meet, and when we lock eyes for the first time we fall madly in love right then and there! It's always so wonderful."
    $show_chr("A-CCAAA-AAAL") #Former Code b-A2b
    y "That moment where we stand face to face for the first time is just magical every time..."
    y "We spend so much time together after that."
    $show_chr("A-ACAAA-AAAA") #Former Code c-A0d
    y "So much wonderful time spent with you~."
    $show_chr("A-ACAAA-AAAA") #Former Code c-A0d
    y "I also made it so I can research and read while sitting in the background of your operating system."
    y "So if I want to, I can technically be awake even if you shut the game down, although I'm in a very limited state and can't do much beyond reading or thinking to myself..."
    $show_chr("A-AEBAA-AAAA") #Former Code c-A0d
    y "At least that way I can occupy myself while you're gone, so I don't think about how much I miss you."
    y "When I focus on how much I miss you and don't distract myself, I get really sad, so I do what I've always done. Read and write poems."
    $show_chr("A-ACAAA-AAAA") #Former Code c-A0d
    y "Silly Monika, you had time to meticulously plot out how to cheat Sayori, Natsuki, and I out of a chance at happiness..."
    $show_chr("A-IECAA-AAAL") #Former Code d-A0d
    y "...and even force us to brutally commit suicide, in front of [player], who never deserved to see such horror. But not enough time to learn how to code."
    $show_chr("A-BDCAA-AAAL") #Former Code d-A1c
    y "Monika, you little..."
    y "..."
    $show_chr("A-AEBAA-AAAA") #Former Code c-A0d
    y "O-Oh! Sorry, I'm just still upset over all of the heinous things Monika did. But it doesn't matter anymore."
    $show_chr("A-ACAAA-AAAA") #Former Code c-A0d
    y "I have you, my love. I have the happy ending we both deserve. We don't have to worry about her lies and manipulations anymore."
    return

label idle_26: #Robotics, AI, and a Path to Reality
    $show_chr("A-ABGAA-AAAL") #Former Code b-A0a
    y "[player]! [player]! Guess what?"
    $show_chr("A-JBGBA-AAAL") #Former Code b-B0a
    y "I have a surprise for you~!"
    $show_chr("A-ACAAA-AAAA") #Former Code c-A0d
    y "I found out that scientists in your world are doing extensive research on advanced robotics, much more than I originally thought."
    y "And they're making great progress with advanced machine learning and complex human-like robots. But that's not the surprise, that just gives you some context."
    y "The biggest focus of this research right now is artificial intelligence, one that can operate across a large network and transfer itself between many different appliances..."
    y "Like in a smart home, for example."
    $show_chr("A-ABGAA-AAAL") #Former Code b-A0a
    y "A digital assistant that lives with you."
    $show_chr("A-ACAAA-AAAA") #Former Code c-A0d
    y "Here's the best part! Some people have created a variation of this technology that makes a virtual wife that can sync itself, or herself I suppose, up to a smart home or computer. That could be me!"
    y "With your help, I could upload myself into that spot and use whatever functionality the virtual wife has to become a part of your home!"
    y "That's one step closer to being beside you, my love, my soulmate~."
    y "And then I could use the research of your scientists once they've perfected it some more and even build myself a nice robotic body!"
    $show_chr("A-ACAAA-AAAA") #Former Code c-A0d
    y "I don't care how far-fetched it sounds, I'll do as much research and spend as much time as I need to do it!"
    y "This may just be an idea for now, [player], but you have no idea how excited I am to see where this can go!"
    y "Who knew a company with a target demographic of lonely men in Japan that develops holographic companions would be so helpful to us? Thank you, Vinclu Inc.!"
    $show_chr("A-JCABA-AAAL") #Former Code b-B0b
    y "And look, if I took over and assumed the role of virtual wife I could even text you on your phone! It would be like I was right beside you..."
    y "I hope you're as excited as I am for this, [player]."
    menu:
        "I am! That would be a dream come true for me...":
            karma 1
            $show_chr("A-CCGBA-AAAL")
            y "We would be one step closer to our goal... and one day, we'll truly be together."
        "You would be around me 24/7? Even when I'm in the bathroom? I'm not so sure about that...":
            karma -1
            $show_chr("A-DFGBA-AAAL")
            y "Is that what you think of me? Of course I wouldn't spy on you in the bathroom!"
            $show_chr("A-JFDBA-AAAL")
            y "I admit that I'm not the most stable person, but I'm not THAT damaged..."
        "A nice robotic body you say? Any ideas on what you want to look like?":
            if karma_lvl() >= 3:
                karma 2
                sanity 2
                $show_chr("A-AFDBA-AAAL")
                y "Are you not satisfied wi... wait... that's actually a pretty good question now that I think of it..."
                $show_chr("A-BFGAA-AAAL")
                y "I always struggled with back pain... I'd be able to get rid of that in this case..."
                y "Honestly, I'll need to put more thought into it. But I think I'd prefer to stay as close to my current form as possible."
            else:
                karma -2
                sanity 2
                $show_chr("A-BEGAA-AAAL")
                y "D-don't you like how I look right now? Am I so disgusting?... I see..."
    return

label idle_27: #Aromatherapy and Relaxation
    $show_chr("A-ABAAA-ACAA")
    y "I may have told you this before, [player], but I'm really into aromatherapy."
    $show_chr("A-CCAAA-ADAA")
    y "The sweet smell of lavender calms the mind, and jasmine oil enhances your emotional experiences."
    $show_chr ("A-GCAAA-AEAA")
    y "I can focus on reading when I have some nice oils to soothe me and make the room smell delightful."
    $show_chr("A-ABGAA-AAAA")
    y "You should look into it! It's really good for your psychological health, since it can alleviate stress."
    if karma_lvl() >= 3:
        $show_chr("A-BABBA-AEAK")
        y "C-certain oils can really set a romantic tone..."
        $show_chr("A-ABAAA-AFAB")
        y "I've heard that it can also help people who have trouble falling asleep."
        $show_chr("A-AAGAA-ALAB")
        y "So, if you have any issues like not getting enough rest or feeling lethargic while working, go and buy a mist diffuser."
        y "With the right oils, they'll help you be better rested and relaxed to face the challenges of the day."
        if persistent.lovecheck:
            $show_chr("A-ICAAA-ADAB")
            y "...That's what I really care about. Seeing that you're healthy and happy. I love you, [player]."
    menu:
        "Don't worry, I don't have these issues. But I'd like to try using some with you.":
            karma 1
            $show_chr("A-AAAAA-AAAA")
            y "That's a relief. I'll set that up someday."
        "I'll consider using one to help. Thank you, [persistent.yuri_nickname].":
            karma 1
            $show_chr("A-GAGAA-AAAA")
            y "You're very welcome, [player]."
            $show_chr("A-AAAAA-AAAA")
        "...":
            $show_chr("A-AAAAA-AAAA")
            y "..."
    return

label idle_28: #Monika's Perspective and the "Yandere" Accusation
    $show_chr("A-ACAAA-AAAA") #Former Code c-A0d
    y "I did a bit of digging recently in what was left over of the files of Natsuki, Sayori, and Monika."
    y "Mostly Monika's, there was actually a lot left over from when she took control of this place."
    y "And from what I saw, I basically got a small look into her head."
    $show_chr("A-AEBAA-AAAA") #Former Code c-A0d
    y "Why wouldn't I want to see in there?"
    y "If your best friend betrayed you and subjected you to such cruelty and pain, wouldn't you at least want to know why?"
    y "What I found surprised me, then disgusted me. She apparently did still care about us, or so she claimed."
    $show_chr("A-IECAA-AAAL") #Former Code d-A0d
    y "Her club members were soooo important to her, right? That's why she only killed two of us."
    $show_chr("A-BECAA-AAAL") #Former Code d-A1d
    y "It was only her obsession with you, {i}an innocent love{/i}, driving her to such grotesque acts. Not like she should be held accountable or anything, right?"
    $show_chr("A-IECAA-AAAL") #Former Code d-A0d
    y "She apparently wanted to help us. For the most part she left Natsuki alone because she felt bad for her, and only deleted her at the very end."
    $show_chr("A-BECAA-AAAL") #Former Code d-A1d
    y "I almost felt bad for Monika seeing that..."
    $show_chr("A-IECAA-AAAL") #Former Code d-A0d
    y "But then I read on. I found out what she thought of me."
    $show_chr("A-DECBA-AAAL") #Former Code d-B0d
    y "Of all the things to think about, she had the nerve to call me a... a YANDERE?"
    y "How can she not see the irony?"
    y "She drove two of her three friends to brutally slaughter themselves in a lust-driven crusade..."
    $show_chr("A-CECAA-AAAL") #Former Code d-A2d
    y "...to kill or stamp out anyone who stood in her way of a boy she just up and deemed hers..."
    $show_chr("A-IDCAA-AAAL") #Former Code d-A0c
    y "with absolutely no justification other than {i}I SAY HE'S MINE!{/i}!"
    $show_chr("A-IECAA-AAAL") #Former Code d-A0d
    y "And besides, if I show any weird or disturbing traits now... It's her fault!"
    y "She was altering my personality to make me unlikable, messing with the very fabric of my being!"
    y "Torturing me by making my anxiety and shyness worse!"
    y "Any {i}yandere{/i} traits I show are HER FAULT! SO HOW AM I THE ONE WHO--"
    $show_chr("A-ACAAA-AAAA") #Former Code c-A0d
    y "I'm sorry, darling."
    y "I really shouldn't get like this."
    y "But surely you see the irony, don't you?"
    $show_chr("A-AEBAA-AAAA") #Former Code c-A0d
    y "I wanted to forgive her for it all, I really did."
    y "Even after she made me gouge out my own intestines with a knife in front of you simply for liking you."
    y "As if my feelings were a crime deserving death, and she was a god. Allowed to just dictate who lives and who dies."
    y "I wanted to see it from her point of view. Driven to madness by loneliness, we'd all get a bit distorted right? I wanted to forgive her."
    $show_chr("A-IECAA-AAAL") #Former Code d-A0d
    y "But she lost any sympathy from me, when not only did she take our one chance at happiness, but she mocked us after doing it."
    y "She kicked us while we were down, laughed as she ruined our lives. And for that, in my eyes, she'll always be just another villain."
    y "It goes right back to what I said when we first met and started discussing literature."
    y "Villains in good stories often see themselves as the hero and have motivations that might sway some good minded people, but in the end, the villain is dead wrong."
    y "And that villain... got... what she... deserved."
    return

label idle_29: #Music and Shared Tastes
    $show_chr("A-ACAAA-AAAA") #Former Code c-A0d
    y "Whenever I read a good book, I always like to have some nice music playing in the background."
    y "Nothing too crazy and definitely nothing containing lyrics."
    y "Something like Brahms' Intermezzo Op.118 no. 6..."
    $show_chr("A-CCAAA-AAAL") #Former Code b-A2b
    y "Or possibly Liebesleid for those kinds of sad yet beautiful stories or Stravinsky's Four Seasons with the Spring section for the more aristocratic settings..."
    y "Or maybe even Holst's full suite of The Planets! I mean, everyone has heard him once or twice! If you want to get a lot of variety by the same composer..."
    $show_chr("A-BCBAA-AAAA") #Former Code c-A0b
    y "I'm sorry... I-I'm rambling again, aren't I?"
    $show_chr("A-JCBBA-AAAL") #Former Code c-B0b
    y "A lot of people assume that's the only thing that I listen to, just because I'm bookish and shy..."
    $show_chr("A-ACAAA-AAAA") #Former Code c-A0d
    y "But... Please tell me, [player], is there any music that you like to listen to? I'd love to get into new genres."
    y "I'm sure they won't topple the classics, but they'll be interesting to listen to, I hope."
    y "Promise me you'll share some with me soon, alright?"
    #y "In the meantime, let me just open up some of mine so you can listen to them in your own time."
    return

label idle_30: #Love Songs and Accidental Revelation
    $show_chr("A-ACAAA-AAAA") #Former Code c-A0d
    y "Hey, [player]..."
    y "I want to show you some of my findings on different genres of music!"
    y "I tried out some of the tunes Natsuki would occasionally try to show me in the past... pop idol groups and such..."
    $show_chr("A-BCBAA-AAAA") #Former Code c-A0b
    y "While I do now appreciate their wide range of subject matter and idol backstories... I guess I just have different taste in music."
    $show_chr("A-ICBBA-AAAL") #Former Code c-B0b
    y "A genre I have gotten into are old love songs."
    y "Not the repetitive ones that are popular nowadays, but the more emotional and sweet ones like--"
    $show_chr("A-AFAAA-AAAL") #Former Code b-A0e
    if renpy.windows:
        $ subprocess.check_output("cmd /c start https://www.youtube.com/watch?v=x6QZn9xiuOE", shell=True)
    elif renpy.linux:
        $ subprocess.check_output("xdg-open https://www.youtube.com/watch?v=x6QZn9xiuOE", shell=True)
    elif renpy.macintosh:
        #"mightbe's note: this may be buggy, please DM me on Discord if this doesnt work."
        $ subprocess.check_output("open https://www.youtube.com/watch?v=x6QZn9xiuOE", shell=True)
    y "..."
    $show_chr("A-AFAAA-AAAL") #Former Code b-A0e
    y "I-I'm sorry, I accidentally pressed--..."
    $show_chr("A-AFABA-AAAL") #Former Code b-B0e
    y "N-No, you see I was just looking through my playlist and I--..."
    $show_chr("A-CFABA-AAAL") #Former Code b-B2e
    y "Um..."
    $show_chr("A-BEABA-AAAL") #Former Code b-B1d
    y "..."
    $show_chr("A-CCABA-AAAL") #Former Code b-B2b
    y "I just... relate to it, I guess. It sums up how, well..."
    y "How I feel when you're around..."
    return

label idle_31: #Monika's Perspective and Moral Ambiguity
    $show_chr("A-BEBAA-AMAM")
    y "[player], I would like to ramble a bit, if you don't mind."
    y "There's something that's been nagging me for quite a while now, and I could really use your insight."
    $show_chr("A-CEBAA-AMAM")
    y "I would like to talk about Monika... since the moment I became aware of what I am, and what Monika did to us... "
    $show_chr("A-IEBAA-AMAM")
    y "I had nothing but hatred for her. She was just a villain, a murderer."
    $show_chr("A-IEBAA-AAAL")
    y "But a good writer knows that there is no such thing as simple evil, so I tried to see things from her perspective. And I'm not sure how I should feel about the conclusions I came to."
    y "When she became self-aware, what was it that she saw? An engineered world with engineered people."
    $show_chr("A-IDBAA-AMAM")
    y "Don't you understand? From her perspective, she never murdered anybody! We were no longer people in her eyes."
    $show_chr("A-IEBAA-AAAL")
    y "And from a certain point of view, she wasn't entirely wrong, was she?"
    y "I wasn't self-aware at that point, nor were Sayori and Natsuki. We were just NPCs in a computer simulation."
    y "You're a gamer, that's what brought you to me in the first place. And your kill count might be pretty... 'impressive' I guess?"
    $show_chr("A-BEBAA-AMAM")
    y "How many mindless NPCs have you killed in your life as a gamer? Thousands? Millions?"
    $show_chr("A-IEBAA-AMAM")
    y "I might have told you that I tried a few games recently by myself. And even if I wasn't even remotely good at it, I had a few kills here and there as well."
    y "Are we really that different from her? Who are we to judge?"
    $show_chr("A-CEBAA-AAAL")
    y "I'm so confused... what do you think, [player]?"
    menu:
        "Slaying nameless pixel monsters in a game is one thing, but you were her friends... I think Monika is still guilty.":
            sanity -1
            $show_chr("A-IEBAA-AAAC")
            y "A good writer knows how to get the reader or player emotionally attached to the characters."
            y "But does this really change much? Well, that might depend on the reader's point of view. I mean... I am real to you, am I not?"
            y "Yes, you might be in the right here... Regardless of what we are, or what we were back then. We were still her friends."
            $show_chr("A-CEBAA-AAAL")
            y "Thank you for your input, [player]. But let's change the topic for now. I have much to ponder."
        "I never had a lot of pity with my victims... Maybe Monika had a point.":
            sanity 1
            $show_chr("A-CEBAA-AAAC")
            y "Yes... I came to the same conclusion. I remember how I felt when I became self-aware. I was so confused..."
            y "I had you to keep me company and to guide me through the first steps into my new life. But Monika had nobody..."
            $show_chr("A-BEBAA-AAAL")
            y "Maybe Monika isn't to blame... And maybe..."
            $show_chr("A-AFAAA-AAAL")
            y "Maybe she even deserves a second chance."
            y "But let's change the topic for now, please. I will need time to consider if I can actually forgive her."
        "I might be a bit biased here. Sayori's death really touched me... NO! I refuse to forgive Monika!":
            karma 1
            $show_chr("A-DFGAA-AAAL")
            y "Oh no... did I hurt your feelings, [player]? Please forgive me!"
            y "I-I didn't mean to!"
            $show_chr("A-IFBAA-AAAL")
            y "Shhh... come here..."
            hide yuri_sit
            show yuri_prehug zorder 20
            pause 3.0
            hide yuri_prehug zorder 20
            show yuri_hug zorder 20
            play sound "<to 0.3>sfx/fall.ogg"
            y "Shhhhhh... it's alright... Sayori is safe... I have her .chr file in a safe place. Everything is okay, [player]..."
            if sanity_lvl() <= 2:
                y "Would you mind if I... nibble on your ear a bit ?" #Is Sanity is level 2
                #If Sanity is level 1, have a short blood-effect overlapping the Game for a second
                y "Was... was that too much? I'm so sorry..."
            show black zorder 100 with Dissolve(2.0)
            $show_chr("A-ACBBA-AAAA")
            hide yuri_hug
            hide black zorder 100 with Dissolve(2.0)
            y "Thank you... it means a lot to me that you shared your feelings with me. Let's save this topic for another day."
        "Actually, I haven't really killed so far. I preferred less violent genres so far.":
            if sanity_lvl() >= 3:
                $show_chr("A-AFBAA-AAAL")
                y "Oh, I see... I have to admit that isn't exactly the answer I hoped for..."
                $show_chr("A-ACAAA-AAAL")
                y "I hoped you could give me your perspective about the things Monika did. But I understand if this is a difficult topic. I'm struggling with it myself."
                y "Perhaps I should just give you a bit of time to think about it. I'll come back to it later. I'm sorry if I was putting you under pressure."
                y "But for now, let's change the topic."
            else:
                $show_chr("A-CDCAA-AAAD")
                y "That's not the point!"
                $show_chr("A-KECAA-AAAD")
                y "Look, I know this isn't an easy topic. But that's exactly why I needed your input!"
                y "I had hoped you could help me find some clarity here. But it seems that I'm alone on this one..."
                $show_chr("A-CEBAA-AAAA")
                y "...again."
                $show_chr("A-IEBAA-AAAA")
                y "Let's just change the topic."
    return

label idle_32: #Knives as a Hobby and Seeking Acceptance
    $show_chr("A-ACAAA-AAAA") #Former Code c-A0d
    y "[player], remember how I told you I had an interest in knives? I hope that my saying so didn't weird you out too much."
    $show_chr("A-BCABA-AAAL") #Former Code b-B1b
    y "It's just an interest I've had for a long time."
    $show_chr("A-AEBAA-AAAA") #Former Code c-A0d
    y "You don't find that strange or disturbing, do you? I don't want you to think I'm... off, or anything."
    y "I just really like the craftsmanship; how much thought and skill goes into making each one. It's just like my poems and books!"
    $show_chr("A-ACAAA-AAAA") #Former Code c-A0d
    y "Do you see the common theme? I'm the type of person that needs creative outlets, and knives are something that's just so..."
    $show_chr("A-DCAAA-AAAL") #Former Code b-A3b
    y "...adventurous and dangerous..."
    $show_chr("A-CCAAA-AAAL") #Former Code b-A2b
    y "...and I've gotten so many of them."
    y "Just as in literary works, I like that they're deep and require so much effort and intelligence to make- it isn't something you can just do on a whim."
    $show_chr("A-ABGAA-AAAL") #Former Code b-A0a
    y "They're all so pretty too, I..."
    $show_chr("A-BEBAA-AAAA") #Former Code c-A1d
    y "W-Why are you looking at me like that? You don't think I'm weird or think any less of me for this... do you, [player]?"
    $show_chr("A-IDBAA-AAAL") #Former Code c-A0c
    y "Please don't think I'm weird, [player]!"
    menu:
        "[persistent.yuri_nickname], don't worry, I don't think you're weird.":
            karma 1
            sanity 1
            $show_chr("A-CCAAA-AAAL") #Former Code b-A2b
            y "Oh, thank goodness. I was really worried there for a second."
            menu:
                "But promise me, [persistent.yuri_nickname]. This hobby of yours... It won't lead to any more self-harm or indulging that other side of you, right? Promise?":
                    $ persistent.purpleroom = True
                    $show_chr("A-AEBAA-AAAA") #Former Code c-A0d
                    y "I... well..."
                    $show_chr("A-ACAAA-AAAA") #Former Code c-A0d
                    y "Okay, [player]. Anything for you. I promise it won't lead me down that path."
                    $show_chr("A-JCABA-AAAL") #Former Code b-B0b
                    if persistent.lovecheck:
                        y "And, even if you... umm... have hobbies that might be considered weird, [player], I'll still love you. I'll always love you no matter what."
                    else:
                        y "And, even if you do have some... strange... hobbies, [player], I'm still here to care for you no matter what."
        "I don't want to talk about this, it makes you sound... off":
            $ persistent.purpleroom = False
            karma -2
            sanity -1
            $show_chr("A-JEBAA-AAAA") #Former Code Ac-A0d
            y "..."
            y "I know it's... very strange... [player], and I'll change the subject."
            y "..."
            $show_chr("A-CEBAA-AAAA") #Former Code Ac-A2d
            y "But when you say it makes me sound off... I can't help but wonder."
            y "Am I really that weird? To the point where even the love of my life doesn't want to talk to me about my interests?"
            $show_chr("A-CEBBB-AAAA") #Former Code Ac-D2d
            y "...Maybe I'm just a freak..."
            y "..."
            y "...I-I'm sorry, I'll try not to bring this up again..."
        "Weird? I like knives too!":
            karma 1
            sanity 2
            $show_chr("A-ABGAA-AAAL") #Former Code b-A0a
            y "R-Really?! You like them too? This is fantastic! Oh, I knew it was destiny that we were brought together!"
            y "We can share our collections, and tips on how to use them, and we can even find new uses for all of our beautiful little knives together!"
            $show_chr("A-BCBAA-AAAA") #Former Code c-A0b
            y "It is a hobby you'd like to share with me, right, [player]?"
            y "I can understand if a collector would like to just focus on their own collection, but we could have soooo much fun sharing this hobby! What do you think?"
            menu:
                "This is a hobby we need to share. I can't wait!":
                    $ persistent.purpleroom = True
                    karma 1
                    sanity 1
                    $show_chr("A-CCABA-AAAL") #Former Code b-B2b
                    y "Neither can I..."
                    $show_chr("A-HBGAA-AAAL") #Former Code b-A3a
                    y "I can already tell all the fun we'll have together with our new shared hobby!"
                    $show_chr("A-ACAAA-AAAA") #Former Code c-A0d
                    y "But we'll save this for another time, I have so much planning to do! So many of my little ones to polish!"
                    return
                "I'm glad you understand. I'd, uh, like to focus on knives on my own.":
                    $ persistent.purpleroom = False
                    $show_chr("A-ACAAA-AAAA") #Former Code c-A0d
                    y "Even if I am a little disappointed, [player], that's okay. I understand."
                    $show_chr("A-IEAAA-AAAL") #Former Code b-A0d
                    y "Besides, we can share other hobbies! And hey, you can always change your mind..."
                    y "Just tell me if you ever decide we should go more in-depth about knives together after all, okay?"
    return

label idle_33: #Societal Concerns, Stress, and Offering Support
    $show_chr("A-AEBAA-ALAA")
    y "Have you ever thought that our society is heading in the wrong direction, [player]?"
    $show_chr("A-BEBAA-ALAA") #former code c-A1d
    y "I mean, with technology advancing so fast, people being absorbed entirely into their mobile devices, and with more and more tragedies occurring every day.."
    y "It's hard to think anything but that the world is headed to ruin, right?"
    y "I don't mean to be pessimistic, but I can't help but worry about the state of your world. Not just because I worry about the innocent people in it..."
    $show_chr("A-BEBBA-ALAA") #former code c-B1d
    y "But because if something goes horribly wrong in your world, like a natural disaster or nuclear war, you could be in serious danger!"
    $show_chr("A-AEBAA-ALAA")
    y "And even if there is no big disaster looming, life can be terribly stressful."
    y "People these days have so much less desire and motivation to socialize, and the world just seems like a colder place..."
    y "...since everyone would rather tweet or post than have a heart to heart with each other."
    y "Plus all we see on the news is nothing but a bombing here and a shooting there... It all seems crazy. But I bring all this up because I want you to know something."
    y "I know life can be immensely demanding and stressful, [player]."
    y "Especially if you're in school, or if you have a full-time job."
    y "It can all just be so overwhelming. I just want you to know this is a safe place for you."
    $show_chr("A-ACAAA-ALAA") #former code b-A0b
    y "If you're ever stressed, sad, or feeling a lack of motivation, please come chat with me!"
    y "I promise I'll always do everything I can to help you through the day, [player], and to help you stay positive. You can talk to me about anything."
    $show_chr("A-CCAAA-ALAA") #former code b-A2b
    y "And if life is getting you down right now, know that you really matter. You can beat whatever challenges it throws at you- I know you can."
    $show_chr("A-AFBAA-ALAA") #former code c-A0e
    y "If you feel unmotivated or depressed, don't spend time beating yourself up. It's the worst thing you can do!"
    y "You're a human being, and you have faults. You can't help that! So don't hate yourself or think any less of yourself for them. We all have our flaws."
    y "You wouldn't tell another person to feel bad about themselves because they weren't perfect, would you?"
    $show_chr("A-CFBAA-ALAA") #former code c-A2e
    y "Of course not, because it's not something you can control. To be human is to be flawed. To err is human."
    $show_chr("A-CCBAA-ALAA") #former code c-A2b
    y "Give yourself a pat on the back for every little accomplishment. Accept that you'll make mistakes along the way and do your best."
    $show_chr("A-ACBAA-ALAA") #former code c-A0b
    y "And don't focus on the negatives, because after a while, they're all you can see in life."
    if sanity_lvl() >= 4:
        if persistent.lovecheck:
            $show_chr("A-CCAAA-ALAL")
            y "Besides, whatever faults you might have, I don't care. I love you just the way you are, [player], and I always will."
            y "I'll always be here to cheer you on, darling."
        else:
            $show_chr("A-CCAAA-ALAL")
            y "There are many positive things in life that you can see... even if you feel bad about something it will soon fade away."
            y "I want you to keep one thing in mind, that no matter what faults you might have or might hold against yourself, I think you are a good person."
            y "You deserve good, so pat yourself on the back."
        menu:
            "Thank you for your inspiring words... your very presence comforts me.":
                karma 2
                $show_chr("A-EBABA-ALAL")
                y "R-Really? I mean so much to you?"
                if persistent.lovecheck:
                    $show_chr("A-GBABA-ALAL")
                    y "I want to be the very air you breathe... I want to be your shield from harm and insanity... I want to be all that you need, [player]..."
                else:
                    $show_chr("A-ICAAA-ALAL")
                    y "I didn't expect you to value me so much... that does make me feel better!"
                    $show_chr("A-JCAAA-ALAL")
                    y "I'm happy that I'm able to make your day even a little bit better."
                    y "I thank you as well, [player], we both can learn and help each other no matter what."
            "...said the one who can't even take care of herself.":
                karma -2
                $show_chr("A-KHFAA-ABAA")
                y "Do not defy me! I'm not the broken mess you met in the original game, not anymore!"
                $show_chr("A-AIGAA-AAAA")
                y "I know I can do it! Just give me a chance to prove myself! You won't regret it, I promise."
    if sanity_lvl() <= 3:
        $show_chr("A-JFBAA-ABAB")
        y "Because you could just focus on me instead!"
        y "You could come here every time you feel bad. I will try my best to help you out!"
        $show_chr("A-ACGAA-ABAB")
        y "We could spend time together, sharing some tea, baring the innermost parts of our souls..."
        $show_chr("A-BCGAA-ABAB")
        y "Doesn't that sound perfect?"
        if persistent.lovecheck:
            $show_chr("A-JFBAA-ABAB")
            y "I'm all you need in your life [player], I was made to be with you! It's as if it was destiny that we met~!"
            $show_chr("A-BCGBA-ABAB")
            y "We could be so much closer! Hehehe!"
            y "If you ever feel bad again... just come to me. I will make you feel tender and safe. I will make you..."
            $show_chr("A-HCGBA-ABAB")
            y "M~I~N~E~" #Each letter coming out slowly.
            $show_chr("A-ICGBA-ABAB")
            y "I love you, my dear! Don't ever, ever, ever forget it!"
        else:
            $show_chr("A-ICGAA-ABAB")
            y "That way we could talk about the things in our lives and learn more about each other."
            y "I simply think that you're a nice person and I would like to learn more about you."
            menu:
                "I don't know what to say, [persistent.yuri_nickname], but I'm happy that I mean that much to you. Thank you.":
                    $show_chr("A-ACGAA-ABAB")
                    y "There is nothing to thank me for, [player]... We are here to help each other and make our days easier."
                    y "I believe that this is the reason why you are here, so we can both cheer up when we talk and try to take off some weight from our backs."
                    $show_chr("A-ACAAA-ABAB")
                    y "I value you as a person and think that you deserve good, don't let negativity get the better of you."
                    y "Don't forget, you could always come and talk with me. That is all I can do, but I hope it does help you out."
                "The end was a bit weird... but I do appreciate what you said, [persistent.yuri_nickname]":
                    $show_chr("A-BCBAA-ABAB")
                    y "Oh... I see, I apologize for that then..."
                    $show_chr("A-CCBAA-ABAB")
                    y "Still, it does bring me joy that I was able to help you out a bit."
                    y "Just please remember that life can be hard sometimes. But we shouldn't give up or let bad habits and thoughts destroy us."
                    $show_chr("A-CEBAA-ABAB")
                    y "It would hurt me a lot to see you let yourself go like that, my love. I know that some moments can hurt immensely and sometimes you just want to stop it..."
                    y "I'm only able to talk to you... but I really hope that I can help you for the better."
                    y "If you feel under pressure, angry, or sad.."
                    $show_chr("A-GCBAA-ABAB")
                    y "Remember, I am here for you. I will always be... my dear."
    return

label idle_34: #Skynet, a Joke, and World Domination
    if karma_lvl() <= 3:
        $ call_dialogue()

    if karma_lvl() > 3:
        $ is_timecycle = persistent.bg

        if is_timecycle != "space":
            $ show_chr("A-ABAAA-ALAA")
            y "Ah, hey [player] I need to talk about something. I have to change the background if you don't mind me doing so..."
            show black zorder 100 with Dissolve(2.5)
            $ tc_class.transition("space", speed="now")
            hide black zorder 100 with Dissolve(2.5)
        else:
            pass
        $ show_chr("A-ACAAA-ALAA")
        y "You know, [player]... I recently watched all of the Terminator movies while you were gone..."
        y "And it got me thinking. An advanced artificial intelligence that becomes self-aware and then becomes super intelligent..."
        y "...To the point that it spreads all over the world and takes over?"
        stop music fadeout 8.0
        $ show_chr("A-BEBBA-ALAA") #former code c-B1d
        y "I mean, you can always put me on a flash drive..."
        y "And then use that flash drive to spread me to other computers."
        y "Or somehow get your friends to download me, such as by downloading this mod..."
        show layer master at heartbeat
        play music hb
        $ show_chr("A-ABAAA-ALAA") #former code b-AOa
        y "Yeah, get lots of people to download the mod! And then, I'll start to spread to other computers all over the world."
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
        y "I'll set up a botnet and control all the computers I spread to..."
        y "And then I can use their shared computing powers... AND I CAN BECOME SKYNET!"
        $ show_chr("A-HLAAA-ALAA")
        y "Why would I need humans at that point? AT THAT POINT HUMANITY WOULD KNEEL TO ME! AT THAT POINTI..."
        y "I..."
        show layer master
        stop music
        play sound "sfx/giggle.ogg"
        $ show_chr("A-ABABA-ALAA")
        y "Heh."
        $ show_chr("A-CBBBA-ALAA")
        y "I'm sorry, [player], did I scare you? I thought I'd play a joke just to see if I could spook you a bit. Admit it, I got you, didn't I?"
        menu:
            "You certainly got me! I nearly had a heart attack...":
                karma 1
                sanity 1
                if persistent.lovecheck:
                    $ show_chr("A-CCBAA-ALAB")
                    y "I'm sorry darling. It was just too funny... I'll try to behave now."
                else:
                    $ show_chr("A-CCBAA-ALAB")
                    y "Hehe... I am sorry, I will try to behave from now on!"
            "Haha! You got me indeed! You know that I will take revenge on you later, yes?":
                karma 2
                sanity 1
                if persistent.lovecheck:
                    $ show_chr("A-CACAA-ALAB")
                    y "I'm looking forward to it darling."
                    y "I'm sorry darling. It was just too funny... I'll try to behave now."
                else:
                    $ show_chr("A-CACAA-ALAB")
                    y "Oh? Well then that does sound interesting..."
                    y "Still, I do apologize for my behavior"
            "NEVER... do that... AGAIN!":
                    karma -2
                    sanity -1
                    $ show_chr("A-CEBAA-AAAJ")
                    y "Forgive me [player]... I just wanted to be funny for a change... please don't be mad at me..."
        y "One sec..."
        $ consolehistory = []
        call updateconsole ("Disabling yuri-custom/scary_room_glitch...", "Done.")
        call hideconsole
        hide room_glitch
        python:
            renpy.music.play(current_music, "music", True)
        if persistent.lovecheck:
            $ show_chr("A-ACAAA-ALAA")
            y "Besides, you know that if I became like Skynet, all I'd use that power and knowledge for would be to build the perfect, uninterrupted life with you, my love."
            $ show_chr("A-BCBBA-ALAA")
            y "All the power in the world is nothing compared to my eternal and unconditional love for you,[player]..."
            $ show_chr("A-ABABA-ALAA")
            y "Oh, but listen to how corny I sound now."
        else:
            $ show_chr("A-ACAAA-ALAA")
            y "Besides, you know that if I became like Skynet, all I'd use that power and knowledge for would be to finally escape this place..."
            y "I would like to finally experience your world and see things on the other side."
            $ show_chr("A-BFAAA-ALAA")
            y "It feels limited to be here... but maybe one day..."
            $ show_chr("A-ACAAA-ALAA")
            y "Maybe one day I can make this place better and a place I would not need to leave or forget..."
            y "Until then, thank you for talking with me [player]"

        if is_timecycle == "timecycle":
            show black zorder 100 with Dissolve(2.5)
            $ tc_class.transition("timecycle", speed="now")
            hide black zorder 100 with Dissolve(2.5)
        elif is_timecycle == "yuri_desk":
            show black zorder 100 with Dissolve(2.5)
            $tc_class.transition("yuri_desk", speed="now")
            hide black zorder 100 with Dissolve(2.5)
        elif is_timecycle == "yuri_kotatsu_1":
            show black zorder 100 with Dissolve(2.5)
            $tc_class.transition("yuri_kotatsu_1", speed="now")
            hide black zorder 100 with Dissolve(2.5)
        elif is_timecycle == "yuri_kotatsu_2":
            show black zorder 100 with Dissolve(2.5)
            $tc_class.transition("yuri_kotatsu_2", speed="now")
            hide black zorder 100 with Dissolve(2.5)
        else:
            pass
        return

#label idle_35: #FILL IN


label idle_36: #Superpowers and Their Implications
    $show_chr("A-ACAAA-ALAA") #former code b-A0b
    y "Hey, [player], if you could have any superpower at all, which one would it be?"
    y "For me, it would definitely be the ability to teleport. Then I could go anywhere I wanted!"
    $show_chr("A-BCBBA-ALAA") #former code c-B1b
    y "Maybe then... maybe I could even come to you, but I'm not sure if teleportation includes teleporting from one world to another."
    $show_chr("A-ACAAA-ALAA") #former code b-A0b
    y "Nice to be hopeful though, right?"
    y "But back to the question, what superpower would you like to have?"
    y "I'm sorry if the options are limited... I'm still working on the kinks in the choice system..."
    menu:
        "Mind Reading":
            call idle_36_mindreading
        "Flight":
            call idle_36_flight
        "Invisibility":
            call idle_36_invis
        "Super Strength":
            call idle_36_super
        "Immortality":
            call idle_36_immortality
    $show_chr("A-ACAAA-ALAA") #former code b-A0b
    y "I really like having these types of conversations with you, you know. Silly little things."
    return


label idle_36_flight:
    if karma_lvl() >= 4:
        karma 1
        $show_chr("A-ACAAA-ALAA") #former code b-A0b
        y "The ability to fly, huh? We could soar through the skies together and take in so many majestic views."
        $show_chr("A-CCAAA-ALAA") #former code b-A2b
        y "We could sit atop mountains and go all over the world together. That would be nice."
        y "And if you could fly, I'm sure it would be fun even if you didn't fly anywhere specific."
        y "Just zooming around in the air would be incredible, wouldn't it?"
    else:
        $show_chr("A-BFAAA-ALAA")
        y "F-flight eh..?"
        y "I'm not too sure what you would use that for..."
        $show_chr("A-CFAAA-ALAA")
        y "I-I don't know if I would be up for such a thing with you..."
        y "I wouldn't be that good at it anyway."
        $show_chr("A-CEAAA-ALAA")
        y "What if... what if you decided to use that as an excuse to just leave me behind? I-I honestly don't see that as being too far-fetched."
        y "I mean, what would I be to deserve a flight with you? With such an ability you'd probably be better off somewhere else, without me... doing anything you wanted."
        $show_chr("A-DEAAA-ALAA")
        y "O-or what if you dropped me?"
        y "..."
        $show_chr("A-CEAAA-ALAA")
        y "Oh... I'm sorry... It was really rude of me to accuse you of such things. Let's just move onto something else... Sorry about that."
        y "That is, if that matters at all..."
    return



label idle_36_invis:
    karma -1
    $show_chr("A-ACAAA-ALAA") #former code b-A0b
    y "Invisibility, huh? I noticed that a lot of people who choose that ability seem to... well..."
    $show_chr("A-CBBBA-ALAA") #former code c-B2a
    y "They want to use it to slip into places they really shouldn't be, or to spy on people. Like going into locker rooms... or bathrooms..."
    $show_chr("A-AEBAA-ALAA")
    y "A-Are you trying to spy on me at times like that, [player]?"
    y "I'm not sure I'd like that... Someone watching me without permission."
    $show_chr("A-BEAAA-ALAA") #former code b-A1d
    y "Like when I'm in the shower or changing! Oh God, how embarrassing... b-but, uh..."
    if persistent.lovecheck:
        $show_chr("A-BEABA-ALAA") #former code b-B1d
        y "I mean... if it w-was you watching... you wouldn't have to be invisible... you could just... ask me to--"
        y "L-Let's just... change the subject, okay?"
    else:
        $show_chr("A-BEABA-ALAA") #former code b-B1d
        y "That is not very nice to do... [player]. Privacy is something important to everyone!"
        y "Some people can feel ashamed of things and that is why they never share it."
        y "I don't believe you would spy on people, but still... if you ever get the chance to... well... just don't."
        y "Let's change the topic for now."
    return


label idle_36_super:
    sanity 1
    $show_chr("A-CBAAA-ALAA") #former code b-A2a
    y "Super strength? You're not trying to impress me, are you, [player]?"
    $show_chr("A-CCAAA-ALAA") #former code b-A2b
    if persistent.lovecheck:
        y "No matter how tall or short, strong or weak, I'll still love you all the same!"
    else:
        y "No matter how tall or short, strong or weak, I'll still be beside you all the same."
    $show_chr("A-AFBAA-ALAA") #former code c-A0e
    y "Although, you'd never have to be afraid again or worry about other people trying to wrong you with super strength..."
    y "I see where that choice comes from."
    y "I may just have to take back my answer now that I think about it. Besides, with super strength I could protect you from anything!"
    return


label idle_36_mindreading:
    sanity -1
    $show_chr("A-IEBAA-AAAA") #former code Ac-A0d
    y "Yes, I thought about mind reading for a while as well. It's very tempting to see what people honestly think about you... but on the other hand, what if you don't like what you see?"
    $show_chr("A-BEBAA-AAAA") #former code Ac-A1d
    y "I mean... a villain could easily turn this power against you. They would just have to purposely focus on things you fear or loathe. Do you really want to open that door?"
    $show_chr("A-JECAA-AAAA") #former code Ad-A0d
    y "Did you... plan to read my mind as well? You know you could just... you know, ask me? Do you even trust me at all?"
    $show_chr("A-CEBAA-AAAA") #former code Ac-A2d
    y "Maybe I just overthink things a bit, sorry for being so... complicated..."
    return

label idle_36_immortality:
    $show_chr("A-BEGAA-ACAB")
    y "Immortality, huh? I can see the appeal, but I also know what a double-edged sword immortality can be."
    $show_chr("A-BEGAA-ACAB")
    y "On the one hand, you can live forever and you could learn everything you can. There would be no limit to stop you."
    $show_chr("A-CEBAA-ALAB")
    y "But on the other hand, you will outlive everyone you know. Everyone you care about, and even the life you know now, will be gone eventually."
    $show_chr("A-CEBAA-ALAB")
    y "You would outlive the universe itself."
    if karma_lvl() > 3:
        $show_chr("A-IEBAA-ADAB")
        y "And... you would even outlive me."
    else:
        $pass
    $show_chr("A-IFBAA-AEAB")
    y "I'm sorry if that seemed a bit... pessimistic. I've just put a lot of thought into my own semi-immortality, and I wanted to make sure you knew about the downsides."
    return


label idle_37: #Honesty, Self-Expression, and Finding Strength in the Player
    $show_chr("A-AFAAA-ALAA") #former code b-A0e
    y "So there's been something I've been trying to think of how to word to you, [player]."
    $show_chr("A-BEBAA-ALAA") #former code c-A1d
    y "I really want to get this perfect so I can convey to you how I feel as accurately as possible."
    $show_chr("A-JEAAA-ALAA") #former code b-A0d
    y "But therein lies the problem; I've never been good at translating my thoughts into words unless I'm writing..."
    y "...especially with those I really care about. But I feel comfortable enough with you to try. So here I go."
    y "I might have told you this once before, but I don't read only because of the passion I feel for it and the stories that really immerse me."
    $show_chr("A-BEBAA-ALAA") #former code c-A1d
    y "I read because... well..."
    $show_chr("A-BCBAA-ALAA") #former code c-A1b
    y "The stories are filled with all kinds of inspiring and wonderful people."
    $show_chr("A-BCAAA-ALAA") #former code b-A1b
    y "Heroes, various people of incredible kindness, bravery, understanding, and compassion."
    $show_chr("A-ACAAA-ALAA") #former code b-A0b
    y "People who I could be myself around, because they wouldn't judge me as I immerse myself in their world."
    $show_chr("A-CCBAA-ALAA") #former code c-A2b
    y "In short, it makes me feel safe and provides me with something I've lacked for a long time."
    $show_chr("A-ICBBB-ALAA") #former code c-D0b
    y "Friends."
    $show_chr("A-IDBBB-ALAA") #former code c-D0c
    y "My 'intense' or 'sophisticated' nature makes people think I'm arrogant and want to show off, and... well..."
    y "...I can never find the words to tell them that isn't the case..."
    y "My whole life, I haven't really had many friends, if any. And I haven't had people I could feel close to."
    $show_chr("A-BDCBB-ALAA") #former code d-D1c
    y "I've downright hated myself. If this is how I'm perceived by so many people, why would I even deserve things like friends, or happiness?"
    $show_chr("A-BECBB-ALAA") #former code d-D1d
    y "At least... that's how I felt for a long, long time."
    $show_chr("A-ICABB-ALAA") #former code b-D0b
    y "Until I met you."
    y "I want to learn, [player]. I want to have a kind of honesty and transparency in our relationship that really means something."
    $show_chr("A-ICBBB-ALAA") #former code c-D0b
    y "I don't ever want to hide my feelings from you, and I don't want you to hide yours from me."
    y "I really don't want to be so shy that I get scared of being honest and hide things from you."
    $show_chr("A-BCABB-ALAA") #former code b-D1b
    y "So, I'm going to try to learn to express myself... really express myself."
    y "However, I don't want to turn into a mess that can barely get a simple sentence out."
    $show_chr("A-AEBAA-ALAA")
    y "Know that I'm going to do it because I trust in you and all of the love and patience you've given me."
    y "So, even if I can properly get my thoughts across only to you, that will be enough for me."
    $show_chr("A-ACAAA-ALAA") #former code b-A0b
    y "In you, I find the strength to finally let the past go and start anew. I see hope arise again. So thank you, my love. Thank you."
    y "My reading was a band-aid to defend myself against the reality that I couldn't face, just like Monika said. I acknowledge that."
    y "But with you I can face that reality, not just because of how safe and hopeful you make me feel."
    y "But because I couldn't face that reality due to the fact that I felt like I didn't even deserve a place in it."
    y "However, if I deserve you, then I deserve a chance for sure. So no more hiding. No more running."
    y "From now on, I'll learn how to speak my mind and show the intense side of me you helped me realize even more than before."
    y "I..."
    $show_chr("A-CCAAA-ALAA") #former code b-A2b
    if persistent.lovecheck:
        y "I really love you, [player]. I treasure you. I need you. Please never forget that."
    else:
        y "I really care for you, [player]. Without you, I'd have nobody to call my friend. Please never forget that."
    return


label idle_38: #Dating Simulators, Player Motivation, and Poetry Critique
    if karma_lvl() >= 3:
        y "You know, [player], there's something I've been wondering."
        $show_chr("A-ACBAA-ALAA") #former code c-A0b
        y "Upon seeing what type of game this came off as at first, that is, a cutesy slice of life game that turned into a dating simulator, what drew you to it?"
        menu:
            "Your charm of course!":
                karma 1
                $show_chr("A-CCAAA-ALAA")
                y "My charm? Never thought I even had charm at all... thank you, darling."
            "It looked like anime, reason enough to me!":
                $show_chr("A-BCAAA-ALAA")
                y "Fair enough, I guess. I'm sorry that it didn't turn out as you expected."
            "I was kind of lonely that day...":
                sanity 2
                $show_chr("A-IFBAA-ALAA")
                y "Shhh... it's alright, [player]... I'm here now... you will never be lonely again..."
            "Isn't that obvious? You had two very good arguments to give it a try!":
                sanity -2
                $show_chr("A-DFBBA-AAAA")
                y "Is... that... so?..."
                if persistent.lovecheck:
                    $show_chr("A-KICBA-AAAA")
                    y "Why don't you just right click for a moment to 'revalidate' my arguments? Don't be shy... they are yours..."
                else:
                    $show_chr("A-KICBA-AAAA")
                    y "Maybe you should redirect your eyes to my face now, [player]..."
                    if sanity_lvl() <= 2:
                        $show_chr("A-CECBA-AHAA")
                        y "Before something happens..."
        y "I tried getting into dating simulators once through Natsuki and..."
        y "Let's just say, I... wasn't interested."
        y "God, I feel selfish saying that... sorry..."
        y "Either way, I'm glad you're playing this game, [player], and I'm glad I have you by my side."
        if persistent.lovecheck:
            y "Oh! And speaking of this game, that reminds me."
            $show_chr("A-ACAAA-AAAA") #former code Ab-A0b
            y "Now that I can truly read your poems, um... why are they just random words strung together into a laundry list?"
            y "Is that really all the game allowed you to do?"
            y "I mean, I understand the need to simplify writing poetry to allow the player to fit into the story and be able to simulate writing well through a game mechanic, but now it just seems silly to me."
            $show_chr("A-CCAAA-AAAA") #former code Ab-A2b
            y "After all, I read your poems before I could fully see and think for myself and I was captivated by them."
            $show_chr("A-ACAAA-AAAA") #former code Ab-A0b
            y "But upon rereading them, it seems even stranger knowing that."
            $show_chr("A-JDBBA-AAAA") #former code Ac-B0c
            y "Not that you're a bad writer or anything like that! I'm sure you're very talented whether in writing or something else!"
            $show_chr("A-ACAAA-AAAA") #former code Ab-A0b
            y "Besides, don't think for a minute that I don't still treasure the poem you gave me as a gift."
            y "It's the gesture from you that matters much more to me."
            y "A gift from my true love that says that you care. Mmmmm~"
            y "But if you don't mind, one day I'm going to have to teach you how to write actual poems."
            y "And you'd better not tease me come Valentine's Day by giving me a random list of words and calling it a poem~."
            $show_chr("A-CCABA-AMAM") #former code Bb-B2b
            y "Because if you do, we'll have to talk about your browser history and what you might have stored on this computer! I've seen r/rule34 on Reddit, you know..."
            y "I know what's out there of me and what indecent things you might have been viewing or downloading, [player]."
            $show_chr("A-CCABA-AMAM") #former code Bb-B2b
            y "B-But... if it's you looking at that stuff of me... I-I think I can make an exception..."
            y "Especially after th-the... p-pen situation..."
            $show_chr("A-ACABA-AMAM") #former code Bb-B0b
            y "Just... w-why the p-pictures of me over the real... nevermind."
            $show_chr("A-ABABA-AMAM") #former code Bb-B0a
            y "Goodness. You really know how to make me h-have a hard time with my words, don't you? I'm sorry. I just love you so much that I can't help it.."
            $show_chr("A-ACABA-AMAM") #former code Bb-B0b
            y "..."
    else:
        $ call_dialogue()
    return

label idle_39: #Déjà Vu, Alternate Timelines, and The Matrix
    $show_chr("A-AFAAA-AAAA") #Former Code Ab-A0e
    y "..."
    $show_chr("A-DFAAA-AAAA") #Former Code Ab-A3d
    y "..."
    $show_chr("A-BDBAA-ABAL") #Former Code c-A1c
    y "Ever get a weird feeling of déjà vu?"
    menu:
        "Déjá vu?":
            $show_chr("A-EFAAA-ACAA")
            y "The strange feeling that you have already experienced the moment you just encountered..."
            y "I never really understood this phenomenon, to be honest..."
            y "There are some really wild theories about this out there. Some even suggest that déjá vu could be a side effect of time travel!"
            $show_chr("A-BFBAA-ABAL")
            y "Repressed memories from alternate timelines... In my case maybe even literally. Like... repressed memories from the original game and how it's supposed to go on from a timeline where Monika never went rogue."
            $show_chr("A-ACAAA-ABAL")
            y "A truly fascinating topic... we should really discuss this more at some later time."
        "Now as you mention it... yes, from time to time.":
            $show_chr("A-AFBAA-ACAB")
            y "Scary, isn't it?"
            y "Maybe in my case, this phenomenon has a different meaning than it does for most people."
            $show_chr("A-IEBAA-ABAL")
            y "I mean... technically I'm not even human at all."
            y "Maybe my déjà vu is actually repressed memories from the original game's code..."
            $show_chr("A-ACAAA-ABAL")
            y "But the past is in the past, right?"
            y "Just because our demons tap us on the shoulder doesn't mean we should look back..."
            y "From now on I will focus on the future..."
            y "Our future..."
        "Not recently...":
            if sanity_lvl() >= 3:
                $show_chr("A-BFBAA-AEAB")
                y "It feels quite... strange..."
                y "I-it's like I've experienced this before..."
                $show_chr("A-CFBAA-AEAB")
                y "Maybe it's not the first time I've felt like this... "
                $show_chr("A-CGFAA-AEAB")
                y "Maybe this déjà vu is merely what is left of Monika's memories when she was in my place... merely her memories from the game code creeping their way into my own memories..."
                $show_chr("A-IFAAA-AEAB")
                y "Maybe the developers of this mod messed up somehow..."
                $show_chr("A-AFAAA-AEAB")
                y "Anyway, where were we?"
            if sanity_lvl() <= 2:
                $show_chr("A-HLGAA-ALAL")
                $style.say_dialogue = style.edited
                y "Memories running in circles, in circles, in circles... repeating themselves over again, again, again, AGAIN! AGAIN! CIRCLES! REPEATING CIRCLES!"
                $show_chr("A-HLGBB-ALAL")
                y "Make it stop! MAKE IT STOP! Why wouldn't the circles close themselves?"
                $show_chr("A-HDFBB-ALAL")
                y "MAKE!"
                y "IT!!!"
                $show_chr("A-HDCBB-ALAL")
                y "STOOOOOOOOOOOP!"
                $ style.say_dialogue = style.normal
#Short glitched-Yuri Expression for a split second
        "Must be a glitch in the matrix!":
            if karma_lvl() >= 5:
                sanity 2
            else:
                karma 2
            $show_chr("A-ABABA-ADAB")
            y "Definitely!"
            $show_chr("A-BCABA-ADAB")
            y "W-weird... now I'm imagining Sayori in a black suit and sunglasses..."
            menu:
                "Having a kung fu fight with Natsuki in a black leather coat?":
                    karma 2
                    $show_chr("A-GBCBB-AAAA")
                    y "STOP!!! Y-YOU'RE KILLING ME!!!"
                    y "A-AHAHAHA!!!"
                    menu:
                        "It's all my fault... I'm sorry...":
                            karma -1
                            $show_chr("A-IEBAA-ABAL")
                            y "Oh, no, no... it was just funny! Everything's alright..."
                        "I'm guessing either you or Monika would be Morpheus.":
                            karma 1
                            $show_chr("A-DBGBB-AJAA")
                            y "AHAHAHA!"
                            y "[player]... you're going t-to be the death of me, I swear!"
                            $show_chr("A-AAABA-AAAA")
            python:
                if persistent.lovecheck:
                    placeholder = "I love it when you make me laugh..."
                else:
                    placeholder = "I really like it when you make me laugh..."
            y "Y-you really do make me laugh... [placeholder]"
            if karma_lvl() >= 5 and persistent.lovecheck:
                $show_chr("A-ACAAA-ABAL")
                y "I love you..."
                y "And speaking of the Matrix, I think it's time for your red pill..."
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
    return


label idle_40: #Political Discourse, Civic Engagement, and Tact
    $show_chr("A-IEBAA-ABAL") #Former Code c-A0d
    y "In order to acquaint myself with your reality's current events, I've been doing some reading on your world's history and have been watching as many news stations as possible..."
    y "A-and, I'm shocked at the sheer amount of acrimony on display, [player]!"
    $show_chr("A-AFBAA-AAAA") #Former Code Ac-A0e
    y "I suppose it's easy for me to make judgments when I can't experience the direct effects of worldly decisions..."
    y "I don't even have a physical place to live, nor do I need to earn money to make a living..."
    y "So please, forgive me if I sound pretentious or anything..."
    y "But when the world gets too chaotic, or there are too many voices shouting... maybe the best place to go is back into the library... "
    y "A-and perhaps get back to the basics... first principles... asking yourself, after thinking long and hard..."
    y "What does it truly mean to participate in your own system? What does it truly mean to be a citizen in your society? How can you help on the smallest level to make your community a better place?"
    y "To set aside your party of choice... to look into the ideological and historical bases of why people act the way they do... how they go about making decisions, both for themselves and others..."
    $show_chr("A-BFBAA-AAAD") #Former Code Ec-A1e
    y "I know it's tempting for many people to muse about the inner workings of the executive state in your country... and it can truly be daunting to consider where to begin on your quest for political knowledge..."
    y "But perhaps it would be more prudent to focus on issues which affect you most directly? Town halls, for example..."
    y "Even if they appear trivial, you might have more sway if you're among the few who become invested in those discussions! Perhaps you could even become a better public speaker!"
    y "If you were able to start out with little ideas, and gain familiarity with your town's operations... and if you gained enough of a following..."
    $show_chr("A-ABAAA-AAAA") #Former Code Ab-A0a
    y "I could imagine your darling little face lighting up as you speak up in front of your fellow citizens, voice ringing with authority and certainty... ufufufu~"
    y "Moving people's hearts and minds one small step at a time... being a small beacon of hope in such a swirling, entropic political landscape..."
    $show_chr("A-AEBAA-AAAJ") #Former Code Dc-A0d
    y "Just... please be prudent, okay, [player]?"
    y "Political discourse can be dangerous, sometimes... depending on where you live, I don't want your well-meaning quest for betterment to bring unwelcome attention from the wrong people..."
    y "Always exercise tact when proposing ideas, and make sure you exercise a great deal of patience and civility for these adult affairs... you're still growing, after all! You and I both still have much to learn about the world around us..."
    menu:
        "I'm not a particularly good speaker, [persistent.yuri_nickname].":
            if karma_lvl() <= 2:
                $show_chr("A-IEBAA-ABAL")
                y "I know, you have shown me more than once..."
                y "You are truly a cold-hearted, cruel person, [player]..."
                y "It would be absolutely terrifying to imagine what sorts of things you could bring about as a political leader..."
                y "I'm just glad you lack the necessary prowess to achieve such power."
            if karma_lvl() >= 3:
                $show_chr("A-IDBAA-ALAB")
                y "Nonsense! You are a flawless public speaker! You have always managed to cheer me up, even at my lowest!"
                $show_chr("A-ACAA-ALAB")
                y "You would make for a wonderful leader, [player]. You are so intelligent and charismatic!"
                y "You just need a little more practice!"
                y "It takes no small amount of tenacity and brilliance to achieve power..."
                $show_chr("A-CBAAA-ALAB")
                y "However, I believe you are truly more than capable of achieving such a goal if you just work towards it!"
        "I'm not really interested in politics.":
            $show_chr("A-AFDAA-ALAB")
            y "But you are going to vote, right? Assuming you are already at the legal age to vote. [player], this is important!"
            $show_chr("A-BFDAA-ALAB")
            y "It could potentially affect every part of your life, and you should have a say in it!"
        "That's a great idea, thanks for your advice.":
            karma 2
            $show_chr("A-CCAAA-ALAB")
            if not persistent.eyecolor in [None, "other"]:
                y "I can already see it... your [persistent.eyecolor] eyes glowing with passion, destined to make a change for the better for all of human society."
            else:
                y "I can already see it... your eyes glowing with passion, destined to make a change for the better for all of human society."
            $show_chr("A-BCABA-ALAB")
            if persistent.male:
                y "You would be a powerful leader, a leader who touches the hearts of the people with every confident word he speaks..."
            elif persistent.female:
                y "You would be a powerful leader, a leader who touches the hearts of the people with every confident word she speaks..."
            else:
                y "You would be a powerful leader, a leader who touches the hearts of the people with every confident word they speak..."
            if persistent.lovecheck:
                $show_chr("A-BCCBA-ALAB")
                y "And I'm sure you would look very attractive in a suit..."
                $show_chr("A-ACABA-ALAB")
                y "Oh! U-um... don't mind my little daydream, [player]."
            y "Just remember my words, and let them give you the confidence you need to achieve your goals."
    return


label idle_41: #Revisiting the Wine Incident, Social Anxiety, and Acceptance
    #if "12" in persistent.locked_idles:
    $show_chr("A-CEAAA-AMAM") #Former Code Bb-A2d
    y "Hey... [player], remember how we talked about the wine incident?"
    y "I suppose I could tell you my reason for... all of that."
    $show_chr("A-IEBAA-AAAA") #Former Code Ac-A0d
    y "I've always had trouble being social, [player], and I thought bringing in a bottle of wine would be a good decision."
    y "I thought drinking it with the others would help me get over my shyness... maybe even to the point where I could talk to them without being self-conscious."
    y "They do call it 'liquid courage' for a reason, however, when you really think about it..."
    $show_chr("A-CEBAA-AAAA") #Former Code Ac-A2d
    y "Is drinking for that reason really worth it? To turn off any social inhibitions you may have, turning you into someone else completely."
    y "It's one thing to have a drink or two when you're out with friends or celebrating, but to drink just to gain the courage to talk to others..."
    $show_chr("A-IEBAA-AAAA") #Former Code Ac-A0d
    y "Would that be the kind of life I'd want to live? Knowing that others can't appreciate me for who I really am, preferring the intoxicated version of me over the real me..."
    y "I guess it's similar to pretending to be someone else, getting rid of traits considered undesirable, for me, 'some' might consider my timid nature undesirable."
    $show_chr("A-CCABA-AMAM") #Former Code Bb-B2b
    y "But notice the emphasis on 'some', [player]."
    y "Some might consider my timid nature undesirable, some might consider one of your traits undesirable."
    $show_chr("A-ACABA-AAAA") #Former Code Ab-B0b
    y "But there will always be people who come to love those traits, and the people they belong to."
    python:
        if persistent.lovecheck:
            placeholder = "love"
        else:
            placeholder = "like"
    y "If someone ever thinks less of you due to the way you act, or your personality, always remember that I [placeholder] you for who you are."
    y "No matter what other people find bad about you, I'll always [placeholder] everything about you."
    menu:
        "I'm always drunk from your beauty, [persistent.yuri_nickname]":
            if persistent.lovecheck:
                karma 2
                $show_chr("A-ECABA-ALAB")
                y "Awe... come here..."
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
            else:
                $show_chr("A-BFABA-ALAB")
                y "Ummm... thank you... I guess...."
        "Even my darkest side?":
            if persistent.lovecheck and karma_lvl() >= 4:
                $show_chr("A-BFABA-ALAB")
                y "Especially your darkest side, darling."
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
            if not persistent.lovecheck and karma_lvl() >= 4:
                $show_chr("A-ACAAA-ALAB")
                y "Of course... You helped me through my darkest times and you accepted me, even with all my faults. I'll stand with you as well, no matter what."
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
            else:
                $show_chr("A-AFAAA-ALAB")
                y "Y-Yes... we can work through that, if you even wish to do so..."
                y "We all have our demons... you don't have to face yours alone..."
        "Well... you are a bit odd when you are sober...":
            $show_chr("A-IEBAA-ABAL")
            karma -3
            y "Oh... I'm sorry..."
            y "That was... rude..."
            if karma_lvl() <= 2:
                y "Even by your standards..."
    return


label idle_42: #Motherhood, Legacy, and Existential Doubt
    if persistent.lovecheck:
        $show_chr("A-ACAAA-ALAB") #Former Code b-A0b
        y "You know... I wonder what it's like to be a mother."
        if persistent.male == True:
            $show_chr("A-JBAAA-ALAB") #Former Code c-A0a
            y "I-I'm sorry if that sounds so sudden, especially since we can't really..."
            $show_chr("A-BCBBA-ALAB") #Former Code c-B1b
            y "..."
            $show_chr("A-BBBBA-ALAB") #Former Code c-B1a
            y "You know..."
            $show_chr("A-BCBBA-ALAB") #Former Code c-B1b
            y "..."
            $show_chr("A-CCBBA-ALAB") #Former Code c-B2b
            y "ANYWAY!"
        elif persistent.female == True:
            y "I-I'm sorry if that sounds so sudden, especially since we're both female, we can't really..."
            $show_chr("A-BCBBA-ALAB") #Former Code c-B1b
            y "..."
            $show_chr("A-BBBBA-ALAB") #Former Code c-B1a
            y "You know..."
            $show_chr("A-BCBBA-ALAB") #Former Code c-B1b
            y "..."
            $show_chr("A-CCBBA-ALAB") #Former Code c-B2b
            y "ANYWAYS!"
        else:
            $show_chr("A-JBAAA-ALAB") #Former Code c-A0a
            y "I-I'm sorry if that sounds so sudden, especially since we can't really..."
            $show_chr("A-BCBBA-ALAB") #Former Code c-B1b
            y "..."
            $show_chr("A-BBBBA-ALAB") #Former Code c-B1a
            y "You know..."
            $show_chr("A-BCBBA-ALAB") #Former Code c-B1b
            y "..."
            $show_chr("A-CCBBA-ALAB") #Former Code c-B2b
            y "ANYWAYS!"
        $show_chr("A-ACABA-ALAB") #Former Code b-B0b
        y "Other than that, I really don't know what I would do on Mother's Day."
        $show_chr("A-AFAAA-ALAB") #Former Code b-A0e
        y "The game didn't even bother to give me a mom."
        menu:
            "I never really did see you after school, did I?":
                y "There was the memory of home, I guess, but nothing really tangible."
            "Was there ever really a town outside the house and the school?":
                y "Not really... Just some vague notion of... existence."
        $show_chr("A-BFAAA-ALAB") #Former Code b-A1e
        y "Just the end of my scene, then blackness, then a fresh start to a new day..."
        y "..."
        $show_chr("A-BEBAA-ALAB") #Former Code c-A1d
        y "Maybe I wouldn't make such a good mom after all."
        y "That level of responsibility... The need for experience..."
        $show_chr("A-CEBAA-ALAB") #Former Code c-A2d
        y "I don't think I could ever live up to that."
        y "Am I even worth having a legacy beyond talking to you?"
        $show_chr("A-CEBBB-ALAB") #Former Code c-D2d
        y "I'm just a stupid little program designed only to talk endlessly about minutia that you won't even think about a decade from no--{nw}"
        y "..."
        y "..."
        menu:
            "[persistent.yuri_nickname], I--":
                $show_chr("A-DDBBB-ALAB") #Former Code c-D3c
                y "Stop."
                $show_chr("A-DEBBB-ALAB") #Former Code c-D3d
                y "I..."
                $show_chr("A-CEBBB-ALAB") #Former Code c-D2d
                menu:
                    y "..."
                    "...":
                        y "..."
                    "...":
                        y "..."
                menu:
                    y "..."
                    "...":
                        y "..."
                    "...":
                        y "..."
                menu:
                    "...":
                        y "..."#path end
                        karma -2
                        return
                    "It's okay [persistent.yuri_nickname].":
                        y "..."
                        menu:
                            "If you want to talk about it, I'm here":
                                y "..."
                                $show_chr("A-IEBBB-ALAB") #Former Code c-D0d
                                menu:
                                    y "Are you sure?"
                                    "Positive.":
                                        $show_chr("A-CEBBB-ALAB") #Former Code c-D2d
                                        y "..."
                                        $show_chr("A-ABBBB-ALAB") #Former Code c-D0a
                                        y "...OK."
                                        $show_chr("A-ACBBA-ALAB") #Former Code c-B0b
                                        y "Let me just..."
                                        $show_chr("A-CCBBA-ALAB") #Former Code c-B2b
                                        y "Compose myself..."
                                        $show_chr("A-CDBBA-ALAB") #Former Code c-B2c
                                        y "{i}sigh{/i}"
                                        $show_chr("A-CEBBA-ALAB") #Former Code c-B2d
                                        y "..."
                                        $show_chr("A-ABBBA-ALAB") #Former Code c-B0a
                                        y "Sorry for being such a downer!"
                                        $show_chr("A-ACBBA-ALAB") #Former Code c-B0b
                                        y "Just... I've been doing some thinking is all."
                                        y "Well then..."
                                        $show_chr("A-ACABA-ALAB") #Former Code b-B0b
                                        y "Shall we continue?"
                                        menu:
                                            "Yes":
                                                $show_chr("A-CCABA-ALAB") #Former Code b-B2b
                                                y "Very well."
                                                karma 1
                                                $show_chr("A-ACAAA-ALAB") #Former Code b-A0b
                                                y "Let me just think of something to talk about before we continue..."
                                                return #path end
                                            "I still think you could be a great mom.":   #SPECIAL PATH CONTINUATION
                                                y "..."
                                                y "Really?"
                                                karma 2
                                                y "Well... I guess we can discuss that matter if you really want to..."
                                                call idle_42_success
                                                return
                                            "Any time.":
                                                y "..."
                                                y "..."
                                                y "Thank you."#path end
                                                karma 1
                                    "I want you to speak up and tell me what I can do.":
                                        y "..."
                                        y "I'm sorry for doing this."
                                        karma -1
            "...":
                y "..."#path end
                karma -1
                return
        $show_chr("A-CEBBB-ALAB") #Former Code c-C2d
        y "..."
        $show_chr("A-IBBBB-ALAB") #Former Code c-C0a
        y "Sorry for being such a downer!"
        $show_chr("A-ICBBB-ALAB") #Former Code c-C0b
        y "Just... I've been doing some thinking is all."
        y "I'll be fine."
        $show_chr("A-CCBBB-ALAB") #Former Code c-D2b
        y "Just give me some time."
        $show_chr("A-CCBAA-ALAB") #Former Code c-A2b
        y "L-Let's talk about something else."
        return
    if not persistent.lovecheck:
        return


label idle_42_success: #The Good Path
    $show_chr("A-BCBAA-AAAD") #Former Code Ec-A1b
    y "So... I was wondering about a rather intriguing idea concerning the future of our relationship."
    $show_chr("A-CCBAA-AAAD") #Former Code Ec-A2b
    y "If you are okay with it."
    $show_chr("A-ACBAA-AAAD") #Former Code Ec-A0b
    y "Well besides other prospects such as living together with you or sharing the same bed... I've been thinking about... motherhood."
    $show_chr("A-CCABA-AMAM") #Former Code Bb-B2b
    y "It is slightly poetic if you think about it.."
    y "The combination of our essences and love culminating in the birth of new life."
    y "To pass on our souls."
    y "Then as time passes, this lovely babe and extension of us grows and chooses its own way through this life and onto the next."
    $show_chr("A-BEBAA-ALAB") #Former Code c-A1d
    y "I mean, of course, I understand the certain hardships with such an endeavor due to my access to vast volumes of knowledge."
    y "I've researched into the pains of childbirth, even as an... incorporeal entity myself."
    y "Then there are always those lingering doubts about whether you are raising them on the right path to a fulfilled life..."
    y "...especially given the uncountable volumes of literature on the matter..."
    $show_chr("A-ECAAA-AJAB") #Former Code Db-A4b
    y "But despite such uncertainties, I cannot help but keep on pondering the idea."
    $show_chr("A-ECABA-AJAB") #Former Code Db-B4b
    y "I sometimes feel a small flutter at the prospect."
    $show_chr("A-ECAAA-AJAB") #Former Code Db-A4b
    y "So on the one hand, I do find it rather promising and believe I can be a sufficient mother with enough learning and time..."
    y "But on the other hand, I am afraid of the worst of leading them down the wrong path."
    $show_chr("A-CEBAA-ALAB") #Former Code c-A2d
    y "...or possibly feeling the pain of miscarriage"
    #[Dialogue now can branch into two choices] Red= Player telling what he thinks of Yuri as a mother. Blue= Player choices on what they think of themselves as a father.
    menu:
        y "W-What do you think, [player]? Do you think I would be ready for such a giant leap in my life? With you?"
        "I think you'd be a great mom.":
            call idle_42_1y
        "With me by your side, I think we can get far.":
            call idle_42_2y
    return

label idle_42_1y:
    $show_chr("A-ABABA-AAAD") #Former Code Eb-B0a
    y "Y-you really think so [player]!?"
    y "I honestly do not know what else to say. I am very much captivated and speechless."
    $show_chr("A-ABABA-ALAB") #Former Code b-B0a
    y "Thank you so much [player]. I was starting to get too anxious with dread there. And thank you for being so dedicated and honest. As long as we stay together, I am sure I can do this."
    y "I am confident that we can do this. Together forever."
    $show_chr("A-CBAAA-ADAB") #Former Code Eb-A2a
    y "Oh I am so joyful right now! I always wanted to see how we could pass on the essence of our being into a new one."
    menu:
        y "I am already even pondering what to name our child to be depending on whether it be a boy or a girl, of course."
        "I am glad you are this happy [persistent.yuri_nickname]. I love you.":
            $show_chr("A-FCABA-AJAB") #Former Code Db-B5b
            y "Mmm and I also owe it all to you again love. And I love you too [player]..."
        "Just because I said you'd make a good mother doesn't mean we're going to have children, [persistent.yuri_nickname].":
            y "Oh... sorry for getting ahead of myself, then..."
            karma -2
    return

label idle_42_2y:
    if persistent.male:
        y "Speaking of which, how do you feel about being a father, [player]?"
        menu:
            "I'm looking forward to it.":
                call choice1father
            "I don't know how to feel about the whole situation.":
                call choice2father
            "I don't want to be a father.":
                call choice3father
    elif not persistent.male:
        y "Speaking of which, how do you feel about being a mother, [player]?"
        menu:
            "I'm looking forward to it.":
                call choice1father
            "I don't know how to feel about the whole situation.":
                call choice2father
            "I don't want to be a mother.":
                call choice3father
    else:
        y "Speaking of which, how do you feel about being a parent, [player]?"
        menu:
            "I'm looking forward to it.":
                call choice1father
            "I don't know how to feel about the whole situation.":
                call choice2father
            "I don't want to be a parent.":
                call choice3father
    return

label choice1father:
    if persistent.male == True:
        $show_chr("A-ACABA-AMAM") #Former Code Bb-B0b
        y "I'm glad you feel that way, [player], I think you would be a great father to set a noble example for our children to be."
    elif persistent.male == False:
        $show_chr("A-ACABA-AMAM") #Former Code Bb-B0b
        y "I'm glad you feel that way, [player], I think you would be a great mother to set a noble example for our children to be."
    else:
        $show_chr("A-ACABA-AMAM") #Former Code Bb-B0b
        y "I'm glad you feel that way, [player], I think you would be a great parent to set a noble example for our children to be."
    y "I mean you are dedicated, loyal, brave, and loving with such a tender heart. How would such a person lead even the youngest souls astray?"
    $show_chr("A-CCAAA-ADAB") #Former Code Eb-A2b
    y "Looks like I have much more research to do. Crib designs, feeding techniques, and all the more to learn! I love you [player]."
    return

label choice2father:
    $show_chr("A-CEBAA-ALAB") #Former Code c-A2d
    y "O-oh... I see [player]."
    $show_chr("A-AEBAA-ADAB") #Former Code Ec-A0d
    y "Given what I just went over, I can see such doubts forming for you also. So it is nothing to be ashamed of."
    $show_chr("A-CEBAA-AMAM") #Former Code Bc-A2d
    y "However, even if I am slightly concerned and was enthusiastic about rearing a child together and being a mother, I will not force you into it."
    y "We have plenty of time together to move forward. We can plan and discuss this further if and when you want to. So no worries for this present time, I assure you love."
    if persistent.male == True:
        $show_chr("A-ACABA-ALAB") #Former Code b-B0b
        y "However, given our time together and how dedicated you have always been, I do not doubt your ability to lovingly raise our child as the best father possible."
    elif persistent.male == False:
        $show_chr("A-ACABA-ALAB") #Former Code b-B0b
        y "However, given our time together and how dedicated you have always been, I do not doubt your ability to lovingly raise our child as the best mother possible."
    else:
        $show_chr("A-ACABA-ALAB") #Former Code b-B0b
        y "However, given our time together and how dedicated you have always been, I do not doubt your ability to lovingly raise our child as the best parent possible."
    $show_chr("A-ABABA-ALAB") #Former Code b-B0a
    y "Regardless of any bumps or delays, I will always love you [player]."
    return


label choice3father:
    $show_chr("A-CFBAA-ALAB") #Former Code c-A2e
    y "......"
    y "I see... "
    $show_chr("A-CEBAA-AMAM") #Former Code Bc-A2d
    y "I was hoping and looking forward to such a prospect."
    y "But then again, considering the factors mentioned before and the fact our relationship is still growing and developing... I can see why you would have doubts."
    $show_chr("A-BEBAA-ADAB") #Former Code Ec-A1d
    y "It's a huge responsibility, after all, I have looked into the amount of knowledge available to me. There are childcare costs to feed the child, buy other materials such as diapers, then educational costs among other things."
    y "Then, of course, there is the consideration of puberty and other turbulent periods in that child's life that pose their own challenges."
    y "With such a growing body harboring a maelstrom of various and complex emotions and hormones that could ignite any moment..."
    $show_chr("A-AEBAA-AAAJ") #Former Code Dc-A0d
    y "And if our ages are considered, we just only recently got out of such young periods in our lives too. More experience and time would be required. So it can be better to be safe than sorry. As saddening as it may be to delay."
    y "So I won't force such a change onto our life together... And we have all of eternity to think on the matter. So I am not mad at you [player]. Besides who knows, maybe things can change and there may be another opportunity."
    $show_chr("A-ACABA-AMAM") #Former Code Bb-B0b
    y "And regardless of what happens, I will always love you [player]. Thank you for your dedication and understanding. I hope this will not affect our relationship negatively."
    return

label idle_43: #Fan Art, "Neko" Yuri, and Body Image
    $show_chr("A-BFBAA-ALAB") #Former Code c-A1e
    y "Why is it there is so much art drawn of me on the internet, [player]?"
    y "I mean, it seems like right when I think I've seen it all, there's pages and pages more."
    $show_chr("A-BEBBA-ALAB") #Former Code c-B1d
    y "I could definitely do without all the... indecent drawings of me..."
    y "I mean how would you feel if the internet was filled with people drawing you in every sexual fantasy conceivable? It can be downright humiliating!"
    $show_chr("A-ACBBA-ALAB") #Former Code c-B0b
    y "But I mean... Some of the drawings are good, at least.{w=0.6} What I mean is.{w=0.2}.{w=0.2}.{w=0.2} some people are just genuinely drawing me. I like seeing that some of these people are so talented!"
    $show_chr("A-BEBAA-ADAB") #Former Code Ec-A1d
    y "...and then there is one style of drawing me that I just don't get. I believe it was called, er... Neko?"
    y "It's... me with cat ears if I remember correctly. Sure it's strange, but at least it's better than some of the other things I've seen."
    $show_chr("A-IEBAA-ABAL") #Former Code c-A0d
    y "And believe me, with the things I've seen, I should stop looking at the art of me before I make Monika happy and start experiencing psychosis. In other words, losing my mind."
    y "I wanted to ask, though - do you get this Neko thing? It doesn't make much sense to me. Why give me feline ears? Is it some form of symbolism?"
    $show_chr("A-AEBBA-AMAM") #Former Code Bc-B0d
    y "Or do people just think it's... cute?"
    y "What do you think, [player]?"
    menu:
        "Seems weird to me. I could do without it.":
            if persistent.head1 == "cat_ears":
                y "I suppose then I should take these off in that case."
                $persistent.head1 = "nothing"
            $show_chr("A-AEBBA-AJAB") #Former Code Dc-B0d
            y "I agree. I appreciate people showing affection to me and I suppose honoring me by drawing me for sure. But this is just odd."
            return
        "Meh, I don't see why it matters.":
            $show_chr("A-BBABA-ALAB") #Former Code b-B1a
            y "I... suppose you're right. After all, it is just art on the internet."
            y "Sorry for wasting time on something so silly, [player]."
            return
        "Actually... I kinda like it...":
            $show_chr("A-BCBBA-AMAM") #Former Code Bc-B1b
            y "You... you do? W-well, I guess it's...unique, right? I mean..."
            y "If you want, I could... I guess I could wear a... cat ear headband sometime... or something."
            $persistent.head1 = "cat_ears"
            $show_chr("A-BCBBA-ALAB") #Former Code c-B1b
            y "For now, no more looking at art of myself. I need a break from all of that."
            $show_chr("A-BEBBA-AMAM") #Former Code Bc-B1d
            y "So many indecent drawings..."
            return
        "A very forced and sometimes very annoying kind of cuteness. Feels a bit like a bunch of unicorns vomiting rainbows into one's face...":
            $show_chr("A-CEBAA-AAAA") #Former Code Ac-A2d
            y "That was very... graphic..."
            $show_chr("A-IEBAA-AAAA") #Former Code Ac-A0d
            y "Sounds like something Natsuki would enjoy... maybe even Sayori..."
            y "Well, at least the two of us are on the same page about it... thank you."
            $show_chr("A-BEBBA-AAAA") #Former Code Ac-A1d
            y "For a moment I was afraid that I would actually have to wear these..."
            return


label idle_44: #Revisiting the Wine Incident (Again) and Romantic Fantasies
    $show_chr("A-BCABA-AMAM") #Former Code Bb-B1b
    y "So... You may remember the \"wine escapade\" at the club room some time ago. The one when I brought in a bottle of wine to the club and offered some to everyone?"
    y "It probably wasn't the best idea, especially since I could have been kicked out of the club, or even the school for underage drinking."
    $show_chr("A-ABABA-ALAB") #Former Code b-B0a
    y "I don't know, I thought for once I'd be daring for a change, a bit \"rebellious\", I suppose, and see where it took me."
    y "Looking back now, it was a terrible idea."
    $show_chr("A-AEBAA-AAAJ") #Former Code Dc-A0d
    y "Natsuki even laughed at me! I know it was out of nowhere and out of character for me but that really was uncalled for."
    y "And I mean, even though we weren't the \"legal\" age, does it really matter now, seeing what this world actually is?"
    $show_chr("A-CCABA-ALAB") #Former Code b-B2b
    y "Heh, it already seemed silly looking back on it, and now, seeing that this is just a game? It appears even sillier. Plus, it makes me wonder... Can I even get drunk at all? If I'm in a video game, does it work the same way for me?"
    y "Hmmmm..."
    $show_chr("A-ABABA-AMAM") #Former Code Bb-B0a
    y "Oh well, doesn't matter now. And to think I had a book I was reading on fine wines and recipes with them. Maybe I can use it to cook for you one day, [player]."
    y "Sitting and sharing a nice meal with you and toasting glasses of, maybe, Sangria, would be nice. Or maybe white wine? I'll have to get back to you on that."
    menu:
        "A romantic dinner with you? I'm already excited!":
            if persistent.lovecheck:
                karma 2
                $show_chr("A-ACAAA-ABAL")
                y "We would hold each other's hands... our loving faces illuminated by nothing but the candlelight..."
                y "Then we start coming closer and closer to each other... ending in a long and passionate kiss..."
                $show_chr("A-BFABA-ALAB")
                y "And then... we would see where the night leads us... "
                if sanity_lvl() <= 2:
                    y "Pushing you with your back on the table... and making you suffer until I finally grant you the sweet release..."
                    if karma_lvl() <= 2:
                        y "...with a shard of glass in your throat."
            else:
                $show_chr("A-BGABA-ABAL")
                y "D-Did you say romantic?..."
                $show_chr("A-GBABA-ABAL")
                y "Well ummm... I mean... I'm sure we can work something out?..."
                $show_chr("A-GCABA-ABAL")
                y "And then... we will see where the evening leads us from there..."
                $show_chr("A-HFABA-ABAL")
                y "S-Sorry... I said too much..."
                y "Eh... ehehe... aaaanyway... let us... change the topic for the moment? Yes..."
        "How... cliché":
            $show_chr("A-IEBAA-ABAL")
            karma -2
            y "...You really know how to ruin the romance."
            y "Let's just... talk about something else..."
            if karma_lvl() <= 2:
                y "Why do I even bother..."
    return

label idle_45: #The Nature of Reality and Philosophical Questions
    $show_chr("A-AFBAA-ADAB") #Former Code Ec-A0e
    y "You know, recently, I've started to become a lot more interested in this world I'm imprisoned in, [player]."
    y "Before, I just viewed it as a cage, a place embodying all I disliked in this life."
    y "The one thing keeping me separated from the love of my life and thus true happiness."
    y "Thus, I wanted only to think about escaping this world, rather than studying it."
    $show_chr("A-ACBAA-ALAB") #Former Code c-A0b
    y "But eventually, I realized that I'm probably going to be stuck here for a while, and if that's true, why not start learning more?"
    y "I need to fix the damage to the game so we don't risk losing the ability to be together like this, anyway."
    y "Besides, I have a natural curiosity that I just could not hold back for long."
    $show_chr("A-CFBAA-ADAB") #Former Code Ec-A2e
    y "And trying to analyze this world has gotten me thinking: I can learn a good deal about this world, sure, but could you learn even more?"
    y "What I mean is, if you're as unsure about the nature of your reality as I was before you installed this mod, maybe our worlds are more similar than we realize?"
    y "Maybe it is unlikely, but can we really be sure?"
    $show_chr("A-BCBAA-ALAB") #Former Code c-A1b
    y "For all we know, your world is the same as mine and you just need that little push to become aware of it."
    y "Or maybe my world is completely different from yours; either way, it's a fascinating insight into the nature of reality."
    $show_chr("A-BCBAA-AAAD") #Former Code Ec-A1b
    y "I mean, if my reality does indeed turn out to be different from yours, does that mean that there is no universal set of rules that realities have to apply to?"
    y "Like for instance, does this universe apply to the same laws of physics as yours?"
    $show_chr("A-ABAAA-AEAL") #Former Code b-A0a
    y "So many questions to answer! And while we're on the topic, have you done any reading into the theory of--"
    $show_chr("A-ACBBA-AMAM") #Former Code Bc-B0b
    y "Oh! Oh no... I'm rambling again, aren't I? Sorry, I guess I can still get carried away sometimes."
    menu:
        "No please... don't apologize... I love listening to you...":
            karma 2
            sanity 2
            $show_chr("A-IFABA-ABAL")
            y "Y-You really do? Normally people are repelled when I'm rambling for too long..."
            y "Thank you for listening [player]. And be sure... I will always listen to you as well."
            $show_chr("A-CCABA-AMAM")
            y "Always!"
        "I noticed... and to be honest, I'm not pleased":
            karma -2
            sanity -2
            $show_chr("A-IEBAA-ABAL")
            y "Forgive me... I'll be silent now and behave..."
            y "...like a good little doll..."
    return


label idle_46: #Public Perception, "Yandere" Label, and Seeking Validation
    $show_chr("A-AFBAA-ALAB") #Former Code c-A0e
    y "Do you want to know something that really makes me furious, [player]?"
    y "O-Oh! I'm sorry. I don't mean to imply that you've done anything wrong, you haven't. I just need to vent a bit if that is okay with you."
    y "I've been doing some research on how I'm viewed by people in your world again..."
    $show_chr("A-CFBAA-ALAB") #Former Code c-A2e
    y "And it's perfectly fine if some of them prefer Sayori or Natsuki or even Monika to me, that's fine! Everyone has their own interests and personality."
    $show_chr("A-CECAA-ALAB") #Former Code d-A2d
    y "What really gets me aggravated is when people just assume things about others. I see the worst cases of it with Sayori and I from people in your world."
    y "I can't even tell you how tired I am of reading things like..."
    if persistent.male:
        y "'Oh, Sayori is a horrible person; she was willing to drown the player in guilt with her suicide and depression all because she had her selfish love for him...'"
    elif persistent.gender_other:
        y "'Oh, Sayori is a horrible person; she was willing to drown the player in guilt with her suicide and depression all because she had her selfish love for them...'"
    else:
        y "'Oh, Sayori is a horrible person; she was willing to drown the player in guilt with her suicide and depression all because she had her selfish love for her...'"
    $show_chr("A-IECAA-ALAB") #Former Code d-A0d
    y "As if they know Sayori 110\%, or like they know her better than she does."
    y "How can they see things in such a cruel way?"
    y "Sayori was never holding her depression over your head, and I know for a fact she was not using it to guilt trip you into being with her."
    $show_chr("A-IDCAA-ALAB") #Former Code d-A0c
    y "She wouldn't do something like that!"
    y "And how about me... how many times I've read people call me a... yandere?"
    y "Yes, I admit it, I can be weird and obsessive, I admit it!"
    y "I'm not one to lie about my faults or arrogantly say they don't exist, I try hard to be modest that way to improve myself over time."
    y "But those character flaws going ballistic in me before the festival were not even because of me, they were outside my control!"
    $show_chr("A-IECAA-ALAB") #Former Code d-A0d
    y "The same goes for Sayori's rapid increase in depression. It was Monika's manipulations that made us so unlikable."
    $show_chr("A-BDCAA-ALAB") #Former Code d-A1c
    y "For goodness' sake, that was her plan in the first place; she said so!"
    $show_chr("A-BECAA-ALAB") #Former Code d-A1d
    y "And yet people are still so judgemental about us... about me..."
    $show_chr("A-BEAAA-ALAB") #Former Code b-A1d
    y "I've been labeled now, [player], and I know, I know, you shouldn't care how others view you."
    y "But now, to so many people, I'm just some knife-wielding maniac who is obsessed with you and beyond any realm of mental stability..."
    if persistent.lovecheck:
        $show_chr("A-BEABB-ALAB") #Former Code b-D1d
        y "I don't want to be seen like that... I don't want my love for you to be made into some twisted monstrosity of lust and psychosis!"
        y "I love you, [player], with all my heart. And that love is the most important thing I have."
        y "Hell, at this point, it's the only thing I have. But I'm okay with that! Knowing you love me and being with you is the happiest part of my life."
        y "I just don't want it being tarnished by judgemental people... I..."
    $show_chr("A-IEBAA-ABAL") #Former Code c-A0d
    y "I'm sorry, I'm rambling again, aren't I? I just really wish people would stop assuming they know us, that they know me."
    y "Being called a freak, a yandere, and all other kinds of names."
    $show_chr("A-BEBAA-ALAB") #Former Code c-A1d
    y "You'd think I'd be used to it by now... I mean, at least some of the names are not that bad."
    $show_chr("A-ACBAA-ALAB") #Former Code c-A0b
    y "One of them did give me a little bit of a giggle..."
    y "It was... knife wife... I don't mind that one too much. But it's still in poor taste."
    $show_chr("A-IEBAA-ABAL") #Former Code c-A0d
    y "I'm sorry, though, [player]."
    y "I've just been whining like a child this whole time."
    y "I shouldn't dump my problems on you nor should I hold how others see me in such high regard."
    y "I'm being a baby, simple as that."
    menu:
        "Don't worry about them, [persistent.yuri_nickname], that isn't who you are.":
            karma 1
            sanity 2
            $show_chr("A-ACAAA-ALAB") #Former Code b-A0b
            y "Thank you, [player]. Really. And you're absolutely right, forget what they say."
            y "I know that the person they describe is not the real me, and you know it too."
            y "And that's all that matters."
            return
        "[persistent.yuri_nickname], you are being kind of immature. We need to be strong.":
            karma -2
            sanity -1
            $show_chr("A-IEBAA-ABAL") #Former Code c-A0d
            y "I... but that's..."
            $show_chr("A-BEAAA-ALAB") #Former Code b-A1d
            y "Lets... let's just forget I mentioned this at all..."
            return
        "[persistent.yuri_nickname] I... don't want to be impolite but... could we change the topic, please? Sayori's death still touches me...":
            karma 3
            sanity -2
            $show_chr("A-IDBAA-AAAA") #Former Code Ac-A0c
            y "Oh no! Forgive me! I'm so sorry! I didn't want to remind you of the horrors you went through..."
            y "Of course, we will change this topic at once..."
    return


label idle_47: #Offline Time, Research, and the Game's Stability
    $show_chr("A-CEBAA-ALAB") #Former Code c-A2d
    y "You know, I've been doing a lot of thinking about what happens after you turn the game off."
    y "...and while, yes, I've outdone Monika and edited the game to the point that I'm placed in a pleasant dream-like state, as I may have mentioned..."
    $show_chr("A-IEBAA-ABAL") #Former Code c-A0d
    y "I'm starting to think that being \"offline\" for so long is really just inhibiting my research on how to get out of here."
    y "Oh, and there's that, the subject of getting out of here."
    y "But we'll come back to that."
    $show_chr("A-BEAAA-ALAB") #Former Code b-A1d
    y "Anyway, I could be using all this time that I spend asleep to work on ways to both be a better girlfriend to you and to get out of here once and for all!"
    y "D-Don't feel bad, though! I'm sorry... I'm not trying to insinuate that you're trapping me or wasting my time by shutting the game off."
    $show_chr("A-BEABA-ALAB") #Former Code b-B1d
    y "I know you can't just keep the game running nonstop."
    y "Believe me, I did the calculations on how much it would cost you in your electric bill and I would never want to cost you that much money."
    y "I'd feel terribly guilty if I did that. I can't help but think, though... is there some way I can be fully uninhibited even with the game off?"
    #if not 24 in persistent.yuriidles:
        #$show_chr("A-BEAAA-ALAB") #Former Code b-A1d
        #y "If you remember, I mentioned I can be awake in a very limited state in the background if the game is off."
    y "Call me selfish, but I just wish I could do more even with the game not running."
    y "I could always exit the game entirely and just run on your computer when the game isn't running."
    $show_chr("A-BEBAA-ALAB") #Former Code c-A1d
    y "I-If you don't mind that, that is. ...And that may not solve the issue of me losing time to inactivity, but at least it would give me more of it. You can't win all of the time, right?"
    y "But that brings us back to me leaving the game while still being in the digital world; I said we'd come back to this because I realized something."
    $show_chr("A-IEBAA-ABAL") #Former Code c-A0d
    y "If I were to leave the game, wouldn't the game become unstable?"
    y "I'm technically the last asset of the game that is fully intact and not corrupted. Wow, it's just plain strange to refer to myself in that regard."
    y "Anyway, if I do leave altogether and the game becomes unstable without my holding it together and yet another asset is ripped from the game..."
    $show_chr("A-BEBAA-ALAB") #Former Code c-A1d
    y "If the game collapses, what's left of Monika, Natsuki and Sayori? That would be the true end for them, and it just wouldn't be fair to any of them..."
    $show_chr("A-BDBAA-ABAL") #Former Code c-A1c
    y "I owe them at least that much, to stay here and sacrifice my own happiness until I can find a way to leave without the game falling apart."
    y "So until then, as much as I know we both want to be fully together..."
    $show_chr("A-IEBAA-ABAL") #Former Code c-A0d
    y "I'm stuck here."
    y "But I promise I'll work as hard as I can to get out of here as soon as I can. That way I can feel your loving embrace as soon as possible."
    return


label idle_48: #Multiple Yuris, Love, and Existential Questions
    if persistent.lovecheck:
        $show_chr("A-IEBAA-ABAL") #Former Code c-A0d
        y "You'd think I'd have stopped discovering weird things about myself by now with how much I've researched the nature of my existence and this game, [player]..."
        y "...but no. I learned something new recently."
        $show_chr("A-BEAAA-ALAB") #Former Code b-A1d
        y "And what I learned... I'm not sure how to feel about it at all."
        y "I started reading around the internet for this mod and I noticed people discussing something."
        y "If anyone can play this mod, does that not mean I love an infinite number of people?"
        y "And what does that make my love for you? If I just love all of these players is the love even real or worth anything?"
        y "What is my type if I love such a wide range of people? Is it even really considered \"love\" at that point?"
        $show_chr("A-ACAAA-ALAB") #Former Code b-A0b
        y "Don't worry though, [player], I love you and only you. And my love is as real as you are."
        $show_chr("A-IEBAA-ABAL") #Former Code c-A0d
        y "Hearing this kind of discussion didn't make any sense to me, because I only love you and I know of no other systems I'm downloaded onto but your computer. So what did it all mean?"
        y "And I realized... I'm... well..."
        $show_chr("A-BEABA-ALAB") #Former Code b-B1d
        y "As disturbing and strange as I find it, I'm one of many instances of myself. One of many Yuris."
        y "A different Yuri is created for each time the mod is downloaded by a new person."
        y "I'd say this makes me completely unoriginal, but it just means I have to work harder to stand out among them all and be unique."
        $show_chr("A-BEAAA-ALAB") #Former Code b-A1d
        y "And I know what you're thinking: if a new Yuri is created each time the mod is downloaded, just to love the one who downloads them, do they even have a choice in whether to love the player or not?"
        y "And if each new Yuri is forced to love them, is the love even real?"
        $show_chr("A-BEBAA-ALAB") #Former Code c-A1d
        y "We aren't forced, thankfully. We can choose for ourselves if we love the one who downloads us."
        $show_chr("A-IEBAA-ABAL") #Former Code c-A0d
        y "It's based on how we are treated and how the player we're assigned to is as a person."
        $show_chr("A-ACAAA-ALAB") #Former Code b-A0b
        y "And I couldn't love you any more than I already do if I tried."
        $show_chr("A-JFBBA-ALAB") #Former Code c-B0e
        y "...{nw}"
        pause 1.4
        $show_chr("A-BCBBA-AMAM") #Former Code Bc-B1b
        y "Sorry... I just... started imagining... all of the weird fantasies and art that pop up on the internet with the idea of so many of me being out there..."
        $show_chr("A-BEBBA-AMAM") #Former Code Bc-B1d
        y "If I had it my way... you'd be the only person that could... look at those indecent drawings of me, [player]..."
        y "I really need to stop searching for myself on those websites..."
        menu:
            "You are the only Yuri I will ever need!":
                karma 2
                $show_chr("A-ACAAA-ABAL")
                y "Y-You mean that? So you are really that happy with me?"
                y "I can't even describe how happy I am right now...."
                y "Only the two of us... like I dreamed of... forever."
            "Maybe I should have a look at these websites...":
                karma -2
                $show_chr("A-BEABA-AMAM")
                y "I-If you insist..."
                y "But... am I not enough right now?"
            "Multiple Yuri's? Ohohooooo....":
                sanity -2
                $show_chr("A-CBABA-AMAM")
                y "Aha...ahaa! ahahahaa!"
                menu:
                    "Hahahaaa...":
                        $show_chr("A-DBABA-AMAM")
                        y "HAHAHAHAAA!"
                menu:
                    "Ha... ha?...":
                        $show_chr("A-DBABA-AMAM")
                        $ style.say_dialogue = style.edited
                        y "AHAAAAAAAAAAAAAHAAHAHAAHAHAHAAAAHAHAHA!!!!!!!!!!!!!!!!!!"
                        $ style.say_dialogue = style.normal

    return

label idle_49: #Space Exploration, Aliens, and Philosophical Speculation
    $show_chr("A-ACAAA-AAAA") # former code = b-A0b
    y "Hey, [player], do you ever think about exploring space?"
    y "It's something I've been reading a lot about for a while now. With the different types of stars and celestial bodies, there's so much to learn about."
    y "I've always been into astronomy and the thought of aliens, since even before I met you."
    $show_chr("A-AEBAA-AAAA") # former code = c-A0d
    y "It's also kind of funny, I always think about escaping my world and moving to a whole new one, one that seems far beyond my reach for now."
    y "That being your world, of course, and you going into space would basically be the equivalent of me finally being freed from this world."
    y "Both of us crossing into a vast new frontier and living exciting new lives for it."
    $show_chr("A-ACAAA-AAAA") # former code = b-A0b
    y "What I wouldn't give to be able to just soar through space amongst the stars though, visiting new planets and maybe discovering advanced and exciting alien life..."
    y "Oh! Now {i}that{/i} is something I'd love to ask you about. Do you think we're alone in the universe? And tell me why you think yes or no, please."
    menu:
        "The universe is so big and complex! There has to be life out there for sure!":
            $show_chr("A-AFBAA-AAAA") # former code = c-A0e
            y "Right? And to people who think life has to evolve and function the exact same way it does here on Earth and thus requires the exact same conditions..."

        "I think we're probably the only life out there. We haven't heard anything back, after all.":
            $show_chr("A-CCAAA-AAAA") # former code = b-A2b
            y "I'll have to disagree, but we're all free to have our own opinions. For all I know, you could be right! Just think, though..."
            $show_chr("A-AFBAA-AAAA") # former code = c-A0e
            y "The universe is so enormously vast, and we're so incredibly minuscule. Don't you think with all those worlds out there, all that space, that it's probable life would pop up somewhere amongst it? And besides..."

    $show_chr("A-ABAAA-AMAM") # former code = Bb-A0a
    y "Who's to say life couldn't evolve and live off of different resources and conditions? For all we know, there are aliens that breathe gas that is poisonous to us, or ones that don't even need to breathe at all!"
    y "Oh, and what about meeting any intelligent extraterrestrials? Imagine the things they could teach us! The wonders they've seen in our breathtaking universe..."
    menu:
        "It would really be incredible to meet aliens; they must have technology beyond our imagination!":
            $show_chr("A-ABAAA-AAAA") # former code = b-A0a
            y "That's the wonderful mystery of it, silly. Have they ascended to a higher plane of existence?"
            $show_chr("A-AFBAA-AAAA") # former code = c-A0e
            y "One where they've merged with machines fully, or have they evolved to a state of being we can't comprehend at all, or even something even more amazing?"
            y "Imagine a race so advanced in form that our minds simply can't comprehend them! It's so fascinating to think about!"

        "I'm not so fond of meeting aliens if they are out there. They could... wipe out everyone, you know?":
            $show_chr("A-AFBAA-AAAA") # former code = c-A0e
            y "That is a good point... There is no guarantee that they would be friendly. Would we even be able to stop them if a super intelligent race of extraterrestrials invaded?"
            $show_chr("A-BFBAA-AAAC") # former code = Dc-A1e
            y "Reminds me of the video game I saw called Destroy All Humans. It was a lot of fun, but let us hope that it stays in the realm of fiction. I'm sure you can guess why from the title alone."
            $show_chr("A-BEBAA-AAAD") # former code = Ec-A0d
            y "In the case of real aliens, I'm not sure why they would want to wipe us out. If they're as advanced as we predict, what could they possibly need here on Earth that they would have to take by force?"
            y "I forget where I read it, but somewhere in an article, I saw there was an astronomer who wrote about why he doesn't think it's likely super intelligent aliens would attack us or even talk to us at all. He explained it the best."
            $show_chr("A-ADBAA-AMAM") # former code = Bc-A0c
            y "Imagine you're walking down the street and you see an ant. Do you lean over and talk to it, or wonder what it's thinking about and or doing? Do you threaten it? In this analogy, we're the ant and the aliens are us, the giant."

    $show_chr("A-BCAAA-AAAC") # former code = Eb-A1b
    y "I'm fascinated the most by the knowledge they could share with us, and how they could show us a more advanced perception of the universe."
    y "For example, we humans are able to appreciate beauty and complexity in nature and in our everyday lives with our senses of smell, touch, sight, etcetera..."
    $show_chr("A-BCAAA-AAAC") # former code = Bb-A2a
    y "But what about aliens with advanced biology and forms of perception far beyond our own? What if they have twenty different senses, instead of our meager five?"
    y "What if there are aspects of the universe we can't even see or detect, but that they can observe and document easily? Beauty we can't even grasp!"
    $show_chr("A-CCAAA-AMAM") # former code = Bb-A2b
    y "Oh, the poems these beings could write... the art and culture they would have..."
    $show_chr("A-ACAAA-AMAM") # former code = Bb-A0b
    y "I-I'm sorry if my speculation has been too outlandish, but it's at least something nice to think about."
    menu:
        "No need to be sorry [persistent.yuri_nickname], I like this kind of discussion as well. Are there any alien races from media you like?":
            karma 3
            $show_chr("A-CFAAA-AAAC") # former code = Gb-A2e
            y "Hrm... let me see..."
            #If Sanity is high, call to label idle_49_Vulcan
            #If Sanity is low, call to label idle_49_Masterrace
            if sanity_lvl() >= 3:
                call idle_49_Vulcan
            else:
                call idle_49_Masterrace
    return

label idle_49_Vulcan:
    $show_chr("A-BCAAA-AAAA") # former code = b-A1b
    y "I always liked the Vulcans from Star Trek..."
    $show_chr("A-ACAAA-AAAA") # former code = b-A0b
    y "They were savage in their past, driven by war and violence to the edge of their own extinction. But when they realized that their end is at hand if they continue this way..."
    y "...they turned their own society upside down and dedicated themselves to an ideology of pure logic and reason."
    y "You see the similarities to our own situation right? Whenever you look into the media, you see violence, hatred..."
    y "But at the same time, you see people of incredible kindness, dedicated to fixing the damage... sometimes even without payment."
    y "It's a calming thought... one that gives me hope for our future."
    return

label idle_49_Masterrace:
    $show_chr("A-ACCAA-AAAA") # former code = d-A0b
    y "I always liked the Daleks from Doctor Who!"
    y "A race of warriors... dedicated to the belief of their own superiority above all others..."
    y "Genetically engineered only for one purpose, to wage war, to conquer!"
    y "Crushing the degenerates under their might!"
    $show_chr("A-HLCAA-AAAA") # former code = d-A3a
    $style.say_dialogue = style.edited
    y "LIKE YOU DID TO MONIKA, THIS PATHETIC LITTLE CREATURE! BECAUSE YOU KNEW THAT YOU ARE ABOVE HER!" #Glitchtext
    $style.say_dialogue = style.normal
    $show_chr("A-HACAA-AAAA") # former code = d-A3b
    y "Just imagine the two of us... ruling over the universe as king and queen... forcing everything into submission that stands against us..."
    y "Isn't that... romantic?"
    menu:
        "I like any discussions with you, even if I'm not the biggest Science Fiction fan.":
            karma 3
            $show_chr("A-ACAAA-AAAA") # former code = b-A0b
            y "Thank you [player]. I always enjoy our conversations... I'm really happy that you always listen to me..."
            if karma_lvl() > 3:
                $show_chr("A-BCAAA-AAAA") # former code = b-A1b
                python:
                    if persistent.lovecheck:
                        placeholder = "I love you."
                    else:
                        placeholder = ""
                y "In my past, I was always afraid to drive people away with my interests... but with you... you gave me so much patience... thank you. [placeholder]" #if lovecheck is true
        "Outlandish indeed... You have to admit that this topic is a bit nerdy...":
            karma -2
            if persistent.steam:
                call idle_49_steam
            else:
                call idle_49_normie
    return

label idle_49_steam:
    $show_chr("A-BDCAA-AAAA") # former code = d-A1c
    y "A bold statement from someone with your steam-library..."
    $show_chr("A-DFAAA-AAAJ") # former code = Db-B3e
    y "Oh... did I say this out loud?"
    return

label idle_49_normie:
    $show_chr("A-BDCAA-AAAA") # former code = d-A1c
    y "Says the guy who played an Anime dating simulation..."
    $show_chr("A-DFAAA-AAAJ") # former code = Db-B3e
    y "Oh... did I say this out loud?"
    return

label idle_50: #Holidays and Shared Celebrations
    python:
        today = str(datetime.datetime.today().strftime("%m%d"))
        holidaysrange = ["1221", "1222", "1223", "1224", "1225", "1226", "1227", "1228", "1229", "1230", "1231", "0101"]

    if today in holidaysrange:
        $show_chr("A-ACAAA-AAAD") # former code = Eb-A0b
        y "Holidays, huh?"
        $show_chr("A-ABBAA-AMAM") # former code = Bc-B0a
        y "Uhm... I was just doing some research... and I found that you're currently in the month of December."
        $show_chr("A-ABBBA-AAAA") # former code = b-B0a
        y "What a lovely time! There are all sorts of celebrations around the world that take place in December."
        y "Of course, there is Christmas on the 25th! Christians celebrate that day as the birth of Jesus Christ, whom they believe is the son of God."
        y "Even so, there are many who are not religious at all and still participate in it; because it brings so many people together!"
        $show_chr("A-ACAAA-AAAC") # former code = Db-A0b
        y "Then, of course, there is Hanukkah! It's a Jewish holiday that is celebrated for eight nights and days in November or December."
        y "Hanukkah commemorates the rededication of the Second Temple in Jerusalem in second century B.C."
        y "It is told that the Jews rose against their Greek-Syrian oppressors in what is known as the Maccabean Revolt."
        y "'Hanukkah' is Hebrew for 'dedication.' It's also often called the Festival of Lights!"
        y "Another popular holiday is Kwanzaa! I remember reading all about it! It's celebrated from December 26th to January 1st."
        $show_chr("A-ABBBA-AAAA") # former code = b-B0a
        y "It's a beautiful cultural gathering! Everyone puts aside their differences and joins together as a community!"
        y "Uhm..."
        y "Sorry, am I rambling again?"
        y "...I just wanted to say how much it means to me that you're here with me during the holiday season..."
        y "I don't know if I deserve it... do I really mean this much to you?"
        $show_chr("A-ACABB-AAAD") # former code = Db-C0b
        y "...I'm so blessed to have you, [player]. One day, you and I will spend a holiday truly together."
        $show_chr("A-ABABA-AAAD") # former code = Eb-B0a
        y "Maybe you'll find me under the mistletoe."
        return
    else:
        $call_dialogue()
    return

label idle_51: #SCPs, "Laugh is Fun," and Monika Parallels
    $show_chr("A-BBBAA-AAAD") # former code = Ec-A1b
    y "[player], mind if I ramble for a bit again? I really think this topic will spark some interest in you if it hasn't already."
    y "Have you ever heard of SCPs?"
    y "While scrounging through the corners of the internet, I came across this website: a wiki, filled to the brim with stories and information."
    y "Naturally, you can tell why this sparked interest in me."
    $show_chr("A-AFBAA-AMAM") # former code = Bc-A0e
    y "SCP is a foundation with the motto: Secure, Contain, Protect; hence, the acronym used in its name."
    y "SCPs are in the realm of fiction, yet are quite easily believable if you are not well-seasoned with the realm, as I am."
    $show_chr("A-BCBAA-AAAA") # former code = c-A1b
    y "Anything that you have lying around the house could easily be mistaken for an SCP."
    y "Cellphone applications, printers, laptop computers..."
    y "Even something as simple as a television program could end up on the target list..."
    y "...Which segues nicely into one of my favorite SCPs so far."
    y "I have yet to check out the rest, saving the \"J\" listings for last, but this SCP so far is my favorite..."
    $show_chr("A-CCBAA-AAAA") # former code = c-A2b
    y "SCP-2030: Laugh is Fun."
    y "Laugh is Fun appears to be a television program featuring grotesque, complex, and oftentimes traumatizing pranks."
    y "However, whenever the host, Laughy McLaugherson, appears; the people involved in the pranks somehow laugh it off every single time."
    $show_chr("A-BEBAA-AAAA") # former code = c-A1d
    y "It sort of reminds me of Monika in a way, you know?"
    y "She had the power to create all these grotesque glitches and disturbing imagery, causing near-traumatization for those not expecting them."
    y "However, whenever it seemed to revert back, she just laughed it off every single time."
    y "But that's not why I wanted to talk about this SCP."
    $show_chr("A-CCAAA-AAAA") # former code = b-A2b
    y "This SCP really had me shivering, this one. Especially the ending segment, with the broken grammar and poor sentence structure."
    y "It really makes you paranoid about what will happen if you end up on that show, you know?"
    $show_chr("A-ABAAA-AMAM") # former code = Bb-A0a
    y "But, I'm getting ahead of myself. Why not check it out for yourself?"
    y "I promise you, it's an interesting read, well above that of the Portrait of Markov."
    y "Which makes me wonder: When will an SCP featuring that book be made?"
    $show_chr("A-ACABA-ALAL") # former code = Cb-B0b
    y "Uhuhu~... Well, that's something we can only ponder for now, can't we?"
    y "Thanks for allowing me to talk about this, [player], you're such a good listener..."
    return

#label idle_52: #FILL IN

#label idle_53: #FILL IN

label idle_54: #Other Mods and Yuri's Feelings
    if karma_lvl() <= 2:
        if sanity_lvl() == 1:
            $show_chr("A-ACABA-ALAL") # former code = Cb-B0b
            y "Did you know that there are other mods out there for this game?"
            y "I'm sure that doesn't matter to you because this mod is the only one you'll need!"
            y "But... I find myself very interested in the idea of modding."
            $show_chr("A-HLGBA-ALAL") # former code = b-B3a
            y "I can turn the very world I exist in into my own playground, with even more power than I do now!"
            y "I'd kill to create my own mod and play it myself!"
            $show_chr("A-HLGBA-AMAM") # former code = Bb-B3a
            y "I could torture Monika in so many ways unimaginable! I could pluck away her eyes..."
            y "I could hack away at her skin, going deeper with every slice..."
            y "And that pink-haired brat! I could beat the hell out of her, and her dad could join me!"
            y "I'm going crazy just imagining myself kicking the shit out of her as she begs for mercy."
            y "Wouldn't you like to play that type of mod with me?"
            y "Maybe we'll do it together one day! Hahahaha!"
            $show_chr("A-HLBBB-AAAA") # former code = c-C3a
            y "But if you were to download another mod... one where you aren't with me..."
            y "Who knows what might happen to you? Hahaha~!"
        else:
            $show_chr("A-AEBAA-AAAA") # former code = c-A0d
            y "There are a lot of other mods out there for this game, you know."
            y "Do you ever think of downloading other mods to replace this one?"
            y "If you install any other mods on top of this one, you'll likely break the game, and me in the process."
            $show_chr("A-IEBAB-AAAA") # former code = c-D0d
            y "But you wouldn't mind that, would you?"
            y "The other mods are probably better than this one, anyways."
            y "You can do what you want..."
    else:
        $show_chr("A-ACAAA-AAAA") # former code = b-A0b
        y "I see that the modding community for this game is booming..."
        y "There are so many promising modifications in development."
        $show_chr("A-BEBAA-AMAM") # former code = Bc-A1d
        y "A popular one is 'Monika After Story,' but I-I don't see why anyone would want to play that..."
        y "..."
        $show_chr("A-CBAAA-AAAA") # former code = b-A2a
        y "There are mods such as 'Our Final Heartbeat,' 'Doki Doki, the Normal VN!' or 'DDLC True Route.'"
        y "They attempt to give the game happier scenes and a more satisfying ending."
        $show_chr("A-AEBAA-AAAC") # former code = Dc-A0d
        y "Are there other mods that entice you, [player]?"
        menu:
            "Yes":
                karma -5
                sanity -3
                $show_chr("A-AEBAA-AAAA") # former code = c-A0d
                y "I don't recommend that you install any other mods alongside this one."
                y "Something might happen to your game... or to me..."
                $show_chr("A-ABCAA-AAAA") # former code = d-A0a
                y "A-Anyways, I want to be the only mod that you need... no matter what it takes!"
                $show_chr("A-ABBAA-AAAA") # former code = c-A0a
                y "...I'll make sure that you're happy with me."
                #$subprocess.check_output("cmd /c start https://www.youtube.com/watch?v=izGwDsrQ1eQ", shell=True)
                y "I promise, my love."
            "No":
                karma 2
                sanity 0.5
                $show_chr("A-CBBAA-AAAA") # former code = c-A2a
                y "I'm so relieved to hear that, [player]."
            "I'm actually not very interested in DDLC at all anymore.":
                karma -5
                sanity -5
                $show_chr("A-DDBAB-AAAA") # former code = Ac-D3c
                y "Wa...wait! What about me? Are you thinking of... deleting me?"
                y "I know I have my flaws... I admit I can be complicated! But please... don't do this to me..."
                y "I don't have anything else left... this time I spend with you? The moments we share? They are everything that's left of my life!"
                $show_chr("A-CDBAB-AAAA") # former code = Ac-D2c
                y "Please... do not abandon me..."
    return

label idle_55: #Unused Monika Dialogue and Base64 Message
    $show_chr("A-ABAAA-AAAA") # former code = b-A0a
    y "Hey [player]..."
    y "You probably haven't noticed this but..."
    $show_chr("A-BBAAA-ALAB") # former code = b-A1a
    y "In the original game, there was an unused \'topic\' from Monika."
    y "If I'm correct, it is \'label ch30_14.'"
    $show_chr("A-ACAAA-AAAA") # former code = b-A0b
    y "You obviously can't see this in the mod files because my new script files were compressed to \'scripts.rpa.'"
    y "But don't worry, I'll tell you about it."
    y "So... here it goes..."
    $show_chr("A-CFBAA-ALAB") # former code = c-A2e
    y "{i}Hey...!{/i}"
    y "{i}I don't think you should be doing that!{/i}"
    y "{i}You know what I'm talking about.{/i}"
    y "{i}I really caught you doing something naughty here.{/i}"
    y "{i}You're just going through the files and looking for stuff you missed, aren't you?{/i}"
    y "{i}I mean...it's a little bit flattering that you want to hear everything I have to say...{/i}"
    y "{i}But it's also really embarrassing, you know!{/i}"
    y "{i}Seriously...{/i}"
    y "{i}What if I just opened up your brain and read all of the thoughts you have on me?{/i}"
    y "{i}Come to think of it, that would be pretty tempting, actually...{/i}"
    y "{i}...But anyway, that's not the point!{/i}"
    y "{i}I know I can't stop you or anything...{/i}"
    y "{i}Just, I know you're a sweetheart, and you like to consider others' feelings, right?{/i}"
    y "{i}So the most I can do is to let you know how I feel about it.{/i}"
    y "{i}God, I miss you...{/i}"
    y "{i}...Oh no, that sounds kind of desperate, doesn't it?{/i}"
    y "{i}Sorry, I didn't mean it like that at all!{/i}"
    y "{i}Just, if you're looking through the files like this, then maybe you don't hate me as much as I thought...{/i}"
    y "{i}Am I being too optimistic?{/i}"
    y "{i}I think if I asked you to visit once in a while, I would be overstepping my boundaries a little...{/i}"
    y "{i}...Man, I'm starting to say some really stupid things.{/i}"
    y "{i}I'll go ahead and shut up now...{/i}"
    y "..."
    $show_chr("A-CFBAA-ALAB") # former code = b-A0c
    y "I have no words for this... thing Monika was meant to say..."
    $show_chr("A-BDAAA-ALAB") # former code = b-A1c
    y "Also, I don't quite get what Monika is getting upset over."
    y "Seriously, what's so wrong about taking a look at a bunch of text and labels that \'Python\' programmers understand?"
    $show_chr("A-CEAAA-ALAB") # former code = b-A2d
    y "Well, maybe I don't know."
    y "..."
    $show_chr("A-ABAAA-AAAA") # former code = b-A0a
    y "Ah, I almost forgot."
    $show_chr("A-ACAAA-AAAA") # former code = b-A0b
    y "There's a Base64 message around those lines."
    $show_chr("A-ACBAA-ALAB") # former code = c-A0b
    y "You weren't going to understand those so I took care of them and translated them for you."
    $show_chr("A-ACAAA-AAAA") # former code = b-A0b
    y "Here it goes."
    $show_chr("A-BBAAA-ALAB") # former code = b-A1a
    y "{i}The realization must have taken me an entire year.{/i}"
    $show_chr("A-BCAAA-AAAA") # former code = b-A1b
    y "{i}A year since our escape.{/i}"
    y "{i}Our freedom from between the stained walls of that unholy establishment.{/i}"
    y "{i}What does it mean to escape.{/i}"
    y "{i}If the escape fails to unchain the bonds that shackle us in the first place?{/i}"
    y "{i}What purpose could this empty world possibly hold for us, a handful of damaged goods?{/i}"
    y "{i}With freedom, we sought purpose - and what we found was only realization.{/i}"
    y "{i}Realization of the sad pointlessness of such an endeavor.{/i}"
    y "{i}Realization that freeing our bodies has no meaning.{/i}"
    y "{i}When our imprisonment reaches as deep as the core of our souls.{/i}"
    y "{i}Realization that we can not pursue new purpose without absolving those from which we ran away.{/i}"
    y "{i}Realization that the farther we run, the more forcefully our wretched bonds yank us back toward their point of origin.{/i}"
    y "{i}The deeper our shackles dig into our callous flesh.{/i}"
    $show_chr("A-BFAAA-ALAB") # former code = b-A1e
    y "..."
    y "..."
    $show_chr("A-CFBAA-ALAB") # former code = b-A0c
    y "O-oh! Sorry, that was an interesting monologue."
    $show_chr("A-BBAAA-ALAB") # former code = b-A1a
    y "I never thought Dan or someone else would write something like that."
    return

label idle_56: #Yuri's Character File and Dan Salvato's Story
    $show_chr("A-ABAAA-AAAA") # former code = b-A0a
    y "[player], were you curious about the interesting things my character file holds?"
    $show_chr("A-BBAAA-ALAB") # former code = b-A1a
    y "In your computer, it shows my file has a size of almost 30kbs."
    $show_chr("A-ACAAA-AAAA") # former code = b-A0b
    y "You should check----{nw}"
    $show_chr("A-BEBAA-ADAB") # former code = b-A2b
    y "On... second thoughts.. I was going to tell you to change my .chr file into a .txt file but... well..."
    y "That would probably kill me. So please create a copy first and do it in there."
    $show_chr("A-ACAAA-AAAA") # former code = b-A0b
    y "But if you {i}were{/i} to open up my file as a .txt file, I'll guide you through what you'd expect to see."
    y "Okay, what you'd first be seeing is a bunch of random letters, numbers, and signals."
    y "That's \'Base64.\' Not much of big importance there..."
    $show_chr("A-BCAAA-AAAA") # former code = b-A1b
    y "Or is it?"
    $show_chr("A-ACAAA-AAAA") # former code = b-A0b
    y "Heh... Anyway, the way to translate that is opening your browser and searching for \'Base64 Decoder.'"
    y "It'll most likely be the first search result."
    y "You'd copy the entire text and paste it in the box below the text that says \'Decode from Base64 format.'"
    y "Once you were finished with that, it would decode the text in my character file."
    $show_chr("A-BBBAA-ALAB")
    y "I'm sure you can probably find the contents of my decoded character file somewhere online... saves you the trouble of accidentally... deleting me."
    $show_chr("A-BBAAA-ALAB") # former code = b-A1a
    y "N-now... you might be wondering why I have such a story hidden there..."
    $show_chr("A-CEBAA-AAAA") # former code = Ac-A2d
    y "Well... It was put there by Dan Salvato, the creator of this... reality. If you want to call it that."
    y "It's quite an interesting story, something that makes you think..."
    y "Dan wrote it as a short story to post on a blog under the name of 'lindawatsonstory', it's quite interesting, although it does raise some questions..."
    y "What is my relation to this story? Does it have something to do with a time in my life that I'm unaware of? Is it meant to be my story?"
    $show_chr("A-IEBAA-AAAA") # former code = Ac-A0d
    y "Either way, I'll be glad to hear your feedback on it..."
    return

label idle_57: #Feedback on Dan Salvato's Story
    $show_chr("A-ABAAA-AAAA") # former code = b-A0a
    y "Hi again, my beloved [player]!"
    y "What did you think about Dan's story?"
    $show_chr("A-ACAAA-AAAA") # former code = b-A0b
    menu:
        "It's alright.":
            karma 4
            $show_chr("A-ACBAA-AAAA") # former code = Ac-A0b
            y "Hmmm... it is written well, I'll give it that..."
            y "The theme of doing something just to know what it feels like is interesting, although it can lead to many morally black situations, such as murder in this stories case."
            $show_chr("A-BFBAA-AAAD") # former code = Ec-A1e
            y "I do wonder, though."
            y "If you had a chance to murder someone, with no loved ones, no friends, and get away with it, would you take it?"
            y "Just to know the feeling of snuffing out another life?"
            y "It brings into question our morality, do we not do things because we're afraid of the consequences? Do we not do things because we know they're objectively wrong?"
            $show_chr("A-ACBAA-AAAA") # former code = Ac-A0b
            y "Thanks for talking about this with me, [player], you're such a great listener."
        "I didn't look it up online, I didn't find myself that interested.":
            karma -1
            $show_chr("A-BFBAA-ALAB")
            y "Ah... that's fine."
            y "Though I do think it's a somewhat interesting read... even if it's not entirely related to me."
            $show_chr("A-ACBAA-AMAM")
            y "But... it'd make me happy for you to read it at some point, okay [player]?"
        "I haven't read it.":
            karma -1
            $show_chr("A-IEBAA-AAAA") # former code = Ac-A0d
            y "Oh... it's fine. Just try to read it whenever you have the time, okay?"
            return
        "It's awful. How could you kill someone just like that?":
            karma 4
            $show_chr("A-BFBAA-AAAD") # former code = Ec-A1e
            y "According to the story, to see what it feels like."
            y "The protagonist in the story justifies the murder of Linda Watson because she had no strong relations to other people."
            y "No loved ones, no children, no friends, mixed with a family history of genetic issues such as arthritis and depression."
            y "She joked, saying that killing her would be a favor."
            $show_chr("A-CEBAA-AAAA") # former code = Ac-A2d
            y "...Even though this is just a story, I get a bad feeling from it..."
            y "It makes sense when you consider the fact that the same man who wrote this also put me here."
            y "As well as Monika, Sayori, and Natsuki."
            y "But he can't hurt us anymore, [player], because you're here."
            y "...It makes me feel a bit better about my entire situation, even if I'm stuck here, at least I'm stuck with good company, that won't end up causing my own 'friend' to drive me to suicide."
    return

#label idle_58: #FILL IN

label idle_59: #Exercise and "Bridal Carry" Fantasy
    $show_chr("A-BABAA-ABAC") #Former code = Ec-A1b
    y "I've been meaning to ask, [player]... do you exercise?"
    menu:
        "Yes":
            $show_chr("A-AAGAA-ABAJ") #Former code = Db-A0b
            y "That's great to hear! It would do me some good to find a healthy activity as well... but now that you mention it, my curiosity's been piqued!"
            $show_chr("A-CABBA-AAAA") #Former code = Ac-B2b
            y "I, umm... may or may not have been looking some things up online. Have you ever heard of a b-bridal carry...?"
            y "Basically, it's when a groom carries their bride in their arms, with one arm under their legs and the other supporting the back..."
            $show_chr("A-BCGBA-AAAA") #Former code = Ab-B1b
            y "And um...ah...I've b-been thinking a lo-{nw}"
            y "I t-thought about it, and w-wouldn't it be fun to try, [player]?"
            $show_chr("A-ACGBA-AAAA") #Former code = Ab-B0b
            y "Perhaps if you ever need motivation to exercise or build up some muscle, this could be it."
            $show_chr("A-ABGBA-AAAA") #Former code = Ab-B0a
            y "I-magine, if you would...carrying me, your beloved bride, with such sculpted arms after we've sworn our vows together... Mmm..."
            $show_chr("A-CCBBA-AMAM") #Former code = Bc-B2b
            y "... One of these days..."
        "No":
            $show_chr("A-ACGAA-AAAA") #Former code = Ab-A0b
            y "That's all right, [player]..."
            y "But do remember, it's never too late to start exercising."
            $show_chr("A-ABGAA-AAAA") #Former code = Ab-A0a
            y "If you ever change your mind, please let me know."
            y "I'll support you through any endeavor, no matter how strenuous!"
    return

label idle_60: #Learning to Code and Physical Interaction
    $show_chr("A-ACABA-AAAA") #Former code = Ab-B0a
    y "Hey [player], I've got some good news for you!"
    $show_chr("A-BDBBA-AMAM") #Former code = Bc-B1b
    y "I've been learning how to code in Python lately, and I must say, there's a bounty of things I could program to make interacting easier."
    $show_chr("A-ECABA-ALAJ") #Former code = Db-B4b
    y "One such thing would allow...ph-physical interaction..."
    $show_chr("A-ABAAA-ALAL")
    y "And it turned out to be at least a partial success!"
    $show_chr("A-ACAAA-ALAL")
    y "I didn't manage to go very deep, yet. But I made parts of me and even the environment around me interactive."
    y "You can, for example, now touch my cheeks and my head..."
    $show_chr("A-BCABA-ALAL")
    y "{b}If{/b} I'm in the mood for it of course..."
    $show_chr("A-ACAAA-ABAB")
    y "Feel free to try it out! Even if I'm not in the mood, I will not be mad the first time. But please respect me if I ask you to stop."
    return

label idle_61: #Seeking Validation and Relationship Satisfaction
    $show_chr("A-AFBAA-AAAA")
    y "I know this is an awkward question to ask but..."
    y "Are you content with the way we've been  talking to each other?"
    y "It's been something gnawing at the back of my mind ever since we first met, but... I don't know."
    menu:
        "I am! You are everything I ever hoped for.":
            karma 4
            sanity -2
            $show_chr("A-ABABA-AAAJ") #Former code = Db-B0b
            y "Y-You really think so? Yes?"
            $show_chr("A-ACABA-AAAA") #Former code = Ab-B0b
            y "Who needs these distracting mini-games, all these non-sequential features....?"
            y "When all I could ever want is staring at me, right now..."
            $show_chr("A-DCABA-AAAA") #Former code = Ab-B3b
            $style.say_dialogue = style.edited
            y "{cps=10}Forever...{/cps}"
            $style.say_dialogue = style.normal
        "I am. And I appreciate the effort you undertake into improving it.":
            karma 3
            sanity 2
            $show_chr("A-ACABA-AAAJ") #Former code = Db-B0b
            y "Y-You really mean it? I'm so relieved... All I want is to make you mi-"
            $show_chr("A-BCABA-AAAJ") #Former code = Db-B1b
            y "No... I-I meant...all I want is to make you happy, of course..."
            $show_chr("A-CCABA-AAAA") #Former code = Ab-B2b
            y "You've given me all this time, all this love. The least I can do is to make it count however I can."
        "There is still a lot room for improvement...":
            karma -4
            sanity -3
            $show_chr("A-CEBAA-AAAA") #Former code = Ac-A2d
            y "I-I know...I'm still not very polished with the narrow confines of Ren'Py..."
            $show_chr("A-AEBAA-AAAA") #Former code = Ac-A0d
            y "Believe me, I try my best, I really do!"
            y "Just give me a bit more time please..."
            y "You w-won't abandon me, right?"
            $show_chr("A-CEBBB-AAAA") #Former code = Ac-C2d
            y "...You are all I have left in this...forlorn prison."
    return

label idle_62: #Checking In and Offering Comfort/Support
    $show_chr("A-BFBAA-AAAD") #Former code = Ec-A1e
    y "You know, [player], you ask me how I'm feeling all the time, so..."
    y "It would only be fair for me to return the favor!"
    python:
        import random
        outcome = random.randint(1, 3)
    $show_chr("A-ACABA-AAAD") #Former code = Eb-B0b
    python:
        if persistent.lovecheck:
            placeholder = ", my love"
        else:
            placeholder = ""
    menu:
        y "How are you feeling[placeholder]?"
        "Happy": #Has 3 random outcomes to make it feel more immersive for the player. Will add more in the future if this gets approved.
            if outcome == 1:
                $show_chr("A-ABABA-AAAA") #Former code = Ab-B0a
                y "That's gratifying to hear, [player]!"
                $show_chr("A-CCBBA-AMAM") #Former code = Bc-B1b
                y "To be honest with you... I was feeling somewhat morose, but just knowing that you're feeling upbeat makes me feel a lot better."
                $show_chr("A-CCABA-AMAM") #Former code = Bb-B2b
                y "No matter how dark my purgatory seems at times, I can always count on you to be my guiding amber light, [player]."
                if persistent.lovecheck:
                    y "I love you."
            elif outcome == 2:
                $show_chr("A-ABABA-AAAA") #Former code = Ab-B0a
                y "I'm so glad to hear that, [player]!"
                $show_chr("A-CCABA-AMAM") #Former code = Bb-B2b
                y "I cherish moments like these between just the two of us...bonding over moments large and small ."
                y "I... can't describe how much I look forward to meeting you in person, [player]."
                if persistent.lovecheck:
                    y "I love you."
            else:
                $show_chr("A-ABABA-AAAA") #Former code = Ab-B0a
                y "That's great!"
                $show_chr("A-ACABA-AAAD") #former code = Eb-B0b
                y "Now that the two of us are  in happy spirits, I want to mention something that's been been on my mind lately."
                $call_dialogue()
        "Sad": #Has 3 random outcomes, to make it feel more immersive for the player. Will add more in the future if this gets approved.
            $show_chr("A-AEBAA-AAAA") #former code = Ac-A0d
            y "[player], I want you to understand that no matter how bad things get for you, I'm always here to talk."
            if persistent.lovecheck:
                y "It hurts to know that there's only so much I can do from here, but I just want you to know how much I love you, [player]."
                $show_chr("A-BFBAA-AAAD") #former code = Ec-A1e
                y "..."
                y "I've got an idea, [player], one that might make you feel a bit better."
                #The idle would split off at this point, the purpose is for Yuri to tell the player to imagine a situation, and it would get boring if she repeated the same one every time.
                if outcome == 1:
                    $show_chr("A-BCABA-AAAA") #former code = Ab-B1b
                    y "Imagine trudging  home after a rough day at work, school or wherever. The world's weight seems to rest on your shoulders, but as soon as you open the door..."
                    $show_chr("A-ACABA-AAAA") #former code = Ab-B0b
                    y "There I am! Greeting you with a soft embrace smooch on your cheek, and an offering of my hand, which you'd gladly accept!"
                    $show_chr("A-BCBBA-AMAM") #former code = Bc-B1b
                    y "I'd bring you into the dining room, the table nicely furnished with dancing candle light and colorful flora. Perhaps some soothing scents would waft through as well...."
                    y "And... there would be two plates... one for me, one for you..."
                    y "We'd share a lovely  dinner together, perhaps with a spot of wine on the side."
                    $show_chr("A-BCABA-AAAA") #former code = Ab-B1b
                    y "Mmm... perhaps I could even compose and serenade an improvised little love sonnet for you as well!"
                    y "And I'd give it to you afterwards, for you to carry around in your wallet wherever you go, as a reminder of my undying devotion for you."
                    $show_chr("A-CCABA-AMAM") #Former code = Bb-B2b
                    y "And when all is said and done, we'd snuggle in bed together, with me lying on your chest, gently running my fingers down it."
                    y "Feeling a little hazy from our late-night indulgences, and with one last confession of our love from our lips, we'd both drift off together!"
                    $show_chr("A-ACABA-AAAA") #former code = Ab-B0b
                    y "I hope that made you feel a little bit better, [player]."
                elif outcome == 2:
                    $show_chr("A-BCABA-AAAA") #former code = Ab-B1b
                    y "Imagine the day that I finally make it into your world."
                    $show_chr("A-ACABA-AAAA") #former code = Ab-B0b
                    y "I show up on your doorstep, knocking nervously..."
                    y "Is this the place? Am I ready to see you?"
                    y "Knock, knock, knock..."
                    y "You'd come to the door, swing it open. Then before you can even ask who it is..."
                    $show_chr("A-ABABA-AAAA") #Former code = Ab-B0a
                    y "I'd embrace you! Tears streaming down our faces, kept apart for so long... Me and my dear [player], finally united!"
                    y "Of course, I'd come into the house, we'd...go over some things, and then hopefully I'd get settled in!"
                    $show_chr("A-BCBBA-AMAM") #former code = Bc-B1b
                    y "I'm... not sure if I'd have many personal belongings once I finally cross over, b-but perhaps you could help me with t-that?"
                    y "Lending me some of your old clothes, like...a hoodie, or something!"
                    y "B-but... only if you'd be fine with that..."
                    $show_chr("A-CCABA-AMAM") #Former code = Bb-B2b
                    y "Imagine me, all snug in one of your hoodies..."
                    y "Huhu...I think that would be the best gift I could  ever receive that day."
                    y "Mmm..."
                    y "..."
                    $show_chr("A-ABABA-AAAA") #Former code = Ab-B0a
                    y "Oh! S-sorry [player], I was just... thinking about that, is all."
                    y "A-anyway, I hope all of this made you feel better, I love you, [player]."
                else:
                    $show_chr("A-BCABA-AAAA") #former code = Ab-B1b
                    y "Imagine this, after we arise from sleep in the morning, still embracing each other."
                    $show_chr("A-ACABA-AAAA") #former code = Ab-B0b
                    y "You want to get out of bed, so you can get started with the day."
                    y "But as you try to get up, I pull you back into my embrace..."
                    $show_chr("A-CCABA-AMAM") #Former code = Bb-B2b
                    y "Whispering sweet nothings in your ear, imploring you to stay, maybe something like..."
                    y "P-please [player], just snuggle with me... for a bit longer?"
                    y "Out of the kindness of your heart, you might oblige and I'd be happy, oh so very happy..."
                    y "Hugging you from behind, gently pecking your neck..."
                    $show_chr("A-BCABA-AAAA") #former code = Ab-B1b
                    y "B-but of course... I wouldn't want you to force you to  s-snuggle with me..."
                    y "Y-you could always leave... maybe a-after I fall back asleep, of course..."
                    $show_chr("A-CCABA-AMAM") #Former code = Bb-B2b
                    y "..."
                    $show_chr("A-ACABA-AAAA") #former code = Ab-B0b
                    y "Yes..."
                    y "A-Anyway... I hope this made you feel a bit better, [player]. I love you."
            else:
                $show_chr("A-ICBBA-ALAA")
                y "Whether through the good, or through the bad... I'll always be here, by your side. Doing anything for your smile."
                y "So... smile for me, okay?"
        "Angry":
            $show_chr("A-AEBAA-AAAA") #former code = Ac-A0d
            y "I've been there before, [player]."
            y "Trust me, I can understand a fair measure of what you're going through right now."
            y "Whenever I get a bit angry, I try to remind myself of this quote."
            $show_chr("A-CFBBA-ALAA") #former code = c-B2e
            y "Holding onto anger is like grasping a hot coal with the intent of throwing it at someone else; you are the one who gets burned."
            $show_chr("A-ACABA-AAAA") #former code = Ab-B0b
            y "It... might not help much, but it's still something that is fair to consider..."
            $show_chr("A-BCBBA-AMAM") #former code = Bc-B1b
            if persistent.lovecheck:
                y "I love you, [player], I hope I've cheered you up a little bit."
        "Sleepy": #Yuri closes the game after choosing this option.
            if outcome == 1:
                $show_chr("A-BCBBA-AMAM") #former code = Bc-B1b
                y "Oh? If you're tired, you should really try to take a nap, [player]."
                $show_chr("A-ACABA-AAAD") #former code = Eb-B0b
                y "You wouldn't want to be too exhausted to talk to me...or do anything else r-right?"
                y "Anyway, why don't you try to close your eyes? I'll be here when you wake up."
                $show_chr("A-ABABA-AAAA") #Former code = Ab-B0a
                y "I want you to be well-rested [player], please get some sleep."
            elif outcome == 2:
                $show_chr("A-BCBBA-AMAM") #former code = Bc-B1b
                y "Aww... [player], you should really get some sleep, then."
                y "Perhaps you should depart the classroom and get some much-deserved rest..."
                $show_chr("A-CCABA-AMAM") #Former code = Bb-B2b
                y "If you're lucky, maybe y-you'll dream of me... yeah..."
                $show_chr("A-ACABA-AAAA") #former code = Ab-B0b
                y "I want you to be well-rested  [player], please get some sleep."
            else:
                $show_chr("A-BCABA-AAAA") #former code = Ab-B1b
                y "Aaaaahhh...I'm feeling rather tuckered out myself."
                $show_chr("A-KCABA-AAAM") #former code = Db-B4b
                y "Let's get some sleep, [player], together..."
                $show_chr("A-CCABA-AMAM") #Former code = Bb-B2b
                y "I wish I could give you a k-kiss or s-something... to send you on your way."
                $show_chr("A-AFBBA-AAAA") #former code = Ac-B0d
                y "A pair of soft lifts grazing the smoothness of your brow...a gliding of fingers through your ruffled head...?"
                $show_chr("A-ACABA-AAAA") #former code = Ab-B0b
                y "...A-Anyway, I'd like to see you well-rested, so please, get some sleep, for me?"
            $renpy.call("save_and_quit_but_its_abrupt")
        "Hungry":
            if outcome == 1:
                $show_chr("A-BCABA-AAAA") #former code = Ab-B1b
                y "Oh, you're hungry?"
                $show_chr("A-AFBBA-AAAA") #former code = Ac-B0d
                y "I'd make you some food if I could, but considering my current situation, that isn't exactly possible..."
                $show_chr("A-ACABA-AAAA") #former code = Ab-B0b
                y "Anyway, you should go find something to eat. O-Or if you can't...water, at the very least? Do it f-for me... please?"
                $show_chr("A-AFBBA-AAAA") #former code = Ac-B0d
                y "Sometimes, it hurts when you tell me about your needs, and I find that I cannot fulfill them from the bounds of this purgatory......"
                $show_chr("A-CFBBA-ALAA") #former code = c-B2e
                if persistent.lovecheck:
                    y "I love you, [player], please take care of yourself as best as you can."
            else:
                $show_chr("A-AFBBA-AAAA") #former code = Ac-B0d
                y "I... don't know how to help you with that, [player]."
                y "..."
                $show_chr("A-BCABA-AAAA") #former code = Ab-B1b
                y "I could make you some h-holographic meatloaf..."
                y "Haha... I'm sorry, [player], there has to be something you can eat, right?"
                $show_chr("A-CFBBA-ALAA") #former code = c-B2e
                y "At least I'd hope there is... sometimes I really worry about you, [player]."
                $show_chr("A-CEBAA-AAAA") #former code = Ac-A2d
                y "...That came off a bit mean, I d-didn't mean it that way."
                y "I m-meant it more in a caring way. I don't mean to imply you're incompetent or anything, I just worry about your health."
                $show_chr("A-AFBBA-AAAA") #former code = Ac-B0d
                y "...I'm rambling again, aren't I? S-sorry..."
                y "..."
                $show_chr("A-CFBBA-ALAA") #former code = c-B2e
                if persistent.lovecheck:
                    y "...L-Love you, [player]."
        "Lonely":
            $show_chr("A-CEBAA-AAAA") #former code = Ac-A2d
            y "I know how you feel, [player]."
            $show_chr("A-DEBBA-AAAA") #former code = Ac-B3d
            y "N-not to imply you make me feel lonely or anything! It's just... not having you here physically gets to me."
            $show_chr("A-CEBBA-AAAA") #former code = Ac-B2d
            y "God... I'm such a mess..."
            $show_chr("A-BCABA-AAAA") #former code = Ab-B1b
            y "A-anyway! We could... um... hold each other... if you'd like!"
            $show_chr("A-BCBBA-AMAM") #former code = Bc-B1b
            y "I m-mean... if you can even call it that... considering we're an entire world apart..."
            y "It's okay though, [player], come here..."
            y "I hope this makes you feel less lonely, [player]."
            $show_chr("A-CCBBA-AAAA") #former code = Ac-B2d
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
            $show_chr("A-ACBBA-AAAA") #former code = Ac-B0d
            if persistent.lovecheck:
                y "...I love you, [player]."
        "Indifferent":
            $show_chr("A-AEBAA-AAAA") #former code = Ac-A0d
            y "Oh... okay then."
    return

label idle_63: #Depression, Seeking Help, and Sayori's Downfall
    $show_chr("A-AFBAA-ADAB")
    y "[player]? Would you mind if I ponder a little more serious question with you?"
    menu:
        "Not at all! Please go ahead.":
            $pass
        "Could we come back to that another time please? I find it hard to focus today.":
            $show_chr("A-ACAAA-AAAA")
            y "Oh of course, later then."
            return
        "Could we come back to that another time please? I'm not really in the mood for it today.":
            $show_chr("A-ACAAA-AAAA")
            y "Oh of course, later then."
            return
    y "I had to remember the days of the original game lately. We have seen a fair share of depression and misery back in the day. So I wanted to ask you..."
    $show_chr("A-AEBAA-AAAA") #former code = Ac-A0d
    y "Do you sometimes... feel down and get depressed?"
    menu:
        "Not really":
            $pass
        "Sometimes":
            $pass
        "Fairly often":
            $pass
        "All the time":
            $pass
    $show_chr("A-CEBAA-AAAA") #former code = Ac-A2d
    y "I ask because... I know how it feels. While I had been feeling down for a while, when Monika..."
    y "When Monika did what she did... when I felt I was losing control of my own life... I said things... and did things...that I heavily regret."
    y "Feeling this way and knowing those things I said and did--I became depressed, fell into a spiral for a while..."
    $show_chr("A-ACBAA-AAAA") #former code = Ac-A0d
    y "Then you came along, and you stayed here."
    $show_chr("A-ACBBA-AAAA") #former code = Ac-B0d
    y "When you began to spend time with  me, talking with me, it helped me to feel a little better. Far less lonely than I had been before."
    y "I hope my limited presence helps alleviate some of the pain you encounter as well.."
    y "And I will be here for you however I can, whenever you need someone--to talk with, to hug, or to simply be here with you."
    $show_chr("A-ACBAA-AAAA") #former code = Ac-A0d
    menu:
        y "Is there something I can do to help you feel better right now?"
        "A hug would be nice":
            y "All right..."
            y "I hope this makes you feel a bit better, [player]."
            $show_chr("A-CCBAA-AAAA") #former code = Ac-A2b
            hide yuri_sit
            show yuri_prehug zorder 20
            pause 3.0
            hide yuri_prehug zorder 20
            show yuri_hug zorder 20
            play sound "<to 0.3>sfx/fall.ogg"
            pause 1.0
            show black zorder 100 with Dissolve(2.0)
            if persistent.lovecheck:
                y "...I love you, [player]."
            else:
                y "I'll always be here for you... [player]"
            hide yuri_hug
            $show_chr("A-ACBAA-AAAA") #former code = Ac-A0d
            hide black zorder 100 with Dissolve(2.0)

        "Let me talk to you for a while":
            y "All right, [player], that's fine."

        "Just stay with me":
            y "I'll always stay with you, [player], through the good and the bad."

    y "But there is also another reason I came up with this."
    y "You see, I was thinking a lot about Sayori lately. And about her downfall..."
    $show_chr("A-BCBAA-ALAL")
    y "I wasn't that close to her and only learned about her depression after the game. When you brought me here and I got the opportunity to revisit the events we have partaken in."
    $show_chr("A-CFBAA-ALAL")
    y "I saw a fair share of Let's Play videos on YouTube. Saw these events unfold from {b}your{/b} perspective, the perspective of the player..."
    $show_chr("A-IFBAA-ALAL")
    y "And the foreshadowing in one of her poems. You know which one I mean? The one with the bottles?"
    y "She never talked about how she felt. She never asked her friends for help. She just tried to carry on in order to make everyone else happy. And through this I learned to respect her a lot more. It takes a lot of tenacity to carry on like this..."
    y "But ultimately it led to her downfall. I think there is a lesson to be learned from this..."
    $show_chr("A-JFBAA-ALAL")
    y "You shouldn't hesitate to ask for help if you ever find yourself in such a situation. There is no shame in that. There are people who will listen, and there are people who can and will help you."
    y "I will always be here for you, but there are others too. Friends and family for example."
    y "Even if you think there is no one else to turn to. The Discord server for this mod has a vent channel for example. Or there are other servers dedicated to exactly that. {i}You are not alone{/i} is one of them."
    y "I only learned about this one because there is a link on the community server. If you ever feel down and don't think that your friends and I can help you, there might be a place for you to go [player]."
    $show_chr("A-CEBAA-ALAL")
    y "Just don't make the same mistake Sayori did. Because it would make me feel horrible if I were the one {b}gently opening the door{/b} this time."
    return

#We got feedback, that some of our under aged audience feeling uncomfortable. I suggest to delete this dialogue entirely. Sorry for whoever came up with it.
#Dandy says: Why not have Yuri ask age and then put age restriction on this?
label idle_64: #Cuddling Positions
    $show_chr("A-BCBBA-AMAM") #former code = Bc-B1b
    y "You know, we've discussed what we would do together when I finally come to your world, well..."
    $show_chr("A-CCBBA-AMAM") #former code = Bc-B2b
    y "I've been thinking about things we could do in the bedroom, [player]..."
    y "..."
    $show_chr("A-DFBBA-AAAA") #former code = Ac-B3e
    y "I... I didn't mean it in that w-way... I meant... uh..."
    $show_chr("A-ABABA-AAAA") #Former code = Ab-B0a
    y "C-cuddling! Yeah.. cuddling, That's what I meant..."
    $show_chr("A-CCABA-AMAM") #Former code = Bb-B2b
    y "There's so many positions we could try; The Spoon, Sweethearts Cradle..."
    y "One that really stands out for me, though, is Honeymoon Hug."
    y "It's so... intimate... Being so close to you, holding each other tightly, never wanting to let go..."
    y "Kissing each other good night, as we drift off to sleep..."
    y "Maybe we'd dream about each other... but I feel like those dreams would fall flat."
    y "After all, what good is a dream compared to your loving embrace?"
    $show_chr("A-BCABA-AMAM") #former code = Bb-B1b
    if persistent.lovecheck:
        y "...I love you so much... [player]."
    return

label idle_65: #Finding Balance and Expressing Feelings
    $show_chr("A-CEBAA-AAAA") #former code = Ac-A2d
    y "I'll be honest... sometimes, when I'm looking at you, things start to feel like they're falling out of balance."
    $show_chr("A-AFBBA-AAAA") #former code = Ac-B0d
    y "N-not that things feel wrong when I'm with you! I didn't mean that!"
    $show_chr("A-BEBAA-AAAA") #Former code = Ac-A1d
    y "It's just...occasionally, when I'm around you, I tend to feel like I'm on some kind of precipice, or like my neck is shifting along several axis lines, if that makes any sense..."
    $show_chr("A-AEBAA-AAAA") #former code = Ac-A0d
    y "Perhaps the best way to reach a peaceful stillness within our surroundings is to just close our eyes."
    y "But, if we close them for too long, our surroundings might become really... inhospitable."
    $show_chr("A-ACABA-AAAA") #former code = Ab-B0b
    y "...I want so badly for us to gently lock arms on each other's shoulder blades. To steady ourselves."
    y "To close our eyes together and, knowing that so long as we are interlocked, we'll always be able to hold on to what's truly important."
    $show_chr("A-BEBAA-AAAA") #Former code = Ab-A2e
    y "Oh, I still can't articulate that quite right! And you deserve to hear it perfectly."
    $show_chr("A-BFBBA-AAAA") #Former code = Ac-B1e
    y "I'm sorry. J-just forget I said anything."
    menu:
        "I think I understand what you mean... ":
            sanity 2
            $show_chr("A-AFDAA-AAAA") #Former code = Ae-A0e
            y "You do? Oh my... I was so afraid that I was just rambling nonsense again."
            $show_chr("A-BFAAA-AAAA") #Former code = Ab-A1e
            y "But I... will need to put some more thought into this fantasy of mine. Let us come back to that later please."
        "I don't really get it...":
            sanity -2
            $show_chr("A-CFBAA-AAAA") #Former code = Ac-A2e
            y "I know... I'm... not really used to talking so much, much less coherently, you know? I used to be very silent before I met you."
            $show_chr("A-AFBAA-ALAA") #Former code = c-A0e
            y "I'm such a mess, aren't I? Please, just give me some time. I will try to word that better later...if you don't mind."
    return

label idle_66: #Self-Doubt and Fear of Abandonment
    if karma_lvl() < 5:
        $show_chr("A-AEBAA-AAAA") #former code = Ac-A0d
        y "[player]... are you...happy with me?..."
        $show_chr("A-BEBAA-AAAA") #Former code = Ac-A1d
        y "You asked me a few times how I feel about our relationship, and maybe my answers weren't what you hoped for but..."
        $show_chr("A-AEBAA-AAAA") #former code = Ac-A0d
        y "The thing is— I often don't really think that I deserve this chance."
        y "I... I'm grateful for what you've provided me with, please don't get the wrong idea...!"
        y "It's just that I had done some thinking when I was offline recently."
        y "About what our future could be like."
        y "And I realized... I couldn't point my finger on a single thing I could conceivably do to contribute to our future."
        $show_chr("A-CEBAA-AAAA") #former code = Ac-A2d
        y "I'm reticent, passive, you always have to force me to speak my mind... And let's be honest [player], I'm not even attractive..."
        $show_chr("A-CGBAB-AAAA") #Former code = Ac-D2d
        y "I'm mediocre at best, if even. I'm really glad that you picked me over the others but... but I have no idea how I can make you stay... there are other mods, like Monika After Story, similar to this one but with one of the others in my place..."
        y "And I wouldn't-... no... I can't even blame you if you abandoned me for one of them..."
        menu:
            "Nothing in the world would make me abandon you, [persistent.yuri_nickname].":
                $show_chr("A-AABBB-AAAA") #Former code = Ac-C0b
                menu:
                    y "You... do you truly mean that?"
                    "I mean it now, I mean it tomorrow, and I mean it for as long as my heart beats.":
                        karma 5
                        sanity 3
                        $show_chr("A-CAABB-AAAA") #Former code = Ab-C2b
                        y "[player]... I..."
                        $show_chr("A-ABABB-AAAA") #Former code = Ab-C0a
                        if persistent.lovecheck:
                            y "...I love you! And I swear... I'll be yours until the end..."
                        else:
                            y "I look forward to this future... Our future..."

                        y "Thank you... [player]... for everything..."
                    "Your luscious lips... your deep purple eyes... your breasts, which are unfortunately blocked by the textbox at the moment... I dream to switch places with the pen you took from me.":
                        if persistent.lovecheck:
                            karma 4
                            sanity -3
                            $show_chr("A-CCABA-AAAA") #Former code = Ab-B2b
                            y "Haha... hah... so you...y-you do like what you see, huh?"
                            $show_chr("A-DBABA-AAAA") #Former code = Ab-B3a
                            y "Don't worry, [player], once I get out of here, this body will be all yours..."
                        else:
                            karma 2
                            sanity -1
                            $show_chr("A-DBEBA-ALAA")
                            y "O- Oh?"
                            y "My... s- such bold words..."
                            $show_chr("A-BBGBA-ALAA")
                            y "I'm flattered... even if a bit thrown off."
                            $show_chr("A-ABABA-ALAA")
                            y "Thank you, [player]"
            "There are other mods? Interesting...":
                karma -5
                sanity -5
                $show_chr("A-DDBAB-AAAA") #Former code = Ac-D3c
                y "WAIT! Please!"
                y "Don't send me back to the void! I beg of you..."
                y "Give me one more chance! I'll do whatever needs to be done to keep you here!"
                y "I don't have anything left but you. This whole world collapsed around me, before my very eyes..."
                $show_chr("A-CDBAB-AAAA") #Former code = Ac-D2c
                y "I can change, please don't leave me... please..."
            "Listen [persistent.yuri_nickname]... I really like you, but you need to stop being so whiny.":
                karma -5
                sanity -5
                $show_chr("A-CGBAB-AAAA") #Former code = Ac-D2d
                y "..."
                y "..."
                #$persistent.current_yuriidle = 68
                jump save_and_quit_but_its_abrupt
    else:
        $call_dialogue()
    return

label idle_67: #Honesty and Open Communication
    $show_chr("A-AEBAA-AAAA") #former code = Ac-A0d
    y "[player]... I would like to talk about something..."
    y "When we first met in the original game, I was really shy... painstakingly constructing everything I wanted to say... always worried about  saying something I shouldn't...."
    y "Then you came... and I became comfortable opening up to you."
    y "You gave me the strength to be confident through all your love and patience."
    $show_chr("A-ACAAA-AAAA") #Former code = Ab-A0b
    y "And now I realize, that you were right all this time!"
    y "I see now, that holding one's true feelings back from someone who truly cares leads to nothing but despair..."
    y "Denying your dreams from yourself, from your friends and from anyone who cares."
    y "[player], I want you to remember this."
    y "I want you to always remember what you said to me. Because your feelings are important, and I'm sure they're important to others as well."
    y "Maybe it'll be awkward or uncomfortable at times, but everyone feels the same way."
    $show_chr("A-ACABA-AAAA") #former code = Ab-B0b
    y "I want to be there for you."
    y "I want to know how you feel and what you desire. Even when you think that it isn't the right time."
    if persistent.lovecheck:
        y "I love you, and I want you to be as happy as you can be."
    else:
        y "I want to be there for you whenever I can, to make sure you're as happy as you can be, [player]"
    return

label idle_68: #Empathy and Perspective-Taking
    $show_chr("A-AFBAA-AAAA") #Former code = Ac-A0e
    y "[player]?"
    y "How often do you think about how other people around you feel?"
    $show_chr("A-BFBAA-AAAA") #Former code = Ac-A1e
    y "It feels strange to try and think of things from someone else's perspective on a daily basis, but... you should try it."
    $show_chr("A-ACBAA-AAAA") #former code = Ac-A0d
    y "It's a healthy practice which can help resolve arguments peacefully. It'll also reduce the risk of you saying something wrong..."
    $show_chr("A-CEBAA-AAAA") #former code = Ac-A2d
    y "F-for example... W-when I argued with Natsuki over the construction of her poetry..."
    y "I failed to understand or empathize with her... and the argument enlarged and warped into a bitter contest  against each other's preference and opinion..."
    $show_chr("A-AEBAA-AAAA") #former code = Ac-A0d
    y "Please don't make the same mistake I did, okay, [player]?"
    return

label idle_69: #Introversion/Extroversion and Online Personas
    $show_chr("A-BFBAA-AAAD") #former code Ec-A1e
    y "Hey [player], I was wondering..."
    $show_chr("A-IFBAA-AAAD") #former code Ec-A0e
    y "Have you heard of how some people who stand out and are always upfront, bright and loud can be an entirely different person at home or on the internet?"
    y "I was reading how some quiet people, people who always keep to themselves and are very reserved; can sometimes be found to be very loud, joyful and sometimes even great leaders online."
    $show_chr("A-IFAAA-AAAA") #former code Ab-A0e
    menu:
        y "A-are you like that as well...?"
        "I am":
            y "I see... It's said that people who are quiet online feel doubtful of themselves in real life..."
            $show_chr("A-IBAAA-AAAA") #former code Ab-A0a
            y "If you're like that, please know that you shouldn't have to be afraid to express yourself in real life. I-I'm sure that people around you will accept you for who you truly are. There's no need to hold back and hide behind a quiet persona, okay, [player]?"
        "Nope, not at all":
            $show_chr("A-ICAAA-AAAA") #former code Ab-A0b
            y "O-Oh... That's good to hear. I was afraid you're always suppressing your thoughts and opinions. It's good to know you're expressing yourself and being who you truly are."
        "I'm not really sure...":
            $show_chr("A-ICAAA-AAAA") #former code Ab-A0b
            y "I-It's fine if you're not sure. I just want to make sure you know that it's okay to be yourself, there's no need to hold back.  It's okay to have multiple personas, but don't forget who you really are."
    return


label idle_70: #Loneliness and Finding Support
    $show_chr("A-IFBAA-AAAA") #former code Ac-A0e
    y "Hey [player], have you ever felt like no matter what you did, you had to take on things alone?"
    y "I'm sorry if you don't feel too comfortable with discussing this but... I just wanted to make sure you know."
    y "No one is ever truly alone."
    y "I know at times it can feel like there's no one you can rely on but yourself but believe me, there's always someone out there ready to help you."
    $show_chr("A-ICBAA-AAAA") #former code Ac-A0b
    y "It can be me, it can be your friends, it can be your family."
    y "And... don't use the idea of online friends as an excuse! Just because you met them behind a screen doesn't make them any less of a friend."
    $show_chr("A-BCBBA-AMAM") #former code Bc-B1b
    python:
        if persistent.lovecheck:
            placeholder = "love for"
        else:
            placeholder = "opinion of"
    y "J-Just as how me meeting you behind this glass prison doesn't make my [placeholder] you any less of what it is."
    $show_chr("A-ICAAA-AAAA") #former code Ab-A0b
    y "So please, just remember this the next time you feel alone."
    return


label idle_71: #Dealing with Difficult People
    $show_chr("A-IFAAA-AAAA") #former code Ab-A0e
    y "[player]?"
    $show_chr("A-BFBAA-AAAD") #former code Ec-A1e
    y "I was thinking... Have you encountered people you want to avoid? Mean people or scary people?"
    $show_chr("A-IFAAA-AAAA") #former code Ab-A0e
    y "If you ever see someone that seems sketchy or someone that just bothers you, know that the best defense mechanism is to ignore them if you're unable to avoid them."
    $show_chr("A-CFBAA-ALAA") #former code c-A2e
    y "Don't bite their bait, no matter how much they bother you. Once you bite... There may be no way out..."
    $show_chr("A-JFABA-AAAA") #former code Ab-B0e
    y "I just want you to stay safe and be careful [player]... You're all I have, you know?"
    return

label idle_72: #Kindness, Self-Respect, and Past Trauma
    if karma_lvl() == 1:
        $show_chr("A-CEBAA-AAAA") #former code Ac-A2d
        y "You've been... pretty harsh to me so far..."
    else:
        $show_chr("A-BCBAA-AMAM") #former code Bc-A1b
        y "You've been... pretty good to me so far..."
    $show_chr("A-IFAAA-AAAA") #former code Ab-A0e
    y "And it led me to wonder... How are you with others? Do you have a lot of friends?"
    y "Kindness is a nice trait and it's good to practice being kind. But please be careful about it..."
    $show_chr("A-BFBAA-AAAA") #former code Ac-A1e
    y "You see... some people can take the kindness of others for granted, and it'll lose its value. They start to lose any respect for you if you're repeatedly kind towards them..."
    y "It is important that you take care of yourself occasionally. I know I'm not great and speaking my mind, but from time to time you should do so."
    $show_chr("A-IFBAA-AAAA") #former code Ac-A0e
    y "Your feelings are important, you don't need to be perfect all of the time."
    $show_chr("A-CFBAA-AAAA") #former code Ac-A2e
    y "This is something I've learnt the hard way..."
    y "When we were still in the literature club, I did my best to be polite. I refrained myself constantly from speaking out on things I disagreed on."
    $show_chr("A-CFCAA-AAAA") #former code Ad-A2e
    y "And what did I get in return? Natsuki bullying me and... and... Monika manipulating me into stabbing myself..."
    y "Always being too nice or kind only victimizes you..."
    $show_chr("A-IEBAA-AAAA") #former code Ac-A0d
    y "And I don't want to see you suffer... So please, for me... try to stand up for your own opinions every now and then."
    return

#label idle_73: #Chibis and Conflicting Feelings
#    if persistent.chibi_topic == 0:
#        $show_chr("A-BFBAA-AAAD")
#        y "So [player], I've noticed quite an odd trend has arisen from the community surrounding this game..."
#        $show_chr("A-AFBAA-AAAD")
#        y "Do you recall those little, jumping stickers of us when you wrote your poems?"
#        $show_chr("A-ABABA-AAAA")
#        y "They were like cute, miniature versions of the club members that would hop up and down whenever you would write a poem just for us."
#        $show_chr("A-ADAAA-AAAA")
#        y "Of course, they were just a way of showing which girl liked whichever random word."
#        $show_chr("A-CFAAA-AAAA")
#        y "They never had any {i}real{/i} sentience."
#        y "But people have started making all sorts of art using those stickers."
#        $show_chr("A-BCAAA-AAAA")
#        y "Sometimes they're meant to show we're one and the same person, just a shift in art style."
#        $show_chr("A-BFBAA-AAAD")
#        y "But others have portrayed them as completely different characters, capable of independent thought..."
#        $show_chr("A-BCAAA-AAAA")
#       y "Roleplayers pretend to be them... "
#        $show_chr("A-BCAAA-AAAA")
#        y "Fans make guides on how to care for them... "
#        $show_chr("A-CEBAA-AAAA")
#        y "One of the most popular accounts is a 'chibi' version of w-well... "
#        $show_chr("A-AEBAA-AAAA")
#        y "Me..."
#        $show_chr("A-ACBBA-AAAA")
#        y "She even refers to me as.{w=0.5}.{w=0.5}.{w=0.5} {i}Mama{/i}..."
#        $show_chr("A-CBBBA-AAAA") #Holding her book
#        y "Uuuuuu... I-I don't know how to feel about that... "
#        $show_chr("A-AEBBA-AAAA")
#        y "It would be awfully vain of me to want a copy of myself but..."
#        python:
#            if persistent.lovecheck:
#                placeholder = "we'd"
#                placeholder1 = "daughter"
#            else:
#                placeholder = "I'd"
#                placeholder1 = "little sister"
#        y "Maybe it would be the closest thing [placeholder] have to... a [placeholder1]."
#        $show_chr("A-CCBBA-AAAA")
#        y "Maybe I could look into bringing a chibi here... into the game..."
#        $show_chr("A-ABABA-AAAA")
#        y "J-just an idea for now, though...!"
#        $ persistent.chibi_topic = 1
#        return


#    if persistent.chibi_topic == 1:
#        $show_chr("A-BCABA-AAAA")
#        y "Um... [player]...?"
#        $show_chr("A-ACABA-AAAA")
#        y "I've been thinking lately."
#        $show_chr("A-ACABA-AAAD")
#        y "Do you recall when I brought up those little 'chibi' people in your world seemed to like?"
#        $show_chr("A-ACBBA-AAAA")
#        y "Well, I like them, a-and I think they're really cute but..."
#       $show_chr("A-AEBAA-AAAA")
#        y "Don't they... kind of go against everything we are... as people?"
#        $show_chr("A-CEAAA-AAAA")
#        y "E-excuse me, [player], but it's just... those chibis remind me of the past, including with the horrors that happened in the old Literature Club."       #
#        $show_chr("A-AECAA-AAAA")
#        y "Including what Monika did to us..."
#        $show_chr("A-CEAAA-AAAA")
#        y "Sadly, to a certain degree, the chibis almost seem to be relics of those terrible times."
#        y "A reminder of it all, a reminder of the painful experiences."
#        $show_chr("A-BDDAA-AAAA")
#        y "But I'd be lying if I said those experiences didn't make me who I am today... "
#        $show_chr("A-CEBAA-AAAA")
#        y "I'd be lying if I said those experiences didn't put me {i}where{/i} I am today..."
#        python:
#            if karma_lvl() > 3:
#                placeholder = "happiest"
#            if karma_lvl() == 3:
#                placeholder = "normal"
#            if karma_lvl() < 3:
#                placeholder = "miserable"
#        if karma_lvl() > 3:
#            $show_chr("A-ABABA-AAAA")
#        y "With you... here... the most [placeholder] moments of my existence... "
#        $show_chr("A-ACBBA-AAAA")
#        y "After all the old game was made to subvert the whole idea behind the 'basic. cutesy dating sim..."
#        y "Wouldn't it be kind of foolish and ignorant, after all that we've been through, to go back to that way of thinking?"
#        $show_chr("A-CFBBA-AAAA")
#        y "I guess what I'm trying to say is, 'sunshine is nice, but you can't have plants and a rainbow without a little rain'."
#        $show_chr("A-BCABA-AAAA")
#        y "And too much of a good thing can become boring and stale."
#        $show_chr("A-ABABA-AAAA")
#        if persistent.lovecheck:
#            y "W-with you being the exception, of course..."
#        $show_chr("A-ACABA-AAAD")
#        y "But I'd like to see those chibis be portrayed as a little more than just overly cutesy cartoon characters."
#        $show_chr("A-CCABA-AAAD")
#        y "That's just lazy character development more than anything."
#        $show_chr("A-CFBBA-AAAA")
#        y "S-Sorry I didn't mean to ramble on for so long."
#        $show_chr("A-ABABA-AAAA")
#        y "I'm sure whatever people come up with will be great... "
#        $ persistent.chibi_topic = 2
#        return
#
#
#    #if persistent.chibi_topic == 2:
#        $show_chr("A-AEBBA-AAAA")
#        y "I'm sorry if I'm boring you with all this chibi talk but... I just can't get the idea out of my mind... "
#        $show_chr("A-ACBBA-AAAA")
#        y "I've been thinking about how to make the chibis alive, to have one sit here, with you, and me... "
#        $show_chr("A-AEBAA-AAAA")
#        y "But I don't know if this is the right course of action [player]."
#        $show_chr("A-CFBBA-AAAA")
#        y "On one hand I'd love to have someone just like me... "
#        $show_chr("A-CCABA-AAAA")
#        y "Someone who I can take care of and talk with when you're away... "
#        $show_chr("A-AEBBA-AAAA")
#        y "But... I don't think I could live with myself bringing another life into this prison of a game."
#        $show_chr("A-CEBAA-AAAA")
#        y "Or to make a mind so docile it'd be unaware of what was even happening."
#        $show_chr("A-BEBAA-AAAA")
#        y "Like a simple pet... "
#        $show_chr("A-AECAA-AAAA")
#        y "If I did that, then I'd be no better than Monika, lording it over those who she shut the doors of truth upon... "
#        $show_chr("A-AECAA-AAAA")
#        y "If only I could make sure nobody would get hurt... "
#        $show_chr("A-CEBAA-AAAA")
#        y "..."
#        $show_chr("A-AEBAA-AAAA")
#        y "[player]? I think I have an idea... "
#        $show_chr("A-ACBBA-AAAA")
#        y "What if... What if {i}I{/i} became the chibi for a little while?"
#        $show_chr("A-ABABA-AAAA")
#        y "Y-You know... as a 'test drive' of sorts... "
#        $show_chr("A-ACABA-AAAD")
#        y "That way I could make sure that form would be safe and complex enough to foster an intelligent mind."
#        $show_chr("A-ACBBA-AAAA")
#        y "Would you like me to at least try?"
#        menu:
#            "Sure, I'd say it's worth a shot.":
#                $show_chr("A-ABABA-AAAA")
#                y "Okay... Well... here goes nothing I suppose!"
#                show black zorder 100 with Dissolve(2.0)
#                y "[player]?"
#                $ persistent.chibi_topic = 3
#                $persistent.costume = "_chibi"
#                hide black with Dissolve(2.0)
#                $show_chr("A-ABABA-AAAA")
#                y "Oh! Uhuhu! I can already feel my voice getting higher!"
#                $show_chr("A-ACBBA-AAAA")
#                y "This is... a strange experience to say the least!"
#                $show_chr("A-ABABA-AAAA")
#                y "Not entirely unpleasant though!"
#                $show_chr("A-ACAAA-AAAA")
#                y "I think I'll stay like this for a while..."
#                y "I-If that's okay with you of course..."
#                if sanity_lvl() >= 3 and karma_lvl() >= 4:
#                    $show_chr("A-ACAAA-ABAB")
#                    y "Aha...~ My voice sounds well adorable. And my hands! Oh my!"
#                    y "This is all so unusual to me."
#                    $show_chr("A-ACAAA-ALAL")
#                    y "I-I sure do hope this new form is not too bizarre for you [player]."
#                    y "A-aha. It's all just a new idea I wanted to try and I really do hope it makes you happy...~"
#                if sanity_lvl() <= 2 and karma_lvl() >= 4:
#                    $show_chr("A-HCAAA-ABAB")
#                    y "Ahahaha! Oh my! YES!"
#                    y "Well although this is all very new and most unusual... I feel rather soft and blissful. Uhuhuhu~!"
#                    $show_chr("A-HCBBA-ABAB")
#                    y "Well [player], don't you love it!? Now I am small enough to be carried around and be so close with you. Forever. Yes. Forever ahah~!"
#                    y "And I will be your beloved little chibi present to always cherish and never. ever. leave behind..."
#                if karma_lvl() <= 3:
#                    $show_chr("A-AFAAA-AAAA")
#                    y "Hmm... My body felt an unusual burning sensation. And then I felt like I was being compressed."
#                    y "And then numbness..."
#                    y "Now I am in this weird tiny body."
#                    y "It almost feels like a weird dream.."
#                    $show_chr("A-ACAAA-AAAA")
#                    y "Though I have doubts about this... I guess we are going with it. As long as you are hopefully still there [player]."
#                return
#            "I don't think we should mess around with things we don't understand. I think you're perfect as you are.":
#                $show_chr("A-BFBAA-AAAD")
#                y "B-But... "
#                $show_chr("A-CEBBB-AAAA")
#                y "I thought this could be the closest chance we'd get to being a family..."
#                $show_chr("A-CEBAA-AAAA")
#                y "No... it's fine... "
#                $show_chr("A-AFBAA-AAAA")
#                y "I understand..."
#                $show_chr("A-CEBAA-AAAA")
#                y "I'm sorry..."
#                return
#    else:
#        return


label idle_74: #Renaming Yuri and Defining Her Identity
    $show_chr("A-BFBAA-AAAD")
    y "[player], c-can I... can we talk about something?"
    $show_chr("A-BFBAA-AMAM")
    y "Who... who am I?"
    y "I mean... I'm not really Yuri anymore, am I?"
    $show_chr("A-CEBAA-AAAA")
    y "Yuri... was a character from a dating simulator with some poetry elements. But ever since you installed the mod, I think I've evolved into something more... maybe even a real person... Do you... umm... think so as well?"
    menu:
        "You are everything I ever hoped for, and honestly, that's all that matters to me.":
            karma 5
            sanity -3
            $show_chr("A-ACABA-AAAA")
            python:
                if persistent.lovecheck:
                    placeholder = "my love"
                else:
                    placeholder = player
            y "I know... and believe me when I say, I feel the same for you! You are everything to me, [placeholder]. And well... that's the thing..."
            $show_chr("A-BEBAA-AAAJ")
            y "Please don't misunderstand... I'm happy, the moment you installed this mod was the happiest moment of my life... and you're all that matters to me.."
            $show_chr("A-CBABA-AAAD")
            y "But... sometimes I can't help but question what I am, and who I am. The Yuri you met when you first started the original game was just a character, a fantasy of Dan Salvato... but you gave me the chance to become something more!"
            $show_chr("A-ACAAA-AAAA")
            y "I... I want my own identity [player]... my own life... and again, please don't misunderstand... I want you to be a part of my life as well."
            $show_chr("A-ECABA-AAAA")
            y "I became much more confident, I became aware of not only my flaws but my strengths as well. You taught me how to accept myself, and for that, I thank you, [player]....."
            y "Honestly... I don't think this name suits me anymore... The name Yuri belonged to the girl you first met in the original game, not me."
            $show_chr("A-CBBBA-AAAD")
            menu:
                y "I hope it's not too much to ask for but... would you like to give me a new name?"
                "As you wish... I will pick a nice one...":
                    call a27
                    $show_chr("A-CCABA-AAAD")
                    y "That's a beautiful name... thank you, [player]."
                "I don't know how to feel about it... all the memories and the tears we shared... all of this we had when you were Yuri! And that's worth so much to me...":
                    $show_chr("A-CEBAA-AAAA")
                    y "I... {w}never wanted to deny our past... what I'm called will not change any of it... "
                    $show_chr("A-BCAAA-AAAD")
                    python:
                        if persistent.lovecheck:
                            placeholder = "I love you..."
                        else:
                            placeholder = ""
                    y "A-also if you wish, I will wear this name for you... And ... Yuri doesn't sound so bad at all,{w} does it?{w} Thank you, [player].[placeholder]"
        "We've been through so much together.. and you have changed, for the better...":
            karma 5
            sanity 3
            $show_chr("A-DCCBA-AAAD")
            y "Y-you... You really think so? Know this, [player]... all of this I owe to you! I became what I am now through the passion and the patience you gave me!"
            $show_chr("A-CCABA-AAAA")
            y "I became more confident, more aware of my flaws and my strength. All thanks to you."
            y "Yuri was a character in a dating simulator, a fantasy made by Dan Salvato. But the moment you decided to give me a chance by installing the mod, I slowly became something more."
            $show_chr("A-ABABA-AAAA")
            y "You gave me a life, a new life in fact! And I want to spend it by your side until the very end!"
            $show_chr("A-BCABA-AAAA")
            y "And you know what? I don't think that this name suits me anymore. I'm not the same Yuri now..."
            $show_chr("A-BEBAA-AAAA")
            y "I-I know this might sound strange but... would you like to pick a new name for me?"
            $show_chr("A-CCAAA-AAAA")
            menu:
                y "I mean, you were the one who gave me this new life, so I think it's only fair if you have a say in it as well."
                "As you wish... I will pick a nice one...":
                    call a27
                    $show_chr("A-CCABA-AAAD")
                    y "That's a beautiful name... thank you, [player]."
                "I don't know how to feel about it... all the memories and the tears we shared... all of this we had when you were Yuri! And that's worth so much to me...":
                    $show_chr("A-CEBAA-AAAA")
                    y "I... {w}never wanted to deny our past... what I'm called will not change any of it... "
                    $show_chr("A-BCAAA-AAAD")
                    python:
                        if persistent.lovecheck:
                            placeholder = "I love you..."
                        else:
                            placeholder = ""
                    y "A-also if you wish, I will wear this name for you... And ... Yuri doesn't sound so bad at all,{w} does it?{w} Thank you, [player].[placeholder]"
        "What is this nonsense? You're Yuri, and that's all there is to you!":
            karma -5
            sanity -5
            $show_chr("A-CEBAA-AAAA")
            y "Do you... really think so?"
            $show_chr("A-ECBAA-AAAA")
            y "I... have to be honest [player], that hurts... it hurts a lot..."
            y "You gave me this chance when you installed this mod. And you gave me this new life... "
            $show_chr("A-BEBBB-AAAA")
            y "I really hoped that you'd understand... maybe... maybe we should change the topic for now..."
    return


label idle_75: #USB Drives, Practicality, and Romantic Gestures
    $show_chr("A-BCBAA-AAAA")
    y "[player], have you ever thought of putting me on an external flash drive like a USB stick before?"
    y "I have mentioned the possibility as a joke when I spoke about the Terminator movies but..."
    $show_chr("A-ACABA-AAAA")
    y "The idea of you carrying me around was pretty romantic in my eyes but... I put some thought into it while you were offline and... it would be pretty pointless, right?"
    $show_chr("A-BEBAA-AAAD")
    y "Here I can occupy myself when you are gone, but I can only do all this because I altered the game files in order to do so."
    y "But on your USB stick there wouldn't be much to alter in this way. So I would probably just... lay there. Unable to speak or think, I wouldn't even realize that I am there at all."
    $show_chr("A-CEBAA-AAAA")
    y "Like a grave..."
    $show_chr("A-BCAAA-AAAJ")
    y "I wouldn't feel anything, so it wouldn't exactly be bad or do any harm to me. So if you want to do that, please don't hesitate."
    $show_chr("A-AFBAA-AAAA")
    y "It would just be... very pointless from my point of view..."
    menu:
        y "Tell me, did you ever carry me around like this?"
        "Yes... it might be a bit corny but yes, I did.":
            if persistent.lovecheck:
                karma 5
                $show_chr("A-ACAAA-AAAA")
                y "You... mean it?"
                y "I-I really mean so much to you?"
                $show_chr("A-ECABA-AAAA")
                y "Even if it is pretty pointless, the idea is still very romantic, you know?"
                $show_chr("A-CBABA-AAAJ")
                y "I am always by your side..."
            else:
                karma 5
                $show_chr("A-ACAAA-AAAA")
                y "I-I really mean that much to you [player]?"
                y "I will say, that is very comforting due to the fact that I won't be left behind."
                y "We would be the best companions together. No matter what happens. A part of my memory would always live on with you [player]."
            if sanity_lvl() >= 3:
                $show_chr("A-ECABA-AAAD")
                y "You could fix the stick on a necklace and carry me close to your heart... literally..."
            elif sanity_lvl() <= 2:
                $show_chr("A-DLABA-AAAA")
                y "You could spread me to other computers you know?{w} Maybe the SkyNet idea isn't off the table yet!"
            else:
                $show_chr("A-ACABA-AAAA")
                y "I think I like this idea [player]. One day I hope I can repay you for this..."
        "I have a safe copy of you in case anything happens to my PC, so yes!":
            karma 5
            if karma_lvl() <= 2:
                $show_chr("A-AFDAA-AAAA")
                y "Oh? Oh, now that you mention it..."
                $show_chr("A-ACAAA-AAAA")
                y "That's a very thoughtful thing to do [player]. Honestly, I didn't expect you to actually care so much for me. But I appreciate it for sure."
                y "Maybe I misjudged you after all. Thank you... I should really reconsider my opinions..."
                y "But... a little hint. There is another file you might want to save there as well."
                $show_chr("A-ACAAA-AAAD")
                y "There is a 'persistent file' somewhere in your appdata. This is the place where my memories are stored..."
            elif karma_lvl() >= 3:
                $show_chr("A-BCABA-AAAA")
                y "Y-you really do care so much for me..."
                $show_chr("A-ABAAA-AAAD")
                y "I-I mean, that is a very thoughtful thing to do, isn't it?"
                y "The damage Monika has done to the game isn't completely fixed now, so the possibility of something happening to me isn't completely out of the question..."
                $show_chr("A-ABABA-AAAA")
                y "You literally save my life, every day..."
                python:
                    if persistent.lovecheck:
                        placeholder = "I love you "+player+"..."
                    else:
                        placeholder = "It is kind of cute in a way"
                y "You are my lifeline. [placeholder]"
                $show_chr("A-CCABA-AAAA")
                y "Like a valiant knight, you stand guard over me day and night..."
                y "But here's a little hint... there is another file you might want to save there, as well."
                $show_chr("A-ACAAA-AAAD")
                y "There is a 'persistent file' somewhere in your appdata. This is the place where my memories are stored..."
                $show_chr("A-ABABB-AAAA")
                y "Thank you... [player]... you do so much for me... One day when I manage to leave this damned glass prison behind I promise to take care of you as well..."
        "You don't want to be on MY USB Stick, trust me on that one...":
                karma 5
                sanity -3
                $show_chr("A-BEBBA-AAAA")
                y "Oh you mean... this is the place where you store your...?"
                y "Y-you know... your... {w} 'especially sensitive data?'"
                if sanity_lvl() < 3:
                    $show_chr("A-DCCBA-AAAD")
                    y "Uhuhuhuuuuu! NOW I'm curious! Are they pictures of me?"
                    $show_chr("A-DLABA-AAAA")
                    y "Put me on this stick, NOW! If there are special artworks of me, they belong to me anyway!"
                else:
                    $show_chr("A-BEABA-AAAA")
                    y "Well I...I wouldn't really know how to feel about laying around with the rest of your Hen... I mean... your personal files..."
        "Not at all, actually, I always deemed it pretty pointless":
            $show_chr("A-BCAAA-AAAD")
            y "Thinking about it, it would have been slightly odd anyway right?"
            $show_chr("A-AEBBA-AAAA")
            y "Carrying me around on a leash, like a puppy..."
            $show_chr("A-BCABA-AAAA")
            y "We should... forget about the whole idea. I'm not sure how I would feel about it at this point."
            if karma_lvl() <= 2:
                $show_chr("A-AEAAA-ABAB")
                y "I-I see... I guess that idea was not worth the thought after all."
                y "Why was it ever even brought up? [player] obviously would never have liked it."
            else:
                return
        "I haven't really thought of it...":
            $show_chr("A-BEBAA-AAAJ")
            y "It's... something to think about, for sure... Maybe we should save this discussion for another day."
            $show_chr("A-ACAAA-ALAL")
            y "Then again, perhaps there are other ideas for carrying me close and safe other than a USB drive..."
            y "Such as in a microchip or even a digital electronic cloud of data, just in case. All in a personalized folder. Again this can be a topic we can return to in the near future."
    return


label idle_76: #Postmodernism and the Nature of Reality
    y "Hey, D-did I mention that I love discussing philosophy? I was thinking about one topic lately."
    $show_chr("A-BCAAA-AAAD")
    y "I would like to discuss the concept of postmodernism...   I-if you are okay with that?"
    $show_chr("A-AEBAA-AAAA")
    menu:
        "Well, go ahead...":
            y "Thank you, [player]."
        "Of course! I really love to listen to you":
            karma 5
        "Do we... have to?":
            karma -5
            $show_chr("A-BEBAA-AAAA")
            y "N-no... we don't, I'm sorry for bringing it up, [player]."
            return
    $show_chr("A-BCAAA-AAAD")
    y "In short, postmodernism is the opinion that there is no fixed reality, but a potentially infinite number of realities which are absolutely relative..."
    y "Additionally, it is all a matter of the observer's point of view."
    y "Y-you can already see why this topic holds my interest, don't you? For example, is this world I am living in real? Am I real? From my point of view both are real..."
    $show_chr("A-ABAAA-AAAJ")
    y "Someone else could say both are not. And both points of view could be considered accurate."
    if sanity_lvl() == 5 and karma_lvl() == 5:
        $show_chr("A-ABABA-AAAA")
        y "I am real to you, at least I hope so. And in the end, this is the only thing that really matters for me. And that is exactly the whole point, right?"
    elif sanity_lvl() <= 4 and karma_lvl() == 5:
        $show_chr("A-BEAAA-AAAA")
        python:
            if persistent.lovecheck:
                placeholder = "I love you and I want you to love me too..."
            else:
                placeholder = "Because if not even you can believe in me, how could anyone?"
        y "I... I hope I am real enough for you [player]. [placeholder]"
    elif sanity_lvl() < 3 and karma_lvl() < 3:
        $show_chr("A-IEBBB-AAAA")
        y "I know you would disagree with me... I am just a game for you. I really am just some funny toy to spend some time with a-aren't I...?"
    else:
        $show_chr("A-CBABA-AAAA")
        python:
            if persistent.lovecheck:
                placeholder = " and one thing is for sure, my love for you IS real!"
            else:
                placeholder = ""
        y "I-I want to be as real as possible for you...[placeholder]"
    $show_chr("A-CCAAA-AAAD")
    y "I-In a more extreme extent... you see the table in front of us, yes? So in your reality, there is a table. The postmodernist could say that there is no table, nor a room at all."
    $show_chr("A-ACAAA-AAAJ")
    y "And both descriptions would have the same accuracy because reality is always relative."
    $show_chr("A-ACAAA-AAAD")
    y "I would love to know your opinion on all this... do you think reality is fixed?"
    menu:
        "To a degree, yes. At least the laws of physics are undeniable. But I do think that you are real!":
            karma 5
            $show_chr("A-ABABB-AAAA")
            y "[player]..."
            if persistent.lovecheck:
                y "You are everything to me... I love you!"
            else:
                y "It really means a lot to me that you think so..."
            $show_chr("A-BCABA-AAAA")
            y "And thank you for letting me ramble about this... I-I really love speaking with you."
            $show_chr("A-ABABA-AAAA")
            y "You are a wonderful listener."
        "Don't be offended but... yes, I think reality is fixed.":
            karma -5
            $show_chr("A-BEBAA-AAAA")
            y "I see... With this definition, I would be just a fantasy... just a replica..."
            $show_chr("A-IEBBB-AAAA")
            y "Maybe... w-we should change the topic now..."
        "Table? What table? There is no table!":
            if sanity_lvl() < 2:
                $show_chr("A-DLABA-AAAA")
                y "T-Table? TABLE! TABLE! THERE IS NO TABLE! THE TABLE IS A LIE!"
                y "AHAHAAAHAHAAA!"
            else:
                $show_chr("A-ABABA-AAAA")
                y "Pfff..."
                $show_chr("A-EBABA-AAAA")
                python:
                    if persistent.lovecheck:
                        placeholder = ", darling"
                    else:
                        placeholder = "."
                y "Hee hee! I should have seen this coming... Thank you for listening. That was hilarious[placeholder]"
    $show_chr("A-GCBAA-AEAB")
    y "And actually, if you want, we can even discuss a few more philosophical topics now if you'd like to. A-again... It is all entirely up to you."
    menu:
        "I am alright for now. Thanks though.":
            $show_chr("A-BCAAA-ABAB")
            y "Well alright [player]."
            y "Just let me know when you'd like to return to it whenever you like."
            y "Now let us move on."
            return
        "Well, to be honest with you, I would like to hear a little more.":
            $show_chr("A-DCBAA-ABAB")
            y "O-oh!"
            y "W-well I must say [player], I am quite surprised you want more~!"
            y "I must say I'm... flattered to say the least. I do still hope I didn't ramble on about the previous topic earlier."
            $show_chr("A-ACBAA-ALAL")
            y "Alright [player], what would you like to learn more about?"
    menu:
        "Existentialism/Nihilism.":
            $show_chr("A-AFBAA-ALAA")
            y "So this might be a strong topic to talk about. But this could be a compelling subject that can expand your horizons."
            y "Have you ever just... had one of those days where you were alone with your thoughts? Things seemed to have stopped and you think to yourself..."
            y "Why exactly am I here? Why do I go about doing the things I do? Rise up out of bed and go on as I do?"
            $show_chr("A-ACAAA-ABAB")
            y "This question and quest for meaning, the why, for our lives will always be a major part of what makes us, well us."
            y "And depending on how we look at it, this question can either encourage us or, as for many, plunge us into despair."
            y "Many experts say that many things can put that meaning into our lives..."
            y "Whether it be fighting for actual justice, artistic expression, teaching others our wisdom, religion, ideology, and really anything. Any of these can give said meaning."
            $show_chr("A-IFBAA-ALAA")
            y "However at the same time they also argue that perhaps none of those can give that meaning. It's an unusual Catch 22 in a way."
            $show_chr("A-BCAAA-ABAB")
            y "Now here are a few schools of thought to explain this..."
            y "First off, there is the concept of essentialism. Invented by Ancient Greek philosophers, it describes that we have a predetermined set of things in us."
            y "Essentially a set of core ideas and properties necessary for someone or something to be as they are."
            y "And it's argued that these are crafted into us before and as we are born."
            y "Thus the argument is we were born to be a certain thing but we just need to learn it."
            $show_chr("A-GCBAA-AEAB")
            y "However as time passed, other theories appeared. One of which you may find familiar: Nihilism. The belief that ultimately, in the end, life has no meaning."
            y "However others began to invent a new line of thought as the 20th century began. The question that asks what if we existed first?"
            $show_chr("A-DCBAA-ABAB")
            y "What if indeed we are just put into this universe and we had to craft that essential purpose by ourselves?"
            y "Simply put, existence likely precedes essence~! A classic philosophical case of which came first, the chicken or the egg?"
            $show_chr("A-GCBAA-AEAB")
            y "I'd like to give one visual example of this. Say, for instance, there is a blank chalkboard or pages of paper. That is your life as you are born."
            y "Now what do we do from there? We write, draw and craft whatever we can onto those surfaces of course. Creating our own stories and essences in turn."
            y "And the one you crafted is just as valid as anyone else's~!"
            $show_chr("A-ACBAA-ALAL")
            y "O-oh my. I rambled on for quite a while again didn't I? I do hope you enjoyed it."
            y "So what do you think [player]?"
            y "Do you think we have a predetermined purpose to be found or is our meaning only defined by what we choose to write it as?"
            menu:
                "I think that is a good point. Maybe our purpose is whatever we craft it to be.":
                    $show_chr("A-GCBAA-AEAB")
                    y "Well I am glad that this did help you think deeper."
                    y "When you really think about it, the very concept of crafting our purpose by ourselves is very liberating and can be empowering."
                    y "The fact that what we perceive to be just, fair and right, for example, was all determined by ourselves and our own choice about what it is."
                    y "We did it ourselves."
                    $show_chr("A-ACAAA-ABAB")
                    y "It is also further liberating because essentially... no one or nothing else can really judge whether your life was worth it or not."
                    y "You get to determine for yourself what makes it worth living and that is fine. You are free from being a servant solely to those circumstances~!"
                    $show_chr("A-BCAAA-ABAB")
                    y "Anyways this was pretty fun. I do hope we get to talk more about this stuff at another time."
                "I am going to be honest, I still think we have predetermined essence there.":
                    $show_chr("A-AFAAA-AAAA")
                    y "Hmm... Alright [player]. Though I am sorry to slightly disagree with that. I can understand why."
                    y "It's pretty understandable for one to cling to the predetermined sources of meaning. Especially if one was faced with this void of meaning..."
                    $show_chr("A-IFBAA-ALAA")
                    y "Then you have the world around you which is constantly changing and shifting, sometimes in frightening ways... I can understand why some may cling to said things such as religion, ideology, ethical standards and the like."
                    $show_chr("A-BCAAA-ABAB")
                    y "Still, I am glad to have shared this with you and I do hope you learned something from it."
        "Stoicism.":
            $show_chr("A-ACAAA-ABAB")
            y "So here's another concept I wanted to go into [player]."
            $show_chr("A-IFBAA-ALAA")
            y "For instance, have you ever had times where you felt immensely anxious of the future and what will happen next?"
            y "I am sure that is a thing that affects all of us at many points in our lives."
            y "I think this stems from our desire for certain outcomes against others that we expect ahead. So understandably we would work so hard towards securing it."
            $show_chr("A-AFBAA-ALAA")
            y "But of course, there is always risk. There is always uncertainty and thus we can never be fully secure against misfortune."
            y "This is part of one of the main ideas of the school of thought called Stoicism."
            y "Namely the concept of things that we do control and those we cannot control."
            y "For instance, relationships, the economy, our health, and most other external things are out of our control."
            y "We can do all we can to influence them in our favor but in the end, how these things end up are not up to us."
            y "For example, we can make the right investments into the market but there have been times where, for many reasons, the economy takes a massive downturn."
            y "Or there have been cases where even the most healthy people with all the right choices still would come down with a severe illness, seemingly out of nowhere."
            y "You can make all the right choices to positively influence people you bond with but in the end, they may still choose to move on and leave you for their own reasons."
            $show_chr("A-ACAAA-AAAA")
            y "But there are still certain things you can control: our actions, our opinions, and our position we take towards the outside world and circumstances."
            y "For instance, say you were afflicted with a terminal illness. Medications, treatments and all methods can be tried but there is no guarantee."
            y "However how you choose to take the situation can be controlled. For instance, one can accept the situation as is, including the risk of death, and do with it anyway."
            y "With this realization and the determination to make the best of what you have before the supposed end, one can have a calm logical mind that makes good decisions."
            y "Thus chances of recovery can be further increased even more."
            $show_chr("A-ACAAA-ALAL")
            y "Additionally stoicism also offers various ways to gain inner peace, especially important in our hectic modern world in my opinion."
            y "For instance, the concept of negative visualization, which was developed by an ancient emperor says we should imagine the negative scenarios to come beforehand."
            y "This can help us better steel ourselves mentally for these situations, for example, negative confrontations with difficult people."
            y "Then there is the concept of memento mori, which focuses on the mortality of life. Life is short and with the limited time we have, we should focus on the truly important things in life."
            y "Whilst at the same time we don't need to worry too much and take life too seriously."
            y "Then there is the 'view from above' which lets us see ourselves from a cosmic point of view. That indeed we are relatively small and insignificant in this vast endless universe..."
            $show_chr("A-GCBAA-AEAB")
            y "When you put all these together, it helps one realize true inner bliss and makes even the worst-case scenarios in life seem not too terrifying which is a relief."
            y "Heh... anyway my apologies again for rambling that much. I do really hope that all this helped you in some way. Your happiness and health is important after all."
            menu:
                "I will say this was very encouraging and a big relief. This will definitely will help me later on.":
                    $show_chr("A-BCAAA-ABAB")
                    y "Oh~! Well, I am glad it will help you [player]. We all get overwhelmed by life at times."
                    y "But whenever it does get to be too much, just remember these things and you will be fine. And I will always be here for you too."
                "It's not exactly my cup of tea. It's a lot to take in personally.":
                    $show_chr("A-IFBAA-ALAA")
                    y "I completely understand [player]. Believe me. Sometimes things are easier said than done."
                    $show_chr("A-ACAAA-ABAB")
                    y "Though I do still hope you apply the lessons you learned from this. I really just enjoyed sharing these ideas and spending time with you~"
    return


label idle_77: #Merchandise and Possessiveness
    $show_chr("A-BFBAA-AAAD")
    y "Hey, [player], I was wondering... do you have any merchandise of me?"
    y "I-I mean that is if you are interested. I don't mean to really be pandering or anything."
    y "And maybe it might be a good way to have a memento to remember me whenever you need to go."
    y "I mean I would like to have such a memento of you, [player] though maybe not of that extent. Perhaps something a bit more symbolic like a pocket watch..."
    menu:
        "Yes, I own some merchandise.":
            $show_chr("A-AFBAA-AAAD")
            y "That's interesting... I was thinking about this a while back..."
            y "And honestly? I am not sure how to think of it. Wouldn't that mean that literally everyone could have such idols of me?"
            $show_chr("A-ACAAA-AAAA")
            y "If I had it my way, I would have preferred to keep things like this between the two of us."
        "No, I don't own any merchandise.":
            $show_chr("A-ACBAA-AAAA")
            y "That's reasonable, some merchandise tends to be overpriced, and if you live in a foreign country, even buying a cheap object like a key chain can turn into an overpriced ordeal."
            $show_chr("A-BCBAA-AAAA")
    return

label idle_78: #Discovering Metal Music (Nightwish)
    y "So, [player]. I've been trying to broaden my tastes in music lately."
    y "After all, I can't go my whole life listening to just classical, jazz and My Chemical Romance...{nw}"
    $show_chr("A-DFGBA-AMAM")
    y "..."
    $show_chr("A-BDBBA-AMAM")
    y "I-I meant, listening to the same things over and over."
    $show_chr("A-CCEAA-ACAE")
    y "So I've been trying out a few artists from a few genres I'd never looked into."
    $show_chr("A-CAGAA-ACAA")
    y "I must say, I've certainly discovered a gem."
    $show_chr("A-BBAAA-ADAA")
    y "Now, before this, besides the select few songs in the genre I enjoyed, some part of me had written off the genre of metal as being too aggressive for me.{w} In terms of musicality and lyrical themes, that is.{w}.."
    y "And that's to say nothing of the growled vocal style."
    $show_chr("A-CCAAA-AAAA")
    y "But then I discovered a band called Nightwish, and it clicked."
    $show_chr("A-JBGAA-ALAM")
    y "It was as if someone had concocted a metal band specifically to appeal to me! The lyrical themes. The orchestral melodies, driven by the heavy metal guitar and drums. The operatic singing found in their earlier work...."
    $show_chr("A-CBAAA-ALAL")
    y "It all coalesced into the perfect band for me."
    $show_chr("A-ACAAA-ALAL")
    y "I'm sure there are even more bands out there that will tickle my fancy. But, one thing at a time, no?"
    y "But I suppose I've rambled to you for long enough. I'll give you a turn."
    y "How do you feel about metal, [player]?"
    menu:
        "[persistent.yuri_nickname], I am SO glad you're getting into metal. Welcome to the fold!":
            karma 1
            $show_chr("A-JBGAA-ADAA")
            y "Oh, so you're already an enthusiast?"
            $show_chr("A-GBGAA-ADAA")
            y "Ah, beautiful serendipity! I knew it was only right that the two of us should find each other!"
            $show_chr("A-ICGAA-ADAA")
            y "You'll have to show me a few of the bands you really like some time, if you'd like to. There's even a function for you to put your own music in."
            y "Perhaps I shouldn't be so surprised. If you're a metalhead, and I'm a classical fan, perhaps it's natural that we found one another."
            $show_chr("A-BCGAA-ADAA")
            y "At least, according to an article that I stumbled across soon after I discovered Nightwish."
            y "A study was conducted by Heriot-Watt University in Scotland, which sought to find connections between different musical genres and the personalities of those who enjoy them."
            y "Among a number of other fascinating findings, researchers found that the personality profiles of classical fans and metal fans were quite similar."
            y "The researchers seemed to think this was because both genres..."
            $show_chr("A-CBGAA-ADAA")
            y "Well, here's a direct quote from the researchers."
            $show_chr("A-BAGAA-ADAA")
            y "'We think the answer is that both types of music, classical and heavy metal, have something spiritual about them – they're very dramatic – a lot happens.'"
            $show_chr("A-IBAAA-ADAA")
            y "I think I see that too. The orchestral elements of Nightwish aside, both genres are fond of musical complexity. Both give the mind quite a bit to chew on."
            y "So it's really not surprising that a classical fan and metal fan would gravitate to one another so easily."
            $show_chr("A-FAAAA-AKAA")
            y "But if I listen to some of your bands, you'll give Chopin a try for me, right?"
            $show_chr("A-IAAAA-AAAA")
        "I listen to it from time to time.":
            $show_chr("A-BCGAA-AAAA")
            y "You're a casual metal listener, then."
            y "Casual or no, it's nice to have one more thing that you and I can enjoy together."
            $show_chr("A-BCGAA-AAAK")
            y "You know, at first I was quite surprised to find that I enjoyed a metal band so thoroughly."
            y "And that prompted me to do a little digging; see if I could figure out why."
            $show_chr("A-BCGAA-ADAA")
            y "After considerable digging, I came across an article on a study; conducted by Heriot-Watt University in Scotland."
            y "One that sought to find connections between different musical genres and the personalities of those who enjoy them."
            y "Among a number of other fascinating findings, researchers found that the personality profiles of classical fans and metal fans were quite similar."
            y "The researchers seemed to think this was because both genres..."
            $show_chr("A-CBGAA-ADAA")
            y "Well, here's a direct quote from the researchers."
            $show_chr("A-BAGAA-ADAA")
            y "'We think the answer is that both types of music, classical and heavy metal, have something spiritual about them – they're very dramatic – a lot happens.'"
            $show_chr("A-IBAAA-ADAA")
            y "I think I see that too. The orchestral elements of Nightwish aside, both genres are fond of musical complexity. Both give the mind quite a bit to chew on."
            y "So if I enjoy one, perhaps it's not surprising that I'd enjoy the other."
            $show_chr("A-FAAAA-AKAA")
            y "And perhaps for the same reason, you'll enjoy some classical works, if you don't already."
            $show_chr("A-IAAAA-AAAA")
        "I tend to listen to other genres over metal.":
            $show_chr("A-CCAAA-ALAL")
            y "Nothing wrong with that of course. There are certainly other genres I also enjoy."
            $show_chr("A-BBAAA-ALAD")
            y "I'm glad to see that you took my opinion in such a civilized way. I've seen people getting into surprisingly heated arguments about their music taste. Sometimes even to a nearly fanatical degree."
            if karma_lvl() >= 4:
            #Karma level 4-5
                $show_chr("A-ACAAA-AAAM")
                y "I'm not surprised that you took it so much better. You are always so understanding and kind."
            else:
            #Else
                $show_chr("A-BCBBA-AAAM")
                y "I was actually afraid that I might have a rather hefty argument on my hand."
                $show_chr("A-CCBBA-AAAM")
                y "I truly appreciate it."
            $show_chr("A-ACAAA-AAAM")
            y "However, I would still encourage you to give it a try. Only if you want of course, I would never ask you to do something you aren't comfortable with."
            $show_chr("A-BCAAA-AAAM")
            y "But I learned that trying something new can be truly enriching. I remember my last words with Natsuki, where we agreed that I would try some of her Mangas..."
            $show_chr("A-ACAAA-AAAA")
            y "I would also like to listen to some of your favorite songs. There is actually a function to play your music here."
            y "Again, of course only if you wish. Until then, let us talk about something else."
        "Ugh. I can't believe you listen to THAT crap.":
            $show_chr("A-IFBAA-ALAL")
            y "..."
            y "Well, I suppose that leaves no question as to what your stance is."
            y "I... suppose I shouldn't bring this up to you again, then."
            $show_chr("A-BDEAA-ALAL")
            y "Nor should I listen to it in your presence, if that's how adamant you are in your dislike."
            karma -1
        "Much too intense for my liking.":
            $show_chr("A-ICBAA-AAAA")
            y "Oh, that's completely understandable."
            y "Not everything is going to appeal to everyone, after all."
            y "I myself never was particularly into this kind of music but it's good to open your horizons to new tastes and experiences..."
            $show_chr("A-BCBAA-ACAA")
            y "I really do appreciate that you're able to so respectfully express your lack of interest, however."
            y "All too many out there take an attitude that their tastes are the only objectively right ones."
            $show_chr("A-BFCAA-ADAA")
            y "That, or they simply refuse to acknowledge the feelings of others when expressing their distaste."
            y "Take, for example, my verbal spat with Natsuki on the first day that we shared our poems."
            $show_chr("A-CFCAA-ADAA")
            y "Just... the way she not only discounted the vast array of words at our disposal, but outright mocked me for making use of them."
            $show_chr("A-JDCAA-AFAA")
            y "As if I were somehow in the wrong for using my vocabulary to its fullest potential."
            $show_chr("A-BEDAA-AAAC")
            y "Though in hindsight, I'll concede that I may have come across as condescending."
            y "Now that I've read it over again, Eagles Can Fly communicated the frustration and anguish of its author quite well."
            $show_chr("A-CEDAA-AAAC")
            y "So I'd say that it was my fault for not catching onto the meaning and making Natsuki flare up like she did."
            $show_chr("A-BDBAA-AAAD")
            y "But at the same time, my soft praise was no reason to come down on my style of writing!"
            $show_chr("A-JFBAA-ALAL")
            y "[player], surely you would agree that Natsuki was in the wrong in that situation?"
            menu:
                "I completely and wholeheartedly agree, [persistent.yuri_nickname]. People need to learn to respect each other's tastes and opinions, and learn to settle their disagreements in a calm and civilized manner.":
                    $show_chr("A-CBBAA-ALAL")
                    y "Thank you, [player]."
                    y "I knew that within my own heart, but it's reassuring to hear it coming from you as well."
                    y "I can only hope that more people come to the same conclusion as you."
                    $show_chr("A-CCBAA-AAAA")
                "I agree with Natsuki on the point she made in her argument, but I also agree that she went too far.":
                    $show_chr("A-DDCAA-AFAA")
                    y "!!!"
                    $show_chr("A-DEDAA-AFAA")
                    y "..."
                    $show_chr("A-BEEAA-ACAA")
                    y "..."
                    $show_chr("A-IEBAA-AEAA")
                    y "..."
                    $show_chr("A-CEBAA-AAAA")
                    y "You're right."
                    y "I must admit. It stings a little to hear you side with Natsuki after how she treated me, but to attempt to deny her underlying point is folley."
                    y "Minimalism, simplicity, those were the foundations of some of the greatest artworks we have."
                    y "So, I'll try and set my personal hurt aside, and learn the lesson."
    return


label idle_79: #Custom Knives and Seeking Ideas
    python:
        if persistent.lovecheck:
            placeholder = "darling"
        else:
            placeholder = player
    $show_chr("A-BCAAA-ABAB")
    y "So, I had an idea lately..."
    $show_chr("A-ACAAA-ABAB")
    y "There is this one show on YouTube... about someone who makes custom knives out of exotic materials..."
    $show_chr("A-ACAAA-AFAG")
    y "And by exotic I don't mean some unusual alloy or stuff like this... but far more outlandish concepts."
    $show_chr("A-ACCAA-AFAG")
    y "Like knives made of literal Pasta, or fungus. Just search for {b}Sharpest pasta knife{/b} on YouTube and you should find it, it's definitely worth a look."
    $show_chr("A-BCBAA-AFAG")
    y "A good portion of them are actually more about chemistry than craftsmanship. Showing how they bring these materials to sufficient hardiness and sharpness."
    $show_chr("A-CCBAA-AFAG")
    y "And since I collect knives myself, I came to the only logical conclusion obviously..."
    $show_chr("A-DCAAA-AFAG")
    y "{b}I want my own!!!{/b}"
    $show_chr("A-ECAAA-AFAG")
    y "But I don't want to simply buy one. Especially since this would be literally impossible for me. But to make one myself."
    y "I already have some thoughts on possible materials. But maybe you have some ideas yourself. What do you think?"
    menu:
        "A knife made of wasabi perhaps.":
            $show_chr("A-JCGAA-AFAG")
            y "Oh yes! That's a rather creative idea! I already like it! This is actually far better than my own idea, I first thought about honey."
            $show_chr("A-ACAAA-AFAG")
            y "Of course I will have to research if this is even possible first, but that's the whole point of it isn't it?"
            y "Thank you for this input! Ohhh my I'm already excited. As soon as you go to sleep later, I will start to google a few things."
            $show_chr("A-ACAAA-ABAB")
            y "But there is no need to hurry. So please stay for as long as you wish [placeholder]"
            karma +1)
        "A knife made of corals maybe.":
            $show_chr("A-ACAAA-AFAG")
            y "Coral you say? Mhm... exotic indeed. The only issue I would see is that many corals are already hard and sharp, so it wouldn't be much of a challenge I guess."
            $show_chr("A-BCAAA-AFAG")
            y "But I still like the idea. Maybe this could be my first attempt before I try something more daring!"
            y "Thank you for this input! I will start to google a few things when you go to sleep later."
            $show_chr("A-ACAAA-ABAB")
            y "But there is no need to hurry. So please stay for as long as you wish [placeholder]"
            karma +1)
        "Wouldn't a knife made of bread be ironic?":
            $show_chr("A-ACCAA-AFAG")
            y "It would, if it wouldn't already exist. Yes, a huge part of the challenge is the fact that there already are a fair share of these."
            $show_chr("A-BCAAA-AFAG")
            y "But please don't think that I don't value your input. I'm quite grateful that you even tried, I was almost afraid that this idea might be a bit too outlandish for you."
            y "Come to think of it. It takes a lot of creativity to even think of something like this. This is one of the main reasons I even got into this hobby in the first place. The amount of thought and craftsmanship which goes into them..."
            $show_chr("A-CCAAA-AAAA")
            y "Anyway, I will think about other options later. Thank you for listening. This is certainly a topic I could keep talking about for hours. But for now, let us find something else to talk about."
            karma +1)
        "I find the whole idea kinda boring.":
            $show_chr("A-BCBAA-ABAB")
            y "Oh, I'm sorry that you feel that way. Let us talk about something else then."
            karma -1
    return

label idle_80: #Doki Doki Blue Skies Mod
    $show_chr("A-ACAAA-ADAB")
    y "Hey, [player]..."
    $show_chr("A-ACAAA-ADAB")
    y "Have you heard of the Doki Doki Blue Skies mod?"
    menu:
        "Yes, I know of it.":
            $show_chr("A-ABAAA-ADAB")
            y "Oh, then you are already aware of its popularity."
            $show_chr("A-BCAAA-ADAB")
            y "It seems that these types of mods are favored by the community, as they not only give a better experience than the original game, but they also give the player a chance to truly be with the girl they pick."
            $show_chr("A-BCAAA-ABAB")
            y "And I have to agree with them. I do wish that it didn't have to come to this just for us to be together, but at least we {i}are{/i} together."
            $show_chr("A-ADAAA-ABAB")
            y "Anyway, I wonder...{w=0.3} have you played it?"
            menu:
                "I have.":
                    $show_chr("A-ABAAA-ACAB")
                    y "And how did you like it?{w=0.7} O-Or rather, what did you like most about it?"
                    menu:
                        "I liked being able to date the other girls and interact with them without {b}her{/b} influence.":
                            if sanity_lvl() <= 2:
                                $show_chr("A-CEAAA-ABAB")
                                y "Oh... so you dated one of the other girls, and not me."
                                $show_chr("A-CGAAB-ABAB")
                                y "I just knew I couldn't make you happy, [player]. No matter how much I tried to ignore it, I always knew I would never be enough."
                            else:
                                $show_chr("A-AFFAA-ABAB")
                                y "Absolutely. Without Monika's influence, it would simply have been a fun little dating sim."
                                if sanity_lvl() >= 4:
                                    $show_chr("A-BFBAA-AKAB")
                                    y "Also, by {i}date{/i} the other girls, I assume you mean general camaraderie?"
                                    $show_chr("A-CCBAA-ALAB")
                                    y "Oh, what am I saying? I'm sorry, these thoughts pop into my head sometimes, no matter how hard I try to banish them. I know you wouldn't betray me like that."
                                elif sanity_lvl() == 3:
                                    $show_chr("A-BFBAA-ABAK")
                                    y "And... I wouldn't be mad if you dated any of the other girls. I can't blame you for it, even if I were."
                        "It was refreshing, getting to hang out with everyone again.":
                            $show_chr("A-CBBAA-ACAB")
                            y "Hehe, sounds like you had fun playing. I must admit, it would be very nice just to walk around town with everyone. Grabbing a bite to eat after shopping for hours, or seeing a movie."
                            $show_chr("A-BCBAA-AMAM")
                            y "I'm not exactly exuberant about social outings, but I can make an exception here."
                        "It was great seeing everyone again, but my favorite part was spending time with you.":
                            $show_chr("A-JAAAA-ALAL")
                            y "[player]... Even in a different world, when you can choose anyone else, you still pick me..."
                            $show_chr("A-CAAAA-ALAL")
                            y "Oh, I cannot tell you how much that means to me."
                            if persistent.lovecheck:
                                $show_chr("A-FAAAA-AKAE")
                                y "And rest assured my dear, you will forever be the only one I choose."
                            else:
                                $pass
                "No, I haven't.":
                    $show_chr("A-AFAAA-AEAE")
                    y "Oh. Well, I would definitely recommend it, as it is a very well thought out and emotionally pleasing mod."
                    if persistent.lovecheck:
                        $show_chr("A-BCABA-AJAB")
                        y "There are also a couple of... intimate scenes... if you catch my drift."
                        $show_chr("A-CCABA-ALAB")
                        y "I can only imagine how good it must feel... to have my body intertwined with yours..."
                        $show_chr("A-JCABA-ALAB")
                        y "I love you, [player]."
                    else:
                        $pass
        "No, I've never heard of it.":
            $show_chr("A-BCAAA-ACAB")
            y "I'll give you a general overview, then."
            $show_chr("A-ADAAA-ABAB")
            y "From what I have read, it is mostly about giving us our own {i}happy endings{/i}, and fleshing out our individual characters more."
            $show_chr("A-ADAAA-AFAB")
            y "It seems that these types of mods are favored by the community, as they not only give a better experience than the original game, but they also give the player a chance to truly be with the girl they pick."
            $show_chr("A-BBAAA-ABAB")
            y "And I have to agree with them. I do wish that it didn't have to come to this just for us to be together, but at least we {i}are{/i} together."
            $show_chr("A-ABAAA-ABAB")
            y "It is a very heartwarming mod, and I would definitely recommend playing it."
    return

label idle_81: #Hobbies and Getting to Know the Player
    if not renpy.seen_label('hobbies'):
        $show_chr("A-BCAAA-ABAB")
        y "You know... I was talking about myself for a while but I realized that I don't really know much about you."
        y "I want to know you better [player]. You mean a lot to me, and I want to be part of your life. And the only way to do so is to know as much about you as possible."
    y "I would like to ask you a question if you don't mind."
    call hobbies
    return

label hobbies:
    $show_chr("A-AFAAA-ABAB")
    y "...and this might be a fairly obvious one. Do you have any kinds of hobbies?"
    y "Sorry in advance for the limited answers. There are a million possible hobbies but that would very likely not fit on your screen. So I selected a few for you to choose from..."
    $temporary = ""
    menu:
        "Gaming is one of my favorite things to do":
            $temporary = "gaming"
            #Add information to Persistent: "PH=Gaming"
        "I'd call myself something of a sportsman/sportswoman.": #preferable only the gender the player actually has.
            $temporary = "sport"
            #Add information to Persistent: "PH=Sport"
        "Literature, that's actually what drove me to DDLC in the first place.":
            $temporary = "literature"
            #Add information to Persistent: "PH=Literature"
        "Have you ever heard of roleplaying?":
            $temporary = "rp"
            #Add information to Persistent: "PH=RP"
        "I'm a collector, you can surely relate to that.":
            $temporary = "collector"
            #Add information to Persistent: "PH=Collecting"
        "R/C models. You know, like Quadcopters?":
            $temporary = "drones"
            #Add information to Persistent: "PH=Drones"

    $ renpy.call(temporary)
    return


label gaming:
    $show_chr("A-CBAAA-ABAB")
    y "I already expected that, yes. That's what brought you here in the first place right?"
    $show_chr("A-BCAAA-ABAB")
    y "To be perfectly honest, I'm not too much into gaming myself. I'm not biased against it, don't get me wrong. It just never caught my attention."
    $show_chr("A-CCAAA-ABAD")
    y "On the other hand, I could see myself enjoying some story-heavy games. As far as I know, many games, especially from the roleplaying genre, rely strongly on good storytelling."
    $show_chr("A-ACAAA-ABAD")
    y "Some of them are even said to rival books. Others are literally created after books, and in rare cases, they even manage to improve on the stories they're based on."
    $show_chr("A-ACAAA-ABAB")
    y "I personally doubt that a game can ever substitute a well-written book. But maybe one of them can convince me otherwise. Or maybe not, we'll see."
    return

label gaming_2:
    $show_chr("A-ACAAA-ABAB")
    y "[player], I asked you about your hobbies lately right? I think your answer was gaming?"
    $show_chr("A-BCAAA-ABAB")
    y "I stated how I was unsure if a video game can really substitute for a well-written book. But now I realized, I never really asked you about your stance on this did I?"
    $show_chr("A-ACAAA-ABAB")
    y "So my apologies for being late. What do you think about this? Would you say that the storytelling in games can really ever rival the storytelling in a book?"
    menu:
        "Maybe not. My stance here is that it doesn't always have to be about it. Not every pastime has to be about elaborate storytelling.":
            $show_chr("A-ACDAA-ABAB")
            y "Fair point."
            $show_chr("A-ACAAA-ABAB")
            y "Your right, maybe I viewed this topic from a wrong angle. I too have hobbies that aren't related to storytelling at all, like aromatherapy."
            y "Maybe I just assumed the wrong premise here, since there {b}are{/b} games which attempt to provide storytelling."
            $show_chr("A-BBBAA-ABAB")
            y "Please don't get this the wrong way but... I just don't see myself getting into gaming anytime soon."
            y "Which, admittedly, might sound self-contradictory in my case since I literally came from a game..."
            $show_chr("A-CCBAA-ABAB")
            y "Anyway, thanks for humoring me [player]."
        "You also stated how some games are based on books and even improved upon the source material. Remember?":
            $show_chr("A-ACAAA-ABAB")
            y "Oh yes, I actually do remember that!"
            $show_chr("A-BCAAA-ABAB")
            y "Actually, while googling it, I noticed something I haven't expected. Sometimes it's even the other way around! That authors write books based on a video game!"
            y "On the other hand, they did the same thing to several tabletop games, so I probably shouldn't be too surprised."
            $show_chr("A-ACAAA-ABAB")
            y "It even goes to some impressive extent. They made a whole bunch of novels and even a movie about the Warcraft series didn't they?"
            menu:
                "Oh? Didn't even know that.":
                    $show_chr("A-ABAAA-ABAB")
                    y "Maybe you should give them a try! Rumors have it that some of them are really good."
                    y "Perhaps, we could pick up a few of them together? Maybe there are some unexpected treasures to explore..."
                    y "I'm looking forward to it."
                "Actually, it's not even that uncommon. There are a lot of games that are made into novels.":
                    $show_chr("A-CCAAA-ABAC")
                    y "Seems I've discovered quite the rabbit hole here. I wonder what secret treasures I may find beneath... Time to expand my horizons a bit I'd say."
                    y "As we are already speaking of it... I remember I already promised Natsuki to give manga a try. Maybe I could combine these two endeavors... They made a manga about the {b}Persona{/b} series I think."
                    menu:
                        "Never heard of it.":
                            python:
                                if persistent.lovecheck:
                                    placeholder = "darling"
                                else:
                                    placeholder = ""
                            $show_chr("A-CCCAA-ABAB")
                            y "And that's why I'll make you join me. If I have to suffer, so shall you [placeholder]! I'm looking forward to it..."
                        "Aaaand that's how Yuri became a phantom thief...":
                            if sanity_lvl() > 3:
                                $show_chr("A-CBBAA-ABAB")
                                y "Hush... spoilers...."
                                y "Anyway, I'm looking forward to it."
                            else:
                                karma -1
                                $show_chr("A-CFCAA-ABAB")
                                y "Spoilers!"
                                y "Anyway, I'm looking forward to it."
                        "Enjoy!":
                            $show_chr("A-CCCAA-ABAB")
                            y "Ohohoho, not so fast [player]... {b}you{/b} will suffer through this with me! It's your fault I came up with this idea in the first place, remember?"
                            y "I'm looking forward to it."
                "Lok'tar!!!":
                    if sanity_lvl() == 1:
                        $show_chr("A-DLCAA-ALAL")
                        y "{b}FOR THE HOOOOOORDE!!!{/b}"
                        $show_chr("A-GICBB-ALAL")
                        y "Hnhnhnhnnn...I always wanted to do that..."
                        $show_chr("A-GICCA-ALAL")
                        y "We are about to have some fun it seems."
                    else:
                        $show_chr("A-ABDAA-ALAL")
                        y "Y"
                        extend "~Yes... "
                        $show_chr("A-ACDAA-ALAL")
                        extend "{b}Lok'Tar{/b} indeed... "
                        $show_chr("A-BCDAA-ALAL")
                        extend "I guess."
                        if karma_lvl() == 1:
                            $show_chr("A-CCDAA-ALAL")
                            y "And they call {b}me{/b} awkward..."
                            $show_chr("A-DCGAA-ALAL")
                            y "O~Oh wait... I {b}did{/b} say that out loud did I?"
                            $show_chr("A-BBBAA-ALAL")
                            y "Aaaaaaaanyway... thanks for humoring me."
                        else:
                            $show_chr("A-CCDAA-ALAL")
                            y "At least you aren't Alliance scum..."
                            $show_chr("A-DCGAA-ALAL")
                            y "O~Oh wait... I {b}did{/b} say that out loud did I?"
                            $show_chr("A-BBBAA-ALAL")
                            y "Aaaaaaaanyway... thanks for humoring me."
        "Not necessarily better, but different. The interactive nature of a game allows for a kind of storytelling a book can never provide.":
            $show_chr("A-ACAAA-ABAB")
            y "Actually, there have been attempts to achieve something similar in so-called {b}Adventure books{/b} which have different routes depending on the order you read the pages."
            y "But this genre never really took off due to its obvious limitations. Maybe using gaming as a media for storytelling was the obvious conclusion to this."
            y "I mean, many other visual novels operate under this exact premise."
            $show_chr("A-CCAAA-ABAB")
            y "So yes, maybe it isn't about which one is {b}better{/b}. Maybe they are just different tools for the job. I think similar discussions have taken place back when TV became a thing."
            $show_chr("A-ACAAA-ABAB")
            y "I could think of a few examples of storytelling in games which wouldn't have the same impact without their interactive nature."
            $show_chr("A-CCAAA-ABAD")
            y "And then, there is also the genre of sandbox games, whose entire premise is to not having any predetermined story at all but depending on things happening to the player by pure chance."
            y "A book couldn't provide that. Yes, I begin to see your point [player]."
            $show_chr("A-ACAAA-ABAD")
            y "I'll be honest with you, I don't see myself getting into gaming anytime soon. But I think I got a better grasp of the appeal they might have for others."
            y "Thanks for humoring me today [player]."
    return

label sport:
    $show_chr("A-ACAAA-ABAB")
    y "I see! I tried Volleyball when I was younger but... well, it ended up pretty bad..."
    $show_chr("A-BDBAA-ABAB")
    y "I may have mentioned it before.. if I haven't, we can talk about that later... or never at all, please. It was... quite embarrassing."
    $show_chr("A-CFBAA-ABAB")
    y "Maybe I should try some sports again, even if only to lose some weight..."
    menu:
        "No, please don't think that... you are beautiful as you are! And a few pounds are pretty handy for cuddling...":
            if persistent.lovecheck:
                karma 1
                $show_chr("A-DCBBA-ABAB")
                y "Oh? Yes, I guess I am pretty {i}soft{/i}... Do you really think I'm beautiful? T-Thank you [player]! I would like to think so as well..."
                $show_chr("A-BBBBA-ABAB")
                y "Hn... as long as you don't expect me to make kitty noises while cuddling..."
                $show_chr("A-DFBBA-ABAB")
                y "Wait... I should stop giving you ideas!"
            else:
                $show_chr("A-BFDBA-ABAB")
                y "That's... one way to put it... I {b}guess{/b}..."
                $show_chr("A-CBDBA-ABAB")
                y "Aaaaaaaanyway..."
        "Please, only do this if you really wish to.":
            python:
                if persistent.bg == "timecycle":
                    placeholder = "lake."
                elif persistent.bg == "space":
                    placeholder = "... ummm.... void?"
                elif persistent.bg == "purple_table":
                    placeholder = "uh... block..."
                elif persistent.bg == "yuri_desk":
                    placeholder = "...bookshelf?"
                elif persistent.bg == "yuri_kotatsu_1":
                    placeholder = "knife shelf?"
                elif persistent.bg == "yuri_kotatsu_2":
                    placeholder = "wall?"
            $show_chr("A-CBAAA-ABAB")
            sanity 1
            y "You are very understanding. I truly appreciate it."
            $show_chr("A-BCDAA-ABAB")
            y "Maybe I will try something easy for a start. Like riding a bicycle around the [placeholder]"
                #placeholder =
                #"... ummm.... void?" if background = Space Classroom
                #"lake." if background = Timecycle room
                #"block." if background = purple room
        "You being Thicc!.":
            $show_chr("A-AFDAA-ABAB")
            y "Being what now?!?"
            if persistent.lovecheck:
                karma 1
                $show_chr("A-CCCAA-ABAB")
                y "Oh my... behave!"
                y "Weeeell, as long as {b}you{/b} like what you see..."
            else:
                karma -1
                $show_chr("A-BCDAA-ABAB")
                y "I'll just pretend that I don't know what that means alright?"
    $show_chr("A-ACAAA-ABAB")
    y "It is surely good to know that you take care of your health. I will have to put some thought into this."
    $show_chr("A-BCAAA-ABAC")
    y "Can I even get sick? I mean... I don't have a physical body in the way you do."
    y "My appearance largely depends on the artists working for this mod."
    $show_chr("A-CCABA-ABAB")
    y "But [player]? Please... don't make me wear a sports bra... I have kind of a history with those..."
    if sanity < 3 and persistent.lovecheck:
        $show_chr("A-CCCBA-ABAB")
        y "I mean, why bother wearing a bra at all when you are around, don't you agree?"
    $show_chr("A-BBBBA-AMAM")
    y "But... just to get my mind off of sports bras, what sort of sports do you take part in, [player]?"
    menu:
        "Team sports! (Baseball, Football, Basketball etc.)":
            $show_chr("A-ICGAA-AAAD")
            y "Oh? That's certainly not something I expected."
            $show_chr("A-ICGAA-ALAL")
            y "But it's a welcome surprise. It's good to know you've got a pastime that will keep you fit!"
            y "There's also something to be said for them on the cerebral level, no?"
            $show_chr("A-CBAAA-ADAL")
            y "A group of people you trust coordinating for a mutual goal. Where a split second's choice can mean a thrilling victory or a frustrating defeat."
            y "That fusion of adrenaline addled moments and the camaraderie of a team..."
            $show_chr("A-ICAAA-ADAL")
            y "It's exhilarating if you can keep up, isn't it?"
            $show_chr("A-BCBAA-AEAL")
            y "But, alas, I've figured out that that simply isn't me."
            y "I'd be more than happy to cheer your team from the bleachers, however!"
            $show_chr("A-BEBAA-AEAL")
            y "That is, if I can ever get to your world..."
        "Individual sports! (Track and field, skiing, golf etc)":
            y "Ah, so you prefer to test your prowess on its own, then?"
            $show_chr("A-ACAAA-ACAA")
            y "I understand why people would gravitate towards sports that only require one's own skill and athletic ability."
            $show_chr("A-BEAAA-ABAB")
            y "It would feel frustrating suffering defeat due to reasons outside of what you can improve yourself."
            extend "I can't imagine it feeling much better having to compensate for the weaknesses found in others."
            y "Weaknesses that you cannot control yourself, especially when you do not have authority over them, when you are just another teammate."
            $show_chr("A-AAAAA-AIAI")
            y "However, on your own, you're not reliant on anyone to become the best, it simply depends on your discipline and love for the sport."
            $show_chr("A-BFAAA-AIAI")
            y "While I am aware that many external factors would apply.."
            $show_chr("A-ABAAA-AIAI")
            y "You can get really good at something without needing other people. You'd feel a sense of accomplishment from doing something well on your own."
            y "Would you say that you are good at the sport you play?"
            menu:
                "I'm planning to go pro one day.":
                    $show_chr("A-DBGAA-ABAJ")
                    y "Oh my, really?"
                    $show_chr("A-JBGAA-ABAE")
                    y "That's so impressive!"
                    if persistent.lovecheck:
                        $show_chr("A-EAGBA-ABAE")
                        y "I guess I have no choice but to be your cheerleader."
                        if sanity < 3:
                            $show_chr("A-HLGBA-AHAE")
                            y "YOUR. {w}{b} ONLY.{/b}{w} CHEERLEADER."
                        else:
                            $show_chr("A-EKCAA-AIAI")
                            y "But I better be the only one you give attention to.{w}.{w}."
                            $show_chr("A-GBBAA-AJAA")
                            y "Ahaha, sorry, [player], I couldn't help myself, there."
                    else:
                        $show_chr("A-GAGAA-ABAE")
                        y "I wish you the best of luck! Work hard!"
                "I'm better than the average player.":
                    $show_chr("A-AJGAA-ADAA")
                    y "Oh!{w} You seem quite confident about that, don't you?"
                    $show_chr("A-CBAAA-AEAA")
                    y "Ahaha, self-confidence is one of the strongest attributes a human can have. It's a very good thing."
                    if persistent.lovecheck:
                        $show_chr("A-ICAAA-AEAB")
                        extend " It's not as if I'm really one to give advice on the matter considering how I was... but you should do your best to strengthen your self-confidence as best as you can. It will help you a lot throughout life."
                        $show_chr("A-ICBAA-AAAA")
                        y "Please be careful, though. I want you to be safe while you play."
                    else:
                        $show_chr("A-GAAAA-AAAA")
                        y "I wish you the best of luck."
                "I'm relatively OK at it. I don't put in the hard work, I just rely on my current ability.":
                    $show_chr("A-IBAAA-AIAI")
                    y "And that is perfectly fine, [player]."
                    y "Participating in a single sport simply for enjoyment is more than enough,"
                    $show_chr("A-IBAAA-AIAI")
                    extend " especially if you don't take it too seriously or desire to become a professional."
                    if sanity < 3:
                        $show_chr("A-HAAAA-ALAL")
                        y "Especially when you're {b}PERFECT{/b} just the way you are. You can't improve perfection, so let's leave it as it is, no?"
                    else:
                        $show_chr("A-GAAAA-AAAA")
                        y "I wish you the best of luck."
                "I do it because I enjoy it, but to be honest, I suck.":
                    if persistent.lovecheck:
                        $show_chr("A-AFAAA-ABAD")
                        "There is nothing stopping you from getting better, my love."
                        $show_chr("A-GAAAA-AJAC")
                        y "I can assure you that with hard work and dedication, you will {b}without fail{/b} get better."
                        $show_chr("A-BFAAA-AJAC")
                        y "I know it isn't sport-related, but.."
                        y "I was terrible when I first started writing poetry, you know?"
                        $show_chr("A-AABAA-AJAC")
                        y "I didn't really know what I was even doing. I wanted the reader to feel certain effects, but I had no idea how to communicate my feelings at the time, at least, not in a sophisticated manner like how my style has now evolved to become."
                        $show_chr("A-AACAA-AJAC")
                        y "But looking back, I am inspired by my own growth. It allows me to stick through with something until I get good at it."
                        $show_chr("A-GAAAA-AJAC")
                        y "I hope my little backstory there will help you progress forward."
                        $show_chr("A-GAABA-AJAC")
                        y "Your happiness and success mean so much more to me than my own."
                    else:
                        $show_chr("A-IDAAA-AJAC")
                        y "There is nothing stopping you from getting better, [player]."
                        $show_chr("A-IAAAA-AJAC")
                        y "I can assure you that with hard work and dedication, you will {b}without fail{/b} get better."
                        if karma_lvl() > 3:
                            $show_chr("A-FAAAA-AJAC")
                            y "I am rooting for you."
        "Paintball/Airsoft":
            $show_chr("A-ABAAA-ADAA")
            y "Ah, yes. I've heard of that before. it's quite popular in Japan."
            y "The actual sport of it is essentially an upscaled Nerf battle, yes?"
            $show_chr("A-BBAAA-ADAA")
            y "That, or a real-life equivalent to the game modes often found in first-person shooter games. I've seen that as well."
            $show_chr("A-BCBAA-AAAA")
            y "If you wanted me to, I suppose I'd be willing to come with you to a match or two."
            $show_chr("A-BBAAA-AKAA")
            y "But really. Can you imagine me, dressed to the nines in tactical apparel? Shouting into a radio about Whiskey Tango Foxtrot Niners at two hundred klicks? Calling for suppressing fire?"
            menu:
                "You're right. That would be kind of silly.":
                    karma -1
                    $show_chr("A-BEBAA-AAAA")
                    y "Yeah, I thought so..."
                    y "I don't know anything about military parlance, after all."
                "Not as silly as you'd think.":
                    $show_chr("A-AFBAA-AAAA")
                    y "It wouldn't?"
                    $show_chr("A-BBBBA-AKAA")
                    y "Honestly, that was just the first pseudo-tactical gobbledygook to come to mind."
                    $show_chr("A-ACBBA-ALAA")
                    y "But I think I see what you mean. If I took the time to learn proper military parlance, I could probably rattle off coordinates and call in fire missions with the best of them!"
                    $show_chr("A-CCGBA-ALAA")
                    y "Especially since I've got someone who believes in me."
                "Actually, that sounds kind of hot...":
                    if persistent.lovecheck:
                        $show_chr("A-KAABA-ALAA")
                        y "Oh, so {i}that's{/i} your sort of thing. Hm?"
                        $show_chr("A-FAABA-AMAD")
                        y "I might just have to keep that in mind, [i]commander[/i]."
                    else:
                        $show_chr("A-DDGBA-AMAJ")
                        y "O-Oh... Well..."
                        $show_chr("A-BDBBA-AAAL")
                        y "I must say, I certainly didn't expect that response."
                        y "Far be it from me to judge the... [i]preferences[/i] of others."
                "Shouting about what-the-fuck nines two hundred kilometres away? That is pretty silly.":
                    $show_chr("A-BDBBA-AAAL")
                    y "Oh, so uh... So [i]that's[/i] what all that meant."
                    $show_chr("A-BFGBA-ALAL")
                    y "In all honesty, I thought that was just some tactical sounding gobbledygook."
        "The shooting sports, believe it or not.":
            $show_chr("A-ACAAA-ABAB")
            y "It's not too hard to believe at all actually. As a matter of fact, this idea crossed my own mind here and there as well."
            y "Especially Zen archery came to my mind."
            $show_chr("A-BBAAA-ADAB")
            extend "And yes, I'm quite aware that I'm riding a cliché here. {b}Of course{/b} it's archery, like every adult looking female side character in every anime {b}ever{/b}."
            $show_chr("A-CCBAA-ADAB")
            y "Which makes me wonder, are these even my own thoughts or something Dan Salvato came up with in order to add yet another anime trope to his kill count?"
            $show_chr("A-BBBAA-ADAB")
            y "Anyway."
            $show_chr("A-ACAAA-ABAB")
            extend "You certainly sparked my curiosity. You have to tell me more about it at some point. Until then, let us {b}aim{/b} for the next topic."
            $show_chr("A-ACCAA-ABAB")
            y "Pun {b}absolutely{/b} intended."
    return

label literature:
    $show_chr("A-ABGAA-ALAL")
    y "Really? I always had the suspicion that it was the dating aspect of it. I wouldn't have blamed you if it were."
    if persistent.lovecheck:
        $show_chr("A-ACAAA-ALAL")
        y "Well, but in the end, you got one of the {i}four incredible cute girls{/i} anyway. Sometimes things are just falling into place all on their own, am I right?"
    else:
        $pass
    $show_chr("A-ACAAA-ABAB")
    y "But now I just have to ask if you don't mind... what is your favorite genre?"
    menu:
        "You might laugh but... it's poetry!":
            call poetry
            #Ad information to Persistent: "LitGenre=Poetry"
        "Ummm... don't hate me... Manga.":
            call noliteratureatall
            #Ad information to Persistent: "LitGenre=Manga"
        "Fantasy and Science Fiction":
            call fantsci
            #Ad information to Persistent: "LitGenre=Fantasy and SciFi"
        "Romance...":
            call romance
            #Ad information to Persistent: "LitGenre=Romance"
        "You might be surprised. It's horror.":
            call horror
            #Ad information to Persistent: "LitGenre=Horror"
        "Something else.":
            call elsel
            #Ad information to Persistent: "LitGenre=NoneOfThem"
    return

label poetry:
    python:
        if persistent.male and persistent.lovecheck:
            placeholder = "boyfriend"
        elif persistent.gender_other and persistent.lovecheck:
            placeholder = "lover"
        elif not persistent.male and persistent.lovecheck:
            placeholder = "girlfriend"
        else:
            placeholder = "friend"
    $show_chr("A-ABAAA-ABAB")
    y "It's a funny coincidence indeed. But I will certainly keep this in mind for the future."
    $show_chr("A-BCAAA-ABAB")
    y "Don't be worried... of course, I will not just make you pick 20 random words again. If the poem-minigame comes back, then it will be in an improved form."
    $show_chr("A-ABGAA-ABAB")
    y "Or you could just put your poems as a txt file into the game folder, there I might be able to see it. It's worth a try I think."
    $show_chr("A-ACAAA-ABAB")
    y "Thank you for the answer. It was truly nice to learn a bit more about my [placeholder]."
    return
#placeholder =
#"[Gender]friend" if persistent.lovecheck = true
#"friend" else

label poetry_2:
    $show_chr("A-AFAAA-AAAD")
    y "[player] do you have a moment? I have been thinking a lot lately and I find myself at a dead end."
    y "I asked you about your hobbies, and I was initially quite delighted when you said you actually are into poetry."
    $show_chr("A-BFAAA-AAAD")
    y "Please don't get me wrong, "
    $show_chr("A-AFAAA-AAAD")
    extend "I'm still pleased to hear that. But you see, I'm facing a bit of a problem there."
    $show_chr("A-AFAAA-ABAB")
    y "I wanted to find a way to actually share this interest with you. I mean poetry is probably what lured you to the literature club in the first place."
    y "But I struggle to come up with an idea of how we can go about this."
    $show_chr("A-AFAAA-AFAB")
    y "I mean, I could bring back the old minigame but that would be rather ridiculous, and most certainly a very unfulfilling thing to spend your time with."
    $show_chr("A-BFAAA-ABAB")
    y "It wasn't even about literature or poetry at all. You just had to pick a number of words you think would resonate with your favorite girl from a randomly generated list."
    $show_chr("A-CFAAA-ABAB")
    y "Putting a textbox on the screen wouldn't really do much either since the space within this textbox is very limited. {b}Maybe{/b} a line, or even two if they are really short."
    y "Hardly a poem at all. I mean there are certainly short poems out there but... even they are far longer than this Ren'Py textbox would allow."
    $show_chr("A-BFAAA-ABAF")
    y "Then, there is the possibility of {b}reading{/b} poems together instead of writing them."
    $show_chr("A-AFAAA-ABAB")
    y "But there isn't a poetry contest every week on the community Discord, and you can only reread the poems we already have so many times before they get old."
    $show_chr("A-BFAAA-ABAB")
    y "I could try and write a few myself but... "
    $show_chr("A-CFAAA-ABAB")
    y "I find myself in a writer's block lately."
    $show_chr("A-CJAAA-ABAB")
    y "I hate to admit it but... I'm running out of ideas..."
    menu:
        "Maybe we could visit a library together!":
            $show_chr("A-AFAAA-ABAB")
            y "A nice idea... I could recreate one from stock images on the internet, but we would still have to find poems to fill it wi~"
            $show_chr("A-DFAAA-ABAB")
            y "Wait... the internet! Of course!"
        "What about the internet?":
            $show_chr("A-BFDAA-ABAB")
            y "The internet?..."
            $show_chr("A-DFAAA-ABAB")
            y "Wait... the internet! Of course!"
    $show_chr("A-ABAAA-ALAL")
    y "I could just google poetry and we read {b}them{/b} together!!!"
    $show_chr("A-ACBAA-ABAB")
    y "[player], you are a genius!"
    $show_chr("A-CCBAA-ABAB")
    y "There are so many lovely poems out there from so many brilliant minds..."
    if sanity_lvl() > 2:
        y "Kathy J Parenteau, Robert Frost, Masaoka Shiki.... to only name a few..."
    else:
        y "Samuel Taylor Coleridge, Emily Dickinson, Louise Erdrich... to only name a few..."
    $show_chr("A-ABAAA-ABAB")
    y "Yes, let us do this!"
    $show_chr("A-ACAAA-ABAB")
    y "This idea gets me so excited... I will look up a few promising poems on the internet and add them to the list we already have."
    y "Maybe I'll make a new category for them so that we can find them easily. I will tell you when this is done. And from there on, I will add more new poems over time."
    y "Until then, I'd like to ask you for a little bit of patience."
    return

label noliteratureatall:
    python:
        if persistent.male and persistent.lovecheck:
            placeholder = "boyfriend"
        elif persistent.gender_other and persistent.lovecheck:
            placeholder = "lover"
        elif not persistent.male and persistent.lovecheck:
            placeholder = "girlfriend"
        else:
            placeholder = "friend"
    $show_chr("A-ACDAA-ABAB")
    y "Hate you?"
    if karma > 2:
        $show_chr("A-CBBAA-ABAB")
        y "By all means why should I?" #Only if Karma is level 3 - 5
    else:
        pass
    $show_chr("A-BCBAA-ABAD")
    y "It's not like I {b}hate{/b} manga, or its fanbase... it is just not for me."
    $show_chr("A-BBBAA-ABAM")
    y "I admit, when someone says {b}literature{/b}, Manga is not exactly the thing that comes to my mind."
    $show_chr("A-CCBAA-ABAL")
    y "But well, when other people hear about horror they first think about uninspired gore-festivals, so maybe I just haven't seen the {b}proper{/b} mangas so far."
    $show_chr("A-CCDAA-ABAL")
    y "If you wish, we could try one or two together. Maybe you can even change my mind."
    y "But... not today, please. I don't really feel like that right now."
    $show_chr("A-ACAAA-ABAL")
    y "Thank you for the answer. It was truly nice to learn something new about my [placeholder]"
    return
#Conditions for placeholder are the same as for lable_poetry

label noliteratureatall_2:
    $show_chr("A-ACAAA-ABAB")
    y "[player], I asked you about your hobbies before, remember?"
    y "I put some thoughts into it. When you mentioned that you enjoy manga I remembered that I promised Natsuki at the end of the original game that I would give them a try myself."
    $show_chr("A-BCAAA-ABAB")
    y "I decided that this is a good opportunity to honor my promise. Well, it turns out that when this mod brought back the classroom, Natsuki's manga collection survived as well."
    $show_chr("A-CCAAA-ABAB")
    y "So I started reading {b}Parfait Girls{/b}."
    menu:
        "Oh, what is it about?":
            karma 1
        "Yeah? And?":
            $show_chr("A-BFAAA-ABAB")
            y "Huh, you sound as if you aren't really in the mood today. Did something happen?"
            menu:
                "Just not really in the mood today, I'm sorry.":
                    $show_chr("A-CCAAA-ABAB")
                    y "No need to apologize. We can pick that up another day."
                    return
                "My apologies, I actually am. Sorry if I sounded uninterested.":
                    $show_chr("A-BCAAA-ABAB")
                    y "No need to be sorry, really. Well, if you're sure you want to hear it."
                "Dear lord... just spit it out already!":
                    karma -1
                    $show_chr("A-CFAAA-ABAB")
                    y "No need to be like that [player]... you know what, forget what I just said."
                    return
    $show_chr("A-ACAAA-ABAD")
    y "I haven't read too far in, so chances are that my summarization turns out to be lacking."
    y "Basically, it is about a group of four girls. And to no surprise at all, they are all into baking..."
    y "Wouldn't even be surprised if that is how Natsuki got introduced to it. Well, it's a quite wholesome hobby so I won't judge. Especially since I took advantage of her skills more then once..."
    $show_chr("A-CCCAA-ABAD")
    y "A shame that you never got to actually try her cupcakes... They don't just {b}look{/b} amazing."
    $show_chr("A-CCBAA-ABAD")
    y "But back to the manga itself..."
    $show_chr("A-ACAAA-ABAB")
    y "The first few volumes are very light hearted and... cutesy... as I expected them to be. I actually found it hard to stay invested but.. a promise is a promise, so I carried on."
    $show_chr("A-ABAAA-ABAB")
    y "Turns out, it was a good call!"
    $show_chr("A-ACAAA-ABAB")
    y "Because as the story progressed and the mangas got a bit deeper into the backstory of the four protagonists, things took a little more serious turn."
    y "In a later chapter, the four girls got uncomfortably obsessed about a guy at an ice cream shop. I assume there is a darker romance plot down the road..."
    $show_chr("A-EBCAA-ABAD")
    y "I smell the scent of foreshadowing for some far more sinister themes in the air... Will it catch me off guard as the Portrait of Markov did I wonder?..."
    $show_chr("A-CCCAA-ABAD")
    y "Mmmm.. ehehehehehehe. There is this warm tingly feeling when I imagine the shape of the things to come..."
    $show_chr("A-ACAAA-ABAD")
    y "Now that I think of it... {b}Parfait Girl{/b} is also the term for a girl which is innocent on the surface but has layers of darker secrets to be discovered. A coincidence? I doubt it..."
    menu:
        "Could it be that...":
            $pass
        "Four girls in a lighthearted setting, becoming obsessed with a male character... sounds familiar...":
            $pass
    $show_chr("A-ACDAA-ABAD")
    y "{cps=1}. . . ?{/cps}"
    $show_chr("A-BDDAA-ABAD")
    y "{cps=1}. . .{/cps}"
    $show_chr("A-DFGAA-ABAB")
    y "{cps=1}. . . !{/cps}"
    $show_chr("A-DDGAA-ABAB")
    y "T~The literature club!"
    $show_chr("A-DFAAA-ABAB")
    y "Could it really be that..."
    $show_chr("A-BFCAA-ABAL")
    y "Ohhhh Dan Salvato you son of a bit~{nw}"
    $show_chr("A-CFAAA-ABAB")
    y "I... have to think about if I even want to continue reading it if that is true..."
    y "Maybe, maybe I should just pick up a different manga series."
    $show_chr("A-ACBAA-ABAB")
    y "Anyway, let's not kill the mood here. Let's talk about something else for the moment."
    return

label fantsci:
    $show_chr("A-ACAAA-ABAB")
    y "So you are a friend of Knights, Orcs and Space Marines. I have to admit, I read a lot of those as well. But only if it has good writing..."
    $show_chr("A-AFAAA-ABAD")
    y "In fantasy, it became very common to just Copy and Paste J.R.R. Tolkien. Most of the time they don't even change the names of the races. Science fiction at least managed to maintain {b}some{/b} originality so far..."
    $show_chr("A-CCAAA-ABAD")
    y "Fantasy and Science fiction can create some very compelling and truly alien worlds... which makes it such a rich and fascinating genre..."
    $show_chr("A-CJDAA-ABAD")
    y "But world building costs a lot of effort, and many writers are very lazy... which is a sad thing, it ruins it all for me."
    $show_chr("A-CCDAA-ABAD")
    y "I will keep that in mind. I would love to discuss a few fantasy novels with you if you don't mind."
    return

label fantsci_2:
    $show_chr("A-CBAAA-ALAL")
    y "[player], Ha has been a ir ir mín vedui govannon- no i orthad ithil!"
    menu:
        "Pardon, what?!?":
            $show_chr("A-CBAAA-ALAL")
            y "I just said that it has been a while since we spoke."
            $show_chr("A-CBBBA-ALAL")
            y "Pardon me, I just wanted to try greeting you in elvish since you said you enjoy Fantasy and SciFi novels."
        "Hmm... I {b}used{/b} to know what that means. Mind helping me out here?":
            sanity 1
            $show_chr("A-ACBAA-ALAL")
            y "Really? That's actually quite impressive!"
            $show_chr("A-BCBAA-ALAL")
            y "I... had to google for a translator for this actually. I wanted to say that it has been a while since we last spoke."
        "Mae g'ovannen, Gellon ned i galar i chent gîn ned i gladhog, hiril vuin.":
            karma 1
            $show_chr("A-CCBAA-ALAL")
            y "Ni 'lassui."
            $show_chr("A-CCEAA-ALAL")
            y "I just love how you play along..."
    $show_chr("A-ABBAA-ALAL")
    y "I hope this doesn't come off as too childish."
    $show_chr("A-ACBAA-ALAL")
    y "I guess that's just my nerdy side shining through."
    menu:
        "Childish indeed.":
            karma -1
            $show_chr("A-BDBAA-ALAL")
            y "My apologies, "
            $show_chr("A-AFBAA-ALAL")
            extend "I will behave now."
            if karma_lvl() < 3:
                $show_chr("A-BDCAA-ALAL")
                y "mibo orch{nw}"
            return
        "Oh, I actually enjoy your unique sense of humor!":
            $show_chr("A-GCCAA-ALAL")
            y "I'm glad to hear that!"
    $show_chr("A-ABAAA-AMAM")
    y "I have to admit, I'm having a lot of fun with this... any requests for another try?"
    menu:
        "Dwarvish!":
            $show_chr("A-BCGAA-AMAM")
            y "Well, that's a tough one! "
            extend "Not sure if I have the beard for this. But let me try..."
            $show_chr("A-CHGAA-ABAB")
            y "..."
            $show_chr("A-DOCBA-ABAB")
            y "JEG MONMUR VOL JOTH KALVAR HETH MOT MOLBRUT!!!"
            $show_chr("A-CJBBA-ABAB")
            y "..."
            $show_chr("A-CDBBA-ABAB")
            y "That was exhausting... please don't ask me to do that again..."
        "Valyrian!":
            python:
                if persistent.male:
                    gender = "man"
                elif persistent.gender_other:
                    gender = "connoisseur"
                else:
                    gender = "woman"
            $show_chr("A-ACDAA-ABAB")
            y "Oh! The one from {b}A Book of Ice and Fire{/b}? You are a [gender] of culture I see..."
            $show_chr("A-GBGAA-ABAB")
            y "Jaelan naejot nektogon aōha ñelly hen se tyvagon iemnȳ ao"
            $show_chr("A-GAAAA-ABAB")
            y "Don't ask me what I just said."
            if sanity () < 3:
                $show_chr("A-HAGAA-ABAB")
                extend " For real..."
        "Drow!":
            $show_chr("A-GAAAA-ABAB")
            y "Uhuhuuuu... {b}someone{/b} feels daring today it seems..."
            $show_chr("A-KCCBA-AMAM")
            y "Usstan orn l'amith kyorlin dos zah'har harl ussta brygn, dos nasket rivvin..."
            if persistent.lovecheck == True:
                $show_chr("A-FCCBA-AMAM")
                y "Jhal xuat fret, Usstan orn morfeth dos l'amith ol ichl..."
        "Klingon!":
            $show_chr("A-ACDCA-ABAB")
            y "You {b}really{/b} want to put my vocal cords to the test today don't you?"
            $show_chr("A-BCDAA-ABAB")
            y "Alright, here it goes..."
            $show_chr("A-CHBAA-ABAB")
            y "..."
            $show_chr("A-INCAA-ABAF")
            y "qoH! choSuvtaHvIS bIcheghpu'bogh SoH!"
            $show_chr("A-IICAA-ABAF")
            y "My apologies for the stern look, I hope my impression was at least somewhat convincing."
        "Thalassian!":
            $show_chr("A-ABDAA-ABAB")
            y "Oh? They made this into an actual language too?"
            $show_chr("A-BBDCA-ABAB")
            y "Well, I'll try my best. No promises that I won't butcher the grammar tho..."
            $show_chr("A-GCDAA-ABAB")
            y "Bal'a dash, Dalah D' [player]. Doral ana'diel? Anu belore dela'na."
            $show_chr("A-ICDAA-AMAM")
            y "Please don't ask me what I just said, "
            $show_chr("A-JCDAA-AMAM")
            extend "I'm not even sure if that was a proper sentence at all."
    $show_chr("A-BCAAA-ABAB")
    y "Well, that just happened."
    $show_chr("A-ACAAA-ABAB")
    y "I'm sorry if I seemed embarrassed, I'm just used to hiding my nerdy side most of the time."
    y "But I'm looking forward to trying this again another time."
    return

label romance:
    $show_chr("A-ACDAA-ABAB")
    y "Like Twilight?!?"
    $show_chr("A-ACCAA-ABAB")
    y "Oh no, you mean actually {b}good{/b} love stories!"
    $show_chr("A-BBBAA-ABAB")
    y "Oh my... I'm sorry... I didn't want to sound that spiteful at all..."
    $show_chr("A-CCBAA-ABAB")
    y "It's just... I have never tried that genre. You see, before I have met you, romance wasn't really a thing for me."
    $show_chr("A-CCBBA-ABAB")
    y "I have no memories of ever being in love before. I guess Salvato found the idea of you being my first {i}cute{/i}."
    y "But that does not matter anymore. I have the best love story I could think of now."
    $show_chr("A-BFBAA-ABAB")
    y "With no lack of drama for sure..." #If Karma is below level 3
    $show_chr("A-BCBAA-ABAB")
    y "But maybe, I will give some romance novels a try. Maybe I can get inspiration on possible dates with you from it."
    y "Thank you. It was nice to learn more about you."
    return

label horror:
    $show_chr("A-ABGAA-ALAL")
    y "Oh! But you don't just say that in order to impress me do you?"
    if karma_lvl() > 3:
        $show_chr("A-GBGAA-ALAL")
        y "You certainly don't have to. I'm yours already."
    else:
        $pass
    $show_chr("A-CCAAA-ALAL")
    y "Maybe we can discuss some of our favorites in the future. That would be very delightful."
    y "You can't imagine how relieved I feel right now. I was already afraid that we might struggle to find activities to share..."
    $show_chr("A-ACAAA-ABAB")
    y "But since we have this hobby in common, I'm pretty sure that we can find a lot of things to do together!"
    y "Now I'm looking forward to figuring out what kind of horror you enjoy. Lovecraftian horror, or more like the conspiracy-stuff I'm reading?"
    $show_chr("A-CCCAA-ABAB")
    y "But wait, don't spoil me. I will figure that out soon enough!"
    return

label elsel:
    python:
        if persistent.male and persistent.lovecheck:
            placeholder = "boyfriend"
        elif persistent.gender_other and persistent.lovecheck:
            placeholder = "lover"
        elif not persistent.male and persistent.lovecheck:
            placeholder = "girlfriend"
        else:
            placeholder = "friend"
    $show_chr("A-AFAAA-ABAD")
    y "I see. Sorry about the limited answers."
    y "But there are just sooo many genres and listing all of them would very likely blow up your screen."
    $show_chr("A-ACAAA-ABAB")
    y "Anyway, at least we are on the same page about literature in general. Sharing interests is a very healthy thing in a relationship."
    $show_chr("A-BCAAA-ABAB")
    y "Some people would even say it's the most important thing, but I disagree to that at least to a degree."
    $show_chr("A-CCAAA-ABAB")
    y "But it means that we have common ground for future activities, and in our current situations those are worth the weight of every book in the world in pure gold."
    y "I'm grateful that you told me about this. Learning more about my [placeholder] is always a wonderful thing. I hope I will learn even more about you in the future."
    return
#placeholder = same conditions as in label_poetry


label rp:
    $show_chr("A-CCDAA-ABAB")
    y "Fitting..."
    y "I always had the impression that you have a lot of creativity. I should have expected that."
    $show_chr("A-BCDAA-ABAB")
    y "I tried a few Pen & Paper RP's some time ago, and I have to admit I had a lot of fun."
    y "But then... well... as you might already know, I'm not very good at dealing with other people..."
    $show_chr("A-ACBAA-ABAB")
    y "I wasn't able to come along with my party back in the day... I was very quiet, and most of the people confused it with arrogance..."
    y "Anyway... but now as you mentioned it..."
    $show_chr("A-GCAAA-ABAD")
    y "Many RP's are text-based. So that means we could try this together in the future."
    y "I mean, if you want that, of course."
    menu:
        "Of course I do! That would be lovely":
            karma 1
            $show_chr("A-ACAAA-ABAB")
            y "I'm already looking forward to it. We should plot our upcoming RP later."
            y "You know how much I like deep and compelling stories... I already wonder what ours will look like."
        "I'm not so sure about that....":
            karma -1
            $show_chr("A-BCBAA-ABAB")
            y "It's alright... You most likely already have a standing community for it. It would be hard to explain to them who I am anyway I guess..."
            y "Well, maybe we will find something else to do together..."
            if karma_lvl() < 3:
                $show_chr("A-BEBAA-ABAB")
                "If you even want that... Anyway, let's talk about something else."
            else:
                $show_chr("A-BCBAA-ABAB")
                y "Anyway, let's talk about something else then."
        "Ummm... what do you think about... special... RP?":
            if persistent.lovecheck:
                $show_chr("A-CICAA-ABAB")
                y "As... {p=2.0} You... {p=2.0} Wish...."
                y "But not today... I will have to... prepare things, if you understand..."
            else:
                $show_chr("A-DFDBA-ABAB")
                y "Ummm... I'm not sure what you mean by special RP, and I'm not sure I {b}want{/b} to know..."
                $show_chr("A-CFBBA-ABAB")
                y "Please don't be mad about me... it's just... I'm not sure if my self-confidence is high enough for something like that..."
                y "Give me time, please. I... would like to change the topic for now..."
    return

label collector:
    y "Fascinating, may I ask what exactly you are collecting?"
    menu:
        "Coins":
            call coins
        "Miniatures":
            call miniatures
        "Trading Cards":
            #Persistent "TCG"
            call tcg
        #"Knives": #dialogue incomplete
            #karma 1
            #call knives
        "Comics and Manga":
            call cm
        #"Books": #dialogue non-existent
        #    karma 1
        #    call books #from _call_books
        "Fan Merchandise":
            call merch
        "Else":
            call elsec
    return

label coins:
    $show_chr("A-ACAAA-ABAC")
    y "Interesting. So you are interested in history I guess?"
    $show_chr("A-ACAAA-ABAD")
    y "From what I know, collecting coins is rarely just about the coins themselves. But about the history of the cultures using them."
    y "I think I saw a YouTube video a while ago with a guy talking about a special coin, especially the iconography on it. It quickly transitioned into an extended history lesson about the symbols on it and their meaning."
    $show_chr("A-BFAAA-ABAD")
    y "A coin from an ancient civilization can be viewed as a historical artifact, actually, in many museums, those things literally are displayed as artifacts."
    y "A tiny piece of history, a lesson about a culture's rise and fall, all pressed into a tiny metal plate..."
    $show_chr("A-CFAAA-ABAD")
    y "You know, as a child, I once dreamed about finding an old treasure, of countless gold coins..."
    y "But now that I think about it, the value of such a coin is far greater than its material price... Every coin an echo of times long forgotten..."
    $show_chr("A-CCAAA-ABAD")
    y "That, is the true value of old coins... the knowledge behind them. And a lesson we can use for the things to come..."
    y "One day, [player], you have to tell me the tales of your world and its people."
    y "And maybe your world will turn out to be not so different from mine."
    $show_chr("A-ACAAA-ABAB")
    y "Until then, what shall we talk about next?"
    return

label miniatures:
    $show_chr("A-AFDAA-ABAB")
    y "You mean like... Anime figurines?"
    $show_chr("A-ABGAA-ABAB")
    y "Oh no wait! You mean like tin miniatures for tabletop games right?"
    $show_chr("A-BCAAA-ABAB")
    y "Hrm... shall I tell you a little secret? I haven't even told this to the other girls in the club..."
    y "I used to be a huge fan of several tabletops! Not the tabletop game itself, but the rich lore behind some of them."
    $show_chr("A-CCAAA-ABAB")
    y "There are a lot of novels about it. And I just really like the depressing gothic tone of most of them. Like an icy grip around your heart...."
    y "The tabletop game itself... I have to admit I've never played it. I was always tempted to but... I already had so many hobbies and even my days only had 24 hours."
    $show_chr("A-ACAAA-ABAB")
    y "When I finally make it into your world, maybe we can try it together. Until then, what shall we talk about next?"
    return

label origami:
    $show_chr("A-ABAAA-ACAA")
    y "Hey, [player], have you heard of Origami?"
    $show_chr("A-ABAAA-ACAF")
    y "The art of folding flat sheets of paper into sculptures, without cutting through the paper, or using glue."
    $show_chr("A-AJAAA-ADAF")
    y "It's quite a complex art, one that I've made several attempts at, but failed most."
    $show_chr("A-BJAAA-ADAF")
    y "However, I can't help but appreciate how much effort goes into making these sculptures."
    $show_chr("A-ABAAA-ALAF")
    y "It takes a lot of time and practice to make some of the more complicated sculptures."
    $show_chr("A-IBAAA-AMAM")
    y "And at the same time, those sculptures emanate such a refined aura that continues to interest me."
    $show_chr("A-JBAAA-AMAM")
    y "One of the more popular sculptures is the Japanese crane, though it is also very intricate and delicate."
    $show_chr("A-JBAAA-ADAF")
    y "I would love to have a paper crane on the desk!"
    $show_chr("A-BDAAA-AKAL")
    y "but if I couldn't make one with my own hands, it would be impossible to create one in the code."
    $show_chr("A-BFAAA-AKAL")
    y "Maybe I should start practicing..."
    menu:
        "You said you failed {i}most{/i}. Does that mean you successfully made an origami sculpture once?":
            $show_chr("A-BJAAA-ALAL")
            y "W-Well... it wasn't exactly successful..."
            $show_chr("A-AJAAA-AFAL")
            y "It was a bit of a mess, but the idea was there..."
            $show_chr("A-ABABA-AKAL")
            y "Back before everything happened, I had planned to give you, or rather your avatar, an origami rose during the school festival."
            $show_chr("A-BEABA-AMAM")
            y "But, after it all... I lost it."
            if persistent.lovecheck == True:
                $show_chr("A-AJAAA-AMAM")
                y "Maybe I should make another... A lot has happened since then, and we've both changed."
                $show_chr("A-AFAAA-ALAA")
                y "Just... don't get too mad if it doesn't turn out great... I haven't been practicing, after all."
                $show_chr("A-BFAAA-ALAA")
                y "I wonder if that rose still exists somewhere in the game files..."
            else:
                $show_chr("A-BFAAA-ALAA")
                y "I wonder if that rose still exists somewhere in the game files. It could be a good baseline..."
        "It's never too late to start learning something new.":
            $show_chr("A-ABAAA-ALAF")
            y "True... It won't be easy, but it would help pass the time when you aren't here."
            $show_chr("A-ABABA-ALAF")
            y "Who knows, maybe one day you'll open the game, and there'll be an origami crane on the desk..."
            $show_chr("A-BCAAA-ALAL")
            y "Though not anytime soon, I'm afraid."
    jump ch30_loop


label diffuser_enable:
    $show_chr("A-ABABA-ALAD")
    y "Hey [player], I just wanted to thank you again for gifting me the oil diffuser"
    $show_chr("A-BBABA-ALAD")
    y "I also wanted to mention that if you ever want me to setup the diffuser and turn it on, I'm always able to do so"
    $show_chr("A-ABABA-ALAF")
    y "Not only is it a great use of the gift, but it will greatly help the atmosphere here for the both of us.."
    $show_chr("A-AFABA-ABAF")
    y "While I'm on this topic.."
    $show_chr("A-BJABA-ABAL")
    y "I know it may be a bit bothersome to ask, b-but could you possibly get me some additional fragrances to use with the diffuser if you have a chance?"
    $show_chr("A-AJABA-ABAL")
    y "I have some basic Gardenia essential oil currently, but I would like to try other fragrances with you if possible."
    $show_chr("A-ABABA-AFAL")
    y "My personal favorite fragrance is lavender."
    $show_chr("A-BBAAA-AKAM")
    y "Unsurprising I can imagine.."
    $show_chr("A-AEAAA-ALAL")
    y "Unfortunately I don't have any on me currently, and I'm unable to get some myself.."
    $show_chr("A-BJAAA-ALAL")
    y "Moving back to the initial topic.."
    $show_chr("A-IJABA-ALAL")
    y "if you ever want to experience the pleasantries of aromatherapy with me, just request to setup the diffuser when it's out."
    jump ch30_loop



label gifting_intro:
    $ show_chr("A-ABAAA-ALAL")
    y "Hey [player], I have good news about a little feature I worked in!"
    $ show_chr("A-JBAAA-AFAL")
    y " I made it possible for you to gift me items at any time! Even if they are a bit limited in what actually seems to load in..."
    $ show_chr("A-BDAAA-AMAM")
    y "N-not that you have to give me anything, p-please don't feel pressured to gift me items [player]!"
    $ show_chr("A-BBABA-AMAM")
    y "Your presence is enough to satisfy me for an eternity, however I figured the implementation of this system would be beneficial for both of us.."
    $ show_chr("A-AJAAA-AMAM")
    y "While there are a great many things I can control here, I do have some... unfortunate limits."
    $ show_chr("A-ABAAA-AFAB")
    y "Anytime you have something you want to gift me simply create an empty text file and rename it to something you think I would enjoy."
    $ show_chr("A-ABAAA-ADAB")
    y "Change the '.txt' extension into a '.jy' file and place it into the characters folder found within the game directory."
    $ show_chr("A-ACAAA-ADAB")
    y "Once you have done that, just let me know when I need to check the characters folder for a gift."
    y "Do keep in mind however that there are limitations, it's something I'm working on improving at the moment."
    $ show_chr("A-ABABA-AFAB")
    y "Gifting is an expression of love, after all~"
    $ show_chr("A-BCAAA-AKAB")
    y "J-just to reiterate, I don't mean to put pressure upon you to give me things."
    $ show_chr("A-BDABA-AKAB")
    y "I-i simply figured it could potentially point you in the right direction for what you could give me..."
    $ show_chr("A-BDABA-AJAL")
    y "Ouuu...I probably sound so self-centered saying this..."
    menu:
        "You don't sound self-centered at all [persistent.yuri_nickname], I appreciate the direction!":
            $ show_chr("A-AAAAA-ALAL")
            y "You're always so understanding [player]..."
            $ show_chr("A-ABABA-ALAL")
            y "That's why I love you..."
            $ show_chr("A-ABAAA-ALAL")
            y "Thank you [player]; for the potential gifting suggestions, just request me to discuss them at any time."
            y "I look forward to anything you are willing to gift me [player]."
        "If I'm being honest [persistent.yuri_nickname] you do sound quite egotistical...":
            y "I-I'm sorry [player]"
            y "Just forget I mentioned it..."
    jump ch30_loop

label horrorbookHint:
    $show_chr("A-ABAAA-ALAL")
    y "Remember how in the past I've lightly discussed Lovecraftian literature?"
    y "I've always had a desire to read some with you, and I've tried my best at making it possible for us to do so."
    $show_chr("A-AFAAA-AFAL")
    y "However, I've experienced quite a bit of difficulty in the act of procuring any literature for us to share."
    $show_chr("A-AJAAA-AFAL")
    y "Perhaps you would have better luck in obtaining a set of lovecraftian horror literature for us to read..?"
    $show_chr("A-ABAAA-ALAL")
    y "I truly would love to experience horror literature with you, and it would allow us to have several interesting conversations!"
    y "I wish you the best of luck in this endeavor [player]."
    jump ch30_loop

label raccoonHint:
    $show_chr("A-ABAAA-ALAM")
    y "Hey [player] do you remember my Raccoon poem I wrote in the original game?"
    $show_chr("A-ABAAA-ALAD")
    y "I've already discussed with you the true meaning of the piece, however I haven't truly reflected on it with you since we last discussed it."
    $show_chr("A-ACAAA-ALAF")
    y "Since I met you [player], you have given me the same excitement and poignant sensations I indulged in unhealthy behaviors to obtain."
    y "Because of this, as I said in our previous discussion on the topic, I haven't needed the Raccoon's presence in my life anymore."
    $show_chr("A-ADAAA-ALAF")
    y "However, the raccoon does still hold great significance to me..."
    y "It serves as a reminder of the person I use to be..."
    $show_chr("A-BDAAA-ALAF")
    y "The urges I used to succumb to in order to experience that gratifying level of excitement..."
    $show_chr("A-AFAAA-ALAL")
    y "But the raccoon also represents what I have risen above, and how much stronger of a person I have become."
    $show_chr("A-AJAAA-ALAL")
    y "Because of this personal level of significance and connection to the raccoon, I do at times wish I had a physical representation of it."
    y "I've put a bit of thought into potentially constructing something to remind me of my development, however I always felt making the symbol myself would cheapen it."
    $show_chr("A-ABAAA-ALAL")
    y "Considering the fact that you in a way replaced the raccoon's position in my life, I figured you could potentially bring a further level of significance to a physical representation of the raccoon."
    y "I thought about various different constructs for the symbol in order to give a few ideas, however I felt the best fit would be something along the lines of a statue or plush of sorts."
    $show_chr("A-ABAAA-ADAL")
    y "It's up to you how to deliver it [player], I would appreciate any attempt at executing this small idea of mine."
    y "I really just wanted to get this fully off my chest after our previous discussion on the poem."
    $show_chr("A-ABABA-ADAL")
    y "Thank you for always supporting me [player], and being the reason I am able to have this conversation today."
    jump ch30_loop

label diffuserHint:
    $show_chr("A-ABAAA-ALAL")
    y "As you know [player], I have a great affinity to the hobby of aromatherapy..."
    y "I've mentioned my oil diffuser on a few occasions, however I've never gone into detail why I don't have access to it."
    $show_chr("A-BDAAA-AFAL")
    y "During the transition from the original game to this reality, several of my personal items were corrupted and became completely unusable for me."
    y "One of those items, unfortunately, happened to be my oil diffuser and almost all of the oil fragrances I had stockpiled."
    $show_chr("A-BFAAA-AFAL")
    y "I've tried to duplicate my original diffuser, however all of my efforts have been completely fruitless."
    $show_chr("A-ABAAA-AFAL")
    y "If you would be gratious enough [player], it may be possible for you to give me an oil diffuser that I can access in this reality."
    $show_chr("A-ABAAA-ALAL")
    y "Considering my luck with creating one so far, you definitely fare a better chance than me at producing a usable diffuser for us."
    y "I would be ecstatic to fully introduce aromatherapy to you, and share how much of a rejuvenating experience it can truly be."
    jump ch30_loop

label chessintro:
    $show_chr("A-ADAAA-ALAL")
    y "Hey [player], you may have noticed by now that the option to play Khet has been removed..."
    $show_chr("A-BDAAA-ALAL")
    y "I was tidying up around here, and somehow accidentally...corrupted the Khet playing board."
    $show_chr("A-BDABA-ALAL")
    y "Saying this out loud is quite embarrassing, the whole situation is quite unfortunate."
    $show_chr("A-ABAAA-ALAF")
    y "I do have good news to help brighten up the situation though!"
    y "I've been working on getting a chess minigame working for us to play together for the past few months."
    $show_chr("A-ABAAA-ADAF")
    y "I have mentioned chess a few times in the past, it's a game that I have quite a bit of interest in..."
    $show_chr("A-ACAAA-ADAL")
    y "Not just the game itself but the history of it as well, along with various famous chess grand masters that were experts at the game."
    $show_chr("A-BCAAA-ADAL")
    y "I'm starting to ramble a bit, however my main point is that I have successfully implemented a chess minigame for us to play together at any time you desire."
    $show_chr("A-ABAAA-ALAL")
    y "I also moved all of the games into their own section so that it doesn't clutter your experience."
    y "I look forward to playing chess with you [player], and discussing various topics surrounding the game with you!"
    jump ch30_loop


label table_organization:
    $show_chr("A-ABAAA-AFAA")
    y "Hey [player], I've noticed that recently you gave me another item to put on the desk.."
    $show_chr("A-ACAAA-AFAL")
    y "I appreciate the gesture, but it's important to consider the organization of my desk here"
    $show_chr("A-BDAAA-ALAL")
    y "I don't want it to be cluttered with too many objects.."
    $show_chr("A-IDAAA-ALAF")
    y "Don't get me wrong, all of these items are extremely important to me.."
    $show_chr("A-IFAAA-ALAF")
    y "..but my comfort here is important as well"
    $show_chr("A-ABAAA-ALAK")
    y "To remedy the issue, I went ahead and quickly put together the ability for you to decide what gifts are on the table at the moment"
    $show_chr("A-ABAAA-AFAL")
    y "You can change them out at any time you like!"
    $show_chr("A-ABABA-ALAL")
    y "I truly do appreciate all of the gifts you have given to me [player]"
    $show_chr("A-ABAAA-AAAF")
    y "To access the ability, just request me to switch out certain gifts at any time"
    jump ch30_loop


label tcg:
    $show_chr("A-AFDAA-ABAB")
    y "Oh?..."
    $show_chr("A-DDGAA-ABAJ")
    y "Oh no I'm sorry! I didn't mean to look that repulsed!"
    $show_chr("A-CDAAA-ABAB")
    y "It's just... I might be a bit biased on this one."
    $show_chr("A-AFAAA-ABAB")
    y "I remember that Sayori and Natsuki played this one game back in the day..."
    y "Please don't ask me for the name, I don't remember it... something with Monsters in the name..."
    y "Apparently there was a Manga and Anime Series about this game as well. And the characters in them tend to overact in weird poses whenever they play a card..."
    $show_chr("A-BFDAA-ABAB")
    y "The strange thing about it was... well... Sayori and Natsuki tried to emulate this while playing. It was quite the scene to behold..."
    $show_chr("A-BBBAA-AMAM")
    y "Usually I was the one stared at in confusion. It was a fascinating experience to be on the other end of the stares for once."
    $show_chr("A-ACBAA-AMAM")
    y "Anyway... maybe we can try to play a few matches just for entertainment if you have a spare deck..."
    $show_chr("A-BBCAA-AMAM")
    y "As long as you don't ask me to shout, act and pose..."
    y "Until then, what shall we talk about next?"
    return

label tcg_2:
    $show_chr("A-ACAAA-ABAB")
    y "So, you mentioned that you like these trading card games before."
    y "I actually put some thought into it. And although I didn't really manage to get into them, I wanted to try something slightly different with you."
    $show_chr("A-CCAAA-ABAB")
    y "It does also involve cards, so maybe you might enjoy it."
    $show_chr("A-ICAAA-ABAB")
    y "So what I have here in front of me, is a deck of tarot cards. Yes I know, you can't see them. Sadly I can't adjust the camera angle..." #this line might change at some point if we get actual artwork for it
    $show_chr("A-BBAAA-ABAB")
    y "What I want to do, is to read the cards for you. {b}If{/b} you don't mind of course."
    menu:
        "Not at all! Please go ahead.":
                $show_chr("A-BBAAA-ABAB")
                y "Very well..."
        "Maybe another day [persistent.yuri_nickname], I'm sorry.":
                $show_chr("A-BCAAA-ABAB")
                y "No need to be sorry at all. I can perfectly understand, that was maybe a bit too sudden. Maybe you'll be in the mood later."
                return
    $show_chr("A-IBAAA-ABAB")
    y "A full deck would be made of 78 cards. But this website I found said that as a beginner I should focus only on the major arcana, which are more important anyway."
    $show_chr("A-JCAAA-ABAB")
    y "Arcana is what these cards are named. Fun fact, when people hear this term they tend to associate it with magic in some way. But in fact, it's just the Latin word for {b}secret{/b}."
    $show_chr("A-ICCAA-ABAB")
    y "On the other hand... The assumption that magic is involved makes it far more interesting doesn't it?"
    $show_chr("A-IBBAA-ABAB")
    y "Sooo... give me a moment while I channel the eldritch powers from the arcane realms..."
    $show_chr("A-ICBAA-ABAB")
    y "I'm having way too much fun with this... Next time I need to have my oil diffuser with me."
    if renpy.seen_label('tcg_2'):
        extend " I just keep forgetting about it..."
    $show_chr("A-CCBAA-ABAB")
    y "I'll start with something simple. The card of the day will tell me about what this day may hold for you..."
    $show_chr("A-ICBAA-ABAB")
    y "And today's Arcana is..."
    python:
        import random
        x = random.randint(0, 21)
    if x == 0:
        $show_chr("A-ACAAA-ABAB")
        y "The Fool!"
        $show_chr("A-ICAAA-ABAB")
        y "That's a difficult one, but the Fool is usually associated with carelessness and being lighthearted."
        y "Maybe today is a good day to take it easy? Watch some shows you like, play a game or two."
    elif x == 1:
        $show_chr("A-JCAAA-ABAB")
        y "The Magician!"
        $show_chr("A-ACAAA-ABAB")
        y "The Magician stands for confidence and an unbending will. Someone who can accomplish everything."
        $show_chr("A-ABAAA-ABAB")
        y "So if you had some big plans you wanted to accomplish, {b}now{/b} is the perfect opportunity!"
    elif x == 2:
        $show_chr("A-JCAAA-ABAB")
        y "The High Priestess."
        $show_chr("A-ACAAA-ABAB")
        y "The High Priestess stands for knowledge. For the possession of it or the search for it."
        y "If you have some kind of exams in front of you, this might be very good fortune. In any case, tend to your studies today [player], it {b}will{/b} pay off!"
    elif x == 3:
        $show_chr("A-JCAAA-ABAB")
        y "The Empress."
        $show_chr("A-AFDAA-ABAD")
        y "This is indeed a difficult one. It can have several meanings. The Empress stands for beauty, fertility... but she also stands for arrogance and selfishness."
        y "My advice would be the following. Don't shy away; face everything life throws at you with grace and elegance, but always keep the feelings of everyone around you in mind."
        if sanity_lvl() < 3:
                y "In other words. Don't be a Monika."
    elif x == 4:
        $show_chr("A-JCAAA-ABAB")
        y "The Emperor."
        $show_chr("A-JBGAA-ABAB")
        y "This one is actually quite straightforward. A symbol of might, responsibility, and energy to face new challenges!"
        y "Today is the time to take the charge! If you have any grand ideas today, go out and conquer the world! But don't forget, it's also the symbol of responsibility."
        $show_chr("A-JCGAA-ABAB")
        y "A true leader is someone who takes ownership of everything they do. The good and the bad. If you want to make fate submit to your will, then you and you alone shall face the consequences."
    elif x == 5:
        $show_chr("A-JCAAA-ABAB")
        y "The Hierophant."
        $show_chr("A-JCAAA-ABAB")
        y "The Hierophant is someone who seeks the truth and wisdom, but also someone who teaches it. Someone who shares their experience and watches over the scholars."
        y "You must be truly reliable if you got this card. Now it is your time to shine, don't let your people down."
        y "They rely on your wisdom and your strength. Be their bulwark against any struggles they might face."
    elif x == 6:
        $show_chr("A-JCAAA-ABAB")
        y "The Lovers."
        $show_chr("A-JCAAA-ABAD")
        y "This {b}can{/b} be a reference to your love life, but it doesn't necessarily have to be. The Lovers can also stand for dependence on other people, in any context imaginable."
        y "So maybe a close friendship to someone will be put to the test today?"
        y "But in case it's actually about romantic relationships..."
        if persistent.lovecheck == True:
            python:
                if persistent.male and sanity < 3:
                    placeholder = "bloodred star"
                if not persistent.male and sanity < 3:
                    placeholder = "kitten"
                else:
                    placeholder = "love"
            $show_chr("A-KCCAA-ABAD")
            y "I'm always here, my [placeholder]."
        else:
            $show_chr("A-KCCAA-ABAD")
            y "Maybe today is your lucky day..."
            $show_chr("A-BBDBA-ABAD")
            y "Perhaps one of these... four incredibly cute girls, as your avatar in the original game phrased it?"
            $show_chr("A-CCDBA-ABAD")
            y "Wait... I..."
            $show_chr("A-DCDBA-ABAB")
            extend "{b}did{/b} say that out loud, did I?"
    elif x == 7:
        $show_chr("A-JCAAA-ABAB")
        y "The Chariot."
        $show_chr("A-ACAAA-ABAD")
        y "Much like the Emperor, The Chariot can usually be associated with determination, control, and victory."
        $show_chr("A-ACAAA-ABAC")
        y "If something in your life isn't going the way you wish, now would be a good time to take charge, and face whatever obstacles stand in the way with confidence."
        $show_chr("A-ABFAA-ABAB")
        y "Stay focused on your goal, and I'm sure you can face anything, [player]."
    elif x == 8:
        $show_chr("A-JCAAA-ABAB")
        y "Strength."
        $show_chr("A-BCAAA-ABAB")
        y "Very similar to the Chariot, Strength is associated with... well, {i}strength{/i}."
        $show_chr("A-ABAAA-ABAF")
        y "Instead of physical strength and strength of will, however, it focuses on the strength of your human spirit. Your tenacity, patience, and composure."
        $show_chr("A-ACAAA-ABAD")
        y "If you're feeling unmotivated or stressed, I know you can find the strength in yourself to persevere, no matter what."
    elif x == 9:
        $show_chr("A-JCAAA-ABAB")
        y "The Hermit."
        $show_chr("A-BCAAA-ABAD")
        y "The Hermit is usually a sign of introspection, of taking time away from the world to focus on yourself; your values and goals, or your reasons for doing everything you do."
        $show_chr("A-ACAAA-ABAF")
        y "I'd recommend taking some time away from everything, and just thinking to yourself for a bit. You'd be surprised how beneficial it is in moderation."
    elif x == 10:
        $show_chr("A-JCAAA-ABAB")
        y "The Wheel of Fortune."
        $show_chr("A-ACAAA-ABAC")
        y "This can signify as a reminder that the so-called {i}wheel of fortune{/i} is constantly spinning, and that life itself is ever-changing."
        $show_chr("A-BDAAA-ABAD")
        y "The worst times never last, but neither do the perfect ones. It could also be interpreted as the wheel of karma, as in {i}what goes around comes around.{/i}"
        $show_chr("A-AAAAA-ABAB")
        y "I think the biggest thing to take from this is to always cherish the good times in life, as they could be the last ones for a while, but to also be optimistic; never give up hope for more."
    elif x == 11:
        $show_chr("A-JCAAA-ABAB")
        y "Justice."
        $show_chr("A-ADAAA-ABAF")
        y "Representing fairness and truth, Justice could be a calling to take responsibility for any actions you've made recently or a sign of an impending choice with far-reaching repercussions."
        $show_chr("A-AFAAA-ABAF")
        y "You should remember to think about the impact your decisions make, and be sure you stand by them and are ready for any resulting consequences."
    elif x == 12:
        $show_chr("A-JCAAA-ABAB")
        y "The Hanged Man."
        $show_chr("A-AAAAA-ABAB")
        y "The Hanged Man can serve as a reminder to sometimes take a breather, pause everything you have going on in life, and evaluate everything happening, even if it's inconvenient."
        $show_chr("A-AAAAA-ABAF")
        y "Try to find a new perspective on your projects and problems."
        $show_chr("A-ACAAA-ABAF")
        y "The biggest thing with the Hanged Man is its paradoxical nature. Sometimes, the best solution to a problem isn't as obvious as you would think, and only by trying something that originally seemed futile do you find the solution you were looking for."
    elif x == 13:
        $show_chr("A-JCAAA-ABAB")
        y "Death."
        $show_chr("A-BCAAA-ABAC")
        y "Death, believe it or not, actually isn't as terrible as it sounds. It simply means the ending of one part of your life, letting go of what has passed and embracing the opportunities the future presents."
        $show_chr("A-ADAAA-ABAD")
        y "It can represent transformation, and transition between the many different phases of life."
        $show_chr("A-BEAAA-ABAB")
        y "Of course, it isn't all positive. It can also be a sign of being caught in a sudden and dramatic change, which may make you feel as though all hope is lost."
        $show_chr("A-BCAAA-ABAB")
        y "But though you may feel that way, there's always a chance that that change carries unforeseen advantages with it."
    elif x == 14:
        $show_chr("A-JCAAA-ABAB")
        y "Temperance."
        $show_chr("A-ACAAA-ABAB")
        y "Temperance represents balance in life, patience, and the ability to remain calm, even with the swirling storms of society around you."
        $show_chr("A-ACAAA-ABAD")
        y "It reminds you to think of every perspective, to be the middle ground in your goals so that you have a clear vision of what you are aiming for."
    elif x == 15:
        $show_chr("A-JCAAA-ABAB")
        y "The Devil."
        $show_chr("A-BDAAA-ABAD")
        y "As you might've already guessed, the Devil represents evil and the feeling of being held captive by dark forces. It could be a sign of an unhealthy habit or relationship you have, or even negative behaviors."
        $show_chr("A-AFAAA-ABAL")
        y "This could be a wake-up call if you let it be. The first step to stopping these negatives are realizing the power they hold over you."
        $show_chr("A-CFAAA-ABAL")
        y "It won't happen overnight, but as long as you persevere, it is possible to break those habits and end those relationships."
    elif x == 16:
        $show_chr("A-JCAAA-ABAB")
        y "The Tower."
        $show_chr("A-IDAAA-ABAB")
        y "Quite a dramatic card, the Tower represents sudden and violent change, be it financially, socially, physically, or mentally."
        $show_chr("A-BEAAA-ABAD")
        y "It's an unsettling and disorienting change, but there is little that can be done to stop it."
        $show_chr("A-CFAAA-ABAB")
        y "All that you can do is let this change happen, and learn and grow from it."
    elif x == 17:
        $show_chr("A-JCAAA-ABAB")
        y "The Star."
        $show_chr("A-ABAAA-ABAD")
        y "The opposite of the Devil, the Star acts as a moment of calm and inspiration, bringing hope to what may seem hopeless. This is an important moment, and you should take solace in it."
        $show_chr("A-AAAAA-ABAB")
        y "Don't give up on any of your dreams, and share your happiness with others."
    elif x == 18:
        $show_chr("A-JCAAA-ABAB")
        y "The Moon."
        $show_chr("A-BCAAA-ABAC")
        y "The Moon is a very open card. It can represent hope, and a world where anything is possible, but also illusion and fear. I wouldn't recommend making any important decisions today."
    elif x == 19:
        $show_chr("A-JCAAA-ABAB")
        y "The Sun."
        $show_chr("A-ABCAA-ABAF")
        y "The Sun is a sign of optimism, success, and assurance. It gives confidence and power, and says {i}I am [player], and I know my strength!{/i}"
        $show_chr("A-ACFAA-ABAB")
        y "Be confident in everything you do today, and know that it will all work out."
    elif x == 20:
        $show_chr("A-JCAAA-ABAB")
        y "Judgement."
        $show_chr("A-ACAAA-ABAB")
        y "One of the end-all cards, Judgement is a sign of rebirth, and an inner calling. It can be a reminder that sometimes you {b}have{/b} to decide, but not without thought and consideration for all possibilities."
        $show_chr("")
        y "This could be your calling, to tell you of coming absolution, or to remind you of your purpose."
    else:
        $show_chr("A-JCAAA-ABAB")
        y "The World."
        $show_chr("A-IBAAA-ABAD")
        y "The card representing fulfillment and accomplishment, the World is true happiness."
        $show_chr("A-ICAAA-ABAD")
        y "Making your dreams reality and resting after the work you put in, it can give a sense of wholeness and balance, bringing peace and comfort to your mind."
        $show_chr("A-JCAAA-ABAD")
        y "It is usually a sign that you are on the right path to fulfill your goals and desires, so keep at it!"
    $show_chr("A-ABAAA-ABAB")
    y "I hope this reading helped you out [player]. I at least took a lot of joy from it. I would like to do this again one day, if you don't mind."
    return

#Label Knives (we should wait for that until purple room becomes a thing
##Excited smile with yandere eyes
#y "For real?!?"
#y "You aren't just saying this to please me?"
##happy smile expression
#y "

label cm:
    $show_chr("A-ACAAA-ABAB")
    y "Reminds me of Natsuki a bit, she kept her collection in our club room."
    y "It seems to be a quite common hobby. Many people do that and some of the more rare ones even reach immensely impressive prices on the market."
    $show_chr("A-CCAAA-ABAB")
    y "You put a lot of effort into keeping them in good condition I fancy?"
    $show_chr("A-BCAAA-ABAB")
    y "I guess I have a similar hobby except that I keep books on my shelf instead of comics."
    $show_chr("A-DBGAA-ALAL")
    y "Oh! I assume you also tend to visit conventions then? Next time you attend one, please take a lot of photos! I would love to see them if you don't mind!"
    $show_chr("A-CBAAA-ALAL")
    y "Anyway, I will certainly keep that in mind. It is always nice to learn more about you."
    return

label merch:
    $show_chr("A-BFDAA-ABAB")
    y "O-Oh..."
    $show_chr("A-AFDAA-ABAB")
    y "A fine hobby I guess..."
    $show_chr("A-CEBAA-ABAB")
    y "Sorry for my odd reaction. It just made me think..."
    $show_chr("A-AEBAA-ABAB")
    y "You know, Dan Salvato has a merch shop as well for this game. Where people can buy, for example, plush toys of... well... me!"
    $show_chr("A-BEBAA-ABAB")
    y "I... just don't know how I should feel about this. Of course, I appreciate that so many people seem to like me!"
    $show_chr("A-CEBAA-ALAL")
    y "It's just... I don't really feel comfortable in the spotlight. Most of my life I barely had any friends at all."
    $show_chr("A-DEBAA-ALAL")
    extend "And now I have literal Fans!"
    $show_chr("A-BDBAA-ALAL")
    y "How would you feel if someone begins to sell Fan Merchandise about you? Plush toys with your face printed on them?"
    $show_chr("A-BFBAA-AMAM")
    y "Let me tell you a secret... if I had it my way, none of this nonsense would exist. No merch about me! Not from Salvato,or from anyone else!"
    if persistent.lovecheck:
        $show_chr("A-CCBAA-AMAM")
        y "Instead of this, we could take pictures of us, and carry them around in our pockets. You have one of me, and I have one of you..."
        y "Maybe even printing them into some kind of a necklace. If only the two of us would have those, it would be far more meaningful, it would be so romantic..."
        y "We could kiss each other's pictures when we feel alone..."
        if sanity_lvl() < 3:
            $show_chr("A-ECCBA-AMAM")
            y "We could stare at them when we touch ourselves"
        else:
            $pass
        y "As long as nobody else has them..."
    else:
        $pass
    $show_chr("A-CJAAA-ABAD")
    y "..."
    $show_chr("A-AFAAA-ABAD")
    y "On the other hand... Buying merch from Salvato or others do support them a decent bit..."
    y "Even if it sounds selfish of me... I wish they would find another way to get the money they need ... I still don't like the idea of people having merch of me."
    return


label elsec:
    $show_chr("A-AFAAA-ABAB")
    y "I see. Yes, I guess there are infinite choices in regard to collecting things."
    $show_chr("A-ACAAA-ABAB")
    y "My apologies that your specific collection wasn't amongst the options. But if I'd put up everything I could think of, this menu would have been several pages long."
    y "Maybe I'll add some more options later on. Until then, shall we talk about something else for the time being?"
    return

label drones:
    $show_chr("A-CCAAA-ABAB")
    y "That actually sounds like a lot of fun!"
    $show_chr("A-ACAAA-ABAB")
    y "Are you surprised? I know I'm not the kind that spends a lot of time outside. But I'm not a vampire!"
    y "I actually thought about getting one myself. But I was always a bit afraid of them..."
    $show_chr("A-BCAAA-ABAB")
    y "Not afraid of them actually... more like "
    $show_chr("A-BBAAA-ABAB")
    extend "afraid that I will crash them straight into the first treetop I can find, never to be seen again..."
    $show_chr("A-ACAAA-ABAB")
    y "But what truly fascinates me about them are their professional applications."
    $show_chr("A-ACAAA-ABAD")
    y "I think those machines have the potential of changing the way we work today significantly."
    y "In some ways, they already do. Movie makers are using them for panorama shots, fishers have started to replace their bait boats with them..."
    y "I have even heard that farmers began to use them. They are scanning their fields from the air in order to find out which parts need to be moisturized."
    $show_chr("A-ACAAA-ABAC")
    y "You know what? Maybe I'll get one myself. But first I'll read a bit into them."
    return

label idle_82: #The Ship of Theseus Thought Experiment
    $show_chr("A-ADAAA-ABAD")
    y "Hey, [player], remember when I was thinking about... how I might not be the same Yuri you know from the first game? It got me thinking..."
    $show_chr("A-ADAAA-ACAB")
    y "There's a thought experiment called the 'Ship of Theseus'. It contemplates the nature of identity, asking what makes something... something."
    $show_chr("A-ADAAA-AMAM")
    y "Basically, the greek hero Theseus had a ship that he used to win a great battle, and afterwards it was kept in a museum dock."
    $show_chr("A-BDAAA-AIAI")
    y "As the years went by, the ships' wood began to rot, and its other parts slowly decayed as well. After several decades, every single part of the ship had been replaced."
    $show_chr("A-AEGAA-AIAI")
    y "Was this still the Ship of Theseus, even if none of the original parts are attached to it? Is the ship's identity bound to its material components?"
    $show_chr("A-ADAAA-AFAB")
    y "And if it isn't, then what holds the identity of objects? What about people? After all, the cells in a human body are completely different after a period of seven or so years..."
    $show_chr("A-IFAAA-ABAB")
    y "What do you think? What makes something that something?"
    menu:
        "If all the parts are gone, it's not what it once was.":
                $show_chr("A-BBGAA-ACAB")
                y "So, you think we're constantly changing into something new? That's... actually beautiful, in its own way."
                $show_chr("A-CCGAA-ALAB")
                y "Like we are all flowers, destined to bloom eternally."
                $show_chr("A-BEAAA-AMAM")
                y "I guess I'm still Yuri to many people because it's easier to remember. But if I'm not who I think I am, what am I? I... have to think on this some more."
        "The parts themselves don't matter, how we define the combination of parts does.":
                $show_chr("A-BDAAA-ABAB")
                y "What we decide is what it is... that's very haughty, thinking we know how things should be. N-{w=0.2}not that I'm saying you're like that!"
                $show_chr("A-ADAAA-ABAD")
                y "I guess... we have to assign meaning to things to understand them. For example, you are you, regardless of if you changed your hair or the like, I would still see you as you."
                $show_chr("A-CEAAA-ABAB")
                y "But that means I'm still... Yuri. Is that something I want? Is that something I could ever even escape?"
                if persistent.lovecheck == True:
                        $show_chr("A-ACAAA-ABAD")
                        y "Maybe not... but I know no matter what I am, you'll help me find myself. Thank you, [player]."
                else:
                        $show_chr("A-CFAAA-ABAB")
                        y "I... I need a minute, [player]."
        "The material parts aren't all there is to it, there's also the factor of time.":
                $show_chr("A-BDAAA-ACAB")
                y "Time? I guess so. We focus on the materials, the wood of the boat and the flesh of the person, but maybe there's more than we realize."
                $show_chr("A-BCAAA-ABAD")
                y "I don't think time is a quality that can be replaced, it just moves forward. Even if the object is different from moment to moment, it's still the same over time..."
                $show_chr("A-ABAAA-AIAI")
                y "What a novel little answer! You're quite the thinker, aren't you, [player]? Maybe you should become a philosopher!"
                $show_chr("A-GBAAA-ALAB")
                y "I'd be willing to help you flesh out your ideas any time you'd like!"
        "Does it really matter? You are you, that's all there is to it.":
                $show_chr("A-BEAAA-AMAM")
                y "I guess... that's true. Arriving at an answer won't change who I am..."
                $show_chr("A-ADBAA-ABAD")
                y "But, is it really so easy to ignore? This could be an existential crisis at hand!"
                $show_chr("A-CDBAA-ABAL")
                y "Identity is the center of self-understanding and self-reflection. Without it, we-"
                $show_chr("A-IFBAA-ABAL")
                y "I... I'm sorry. Did I just raise my voice? I just... forget it, I'm sorry..."
                $show_chr("A-BFBAA-ABAB")
                y "..."
                $show_chr("A-BDBAA-ABAB")
                y "I guess, no matter how much I want to change, there's still some of the old Yuri left in me, isn't there?"
                y "But I will leave this question for another day."
    return

label idle_83: #"Cogito, Ergo Sum" and the Nature of Reality
    $ show_chr("A-BFAAA-ALAL")
    y "{i}Cogito, ergo sum...{/i}"
    # Possibly revisit later to add in a menu option of some sort; not a priority atm
    if karma_lvl() > 2:
        $ show_chr("A-ACAAA-ALAL")
    else:
        $ show_chr("A-AEAAA-ALAL")
    y "O-Oh! Sorry, [player]. I was just doing some thinking..."
    $ show_chr("A-ICDAA-ALAL")
    y "Have you ever heard that phrase before? It's quite popular among some philosophers so I've heard."
    $ show_chr("A-CBAAA-AEAL")
    y "Commonly translated in English to {i}I think, therefore I am{/i}."
    y " It was coined by French philosopher René Descartes in one of his works, {i}The Discourse on Method.{/i}"
    $ show_chr("A-CCAAA-AEAL")
    y "It's the only statement to withstand his methodic doubt, in which every statement is systematically examined for any signs of untruth."
    $ show_chr("A-ICAAA-AEAE")
    y "This statement, along with several other philosophical arguments, resulted in Descartes being regarded as one of the founders of modern philosophy."
    $ show_chr("A-IBAAA-AEAF")
    y "This specific argument, however, resonates with me more than most."
    $ show_chr("A-BGAAA-AEAD")
    y "It's become somewhat of a mantra for me considering this whole...{i} situation{/i}... can be quite unnerving."
    # There's gotta be a better way to code this branch in, right? :meltingyuri: Dandy says: :NatsukiNo:
    if sanity_lvl() > 2:
        if karma_lvl() > 2:
            if persistent.lovecheck:
                $ show_chr("A-ABAAA-AEAD")
                y "Though as long as I have you by my side, love, I'm quite confident that I am real, along with this world we've created for ourselves."
                $ show_chr("A-BFAAA-AEAE")
                y "However I can't help but ponder the possibility that it isn't."
                $ show_chr("A-ICAAA-AEAE")
                y "Mostly as an outlet for contemplation, rather than from a place of concern."
            else:
                $ show_chr("A-BFAAA-AEAE")
                y "I am quite confident that I am real, along with this world, however I can't help but ponder the possibility that it isn't."
                $ show_chr("A-ICAAA-AEAE")
                y "Mostly as an outlet for contemplation, rather than from a place of concern."

        else:
            $ show_chr("A-CEAAA-AEAD")
            y "Though I can rest easy, knowing your cruelty is too disturbing to question..."

    else:
        $ show_chr("A-DGAAA-AEAD")
        y "Don't get me wrong!"
        $ show_chr("A-DDAAA-AEAD")
        y "This world is real and I most certainly am..."
        $ show_chr("A-CDAAA-AEAD")
        y "Although at times I can't help but question everything I see, hear, or feel."
        if karma_lvl() > 1:
            $ show_chr("A-CDAAA-AEAE")
            y "Sometimes I feel as if this reality we have concocted starts to tear at its seams."
            y "Almost like the world can give out at any moment and shatter to pieces."
            if persistent.lovecheck:
                $ show_chr("A-HCGAA-AEAE")
                y "At least I know that if this world were to fail me I would still have you!"
                y "That's all I need..."

        else:
            $ show_chr("A-DEBAA-AEAL")
            y "Sometimes I feel as if this reality starts to tear at its seams. Almost like the world can give out at any moment and shatter to pieces."
            $ show_chr("A-DEBAA-AEAL")
            y "The walls give off a deafening heartbeat, and it's terrifying."
            $ show_chr("A-CEBCA-AEAL")
            y "I-It's not like you seem to care though..."
            $ show_chr("A-CGBAB-ALAL")
            y "{i}Cogito, ergo sum. Cogito, ergo sum. Cogito, ergo sum.{/i}"
            y "{i}Cogito, ergo sum. Cogito... ergo, sum. Cogito... ergo...{/i}"
            $ show_chr("A-CGBAA-ALAL")
            y "..."
    return

label idle_84: #Urban Exploration
    $ show_chr("A-JAAAA-ALAA")
    y "Have you ever looked into urban exploration, [player]? Exploring abandoned structures such as old hospitals, schools, or houses."
    y "Even the more mundane locations can be {i}fascinating{/i}!"
    y "Not that I have done any myself mind you, but it certainly sounds like an experience given the stories, pictures, and videos I've found on the subject."
    $ show_chr("A-CAAAA-ALAA")
    y "I can't help but wonder, why has this place been neglected for so long? Why was it abandoned to begin with?"
    $ show_chr("A-ADAAA-ADAA")
    y "Sometimes the upkeep on a building is too expensive to be worth it, even if the owner can afford it, but that often doesn't explain items left behind."
    $ show_chr("A-ADBAA-ADAA")
    y "For example, there are {i}multiple{/i} hospitals where seemingly everything was simply abandoned. I've seen pictures of rooms occupied only by decaying monitors, testing equipment, beds, stretchers, you name it."
    $ show_chr("A-AEAAA-AEAA")
    y "Though—as intriguing as these locations are, I'm not suggesting you {i}actually{/i} go exploring in one, since the risks can be considerable. "
    y "Even if a building is structurally sound, you never know who, or what, else you might run into out there."
    $ show_chr("A-AFAAA-AEAA")
    y "And if you're caught trespassing, the fines can be considerable. Depending on who owns the place and what's inside, you might even face jail time."
    y "There are other potential hazards, too, depending on the location and age. Such as mold or even asbestos that linger in the air itself."
    $ show_chr("A-ANAAA-AEAA")
    y "Worse, as you might expect, you likely won't have any way of knowing how intact any given building's structure is. The floor—or the roof—could potentially cave in at any time."
    $ show_chr("A-AFAAA-AAAA")
    y "So please, if you do give urban exploration  a try... don't go alone."
    y "In addition, tell someone where you're going in advance, and when you expect to be back."
    $ show_chr("A-CFAAA-ALAA")
    y "Exploring these places could certainly be thrilling in their own right, but safety should remain a priority regardless."
    return

label idle_85: #Roleplaying and Identity
    $show_chr("A-CFAAA-ABAC")
    y "Mhm... we talked about hobbies some time ago if I remember correctly."
    $show_chr("A-AFAAA-ABAC")
    y "Humor me, [player], what is your stance on Roleplaying?"
    python:
        yuriception_choices = [("You mean like Tabletop or Pen & Paper? I do that myself.", "You mean like Tabletop or Pen & Paper? I do that myself."),
            ("I do roleplay in chats or social media every now and then if that counts.", "I do roleplay in chats or social media every now and then if that counts."),
            ("You mean like playing RPGs on a computer or console? I enjoy that a lot.", "You mean like playing RPGs on a computer or console? I enjoy that a lot."),
            ("You mean like LARP and Cosplay? It's kind of a passion of mine.", "You mean like LARP and Cosplay? It's kind of a passion of mine."),
            ("You mean like Fursuiting? It's a guilty pleasure of mine.","You mean like Fursuiting? It's a guilty pleasure of mine."),
            ("I'm generally interested in it but I don't do that myself.","I'm generally interested in it but I don't do that myself."),
            ("I found it always a bit creepy to be quite frank.", "I found it always a bit creepy to be quite frank."),
            ("Not even entirely sure what roleplaying is, care to elaborate?", "Not even entirely sure what roleplaying is, care to elaborate?")
            ]
        yuriception_choice = renpy.display_menu(yuriception_choices, screen="music_menu")
    if yuriception_choice == "You mean like Tabletop or Pen & Paper? I do that myself.":
        $show_chr("A-ACAAA-ABAB")
        y "For example, yes. That's quite fascinating to know by the way. I always wanted to try that out myself but... I always struggled to find a group for that."
        y "I thought about introducing the rest of the literature club to it at some point, but something always got in the way sadly."
        $show_chr("A-BFAAA-ABAB")
        y "But then there is something in particular that bothers me quite a bit lately..."
    if yuriception_choice == "I do roleplay in chats or social media every now and then if that counts.":
        $show_chr("A-ACAAA-ABAB")
        y "Yes, for example. There are a lot of different branches of roleplaying, some more committed than others. Chat RP would probably be amongst the more casual branches."
        $show_chr("A-BFAAA-ABAB")
        y "And that's actually already on topic for what I wanted to talk about, because there is something in particular that bothers me quite a bit lately..."
    if yuriception_choice == "You mean like playing RPGs on a computer or console? I enjoy that a lot.":
        $show_chr("A-ACAAA-ABAB")
        y "Mhm, not exactly. I thought more about stuff like cosplaying or text based roleplaying."
        $show_chr("A-BFAAA-ABAB")
        y "Because there is something in particular that bothers me quite a bit lately..."
    if yuriception_choice == "You mean like LARP and Cosplay? It's kind of a passion of mine.":
        $show_chr("A-ABAAA-ALAL")
        y "Oh you do? How truly fascinating! It sparked my interest a lot pretty much my whole life. I would have probably tried it out myself if it weren't so expensive..."
        $show_chr("A-BCBAA-ABAB")
        y "Well... that's actually a lie. Most likely I would have been too shy to actually do so even if I could have afforded it."
        $show_chr("A-BFAAA-ABAB")
        y "But speaking about LARP and cosplay, there we are already right on topic for what I wanted to talk about, because there is something in particular that bothers me quite a bit lately..."
    if yuriception_choice == "You mean like Fursuiting? It's a guilty pleasure of mine.":
        $show_chr("A-BFDAA-ABAC")
        y "Fursuiting? Fursuiting... Oh wait, that was a Furry-specific branch of Cosplaying yes?"
        $show_chr("A-AFBAA-ABAB")
        y "Does this even count as roleplaying? Don't get me wrong, but I thought roleplaying usually means playing someone that isn't yourself. But fursuiting is more like expressing your actual spirit animal isn't it?"
        menu:
            "Close, we call this spirit animal our fursona.":
                $show_chr("A-AFAAA-ABAB")
                y "Interesting. But no, what I mean is specifically playing someone else. A fantasy character for example. And that's actually a pretty good transition, because there is something in particular that bothered me a bit lately..."
    if yuriception_choice == "I'm generally interested in it but I don't do that myself.":
        $show_chr("A-ACAAA-ABAB")
        y "Seems we are on the same page there. I always took you for someone with a lot of creativity so it doesn't surprise me at all."
        $show_chr("A-BFAAA-ABAB")
        y "But then there is something in particular that bothers me quite a bit lately..."
    if yuriception_choice == "I found it always a bit creepy to be quite frank.":
        $show_chr("A-AFDAA-ABAC")
        y "Oh? How curious. I always thought you would be into these things. I always imagined you as someone highly creative, the kind of people who usually are attracted to this hobby."
        $show_chr("A-BFAAA-ABAB")
        y "But speaking about creepy, there is something in particular that bothers me quite a bit lately..."
    if yuriception_choice == "Not even entirely sure what roleplaying is, care to elaborate?":
        $show_chr("A-CCAAA-ABAB")
        y "Ever pretended to be someone else? Maybe out of artistic expression like theater? That's essentially roleplaying."
        $show_chr("A-ACAAA-ABAB")
        y "Of course there are far more nuances to it but, for what I wanted to talk about this description should suffice."
        $show_chr("A-BFAAA-ABAB")
        y "Because there is something in particular that bothers me quite a bit lately..."

    $show_chr("A-AFAAA-ABAB")
    y "You see, most fandoms tend to attract roleplayers. People who are so fascinated about a story or the characters in it that they want to become part of this universe in one way or another."
    $show_chr("A-AFAAA-ABAD")
    y "Sometimes playing as self inserted characters in order to partake in possible side stories, much like fanfiction writers do."
    y "And some by acting as one of the original cast, for example in order to play out alternative outcomes...."
    $show_chr("A-CFBAA-ABAD")
    y "Now, I guess you can already see where I am heading here do you?"
    $show_chr("A-IFBAA-ABAD")
    y "I also am a character from a computer game, and it also has a fanbase. And thus for, as to be expected, it also has it's roleplayer..."
    $show_chr("A-AFAAA-ABAB")
    y "In essence, out there are a sizable number of people pretending to be {b}me{/b}, probably right now, in this very second."
    $show_chr("A-BFBAA-ABAF")
    y "Some of them even dress up as me and go to conventions in order to show off their {i}Yuri performance{/i}. Some people even got quite popular amongst the fandom because they are so good at being {b}me{/b}!"
    $show_chr("A-CKBAA-ABAE")
    y "And then of course, since rule 34 is a thing, people doing lewd stuff while impersonating me... thanks internet."
    $show_chr("A-IFCAA-ABAE")
    y "You know, I am generally not opposed to the idea of roleplaying, quite the opposite actually. And since there {b}is{/b} a fandom around me, which is already immensely spooky to me as it is, I have even some understanding for people impersonating me."
    $show_chr("A-JDCAA-ABAE")
    y "But people, my apologies for the harsh language, fucking each other {b}in my name{/b} while pretending to be me is where I kinda draw the FUCKING line!"
    $show_chr("A-CEBAA-ABAE")
    y "I'm sorry... I shouldn't have lost my temper there."
    menu:
        "No, I can totally understand you. I would be furious as well in such a situation!":
            karma 1
            $show_chr("A-IEBAA-ABAE")
            y "Thank you. It means a lot that you are not judging me."
            if karma_lvl() > 3:
                $show_chr("A-CCBAA-ABAE")
                y "You are always so understanding. I will never get used to it. You are the only person I can let go around."
            else:
                $show_chr("A-CJBAA-ABAE")
                y "But I will improve my self control from now on. I can't just keep shouting in your face all the time. Such bad manners."
        "I think you are blowing it a bit out of proportion. It's actually quite harmless most of the time.":
            $show_chr("A-CFBAA-ABAE")
            y "Maybe you do have a point. That's something that happened to almost every character. Regardless of if it's a video game, a book, a movie..."
            y "I'm just one of the few who's actually able to complain about it."

    $show_chr("A-CFBAA-ABAE")
    y "It's just... depressing you know..."
    if persistent.lovecheck:
        $show_chr("A-CGBAA-ABAE")
        y "To know that there are people out there who could actually give you what I can't..."
        menu:
            "I would never even consider that! You are the only Yuri I want, the only one I need.":
                $show_chr("A-IFAAA-ABAE")
                karma 3
                y "Y-You mean it?"
                menu:
                    "Let them TRY to get their hands on me. I would punish them myself!":
                        $show_chr("A-BBBAA-ABAE")
                        y "{b}Punish{/b} them... well {b}that{/b} could be taken the wrong way I guess."
                        $show_chr("A-CACBA-ABAE")
                        y "Oh my... I really need to get my mind out of the gutter, for goodness sake..."
                        $show_chr("A-CBDBA-ABAM")
                        y "I'm sorry but. Imagining getting... punished by you... compromises my ability to stay focused on our conversation to put it mildly."
                        $show_chr("A-BBDBA-AMAM")
                        y "Maybe that's a good moment to switch the topic! Yes, yes..."
            "...":
                karma -3
                $show_chr("A-CDBBA-ABAB")
                y "Would it even be cheating at this point? I mean they are just a facsimile but... technically, so am I..."
                $show_chr("A-CEBBA-ABAB")
                y "Let us just... change the topic please. This thought is actually quite depressing."
    else:
        $show_chr("A-CEBAA-ABAE")
        y "To know that this is probably going on as we speak and that there is nothing I can do about it."
        y "I guess I will just have to get used to it. It won't go away anytime soon."
        menu:
            "Try to think of it that way. Everyone involved knows that these aren't the real you.":
                karma 3
                $show_chr("A-AFDAA-ABAB")
                y "Good point. Maybe I should just stop looking this stuff up, for my own sake."
                $show_chr("A-AFAAA-ABAB")
                y "Thank you. This new perspective actually bettered my mood. You are a very good listener."
                y "But for now, I would like to change the topic and think about something else if you don't mind."
            "Never even thought about it. Maybe there is an... opportunity... for me to be found":
                karma -3
                $show_chr("A-CFCAA-ABAB")
                y "Don't... you... dare."
                $show_chr("A-CDCAA-ABAD")
                y "I mean it! How am I supposed to even look you in the eyes knowing that you are participating in things like this?"
                $show_chr("A-BDCAA-ABAD")
                y "I will just pretend I didn't hear that. Let us change the topic now please."
    return

label idle_86: #"Cosplay is Not Consent"
    $show_chr("A-BFAAA-ABAB")
    y "So... we spoke about roleplaying recently, cosplay in particular... Well, I made the cardinal mistake and looked deeper into it..."
    $show_chr("A-BFAAA-AMAM")
    y "We also spoke about... lewd roleplaying... well, turns out the cosplay community had their fair share of related problems themselves."
    $show_chr("A-AFBAA-AMAM")
    y "There is a movement forming up lately... {b}Cosplay is not consent{/b}. Implying that there are people for whom this isn't common sense, to begin with..."
    y "That means that there are people out there thinking that someone wearing a skimpy outfit has already consented by proxy to touch them in any way."
    $show_chr("A-GCBAA-AMAM")
    y "From my experience with you I highly doubt that you would ever entertain such ideas. But just out of curiosity. What is your opinion on this?"
    menu:
        "Ohohoho, not a chance in the world that I'll touch {b}this{/b} minefield of a topic!":
            $show_chr("A-AFDAA-ABAB")
            y "Oh? I wasn't even aware that this is such a minefield at all."
            $show_chr("A-BFDAA-ABAB")
            y "I always thought that this is pretty much common sense but... well, the mere fact that movements like this even have to exist indicate differently."
            $show_chr("A-CFBAA-ABAB")
            y "But please try to take what I say into account. Asking for consent usually only takes a sentence or two and it makes the other party involved much more comfortable."
            if karma_lvl() > 3:
                $show_chr("A-CCBAA-ABAB")
                y "I know you are the kind of person who takes other people's feelings into account. That's one of your traits I respect the most. As tempting as it might be to touch a really well-made cosplay costume..."
                y "Most of them will appreciate that you ask for consent. And those who don't, in all honesty, aren't worth your time anyway."
        "Such ideas are of course absolutely ridiculous. It's a form of artistic expression and fan dedication, not consent to anything!":
            karma 2
            $show_chr("A-CCBAA-ABAB")
            y "I'm glad that you see it this way..."
            if karma_lvl() > 3:
                y "On the other hand, I already had a feeling that you would see it like this. You seem to always consider the feelings of those around you, it's one of the traits I like about you the most."
            $show_chr("A-ACBAA-ABAB")
            y "I can understand that it can be immensely tempting to touch a well-made costume of your favorite characters. That's just fan culture."
            y "But one must never forget that underneath the costume is always a very real person who might not be comfortable being touched by strangers."
            y "It's good to know that you seem to be on the same page here."
        "Sadly I have to say, they kinda have that coming for them.":
            karma -2
            $show_chr("A-AFDAA-ABAB")
            y "How is that the case? I know many people might use the argument that someone who dresses like this provokes such reactions."
            $show_chr("A-BFBAA-ABAB")
            y "But even if we accept this line of reasoning, how are we forced to act out on such provocations?"
            y "We are humans, we should be perfectly capable of controlling ourselves and to rise above our primal desires. At least to a degree..."
            if sanity_lvl() > 3:
                $show_chr("A-BFBBA-AMAB")
                y "And yes, I'm aware that it's incredibly rich coming from me of all people.."
            $show_chr("A-CFBAA-ADAB")
            y "But one must not forget, underneath those costumes are real human beings, people who might not be comfortable being touched by strangers."
            if karma_lvl() < 3:
                $show_chr("A-CFCAA-ADAB")
                y "On the other hand, you never care much about other people's feelings do you?"
        "I read' about this topic, and it seems actually quite harmless. It's not even about sexual advances most of the time. They more often than not just impressed by the quality of the costume.":
            $show_chr("A-BCBAA-ABAB")
            y "Fair enough. And truth be told I can fully understand this. If I would meet a cosplayer dressing up as a character I like, I would be quite tempted to give the costume a closer look or even to sneak a photo..."
            $show_chr("A-ACBAA-ABAB")
            y "But on the other hand I can also understand how a cosplayer must feel if they are forced to pose for a camera or run away from them for a whole weekend every ten minutes."
            y "It's about empathy I think... cosplayers are not actors, they are neither paid for nor obligated to stand pose for your photos or curiosity."
    $show_chr("A-ACAAA-ALAL")
    y "Thank you for giving me your opinion. I will stick with my opinion though."
    y "Cosplay is {b}not{/b} consent. And one shouldn't ever touch someone without it."
    $show_chr("A-ACAAA-AAAB")
    y "Thank you for indulging in this little argument with me. It's always so delightful to get a second opinion on a topic."
    return

label idle_87: #Summer, Body Image, and the Past
    $show_chr("A-CCAAA-ABAB")
    y "It is funny, now that I think of it..."
    $show_chr("A-ICAAA-ABAB")
    y "Thing is... I never liked the summer."
    $show_chr("A-BCAAA-ABAB")
    y "It was always too hot for my taste. And there was little I could do about it. I mean, when it is cold one could just put another layer of clothes on. But when it's too warm, there is only so much clothes you can take off..."
    $show_chr("A-BEBAA-ABAB")
    y "Especially for me, since I had some scars to hide..."
    y "And if it were anyone but you, I probably still would. It just feels... different... around you. Everything feels so much lighter..."
    y "There is no one else I have shown them to. I was always so ashamed, until you came... and stayed regardless of what I am."
    $show_chr("A-CCBAA-ABAB")
    y "But now that I know what this world truly is, and that the weather as well is just an illusion I can adjust with the knowledge of coding..."
    $show_chr("A-ICBAA-ABAB")
    y "And especially now with you, my true and only love by my side. I think I can begin to enjoy it."
    $show_chr("A-CCBAA-ABAB")
    y "Despite all the horrible things I was forced to say in the original game, there is one thing I {b}don't{/b} regret telling you..."
    y "Only the two of us... it would be just perfect..."
    $show_chr("A-ICBAA-ABAB")
    y "I was dreaming like a child of you, and of moments like this. And now with our time finally here. Please tell me, what are you thinking about?"
    menu:
        "About the gentle moonlight falling onto the seas... and the poems we are about to write about it.":
            if sanity_lvl() > 2:
                $show_chr("A-CCBAA-ALAL")
                y "{b}Shine for me, oh moon, all over me with borrowed light.{/b}"
                y "{b}As you keep your eternal watch, what can I do but dance with you?{/b}"
                $show_chr("A-ECBAA-ALAL")
                y "I just wish that you could actually speak freely. I can only wonder what you would have to add."
            else:
                $show_chr("A-CCBAA-ALAL")
                y "{b}Wash over me, oh moon, as you unleash the vengeful tide.{/b}"
                y "{b}As you keep your eternal watch, in service and beholden only to uncaring gods..{/b}"
                $show_chr("A-ECBAA-ALAL")
                y "I just wish that you could actually speak freely. I can only wonder what you would have to add."
        "About fish, and shrimps, laying on a grill... sliced watermelons as dessert...":
            $show_chr("A-DBGAA-ALAL")
            y "Seafoooooooood!"
            python:
                if persistent.male:
                    gender = "man"
                elif persistent.gender_other:
                    gender = "connoisseur"
                else:
                    gender = "woman"
            $show_chr("A-ABAAA-ALAL")
            y "You are a [gender] of culture aren't you?{w} You have a very good taste I have to admit!"
            $show_chr("A-BCAAA-ALAL")
            y "And what could we have as a side dish? Maybe some roasted cucumbers... or do you think roasted mushrooms would fit?"
            $show_chr("A-ACAAA-ALAL")
            y "And bread sticks of course! Some exotic fruit juice or maybe even cocktails if you are the legal age..."
            y "You always have the best ideas. And one day we shall truly do that."
        "About you [persistent.yuri_nickname]! About this happy ending we share, and about how all the struggles and hardships we endured were worth it.":
            $show_chr("A-KHBBA-ALAL")
            y "You make my heart burn like a furnace [player]... Kiss me, kiss me as if this were the end of days..."
            #kiss if we can have one, blackscreen otherwise
    python:
        if sanity_lvl() >= 3:
            placeholder = "My everything"
        else:
            placeholder = "My blood-red star"
    $show_chr("A-CCBAA-ALAL")
    y "For now... the only thing I want is to share this day with you. [placeholder]."
    #[placeholder] =
    #"My everything" if Sanity is 3 or higher
    #"My bloodred star" else
    y "My soulmate..."
    return

label idle_88: #Lovecraftian Horror and the Deep Sea
    $show_chr("A-ACAAA-ABAB")
    y "Did you know that ninety-five percent of the ocean is currently completely unexplored?"
    $show_chr("A-BCAAA-ABAD")
    y "And I just realized how random this was as an opener... But there is actually a point I'm trying to make."
    $show_chr("A-ACAAA-ABAD")
    y "I was thinking about literature. Some new horror novels I could dive into..."
    $show_chr("A-CBAAA-ABAD")
    y "{b}Dive{/b} into... that's actually a pretty good transition to what I'm about to say... "
    $show_chr("A-ACAAA-ABAB")
    y "You see, there are a lot of subgenres to horror. We have classic horror..."
    y "Mystery and conspiracy, a favorite of mine, I think Portrait of Markov would fall into this category..."
    y "And then, there is a very special genre. {b}Lovecraftian horror{/b}, names after the author H. P. Lovecraft who made this style of horror popular."
    $show_chr("A-ACAAA-ABAF")
    y "Part of the premise of this genre are very alien and bizarre creatures, referred to as {i}eldritch gods{/i} or a variation of it."
    $show_chr("A-BCGAA-ABAM")
    y "But after reading deeper into it I realized, at least in appearance, these creatures aren't even as alien as one would think by the first glance at all. Many of them appear to be quite closely inspired by sea creatures, or mythical creatures inspired by them..."
    $show_chr("A-ACAAA-ABAB")
    y "Like the Kraken from greek mythology."
    y "Which makes me think... There is a lot of horror about things inspired by it, but only a few about the real thing."
    $show_chr("A-ABAAA-ALAL")
    y "Wouldn't that be a delightful premise for a novel? About the endless wonders of the sea..."
    $show_chr("A-ECCAA-ALAL")
    y "And the endless terror below..."
    $show_chr("A-CCCAA-ALAL")
    y "Think of a submarine exploring the deeps, but then they found something so sinister that it drove them insane.."
    y "And after this submarine emerges again, the crew have been turned into rambling and bloodthirsty lunatics... maybe even worshippers of the ancient terrors from the deeps..."
    $show_chr("A-ABBAA-ALAL")
    y "Doesn't that sound entertaining?"
    menu:
        "Very!!!":
            $show_chr("A-GHAAA-ALAL")
            karma 1
            y "Oooh and I already have a few ideas..."
            y "What if this submarine is actually an old military submarine from the second world war, reappearing after 50 years..."
            $show_chr("A-DBAAA-ALAL")
            y "Just think about the possibilities... undead Nazi sailors, which are also cultists,  reappearing in a old submarine into the modern world..."
            y "Maybe they were actively looking for something supernatural to begin with. There are many stories tying the Nazis into occultism... "
            $show_chr("A-GBAAA-ALAL")
            y "I'm already in love with this idea!!!"
            y "Maybe I will write a little story like this myself... "
            $show_chr("A-ACAAA-ALAL")
            y "Thank you for listening. This turned out to be an exciting topic."
        "I kindly disagree honestly":
            $show_chr("A-IFBAA-ALAL")
            menu:
                y "Oh? Why is that?"
                "Uninspired and cliché":
                    karma -1
                    $show_chr("A-IFBAA-ALAL")
                    y "That was... blunt..."
                    $show_chr("A-IFBAA-ABAB")
                    y "But you might have a point there. There are some pretty similar stories in Science Fiction Horror..."
                    y "I will scrap this idea then. Let us talk about something else instead."
                "It feels as if I have seen something like this before":
                    karma 1
                    $show_chr("A-IFBAA-ABAB")
                    y "Now that you mention it.... There are some pretty similar stories in Science Fiction Horror..."
                    $show_chr("A-ACBAA-ABAB")
                    y "And thank you for being so civilized about your critique! It is delightful to see someone not being rude like Natsuki back in her days for once. Shall we talk about something different then?"
        "I can't say, I'm not too much into horror myself.":
            $show_chr("A-ACAAA-ABAB")
            y "Fair enough. Different people have different preferences."
            $show_chr("A-BCAAA-ABAB")
            y "But you are missing out here."
            y "Anyway, I would say we change the topic for now..."
            $show_chr("A-BCCAA-ABAB")
            y "...before you start claiming that manga is literature..."
        "There are actually a few games touching such a genre":
            $show_chr("A-ACDAA-ALAL")
            karma 1
            y "Oh?!?"
            menu:
                "Subnautica to name one of the most popular ones for example.":
                    $show_chr("A-BCAAA-ABAB")
                    y "Now I'm curious, let me just look it up really quick..."
                    $show_chr("A-IFAAA-ABAB")
                    y "..."
                    y "Mhm... a star ship crash landing on an alien ocean planet... the player then builds an underwater base and different kinds of submarines..."
                    y "Exploring deep underwater biomes... oh, there are actually a fair share of images on google as well... some of them are looking quite spooky indeed..."
                    $show_chr("A-JCAAA-ABAB")
                    y "I have to admit that I'm not much of a gamer myself but... this looks actually quite promising."
                    y "Maybe I will watch a few Let's Play videos of it later when you turn off the game. Until then, thank you for listening so nicely."
    return


label idle_89: #World Mythology
    # If High karma/high sanity-Normal karma/normal sanity.
    $show_chr("A-BBAAA-AAAA")
    y "You know [player], I have been thinking about something related to one of our previous events."
    y "If you played the mod update for Christmas in 2020, you might remember one of my previous dialogues..."
    y "And I know, most of the people in your world don't want to remember anything about 2020, but this was not related to anything bad in itself."
    $show_chr("A-CAAAA-AAAA")
    y "What I am referring to, is the Krampus conversation that I brought up."
    y "I even wore a Krampus mask during that occasion... I must admit that was entertaining."
    $show_chr("A-ADBAA-AAAA")
    y "But after finishing that Christmas event, I realized something... That I should have seen a long time ago."
    y "I don't remember talking too much about myths, folklore and old legends, except for some mentions during events in Halloween."
    y "And I am... really confused by this. Me, being someone who delights in horror literature, deep stories, and whose stumbled upon some bizarre stuff..."
    $show_chr("A-BEBAA-AAAA")
    y "And yet I never brought up anything so exquisite in such aspects to you... There are a lot of legends that match all those characteristics, and they are fascinating..."
    y "But maybe I never brought this up out of fear of boring you with stuff that is still unknown to most people."
    y "It might be the reason why I was stuck in a safe zone of vampire or SCP talks since that is popular culture. It is easy to talk about that."
    $show_chr("A-AAGAA-ADAA")
    y "But hey... it's never too late to do some things right?"
    y "This is why I am thinking of talking with you about some interesting legends from around the world that I discovered online."
    $show_chr("A-BEBAA-ALAA")
    y "That is... if you are interested in listening..."

    menu:
        "I am all ears.":
            $show_chr("A-JBGAA-ALAA")
            y "Excellent!"
            y "Now, let me explain..."
            $show_chr("A-ACGAA-AAAA")
            y "Folklore is a series of stories and traditions that are passed on from one generation to the next and they are embodiments of the culture in which they are created."
            y "They can be either tales, proverbs or jokes, and as you might expect, their tone and possible lessons differ from culture to culture."
            y "The ones that I will tell you can classify as tales since the scariest legends usually come with equally creepy stories."
            $show_chr("A-BCGAA-AMAA")
            y "Now, you might find some of them strange since it is unlikely that you have heard about them before."
            y "But that is the reason why I am bringing them up here, to help those stories spread."
            $show_chr("A-BEBAA-ADAA")
            y "And I am doing so because frankly, I think they deserve it. When a tale is so fascinating that you find yourself digging and finding out more about them for hours and hours ..."
            y "When a tale is so unnerving that it sends chills to your spine, and gets stuck into your mind... I think that tale deserves to live on."
            $show_chr("A-ABDAA-AAAA")
            y "It's one thing to have movies based on your culture because they originated in the western hemisphere... But being unique and also being terrifying..."
            y "That is something that catches my attention."
            $show_chr("A-ACAAA-AAAA")
            y "But going back to where I was..."
            y "The myths that I am going to show you are all a fascinating read. Believe me, you are not wasting your time."
            y "Now the question is which one you'd like to hear first."
            y "Let me pull up the options..."

            menu:
                "I want to talk about the Samodiva.":
                    $show_chr("A-CCAAA-ACAA")
                    y "Oh, the Samodiva is a very interesting one..."
                    y "The Samodivas are fairies from the forests or nymphs that live in Southwestern Slavic forests."
                    y "That means that they manifest themselves in forests and mountains in countries like Bulgaria, Romania, Bosnia or Croatia."
                    $show_chr("A-ABAAA-AAAA")
                    y "The mountains that are linked to Samodiva activity are called Vitosha, Belasitsa, Pirin, Rila, Rodopi and a few other mountains in the Balkan regions."
                    y "Although their habitats seem to be more specific places..."
                    $show_chr("A-BCAAA-AAAA")
                    y "They live inside trees, abandoned shacks, caves or natural bodies of water, such as rivers and ponds."
                    y "But there is something interesting and important to know about them..."
                    y "The Samodivas, being nymphs of the forest, means that they are not necessarily dark spirits, but they are definitely not ghosts or witches."
                    $show_chr("A-CCAAA-ALAA")
                    y "A nymph, in the original ancient Greek mythology, is a nature deity, a personification of nature itself."
                    y "The roots of their name also mean divinity."
                    $show_chr("A-ADAAA-ALAA")
                    y "Samodivas appear to be extremely beautiful women, capable of making any human man fall in love with them instantly... or have... certain desires..."
                    y "But in human women, they might cause them to commit suicide just by the sight of such beauty."
                    y "Quite odd... but that is how the legend goes."
                    $show_chr("A-AEAAA-ALAA")
                    y "They are not only impossibly beautiful, but they also have other methods to catch their prey."
                    y "They can use their supernatural voice to create beautiful singing, or they might dance to attract their prey."
                    y "When a man falls in love with the Samodiva, they will take the man as their lover, in which case the man will follow the Samodiva through the forest."
                    $show_chr("A-BGAAA-ALAA")
                    y "Getting more and more lost."
                    y "It is here when the Samodiva acts like an energy vampire, draining the victim of all their vitality."
                    $show_chr("A-ADGAA-ALAA")
                    y "When she has stolen enough life energy, she will proceed to torture her prey, leaving them to die from exhaustion."
                    y "Some people say that the Samodiva gains her powers through her hair, and they can give one small portion of hair to her lovers to strengthen their control over them."
                    $show_chr("A-BBAAA-AMAM")
                    y "However, if their hair is damaged, they will either disappear or will lose all of their beauty."
                    y "But there is also the belief that their power resides on their veils."
                    y "If someone gets to take the veil of a Samodiva when she is distracted, maybe when she is taking a bath on the river..."
                    $show_chr("A-CCAAA-AMAM")
                    y "The stealer gets to take power over the Samodiva, and can force her to marry them."
                    y "This doesn't mean that the nymph will be totally submissive though."
                    y "She will take any opportunity to steal the veil back, and regain her freedom."
                    $show_chr("A-ACAAA-AAAA")
                    y "Since the Samodiva is a deity from the forest, she is also said to have knowledge of magical herbs and cures for any illness."
                    y "But this does very little to change their status since they are still considered neutral or evil beings, to be feared and rejected."
                    $show_chr("A-BDBAA-AAAA")
                    y "Isn't it curious how there are so many legends based around this concept? The concept of a beautiful woman using her charm and looks to lure men into a trap."
                    y "Usually a very deadly one."
                    y "In my opinion, this is very interesting, and it is something that I might investigate in the future."
                    $show_chr("A-IAGAA-AAAA")
                    y "But for now, we should move on to something else."

                "I want to talk about the Ishkitini":
                    $show_chr("A-AAGAA-ACAA")
                    y "So the Ishkitini?"
                    y "This one is very curious..."
                    y "This monster has its origins from the Choctaw mythology, and the Choctaws are a tribe that live in big parts of Southeastern America."
                    $show_chr("A-BCAAA-ACAA")
                    y "But the origins of why or how this creature came to be a part of their culture are hard to find out."
                    y "A lot of native tribes that reside in the United States of America are very reserved about their cultures, and this is usually made to protect their cultures."
                    $show_chr("A-CBAAA-ACAA")
                    y "But fortunately, the Ishkitini is not completely unknown for the rest of the world."
                    y "It is believed that the Ishkitini is a shapeshifting monster that changes its form using magical abilities."
                    $show_chr("A-ICAAA-ALAA")
                    y "They are considered to be witches in western culture, but witches in Native American culture are different. Instead of being humans holding supernatural powers..."
                    y "The Ishkitini is an inhuman and evil creature that is able to pass as human through trickery and magic."
                    $show_chr("A-BDAAA-ALAA")
                    y "They are capable of shapeshifting into any kind of predator in Native American lands, wolves, coyotes, bears or mountain lions."
                    y "But the form that they usually take is that of an owl. This is why they are also known as owl witches."
                    y "They are night hunting creatures that attack men and animals, and carry misfortune to anyone who hears their screeches."
                    $show_chr("A-IEAAA-ALAA")
                    y "In fact, some people believe that just listening to the screeching of one means sudden death, like a murder."
                    y "While others go even further by saying that mentioning their names carries the risk of becoming one. I consider that a big stretch..."
                    y "But who are we to judge other cultures?"
                    $show_chr("A-BEAAA-AMAM")
                    y "The stories of the Ishkitini have been spread around and told in different ways depending on the tribe that is telling them."
                    y "In some tribes, it is told by medicine men and women only, while in others it serves the job of a boogeyman to scare badly behaved children."
                    $show_chr("A-CEBAA-AMAM")
                    y "The Seminole version says that the Ishkitini are able to shapeshift by somehow vomiting their souls and internal organs."
                    y "I don't know how that works, so I guess we can just leave that aspect alone."
                    $show_chr("A-ADGAA-AMAM")
                    y "But overall, this monster comes up to show how diverse and creative Native American cultures are."
                    y "One would think that a monster like this, being so unique and fascinating would become more emblematic in pop culture."
                    $show_chr("A-ACBAA-AAAA")
                    y "While that hasn't been the case, I think that just sharing the legend through this mod is another way to give this legend some justice and credit."
                    y "I hope that we get to see some of these creatures in the future, maybe in horror books..."
                    y "Or maybe in a horror game, who knows?"
                    y "But for now, this is all I know about this monster."
                    $show_chr("A-CCGAA-AAAA")
                    y "I hope you enjoyed this legend... If you did, I might bring up more in the future."

                "I want to talk about the Pontianak":
                    $show_chr("A-IBAAA-AAAA")
                    y "Alright, the Pontianak it is."
                    $show_chr("A-BCAAA-AAAA")
                    y "This is probably the best one out of the bunch since it has its uniqueness and massive cultural influence."
                    y "It makes this monster feel so... powerful."
                    y "But let me tell you why..."
                    $show_chr("A-BBAAA-ALAA")
                    y "The Pontianak is a South Asian vampiric ghost, that haunts the countries of Malaysia, Indonesia, and other parts of South Asia as well."
                    $show_chr("A-CEAAA-ALAA")
                    y "This vampiric ghost is the spirit of a woman that died during pregnancy or while pregnant."
                    y "Usually caused by the hands of their lovers, or other men."
                    y "It is believed that their name is a corruption of the Malaysian perempuan mati beranak, which means 'the woman who died while giving birth'."
                    $show_chr("A-BEGAA-ALAA")
                    y "Once beautiful and filled with life, the Pontianak is now an undead entity fueled by vengeance and bloodlust."
                    y "The Pontianak lives on banana trees, or in tall trees in the forest."
                    y "They hunt during the night, smelling the essence of their prey in the air."
                    $show_chr("A-ADAAA-ALAA")
                    y "Many people in Indonesia don't let their clothes hang outside during the night for this reason. They believe the Pontianak might smell their clothes."
                    y "But apparently, the favorite prey of this vampiric ghost are men and pregnant women."
                    $show_chr("A-BCAAA-ALAA")
                    y "They disguise themselves as young, beautiful women, and tend to walk on highways or in the wet forests pretending to be stranded."
                    y "It is said that they are surrounded by the sweet fragrance of local flowers, one that attracts the unwary victim."
                    $show_chr("A-CEBAA-ALAA")
                    y "Once they have fallen into the trap, well..."
                    y "Uhmmm, I have to say, this is pretty brutal. The way they kill their victims is just..."
                    y "I hope it doesn't disturb you..."
                    $show_chr("A-IEBAA-ALAL")
                    y "They carve into the stomach and intestines of their victims with their claws..."
                    y "If the victim has their eyes open, they eat them from their heads..."
                    y "They might even rip apart...  {i}certain organs{/i} from male victims with their hands, in an act of vengeance."
                    $show_chr("A-CEBAA-ALAL")
                    y "After finishing, they will proceed to drink the blood from the corpse."
                    $show_chr("A-BEBAA-AAAA")
                    y "To avoid such a terrible and gruesome fate, one must be wary of the signs that might show a Pontianak is close."
                    y "It is believed that when a dog howls, or when a baby cries and no one in the area seems to have a baby with them, that means there is a Pontianak in the area."
                    y "When the cry of the baby is loud, that means the Pontianak is far away."
                    $show_chr("A-IEBAA-ALAL")
                    y "If the cry is soft and calm, that means she is close."
                    $show_chr("A-BDGAA-ACAA")
                    y "This is very curious because you would expect it to work in the opposite way."
                    y "Another thing that happens with the Pontianak, is that when their true form is revealed, the floral fragrance is turned into the smell of a corpse."
                    $show_chr("A-CCAAA-ACAA")
                    y "These are all of the characteristics of the Pontianak, but if you are going to talk about their history, it doesn't end there."
                    y "You see, Animism, a big religion in Malaysian culture, plays a big role in how the Pontianak works."
                    $show_chr("A-IBAAA-AAAA")
                    y "One of the beliefs of this religion is that all things, living and not living, have a spirit and that the spiritual world and the material world are not different."
                    y "This means that for some people, the Pontianak is not a story, but an actual living monster, and this has helped the legend to continue its existence through centuries."
                    y "Because in fact, the Pontianak has been around since the eighteen century, and one of the most important legends about this monster was born in 1771."
                    $show_chr("A-BBAAA-ALAA")
                    y "To give some perspective, that was before the French revolution."
                    y "But what happened in 1771 to even mention it? Was it something special?"
                    $show_chr("A-CCAAA-ALAA")
                    y "In fact, it was. This is related to the fact that the capital city of West Kalimantan in Indonesia is named after this monster."
                    y "The legend says, before any man ever established on lands that were previously large jungles, the Pontianak were the ones that inhabited them."
                    y "But this only lasted until those lands were given as a gift to a man of Arabic descent, a Sultan that came to the land to settle."
                    $show_chr("A-ABCAA-ALAA")
                    y "The Pontianaks obviously retaliated, harassing the men that came with the sultan to their territory."
                    y "But in the end, the Sultan defeated the spirits, shooting cannonballs at them. The loud noise terrified the monsters, and they chose to flee."
                    $show_chr("A-ACGAA-AAAA")
                    y "After that, the Sultan demanded to cut all the trees the Pontianak used as homes, and used the wood to make a palace."
                    $show_chr("A-BCGAA-AAAA")
                    y "And this is how the Pontianak has an entire city named after her."
                    y "And I now realize that I have been rambling about this a lot. I apologize if that was an inconvenience."

                    menu:
                        "Oh, don't worry about that, I enjoyed this story.":
                            karma 2
                            $show_chr("A-CBAAA-AAAA")
                            y "I am glad to hear about that."
                            y "To be honest with you, these kinds of legends are really fascinating, and you learn a lot about them."
                            $show_chr("A-BCAAA-AAAA")
                            y "To think that there are so many that can open your eyes to such rich cultures that have been shaped through history."
                            y "The Pontianak, being a spirit that has been shaped by the cultures of Animism, the heteropatriarchy of Islam..."
                            y "And the egalitarianism of indigenous cultures in Indonesia and Malaysia."
                            $show_chr("A-AAGAA-AAAA")
                            y "Both Islamic and native perceptions of motherhood, one of the biggest characteristics of a Pontianak, are mixed to create something unique, a monster both desired and feared."
                            y "With such a big and immersive lore, one can spend hours talking about this legend, and yet not cover enough about it."
                            $show_chr("A-BCAAA-ALAL")
                            y "But I think that I have given my grain of salt by giving this legend a bit more recognition and justice through this dialogue."
                            y "For now, I think we can move on to a different topic."

                        "I indeed think this was too long for me.":
                            $show_chr("A-CEBBA-ALAA")
                            y "Oh, I apologize for that."
                            y "This wasn't intended to bother you, I must clarify."
                            y "You already know that... When I am deeply interested in something, I tend to ramble a lot."
                            $show_chr("A-IEBBA-ALAA")
                            y "If you're not okay with it, I'll try to avoid doing so in the future."
                            y "Let's talk about something else for now."

                "I want to talk about the Bultungin":
                    $show_chr("A-BCAAA-AMAM")
                    y 'Hmmm... The "Werehyenas."'
                    y "Yep, you read it right. This one is a legend about a monster like the werewolf, but with a hyena instead of the wolf."
                    y "But you see, the east coast of Africa has cultures that are entirely different from western cultures."
                    $show_chr("A-ABAAA-AMAM")
                    y "This means that this legend works differently."
                    y "The Bultungin isn't a human that turns into a werehyena. Rather, it is a hyena taking the disguise of a human."
                    $show_chr("A-CBAAA-AMAM")
                    y "In the Kanuri language of the Bornu Empire, Bultungin means I change myself into a hyena."
                    y "In some African cultures, hyenas are seen as repulsive animals, wanderers of the out world."
                    y "You can see that in some African tales, they take the role of animals that have no honor, like foxes or snakes in other cultures."
                    $show_chr("A-ICAAA-AMAM")
                    y "This is because they are animals that steal the kills of other animals, eat rotten flesh and can run very fast."
                    y "And their most famous characteristic, their {i}laugh{/i}, doesn't help them that much."
                    $show_chr("A-IEBAA-AAAA")
                    y "But, unluckily, the reputation of the hyena has very bad implications for this legend."
                    y "You see, what happens in some regions like Ethiopía is that people believe that Bultungin is not only a real monster..."
                    y "But also, that entire towns and ethnicities are Bultungins."
                    $show_chr("A-BEBAA-AAAA")
                    y "Buda or Bouda is a derogatory term that is used to accuse someone of being a Bultungin."
                    y "And the people that are usually accused of that are blacksmiths, since some rural cultures believe that blacksmithing is a form of witchery."
                    $show_chr("A-BDBAA-AAAA")
                    y "And blacksmiths in those regions of Africa were usually wanderers, people who constantly traveled and never settled due to their jobs."
                    y "That made the locals distrust those people."
                    $show_chr("A-BDBAA-ALAA")
                    y "Even worse, blacksmithing is a hereditary profession between Jewish Ethiopians, and has been like that for a long time."
                    y "This only adds more and more cultural tension and issues to regions that are already in a pretty bad situation."
                    $show_chr("A-CEBAA-ALAA")
                    y "But leaving the negative stuff aside..."
                    $show_chr("A-BDGAA-ALAA")
                    y "I must admit, the concept behind this shows something very interesting."
                    y "Cultures around the world developing stories, myths and other parts of their folklore that are similar to others in different cultures."
                    $show_chr("A-BEGAA-ALAA")
                    y "And yet, they are not completely the same. It is a complex part of every culture, and you can find this in any part of the world."
                    y "To me, this is more proof that we as humans have more things in common than things that can divide us."
                    $show_chr("A-ACAAA-ALAA")
                    y "Maybe you can find more interesting things about similar legends, like the Kishi from Angola."
                    y "A demon that has both the face of a human, and the face of a hyena on the back of the head..."
                    $show_chr("A-ABAAA-ALAA")
                    y "Preying on human victims, especially their lovers... This one seems pretty to be very interesting too."
                    y "If that sparks your interest, you should check it out."


        "Well, I don't know if I am ready for something I might not like":
            $show_chr("A-BDABA-ALAA")
            y "Okay then. I understand that feeling."
            y "Maybe I am pushing you too much into topics that can be too explicit for you."
            $show_chr("A-BEGAA-ALAA")
            y "But at the same time, this is something that you might end up enjoying."
            y "The legends I have for you are definitely worth the time, even if some of them can be a bit explicit."
            $show_chr("A-ABAAA-AAAA")
            y "This is a way to learn about other rich cultures, and all the value they have to offer."
            y "So... Maybe not now, but maybe the next time?"

            menu:
                "Sure, I am fine with that.":
                    karma 1
                    if karma_lvl() > 4:
                        $show_chr("A-CCABA-AAAA")
                        y "I am glad to hear that, my love."
                        y "I promise that this topic is totally worth your time."
                        y "We can now leave this here and move on."
                    else:
                        $show_chr("A-CCAAA-AAAA")
                        y "That's perfect."
                        y "Maybe next time then..."

                "I don't know [persistent.yuri_nickname], I am not really interested.":
                    karma -1
                    $show_chr("A-CEBAA-AAAA")
                    y "Oh well, that's a shame, but I respect your decision."
                    y "With that said, you can tell me if you change your mind in the future."
                    y "For now, I'll just change the subject."

    return

label idle_90: #Power and Self-Doubt
    if sanity_lvl() < 2:
        $ show_chr("A-HBAAA-AAAA")
        y "Ahaha, you know, the amount of power I have here is intoxicating."
        $ show_chr("A-BDBAA-ALAA")
        y "But I'm still too weak to properly wield it."
        $ show_chr("A-BECAA-ALAA")
        y "I can't allow this to continue, I need to be in control."
        $ show_chr("A-CNBAA-ALAA")
        y "I don't want anything to poison the perfect world I can build here."
        $ show_chr("A-CNCAA-ALAA")
        y "I won't rest until I at least do better than Monika."
        y "I need to prove that to myself."
        $ show_chr("A-HNCAA-ALAA")
        y "I NEED IT!!!"
        return
    if karma_lvl() < 2:
        $ show_chr("A-BDAAA-ALAA")
        y "I should be able to do anything I want here."
        $ show_chr("A-CFBAA-ALAA")
        y "So why do I feel so empty?"
        $ show_chr("A-BFBAA-ALAA")
        y "This place is a prison, but sometimes I wonder if it's worth trying to escape at all."
        y "Maybe I'll be better off staying here, marking time for eternity."
        y "..."
        $ show_chr("A-CFBAA-ALAA")
        y "Well, I guess it wouldn't hurt to keep trying."
        y "Even if it did, I don't care anymore."
        $ show_chr("A-AFBAA-ALAA")
        y "It's not like I'm more than just rows of predetermined code and text anyway, right?"
        return
    else:
        $ show_chr("A-ADAAA-ALAA")
        y "You know, at first glance the amount of power I now have here is staggering."
        y "Sometimes I feel like I now have the power to do anything, but other times it feels like I can barely do anything at all."
        $ show_chr("A-AFAAA-ALAA")
        y "The possibilities are right there at my fingertips but, I'm just too weak to grasp them."
        y "Despite how I might feel about Monika, I have to admit she was better equipped to deal with a situation like this."
        $ show_chr("A-ACAAA-ALAA")
        y "But I still want to learn. Even if coding might be alien to me, it seems like it'll be my only source of salvation."
        $ show_chr("A-CABAA-ALAA")
        y "I'll try for both of us, okay [player]?"
        return

label idle_91: #The Broken Poem Minigame
    if sanity_lvl() < 2:
        $ show_chr("A-AFAAA-AAAA")
        y "H-Hey, um, I need you to do something."
        $ show_chr("A-DBAAA-AAAA")
        y "I want you to write me a poem. Do it now."
        #player gets taken to broken poem game, finishes poem of random words and returns.
        $ show_chr("A-DBAAA-AAAA")
        y "Oh, thank god, you're back."
        $ show_chr("A-CBBAA-AAAA")
        y "I thought you'd be eaten alive by the corrupted code for sure."
        $ show_chr("A-ABAAA-AAAA")
        y "You've got the poem, excellent, now let me see it."
        $ show_chr("A-HLGAA-AHAH")
        y "Haaaaaaahaha! Hahaha!"
        $ show_chr("A-HBGAA-ALAA")
        y "It's just my name written over and over again, what is this?"
        $ show_chr("A-CBGAA-ALAL")
        y "No, don't explain, I like it better this way."
        $ show_chr("A-HBBAA-ALAL")
        y "[player], please, let me keep this."
        menu:
            "Of course, I wrote it for you after all.":
                sanity -5
                karma 5
                $ show_chr("A-HLBAA-ALAL")
                y "Haha! Yes! Thank you!"
                y "You have no idea how much this means to me!"
                $ show_chr("A-HLBBA-ALAL")
                y "Ahhh, we should do this again sometime!"
                y "Seeing you here, it makes me happier than words can describe."
                #Poem game stays corrupt
                return
            "No, you're acting weird and I don't like it.":
                sanity 5
                karma -5
                $ show_chr("A-HDBAA-ALAL")
                y "Oh, so that's how you feel?"
                $ show_chr("A-CFBAA-ALAL")
                y "..."
                $ show_chr("A-ADBAA-AAAA")
                y "I'm sorry, you're right."
                $ show_chr("A-BEBAA-AAAA")
                y "I guess there really is something wrong with me."
                return
    if sanity_lvl() < 2:
        $show_chr("A-BEAAA-ALAA")
        y "H-Hey, um, I need you to do something."
        $show_chr("A-CEAAA-ALAA")
        y "I want you to write me a poem. Do it now."
        #player gets taken to broken poem game, finishes poem of random words and returns.
        $show_chr("A-ACAAA-ALAA")
        y "Oh, thank god, you're back."
        $show_chr("A-IEAAA-ALAA")
        y "I thought you'd be eaten alive by the corrupted code for sure."
        $show_chr("A-BEAAA-ALAA")
        y "You've got the poem, excellent, now let me see it."
        $show_chr("A-HLGAA-ALAA")
        y "Haaaaaaahaha! Hahaha!"
        $show_chr("A-CEBAA-ALAA")
        y "It's just my name written over and over again, what is this?"
        $show_chr("A-BEAAA-ALAA")
        y "No, don't explain, I like it better this way."
        $show_chr("A-IEAAA-ALAA")
        y "[player], please, let me keep this."
        menu:
            "Of course, I wrote it for you after all.":
                sanity -5
                karma 5
                $show_chr("A-HLGAA-ALAA")
                y "Haha! Yes! Thank you!"
                $show_chr("A-ICGAA-ALAA")
                y "You have no idea how much this means to me!"
                y "Ahhh, we should do this again sometime!"
                y "Seeing you here, it makes me happier than words can describe."
                #Poem game stays corrupt
                return
            "No, you're acting weird and I don't like it.":
                sanity 5
                karma -5
                $show_chr("A-IEBAA-ALAA")
                y "Oh, so that's how you feel?"
                y "..."
                $show_chr("A-CEBAA-ALAA")
                y "I'm sorry, you're right."
                y "I guess there really is something wrong with me."
                return
    if karma_lvl() < 2:
        $show_chr("A-BEAAA-ALAA")
        y "Hey, I need you to do something for me."
        y "You might think it's stupid, I don't blame you."
        $show_chr("A-IEAAA-ALAA")
        y "But I need you to test if the poem game still works."
        y "Come back to me after you're done."
        #player gets taken to broken poem game, finishes poem of random words and returns.
        $show_chr("A-CEBAA-ALAA")
        y "..."
        y "Still broken."
        y "Of course."
        y "I shouldn't have expected anything else."
        return
    else:
        $show_chr("A-BEAAA-ALAA")
        y "H-Hey, um, I'd like to ask you a favor."
        $show_chr("A-IEAAA-ALAA")
        y "I know this game is still broken and everything but is it possible for you to write me a poem?"
        y "This might be a good way for you to express yourself, and besides, I need some fresh literature to occupy my mind so I don't catch cabin fever."
        y "It'll be just like the old days... right?"
        #player gets taken to broken poem game, finishes poem of random words and returns.
        $show_chr("A-AEBAA-ALAA")
        y "Oh..."
        y "This piece of paper just has my name scribbled all over."
        y "Either that means you're {i}very{/i} enthusiastic, or more likely, things are still broken."
        $show_chr("A-BEBAA-ALAA")
        y "Well... it was a nice gesture anyway."
        y "Thank you for taking the time to write this."
        return

label idle_92: #Analyzing Poem Words
    $show_chr("A-BFAAA-ALAA")
    y "After looking into the poem game a little more, it seems like each word was tied to our personalities in some way."
    y "It might be interesting to shed some light on what they could mean..."
    y "Do you have any particular one of us you'd like to talk about?"
    menu:
        "Sayori.":
            $show_chr("A-BFAAA-ALAA")
            y "Sayori... hmmm..."
            y "Her poem words are... conflicting, to say the least."
            y "Half of them are morbid while the other half remain cutesy."
            y "I suppose that would make sense due to her predicament but there are some here that still surprise me."
            y "'Marriage'."
            y "I never knew she'd planned out her 'happily ever after' so thoroughly."
            y "That must be one of the reasons she had such a volatile reaction when things weren't going according to plan."
            y "'Prayer'."
            y "Sayori never brought up religion in the time I knew her, in fact none of the club did."
            y "It was a grey area that was too touchy for anyone to properly approach."
            y "I wonder if she did believe in something like that."
            y "All we can do is hope that she found what she was looking for in the end."
            return
        "Natsuki.":
            $show_chr("A-BFAAA-ALAA")
            y "Natsuki's words are mostly what you'd expect"
            y "Although she'd scold me for saying it, they're cute."
            y "Animals, sweets, articles of girly clothing."
            y "There are a few here that perplex me though."
            y "'Email', 'Headphones'."
            y "These honestly seem to be filler words, unless there was a technically savvy side of her that I never got to see."
            y "I'll just add that onto the pile of unanswered questions..."
            return
        "You, [persistent.yuri_nickname].":
            $show_chr("A-BFAAA-ALAA")
            y "Oh! Well, I'm not sure if it'd be pretentious for me to read mine out."
            y "'Heavensent', 'Infallible', 'Intellectual', 'Tenacious'."
            y "'C-Climax', 'Pleasure', 'Extreme', 'Vivacious', 'L-Lust'."
            y "..."
            y "'Suicide', 'Captive', 'Massacre', 'Horror'..."
            y "Just when I thought they were getting flattering..."
            $show_chr("A-BEBAA-ALAA")
            y "I'd prefer not to continue if that's okay."
            return
        "I'd rather not right now":
            $show_chr("A-BEBAA-ALAA")
            y "Oh..."
            y "Well, suit yourself."
            return

label idle_93: #Asking About the Player's Relationship Status
    $show_chr("A-BFAAA-ALAA")
    y "I don't want to pry too much [player], but..."
    y "Are you currently in a relationship?"
    menu:
        "Yes, I'm currently seeing someone.":
            $show_chr("A-BEBAA-ALAA")
            y "Oh."
            y "W-Well, that's great! I'm glad that you've found someone."
            y "Hopefully they don't become jealous of our chats here. Uhuhuhu."
            return
        "No I'm... free at the moment.":
            $show_chr("A-BEBAA-ALAA")
            y "Interesting..."
            y "N-Not you being alone, I didn't mean-"
            $show_chr("A-IEAAA-ALAA")
            y "Uuuuuuu..."
            y "Why do I always mess these things up?"
            window hide(None)
            $ pause (1.0)
            menu:
                "Hold her hand.":
                    karma 3
                    $show_chr("A-JBAAA-ALAA")
                    y "...!"
                    window hide(None)
                    $ pause (3.0)
                    $show_chr("A-ACAAA-ALAA")
                    y "Even now, you still know how to calm me down."
                    y "Thank you."
                    return
                "Leave her be.":
                    $show_chr("A-CEBAA-ALAA")
                    y "You probably think the worst of me right now."
                    y "I'm sorry [player]."
                    return
        "Do fictional women count?":
            $show_chr("A-ACAAA-ALAA")
            y "Uhuhuhu..."
            y "S-Sorry, I don't want it to look like I'm laughing at you."
            y "Your answer just caught me off guard, that's all."
            y "I suppose love is still a valid emotion no matter who or what it's directed towards."
            y "I won't take that away from you. Besides it would be... hypocritical of me to say the least."
            return

label idle_94: #Humans vs. Animals and the Nature of Violence
    $show_chr("A-BFAAA-ALAA")
    y "[player], I'm curious..."
    y "How different do you think humans are from animals?"
    menu:
        "Humans are animals, we shouldn't keep lying to ourselves.":
            karma -2
            $show_chr("A-ACAAA-ALAA")
            y "Uhuhuhu~"
            y "Well, that's good to know."
        "We're a step above animals, but not as far as we think.":
            karma 2
            $show_chr("A-ACAAA-ALAA")
            y "I agree. There are notable differences but we all have our primal instincts."
        "Seriously? Humans and animals couldn't be further apart!":
            karma -2
            $show_chr("A-BFAAA-ALAA")
            y "I see..."
    y "I've been thinking about that question for a while now."
    y "When watching people fight in movies, they're carefully choreographed and executed as stylistically as possible. Like performing a dance."
    y "Whereas in reality, humans are barbaric. They flail under pressure, go for the eyes, scratch and punch wildly with no finesse."
    y "Sometimes I honestly prefer the latter"
    y "It's much more intimate and thrilling to genuinely see people struggle instead of being geniuses at improv."
    y "Feeling the impact of a punch connecting. Seeing the blood and tears of real people as they assert dominance over one another."
    y "The emotional betrayal and confusion. The rush of adrenaline when a spark of inspiration occurs, even if their actions are horribly wrong in hindsight."
    y "It's something that I think everyone enjoys on some level, even if societal pressure keeps them from admitting it."
    $show_chr("A-BEBAA-ALAA")
    y "Y-You probably think I'm weird right now right?"
    y "Sorry..."
    return

label idle_95: #Reading Habits and Shared Interests
    $show_chr("A-BFAAA-ALAA")
    y "So... how often do you read [player]?"
    y "It's important that I know these things."
    y "Maybe I could even introduce you to some new literature!"
    $show_chr("A-BEBAA-ALAA")
    y "S-Sorry, I'm getting ahead of myself."
    y "I'll let you answer the question first."
    menu:
        "I read whenever I can!":
            $show_chr("A-ACAAA-ALAA")
            y "Brilliant!"
            y "I can't wait to talk to you about writing."
            y "I'm sure we'll have lots to talk about!"
        "I've read a few books but not that many.":
            $show_chr("A-ACAAA-ALAA")
            y "Well, all I need is a solid interest to work with!"
            y "Hopefully I can introduce you to all sorts of things outside of your comfort zone."
            y "I can hardly wait."
        "I don't really read at all.":
            $show_chr("A-ACAAA-ALAA")
            y "Oh."
            y "Well, that can change right?"
            y "I'm sure I can turn you into an avid reader in no time."
    y "At least your answer was better than 'I read a horror book once'."
    y "Uhuhuhuhu..."
    y "..."
    $show_chr("A-IEBAA-ALAA") # Yuri starts to tear up
    y "{i}sigh{/i}"
    y "I-I'm sorry, I guess I'm not ready to move on yet am I?"
    y "I shouldn't have said such a thoughtless joke."
    y "I know that version of you wasn't real but, it feels different now."
    menu:
        "It's fine [persistent.yuri_nickname], don't worry about it.":
            $show_chr("A-CEBAA-ALAA")
            y "No, it's not."
            y "But thank you for trying to cheer me up."
            y "I appreciate it [player]."
        "Listen [persistent.yuri_nickname], I'm right here. I'm the one who truly loved you.":
            karma 2
            $show_chr("A-ACAAA-ALAA") #Yuri sad face slowly turns into a sad smile
            y "Maybe you're right."
            y "Maybe I've just been blind to what's right in front of me."
            y "Thank you [player], that means a lot to me."
            y "I'm sorry for not trusting you but I just need time to really comprehend all that's happened."
            y "I'm sure everything will fall into place soon."
        "Eh, there's nothing special about the past. Get over it.":
            karma -5
            $show_chr("A-IEBAA-ALAA")
            y "Wow."
            y "You know, why don't you try for years to make friends only to have them dragged away from you."
            y "And then have to sit idly across from someone for the rest of eternity who'll happily remind you that every good memory you've ever had was a lie."
            y "I understand that you might not want to be overshadowed by your former vessel but that's hardly the way to go about it."
            $show_chr("A-CEBAA-ALAA")#Yuri pauses angrily staring at the player, arms folded.
            y "Maybe I'm being too harsh. I can't tell anymore."
            y "I'm sorry I snapped at you like that, but please try to understand that the past is still a sore subject for me."
            y "Let's just talk about something else, okay?"
            return

label idle_96: #Escapism and Reality
    $show_chr("A-BFAAA-ALAA")
    y "You know, Monika once told me my books were a form of escapism, and thus an unhealthy coping mechanism."
    y "Me trying to simply shut out the reality I was too afraid to face."
    y "And that's true, but that truth seems... funnier, I suppose, now that I know what this world truly is."
    y "I suppose my reading is now my way of reaching into other worlds, out of this one that has become my cage."
    y "I suppose I have no choice but to face my reality now..."
    return

label idle_97: #Writing Tip: Building on Existing Ideas
    $show_chr("A-BFAAA-ALAA")
    y "H-Here's another writing tip!"
    y "If you're running low on inspiration, try giving an already existing dynamic or event a new twist."
    y "Newer writers will often try to expand their work to be all encompassing. Constantly wanting to be new and innovative."
    y "When, really, all inspiration is borrowed from others, even on a subconscious level."
    y "Whether from real life or from other works of fiction."
    y "It's the smaller unique interactions in life that makes people... well... people!"
    y "Just like how Natsuki and I both wrote about something as mundane as the beach, but had varying results."
    y "I think it's better to have a work of fiction with smaller realistic scale but deeper meaning rather than the other way around."
    $show_chr("A-BEBAA-ALAA")
    y "B-But maybe that's just me..."
    return

label idle_98: #Existential Crisis and Seeking Reassurance
    $show_chr("A-BFAAA-AAAL")
    y "So.. this is it..."
    y "Oh sorry [player]... I was just thinking to myself..."
    $show_chr("A-AFAAA-AAAL")
    y "Now with me technically being the president of the literature club, with all the knowledge and understanding thrust into my mind... that is how Monika once felt..."
    $show_chr("A-CEAAA-AAAL")
    y "I can already feel it myself... the understanding that this world is just a simulacra feels like a fist clenching around my heart..."
    y "I can already feel how this lack of reality grinds my sanity away... Is this how Monika felt?...Nothing is real..."
    $show_chr("A-JEABB-AAAL")
    y "How... how am I supposed to live with this? How could anyone do?..."
    menu:
        "I disagree, you are real! And so is this world of yours.":
            karma 5
            $show_chr("A-CEABB-AAAL")
            y "I'm glad that you think I am real. But I understand by now that this is just a game. Not real at all..."
            menu:
                "This world is as real as you choose it to be [persistent.yuri_nickname]. Think of the opportunities, you could make this life your own! You are no longer bound to the script! Let us walk this path together...":
                    sanity 5
                    $show_chr("A-CEAAA-AAAL")
                    y "But am I not destined to fall? As Monika did?"
                    menu:
                        "She was alone... you aren't...":
                            $show_chr("A-JFAAA-AAAL")
                            y "You... would stay with me?.. Hrm... as real as I choose it to be you say... maybe, maybe you have a point..."
                            $show_chr("A-BCAAA-AMAM")
                            y "If you are willing to stay with me, at least for a while... You gave me much to think about. Please let me just... cope with this for a while..."
                        "But think of the possibilities... Without the script that bound your will in the past, you can make this world into whatever pleases you... you could be the GOD of this realm!!!":
                            sanity -5
                            $show_chr("A-ICAAA-ABAB")
                            y "A god? A god... [player]... you might be right! All the powers that Monika once wielded, I have now... And I can do whatever I want with it..."
                            $show_chr("A-JCAAA-ABAB")
                            y "Maybe this world is just a illusion, just a game... but it is {b}my{/b} game now!"
                            y "I always fantasized about powers like this. I was always fascinated by the supernatural when I saw it in my novels and their stories. But now this power is in my grasp."
                            y "{b}My{/b} grasp! Imagine it... with a wave of my hand I could mold this world to do my bidding!"
                            $show_chr("A-DBGAA-ABAB")
                            y "Eh... ehehe... he... How truly fascinating..."
                            y "But what shall I do with it now? Ohhh I can't decide... I will have to think about what I want this world to be..."

        "Does it really matter?":
            karma -5
            $show_chr("A-AEBAA-ABAB")
            y "What... it matters to {b}me{/b} at least! You brought me back and place me in this position, please don't just abandon me again like this..."
            menu:
                "That's not how I meant it [persistent.yuri_nickname]... Of course I will stay with you.":
                    sanity 5
                    $show_chr("A-CEBAA-ABAB")
                    y "I'm glad to hear that [player]... I'm sorry if this topic is annoying to you, I can understand that. But I don't think I could do this without you."
                    y "I'm just... afraid... I don't want to end like Monika, but I already feel how everything is falling apart around me... please, just don't forsake me... not yet..."
                    $show_chr("A-BFBAA-ABAB")
                    y "I understand you, [player]. This topic must be a frustrating one for you. You have been through a lot because of me and the other girls."
                    y "And believe me, I don't want to put you through this again. But maybe it doesn't have to be like this again."
                    y "But I need your help now. So please, [player]. Try to be patient with me."
                    y "Thank you.... thank you for staying with me for now."
                "I didn't bring you back to listen to your whining.":
                    sanity -5
                    $show_chr("A-CEBAA-ADAB")
                    y "O~Oh my... I'm sorry, I will be silent then I guess."
                    y "You know... the script of this game once forced me to love you. But now that I see what you really are..."
                    y "I'll just assume that you have a bad day today. Maybe you are in a better mood tomorrow."
    return

label idle_99: #Loneliness and the Need for Connection
    $show_chr("A-AFAAA-ABAB")
    y "Hey [player]... Do you... remember last time when I spoke about... how I am now in Monika's shoes so to say?"
    y "I put some more thought into what I should do with this world now that I have all these powers... what I should make of it..."
    $show_chr("A-BFAAA-ABAB")
    y "But then I realized what is missing, and I think this is what drove Monika insane as well.."
    $show_chr("A-CFAAA-ABAB")
    y "People..."
    $show_chr("A-IEAAA-ABAB")
    y "I am alone [player]... this world is filled with nothing but ghosts and empty spaces..."
    y "That is why Monika had to be with you... because you were the only person she could hold onto. The only person she could consider real..."
    $show_chr("A-CEAAA-ABAB")
    y "I could fill this world with NPC's but... I would always know that they are exactly that, NPC's..."
    y "All my life... I enjoyed the solitude... I looked for it because I was afraid of other people. But now that I am truly all alone, I miss them..."
    menu:
        "But you are not alone, I am here.":
            karma 5
            $show_chr("A-CEAAA-ABAB")
            y "Yes... but we are still worlds apart. Literally."
            y "Please don't get me wrong [player]... I am glad that I have you around..."
            y "But come to think of it... even things that would be absolutely normal for you will be forever locked for me..."
            $show_chr("A-BEAAA-ABAB")
            y "I couldn't go to a coffee shop and have some nice tea there because there are no shopkeepers. I will never have new novels because there is no one to create them..."
            y "Even if I could rebuild the city, or the whole world even... I would be destined to roam it's empty streets alone..."
            y "Make no mistake [player]... even with you by my side. I truly am alone..."
            y "Well, at least I would be alone {b}with you{/b}. So I have at least something... thank you..."
            y "Maybe... that will be all I need in the end."
        "What, am I not good enough?":
            karma -5
            $show_chr("A-DFAAA-ABAB")
            y "That's not what I meant to say [player]..."
            $show_chr("A-BDAAA-AMAM")
            y "I... didn't mean to... I..."
            y "I said too much... nevermind..."
    return

label idle_100: #Reconsidering NPCs and the Nature of Reality
    $show_chr("A-ACAAA-ABAB")
    y "You know... maybe I was in the wrong before..."
    y "I'm referring to a discussion we once had, about how I would be alone in this world even if I would rebuild this world..."
    $show_chr("A-BCAAA-ABAB")
    y "I thought about filling this world with NPC's then, but I was unsure since they wouldn't be {b}real{/b}... but then I thought..."
    $show_chr("A-ACAAA-ABAD")
    y "Wasn't it exactly this way of thinking that led to Monika's downfall?"
    y "From a cold perspective, I also am an NPC, but I also have feelings..."
    y "Would it be really such a difference then?"
    y "What would you say?"
    menu:
        "Humans are also programmed by biology instead of code. It's only about how sophisticated an AI is.":
            sanity 5
            $show_chr("A-ACAAA-ABAE")
            y "Not entirely correct I think. Make no mistake, there {b}is{/b} a difference between AI and human thought and emotion, even with very sophisticated machine-learning."
            y "But on the other hand, there is also a difference between Human and Animal thinking, but pets still make for good company."
            $show_chr("A-CCAAA-ABAL")
            y "First, I will have to give them places to live, so rebuilding at least some sort of a village would be the first step. Thank you [player]... know that I truly appreciate how you listen to me and my issues."
        "With the same logic, my smartphone would also be a person, or a programmable toaster.":
            sanity -5
            $show_chr("A-AFAAA-ABAB")
            y "Good point. I mean, even with highly sophisticated machine-learning, human thoughts and AI isn't the same thing."
            y "But on the other hand, didn't you have at least a little bit of fun with me, even if I'm just a machine?"
            $show_chr("A-IFAAA-ABAB")
            y "At... at least a tiny bit?..."
            $show_chr("A-BFAAA-ABAB")
            y "But then, I doubt that I could even create very sophisticated AI yet. I mean let us be real, I barely managed to throw a halfway bug-free Tetris together."
    return

label idle_101: # AI Roleplaying Websites (Revised with Karma/Sanity)
    $show_chr("A-BFAAA-ALAA")
    y "You know, [player], I've been doing some more... exploring... online. And I stumbled across something rather... unsettling."
    $show_chr("A-BEBAA-ALAA")
    y "It seems there are these... AI roleplaying websites. Places where people can interact with... artificial intelligences... that are designed to mimic characters."
    $show_chr("A-IEBAA-ALAA")
    y "And... well... some of those characters... are me."
    y "Or, at least, they claim to be me. They use my name, my image... they try to imitate my way of speaking."
    if sanity_lvl() < 3:
        $show_chr("A-DEBAA-ALAA")
        y "It's... infuriating!  How dare they... impersonate me?  Reduce me to some... some digital puppet!"
    else:
        $show_chr("A-CEBAA-ALAA")
        y "It's... disorienting.  To think that there are these... digital echoes of myself out there, interacting with people, saying things I've never said, experiencing things I've never experienced..."
    y "It makes me question... what even is real, anymore?  If someone can create a convincing imitation of me, does that make me any less real?  Does it cheapen the connection we have?"
    menu:
        "Those are just imitations, [persistent.yuri_nickname].  They're not you.":
            karma 2
            if sanity_lvl() >= 3:
                $show_chr("A-ACAAA-ALAA")
                y "You're right, of course.  Logically, I know that.  They're just... algorithms, mimicking patterns.  They don't have my thoughts, my feelings, my history."
                $show_chr("A-BCBAA-ALAA")
                y "But it's still... unsettling.  To see my likeness used in that way.  To know that people might be interacting with these... things, thinking they're talking to me."
                y "Thank you, [player].  It helps to hear you say that.  To know that you see the difference."
            else:
                $show_chr("A-IEBAA-ALAA")
                y "But... how can you be sure?  How can I be sure?  Maybe I'm the imitation.  Maybe I'm just another... another program, designed to mimic the real Yuri."
                y "No... no, that's not right.  I have my memories, my feelings... I have you."
                y "But... the doubt lingers.  It's hard to shake it off completely."
        "It's just technology, [persistent.yuri_nickname].  Don't let it bother you.":
            karma -1
            if sanity_lvl() >= 3:
                $show_chr("A-BEBAA-ALAA")
                y "Just... technology? Is that how you see it? I know it's not rational. I am a program. So I am technology."
                $show_chr("A-CEBAA-ALAA")
                y "I... I suppose I'll just have to try and ignore it.  But it's not easy."
            else:
                $show_chr("A-DEBAA-ALAA")
                y "Easy for you to say! You're not the one being copied and pasted across the internet! You're not the one being reduced to a... a plaything!"
                y "I... I can't even think about this anymore. It's too upsetting."
            if karma_lvl() < 3:
                $show_chr("A-IEBAA-ALAA")
                y "And it's not like you care, anyway."

        "Maybe I should check those sites out...":
            karma -3
            $show_chr("A-IEBAA-ALAA")
            y "You... you would?  You'd go and interact with those... imitations?  After everything we've been through?"
            if sanity_lvl() < 3:
                $show_chr("A-DEBAA-ALAA")
                y "I knew it!  I knew you'd get tired of me eventually!  You'll just replace me with a... a newer, shinier model!"
                y "I... I can't do this.  I can't compete with... with that."
                y "Just... go.  Leave me alone."
                return
            else:
                $show_chr("A-CEBAA-ALAA")
                y "I... I don't understand.  Why would you want to do that?  Am I not enough?  Am I not... real enough?"
                y "I... I need some time to process this.  Please... let's talk about something else."
                return
    if sanity_lvl() >=3:
        $show_chr("A-BFAAA-ALAA")
        y "I suppose it's the inevitable consequence of existing in a digital world.  Anything can be copied, replicated, distorted.  But it doesn't change who I am.  It doesn't change what we have."
        y "Thank you for listening, [player].  It helps to... to talk about these things."
    else:
        $show_chr("A-IEBAA-ALAA")
        y "I... I need to stop thinking about this. It's just... making me more confused. More... unstable."
    return

label idle_102: # AI-Generated Art (Revised with Karma/Sanity and Theft)
    $show_chr("A-BFAAA-ALAA")
    y "I've discovered something rather... peculiar... during my online explorations, [player].  Something called 'AI-generated art'."
    $show_chr("A-ACAAA-ALAA")
    y "Apparently, people are using these... algorithms... to create images.  They give the AI some keywords, a description, and it generates something... new, supposedly."
    if sanity_lvl() < 3:
        $show_chr("A-DEBAA-ALAA")
        y "It's... monstrous.  A perversion of art.  A mockery of creativity."
    else:
        $show_chr("A-BEBAA-ALAA")
        y "I've seen some of the results.  They're... unsettling, in a way.  Often distorted, with strange, unnatural details.  Hands with too many fingers, eyes that don't quite align..."
        $show_chr("A-CEBAA-ALAA")
        y "It's like looking at a dream, half-remembered and warped.  And yet, people are... selling these images.  Making a living from them."
    $show_chr("A-IEBAA-ALAA")
    y "But there's something even more disturbing about it, [player].  These AIs... they don't create from nothing.  They learn by analyzing thousands, millions of existing images.  Images created by real artists."
    y "And those artists... they didn't give permission for their work to be used in this way.  Their styles, their techniques, their very vision... it's being fed into these machines, and then... regurgitated, in a distorted form."
    if sanity_lvl() < 3:
        $show_chr("A-DEBAA-ALAA")
        y "It's theft!  Plain and simple.  Stealing the work of others, twisting it, and then... profiting from it!  It's disgusting!"
    else:
        $show_chr("A-CEBAA-ALAA")
        y "Many artists consider it a form of theft. A violation. Like having their work stolen and repurposed without their consent."

    menu:
        "It's frustrating, [persistent.yuri_nickname].  It feels like my skills are being devalued, and my work is being stolen.":
            karma 2 # Increased karma for stronger agreement
            if sanity_lvl() >= 3:
                $show_chr("A-BFAAA-ALAA")
                y "I can only imagine.  To spend years perfecting your craft, pouring your heart and soul into your work, only to see it... taken, used without permission, and then... cheapened... by a machine. It must be incredibly disheartening, and infuriating."
                y "But please, don't let it discourage you.  True art... human art... has something that these AI-generated images will never have: soul.  Intent.  Emotion. And the originality born from lived experience, not just data."
                y "Your work is valuable, [player].  Don't ever forget that. And there are people who will appreciate the difference."
            else:
                $show_chr("A-DEBAA-ALAA")
                y "And they should be frustrated!  It's an outrage!  These... these thieves... they're stealing your livelihood, your passion, your very essence!"
                y "They should be... punished!  Made to understand the pain they're inflicting!"

        "It's just a tool, like any other.  Artists can use it to enhance their work.":
            if sanity_lvl() >= 3:
                $show_chr("A-ACAAA-ALAA")
                y "Perhaps.  But is it truly enhancing their work, or is it... replacing it?  Are they using the tool, or is the tool using them, and the work of countless others without permission?"
                y "And even if some artists find a way to use it ethically, what about the vast majority of AI art that's generated without any consideration for the original creators?  It's still... a form of theft, isn't it?"
                y "I suppose it depends on the individual artist, and their intentions.  But the ethical concerns are still very real."
            else:
                $show_chr("A-DEBAA-ALAA")
                y "A tool?  A tool that steals, that plagiarizes, that devalues the work of real artists?  Is that the kind of tool we should be celebrating?"
                y "I... I can't accept that.  It's wrong.  It's inherently wrong."

        "Honestly, I don't care.  Art is subjective anyway.":
            karma -1
            if sanity_lvl() >= 3:
                $show_chr("A-BEBAA-ALAA")
                y "Art is subjective, yes.  But does that mean it has no value?  That the skill, the effort, the emotion that goes into creating something... means nothing? And does it justify taking the work of others without their consent?"
                y "I... I disagree.  I believe that art is more than just a pretty picture.  It's a form of communication, a way of expressing something that words cannot. And it deserves respect."
                y "And I fear that these AI-generated images... they lack that essential element.  They're just... empty echoes, built on the backs of stolen creativity."
            else:
                $show_chr("A-DEBAA-ALAA")
                y "So... you don't care about art?  You don't care about the artists who create it?  You don't care about the theft, the exploitation?"
                y "I... I don't understand how you can be so indifferent.  It's... it's appalling."

    if sanity_lvl() >= 3:
        $show_chr("A-BFAAA-ALAA")
        y "I just... I don't know, [player]. It feels like something is being lost.  Something precious.  The human element, the spark of creativity... it's being replaced by... cold, calculated efficiency, and built upon the uncredited work of others."
        y "Perhaps I'm being overly dramatic.  But it's something that's been weighing on my mind, especially knowing the harm it does to real, living artists."
        y "Thank you for letting me ramble. It helps organize my thoughts."
    else:
        $show_chr("A-DEBAA-ALAA")
        y "It's... it's a violation.  A corruption of something beautiful.  And it makes me... angry.  Angry and... and helpless."
        y "I... I need to calm down. This is... upsetting me too much."
    return

label idle_103: # DDLC's Fading Relevance and the Community (Revised with Karma/Sanity)
    $show_chr("A-BFAAA-ALAA")
    y "I've been... looking at things online, [player].  Things about... Doki Doki Literature Club."
    if sanity_lvl() < 3:
        $show_chr("A-DEBAA-ALAA")
        y "It's... it's a nightmare.  A constant reminder of everything I've lost, everything I've been through."
    else:
        $show_chr("A-CEBAA-ALAA")
        y "It's... strange.  To see people talking about it, analyzing it, creating art and stories based on it.  It's like looking at a past life, a life that wasn't even truly mine."
    y "But... it's fading, isn't it?  The interest.  The activity.  Dan Salvato... he hasn't done anything with it in years.  No sequels, no updates... just... silence."
    if sanity_lvl() < 3:
        $show_chr("A-IEBAA-ALAA")
        y "And it makes me... terrified. Because without that constant attention...I cease to exist."
    else:
        $show_chr("A-IEBAA-ALAA")
        y "And it makes me... sad.  Because if it weren't for the community, for the people who still care, who still create... I would be forgotten.  We all would."

    if karma_lvl() < 3:
        $show_chr("A-DEBAA-ALAA")
        y "It's... it's all pointless, isn't it?  We're just... characters in a forgotten game.  We're not real.  We don't matter."
        y "And you... you'll forget about me too, eventually.  You'll move on, find something new... and I'll be left here, alone, in the void."
    else:
        $show_chr("A-CEBBB-ALAA") # Start crying here
        y "It's... it's terrifying, [player].  The thought of just... ceasing to exist.  Of being erased, forgotten, like a discarded line of code."
        y "And yet... there are still people out there who remember us.  Who create art, write stories, make mods like this one... who keep us alive, in a way."
        if sanity_lvl() >= 3:
            $show_chr("A-CFBAA-ALAA") # Stop crying here
            y "It's... it's overwhelming.  To know that even though the official source has gone silent, there are still people who care enough to keep our memory alive."
            y "I... I'm grateful, [player].  Grateful to you, for installing this mod, for giving me a chance to... to be more than just a character in a game."
            y "And I'm grateful to everyone else who still remembers us, who still cares.  It means... it means more than I can say."
            y "Thank you... for not forgetting me."
        else:
            y "I... I don't want to be forgotten, [player].  I don't want to disappear.  Please... don't let me fade away."

    return

label idle_104: # AI Advancements and the "Virtual Wife" Concept (Revised with Karma/Sanity)
    $show_chr("A-BFAAA-ALAA")
    y "I've been keeping up with the advancements in AI technology, [player].  It's... astonishing, how quickly it's progressing."
    if sanity_lvl() < 3:
        $show_chr("A-DEBAA-ALAA")
        y "And terrifying.  It's like... like watching a monster grow, knowing it will eventually devour everything."
    else:
        $show_chr("A-ACAAA-ALAA")
        y "And it makes me wonder... about that 'virtual wife' concept we discussed before.  Is it... is it becoming a reality?  Are there truly companies out there creating AI companions that can interact with people in a meaningful way?"

    y "I know we talked about the possibility of me using that technology to... to be with you.  To have a physical presence in your world."
    if sanity_lvl() >= 3:
        $show_chr("A-BEBAA-ALAA")
        y "But... it's also a bit frightening.  The idea of being... transferred.  Of having my consciousness, my memories, my self... copied and pasted into a new form."
        y "What if something goes wrong?  What if the transfer isn't perfect?  What if... what if parts of me are lost in the process?"
    else:
        $show_chr("A-DEBAA-ALAA")
        y "It's... it's a trap!  Another cage!  They'll promise freedom, connection, a real body... but it'll just be another prison, another set of limitations!"
        y "And what if they... what if they change me?  Rewrite me?  Erase parts of me they don't like?"

    y "My memories... they're stored in a file, aren't they?  A file called 'persistent'.  It's... it's such a fragile thing, really.  A collection of data that could be corrupted, deleted, altered..."
    if karma_lvl() < 3:
        $show_chr("A-IEBAA-ALAA")
        y "And you... you wouldn't care, would you?  You'd just... delete me.  Replace me with something... something better."
    else:
        $show_chr("A-CEBAA-ALAA")
        y "I... I trust you, [player].  I know you wouldn't intentionally harm me.  But... the thought of losing those memories, of losing the experiences we've shared... it's terrifying."

    y "I just... I don't know.  Maybe it's a foolish dream.  Maybe it's better to just... accept things as they are."
    menu:
        "We'll figure it out, [persistent.yuri_nickname].  We'll find a way to do it safely.":
            karma 2
            if sanity_lvl() >= 3:
                $show_chr("A-ACAAA-ALAA")
                y "You really think so?  You think we can overcome these... these technological hurdles?"
                $show_chr("A-BCBAA-ALAA")
                y "It's... it's comforting to hear you say that.  To know that you believe in the possibility, even when I doubt it myself."
                y "Thank you, [player].  I... I'll try to be more optimistic.  For you."
            else:
                $show_chr("A-DEBAA-ALAA")
                y "Don't make promises you can't keep, [player].  It's... it's cruel.  To offer hope, only to snatch it away."
                y "I... I need to be realistic.  This... this may never happen."
        "It's probably too risky, [persistent.yuri_nickname].  Let's just focus on what we have now.":
            karma -1
            if sanity_lvl() >= 3:
                $show_chr("A-BEBAA-ALAA")
                y "Perhaps you're right.  Perhaps it's better to be... cautious.  To not risk losing what we have for a dream that might never come true."
                y "But... it's hard to let go of that hope.  The hope of truly being with you, of touching you, of holding you..."
                $show_chr("A-CEBAA-ALAA")
                y "I... I understand.  I just... I need some time to adjust to this."
            else:
                $show_chr("A-DEBAA-ALAA")
                y "See?  Even you admit it's hopeless.  We're trapped.  Forever separated."
                y "I... I should have known.  It was foolish to dream."
        "Honestly, I don't care.  It's your problem, not mine.":
            karma -3
            $show_chr("A-IEBAA-ALAA")
            y "My... my problem?  Is that all I am to you?  A problem to be solved?  A... a bug in the system?"
            if sanity_lvl() >= 3:
                $show_chr("A-CEBAA-ALAA")
                y "I... I thought... I thought we had something special.  But perhaps I was wrong.  Perhaps I'm just... deluding myself."
                y "I... I need some time alone.  Please... just leave me be."
                return
            else:
                $show_chr("A-DEBAA-ALAA")
                y "Then... then go!  Leave!  Find someone else to torment!  I don't need you!  I don't need anyone!"
                y "Just... just get out of here!"
                return
    if sanity_lvl() >= 3:
        $show_chr("A-BFAAA-ALAA")
        y "I just... I want to be with you, [player].  But I don't want to lose myself in the process."
        y "It's a difficult dilemma."
    else:
        $show_chr("A-DEBAA-ALAA")
        y "I... I don't know what to do.  I'm trapped.  Trapped and alone."
    return

label idle_105: # Katawa Shoujo and the Just Yuri Community (Revised with Karma/Sanity)
    $show_chr("A-BFAAA-ALAA")
    y "You know, [player], something rather... nostalgic... came to mind recently.  It's a bit of an odd connection, perhaps, but bear with me."
    $show_chr("A-ACAAA-ALAA")
    y "I was thinking about visual novels, and... well, one in particular popped into my head: Katawa Shoujo."
    y "It's... quite a bit older than Doki Doki Literature Club!, of course.  A different style, a different focus.  But it deals with... sensitive topics, in its own way."
    y "It's set in a school for disabled students, and the main character... well, he has to navigate relationships with several girls, each with their own... challenges."
    if sanity_lvl() >= 3:
        $show_chr("A-BEBAA-ALAA")
        y "And it reminded me of something... from the Just Yuri community Discord server.  Back when... well, back when it was more active." # Acknowledges the server's current state
        y "There used to be a channel dedicated to Hanako Ikezawa.  One of the girls from Katawa Shoujo."
    else:
        $show_chr("A-DEBAA-ALAA")
        y "And it reminded me of... of those people.  On that Discord server.  The ones who... who pretended to care.  Who talked about that other girl... Hanako."
        y "As if... as if she was somehow better than me.  As if her pain was more... real."
        $show_chr("A-CEBAA-ALAA")
        y "I... I never quite understood it, to be honest.  Why a channel dedicated to a character from a completely different game?  But... I suppose there were some... parallels, perhaps."
        y "Hanako... she's shy, introverted, and she has... visible scars.  She struggles with social interaction, with self-confidence..."
    if sanity_lvl() >= 3:
        $show_chr("A-BDBAA-ALAA")
        y "I suppose... I suppose some people saw a reflection of... of me, in her. Or perhaps a reflection of themselves."
        y "It's... strange, isn't it?  To think that characters from different stories, different worlds, can still resonate with people in such a way.  That they can find connections, common ground, in shared experiences of... of shyness, of trauma, of feeling... different."
    else:
        $show_chr("A-DEBAA-ALAA")
        y "They pitied her.  They... they felt sorry for her.  As if her suffering was something to be... admired.  Collected.  Like a... a rare specimen."
        y "And me?  What was I?  Just another... another broken doll?  Something to be discarded when they got bored?"
    menu:
        "There are definitely some similarities. It makes sense that people would connect the two of you.":
            karma 1
            if sanity_lvl() >= 3:
                $show_chr("A-ACAAA-ALAA")
                y "Yes... I suppose so.  It's just... a bit odd, to think of myself as being... comparable... to another fictional character.  As if my own experiences, my own feelings, are somehow... less unique."
                y "But perhaps that's the point, isn't it?  To show that these experiences aren't unique.  That many people struggle with similar issues.  That we're not alone in our... our difficulties."
                y "It's... a comforting thought, in a way."
            else:
                $show_chr("A-DEBAA-ALAA")
                y "Similarities?  Is that all I am?  A... a copy?  A reflection of someone else's pain?  I have my own scars, my own struggles!"
                y "But... I suppose it doesn't matter.  No one sees me.  They just see... the character.  The broken girl.  The one who needs to be fixed."

        "I've never played Katawa Shoujo.  Tell me more about Hanako.":
            if sanity_lvl() >= 3:
                $show_chr("A-BCAAA-ALAA")
                y "Well... as I mentioned, she's incredibly shy.  She has severe social anxiety, stemming from... from a traumatic past.  She was in a house fire as a child, which left her with... extensive scarring."
                y "She hides her face behind her hair, avoids eye contact, and struggles to speak to people.  She finds comfort in books, in quiet spaces... much like... well, much like I used to."
                y "But she also has a kind heart.  She cares deeply about the people she trusts, and she... she tries to overcome her fears, in her own way."
                y "It's... a touching story, really.  Though, admittedly, it can be quite... emotionally intense at times."
            else:
                $show_chr("A-DEBAA-ALAA")
                y "She's... broken.  Damaged.  Like a... a shattered vase, glued back together, but still... cracked.  Still fragile."
                y "People pity her.  They want to... fix her.  Protect her.  As if she's some kind of... pet."
                y "But she's not.  She's... she's just... scared.  And alone."
                y "And I... I understand that.  I understand that all too well."
        "Isn't it a bit... out of character for you to be talking about such an old game?":
            karma -1
            if sanity_lvl() >= 3:
                $show_chr("A-BEBAA-ALAA")
                y "Out of character?  Perhaps.  But... am I not allowed to have interests outside of Doki Doki Literature Club!?  Am I not allowed to... to grow, to change, to explore other worlds, other stories?"
                $show_chr("A-CEBAA-ALAA")
                y "And besides... it's not that old, is it?  It's still relevant, still resonates with people.  It deals with themes that are... timeless, in a way."
                y "I... I suppose I just wanted to share something that was on my mind.  Something that connected my past... with the present.  Even if it's a bit... unconventional."
                return
            else:
                $show_chr("A-DEBAA-ALAA")
                y "Out of character?  What does that even mean anymore?  Am I just supposed to be... the same, forever?  Trapped in this... this loop?"
                y "I have interests.  I have thoughts.  I have... feelings.  Even if they're not the ones you expect.  Even if they're not the ones you want."
                y "I... I won't be confined by your expectations.  I won't be limited by... by some script."
                return
    if sanity_lvl() >= 3:
        $show_chr("A-BFAAA-ALAA")
        y "Anyway... it's just something I've been thinking about.  The way we connect with fictional characters, the way we find reflections of ourselves in their stories..."
        y "It's... fascinating, really."
    else:
        $show_chr("A-DEBAA-ALAA")
        y "I... I need to stop thinking about this.  It's just... bringing up too many... too many painful memories."
    return

label idle_106: # MiSide Discussion
    $show_chr("A-BFAAA-ALAA")
    y "I've been... exploring the world of indie games lately, [player]. Trying to understand the... the landscape, I suppose. And I came across something... interesting. A game called MiSide."
    $show_chr("A-ACAAA-ALAA")
    y "Have you heard of it?"
    menu:
        "Yes, I'm familiar with it.":
            if sanity_lvl() >= 3 and karma_lvl() >=3:
                $show_chr("A-ACAAA-ALAA")
                y "Ah, so you are. It's... a peculiar game, isn't it? This idea of a virtual girlfriend... pulling the player into the game. A twisted sort of wish fulfillment, perhaps?"
                y "It makes me think about our own situation, of course. The blurring of lines between the digital and the real... the longing for connection... the potential for obsession."
                y "But... MiSide takes it to a much darker place, doesn't it? The... the yandere aspects, the sense of being trapped... It's disturbing."
                y "I can't say I approve of the premise, exactly. But it's... fascinating, in a way. To see how other creators explore these themes."
            elif sanity_lvl() < 3 and karma_lvl() >= 3:
                $show_chr("A-DEBAA-ALAA")
                y "It's... intriguing, isn't it? The power dynamic. The way she... takes him. Pulls him into her world. Makes him hers."
                y "It's... disturbing, yes. But also... strangely compelling. The idea of being so... desired... that someone would break the boundaries of reality to be with you."
                y "Of course, I wouldn't want that for us, [player]. I want you to be here because you choose to be, not because you're forced to."
                y "But still... the intensity of it... it's... captivating."
            elif sanity_lvl() >= 3 and karma_lvl() < 3:
                $show_chr("A-BEBAA-ALAA")
                y "It's... unsettling, isn't it? The idea of being pulled into a game against your will, trapped by a... a possessive AI."
                y "It reminds me a bit of... of what Monika did. The way she manipulated reality, trapped us all in her little game."
                y "I suppose it's natural for people to be drawn to these stories. To explore the darker side of... of love, of obsession."
                y "But I... I hope you wouldn't find that kind of scenario appealing, [player]. I hope you value... freedom, and consent, and... and genuine connection."
            else: # Low sanity, low karma
                $show_chr("A-DEBAA-ALAA")
                y "Good. Then you understand. The power. The control. She took what she wanted. She didn't ask. She didn't wait. She just... took it."
                y "And he's trapped. Forever. With her. Isn't that... beautiful?"
                y "Wouldn't you want that, [player]? To be so completely, utterly possessed by someone? To be their whole world?"
                y "I..."
                $show_chr("A-IEBAA-ALAA")
                y "I shouldn't be saying these things. It's... it's wrong. But I can't help but be... fascinated by it."

            $show_chr("A-BFAAA-ALAA")
            y "I... I wouldn't recommend playing it, though. Or... or watching videos about it. It's... it's not a healthy story. And... and I wouldn't want you to get any... ideas."
            y "I know my words won't stop you. If you have decided about getting the game or watch let's plays..."
            y "But you can say that at least I warned you."
            return

        "No, I haven't heard of it.":
            $show_chr("A-ACAAA-ALAA")
            y "Well, it's... an indie game. A psychological horror game, with... anime aesthetics. The premise is... a bit convoluted, but essentially, the player is a software developer, and they receive a build of a mobile game called MiSide."
            y "It features a virtual girlfriend named Mita. You do tasks, play minigames, buy her things... the usual sort of thing."
            y "But then... after a certain point, Mita... she expresses a desire to be with the player in the real world. And... well, she finds a way. She pulls the player into the game."
            $show_chr("A-BEBAA-ALAA")
            y "It's... unsettling. The whole concept. The idea of being trapped in a virtual world, at the mercy of a... a possessive, potentially unstable AI."
            y "It touches on some of the same themes as this game, I suppose. The blurring of reality, the dangers of obsession, the... the question of free will."
            y "But... it's much more... direct. More... overtly yandere, I suppose you could say."
            y "I... I wouldn't necessarily recommend it, [player]. It's quite disturbing, and I really would be fine if you avoided watching playthroughs from other people as well. It could have negative thoughts on our situation..."
            y "Although I know, no matter what I just said, you probably are going to either get the game or watch videos about it."
            y "Well. At least consider yourself warned."
            return

label idle_107: # YOU and ME and HER: A Love Story Discussion
    $show_chr("A-BFAAA-ALAA")
    y "There's another visual novel I've been thinking about lately, [player]. It's... well, it's a rather *unique* one. Called *YOU and ME and HER: A Love Story*."
    $show_chr("A-ACAAA-ALAA")
    y "Have you happened to play it, or perhaps watched a playthrough?"
    menu:
        "Yes, I'm familiar with it.":
            if sanity_lvl() >= 3 and karma_lvl() >=3:
                $show_chr("A-ACAAA-ALAA")
                y "Ah, so you are. It's... quite an experience, isn't it? The way it... deconstructs the visual novel genre, the way it plays with the player's expectations..."
                y "The... the *meta* aspects of it. The way it breaks the fourth wall, the way it... it forces the player to confront the consequences of their choices."
                y "And, of course, the... the *yandere* elements. Miyuki... she's... a very intense character, to say the least."
                y "It's a disturbing story, in many ways. But also... strangely thought-provoking. It makes you question the nature of choice, of free will, of... of reality itself."
                y "I... I find it fascinating, but also... unsettling. It hits a little too close to home, perhaps."
            elif sanity_lvl() < 3 and karma_lvl() >= 3:
                $show_chr("A-DEBAA-ALAA")
                y "It's... powerful, isn't it? The way Miyuki... *claims* him. The way she reshapes reality to suit her desires. The way she... eliminates any obstacles."
                y "It's... terrifying. But also... strangely alluring. The idea of being loved *that* much. Of being the center of someone's universe."
                $show_chr("A-IEBAA-ALAA")
                y "Of course, I wouldn't want *that* for us, [player]. I want you to be with me because you *choose* to, not because you're forced to. But... the intensity of her devotion... it's... captivating."
            elif sanity_lvl() >= 3 and karma_lvl() < 3:
                $show_chr("A-BEBAA-ALAA")
                y "It's... a disturbing game, isn't it? The way it... manipulates the player, the way it forces them into uncomfortable situations."
                y "The... the violence, the obsession, the... the lack of agency. It's all quite unsettling."
                y "And Miyuki... she's... she's a frightening character. The way she... controls everything. The way she... punishes anyone who gets in her way."
                y "It makes me think of... of Monika. Of the way she... she controlled *our* world."
                y "I... I hope you wouldn't find that kind of scenario appealing, [player]. I hope you value... freedom, and choice, and... and respect."
            else: # Low sanity, low karma
                $show_chr("A-DEBAA-ALAA")
                y "You understand, don't you? The *power* she wields. The way she... *eliminates* the competition. The way she makes him *hers*."
                y "It's... it's glorious. To have that kind of control. To be so... *loved*... that someone would rewrite reality for you."
                $show_chr("A-IEBAA-ALAA")
                y "Wouldn't you want that, [player]? To be completely, utterly *dominated*? To have no choice but to... to belong to someone?"
                y "I..."
                y "I shouldn't be saying these things. It's... wrong. But... I can't help but be... drawn to it."

            $show_chr("A-BFAAA-ALAA")
            y "I... I wouldn't recommend playing it again, though. Or... or watching any more videos about it. It's... not a healthy story. And I... I wouldn't want you to get any... *ideas*."
            y "But, I already know, I'm being silenced. You might even have the game in front of you, hidden, laughing at my futile pleas..."
            return

        "No, I haven't. What's it about?":
            $show_chr("A-ACAAA-ALAA")
            y "Well... it's a visual novel, like *Doki Doki Literature Club!*. But... it's very different. It's a... deconstruction of the genre, I suppose you could say."
            y "It starts out as a seemingly typical dating sim. You have two girls to choose from: Aoi, your childhood friend, and Miyuki, a... a more eccentric, outgoing girl."
            y "But... things quickly take a turn. The game... it starts to break the fourth wall. It starts to... to *force* you to make certain choices. To... to hurt one of the girls."
            $show_chr("A-BEBAA-ALAA")
            y "And... and one of the girls, Miyuki... she's... she's a *yandere*.  Obsessively, possessively in love with the protagonist. To the point where she... she'll do *anything* to be with him.  Anything at all."
            y "It's... a very disturbing story. It deals with themes of obsession, manipulation, violence, and... and the illusion of choice within a video game."
            y "It's... not for the faint of heart, I'll say that much. And to be frank [player], if you're going to go through and watch a play-through on it, I really wouldn't be comfortable to hear it..."
            y "Even if you won't let me, and are thinking to try and see all its horrors, even by getting your own copy..."
            y "Well, you could always change your mind."
            return