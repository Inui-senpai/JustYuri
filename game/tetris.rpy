default persistent.skin = 0
define TetrisWinner = 0
define LineLimit = 0
define TetrisScore = 0
define PlayerForYuri = 0

label tetris:
    python:
        DisableTalk()
        boopable = False
        show_chr("A-BFBAA-AAAC")
        LineLimit = 0
        TetrisScore = 0
    if sanity_lvl() > 2 and karma_lvl() > 2:
        menu:
            y "Oh, so you'd like to play some Tetris, hm?"
            "Yes.":
                y "Oh, good."
                y "Which theme would you like this time?"
                $pass
            "No.":
                y "I see..."
                y "Perhaps some other time, then."
                jump ch30_loop
    elif sanity_lvl() > 2 and karma_lvl() < 3:
        menu:
            y "You... want to play Tetris...?"
            "Yes.":
                y "Oh..."
                y "Well, sure, I guess I wouldn't really mind."
                y "I have to wonder if you'll mock me for losing."
                y "Judging from how much pleasure you derive from my misery I assume you will."
                y "Anyway, just pick a theme and let's get on with it."
                $pass
            "No.":
                y "Oh..."
                y "Perhaps... some other time, then."
                jump ch30_loop
    elif sanity_lvl() < 3 and karma_lvl() > 2:
        menu:
            y "Y-you want to play Tetris, yes?"
            "Yes.":
                y "Uhuhuhu~!"
                y "Which theme would you like this time?"
                y "It doesn't matter which one you'll choose, I'm sure you'll still dominate me no matter what you choose!~"
                $pass
            "No.":
                y "O-oh..."
                y "Well..."
                y "Alright..."
                y "Perhaps some other time, then..."
                jump ch30_loop
    elif sanity_lvl() < 3 and karma_lvl() < 3:
        menu:
            y "You want to play Tetris, hm?"
            "Yes.":
                y "I'm sure you'll somehow find a way to make even such a trivial matter into a nightmare for me..."
                y "Somehow you'll still find a way to humiliate me..."
                y "Right..."
                y "Anyway, which theme do you want?"
                $pass
            "No.":
                y "Oh..."
                y "Well... I see..."
                y "Perhaps some other time when you learn to make up your mind."
                jump ch30_loop

    if current_timecycle_marker == "_night":
        menu:

            "Default Theme.":
                y "You don't want to give Tetris any kind of skin? That's okay."
                $ persistent.skin = 1

            "Tetris 99 Theme.":
                y "Oh? Going to experience one of the latest Tetris themes?"
                y "But please don't expect too much of it."
                $ persistent.skin = 2

            "GameBoy Tetris Theme.":
                y "Oh! Is this the classic Tetris for HandHelds? Have in mind that this is the color version."
                $ persistent.skin = 3

            "Mega Drive Tetris Theme.":
                y "Okay. It's unfortunate that you can't experience Blast Processing in Ren'Py."
                $ persistent.skin = 4

            "M1ND BEND3R Theme.":
                $ persistent.skin = 5

            "Custom Theme.":
                call custom_tetris_checkpoint_start

    else:
        menu:

            "Default Theme.":
                y "You don't want to give Tetris any kind of skin? That's okay."
                $ persistent.skin = 1

            "Tetris 99 Theme.":
                y "Oh? Going to experience one of the latest Tetris themes?"
                y "But please don't expect too much of it."
                $ persistent.skin = 2

            "GameBoy Tetris Theme.":
                y "Oh! Is this the classic Tetris for HandHelds? Have in mind that this is the color version."
                $ persistent.skin = 3

            "Mega Drive Tetris Theme.":
                y "Okay. It's unfortunate that you can't experience Blast Processing in Ren'Py."
                $ persistent.skin = 4

            "Custom Theme.":
                call custom_tetris_checkpoint_start

    y "Alright [player], now I can let you select the modes you want to play."
    menu:
        "Line count":
            if persistent.lovecheck and karma_lvl() > 3:
                #If lovecheck is true along with K: 4-5
                $ show_chr("A-BBBAA-ADAA")
                y "It's a nice way to pass the time, really."
                y "Just a couple doing things together..."
                y "Ahem... Anyway let's get started."
                $ show_chr("A-FCAAA-ACAB")
                menu:
                    "30":
                        $ LineLimit = 30
                    "50":
                        $ LineLimit = 50
                    "100":
                        $ LineLimit = 100
                    "150":
                        $ LineLimit = 150
                    "300":
                        $ LineLimit = 300
                jump tetris_difficulty
            elif karma_lvl() >= 3:
                #If K = 3-5 regardless of S value
                $ show_chr("A-ACEAA-AMAM")
                y "Oh, lovely choice, [player]~"
                y "W-well, hopefully I will prove a worthy challenge..."
                y "Uhuhuhu..."
                y "Well whoever gets to the specific amount of lines wins..."
                menu:
                    "30":
                        $ LineLimit = 30
                    "50":
                        $ LineLimit = 50
                    "100":
                        $ LineLimit = 100
                    "150":
                        $ LineLimit = 150
                    "300":
                        $ LineLimit = 300
                jump tetris_difficulty
            elif karma_lvl() < 3:
                #[If K = 1-2
                $ show_chr("A-BEBAA-AMAM")
                y "I-I'm not sure if you'd want to waste your time with me..."
                y "I mean, this mode seems a bit too simple and boring to you."
                y "Especially with someone such as myself."
                $ show_chr("A-CEAAA-ALAL")
                y "Maybe you just want to get an ego boost from seeing me lose?"

                menu:
                    "30":
                        $ LineLimit = 30
                    "50":
                        $ LineLimit = 50
                    "100":
                        $ LineLimit = 100
                    "150":
                        $ LineLimit = 150
                    "300":
                        $ LineLimit = 300
                jump tetris_difficulty

        "Score":
            if persistent.lovecheck and karma_lvl() > 3 and sanity_lvl() < 2:
                #[If K = 3-5 and lovecheck == true, S = 1-2]
                $ show_chr("A-KLAAA-AKAK")
                y "And maybe you will win me as a prize to be cherished... Forever~"
                y "Or maybe I would win you. Hehe. Either way, everyone wins!"
                menu:
                    "20000":
                        $ TetrisScore = 20000
                    "50000":
                        $ TetrisScore = 50000
                    "100000":
                        $ TetrisScore = 100000
                    "200000":
                        $ TetrisScore = 200000
                    "300000":
                        $ TetrisScore = 300000
                    "500000":
                        $ TetrisScore = 500000
                jump tetris_difficulty
            elif karma_lvl() >= 3:
                #[K = 3-5 and regardless of S value]
                $ show_chr("A-FCEAA-ABAB")
                y "Oh, some competition, hm?"
                y "Well I suppose being a little competitive wouldn't be too bad, now would it?"
                $ show_chr("A-ABAAA-AMAM")
                python:
                    if sanity_lvl() >= 3:
                        placeholder = "contest"
                    elif sanity_lvl() <= 3:
                        placeholder = "thrill"
                y "There's nothing wrong with a nice [placeholder] every once in a while..."
                #If sanity 1-2 "thrill"
                #If sanity 3-5 "contest"
                $ show_chr("A-AAEAA-ALAL")
                y "Alright, let us see who will outdo the other!"
                menu:
                    "20000":
                        $ TetrisScore = 20000
                    "50000":
                        $ TetrisScore = 50000
                    "100000":
                        $ TetrisScore = 100000
                    "200000":
                        $ TetrisScore = 200000
                    "300000":
                        $ TetrisScore = 300000
                    "500000":
                        $ TetrisScore = 500000
                jump tetris_difficulty
            elif karma_lvl() < 3:
                #[K= 1-2 regardless of S value]
                $ show_chr("A-AEBAA-ALAL")
                y "W-well... [player], I don't know whether this is simply a jest or you just trying to impress me..."
                y "All just to prove something to me. Just to rub it in my face.."
                y "Then again, at least it's a way to pass the time."
                $ show_chr("A-BECAA-AMAM")
                y "Well, whatever."
                y "Let's get on with it."
                menu:
                    "20000":
                        $ TetrisScore = 20000
                    "50000":
                        $ TetrisScore = 50000
                    "100000":
                        $ TetrisScore = 100000
                    "200000":
                        $ TetrisScore = 200000
                    "300000":
                        $ TetrisScore = 300000
                    "500000":
                        $ TetrisScore = 500000
                jump tetris_difficulty

        "CO-OP":
            if karma_lvl() == 5:
                #[If K = 5]
                $ show_chr("A-ABABA-AMAM") # open mouth smile with blush, hands playing with hair
                y "Oh how fun~!"
                y "W-well if you insist [player]. It is better when we strive toward the same goal together."
                y "As the old saying goes, birds of a feather flock together. Two heads are always better than one ~!"
                $ show_chr("A-FCCBA-AAAL") # smirk with a wink and hand on her chest (This needs expressions)
                y "Maybe it might even become an all-nighter! Ehehe..."
                $ show_chr("A-ECABA-AAAJ")  # closed mouth smile with hands on her lips and half-lidded eyes (needs expressions)
                y "Okay game on dear [player]!"
                $ AI_difficulty = "CO_OP"
                jump tetris_rules
            elif karma_lvl() == 1:
                #[If K = 1]
                $ show_chr("A-CEBAB-AAAL") # insert closed frown with worried eyebrows and slightly teary eyes and hand on her chest
                y "A-are you sure...?"
                y "I mean why would you want to work together with me, let alone play a game together?"
                y "Is this again a big joke to you? I... I don't know anymore."
                #insert open frown with closed eyes and worried eyebrows with hands on hair
                y "Let's try this... I guess."
                #if sanity_lvl() > 2 and karma_lvl() > 2:
                #elif sanity_lvl() > 2 and karma_lvl() < 3:
                #elif sanity_lvl() < 3 and karma_lvl() > 2:
                #elif sanity_lvl() < 3 and karma_lvl() < 3:
                $ AI_difficulty = "CO_OP"
                jump tetris_rules
            else:
                #[If K = 2-4]
                $show_chr("A-ACAAA-AAAA")
                y "O~Oh? You want to try the Co-op mode?"
                y "Well, I guess we could try it together... "
                y "If you are really sure you want to..."
                $show_chr("A-BFAAA-AAAA")
                y "I just hope that I don't mess it up somehow..."
                y "Oh, what am I saying? It's just Tetris, it will be alright..."
                $show_chr("A-AFAAA-ABAB")
                y "So umm... let's just... try it out, I guess."
                $ AI_difficulty = "CO_OP"
                jump tetris_rules

label custom_tetris_checkpoint_start:
    $ show_chr("A-ACAAA-ABAB")
    y "Oh, you'd like to try your hand on a custom Tetris build?"
    y "Well, let me give you a quick walk-through of how it's done or do you already have it all figure out?"
    menu:
        "Try me":
            y "Okay"
            jump custom_tetris_checkpoint
        "No":
            y "By the way, you should probably write this down somewhere..."


label custom_tetris_repeat:
    y "All those files which you will create will have to go to folder \"game\\custom_tetris\""
    y "First thing you need to know is that all images have to be in .png format and all sounds have to be .ogg files. Ren'Py will reject anything else."
    y "Let's start with the background. {b}Line Count{/b} and {b}Score{/b} have two types of background depending on difficulties."
    y "For the Easy, Medium and Hard difficulties it has to be 220 x 420 pixels image. Use the {b}background.png{/b} file from the folder \"game\\images\\tetris\\tetris\" as an example..."
    $ show_chr("A-ACAAA-ABAD")
    y "For the same modes but in the Disadvantage, Veteran and Expert difficulties, it is the exact same procedure, but this time you have to delete the grids and name it {b}backgrund_no_grind{/b}... oh yes, and it still has to be a .png file!"
    y "The Co-op mode shares the same procedure, but this time it is 421 x 420 pixels and you name it {b}grids (coop).png{/b}. It's in the same folder again."
    y "Now we come to the blocks."
    y "Fun fact, did you know that a single block is called a Tetromino?"
    y "There are 7 pieces in Tetris which usually have different colors. You could make them the same colors"
    y "But that would be kind of boring. Don't you think?"
    $ show_chr("A-ACAAA-AFAD")
    y "Each pieces is build from individual blocks which are number from 1 to 7."
    y "Also in newer version of Tetris. You can see where the piece will land. We refer it as {b}shadow pieces{/b} "
    y "They also need to have their own colors which are usually transparency of normal blocks"
    y "Each of the cube need to be a .png image with size 20x20. You can use the {b}cube_1.png{/b} file from the folder \"game\\images\\tetris\\tetris\" as an example..."
    y "For the T Piece you set up cube_1.png and shadow_1.png"
    y "For the S Piece you set up cube_2.png and shadow_2.png"
    y "For the Z Piece you set up cube_3.png and shadow_3.png"
    y "For the L Piece you set up cube_4.png and shadow_4.png"
    y "For the J Piece you set up cube_5.png and shadow_5.png"
    y "For the I Piece you set up cube_6.png and shadow_6.png"
    y "For the O Piece you set up cube_7.png and shadow_7.png"
    y "The last is wall of the game. For wall you set up cube_8.png. Most of the time is black for easy distinguish"
    y "For now in your custome_Tetris folder, you should have 18 files. 2 Background, 8 cube and 8 shadow png"
    y "Is everything good? If not let me know and I will repeat the step again"
    menu:
        "Yes":
            y "Okay. Let's go to next part"
        "No":
            y " Oh dear. Let me repeat steps again."
            jump custom_tetris_repeat


label custom_tetris_repeat_audio:
    $ show_chr("A-ACAAA-ABAD")
    y "Now for the audio part..."
    y "All the audio files must have specific names, otherwise the game will reject them, so here are the names for the sounds."
    y "Keep in mind that sfx should be a very short sounds. If they will be long they will overlap. It will turn into mess"
    y "Here are the names of the sfx sounds"
    y "t-fl.ogg for a single line clear."
    y "t-2f1.ogg for a double line clear."
    y "t-3fl.ogg for a triple line clear."
    y "t-4fl.ogg for a full tetris line clear."
    y "t-drop.ogg for the hard drop sound."
    y "t-move.ogg for whenever you move the piece."
    y "t-rotate.ogg for whenever you rotate the piece."
    y "Those are were sfx sound. For the main music which will loop for the duration of game."
    y "Use \"tetris.ogg\""
    y "So in the end your custome_Tetris folder should have 26 files. 2 Background, 8 cube, 8 shadow png and 8 .ogg files"
    $ show_chr("A-BCBAA-AEAD")
    y "I-I hope I didn't confuse you with that explanation..."
    y "I'm not good at explaining such technicalities..."
    y "If I mess up and you still need to adjust something let me know and I will repeat the steps"
    menu:
        "Everything is fine":
            y "Yay"
        "Please start from start":
            y "Okay"
            jump custom_tetris_repeat
        "Please start from audio files":
            y "Okay"
            jump custom_tetris_repeat_audio
    if karma_lvl() >= 2:
        $ show_chr("A-GCAAA-AEAD")
        y "Anyway, I'm looking forward to what you might come up with!"
        y "Everything you do is fun for me anyway..."
    else:
        $ show_chr("A-BFBAA-AEAD")
        y "Oh, I do wonder what you just might come up with..."
        y "Most likely something ridiculous or nonsensical..."
    call custom_tetris_checkpoint
    return

