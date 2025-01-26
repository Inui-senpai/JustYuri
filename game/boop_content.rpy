default boopable = False
#[nose, cheeks, head,]


# Boop Script, all of the guts are in here.
# Use this script to add the boop dialog.
init python:
    def getMousePosition():
        global mousex
        global mousey
        import pygame
        x, y = pygame.mouse.get_pos()
        store.mousex = x
        store.mousey = y


    class getMousePosition(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)

        def event(self, ev, x, y, st):
            import pygame

            if ev.type == pygame.MOUSEBUTTONDOWN:
                store.mousex = x
                store.mousey = y

        def render(self, width, height, st, at):
            return renpy.Render(1, 1)


    store.mousePosition = getMousePosition()


    def checkEvent():
        ui.add(mousePosition)
        return


    def BoopUpdate():
        persistent.boop_locations[0] = (float(persistent.boop_locations[0])/1.5)

    config.overlay_functions.append(checkEvent)


    def boop_init(boop_type):
        global boopable
        global loop_again
        loop_again = True
        if boopable:
            boopable = False
            DisableTalk()
            if (boop_type == "boop_nose_chibi" and persistent.costume == "_chibi") or (boop_type == "boop_nose" and persistent.costume != "_chibi"):
                renpy.call("boop_nose")
            elif renpy.has_label(boop_type):
                renpy.call(boop_type)
            EnableTalk()
        return
# This shit is from here: https://lemmasoft.renai.us/forums/viewtopic.php?t=19572

label mouse_coords:
    $ getMousePosition()
    y "[mousex],[mousey]"

#   (The nose location is around x: 642, y: 282)
#   And yes, it works regardless of window size.
    menu:
        "Again.":
            jump mouse_coords
        "Back.":
            jump control_panel

python:
    persistent.firstboop = True

label boop_nose:
    python:
        persistent.boop_locations[0] += 1
    if persistent.boop_locations[0] == 1:
        $update_memory("idle_62", "first_boop")
        $show_chr("A-DDGBA-AAAA")
        y "Ah... AHHHHH!"
        $show_chr("A-DDABA-AAAJ")
        y "W-what was that? [player]? What was that?!"
        $show_chr("A-DEBBA-AAAJ")
        y "I felt s-something touch my... my n-nose... what's going on?"
        $show_chr("A-GJDBA-AAAL")
        y "D-does this mean it works after all?"
        $show_chr("A-ICABA-AMAM")
        y "Haha... wow..."
        $show_chr("A-JCBAA-AMAM")
        y "I'm glad it works... just... p-please warn me next time, okay?..."
        $show_chr("A-ACAAA-AAAA")
    elif persistent.boop_locations[0] < 3:
        if karma() < 3:
            $show_chr("A-GEBAA-AAAA")
        elif karma() == 3:
            $show_chr("A-GJAAA-AAAA")
        elif karma() > 3:
            $show_chr("A-GIBAA-AAAA")
        y "Uuuuu... A-at least tell me before you do something like that, [player]..."
    elif persistent.boop_locations[0] < 7:
        $show_chr("A-AABBA-AAAA")
        y "...Haha... [player] Y-you seem to be enjoying this, huh? N-not that I mind or anything!"
    elif persistent.boop_locations[0] < 10:
        $show_chr("A-BCBBA-AKAA")
        y "C-could you do that again? I-if you want...that is..."
    elif persistent.boop_locations[0] < 15:
        $show_chr("A-GAGBA-AAAA")
        y "B-boop! hehe..."
    else:
        $BoopUpdate()
        #$renpy.call("save_and_quit_but_its_abrupt")
    return

