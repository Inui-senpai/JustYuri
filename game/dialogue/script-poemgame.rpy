init python:
    import random


    class PoemWord:
        def __init__(self, word, GoodPoint, SadPoint, InsanePoint, SanePoint, glitch=False):
            self.word = word
            self.GoodPoint = GoodPoint
            self.SadPoint = SadPoint
            self.InsanePoint = InsanePoint
            self.SanePoint = SanePoint


    full_wordlist = []
    try:  # Error Handling is very important!
        with codecs.open('/poemwords_different.txt', 'r', 'utf-8') as wordfile:  # Explicitly declare encoding.  Fix #1
            for line in wordfile:
                line = line.strip()
                if line == '' or line[0] == '#': continue

                # Very Important! Robust error handling for inconsistent data formats
                x = line.split(',')
                if len(x) == 5: # check the length before conversion
                   try:
                        full_wordlist.append(PoemWord(x[0], float(x[1]), float(x[2]), float(x[3]), float(x[4])))
                   except ValueError as e:  # Check for non-floats
                       print_debug(f"Error parsing line '{line}': {e}. Skipping this line") 
                else:
                   print_debug(f"Error: Unexpected number of fields in '{line}'. Skipping this line.")

    except FileNotFoundError:
        print_debug(f"File '/poemwords_different.txt' not found.")
    except Exception as e: #General Error Catch for File Errors
        print_debug(f"An unexpected error occurred while reading the file: {e}")

    seen_eyes_this_chapter = False
    yuriTime = renpy.random.random() * 4 + 4
    yuriPos = 0
    yuriOffset = 0
    yuriZoom = 1


    def randomPauseYuri(trans, st, at):
        if st > yuriTime:
            global yuriTime
            yuriTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomMoveYuri(trans, st, at):
        global yuriPos
        global yuriOffset
        global yuriZoom
        if st > .16:
            if yuriPos > 0:
                yuriPos = renpy.random.randint(-1,0)
            elif yuriPos < 0:
                yuriPos = renpy.random.randint(0,1)
            else:
                yuriPos = renpy.random.randint(-1,1)
            if trans.xoffset * yuriPos > 5: yuriPos *= -1
            return None
        if yuriPos > 0:
            trans.xzoom = -1
        elif yuriPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * yuriPos
        yuriOffset = trans.xoffset
        yuriZoom = trans.xzoom
        return 0

label poem(transition=True):
    if current_timecycle_marker == "_day":
        show bg notebook_day zorder 30
    elif current_timecycle_marker == "_night":
        show bg notebook_night zorder 30
    elif current_timecycle_marker == "_sunrise":
        show bg notebook_sunrise zorder 30
    elif current_timecycle_marker == "_sunset":
        show bg notebook_sunset zorder 30
    else:
        show bg notebook zorder 30
    show screen quick_menu
    show y_sticker at sticker_middle zorder 40
    if transition:
        with dissolve_scene_full
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    python:
        poemgame_glitch = False
        played_baa = False
        progress = 1
        numWords = 1
        GoodPointTotal = 0
        SadPointTotal = 0
        InsanePointTotal = 0
        SanePointTotal = 0
        wordlist = list(full_wordlist)
        yuriTime = renpy.random.random() * 4 + 4
        yuriPos = renpy.random.randint(-1,1)
        yuriOffset = 0
        yuriZoom = 1

        while True:
            ystart = 160
            if persistent.playthrough == 2 and chapter == 2:
                pstring = ""
                for i in range(progress):
                    pstring += "1"
            else:
                pstring = str(progress)
            ui.text(pstring + "/" + str(numWords), style="poemgame_text", xpos=810, ypos=80, color='#000')
            for j in range(2):
                if j == 0: x = 440
                else: x = 680
                ui.vbox()
                for i in range(5):
                    word = random.choice(wordlist)
                    wordlist.remove(word)
                    ui.textbutton(word.word, clicked=ui.returns(word), text_style="poemgame_text", xpos=x, ypos=i * 56 + ystart)
                ui.close()

            t = ui.interact()
            GoodPointTotal += t.GoodPoint
            SanePointTotal += t.SanePoint
            InsanePointTotal += t.InsanePoint
            SadPointTotal += t.SadPoint
            progress += 1
            if progress > numWords:
                break


        Good = [GoodPointTotal > SanePointTotal,
         GoodPointTotal > InsanePointTotal,
         GoodPointTotal > SadPointTotal]

        Sad = [SadPointTotal > SanePointTotal,
         SadPointTotal > InsanePointTotal,
         SadPointTotal > GoodPointTotal]

        Insane = [InsanePointTotal > SanePointTotal,
         InsanePointTotal > SadPointTotal,
         InsanePointTotal > GoodPointTotal]

        Sane = [SanePointTotal > SadPointTotal,
         SanePointTotal > InsanePointTotal,
         SanePointTotal > GoodPointTotal]

        if all(Good):
            renpy.jump ("goodpoemresponse")
        elif all(Sad):
            renpy.jump ("sadpoemresponse")
        elif all(Insane):
            renpy.jump ("insanepoemresponse")
        elif all(Sane):
            renpy.jump ("sanepoemresponse")
        else:
            renpy.jump ("goodpoemresponse")



image y_sticker:
    "/images/poem_game/stickers/sticker_uniform_1.png"
    xoffset yuriOffset xzoom yuriZoom
    block:
        function randomPauseYuri
        parallel:
            function randomMoveYuri
        repeat

image y_sticker hop:
    "/images/poem_game/stickers/sticker_uniform_2.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker"

transform sticker_middle:
    xcenter 210 yalign 0.9 subpixel True

transform sticker_hop:
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