label custom_tetris_failure:
    $show_chr("A-ACDAA-ABAB")
    y "[player]? It seems you need to fix some issue which I mention"
    y "Perhaps I should explain all steps again"
    call custom_tetris_repeat

label custom_tetris_checkpoint:
    menu:
        y "Do you have everything done?"
        "Yes.":
            python:
                from os import walk
                f = []
                for (dirpath, dirnames, filenames) in walk(config.basedir + "/game/custom_tetris"):
                    f.extend(filenames)
                    break
                custom_tetris = []
                #loads music and png files
                for i in f:
                    if i.find(".ogg") == -1 and i.find(".mp3") == -1 and i.find(".wav") == -1 and i.find(".flac") == -1 and i.find(".png") == -1:
                        pass
                    else:
                        custom_tetris.append((i, i))
                custom_tetris.append(("", ""))

                if custom_tetris == [("", "")]:
                    show_chr("A-BFAAA-AAAN")
                    y("Seems like you don't have anything in the folder right now...")
                    show_chr("A-BBBAA-AAAN")
                    y("That's fine. I'll be waiting for them regardless.")
                    renpy.jump("ch30_loop")
                custom_tetris_png_req = ["background", "background_no_grind"]
                custom_tetris_music_req = ["t-fl", "t-2fl", "t-3fl", "t-4fl", "t-drop", "t-move", "t-rotate", "tetris"]
                custom_tetris_all_ready = True
                for i in custom_tetris_png_req:
                    element = (i + ".png", i + ".png")
                    if not element in custom_tetris:
                        y("It seems there is issue with background image:" + i)
                        renpy.call("custom_tetris_failure")
                for i in custom_tetris_music_req:
                    element = (i + ".ogg", i + ".ogg")
                    if not element in custom_tetris:
                        y("It seems there is issue with audio files: " + i)
                        renpy.call("custom_tetris_failure")
                for i in range(1, 9):
                    element = ("cube_" + str(i) + ".png", "cube_" + str(i) + ".png")
                    if not element in custom_tetris:
                        y("It seems there is issue with piece cube image:" + i)
                        renpy.call("custom_tetris_failure")
                for i in range(1, 8):
                    element = ("shadow_" + str(i) + ".png", "shadow_" + str(i) + ".png")
                    if not element in custom_tetris:
                        y("It seems there is issue with piece shadows image:" + i)
                        renpy.call("custom_tetris_failure")
                persistent.skin = 6
        "No.":
            $ show_chr("A-GCBAA-AAAA")
            y "I see."
            $ show_chr("A-ABBAA-AAAA")
            y "No need to rush. Take your time."
            jump ch30_loop
    return


label tetris_difficulty:
    $ show_chr("A-AAAAA-AAAA")
    y "If you are not used to Tetris, we can adjust the difficulty a bit. Just tell me how you wish it to be, I will not judge."


    menu:
        "Easy":
            $ AI_difficulty = 1

            if karma_lvl() >= 3:
                y "Oh, I see."
                y "You'd like me to go easy on you this time, hm?"
                y "I'm happy to oblige, [player]!"

            elif karma_lvl() < 3:
                #[If K= 1 or 2 regardless of S value]
                $ show_chr("A-BEAAA-AMAM")
                y "..."
                y "I-is this some kind of joke? Directed at me?"
                y "To indulge in this activity but at such an infantile level... Seemingly to jest at my abilities?"
                $ show_chr("A-CEBAA-AAAD")  # closed frown with closed eyes and hand on her cheek (needs expressions)
                y "Whatever... Let us proceed."
                #elif sanity_lvl() > 2 and karma_lvl() < 3:
                #elif sanity_lvl() < 3 and karma_lvl() > 2:
                #elif sanity_lvl() < 3 and karma_lvl() < 3:


        "Medium":
            $ AI_difficulty = 2

            if karma_lvl() >= 3:
            #[If K= 3-5 and S: 3-5]
                $ show_chr("A-ABABA-AAAJ")
                y "Oh I see~ Trying to warm up with a slight challenge eh?"
                y "Well then. I would like to see how you do!"
                y "It is good to get out of your comfort zone a bit more."

            elif karma_lvl() < 3:
            #[If K = 1 or 2 regardless of S value]
                $ show_chr("A-ADCAA-AAAL")
                y "Hm... Y-you know I am slightly surprised that you wanted to partake in this game with me. I was thinking you'd pick a harder difficulty just to prove a point."
                y "I mean why even bother with such a simple difficulty with someone as myself?"
                y "If this is meant to be a joke, I quite frankly do not understand it."
                $ show_chr("A-CECAA-ALAL")
                y "Whatever... Anyways let the games begin."


        "Hard":
            $ AI_difficulty = 3

            if karma_lvl() >= 3:
            #[If K = 3-5 and S = 3-5]
                $ show_chr("A-ACCAA-AMAM")
                y "Oh huhuhehehe... Really turning the dial up are you now, [player]?"
                y "Well I do like it when you get a bit more daring~ It is rather inspiring."
                # soft closed smile with a blush and hands on the table
                y "Well as people say nowadays, I guess, let these games begin!"
                y "O-oh but don't go too hard on yourself [player]... Eheheh."

            elif karma_lvl() < 3:
            #[If K = 1-2]
                $ show_chr("A-CECAA-ALAL")
                y "I-I guess you really want to rub it in my face just to prove a point..."
                y "Very well then... Let the games begin, I suppose."
                y "Hmph."


        "Disadvantage":
            $ AI_difficulty = 4

            if karma_lvl() >= 3:
                $ show_chr("A-DCCBA-AAAD")
                y "Mmm..."
                y "Oh dear [player]. That seems like such a Herculean task to tackle. Are you sure?"
                $ show_chr("A-ABAAA-ALAL")
                y "Ehehehehe... Well alright if you insist~"
                y "Prepare thy mind and body for the penultimate gamer's challenge dear [player]!"

            elif karma_lvl() > 3 and sanity_lvl() < 3:
            #[If K= 3-5 and S= 2 or 1]
                $ show_chr("A-DLCBA-AMAM")
                y "Oh oh... Oh my yes!"
                y "A glutton for punishment aren't you [player]?"
                y "Whatever scars from this task you may carry I will bear with you!"
                y "J-just be a bit careful [player]... If you exert yourself too much and get hurt, I might have to thrash a few things here~ Aahahaha..."
                $ show_chr("A-DCAAA-AFAG")
                y "Show me, show them all what you are made of sweet [player]!!!"

            elif karma_lvl() < 3:
            #[If K= 2 or 1, regardless of S value]
                $ show_chr("A-DEDAA-ABAB")
                y "I-I see..."
                y "I guess you just want to jest with me then..."
                $ show_chr("A-BEABB-AMAM")
                y "Maybe prove your point further on how bigger you are than me? Rub it in my face just a little more. To show how much you don't need me?"
                $ show_chr("A-CEAAA-AMAM")
                y "N-nevermind... It wouldn't matter what I said here. Let the games begin I guess."


        "Expert":
            $ AI_difficulty = 5

            $ show_chr("A-ACBAA-AIAI")
            y "Oh you are in for a bumpy ride [player]..."

            if persistent.lovecheck:
            #if lovecheck is true
                $ show_chr("A-ACCBA-AIAI")
                y "...but I guess you like it that way don't you..."

            else:
                if karma_lvl() >= 3:
                #if karma_lvl() is 3-5
                    $ show_chr("A-ACBAA-ABAL")
                    y "Very well, I'll try my best to offer you a suitable challenge."
                    y "Just keep in mind, it is just a game. It doesn't really matter who wins as long as we are having a good time."

                elif karma_lvl() < 3:
                #if karma_lvl() is 1-2
                    $ show_chr("A-AFBAA-ABAL")
                    y "Maybe I can teach you a lesson here..."


        "Veteran":
            $ AI_difficulty = 6
            $ show_chr("A-ACAAA-ABAL")
            y "The highest, I see..."
            y "I'm not even sure if I'm good enough to pull this off but... let's give it a try."


        "Your choice, [persistent.yuri_nickname]":
            # K&S - both karma_lvl() and sanity are...
            # K|S - either karma_lvl() or sanity_lvl() is...

            # Adding random mood.
            $ import random
            $ randomMood = random.randint(-1, 1)

            # K&S are almost maximum.
            if(abs(karma_lvl() + sanity_lvl() - 10) < 2):
                if(randomMood < 1):
                    # Easy.
                    $ AI_difficulty = 1

                    $ show_chr("A-IAABA-AAAC")
                    if persistent.lovecheck == True:
                        y "Oh, how polite of you to let me choose. Why don't we keep it casual for now with easy then darling~"
                    else:
                        y "Oh, how polite of you to let me choose [player]. Why don't we keep it casual with easy then?"

                else:
                    # Medium.
                    $ AI_difficulty = 2

                    $ show_chr("A-IAABA-AAAC")
                    if persistent.lovecheck == True:
                        y "Oh, how polite of you to let me choose. Why don't we keep it casual for now with medium then darling~"
                    else:
                        y "Oh, how polite of you to let me choose [player]. Why don't we keep it casual with medium for now then?"

            # K&S are high.
            elif(abs(karma_lvl() + sanity_lvl() - 8) < 2):
                if(randomMood == -1):
                    # Easy.
                    $ AI_difficulty = 1

                    $ show_chr("A-CCAAA-AAAC")
                    y "Hmm..."
                    $ show_chr("A-ICAAA-AAAC")
                    y "I'm feeling something just a bit less challenging if that's alright with you."
                    y "Easy should work just fine for us then."

                elif(randomMood == 0):
                    # Medium.
                    $ AI_difficulty = 2

                    $ show_chr("A-CCAAA-AAAC")
                    y "Hmm..."
                    $ show_chr("A-ICAAA-AAAC")
                    y "I'm feeling something just a bit challenging if that's alright with you."
                    y "Medium should work just fine for us then."

                else:
                    # Hard.
                    $ AI_difficulty = 3

                    $ show_chr("A-CCAAA-AAAC")
                    y "Hmm..."
                    $ show_chr("A-ICAAA-AAAC")
                    y "I'm feeling something with a decent bit of challenge if that's alright with you."
                    y "Hard should work just fine for us then."

            # K&S are neutral.
            # Or.
            # K|S is high.
            elif(abs(karma_lvl() + sanity_lvl() - 6) < 2):
                if(randomMood == -1):
                    # Medium.
                    $ AI_difficulty = 2

                    if(abs(karma_lvl() - sanity_lvl()) < 2):
                        # K&S are neutral.
                        $ show_chr("A-BCAAA-AMAM")
                        y "I-If you're comfortable with that, [player]."
                        y "Don't expect me to give you a free pass though."
                        $ show_chr("A-IAAAA-AMAM")
                        y "Medium should suffice."

                    elif(karma_lvl() < sanity_lvl()):
                        # Low K, High S.
                        $ show_chr("A-CECAA-AAAA")
                        y "..."
                        $ show_chr("A-CDCAA-AAAA")
                        y "Could you at least have put in the effort to choose your own difficulty setting?"
                        y "Let's just get this over with. Medium it is."

                    else:
                        # Low S, High K.
                        $ show_chr("A-DBAAA-AAAA")
                        y "{b}It would be quite fun if you were always this passive towards me [player].{/b}"
                        $ show_chr("A-CAABA-ADAA")
                        y "..."
                        $ show_chr("A-CBABA-ADAA")
                        y "I still need to go ahead and choose a difficulty don't I? Medium should do just fine then, correct?"

                elif(randomMood == 0):
                    # Hard.
                    $ AI_difficulty = 3

                    if(abs(karma_lvl() - sanity_lvl()) < 2):
                        # K&S are neutral.
                        $ show_chr("A-BCAAA-AMAM")
                        y "I-If you're comfortable with that, [player]."
                        y "Don't expect me to give you a free pass though."
                        $ show_chr("A-IAAAA-AMAM")
                        y "Hard should suffice."

                    elif(karma_lvl() < sanity_lvl()):
                        # Low K, High S.
                        $ show_chr("A-CECAA-AAAA")
                        y "..."
                        $ show_chr("A-CDCAA-AAAA")
                        y "Could you at least have put in the effort to choose your own difficulty setting?"
                        y "Let's just get this over with. Hard it is."

                    else:
                        # Low S, High K.
                        $ show_chr("A-DBAAA-AAAA")
                        y "{b}It would be quite fun if you were always this passive towards me [player].{/b}"
                        $ show_chr("A-CAABA-ADAA")
                        y "..."
                        $ show_chr("A-CBABA-ADAA")
                        y "I still need to go ahead and choose a difficulty don't I? Hard should do just fine then, correct?"

                else:
                    # Disadvantage.
                    $ AI_difficulty = 4

                    if(abs(karma_lvl() - sanity_lvl()) < 2):
                        # K&S are neutral.
                        $ show_chr("A-BCAAA-AMAM")
                        y "I-If you're comfortable with that, [player]."
                        y "Don't expect me to give you a free pass though."
                        $ show_chr("A-IAAAA-AMAM")
                        y "Disadvantaged should suffice."

                    elif(karma_lvl() < sanity_lvl()):
                        # Low K, High S.
                        $ show_chr("A-CECAA-AAAA")
                        y "..."
                        $ show_chr("A-CDCAA-AAAA")
                        y "Could you at least have put in the effort to choose your own difficulty setting?"
                        y "Let's just get this over with. Disadvantaged it is."

                    else:
                        # Low S, High K.
                        $ show_chr("A-DBAAA-AAAA")
                        y "{b}It would be quite fun if you were always this passive towards me [player].{/b}"
                        $ show_chr("A-CAABA-ADAA")
                        y "..."
                        $ show_chr("A-CBABA-ADAA")
                        y "I still need to go ahead and choose a difficulty don't I? Disadvantaged should do just fine then, correct?"

            # K&S are lower than average.
            # Or.
            # K|S is neutral.
            elif(abs(karma_lvl() + sanity_lvl() - 4) < 2):
                if(randomMood == -1):
                    # Hard.
                    $ AI_difficulty = 3

                    if(abs(karma_lvl() - sanity_lvl()) < 2):
                        # K&S lower than average.
                        $ show_chr("A-CEAAA-AAAC")
                        y "I d-don't really know..."
                        y "Does it really even matter what difficulty we play on?"
                        y "I guess I'll just go for hard, You'll probably just boast about it afterwards regardless."

                    elif(karma_lvl() < sanity_lvl()):
                        # Low K, Neutral S.
                        $ show_chr("A-CEAAA-AAAC")
                        y "I d-don't really know..."
                        y "Does it really even matter what difficulty we play on?"
                        y "I guess I'll just go for hard, You'll probably just boast about it afterwards regardless..."
                        $ show_chr("A-CEAAB-AAAJ")
                        y "What did I do to deserve this kind of treatment anyways?"
                        y "..."
                        $ show_chr("A-CEAAA-AAAK")
                        y "Let's just get on with it already."

                    else:
                        # Low S, Neutral K.
                        y "How about we go for hard if you're willing?"
                        $ show_chr("A-DAAAA-AAAD")
                        y "It would be quite fun to pressure you just a bit."
                        y "Not to mention it's cute to watch you squirm around trying to keep up with me."

                elif(randomMood == 0):
                    # Disadvantage.
                    $ AI_difficulty = 4

                    if(abs(karma_lvl() - sanity_lvl()) < 2):
                        # K&S lower than average.
                        $ show_chr("A-CEAAA-AAAC")
                        y "I d-don't really know..."
                        y "Does it really even matter what difficulty we play on?"
                        y "I guess I'll just go for disadvantaged, You'll probably just boast about it afterwards regardless."

                    elif(karma_lvl() < sanity_lvl()):
                        # Low K, Neutral S.
                        $ show_chr("A-CEAAA-AAAC")
                        y "I d-don't really know..."
                        y "Does it really even matter what difficulty we play on?"
                        y "I guess I'll just go for disadvantaged, You'll probably just boast about it afterwards regardless..."
                        $ show_chr("A-CEAAB-AAAJ")
                        y "What did I do to deserve this kind of treatment anyways?"
                        y "..."
                        $ show_chr("A-CEAAA-AAAK")
                        y "Let's just get on with it already."

                    else:
                        # Low S, Neutral K.
                        y "How about we go for disadvantaged if you're willing?"
                        $ show_chr("A-DAAAA-AAAD")
                        y "It would be quite fun to pressure you just a bit."
                        y "Not to mention it's cute to watch you squirm around trying to keep up with me."

                else:
                    # Expert.
                    $ AI_difficulty = 5

                    if(abs(karma_lvl() - sanity_lvl()) < 2):
                        # K&S lower than average.
                        $ show_chr("A-CEAAA-AAAC")
                        y "I d-don't really know..."
                        y "Does it really even matter what difficulty we play on?"
                        y "I guess I'll just go for expert, You'll probably just boast about it afterwards regardless."

                    elif(karma_lvl() < sanity_lvl()):
                        # Low K, Neutral S.
                        $ show_chr("A-CEAAA-AAAC")
                        y "I d-don't really know..."
                        y "Does it really even matter what difficulty we play on?"
                        y "I guess I'll just go for expert, You'll probably just boast about it afterwards regardless..."
                        $ show_chr("A-CEAAB-AAAJ")
                        y "What did I do to deserve this kind of treatment anyways?"
                        y "..."
                        $ show_chr("A-CEAAA-AAAK")
                        y "Let's just get on with it already."

                    else:
                        # Low S, Neutral K.
                        y "How about we go for expert if you're willing?"
                        $ show_chr("A-DAAAA-AAAD")
                        y "It would be quite fun to pressure you just a bit."
                        y "Not to mention it's cute to watch you squirm around trying to keep up with me."

            # K&S are low.
            # Or.
            # K|S is minimal.
            elif(abs(karma_lvl() + sanity_lvl() - 2) < 2):
                if(randomMood == -1):
                    # Disadvantage.
                    $ AI_difficulty = 4

                    if(karma_lvl() < sanity_lvl()):
                        $ show_chr ("A-AECAA-AAAF")
                        y "I couldn't honestly care less what difficulty we play at by this point."
                        y "N-No wait, you know what?"
                        y "This would make for a good opportunity to put you in your place, and I won't waste it."
                        y "Let's set it to disadvantaged and see just how well you do."

                    else:
                        $ show_chr("A-AECAA-AAAF")
                        y "I couldn't honestly care less what difficulty we play at by this point."
                        y "N-No wait, you know what?"
                        y "This would make for a good opportunity to put you in your place, and I won't waste it."
                        $ show_chr ("A-AECAA-AAAG")
                        y "Let's set it to disadvantaged and see just how well you do."

                elif(randomMood == 0):
                    # Expert.
                    $ AI_difficulty = 5

                    if(karma_lvl() < sanity_lvl()):
                        $ show_chr ("A-AECAA-AAAF")
                        y "I couldn't honestly care less what difficulty we play at by this point."
                        y "N-No wait, you know what?"
                        y "This would make for a good opportunity to put you in your place, and I won't waste it."
                        y "Let's set it to expert and see just how well you do."

                    else:
                        $ show_chr("A-AECAA-AAAF")
                        y "I couldn't honestly care less what difficulty we play at by this point."
                        y "N-No wait, you know what?"
                        y "This would make for a good opportunity to put you in your place, and I won't waste it."
                        $ show_chr ("A-AECAA-AAAG")
                        y "Let's set it to expert and see just how well you do."

                else:
                    # Veteran.
                    $ AI_difficulty = 6

                    if(karma_lvl() < sanity_lvl()):
                        $ show_chr ("A-AECAA-AAAF")
                        y "I couldn't honestly care less what difficulty we play at by this point."
                        y "N-No wait, you know what?"
                        y "This would make for a good opportunity to put you in your place, and I won't waste it."
                        y "Let's set it to veteran and see just how well you do."

                    else:
                        $ show_chr("A-AECAA-AAAF")
                        y "I couldn't honestly care less what difficulty we play at by this point."
                        y "N-No wait, you know what?"
                        y "This would make for a good opportunity to put you in your place, and I won't waste it."
                        $ show_chr ("A-AECAA-AAAG")
                        y "Let's set it to veteran and see just how well you do."

            # K&S are almost minimal.
            elif(abs(karma_lvl() + sanity_lvl()) < 2):
                if(randomMood == -1):
                    # Expert.
                    $ AI_difficulty = 5

                    $ show_chr("A-DBCAA-AAAF")
                    y "{b}HA HA...{/b}"
                    y "You want me to choose the difficulty?"
                    y "Fine [player], your wish is my command."
                    $ show_chr("A-DBCAA-AAAC")
                    y "How about expert hmm? Seems like a fair competition don't you think?"
                    $ show_chr("A-CBCAA-AAAC")
                    y "I just hope you'll be able to keep up the pace. It would be quite a shame if I decimated the scoreboard."

                else:
                    # Veteran.
                    $ AI_difficulty = 6

                    $ show_chr("A-DBCAA-AAAF")
                    y "{b}HA HA...{/b}"
                    y "You want me to choose the difficulty?"
                    y "Fine [player], your wish is my command."
                    $ show_chr("A-DBCAA-AAAC")
                    y "How about veteran hmm? Seems like a fair competition don't you think?"
                    $ show_chr("A-CBCAA-AAAC")
                    y "I just hope you'll be able to keep up the pace. It would be quite a shame if I decimated the scoreboard."