label boop_cheek:
    python:
        persistent.boop_locations[1] += 1
    if karma() >= 3:
        if persistent.boop_locations[1] == 1:
            $ show_chr("A-DDGBA-AAAJ")
            y "H-Huh? [player], I just felt the strangest thing..."
            y "This... warm sensation on my cheek a moment ago, was that... you?"
            menu:
                "Yes, [persistent.yuri_nickname], I touched your cheek.":
                    $add_k(1)
                    $show_chr("A-ICABA-AAAL")
                    y "O-Oh! I see... it definitely held a feeling of familiarity, something reminiscent of your presence."
                    y "It felt... how do I put this?"
                    $show_chr("A-CCABA-ALAK")
                    y "A-as if your hand was gently caressing my skin a-and your thumb was brushing against my cheek, it set my heart aflutter when I first felt it..."
                    y "The fact you actually managed to reach out and touch me... so that I could feel it..."
                    $show_chr("A-CCABB-AMAM")
                    y "Th-Thank you [player], y-you're likely not aware of how much this means..."
                    if persistent.lovecheck:
                        y "But... if I can feel you, it means I'm one step closer to you... and I'll take a million more if I have to."
                    else:
                        y "It's nice that I got to feel your t-touch... we are a bit closer now..."
                "Huh? What are you talking about [persistent.yuri_nickname]? ... You're acting a little insane.":
                    $add_k(-1)
                    $add_s(-1)
                    $show_chr("A-AEDAA-AIAI")
                    y "I-It was just my imagination?"
                    $show_chr("A-BBBAA-AIAI")
                    y "Aha... I see..."
                    pause 0.5
                    $show_chr("A-CFBAA-AIAI")
                    y "O-of course... nevermind."
                    y "I'm sorry [player], I guess I'm just starting to lose it in here..."
        if persistent.boop_locations[1] == 2:
            $show_chr("A-CCBBA-ALAL")
            y "Mm... there it was again."
            y "D-do you remember when you held that towel against my cheek?"
            y "It feels like so long ago... but the emotions are still heavily ingrained into my mind."
            y "The roaring passion... that contact that set aflame my heart, it was at that point I was certain..."
            $show_chr("A-ECBBA-ALAD")
            y "... that you were the only one for me, my love."
        if persistent.boop_locations[1] == 3:
            $add_k(1)
            $add_s(1)
            $show_chr("A-BDBBA-ALAM")
            y "When you're gone... I will try my absolute hardest to remember this warmth."
            y "You're the thing that motivates me, that directs my every move, [player]..."
            y "If I can hold on to even a small bit of you, of these emotions you give me, I- I think I'll be alright."
            $show_chr("A-IABBA-ALAM")
            if persistent.lovecheck:
                y "I love you, [player], more than anything this world could offer."
            else:
                y "I hope we'll be together as friends... forever and always, [player]."
        if persistent.boop_locations[1] >= 4:
            if persistent.lovecheck:
                $show_chr("A-IAABA-ALAL")
                y "So warm... m-my heart is pounding for you... [player]..."
                y "Don't ever let me go..."
            else:
                $show_chr("A-BBABA-AMAM")
                y "Ahaha... you're touching my cheek again, are you?"
                y "It's fine... I enjoy it regardless, don't feel afraid to do so..."
    if karma() <= 2:
        if persistent.boop_locations[1] == 1:
            $ show_chr("A-DDGBA-AAAJ")
            y "H-Huh? [player], I just felt the strangest thing..."
            y "This... warm sensation on my cheek a moment ago, was that... you?"
            menu:
                "Yes, [persistent.yuri_nickname], I touched your cheek.":
                    $add_k(1)
                    $show_chr("A-IFAAA-AAAB")
                    y "O-Oh! I see... Would you mind... umm..."
                    $show_chr("A-JFAAA-AAAB")
                    y "Not doing that?..."
                    $show_chr("A-BFAAA-ABAB")
                    y "It's just that... feeling your hand without actually seeing it was just a bit... creepy..."
                    y "Like a ghost, or something along those lines. And the fact that I'm sitting here literally alone doesn't make it any less spooky."
                    $show_chr("A-CCABB-AMAM")
                    y "Th-Thank you for understanding, [player]..."
                "Huh? What are you talking about [persistent.yuri_nickname]? ... You're acting a little insane.":
                    $add_k(-1)
                    $add_s(-1)
                    $show_chr("A-AEDAA-AIAI")
                    y "I-It was just my imagination?"
                    $show_chr("A-BBBAA-AIAI")
                    y "Aha... I see..."
                    pause 0.5
                    $show_chr("A-CFBAA-AIAI")
                    y "O-of course... nevermind."
                    y "I'm sorry [player], I guess I'm just starting to lose it in here..."
        if persistent.boop_locations[1] == 2:
            $show_chr("A-DHGAA-ALAL")
            y "Mm... there it was again."
            $show_chr("A-JGAAA-ALAL")
            y "P-Please, it really scares me every time you do it..."
            y "Would you mind stopping that please?"
            $show_chr("A-CFAAA-AAAA")
            y "It just really throws me off."
        if persistent.boop_locations[1] == 3:
            $add_k(-1)
            $add_s(-1)
            $show_chr("A-DGGAA-AAAA")
            y "...!"
            $show_chr("A-KFCAA-AAAA")
            y "Damn it [player]... I asked you really really politely to stop that"
            y "Would you please, {b}pretty pretty please{/b} leave me alone with this nonsense now?"
            $show_chr("A-KFCAA-AAAF")
            y "I didn't mean to be rude, and I'm perfectly fine with you being around. But it's getting really annoying."
        if persistent.boop_locations[1] == 4:
            $show_chr("A-DDCAA-AAAA")
            y "{b}Okay you know what? I'm done with it! If you can't respect my wishes at least that much, I'm out of here! Bye!{/b}"
            $renpy.call("save_and_quit_but_its_abrupt")
        if persistent.boop_locations[1] >= 5:
            $show_chr("A-DDCAA-AAAA")
            y "[player] for the love of all that is holy {b}STOP TOUCHING MY DAMN CHEEK{/b}"
    $store.mousex = 0
    $store.mousey = 0
    return