label tetris_rules:
    $ show_chr("A-GAGAA-AAAA")
    if persistent.tetris_first:
        y "Allow me to explain the controls..."
        y "You can use arrows to move your pieces. Hitting UP will rotate your piece, hitting DOWN will speed up your drop."
        y "Hitting SPACE will drop the piece instantaneously."
        y "Q key will put the piece into hold, but you can't double hold the same piece..."
        y "...While the E key will use the piece which you are holding."
        $ persistent.tetris_first = False

    menu:
        y "Would you like some Tetris music while we play?"
        "Yes":
            if AI_difficulty != "CO_OP":
                y "Let the best Tetris player win."
                $ show_chr("A-AACAA-AAAA")
                y "Game on, [player]!"
            else:
                y "Let's enjoy our time together trying to get the highest score!"
                $ show_chr("A-CBBAA-AAAJ")
                y "I really hope I will be at least some of help for you, [player]."
                $ show_chr("A-AACAA-AAAA")

            if persistent.skin == 1:
                $ change_music("<loop 21.06>/music/tetris (a).ogg") #Once a musician in the Dev Team Server has finished their Tetris arrangement, please remove this comment.
                #"<loop 1.81>/music/tetris (b).ogg"
            elif persistent.skin == 2:
                $ change_music("<loop 0.80>/music/tetris_99.ogg")
            elif persistent.skin == 3:
                $ change_music("<loop 19.30>/music/tetris_gb.ogg")
            elif persistent.skin == 4:
                $ change_music("<loop 0>/music/tetris_gmd.ogg")
            elif persistent.skin == 5:
                $ change_music("<loop 0>/music/tetris_m1nd_bend3r.ogg")
            elif persistent.skin == 6:
                $ change_music("<loop 0>/custom_tetris/tetris.ogg")
        "No":
            if AI_difficulty != "CO_OP":
                y "Let the best Tetris player win."
                $ show_chr("A-AACAA-AAAA")
                y "Game on, [player]!"
            else:
                y "Let's enjoy our time together trying to get the highest score!"
                $ show_chr("A-CBBAA-AAAJ")
                y "I really hope I will be at least some of help for you, [player]."
                $ show_chr("A-AACAA-AAAA")

    call screen startTetris(AI_difficulty)

label tetris_over:
    $ change_music(current_music)
    if TetrisWinner == 0:
        if karma_lvl() > 3 and sanity_lvl() > 3:
        #[If K= 4-5 and S= 4&5]
            $ show_chr("A-ABABA-AAAL")
            y "O-oh my!! Oh that was quite a little thrill~"
            y "I had enjoyment just being in that moment with you [player]. Even though I may have strived for a higher score."
            $ show_chr("A-CCAAA-AAAD")
            y "Really though, it is indeed the moment shared together and the heart that counts!"
            y "Hehehe... Though I will admit part of me does want to try again and see if I score higher."
            $ show_chr("A-ABAAA-AMAM")
            y "Either way I believe we both put our best effort!"
            menu:
                y "So [player], do you want to try again? Us together one more time?"
                "Yes":
                    menu:
                        y "Would you like the same music as our last game?"
                        "Yes":
                            if persistent.skin == 1:
                                $ change_music("<loop 21.06>/music/tetris (a).ogg") #Once a musician in the Dev Team Server has finished their Tetris arrangement, please remove this comment.
                            elif persistent.skin == 2:
                                $ change_music("<loop 0.80>/music/tetris_99.ogg")
                            elif persistent.skin == 3:
                                $ change_music("<loop 19.30>/music/tetris_gb.ogg")
                            elif persistent.skin == 4:
                                $ change_music("<loop 0>/music/tetris_gmd.ogg")
                            elif persistent.skin == 5:
                                $ change_music("<loop 0>/music/tetris_m1nd_bend3r.ogg")
                            elif persistent.skin == 6:
                                $ change_music("<loop 0>/custom_tetris/tetris.ogg")

                            call screen startTetris(AI_difficulty)

                        "No":
                            call screen startTetris(AI_difficulty)
                "No":
                    $ show_chr("A-GBAAA-AMAM")
                    y "I really enjoy playing with you. Let's do this again sometime soon."
                    jump ch30_loop

        elif karma_lvl() > 3 and sanity_lvl() == 3:
        #[If K=4-5 and S= 3]
            $ show_chr("A-BCAAA-AMAM")
            y "O-oh my... Oh I hope I did not slip up too much."
            y "Aheheh..."
            $ show_chr("A-BCABA-AMAM")
            y "I mean I obviously think your skills are lovely... I-I just don't want to b-bore you too much with mine... I mean! It was a lovely time and I appreciated it very much."
            $ show_chr("A-ACAAA-AAAC")
            menu:
                y "Anyways.. W-would you like to play this again with me [player]...?"
                "Yes":
                    call screen startTetris(AI_difficulty)
                    $ renpy.music.play()
                "No":
                    $ show_chr("A-GBAAA-AMAM")
                    y "I really enjoy playing with you. Let's do this again sometime soon."
                    jump ch30_loop

        elif karma_lvl() <= 2:
        #[If K = 1-2 regardless of S value]
            $ show_chr("A-ACAAA-AAAC")
            y "O-oh you won eh...?"
            y "I suppose now would be a good time to rub it in that you won over me."
            $ show_chr("A-ACAAA-AAAC")
            y "G-go ahead. Boast to your heart's content."
            y "I bet you only pretended to have fun playing against me..."
            y "Go on [player]."
        elif sanity_lvl() > 2 and karma_lvl() < 3:
            $ show_chr("A-ACAAA-AAAA")
            y "Congratulations, well done."
            y "I have to admit, that was more fun than I anticipated. Actually I was a bit worried that Tetris might become boring pretty fast."
            $ show_chr("A-ACAAA-ALAL")
            menu:
                y "I hope you had a bit of fun too? If you wish we could try another round. Are you up for a rematch?"
                "Yes":
                    call screen startTetris(AI_difficulty)
                    $ renpy.music.play()
                "No":
                    $ show_chr("A-GBAAA-AMAM")
                    y "I really enjoy playing with you. Let's do this again sometime soon."
                    jump ch30_loop

        elif sanity_lvl() <= 3 and karma_lvl() >= 3:
            $ show_chr("A-ACAAA-ABAB")
            y "Oh my, it looks like you've beaten me!"
            y "I might have to put more training into this, so that I can be an actual challenge next time."
            y "Actually, would you like to give it another try? Playing with you turned out to be a lot of fun, even if it's only Tetris."
            $ show_chr("A-BCAAA-ABAC")
            y "We could probably try something else in the future. Chess, or maybe a card game?"
            y "I also thought about darts, but honestly I have no idea how to code that in..."
            $ show_chr("A-ACAAA-ABAE")
            menu:
                y "Oh but I almost forgot, would you like to play another round with me?"
                "Yes":
                    call screen startTetris(AI_difficulty)
                    $ renpy.music.play()
                "No":
                    $ show_chr("A-GBAAA-AMAM")
                    y "I really enjoy playing with you. Let's do this again sometime soon."
                    jump ch30_loop

        elif sanity_lvl() <= 3 and karma_lvl() < 3:
            $ show_chr("A-BFAAA-ABAE")
            y "Congratulations, I guess?"
            $ show_chr("A-IFAAA-ABAE")
            y "Oh I'm sorry, I didn't mean to sound so unenthusiastic."
            y "It's just... I find it a bit difficult to focus right now. I can't help but ask myself how we ended up here like this."
            $ show_chr("A-CFAAA-ABAE")
            y "Forgive me, am I too dramatic? What I meant to say is.. I wish we were able to do more together than playing Tetris. Please don't read too much into it. "
            menu:
                extend "Would you like to play another round?"
                "Yes":
                    call screen startTetris(AI_difficulty)
                    $ renpy.music.play()
                "No":
                    jump ch30_loop

    elif TetrisWinner == 1:
        if sanity_lvl() > 2 and karma_lvl() > 2:
            $ show_chr("A-ACAAA-ALAL")#insert closed smile with open eyes, happy eyebrows and hand on her chest
            y "Oh my..."
            y "Good show, good effort~"
            $ show_chr("A-ACABA-AAAD")# open smile with a hand on her chin and blush on her face
            y "I know you wanted a higher score but there will always be a next time!"
            y "I hope you had fun, [player], I know I did!"

        elif karma_lvl() > 4 and sanity_lvl() == 3:
        #[If K=4-5 and S=3]
            $ show_chr("A-ACDAA-AMAM")
            y "O-oh... You lost? Uhm... eheh."
            y "I-I hope I did not get too intense for you. Don't feel bad about it [player]. I had a lot of fun."
            y "I hope you did too... O-oh... I mean but... We can do something else if you'd like. I really hope you enjoyed it though. I-It means so much to me... Just time together like this."
            y "Did I make you feel bad [player]? I hope I didn't... I'd give you a hug at least for your efforts..."
            $ show_chr("A-ACAAA-ABAB")
            y "It's the heart and thought that c-counts after all."
            y "S-so... do you want to play again? Or if you want to do something else, that is okay too [player]~"

        elif karma_lvl() != 3 and sanity_lvl() != 3:
        #[If K=3 and S=3]
            $ show_chr("A-BCABA-AMAM")
            y "W-well... This was quite intriguing to say the least."
            y "I am not exactly sure if this time together does count or whether it matters but... I am intrigued by this game of matching blocks and tiles."
            $ show_chr("A-JEDBA-AMAM")
            y "If you are here and hearing this [player] I would say this session was alright and I do feel slightly bad that you lost."
            y "M-maybe this activity might help me relax and get my bearings on getting used to here and maybe knowing you more?"
            $ show_chr("A-ACAAA-AAAC")
            y "I-I am not sure..."
            y "D-do you want to play a bit more [player]?"

        elif sanity_lvl() > 2 and karma_lvl() < 3:
            $ show_chr("A-AEAAA-AAAC")
            y "Oh... you lost, eh?"
            y "Well then that's no surprise, I guess."
            y "I mean, not that you would care for my input perhaps but.."
            $ show_chr("A-CEAAA-AAAL")
            y "Hm..."
            y "Well, I still hope you enjoyed playing... I guess."

        elif sanity_lvl() < 3 and karma_lvl() > 3:
        #If K= 4-5 and S: 1-2
            $ show_chr("A-ABAAA-AAAD")
            y "Aww... sorry [player]~"
            y "Looks like I won again uhuhuhu~"
            y "Don't feel too bad though, love..."
            y "I had an immensely pleasurable time just playing with you. Imagining seeing you so focused and determined with sweat running down your face as you tried to score."
            $ show_chr("A-HCCAA-AMAM")
            y "Your sweet sweat and essence... Your eyes focusing on mine as the colors of the game shone on your face. Only for me, and me alone."
            $ show_chr("A-HLAAA-AFAG")
            y "I look forward to another session with you as always [player]. Forever and just us.."
            y "No one ELSE!... Just us uhuhuhehehe...~"

        elif karma_lvl() == 3 and sanity_lvl() <= 2:
        #If K= 3 and S: 1-2
            $ show_chr("A-HLAAA-ALAL")
            y "Aww, you lost?"
            y "W-well hey don't feel bad and leave so soon..."
            y "We can stay here in this room together forever. Breathing in each others' scents as we sweat and play this wonderful classic together."
            $ show_chr("A-HCAAA-ALAL")
            y "Here in this room and no one else... I know you want to... And I want to also~"
            y "What do you say [player]? Doesn't that sound so heavenly?" #[maybe show this line as glitch text?]

        elif sanity_lvl() < 3 and karma_lvl() < 3:
            $ show_chr("A-DECAA-ABAB")# angry closed frown with angry eyes/eyebrows and hands on the table.
            y "Oh, so you lost, hm?"
            y "Well, that's not surprising."
            $ show_chr("A-CDCAA-AAAL")# open mouth frown with closed eyes and hand on chest
            y "That was honestly even quite... pathetic..."
            y "To be honest, I expected a greater challenge."

    elif TetrisWinner == 2:
        $ show_chr("A-IBCAA-AAAL")
        y "[player], We cleared  our highest Score!"
        $ show_chr("A-GBAAA-AAAL")
        y "That was quite the game, too..."
    else:
        $ show_chr("A-BEBAA-AMAM")
        y "I am sorry [player]...we fell short of our highest score."
        $ show_chr("A-CBAAA-AMAM")
        y "But fret not! There's always next time..."

    jump ch30_loop

screen startTetris(AI_difficulty):
    if AI_difficulty != "CO_OP":
        fixed:
            area (150, 120, 600, 1100)
            if AI_difficulty < 7:
                default tetris_player = tetris(0)
            else:
                default tetris_player = tetris(-1)
            add tetris_player

        fixed:
            area (900, 120, 600, 1100)
            default tetris_Yuri = tetris(AI_difficulty)
            add tetris_Yuri
    else:
        fixed:
            area (50, 120, 600, 1100)
            default tetris_Co_OP = Co_OP_tetris()
            add tetris_Co_OP

init python:
#-----------------------------------------Tetris----------------------------------------------------#
    import pygame
    class tetris(renpy.Displayable):
        def __init__(self, AI):
            renpy.Displayable.__init__(self)
            if AI == -1:
                self.put_shadow = 0
                self.AI = AI + 1
            else:
                self.put_shadow = 1
                self.AI = AI
            self.movesAI = []
            self.PIXEL_SIZE = 20
            self.piece_list = [0,1,2,3,4,5,6]
            random.shuffle(self.piece_list)
            self.tetris_shapes = [
                [[1, 1, 1],
                [0, 1, 0]],

                [[0, 2, 2],
                [2, 2, 0]],

                [[3, 3, 0],
                [0, 3, 3]],

                [[4, 0, 0],
                [4, 4, 4]],

                [[0, 0, 5],
                [5, 5, 5]],

                [[6, 6, 6, 6]],

                [[7, 7],
                [7, 7]]
            ]

            self.stage = [[9,9,9,9,9,9,9,9,9,9,9,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,9],
                        [9,9,9,9,9,9,9,9,9,9,9,9]]

            if persistent.skin == 1:

                self.color_1 = Image("images/tetris/tetris/cube_1.png")
                self.color_2 = Image("images/tetris/tetris/cube_2.png")
                self.color_3 = Image("images/tetris/tetris/cube_3.png")
                self.color_4 = Image("images/tetris/tetris/cube_4.png")
                self.color_5 = Image("images/tetris/tetris/cube_5.png")
                self.color_6 = Image("images/tetris/tetris/cube_6.png")
                self.color_7 = Image("images/tetris/tetris/cube_7.png")
                self.color_9 = Image("images/tetris/tetris/cube_8.png")

                self.shadow_color_1 = Image("images/tetris/tetris/cube_1.png")
                self.shadow_color_2 = Image("images/tetris/tetris/cube_2.png")
                self.shadow_color_3 = Image("images/tetris/tetris/cube_3.png")
                self.shadow_color_4 = Image("images/tetris/tetris/cube_4.png")
                self.shadow_color_5 = Image("images/tetris/tetris/cube_5.png")
                self.shadow_color_6 = Image("images/tetris/tetris/cube_6.png")
                self.shadow_color_7 = Image("images/tetris/tetris/cube_7.png")

                self.score = 0

                self.playsounds = True
                self.soundbdrop = "sfx/t-drop.ogg"
                self.soundline = "sfx/t-fl.ogg"
                self.soundldrop = "sfx/t-fl-drop.ogg"
                self.soundmove = "sfx/t-move.ogg"
                self.soundrotate = "sfx/t-rotate.ogg"
                self.sound2line = "sfx/t-2fl.ogg"
                self.sound3line = "sfx/t-3fl.ogg"
                self.sound4line = "sfx/t-4fl.ogg"

            elif persistent.skin == 2:

                self.color_1 = Image("images/tetris/tetris_99/cube_1.png")
                self.color_2 = Image("images/tetris/tetris_99/cube_2.png")
                self.color_3 = Image("images/tetris/tetris_99/cube_3.png")
                self.color_4 = Image("images/tetris/tetris_99/cube_4.png")
                self.color_5 = Image("images/tetris/tetris_99/cube_5.png")
                self.color_6 = Image("images/tetris/tetris_99/cube_6.png")
                self.color_7 = Image("images/tetris/tetris_99/cube_7.png")
                self.color_9 = Image("images/tetris/tetris_99/cube_8.png")

                self.shadow_color_1 = Image("images/tetris/tetris_99/cube_1.png")
                self.shadow_color_2 = Image("images/tetris/tetris_99/cube_2.png")
                self.shadow_color_3 = Image("images/tetris/tetris_99/cube_3.png")
                self.shadow_color_4 = Image("images/tetris/tetris_99/cube_4.png")
                self.shadow_color_5 = Image("images/tetris/tetris_99/cube_5.png")
                self.shadow_color_6 = Image("images/tetris/tetris_99/cube_6.png")
                self.shadow_color_7 = Image("images/tetris/tetris_99/cube_7.png")

                self.score = 0

                self.playsounds = True
                self.soundbdrop = "sfx/t-drop(99).ogg"
                self.soundline = "sfx/t-fl(99).ogg"
                self.soundldrop = "sfx/t-fl-drop(99).ogg"
                self.soundmove = "sfx/t-move(99).ogg"
                self.soundrotate = "sfx/t-rotate(99).ogg"
                self.sound2line = "sfx/t-2fl(99).ogg"
                self.sound3line = "sfx/t-3fl(99).ogg"
                self.sound4line = "sfx/t-4fl(99).ogg"

            elif persistent.skin == 3:

                self.color_1 = Image("images/tetris/tetris_gb/cube_1.png")
                self.color_2 = Image("images/tetris/tetris_gb/cube_2.png")
                self.color_3 = Image("images/tetris/tetris_gb/cube_3.png")
                self.color_4 = Image("images/tetris/tetris_gb/cube_4.png")
                self.color_5 = Image("images/tetris/tetris_gb/cube_5.png")
                self.color_6 = Image("images/tetris/tetris_gb/cube_6.png")
                self.color_7 = Image("images/tetris/tetris_gb/cube_7.png")
                self.color_9 = Image("images/tetris/tetris_gb/cube_8.png")

                self.shadow_color_1 = Image("images/tetris/tetris_gb/cube_1.png")
                self.shadow_color_2 = Image("images/tetris/tetris_gb/cube_2.png")
                self.shadow_color_3 = Image("images/tetris/tetris_gb/cube_3.png")
                self.shadow_color_4 = Image("images/tetris/tetris_gb/cube_4.png")
                self.shadow_color_5 = Image("images/tetris/tetris_gb/cube_5.png")
                self.shadow_color_6 = Image("images/tetris/tetris_gb/cube_6.png")
                self.shadow_color_7 = Image("images/tetris/tetris_gb/cube_7.png")

                self.score = 0

                self.playsounds = True
                self.soundbdrop = "sfx/t-drop.ogg"
                self.soundline = "sfx/t-fl.ogg"
                self.soundldrop = "sfx/t-fl-drop.ogg"
                self.soundmove = "sfx/t-move.ogg"
                self.soundrotate = "sfx/t-rotate.ogg"
                self.sound2line = "sfx/t-2fl.ogg"
                self.sound3line = "sfx/t-3fl.ogg"
                self.sound4line = "sfx/t-4fl.ogg"

            elif persistent.skin == 4:


                self.color_1 = Image("images/tetris/tetris_gmd/cube_1.png")
                self.color_2 = Image("images/tetris/tetris_gmd/cube_2.png")
                self.color_3 = Image("images/tetris/tetris_gmd/cube_3.png")
                self.color_4 = Image("images/tetris/tetris_gmd/cube_4.png")
                self.color_5 = Image("images/tetris/tetris_gmd/cube_5.png")
                self.color_6 = Image("images/tetris/tetris_gmd/cube_6.png")
                self.color_7 = Image("images/tetris/tetris_gmd/cube_7.png")
                self.color_9 = Image("images/tetris/tetris_gmd/cube_8.png")

                self.shadow_color_1 = Image("images/tetris/tetris_gmd/cube_1.png")
                self.shadow_color_2 = Image("images/tetris/tetris_gmd/cube_2.png")
                self.shadow_color_3 = Image("images/tetris/tetris_gmd/cube_3.png")
                self.shadow_color_4 = Image("images/tetris/tetris_gmd/cube_4.png")
                self.shadow_color_5 = Image("images/tetris/tetris_gmd/cube_5.png")
                self.shadow_color_6 = Image("images/tetris/tetris_gmd/cube_6.png")
                self.shadow_color_7 = Image("images/tetris/tetris_gmd/cube_7.png")

                self.score = 0

                self.playsounds = True
                self.soundbdrop = "sfx/t-drop(g).ogg"
                self.soundline = "sfx/t-fl(g).ogg"
                self.soundldrop = "sfx/t-fl-drop(g).ogg"
                self.soundmove = "sfx/t-move(g).ogg"
                self.soundrotate = "sfx/t-rotate(g).ogg"
                self.sound2line = "sfx/t-2fl(g).ogg"
                self.sound3line = "sfx/t-3fl(g).ogg"
                self.sound4line = "sfx/t-4fl(g).ogg"

            elif persistent.skin == 5:


                self.color_1 = Image("images/tetris/tetris_mb/cube_1.png")
                self.color_2 = Image("images/tetris/tetris_mb/cube_2.png")
                self.color_3 = Image("images/tetris/tetris_mb/cube_3.png")
                self.color_4 = Image("images/tetris/tetris_mb/cube_4.png")
                self.color_5 = Image("images/tetris/tetris_mb/cube_5.png")
                self.color_6 = Image("images/tetris/tetris_mb/cube_6.png")
                self.color_7 = Image("images/tetris/tetris_mb/cube_7.png")
                self.color_9 = Image("images/tetris/tetris_mb/cube_8.png")

                self.shadow_color_1 = Image("images/tetris/tetris_mb/shadow_1.png")
                self.shadow_color_2 = Image("images/tetris/tetris_mb/shadow_2.png")
                self.shadow_color_3 = Image("images/tetris/tetris_mb/shadow_3.png")
                self.shadow_color_4 = Image("images/tetris/tetris_mb/shadow_4.png")
                self.shadow_color_5 = Image("images/tetris/tetris_mb/shadow_5.png")
                self.shadow_color_6 = Image("images/tetris/tetris_mb/shadow_6.png")
                self.shadow_color_7 = Image("images/tetris/tetris_mb/shadow_7.png")

                self.score = 0

                self.playsounds = True
                self.soundbdrop = "sfx/t-drop(mb).ogg"
                self.soundline = "sfx/t-fl(mb).ogg"
                self.soundldrop = "sfx/t-fl-drop(mb).ogg"
                self.soundmove = "sfx/t-move(mb).ogg"
                self.soundrotate = "sfx/t-rotate(mb).ogg"
                self.sound2line = "sfx/t-2fl(mb).ogg"
                self.sound3line = "sfx/t-3fl(mb).ogg"
                self.sound4line = "sfx/t-4fl(mb).ogg"

            elif persistent.skin == 6:


                self.color_1 = Image("/custom_tetris/cube_1.png")
                self.color_2 = Image("/custom_tetris/cube_2.png")
                self.color_3 = Image("/custom_tetris/cube_3.png")
                self.color_4 = Image("/custom_tetris/cube_4.png")
                self.color_5 = Image("/custom_tetris/cube_5.png")
                self.color_6 = Image("/custom_tetris/cube_6.png")
                self.color_7 = Image("/custom_tetris/cube_7.png")
                self.color_9 = Image("/custom_tetris/cube_8.png")

                self.shadow_color_1 = Image("/custom_tetris/shadow_1.png")
                self.shadow_color_2 = Image("/custom_tetris/shadow_2.png")
                self.shadow_color_3 = Image("/custom_tetris/shadow_3.png")
                self.shadow_color_4 = Image("/custom_tetris/shadow_4.png")
                self.shadow_color_5 = Image("/custom_tetris/shadow_5.png")
                self.shadow_color_6 = Image("/custom_tetris/shadow_6.png")
                self.shadow_color_7 = Image("/custom_tetris/shadow_7.png")

                self.score = 0

                self.playsounds = True
                self.soundbdrop = "/custom_tetris/t-drop.ogg"
                self.soundline = "/custom_tetris/t-fl.ogg"
                self.soundldrop = "/custom_tetris/t-fl-drop.ogg"
                self.soundmove = "/custom_tetris/t-move.ogg"
                self.soundrotate = "/custom_tetris/t-rotate.ogg"
                self.sound2line = "/custom_tetris/t-2fl.ogg"
                self.sound3line = "/custom_tetris/t-3fl.ogg"
                self.sound4line = "/custom_tetris/t-4fl.ogg"


            class current_shape:
                shape = ""
                shape_number = ""
                shape_hold = ""
                new_shape_number = self.piece_list[0]
                next_shape = self.tetris_shapes[new_shape_number]
                x = 5
                y = 1
                move_time = 0.300
                speed = 0.60 - 2
            self.was_it_hold = False
            self.temp_position = 3
            self.current_shape = current_shape()
            self.level = 1
            self.allLines = 0
            self.oldst = None
            self.new_shape = True
            self.game_over = False
            self.winner = None
            self.Yuri_Face = 0

        #Function which add shape to stage.
        #Arguments current x and y position of shape in stage
        def addShapeToStage(self, current_x, current_y):
            for idr, row in enumerate(self.current_shape.shape):
                for idc, column in enumerate(row):
                    if column != 0:
                        self.stage[current_y+idr][current_x+idc]=column

        def render(self, width, height, st, at):
            global PlayerForYuri
            #Win/lose conditions
            def winner(win):
                global TetrisWinner
                if win == 0:
                    if self.AI == 0:
                        TetrisWinner = 0   #Yuri lose
                    else:
                        TetrisWinner = 1   #Player lose
                else:
                    if self.AI == 0:
                        TetrisWinner = 1   #Player lose
                    else:
                        TetrisWinner = 0   #Yuri lose

            for idc in range(4, 8):
                if self.stage[1][idc] != 0:
                    self.game_over = True
                    winner(1)

            if TetrisScore !=0:
                if self.score >= TetrisScore:
                    self.game_over = True
                    winner(0)

            elif LineLimit !=0:
                if self.allLines >= LineLimit:
                    self.game_over = True
                    winner(0)

            if self.game_over:
                import pygame
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            renpy.jump("tetris_over")

            ####################################################################################
            #Function which check if there are lines. If yes, add it to score and return new stage
            def lines():
                numberOfFullLines = 0
                #Check if there are any lines and fix stage
                prevLine = False
                for idr in range(1, 21):
                    fullLine = True
                    for idc in range(1, 11):
                        if self.stage[idr][idc] == 0:
                            fullLine = False
                            break
                    if fullLine:
                        numberOfFullLines += 1
                        renpy.sound.play(self.soundline)
                        for idc in range(1, 11):
                            self.stage[idr][idc] = 0
                        if prevLine != fullLine:
                            for i in range(0, idr-1):
                                for idc in range(1, 11):
                                    self.stage[idr-i][idc] = self.stage[idr-i-1][idc]
                                    self.stage[idr-i-1][idc] = 0
                                    fullLine = False
                    prevLine = fullLine

                #Score points depending on how many lines there were cleared
                self.allLines += numberOfFullLines
                if numberOfFullLines == 1:
                    self.score += 100 * self.level
                elif numberOfFullLines == 2:
                    self.score += 300 * self.level
                    renpy.sound.play(self.sound2line)
                elif numberOfFullLines == 3:
                    self.score += 500 * self.level
                    renpy.sound.play(self.sound3line)
                elif numberOfFullLines == 4:
                    self.score += 800 * self.level
                    renpy.sound.play(self.sound4line)
                self.level =  int(self.allLines/10)+1
            #################################################################################
            r = renpy.Render(width, height)
            if persistent.skin == 1:
                if AI_difficulty >= 4:
                    background = renpy.render(Image("images/tetris/tetris/background_no_grind.png"), width, height, st, at)
                else:
                    background = renpy.render(Image("images/tetris/tetris/background.png"), width, height, st, at)

            elif persistent.skin == 2:
                if AI_difficulty >= 4:
                    background = renpy.render(Image("images/tetris/tetris_99/background_no_grind.png"), width, height, st, at)
                else:
                    background = renpy.render(Image("images/tetris/tetris_99/background.png"), width, height, st, at)

            elif persistent.skin == 3:
                if AI_difficulty >= 4:
                    background = renpy.render(Image("images/tetris/tetris_gb/background_no_grind.png"), width, height, st, at)
                else:
                    background = renpy.render(Image("images/tetris/tetris_gb/background.png"), width, height, st, at)

            elif persistent.skin == 4:
                if AI_difficulty >= 4:
                    background = renpy.render(Image("images/tetris/tetris_gmd/background_no_grind.png"), width, height, st, at)
                else:
                    background = renpy.render(Image("images/tetris/tetris_gmd/background.png"), width, height, st, at)

            elif persistent.skin == 5:
                if AI_difficulty >= 4:
                    background = renpy.render(Image("images/tetris/tetris_mb/background_no_grind.png"), width, height, st, at)
                else:
                    background = renpy.render(Image("images/tetris/tetris_mb/background.png"), width, height, st, at)

            elif persistent.skin == 6:
                if AI_difficulty >= 4:
                    background = renpy.render(Image("/custom_tetris/background_no_grind.png"), width, height, st, at)
                else:
                    background = renpy.render(Image("/custom_tetris/background.png"), width, height, st, at)
            r.blit(background, (0, 0))
            lines()
            if self.new_shape:
                self.was_it_hold = False
                self.current_shape.x = 5
                self.current_shape.y = 1
                self.current_shape.shape = self.current_shape.next_shape
                self.current_shape.shape_number = self.current_shape.new_shape_number
                self.piece_list.pop(0)
                if not self.piece_list:
                    self.piece_list = [0,1,2,3,4,5,6]
                    random.shuffle(self.piece_list)
                self.current_shape.new_shape_number = self.piece_list[0]
                self.current_shape.next_shape = self.tetris_shapes[self.current_shape.new_shape_number]
                self.new_shape = False
                self.temp_position = 1
                if self.AI != 0:
                    temp_AI = True
                    for idc in range(1, 11):
                        if self.stage[2][idc] != 0:
                            temp_AI = False
                    if temp_AI:
                        self.movesAI = self.Yuri_AI()

            if self.oldst is None:
                self.oldst = st
            if self.level > 19:
                speed_Y = 18
            else:
                speed_Y = self.level
            if self.AI == 1:
                if self.current_shape.y >= 10:
                    self.current_shape.speed = 0.30
            elif self.AI == 2:
                if self.current_shape.y >= 5:
                    self.current_shape.speed = 0.15
            elif self.AI == 3:
                if self.current_shape.y >= 2.5:
                    self.current_shape.speed = 0.075
            elif self.AI == 4:
                if self.current_shape.y >= 0.625:
                    self.current_shape.speed = 0.0375 - 13
            elif self.AI == 5:
                if self.current_shape.y >= 0.3125:
                    self.current_shape.speed = 0.01875 - 26
            elif self.AI == 6:
                if self.current_shape.y >= 0.15625:
                    self.current_shape.speed = 0.009375 - 39

            if self.temp_position == self.current_shape.y:
                if len(self.movesAI) != 0:
                    if self.movesAI[0] == "r":
                        self.rotateClockWiseAI()
                    else:
                        self.current_shape.x += int(self.movesAI[0])
                    del self.movesAI[0]
                    self.temp_position += 1

            dtime = st - self.oldst
            self.oldst = st
            temp_can_go_down = True
            if self.current_shape.move_time <= 0:
                # Check if bottom is empty
                for idr, row in enumerate(self.current_shape.shape):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if self.stage[self.current_shape.y + 1 + idr][self.current_shape.x + idc] != 0:
                                temp_can_go_down = False
                                renpy.sound.play(self.soundbdrop)
                                break
                if temp_can_go_down != False:
                    self.current_shape.move_time = self.current_shape.speed
                    self.current_shape.y += 1
                else:
                    self.new_shape = True
                    self.addShapeToStage(self.current_shape.x, self.current_shape.y)
            else:
                self.current_shape.move_time -= dtime

            def draw_shape(sx, sy, current_shape,shadow):
                for idr, row in enumerate(current_shape):
                    for idc, column in enumerate(row):
                        if column == 1:
                            shape = renpy.render(self.color_1, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if self.put_shadow == 1 and shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_1, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape.y)))
                        elif column == 2:
                            shape = renpy.render(self.color_2, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if self.put_shadow == 1 and shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_2, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape.y)))
                        elif column == 3:
                            shape = renpy.render(self.color_3, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if self.put_shadow == 1 and shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_3, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape.y)))
                        elif column == 4:
                            shape = renpy.render(self.color_4, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if self.put_shadow == 1 and shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_4, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape.y)))
                        elif column == 5:
                            shape = renpy.render(self.color_5, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if self.put_shadow == 1 and shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_5, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape.y)))
                        elif column == 6:
                            shape = renpy.render(self.color_6, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if self.put_shadow == 1 and shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_6, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape.y)))
                        elif column == 7:
                            shape = renpy.render(self.color_7, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if self.put_shadow == 1 and shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_7, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape.y)))
                        elif column == 9:
                            shape = renpy.render(self.color_9, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))

            b = "Lines - %(s)d " % {"s":self.allLines }
            c = "Level - %(s)d " % {"s":self.level}
            d = "Next:"

            f = Text(b)
            g = Text(c)
            h = Text(d)

            text_allLines_render = renpy.render(f, width, height, st, at)
            text_level_render = renpy.render(g, width, height, st, at)
            text_next_render = renpy.render(h, width, height, st, at)


            if self.AI == 0:
                r.blit(text_allLines_render, (-120, -100))
                r.blit(text_level_render, (-120, -50))
                r.blit(text_next_render, (-120, -10))
                draw_shape(-100, 40, self.current_shape.next_shape,0)
                i = "Hold:"
                j = Text(i)
                text_hold_render = renpy.render(j, width, height, st, at)
                r.blit(text_hold_render, (-120, 100))
                draw_shape(-100, 160, self.current_shape.shape_hold,0)
                if LineLimit != 0:
                    i = "Line to Victory - %(s)d " % {"s":LineLimit}
                    j = Text(i)
                    text_line = renpy.render(j, width, height, st, at)
                    r.blit(text_line, (420, -100))
                    PlayerForYuri = self.allLines
                elif TetrisScore != 0:
                    a = "Score - %(s)d " % {"s":self.score }
                    e = Text(a)
                    text_score_render = renpy.render(e, width, height, st, at)
                    r.blit(text_score_render, (30, -100))
                    PlayerForYuri = self.score
            else:
                if LineLimit != 0 and (self.allLines > LineLimit/6 or PlayerForYuri > LineLimit/6):
                    if self.Yuri_Face <> 1 and self.allLines > PlayerForYuri:
                        if persistent.skin == 1:
                            music_swap = True
                            if music_swap:
                                change_music("<loop 1.81>/music/tetris (b).ogg")
                                music_swap = False
                            elif not music_swap:
                                pass
                        show_chr("A-ABDAA-AAAJ")
                        self.Yuri_Face = 1
                        renpy.restart_interaction()
                    elif self.Yuri_Face <> 2 and self.allLines < PlayerForYuri:
                        if persistent.skin == 1:
                            music_swap = True
                            if music_swap:
                                change_music("<loop 1.81>/music/tetris (b).ogg")
                                music_swap = False
                            elif not music_swap:
                                pass
                        show_chr("A-DEBAA-AMAM")
                        self.Yuri_Face = 2
                        renpy.restart_interaction()
                elif TetrisScore != 0 and (self.score > TetrisScore/6 or PlayerForYuri > TetrisScore/6):
                    if self.Yuri_Face <> 1 and self.score > PlayerForYuri:
                        if persistent.skin == 1:
                            music_swap = True
                            if music_swap:
                                change_music("<loop 1.81>/music/tetris (b).ogg")
                                music_swap = False
                            elif not music_swap:
                                pass
                        show_chr("A-ABDAA-AAAJ")
                        self.Yuri_Face = 1
                        renpy.restart_interaction()
                    elif self.Yuri_Face <> 2 and self.score < PlayerForYuri:
                        if persistent.skin == 1:
                            music_swap = True
                            if music_swap:
                                change_music("<loop 1.81>/music/tetris (b).ogg")
                                music_swap = False
                            elif not music_swap:
                                pass
                        show_chr("A-DEBAA-AMAM")
                        self.Yuri_Face = 2
                        renpy.restart_interaction()

                r.blit(text_allLines_render, (250, -100))
                r.blit(text_level_render, (250, -50))
                r.blit(text_next_render, (250, -10))
                if TetrisScore != 0:
                    a = "Score - %(s)d " % {"s":self.score }
                    e = Text(a)
                    text_score_render = renpy.render(e, width, height, st, at)
                    r.blit(text_score_render, (30, -100))
                draw_shape(280, 40, self.current_shape.next_shape,0)

            draw_shape(0, 0, self.stage,0)
            draw_shape(self.current_shape.x*self.PIXEL_SIZE, self.current_shape.y*self.PIXEL_SIZE, self.current_shape.shape,1)

            renpy.redraw(self, 0)
            return r
        ############################################################################################################################
        # Rotate piecec functions
        def rotateClockWise(self, mat):
            tempShape = mat
            tempRow = tempShape
            tempX = self.current_shape.x
            tempY = self.current_shape.y
            ifRotation = True
            renpy.sound.play(self.soundrotate)
            lenRow = len(mat)
            lenCol = len(mat[0])
            #Rotation of Long I piece:
            # I to -
            if lenRow == 4:
                tempRow = [[] for _ in range(lenCol)]
                for idr, row in enumerate(mat):
                    lenColumn = len(row)
                    for idc, column in enumerate(row):
                        tempRow[idc].insert(0,column)
                self.current_shape.y+=1
                if self.stage[self.current_shape.y][self.current_shape.x-1] == 0:
                    self.current_shape.x-=1
                for idc, row in enumerate(tempRow[0]):
                    if self.stage[self.current_shape.y][self.current_shape.x+idc] != 0:
                        ifRotation = False
                        break
            # - to I
            elif lenRow == 1:
                tempRow = [[] for _ in range(lenCol)]
                for idr, row in enumerate(mat):
                    lenColumn = len(row)
                    for idc, column in enumerate(row):
                        tempRow[idc].insert(0,column)
                self.current_shape.y-=1
                self.current_shape.x+=1
                for idr, row in enumerate(tempRow):
                    if self.stage[self.current_shape.y+idr][self.current_shape.x] != 0:
                        ifRotation = False
                        break
            #Rotation of Z,L ,T piece
            # xxx    xx
            # xxx to xx
            #        xx
            elif lenRow == 2 and lenCol != 2:
                tempRow = [[] for _ in range(lenCol)]
                for idr, row in enumerate(mat):
                    lenColumn = len(row)
                    for idc, column in enumerate(row):
                        tempRow[idc].insert(0,column)
                for idr, row in enumerate(tempRow):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if self.stage[self.current_shape.y+idr][self.current_shape.x+idc] != 0:
                                ifRotation = False
                                break
            # xx    xxx
            # xx to xxx
            # xx
            elif lenRow == 3:
                tempRow = [[] for _ in range(lenCol)]
                for idr, row in enumerate(mat):
                    lenColumn = len(row)
                    for idc, column in enumerate(row):
                        tempRow[idc].insert(0,column)
                if self.stage[self.current_shape.y][self.current_shape.x+len(tempRow[0])-1] != 0:
                    self.current_shape.x-=1
                for idr, row in enumerate(tempRow):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if self.stage[self.current_shape.y+idr][self.current_shape.x+idc] != 0:
                                ifRotation = False
                                break
            elif lenRow == 2 and lenCol == 2:
                ifRotation = True
            #Fail the rotation, back to orginal position
            if ifRotation == False:
                tempRow = tempShape
                self.current_shape.x = tempX
                self.current_shape.y = tempY
            return tempRow
            ###################################################################################################################

        def find_bottom(self):
            temp_y = 0
            for idr in range(self.current_shape.y+len(self.current_shape.shape)-1, 22):
                for idc, column in enumerate(self.current_shape.shape[0]):
                    if self.stage[idr][self.current_shape.x + idc ] != 0:
                        temp_y = idr-len(self.current_shape.shape)
                        break
                if temp_y != 0:
                    break
            for position in range(0, 4):
                temp_fit = True
                for idr, row in enumerate(self.current_shape.shape):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if self.stage[temp_y+idr][self.current_shape.x + idc] != 0:
                                temp_fit = False
                                break
                if temp_fit:
                    temp_y += 1
                else:
                    temp_y -= 1
                    break
            return temp_y

        def player_t_spin(shape, stage):
            if shape[0][1] != 0 and shape[1][0] != 0 and shape[1][2] != 0 and shape[2][1] != 0:
                return True
            elif shape[0][1] == 0 and shape[1][0] == 0 and shape[1][2] != 0 and shape[2][1] != 0:
                return True
            elif shape[0][1] != 0 and shape[1][0] != 0 and shape[1][2] == 0 and shape[2][1] != 0:
                return True
            elif shape[0][1] != 0 and shape[1][0] != 0 and shape[1][2] != 0 and shape[2][1] == 0:
                return True
            else:
                return False

        def event(self, ev, x, y, st):
            import pygame
            temp_can_left = True
            temp_can_right = True
            if self.level > 19:
                self.current_shape.speed = 0.20
            else:
                self.current_shape.speed = 0.20
            if ev.type == pygame.KEYDOWN and self.AI == 0:
                if ev.key == pygame.K_UP:
                    self.current_shape.shape = self.rotateClockWise(self.current_shape.shape)
                elif ev.key == pygame.K_LEFT:
                    renpy.sound.play(self.soundmove)
                    for idr, row in enumerate(self.current_shape.shape):
                        for idc, column in enumerate(row):
                            if column != 0:
                                if self.stage[self.current_shape.y + idr][self.current_shape.x - 1 + idc] != 0:
                                    temp_can_left = False
                                    break
                    if temp_can_left:
                        self.current_shape.x -= 1
                elif ev.key == pygame.K_RIGHT:
                    renpy.sound.play(self.soundmove)
                    for idr, row in enumerate(self.current_shape.shape):
                        for idc, column in enumerate(row):
                            if column != 0:
                                if self.stage[self.current_shape.y + idr][self.current_shape.x + 1 + idc ] != 0:
                                    temp_can_right = False
                                    break
                    if temp_can_right:
                        self.current_shape.x += 1
                elif ev.key == pygame.K_DOWN:
                    self.current_shape.speed = 0.002
                elif ev.key == pygame.K_SPACE:
                    #if player_t_spin(self.current_shape.shape, self.stage):
                    #    renpy.sound.play(self.soundbdrop)
                    #    self.addShapeToStage(self.current_shape.x, self.find_bottom())
                    #    self.new_shape = True
                    #else:
                    renpy.sound.play(self.soundbdrop)
                    self.addShapeToStage(self.current_shape.x, self.find_bottom())
                    self.new_shape = True
                elif ev.key == pygame.K_q and self.current_shape.shape_hold == "" and self.was_it_hold ==False:
                    self.current_shape.shape_hold = self.current_shape.shape
                    self.new_shape = True
                elif ev.key == pygame.K_e and self.current_shape.shape_hold != "":
                    self.current_shape.next_shape = self.current_shape.shape
                    self.current_shape.shape = self.current_shape.shape_hold
                    self.current_shape.shape_hold = ""
                    self.current_shape.x = 5
                    self.current_shape.y = 1
                    self.was_it_hold = True

        def rotateClockWiseAI(self):
            lenRow = len(self.current_shape.shape)
            lenCol = len(self.current_shape.shape[0])
            tempRow = [[] for _ in range(lenCol)]
            for idr, row in enumerate(self.current_shape.shape):
                for idc, column in enumerate(row):
                    tempRow[idc].insert(0,column)
            del self.current_shape.shape
            self.current_shape.shape = tempRow

        def find_t_spin(shape, stage):
            if shape[0][1] == 0 or shape[1][0] == 0 or shape[1][2] == 0 or shape[2][1] == 0:
                # The shape is a T-shape.
                for x in range(1, 11):
                    # Check if there is a valid T-Spin move to the left.
                    if stage[1][x] == 0 and stage[0][x-1] != 0 and stage[1][x-1] != 0 and stage[2][x-1] != 0:
                        return -1
                    # Check if there is a valid T-Spin move to the right.
                    if stage[1][x] == 0 and stage[0][x+2] != 0 and stage[1][x+2] != 0 and stage[2][x+2] != 0:
                        return 1
            return 0

        def Yuri_AI(self):
            # Find the best T-Spin move.
            t_spin_move = find_t_spin(self.current_shape.shape, self.stage)
            # If there is a valid T-Spin move, make it.
            if t_spin_move != 0:
                self.current_shape.x += t_spin_move
            # Otherwise, find the best regular move.
            else:
                moves = bestMove()
                # Rotate the shape the correct number of times.
                for i in range(0, moves[1]-1):
                    self.rotateClockWiseAI()
                # Move the shape to the correct position.
                signbit = 1 if moves[0] < 0 else 0
                if signbit == 0:
                    for i in range(0, moves[0]):
                        self.current_shape.x += 1
                else:
                    for i in range(moves[0], 0):
                        self.current_shape.x -= 1