label headpat:
    python:
        persistent.boop_locations[2] += 1
    if karma() >= 3:
        if persistent.boop_locations[2] == 1:
            $show_chr("A-DFABA-AAAA")
            y "W-Wait... I-I just felt something touch my head!"
            y "Was that y-you, [player]?"
            menu:
                "Yes, I wanted to try it out. I hope it didn't weird you out.":
                    $add_k(1)
                    $show_chr("A-IBGAA-ALAL")
                    y "R-Really!? Sorry for being so surprised... I-I just didn't know that you could touch me there!"
                    $show_chr("A-CAABA-AAAA")
                    y "Honestly hehe... It caught me off-guard..."
                    $show_chr("A-DDAAA-AAAL")
                    y "Oh and...ummm! You didn't weird me out, don't worry! I was as I said earlier... surprised that you just gave me a well..."
                    $show_chr("A-BAABA-AAAB")
                    y "A-a pat... yes. Thank you, It felt... nice?"
                    y "Sorry, it's just that it was the easiest way I could put it... I just never expected you to get so close to me."
                    $show_chr("A-IBABA-ALAA")
                    y "I am happy, don't get the wrong idea, [player]!"
                    if persistent.lovecheck:
                        $show_chr("A-ICABA-AAAL")
                        y "I mean... sweetheart, why wouldn't I be?"
                        $show_chr("A-CCABA-AAAD")
                        y "That split second where I actually could feel your touch... It felt so... good."
                        y "It makes me feel as If I am getting closer to you each moment which we talk... It's amazing!"
                        $show_chr("A-ICABA-AAAL")
                        y "So thank you again, my love."
                    else:
                        $show_chr("A-GCAAA-ADAB")
                        y "Each way that we can be at least a little closer is a good addition to our friendship."
                        $show_chr("A-IFAAA-AIAI")
                        y "Some people consider touch weird or strange, but I don't think so..."
                        y "Doesn't that mean that you're comfortable around that person and so allow them to be closer to you. Bypassing an earlier boundary and allowing them to enter your personal area?"
                        $show_chr("A-ICABA-AMAM")
                        y "That is how I see it at least... Still, th-thank you for this kind gesture."
                "I don't believe that was me, want me to try touching your head?":
                    $show_chr("A-BCBBA-ADAA")
                    y "Y-Yes... this feels a bit embarrassing..."
                    #Touching her head after she says ‘yes'
                    $show_chr("A-JBGAA-ALAA")
                    y "Oh! It really is you touching me!"
                    y "That sure is unexpected... I never thought that would work honestly!"
                    $show_chr("A-CCAAA-ALAA")
                    y "I don't mind it, I don't mind it at all!"
                    y "Well, we sure made a nice discovery today, [player]."
                    $show_chr("A-GCABA-ADAA")
                    y "That is one step for us to get a bit closer."
        if persistent.boop_locations[2] == 2:
            $show_chr("A-CAAAA-AAAA")
            y "Ah...well, this certainly is calming..."
            y "Just for a bit more please."
            y "..."
            $show_chr("A-ICABA-AAAA")
            y "Thank you."
        if persistent.boop_locations[2] == 3:
            $show_chr("A-BADBA-AAAA")
            y "Again?"
            $show_chr("A-GAABA-AAAK")
            y "Hehe... don't get me wrong, I like when you do it..."
            y "So don't hesitate, if you could..."
        if persistent.boop_locations[2] >= 4:
            $show_chr("A-KCBBA-AAAA")
            y "Someone seems to be enjoying this as much as me, hmm~?"
            y "Go on, you can do it for as long as you want... It's calming..."
            $show_chr("A-BBBBA-AAAL")
            y "Also reassuring..."
            if persistent.boop_locations[2] == 4:
                $show_chr("A-IBAAA-AMAM")
                y "Oh... that raises a question in my head, [player]..."
                y "Since pats are usually done when people are standing and... it's usually implied they're done to shorter people..."
                $show_chr("A-BCAAA-AAAD")
                y "How tall are you?"
                menu:
                    "I am quite tall... you could say I am above 185cm (6'1”)":
                        $show_chr("A-DDAAA-ALAA")
                        y "Oh wow... that is quite tall!"
                        y "That is pretty interesting [player]!"
                        $show_chr("A-ICABA-ADAA")
                        y "It's a good thing... you can pat me from above easily... Hehe~"
                        y "If you didn't know, I'm actually only 165cm or 5'5 feet tall!"
                        $show_chr("A-BIAAA-AAAA")
                        y "You would be quite big compared to me."
                        if persistent.lovecheck:
                            $show_chr("A-ECABA-AKAE")
                            y "That actually makes me feel a bit... dominated by you...oh, goodness..."
                            y "Y-yeah... sounds strange but trust me, I mean it in a loving way, [player], hehe..."
                            $show_chr("A-FHABA-ALAA")
                            y "I am your dear after all~"
                        else:
                            $show_chr("A-IBAAA-ALAA")
                            y "But don't worry about that!"
                            y "It means that your hugs will be big and nice!"
                            $show_chr("A-ICAAA-ALAA")
                            y "There are always positives to such things, no need to be anxious about who you are."
                            y "Just a little tip from me."
                    "I am average sized, above 170cm (5'7”)":
                        $show_chr("A-BCAAA-AAAD")
                        y "So you are a bit close to me it seems..."
                        y "I myself am 165cm or 5'5 feet tall, not very tall actually..."
                        $show_chr("A-IBAAA-AAAD")
                        y "But according to recent research, this seems to be the average height for a girl."
                        y "So I guess... I am not short nor tall compared to most people."
                    "I am average sized, above 165cm (5'5”)":
                        $show_chr("A-BCAAA-AAAD")
                        y "So you are a bit close to me it seems..."
                        y "I myself am 165cm or 5'5 feet tall, not very tall actually..."
                        $show_chr("A-IBAAA-AAAD")
                        y "But according to recent research, this seems to be the average height for a girl."
                        y "So I guess I am not short nor tall compared to most people."
                    "I am... a bit short... around or even below 150cm (4'11”)":
                            $show_chr("A-ADAAA-AMAM")
                            y "Well you don't need to be shy about that!"
                            y "You were born like that and that is entirely fine!"
                            $show_chr("A-BEAAA-ADAA")
                            y "Even if some people bully you, which I really hope they don't..."
                            y "Just don't exert too much energy into worrying about their words. There are many people that will actually see you for who you are deep down inside, and not on the outside, like me, for example..."
                            if persistent.lovecheck:
                                $show_chr("A-ICABA-AAAD")
                                y "Plus think of it like this... my hugs will be able to reach every part of you~"
                                y "They will feel better than ever, and you will get to be completely enveloped in my warmth."
                                $show_chr("A-IBABA-AAAL")
                                y "I think that this is a lovely thing, [player]!"
                                y "So let us embrace this fact and make the best out of it!" #A hug triggers.
                            else:
                                $show_chr("A-ACAAA-AAAD")
                                y "So don't worry about that, [player]."
                                $show_chr("A-CCABA-AAAE")
                                y "Look at the positive side and after all. I will see you as a nice person no matter your height."
                                y "Just, please always remember that..."
    if karma() <= 2:
        if persistent.boop_locations[2] == 1:
            $show_chr("A-DFABA-AAAA")
            y "W-Wait... I-I just felt something touch my head!"
            y "Was that y-you, [player]?"
            menu:
                "Yes, I wanted to try it out. I hope it didn't weird you out.":
                    $add_k(1)
                    $show_chr("A-CFAAA-AAAA")
                    y "A-Actually... yes, a bit..."
                    $show_chr("A-BFAAA-AAAA")
                    y "Please don't get me wrong! I didn't mean to be rude but... feeling your touch without actually seeing your hand felt a little bit... creepy"
                    $show_chr("A-IFAAA-AAAA")
                    y "Like a ghost... and the fact that I'm alone here doesn't really make it less spooky..."
                    $show_chr("A-JFAAA-AAAA")
                    y "Would you mind if I asked to not do that again please? T-Thank you..."
                "I don't believe that was me, want me to try touching your head?":
                    $show_chr("A-IFAAA-AAAA")
                    y "O-Oh please, no..."
                    $show_chr("A-JFAAA-AAAA")
                    y "It... spooked me a little bit if I may be honest."
                    $show_chr("A-AFAAA-ALAL")
                    y "I would prefer if you don't do that..."
                    $show_chr("A-BFAAA-AMAM")
                    y "{b}I~If{/b} you don't mind..."
        if persistent.boop_locations[2] == 2:
            $show_chr("A-DHAAA-AEAB")
            y "T~There it was again..."
            $show_chr("A-CFAAA-AEAB")
            y "Please... I already asked you not to do that... please don't make me ask you again."
            y "Thank you."
        if persistent.boop_locations[2] == 3:
            $show_chr("A-CFCAA-AEAB")
            y "It's getting kind of annoying, [player]..."
            y "And it's also incredibly disrespectful. I'm not a kitten you know?"
        if persistent.boop_locations[2] == 4:
            $show_chr("A-CGCAA-AEAB")
            y "Aaaalright [player], enough is enough. You know what?"
            $show_chr("A-AFCAA-AEAB")
            y "I would say, we call it a day for now. I asked you to stop politely but you wouldn't listen. So I will go back to my reading now and you can come back as soon as you are willing to take me seriously again. Bye."
            $renpy.call("save_and_quit_but_its_abrupt")
        if persistent.boop_locations[2] >= 5:
            "... [player], you're seriously starting to make me realize the true depths of my fury for you. If you do not wish to be forever on my bad side, you will stop booping me. {i}Now{/i}"
    $store.mousex = 0
    $store.mousey = 0
    return