#----------------------------------------------------------------------------------------------------

        def Yuri_AI(self):
            def calculateScoreForMove():
                height = 0
                lines = 0
                holes = 0
                temp_col_height = [None] * 10
                bumpiness = 0
                #Caluclate height and lines
                for idr in range(20, 0, -1):
                    temp_clear_line = True
                    for idc in range(1, 11):
                        if self.stage[idr][idc] == 0:
                            temp_clear_line = False
                            break
                    if temp_clear_line:
                        lines += 1
                #Caluclate holes and bumpiness
                for idc in range(1, 11):
                    temp_col_height[idc-1] = 0
                    temp_holes = 0
                    for idr in range(20, 0, -1):
                        if self.stage[idr][idc] != 0:
                            holes += temp_holes
                            temp_holes = 0
                        else:
                            temp_holes += 1
                        if self.stage[idr][idc] != 0:
                            temp_col_height[idc-1] = 21-idr
                for i in range(0, 9):
                    height += temp_col_height[i]
                    bumpiness += abs(temp_col_height[i] - temp_col_height[i+1])
                height += temp_col_height[9]
                score = (-0.510066 * height) + (0.760666 * lines) - (0.35663 * holes) - (0.184483 * bumpiness)
                return score

            def shapeRotation(shape):
                if shape == 6:
                    return 2
                elif shape == 0 or shape == 3 or shape == 4:
                    return 5
                elif shape == 1 or shape == 2 or shape == 5:
                    return 3

            ####################################################################################################################
            def bestMove():
                import copy
                moves = []
                best_score = -100
                temp_shape = copy.deepcopy(self.current_shape.shape)
                temp_rotation = shapeRotation(self.current_shape.shape_number)

                #Find best position
                temp_stage = copy.deepcopy(self.stage)
                for rot in range(1, temp_rotation):
                    temp_len = len(self.current_shape.shape[0])-1
                    for idc in range(1, 11-temp_len):
                        del self.stage
                        self.stage = copy.deepcopy(temp_stage)
                        temp_break = False
                        for idr in range(1, 22):
                            for idcShape in range(0, len(self.current_shape.shape[0])):
                                if self.current_shape.shape[len(self.current_shape.shape)-1][idcShape] != 0:
                                    if self.stage[idr][idc+idcShape] != 0:
                                        temp_idr = idr
                                        temp_break = True
                                        break
                            if temp_break:
                                break
                        for idr in range(0, 21):
                            temp_free = True
                            temp_idr -= 1
                            for idrShape, row in enumerate(self.current_shape.shape):
                                for idcShape, column in enumerate(row):
                                    if column != 0:
                                        if self.stage[temp_idr+(idrShape-(len(self.current_shape.shape)-1))][idc+idcShape] != 0:
                                            temp_free = False
                            if temp_free:
                                self.addShapeToStage(idc, temp_idr-(len(self.current_shape.shape)-1))
                                temp_score = calculateScoreForMove()
                                if temp_score > best_score:
                                    best_score = temp_score
                                    moves = [idc-5, rot]
                                break
                    self.rotateClockWiseAI()
                self.stage = copy.deepcopy(temp_stage)
                del temp_stage
                self.current_shape.shape = copy.deepcopy(temp_shape)
                del temp_shape

                temp_moves = []
                for i in range(0, moves[1]-1):
                    temp_moves.append("r")
                signbit = 1 if moves[0] < 0 else 0
                if signbit == 0:
                    for i in range(0, moves[0]):
                        temp_moves.append("1")
                else:
                    for i in range(moves[0], 0):
                        temp_moves.append("-1")
                return temp_moves
            return bestMove()


#-----------------------------------------Co_OP Tetris----------------------------------------------------#
    class Co_OP_tetris(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.movesAI = []
            self.PIXEL_SIZE = 20
            self.piece_list_player = [0,1,2,3,4,5,6]
            self.piece_list_Yuri = [0,1,2,3,4,5,6]
            random.shuffle(self.piece_list_player)
            random.shuffle(self.piece_list_Yuri)
            self.tetris_shapes = [
                [[1, 1, 1],
                [0, 1, 0]],

                [[0, 2, 2],
                [2, 2, 0]],

                [[3, 3, 0],
                [0, 3, 3]],

                [[4, 0, 0],
                [4, 4, 4]],

                [[0, 0, 5],
                [5, 5, 5]],

                [[6, 6, 6, 6]],

                [[7, 7],
                [7, 7]]
            ]

            self.stage = [[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
                        [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]]

            if persistent.skin == 1:

                self.color_1 = Image("images/tetris/tetris/cube_1.png")
                self.color_2 = Image("images/tetris/tetris/cube_2.png")
                self.color_3 = Image("images/tetris/tetris/cube_3.png")
                self.color_4 = Image("images/tetris/tetris/cube_4.png")
                self.color_5 = Image("images/tetris/tetris/cube_5.png")
                self.color_6 = Image("images/tetris/tetris/cube_6.png")
                self.color_7 = Image("images/tetris/tetris/cube_7.png")
                self.color_9 = Image("images/tetris/tetris/cube_8.png")

                self.shadow_color_1 = Image("images/tetris/tetris/cube_1.png")
                self.shadow_color_2 = Image("images/tetris/tetris/cube_2.png")
                self.shadow_color_3 = Image("images/tetris/tetris/cube_3.png")
                self.shadow_color_4 = Image("images/tetris/tetris/cube_4.png")
                self.shadow_color_5 = Image("images/tetris/tetris/cube_5.png")
                self.shadow_color_6 = Image("images/tetris/tetris/cube_6.png")
                self.shadow_color_7 = Image("images/tetris/tetris/cube_7.png")

                self.score = 0

                self.playsounds = True
                self.soundbdrop = "sfx/t-drop.ogg"
                self.soundline = "sfx/t-fl.ogg"
                self.soundldrop = "sfx/t-fl-drop.ogg"
                self.soundmove = "sfx/t-move.ogg"
                self.soundrotate = "sfx/t-rotate.ogg"
                self.sound4line = "sfx/t-4fl.ogg"


            elif persistent.skin == 2:

                self.color_1 = Image("images/tetris/tetris_99/cube_1.png")
                self.color_2 = Image("images/tetris/tetris_99/cube_2.png")
                self.color_3 = Image("images/tetris/tetris_99/cube_3.png")
                self.color_4 = Image("images/tetris/tetris_99/cube_4.png")
                self.color_5 = Image("images/tetris/tetris_99/cube_5.png")
                self.color_6 = Image("images/tetris/tetris_99/cube_6.png")
                self.color_7 = Image("images/tetris/tetris_99/cube_7.png")
                self.color_9 = Image("images/tetris/tetris_99/cube_8.png")

                self.shadow_color_1 = Image("images/tetris/tetris_99/cube_1.png")
                self.shadow_color_2 = Image("images/tetris/tetris_99/cube_2.png")
                self.shadow_color_3 = Image("images/tetris/tetris_99/cube_3.png")
                self.shadow_color_4 = Image("images/tetris/tetris_99/cube_4.png")
                self.shadow_color_5 = Image("images/tetris/tetris_99/cube_5.png")
                self.shadow_color_6 = Image("images/tetris/tetris_99/cube_6.png")
                self.shadow_color_7 = Image("images/tetris/tetris_99/cube_7.png")

                self.score = 0

                self.playsounds = True
                self.soundbdrop = "sfx/t-drop(99).ogg"
                self.soundline = "sfx/t-fl(99).ogg"
                self.soundldrop = "sfx/t-fl-drop(99).ogg"
                self.soundmove = "sfx/t-move(99).ogg"
                self.soundrotate = "sfx/t-rotate(99).ogg"
                self.sound2line = "sfx/t-2fl(99).ogg"
                self.sound3line = "sfx/t-3fl(99).ogg"
                self.sound4line = "sfx/t-4fl(99).ogg"


            elif persistent.skin == 3:

                self.color_1 = Image("images/tetris/tetris_gb/cube_1.png")
                self.color_2 = Image("images/tetris/tetris_gb/cube_2.png")
                self.color_3 = Image("images/tetris/tetris_gb/cube_3.png")
                self.color_4 = Image("images/tetris/tetris_gb/cube_4.png")
                self.color_5 = Image("images/tetris/tetris_gb/cube_5.png")
                self.color_6 = Image("images/tetris/tetris_gb/cube_6.png")
                self.color_7 = Image("images/tetris/tetris_gb/cube_7.png")
                self.color_9 = Image("images/tetris/tetris_gb/cube_8.png")

                self.shadow_color_1 = Image("images/tetris/tetris_gb/cube_1.png")
                self.shadow_color_2 = Image("images/tetris/tetris_gb/cube_2.png")
                self.shadow_color_3 = Image("images/tetris/tetris_gb/cube_3.png")
                self.shadow_color_4 = Image("images/tetris/tetris_gb/cube_4.png")
                self.shadow_color_5 = Image("images/tetris/tetris_gb/cube_5.png")
                self.shadow_color_6 = Image("images/tetris/tetris_gb/cube_6.png")
                self.shadow_color_7 = Image("images/tetris/tetris_gb/cube_7.png")

                self.score = 0

                self.playsounds = True
                self.soundbdrop = "sfx/t-drop.ogg"
                self.soundline = "sfx/t-fl.ogg"
                self.soundldrop = "sfx/t-fl-drop.ogg"
                self.soundmove = "sfx/t-move.ogg"
                self.soundrotate = "sfx/t-rotate.ogg"
                self.sound4line = "sfx/t-4fl.ogg"


            elif persistent.skin == 4:


                self.color_1 = Image("images/tetris/tetris_gmd/cube_1.png")
                self.color_2 = Image("images/tetris/tetris_gmd/cube_2.png")
                self.color_3 = Image("images/tetris/tetris_gmd/cube_3.png")
                self.color_4 = Image("images/tetris/tetris_gmd/cube_4.png")
                self.color_5 = Image("images/tetris/tetris_gmd/cube_5.png")
                self.color_6 = Image("images/tetris/tetris_gmd/cube_6.png")
                self.color_7 = Image("images/tetris/tetris_gmd/cube_7.png")
                self.color_9 = Image("images/tetris/tetris_gmd/cube_8.png")

                self.shadow_color_1 = Image("images/tetris/tetris_gmd/cube_1.png")
                self.shadow_color_2 = Image("images/tetris/tetris_gmd/cube_2.png")
                self.shadow_color_3 = Image("images/tetris/tetris_gmd/cube_3.png")
                self.shadow_color_4 = Image("images/tetris/tetris_gmd/cube_4.png")
                self.shadow_color_5 = Image("images/tetris/tetris_gmd/cube_5.png")
                self.shadow_color_6 = Image("images/tetris/tetris_gmd/cube_6.png")
                self.shadow_color_7 = Image("images/tetris/tetris_gmd/cube_7.png")

                self.score = 0

                self.playsounds = True
                self.soundbdrop = "sfx/t-drop(g).ogg"
                self.soundline = "sfx/t-fl(g).ogg"
                self.soundldrop = "sfx/t-fl-drop(g).ogg"
                self.soundmove = "sfx/t-move(g).ogg"
                self.soundrotate = "sfx/t-rotate(g).ogg"
                self.sound4line = "sfx/t-4fl(g).ogg"

            elif persistent.skin == 5:


                self.color_1 = Image("images/tetris/tetris_mb/cube_1.png")
                self.color_2 = Image("images/tetris/tetris_mb/cube_2.png")
                self.color_3 = Image("images/tetris/tetris_mb/cube_3.png")
                self.color_4 = Image("images/tetris/tetris_mb/cube_4.png")
                self.color_5 = Image("images/tetris/tetris_mb/cube_5.png")
                self.color_6 = Image("images/tetris/tetris_mb/cube_6.png")
                self.color_7 = Image("images/tetris/tetris_mb/cube_7.png")
                self.color_9 = Image("images/tetris/tetris_mb/cube_8.png")

                self.shadow_color_1 = Image("images/tetris/tetris_mb/shadow_1.png")
                self.shadow_color_2 = Image("images/tetris/tetris_mb/shadow_2.png")
                self.shadow_color_3 = Image("images/tetris/tetris_mb/shadow_3.png")
                self.shadow_color_4 = Image("images/tetris/tetris_mb/shadow_4.png")
                self.shadow_color_5 = Image("images/tetris/tetris_mb/shadow_5.png")
                self.shadow_color_6 = Image("images/tetris/tetris_mb/shadow_6.png")
                self.shadow_color_7 = Image("images/tetris/tetris_mb/shadow_7.png")

                self.score = 0

                self.playsounds = True
                self.soundbdrop = "sfx/t-drop(mb).ogg"
                self.soundline = "sfx/t-fl(mb).ogg"
                self.soundldrop = "sfx/t-fl-drop(mb).ogg"
                self.soundmove = "sfx/t-move(mb).ogg"
                self.soundrotate = "sfx/t-rotate(mb).ogg"
                self.sound2line = "sfx/t-2fl(mb).ogg"
                self.sound3line = "sfx/t-3fl(mb).ogg"
                self.sound4line = "sfx/t-4fl(mb).ogg"

            elif persistent.skin == 6:


                self.color_1 = Image("/custom_tetris/cube_1.png")
                self.color_2 = Image("/custom_tetris/cube_2.png")
                self.color_3 = Image("/custom_tetris/cube_3.png")
                self.color_4 = Image("/custom_tetris/cube_4.png")
                self.color_5 = Image("/custom_tetris/cube_5.png")
                self.color_6 = Image("/custom_tetris/cube_6.png")
                self.color_7 = Image("/custom_tetris/cube_7.png")
                self.color_9 = Image("/custom_tetris/cube_8.png")

                self.shadow_color_1 = Image("/custom_tetris/shadow_1.png")
                self.shadow_color_2 = Image("/custom_tetris/shadow_2.png")
                self.shadow_color_3 = Image("/custom_tetris/shadow_3.png")
                self.shadow_color_4 = Image("/custom_tetris/shadow_4.png")
                self.shadow_color_5 = Image("/custom_tetris/shadow_5.png")
                self.shadow_color_6 = Image("/custom_tetris/shadow_6.png")
                self.shadow_color_7 = Image("/custom_tetris/shadow_7.png")

                self.score = 0

                self.playsounds = True
                self.soundbdrop = "/custom_tetris/t-drop.ogg"
                self.soundline = "/custom_tetris/t-fl.ogg"
                self.soundldrop = "/custom_tetris/t-fl-drop.ogg"
                self.soundmove = "/custom_tetris/t-move.ogg"
                self.soundrotate = "/custom_tetris/t-rotate.ogg"
                self.sound2line = "/custom_tetris/t-2fl.ogg"
                self.sound3line = "/custom_tetris/t-3fl.ogg"
                self.sound4line = "/custom_tetris/t-4fl.ogg"


            class current_shape_player:
                shape = ""
                shape_number = ""
                new_shape_number = self.piece_list_player[0]
                next_shape = self.tetris_shapes[new_shape_number]
                x = 5
                y = 1
                move_time = 0.300
                speed = 0.20

            class current_shape_Yuri:
                shape = ""
                shape_number = ""
                new_shape_number = self.piece_list_Yuri[0]
                next_shape = self.tetris_shapes[new_shape_number]
                x = 5
                y = 1
                move_time = 0.300
                speed = 0.20

            self.temp_position = 3
            self.current_shape_player = current_shape_player()
            self.current_shape_Yuri = current_shape_Yuri ()
            self.level = 1
            self.allLines = 0
            self.oldst = None
            self.new_shape_player = True
            self.new_shape_Yuri = True
            self.game_over = False
            self.winner = None

        #Function which add shape to stage.
        #Arguments current x and y position of shape in stage
        def addShapeToStage(self, current_shape, current_x, current_y):
            for idr, row in enumerate(current_shape.shape):
                for idc, column in enumerate(row):
                    if column != 0:
                        self.stage[current_y+idr][current_x+idc]=column

        def render(self, width, height, st, at):
            #Win/lose conditions               ):
            global TetrisWinner

            for idc in range(4, 16):
                if self.stage[1][idc] != 0:
                    self.game_over = True

            if self.game_over:
                if self.score > persistent.best_co_op_tetris_score:
                    persistent.best_co_op_tetris_score = self.score
                    TetrisWinner = 2
                else:
                    TetrisWinner = 3
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            renpy.jump("tetris_over")

            ####################################################################################
            #Function which check if there are lines. If yes, add it to score and return new stage
            def lines():
                numberOfFullLines = 0
                #Check if there are any lines and fix stage
                prevLine = False
                for idr in range(1, 21):
                    fullLine = True
                    for idc in range(1, 21):
                        if self.stage[idr][idc] == 0:
                            fullLine = False
                            break
                    if fullLine:
                        numberOfFullLines += 1
                        renpy.sound.play(self.soundline)
                        for idc in range(1, 21):
                            self.stage[idr][idc] = 0
                        if prevLine != fullLine:
                            for i in range(0, idr-1):
                                for idc in range(1, 21):
                                    self.stage[idr-i][idc] = self.stage[idr-i-1][idc]
                                    self.stage[idr-i-1][idc] = 0
                                    fullLine = False
                    prevLine = fullLine

                #Score points depending on how many lines there were cleared
                self.allLines += numberOfFullLines
                if numberOfFullLines == 1:
                    self.score += 100 * self.level
                elif numberOfFullLines == 2:
                    self.score += 300 * self.level
                elif numberOfFullLines == 3:
                    self.score += 500 * self.level
                elif numberOfFullLines == 4:
                    self.score += 800 * self.level
                    renpy.sound.play(self.sound4line)
                self.level =  int(self.allLines/10)+1
            #################################################################################
            r = renpy.Render(width, height)

            if persistent.skin == 1:
                background = renpy.render(Image("images/tetris/tetris/background_co_op.png"), width, height, st, at)

            elif persistent.skin == 2:
                background = renpy.render(Image("images/tetris/tetris_99/background_co_op.png"), width, height, st, at)

            elif persistent.skin == 3:
                background = renpy.render(Image("images/tetris/tetris_gb/background_co_op.png"), width, height, st, at)

            elif persistent.skin == 4:
                background = renpy.render(Image("images/tetris/tetris_gmd/background_co_op.png"), width, height, st, at)

            elif persistent.skin == 5:
                background = renpy.render(Image("images/tetris/tetris_mb/background_co_op.png"), width, height, st, at)

            elif persistent.skin == 6:
                background = renpy.render(Image("/custom_tetris/background_co_op.png"), width, height, st, at)

            r.blit(background, (0, 0))
            lines()

            #Player
            if self.new_shape_player:
                self.current_shape_player.x = 5
                self.current_shape_player.y = 1
                self.current_shape_player.shape = self.current_shape_player.next_shape
                self.current_shape_player.shape_number = self.current_shape_player.new_shape_number
                self.piece_list_player.pop(0)
                if not self.piece_list_player:
                    self.piece_list_player = [0,1,2,3,4,5,6]
                    random.shuffle(self.piece_list_player)
                self.current_shape_player.new_shape_number = self.piece_list_player[0]
                self.current_shape_player.next_shape = self.tetris_shapes[self.current_shape_player.new_shape_number]
                self.new_shape_player = False

            #Yuri
            if self.new_shape_Yuri:
                self.current_shape_Yuri.x = 15
                self.current_shape_Yuri.y = 1
                self.current_shape_Yuri.shape = self.current_shape_Yuri.next_shape
                self.current_shape_Yuri.shape_number = self.current_shape_Yuri.new_shape_number
                self.piece_list_Yuri.pop(0)
                if not self.piece_list_Yuri:
                    self.piece_list_Yuri = [0,1,2,3,4,5,6]
                    random.shuffle(self.piece_list_Yuri)
                self.current_shape_Yuri.new_shape_number = self.piece_list_Yuri[0]
                self.current_shape_Yuri.next_shape = self.tetris_shapes[self.current_shape_Yuri.new_shape_number]
                self.new_shape_Yuri = False
                self.temp_position = 1
                temp_AI = True
                for idc in range(1, 21):
                    if self.stage[2][idc] != 0:
                        temp_AI = False
                if temp_AI:
                    self.movesAI = self.Yuri_AI()

            if self.oldst is None:
                self.oldst = st

            if self.current_shape_Yuri.y >= 4:
                self.current_shape_Yuri.speed = 0.4 - 0.03 * (self.level - 1)

            if self.temp_position == self.current_shape_Yuri.y:
                for i in range(0, 3):
                    if len(self.movesAI) != 0:
                        if self.movesAI[0] == "r":
                            self.rotateClockWiseAI()
                        else:
                            self.current_shape_Yuri.x += int(self.movesAI[0])
                        del self.movesAI[0]
                self.temp_position += 1

            dtime = st - self.oldst
            self.oldst = st
            temp_can_go_down = True

            #Player
            if self.current_shape_player.move_time <= 0:
                # Check if bottom is empty
                for idr, row in enumerate(self.current_shape_player.shape):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if self.stage[self.current_shape_player.y + 1 + idr][self.current_shape_player.x + idc] != 0:
                                temp_can_go_down = False
                                renpy.sound.play(self.soundbdrop)
                                break
                if temp_can_go_down != False:
                    self.current_shape_player.move_time = self.current_shape_player.speed
                    self.current_shape_player.y += 1
                else:
                    self.new_shape_player = True
                    self.addShapeToStage(self.current_shape_player, self.current_shape_player.x, self.current_shape_player.y)
            else:
                self.current_shape_player.move_time -= dtime

            #Yuri
            if self.current_shape_Yuri.move_time <= 0:
                # Check if bottom is empty
                for idr, row in enumerate(self.current_shape_Yuri.shape):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if self.stage[self.current_shape_Yuri.y + 1 + idr][self.current_shape_Yuri.x + idc] != 0:
                                temp_can_go_down = False
                                renpy.sound.play(self.soundbdrop)
                                break
                if temp_can_go_down != False:
                    self.current_shape_Yuri.move_time = self.current_shape_Yuri.speed
                    self.current_shape_Yuri.y += 1
                else:
                    self.new_shape_Yuri = True
                    self.addShapeToStage(self.current_shape_Yuri, self.current_shape_Yuri.x, self.current_shape_Yuri.y)
            else:
                self.current_shape_Yuri.move_time -= dtime

            def draw_shape(sx, sy, current_shape,shadow):
                for idr, row in enumerate(current_shape):
                    for idc, column in enumerate(row):
                        if column == 1:
                            shape = renpy.render(self.color_1, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_1, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape_player.y)))
                        elif column == 2:
                            shape = renpy.render(self.color_2, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_2, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape_player.y)))
                        elif column == 3:
                            shape = renpy.render(self.color_3, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_3, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape_player.y)))
                        elif column == 4:
                            shape = renpy.render(self.color_4, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_4, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape_player.y)))
                        elif column == 5:
                            shape = renpy.render(self.color_5, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_5, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape_player.y)))
                        elif column == 6:
                            shape = renpy.render(self.color_6, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_6, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape_player.y)))
                        elif column == 7:
                            shape = renpy.render(self.color_7, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_7, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape_player.y)))
                        elif column == 7:
                            shape = renpy.render(self.color_7, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))
                            if shadow == 1:
                                temp_shape = renpy.render(self.shadow_color_7, width, height, st, at)
                                temp_shape.alpha = 0.3
                                r.blit(temp_shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, (int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr) + self.PIXEL_SIZE * (self.find_bottom()-self.current_shape_player.y)))
                        elif column == 9:
                            shape = renpy.render(self.color_9, width, height, st, at)
                            r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idc, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * idr))

            a = "Score - %(s)d " % {"s":self.score }
            b = "Lines - %(s)d " % {"s":self.allLines }
            c = "Level - %(s)d " % {"s":self.level}
            d = "Next player:"
            i = "Best Score - %(s)d " % {"s":persistent.best_co_op_tetris_score }
            k = "Next Yuri:"

            e = Text(a)
            f = Text(b)
            g = Text(c)
            h = Text(d)
            j = Text(i)
            l = Text(k)

            text_allLines_render = renpy.render(f, width, height, st, at)
            text_level_render = renpy.render(g, width, height, st, at)
            text_next_player_render = renpy.render(h, width, height, st, at)
            text_next_Yuri_render = renpy.render(l, width, height, st, at)

            text_score_render = renpy.render(e, width, height, st, at)
            r.blit(text_score_render, (5, -50))

            text_score_render = renpy.render(j, width, height, st, at)
            r.blit(text_score_render, (5, -100))
            r.blit(text_allLines_render, (250, -100))
            r.blit(text_level_render, (250, -50))

            r.blit(text_next_player_render, (5, 450))
            draw_shape(25, 500, self.current_shape_player.next_shape,0)

            r.blit(text_next_Yuri_render, (250, 450))
            draw_shape(275, 500, self.current_shape_Yuri.next_shape,0)

            draw_shape(0, 0, self.stage,0)
            draw_shape(self.current_shape_player.x*self.PIXEL_SIZE, self.current_shape_player.y*self.PIXEL_SIZE, self.current_shape_player.shape,1)
            draw_shape(self.current_shape_Yuri.x*self.PIXEL_SIZE, self.current_shape_Yuri.y*self.PIXEL_SIZE, self.current_shape_Yuri.shape,0)

            renpy.redraw(self, 0)
            return r
        ############################################################################################################################
        # Rotate piecec functions
        def rotateClockWise(self, mat):
            tempShape = mat
            tempRow = tempShape
            tempX = self.current_shape_player.x
            tempY = self.current_shape_player.y
            ifRotation = True
            renpy.sound.play(self.soundrotate)
            lenRow = len(mat)
            lenCol = len(mat[0])
            #Rotation of Long I piece:
            # I to -
            if lenRow == 4:
                tempRow = [[] for _ in range(lenCol)]
                for idr, row in enumerate(mat):
                    lenColumn = len(row)
                    for idc, column in enumerate(row):
                        tempRow[idc].insert(0,column)
                self.current_shape_player.y+=1
                if self.stage[self.current_shape_player.y][self.current_shape_player.x-1] == 0:
                    self.current_shape_player.x-=1
                for idc, row in enumerate(tempRow[0]):
                    if self.stage[self.current_shape_player.y][self.current_shape_player.x+idc] != 0:
                        ifRotation = False
                        break
            # - to I
            elif lenRow == 1:
                tempRow = [[] for _ in range(lenCol)]
                for idr, row in enumerate(mat):
                    lenColumn = len(row)
                    for idc, column in enumerate(row):
                        tempRow[idc].insert(0,column)
                self.current_shape_player.y-=1
                self.current_shape_player.x+=1
                for idr, row in enumerate(tempRow):
                    if self.stage[self.current_shape_player.y+idr][self.current_shape_player.x] != 0:
                        ifRotation = False
                        break
            #Rotation of Z,L ,T piece
            # xxx    xx
            # xxx to xx
            #        xx
            elif lenRow == 2 and lenCol != 2:
                tempRow = [[] for _ in range(lenCol)]
                for idr, row in enumerate(mat):
                    lenColumn = len(row)
                    for idc, column in enumerate(row):
                        tempRow[idc].insert(0,column)
                for idr, row in enumerate(tempRow):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if self.stage[self.current_shape_player.y+idr][self.current_shape_player.x+idc] != 0:
                                ifRotation = False
                                break
            # xx    xxx
            # xx to xxx
            # xx
            elif lenRow == 3:
                tempRow = [[] for _ in range(lenCol)]
                for idr, row in enumerate(mat):
                    lenColumn = len(row)
                    for idc, column in enumerate(row):
                        tempRow[idc].insert(0,column)
                if self.stage[self.current_shape_player.y][self.current_shape_player.x+len(tempRow[0])-1] != 0:
                    self.current_shape_player.x-=1
                for idr, row in enumerate(tempRow):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if self.stage[self.current_shape_player.y+idr][self.current_shape_player.x+idc] != 0:
                                ifRotation = False
                                break
            elif lenRow == 2 and lenCol == 2:
                ifRotation = True
            #Fail the rotation, back to orginal position
            if ifRotation == False:
                tempRow = tempShape
                self.current_shape_player.x = tempX
                self.current_shape_player.y = tempY
            return tempRow
            ####################################################################################################################
        def find_bottom(self):
            temp_y = 0
            for idr in range(self.current_shape_player.y, 22):
                for idc, column in enumerate(self.current_shape_player.shape[0]):
                    if self.stage[idr][self.current_shape_player.x + idc ] != 0:
                        temp_y = idr-len(self.current_shape_player.shape)
                        break
                if temp_y != 0:
                    break
            for position in range(0, 4):
                temp_fit = True
                for idr, row in enumerate(self.current_shape_player.shape):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if self.stage[temp_y+idr][self.current_shape_player.x + idc] != 0:
                                temp_fit = False
                                break
                if temp_fit:
                    temp_y += 1
                else:
                    temp_y -= 1
                    break
            return temp_y

        def event(self, ev, x, y, st):
            import pygame
            temp_can_left = True
            temp_can_right = True
            if self.level > 19:
                self.current_shape.speed = 0.20
            else:
                self.current_shape_player.speed = 0.20
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_UP:
                    self.current_shape_player.shape = self.rotateClockWise(self.current_shape_player.shape)
                elif ev.key == pygame.K_LEFT:
                    renpy.sound.play(self.soundmove)
                    for idr, row in enumerate(self.current_shape_player.shape):
                        for idc, column in enumerate(row):
                            if column != 0:
                                if self.stage[self.current_shape_player.y + idr][self.current_shape_player.x - 1 + idc] != 0:
                                    temp_can_left = False
                                    break
                    if temp_can_left:
                        self.current_shape_player.x -= 1
                elif ev.key == pygame.K_RIGHT:
                    renpy.sound.play(self.soundmove)
                    for idr, row in enumerate(self.current_shape_player.shape):
                        for idc, column in enumerate(row):
                            if column != 0:
                                if self.stage[self.current_shape_player.y + idr][self.current_shape_player.x + 1 + idc ] != 0:
                                    temp_can_right = False
                                    break
                    if temp_can_right:
                        self.current_shape_player.x += 1
                elif ev.key == pygame.K_DOWN:
                    self.current_shape_player.speed = 0.002
                elif ev.key == pygame.K_SPACE:
                    renpy.sound.play(self.soundbdrop)
                    self.addShapeToStage(self.current_shape_player, self.current_shape_player.x, self.find_bottom())
                    self.new_shape_player = True

        def rotateClockWiseAI(self):
            lenRow = len(self.current_shape_Yuri.shape)
            lenCol = len(self.current_shape_Yuri.shape[0])
            tempRow = [[] for _ in range(lenCol)]
            for idr, row in enumerate(self.current_shape_Yuri.shape):
                for idc, column in enumerate(row):
                    tempRow[idc].insert(0,column)
            del self.current_shape_Yuri.shape
            self.current_shape_Yuri.shape = tempRow