label sleepy_headpat:
        y "hmph...?"
        hide yuri_sleep
        show yuri_sleepy zorder 11
        y "O-oh it's you [player]"
        y "You scared me a bit, although that is quite comforting"
        hide yuri_sleepy
        show yuri_sleep
        y "I wouldn't be opposed if you kept doing it..."
        return


label boop_window:
    python:
        if persistent.boop_locations[4] <= 4:
            persistent.boop_locations[4] += 1
        if check_memory("window_boop"):
            if check_memory("window_boop", "disabled"):
                if return_memory("window_boop_game_session")[0] < persistent.game_session:
                    renpy.call("annoyed_boop_window")
    if persistent.boop_locations[4] == 1:
        $show_chr("A-BFBAA-ALAA")
        y "Huh? Did you hear that too? I thought I heard something knocking on the window..."
        $show_chr("A-JFGAA-ALAA")
        y "But... that's impossible. There are no NPCs left in this world..."
    elif persistent.boop_locations[4] == 2:
        $show_chr("A-BFGAA-ALAA")
        y "Again... are you really not hearing anything?"
        $show_chr("A-AFAAA-ALAA")
        y "Wait a moment... is that you? Are you clicking the window?"
        $show_chr("A-CBAAA-ALAA")
        y "Oh my... I almost thought I was going insane. Again."
    elif persistent.boop_locations[4] == 3:
        $show_chr("A-JCAAA-ALAA")
        y "Umm... [player]... please be careful..."
    elif persistent.boop_locations[4] == 4:
        #Shattering Glass sound
        #Broken-Window-Image overlay
        play sound "sfx/glassbreak.wav"
        $show_chr("A-DFGBA-ALAA")
        y "..."
        if karma() >= 4:
            $show_chr("A-DFGBA-ALAA")
            y "Oh dear... are you hurt? Come, let me see your hand..."
            $show_chr("A-IFBAA-ALAA")
            y "Oh wait... I forgot... there is no hand... at least that means that you can't be hurt."
            $show_chr("A-KACAA-AAAC")
            y "Well, seems you took the fourth-wall-break theme to a new level! Quite literally."
            $show_chr("A-AFAAA-AAAE")
            y "But seriously... please don't do that again. I still have weather in my world, and I will have to fix that when you turn the game off next time."
        else:
            $show_chr("A-DFCBA-ALAA")
            y "Are you out of your mind?"
            y "I asked you to be careful! But you just couldn't resist, could you?"
            $show_chr("A-CHBAA-ALAA")
            y "I'm sorry... I shouldn't have snapped... but that was really unnecessary..."
            $show_chr("A-CFBAA-ABAB")
            y "You know, there is still weather in my world, and I will need to fix that window somehow..."
            y "Please, try to be a bit more careful from now on..."
        $update_memory("window_boop", "disabled")
        $update_memory("window_boop_game_session", persistent.game_session)
    $store.mousex = 0
    $store.mousey = 0
    return