#----------------------------------------------------------------------------------------------------

        def Yuri_AI(self):
            def calculateScoreForMove():
                height = 0
                lines = 0
                holes = 0
                temp_col_height = [None] * 20
                bumpiness = 0
                #Caluclate height and lines
                for idr in range(20, 0, -1):
                    temp_clear_line = True
                    for idc in range(1, 21):
                        if self.stage[idr][idc] == 0:
                            temp_clear_line = False
                            break
                    if temp_clear_line:
                        lines += 1
                #Caluclate holes and bumpiness
                for idc in range(1, 21):
                    temp_col_height[idc-1] = 0
                    temp_holes = 0
                    for idr in range(20, 0, -1):
                        if self.stage[idr][idc] != 0:
                            holes += temp_holes
                            temp_holes = 0
                        else:
                            temp_holes += 1
                        if self.stage[idr][idc] != 0:
                            temp_col_height[idc-1] = 21-idr
                for i in range(0, 19):
                    height += temp_col_height[i]
                    bumpiness += abs(temp_col_height[i] - temp_col_height[i+1])
                height += temp_col_height[19]
                score = (-0.510066 * height) + (0.760666 * lines) - (0.35663 * holes) - (0.184483 * bumpiness)
                return score

            def shapeRotation(shape):
                if shape == 6:
                    return 2
                elif shape == 0 or shape == 3 or shape == 4:
                    return 5
                elif shape == 1 or shape == 2 or shape == 5:
                    return 3

            ####################################################################################################################
            def bestMove():
                import copy
                moves = [0,1]
                best_score = -100
                temp_shape = copy.deepcopy(self.current_shape_Yuri.shape)
                temp_rotation = shapeRotation(self.current_shape_Yuri.shape_number)

                #Find best position
                temp_stage = copy.deepcopy(self.stage)
                for rot in range(1, temp_rotation):
                    temp_len = len(self.current_shape_Yuri.shape[0])-1
                    for idc in range(1, 21-temp_len):
                        del self.stage
                        self.stage = copy.deepcopy(temp_stage)
                        temp_break = False
                        for idr in range(1, 22):
                            for idcShape in range(0, len(self.current_shape_Yuri.shape[0])):
                                if self.current_shape_Yuri.shape[len(self.current_shape_Yuri.shape)-1][idcShape] != 0:
                                    if self.stage[idr][idc+idcShape] != 0:
                                        temp_idr = idr
                                        temp_break = True
                                        break
                            if temp_break:
                                break
                        for idr in range(0, 21):
                            temp_free = True
                            temp_idr -= 1
                            for idrShape, row in enumerate(self.current_shape_Yuri.shape):
                                for idcShape, column in enumerate(row):
                                    if column != 0:
                                        if self.stage[temp_idr+(idrShape-(len(self.current_shape_Yuri.shape)-1))][idc+idcShape] != 0:
                                            temp_free = False
                            if temp_free:
                                self.addShapeToStage(self.current_shape_Yuri, idc, temp_idr-(len(self.current_shape_Yuri.shape)-1))
                                temp_score = calculateScoreForMove()
                                if temp_score > best_score:
                                    best_score = temp_score
                                    moves = [idc-15, rot]
                                break
                    self.rotateClockWiseAI()
                self.stage = copy.deepcopy(temp_stage)
                del temp_stage
                self.current_shape_Yuri.shape = copy.deepcopy(temp_shape)
                del temp_shape

                temp_moves = []
                for i in range(0, moves[1]-1):
                    temp_moves.append("r")
                signbit = 1 if moves[0] < 0 else 0
                if signbit == 0:
                    for i in range(0, moves[0]):
                        temp_moves.append("1")
                else:
                    for i in range(moves[0], 0):
                        temp_moves.append("-1")
                return temp_moves
            
            #Check if the current tetromino of Yuri_AI has reached the bottom of the grid or a previously placed tetromino.
            temp_can_go_down = True
            for idr, row in enumerate(self.current_shape_Yuri.shape):
                for idc, column in enumerate(row):
                    if column != 0:
                        if self.stage[self.current_shape_Yuri.y + 1 + idr][self.current_shape_Yuri.x + idc] != 0:
                            temp_can_go_down = False
                            break
            
            # If the tetromino has reached the bottom, freeze it in place.
            if temp_can_go_down == False:
                self.addShapeToStage(self.current_shape_Yuri, self.current_shape_Yuri.x, self.current_shape_Yuri.y)
                self.new_shape_Yuri = True
            else:
                # Otherwise, let it continue falling.
                return bestMove()