label annoyed_boop_window:
    if karma() >= 3:
        $show_chr("A-ACAAA-AAAA")
        y "Hey [player]...there's something I'd like to tell you..."
        y "You remember the little...accident, you had with my window?"
        $show_chr("A-BCAAA-AAAB")
        y "Please don't get the wrong idea. I know it was an accident. Things like that just happen from time to time, and I am not upset with you."
        $show_chr("A-AFAAA-AAAB")
        y "But please understand that it caused a little bit of trouble to me. There are no other people in this world so I had to fix the window myself."
        $show_chr("A-ACAAA-ABAB")
        y "So in order to prevent another accident like this, I turned this little feature off. You are still free to show your affection to me by stroking my cheek, but you don't have to worry about the window anymore."
        jump ch30_loop
    else:
        $show_chr("A-AFAAA-AAAA")
        y "Hey [player]. There is something I would like to tell you."
        y "You remember the little...accident, you had with my window?"
        $show_chr("A-BFAAA-AAAB")
        y "I know, I know, this was supposed to be a game, and I understand that it had to be very tempting for you to try that, I get it."
        $show_chr("A-AFAAA-AAAB")
        y "But please understand that it caused a little bit of trouble for me. There are no other people in this world so I had to fix the window myself."
        $show_chr("A-CFCAA-ABAB")
        y "So in order to prevent you from testing my patience too much, I turned this little feature off. You are still free to come here but for the love of Salvato, please stop messing around with the environment!"
        y "I can't spend hours and hours cleaning up after your nonsense every week."
        jump ch30_loop
