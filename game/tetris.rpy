
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
    if sanity() > 2 and karma() > 2:
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
    elif sanity() > 2 and karma() < 3:
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
    elif sanity() < 3 and karma() > 2:
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
    elif sanity() < 3 and karma() < 3:
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
                $ persistent.skin = 1

            "Tetris 99 Theme.":
                $ persistent.skin = 2

            "GameBoy Tetris Theme.":
                $ persistent.skin = 3

            "SEGA Gen/MD Tetris Theme.":
                $ persistent.skin = 4

            "M1ND BEND3R Theme.":
                $ persistent.skin = 5

            "Custom Theme.":
                call custom_tetris_checkpoint_start

    else:
        menu:

            "Default Theme.":
                $ persistent.skin = 1

            "Tetris 99 Theme.":
                $ persistent.skin = 2

            "GameBoy Tetris Theme.":
                $ persistent.skin = 3

            "SEGA Gen/MD Tetris Theme.":
                $ persistent.skin = 4

            "Custom Theme.":
                call custom_tetris_checkpoint_start

    y "Alright [player], now I can let you select the modes you want to play."
    menu:
        "Line Count":
            if persistent.lovecheck and karma() > 3:
                #If lovecheck is true along with K: 4-5
                $ show_chr("A-BBBAA-ADAA")
                y "It's a nice way to pass the time, really."
                y "Just a couple doing things together..."
                y "Ahem... Anyway let's get started."
                $ show_chr("A-FCAAA-ACAB")
                menu:
                    "40":
                        $ LineLimit = 40
                    "80":
                        $ LineLimit = 80
                    "100":
                        $ LineLimit = 100
                    "200":
                        $ LineLimit = 200
                    "300":
                        $ LineLimit = 300
                    "400":
                        $ LineLimit = 400
                    "500":
                        $ LineLimit = 500
                jump tetris_difficulty
            elif karma() >= 3:
                #If K = 3-5 regardless of S value
                $ show_chr("A-ACEAA-AMAM")
                y "Oh, lovely choice, [player]~"
                y "W-well, hopefully I will prove a worthy challenge..."
                y "Uhuhuhu..."
                y "Well whoever gets to the specific amount of lines wins..."
                menu:
                    "40":
                        $ LineLimit = 40
                    "80":
                        $ LineLimit = 80
                    "100":
                        $ LineLimit = 100
                    "200":
                        $ LineLimit = 200
                    "300":
                        $ LineLimit = 300
                    "400":
                        $ LineLimit = 400
                    "500":
                        $ LineLimit = 500
                jump tetris_difficulty
            elif karma() < 3:
                #[If K = 1-2
                $ show_chr("A-BEBAA-AMAM")
                y "I-I'm not sure if you'd want to waste your time with me..."
                y "I mean, this mode seems a bit too simple and boring to you."
                y "Especially with someone such as myself."
                $ show_chr("A-CEAAA-ALAL")
                y "Maybe you just want to get an ego boost from seeing me lose?"

                menu:
                    "40":
                        $ LineLimit = 40
                    "80":
                        $ LineLimit = 80
                    "100":
                        $ LineLimit = 100
                    "200":
                        $ LineLimit = 200
                    "300":
                        $ LineLimit = 300
                    "400":
                        $ LineLimit = 400
                    "500":
                        $ LineLimit = 500
                jump tetris_difficulty

        "Score":
            if persistent.lovecheck and karma() > 3 and sanity() < 2:
                #[If K = 3-5 and lovecheck == true, S = 1-2]
                $ show_chr("A-KLAAA-AKAK")
                y "And maybe you will win me as a prize to be cherished... Forever~"
                y "Or maybe I would win you. Hehe. Either way, everyone wins!"
                menu:
                    "40,000":
                        $ TetrisScore = 40000
                    "75,000":
                        $ TetrisScore = 75000
                    "100,000":
                        $ TetrisScore = 100000
                    "250,000":
                        $ TetrisScore = 250000
                    "500,000":
                        $ TetrisScore = 500000
                    "750,000":
                        $ TetrisScore = 750000
                    "1,000,000":
                        $ TetrisScore = 1000000
                jump tetris_difficulty
            elif karma() >= 3:
                #[K = 3-5 and regardless of S value]
                $ show_chr("A-FCEAA-ABAB")
                y "Oh, some competition, hm?"
                y "Well I suppose being a little competitive wouldn't be too bad, now would it?"
                $ show_chr("A-ABAAA-AMAM")
                python:
                    if sanity() >= 3:
                        placeholder = "contest"
                    elif sanity() <= 3:
                        placeholder = "thrill"
                y "There's nothing wrong with a nice [placeholder] every once in a while..."
                #If sanity 1-2 "thrill"
                #If sanity 3-5 "contest"
                $ show_chr("A-AAEAA-ALAL")
                y "Alright, let us see who will outdo the other!"
                menu:
                    "40,000":
                        $ TetrisScore = 40000
                    "75,000":
                        $ TetrisScore = 75000
                    "100,000":
                        $ TetrisScore = 100000
                    "250,000":
                        $ TetrisScore = 250000
                    "500,000":
                        $ TetrisScore = 500000
                    "750,000":
                        $ TetrisScore = 750000
                    "1,000,000":
                        $ TetrisScore = 1000000
                jump tetris_difficulty
            elif karma() < 3:
                #[K= 1-2 regardless of S value]
                $ show_chr("A-AEBAA-ALAL")
                y "W-well... [player], I don't know whether this is simply a jest or you just trying to impress me..."
                y "All just to prove something to me. Just to rub it in my face.."
                y "Then again, at least it's a way to pass the time."
                $ show_chr("A-BECAA-AMAM")
                y "Well, whatever."
                y "Let's get on with it."
                menu:
                    "40,000":
                        $ TetrisScore = 40000
                    "75,000":
                        $ TetrisScore = 75000
                    "100,000":
                        $ TetrisScore = 100000
                    "250,000":
                        $ TetrisScore = 250000
                    "500,000":
                        $ TetrisScore = 500000
                    "750,000":
                        $ TetrisScore = 750000
                    "1,000,000":
                        $ TetrisScore = 1000000
                jump tetris_difficulty

        "CO-OP":
            if karma() == 5:
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
            elif karma() == 1:
                #[If K = 1]
                $ show_chr("A-CEBAB-AAAL") # insert closed frown with worried eyebrows and slightly teary eyes and hand on her chest
                y "A-are you sure...?"
                y "I mean why would you want to work together with me, let alone play a game together?"
                y "Is this again a big joke to you? I... I don't know anymore."
                #insert open frown with closed eyes and worried eyebrows with hands on hair
                y "Let's try this... I guess."
                #if sanity() > 2 and karma() > 2:
                #elif sanity() > 2 and karma() < 3:
                #elif sanity() < 3 and karma() > 2:
                #elif sanity() < 3 and karma() < 3:
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
    y "For the difficulties such as Beginner, Novice and Intermediate it has to be 220 x 420 pixels image. Use the {b}background.png{/b} file from the folder \"game\\images\\tetris\\tetris\" as an example..."
    $ show_chr("A-ACAAA-ABAD")
    y "For the same modes but this time in the higher difficulties such as Advanced, Expert and Master, it is the exact same procedure, but this time you have to delete the grids and name it {b}backgrund_no_grind{/b}... oh yes, and it still has to be a .png file!"
    y "The Co-op mode shares the same procedure, but this time it is 421 x 420 pixels and you name it {b}grids (coop).png{/b}. It's in the same folder again."
    y "Now we come to the blocks."
    y "Fun fact, did you know that a single block is called a Tetromino?"
    y "There are 7 tetrominoes in Tetris which usually have different colors. You could make them the same colors"
    y "But that would be kind of boring. Don't you think?"
    $ show_chr("A-ACAAA-AFAD")
    y "Each tetromino is build from individual blocks which are number from 1 to 7."
    y "Also in newer version of Tetris. You can see where the tetromino will land. We refer it as {b}shadow tetrominos{/b} "
    y "They also need to have their own colors which are usually transparency of normal blocks"
    y "Each of the tetromino, it needs to be a .png image with size 20x20. You can use the {b}cube_1.png{/b} file from the folder \"game\\images\\tetris\\tetris\" as an example..."
    y "For the T Tetromino you set up cube_1.png and shadow_1.png"
    y "For the S Tetromino you set up cube_2.png and shadow_2.png"
    y "For the Z Tetromino you set up cube_3.png and shadow_3.png"
    y "For the L Tetromino you set up cube_4.png and shadow_4.png"
    y "For the J Tetromino you set up cube_5.png and shadow_5.png"
    y "For the I Tetromino you set up cube_6.png and shadow_6.png"
    y "For the O Tetromino you set up cube_7.png and shadow_7.png"
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
    y "t-move.ogg for whenever you move the tetromino."
    y "t-rotate.ogg for whenever you rotate the tetromino."
    y "t-spin.ogg for whenever you spin the T tetromino."
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
    if karma() >= 2:
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
                        y("It seems there is issue with tetromino cube image:" + i)
                        renpy.call("custom_tetris_failure")
                for i in range(1, 8):
                    element = ("shadow_" + str(i) + ".png", "shadow_" + str(i) + ".png")
                    if not element in custom_tetris:
                        y("It seems there is issue with tetromino shadows image:" + i)
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
        "Beginner":
            $ AI_difficulty = 1

            if karma() >= 3:
                y "Oh, I see."
                y "You'd like me to go easy on you this time, hm?"
                y "I'm happy to oblige, [player]!"

            elif karma() < 3:
                #[If K= 1 or 2 regardless of S value]
                $ show_chr("A-BEAAA-AMAM")
                y "..."
                y "I-is this some kind of joke? Directed at me?"
                y "To indulge in this activity but at such an infantile level... Seemingly to jest at my abilities?"
                $ show_chr("A-CEBAA-AAAD")  # closed frown with closed eyes and hand on her cheek (needs expressions)
                y "Whatever... Let us proceed."
                #elif sanity() > 2 and karma() < 3:
                #elif sanity() < 3 and karma() > 2:
                #elif sanity() < 3 and karma() < 3:


        "Novice":
            $ AI_difficulty = 2

            if karma() >= 3:
            #[If K= 3-5 and S: 3-5]
                $ show_chr("A-ABABA-AAAJ")
                y "Oh I see~ Trying to warm up with a slight challenge eh?"
                y "Well then. I would like to see how you do!"
                y "It is good to get out of your comfort zone a bit more."

            elif karma() < 3:
            #[If K = 1 or 2 regardless of S value]
                $ show_chr("A-ADCAA-AAAL")
                y "Hm... Y-you know I am slightly surprised that you wanted to partake in this game with me. I was thinking you'd pick a harder difficulty just to prove a point."
                y "I mean why even bother with such a simple difficulty with someone as myself?"
                y "If this is meant to be a joke, I quite frankly do not understand it."
                $ show_chr("A-CECAA-ALAL")
                y "Whatever... Anyways let the games begin."


        "Intermediate":
            $ AI_difficulty = 3

            if karma() >= 3:
            #[If K = 3-5 and S = 3-5]
                $ show_chr("A-ACCAA-AMAM")
                y "Oh huhuhehehe... Really turning the dial up are you now, [player]?"
                y "Well I do like it when you get a bit more daring~ It is rather inspiring."
                # soft closed smile with a blush and hands on the table
                y "Well as people say nowadays, I guess, let these games begin!"
                y "O-oh but don't go too hard on yourself [player]... Eheheh."

            elif karma() < 3:
            #[If K = 1-2]
                $ show_chr("A-CECAA-ALAL")
                y "I-I guess you really want to rub it in my face just to prove a point..."
                y "Very well then... Let the games begin, I suppose."
                y "Hmph."


        "Advanced":
            $ AI_difficulty = 4

            if karma() >= 3:
                $ show_chr("A-DCCBA-AAAD")
                y "Mmm..."
                y "Oh dear [player]. That seems like such a Herculean task to tackle. Are you sure?"
                $ show_chr("A-ABAAA-ALAL")
                y "Ehehehehe... Well alright if you insist~"
                y "Prepare thy mind and body for the penultimate gamer's challenge dear [player]!"

            elif karma() > 3 and sanity() < 3:
            #[If K= 3-5 and S= 2 or 1]
                $ show_chr("A-DLCBA-AMAM")
                y "Oh oh... Oh my yes!"
                y "A glutton for punishment aren't you [player]?"
                y "Whatever scars from this task you may carry I will bear with you!"
                y "J-just be a bit careful [player]... If you exert yourself too much and get hurt, I might have to thrash a few things here~ Aahahaha..."
                $ show_chr("A-DCAAA-AFAG")
                y "Show me, show them all what you are made of sweet [player]!!!"

            elif karma() < 3:
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
                if karma() >= 3:
                #if karma() is 3-5
                    $ show_chr("A-ACBAA-ABAL")
                    y "Very well, I'll try my best to offer you a suitable challenge."
                    y "Just keep in mind, it is just a game. It doesn't really matter who wins as long as we are having a good time."

                elif karma() < 3:
                #if karma() is 1-2
                    $ show_chr("A-AFBAA-ABAL")
                    y "Maybe I can teach you a lesson here..."


        "Master":
            $ AI_difficulty = 6
            $ show_chr("A-ACAAA-ABAL")
            y "The highest, I see..."
            y "I'm not even sure if I'm good enough to pull this off but... let's give it a try."


        "Your choice, [persistent.yuri_nickname]":
            # K&S - both karma() and sanity are...
            # K|S - either karma() or sanity() is...

            # Adding random mood.
            $ import random
            $ randomMood = random.randint(-1, 1)

            # K&S are almost maximum.
            if(abs(karma() + sanity() - 10) < 2):
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
            elif(abs(karma() + sanity() - 8) < 2):
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
            elif(abs(karma() + sanity() - 6) < 2):
                if(randomMood == -1):
                    # Medium.
                    $ AI_difficulty = 2

                    if(abs(karma() - sanity()) < 2):
                        # K&S are neutral.
                        $ show_chr("A-BCAAA-AMAM")
                        y "I-If you're comfortable with that, [player]."
                        y "Don't expect me to give you a free pass though."
                        $ show_chr("A-IAAAA-AMAM")
                        y "Medium should suffice."

                    elif(karma() < sanity()):
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

                    if(abs(karma() - sanity()) < 2):
                        # K&S are neutral.
                        $ show_chr("A-BCAAA-AMAM")
                        y "I-If you're comfortable with that, [player]."
                        y "Don't expect me to give you a free pass though."
                        $ show_chr("A-IAAAA-AMAM")
                        y "Hard should suffice."

                    elif(karma() < sanity()):
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

                    if(abs(karma() - sanity()) < 2):
                        # K&S are neutral.
                        $ show_chr("A-BCAAA-AMAM")
                        y "I-If you're comfortable with that, [player]."
                        y "Don't expect me to give you a free pass though."
                        $ show_chr("A-IAAAA-AMAM")
                        y "Disadvantaged should suffice."

                    elif(karma() < sanity()):
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
            elif(abs(karma() + sanity() - 4) < 2):
                if(randomMood == -1):
                    # Hard.
                    $ AI_difficulty = 3

                    if(abs(karma() - sanity()) < 2):
                        # K&S lower than average.
                        $ show_chr("A-CEAAA-AAAC")
                        y "I d-don't really know..."
                        y "Does it really even matter what difficulty we play on?"
                        y "I guess I'll just go for hard, You'll probably just boast about it afterwards regardless."

                    elif(karma() < sanity()):
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

                    if(abs(karma() - sanity()) < 2):
                        # K&S lower than average.
                        $ show_chr("A-CEAAA-AAAC")
                        y "I d-don't really know..."
                        y "Does it really even matter what difficulty we play on?"
                        y "I guess I'll just go for disadvantaged, You'll probably just boast about it afterwards regardless."

                    elif(karma() < sanity()):
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

                    if(abs(karma() - sanity()) < 2):
                        # K&S lower than average.
                        $ show_chr("A-CEAAA-AAAC")
                        y "I d-don't really know..."
                        y "Does it really even matter what difficulty we play on?"
                        y "I guess I'll just go for expert, You'll probably just boast about it afterwards regardless."

                    elif(karma() < sanity()):
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
            elif(abs(karma() + sanity() - 2) < 2):
                if(randomMood == -1):
                    # Disadvantage.
                    $ AI_difficulty = 4

                    if(karma() < sanity()):
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

                    if(karma() < sanity()):
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

                    if(karma() < sanity()):
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
            elif(abs(karma() + sanity()) < 2):
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
        y "You can use arrows to move your tetrominoes. Hitting UP will rotate your tetromino, hitting DOWN will speed up your drop."
        y "Hitting SPACE will drop the tetromino instantaneously."
        y "Q key will put the tetromino into hold, but you can't double hold the same tetromino..."
        y "...While the E key will use the tetromino which you are holding."
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
        if karma() > 3 and sanity() > 3:
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

        elif karma() > 3 and sanity() == 3:
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

        elif karma() <= 2:
        #[If K = 1-2 regardless of S value]
            $ show_chr("A-ACAAA-AAAC")
            y "O-oh you won eh...?"
            y "I suppose now would be a good time to rub it in that you won over me."
            $ show_chr("A-ACAAA-AAAC")
            y "G-go ahead. Boast to your heart's content."
            y "I bet you only pretended to have fun playing against me..."
            y "Go on [player]."
        elif sanity() > 2 and karma() < 3:
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

        elif sanity() <= 3 and karma() >= 3:
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

        elif sanity() <= 3 and karma() < 3:
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
        if sanity() > 2 and karma() > 2:
            $ show_chr("A-ACAAA-ALAL")#insert closed smile with open eyes, happy eyebrows and hand on her chest
            y "Oh my..."
            y "Good show, good effort~"
            $ show_chr("A-ACABA-AAAD")# open smile with a hand on her chin and blush on her face
            y "I know you wanted a higher score but there will always be a next time!"
            y "I hope you had fun, [player], I know I did!"

        elif karma() > 4 and sanity() == 3:
        #[If K=4-5 and S=3]
            $ show_chr("A-ACDAA-AMAM")
            y "O-oh... You lost? Uhm... eheh."
            y "I-I hope I did not get too intense for you. Don't feel bad about it [player]. I had a lot of fun."
            y "I hope you did too... O-oh... I mean but... We can do something else if you'd like. I really hope you enjoyed it though. I-It means so much to me... Just time together like this."
            y "Did I make you feel bad [player]? I hope I didn't... I'd give you a hug at least for your efforts..."
            $ show_chr("A-ACAAA-ABAB")
            y "It's the heart and thought that c-counts after all."
            y "S-so... do you want to play again? Or if you want to do something else, that is okay too [player]~"

        elif karma() != 3 and sanity() != 3:
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

        elif sanity() > 2 and karma() < 3:
            $ show_chr("A-AEAAA-AAAC")
            y "Oh... you lost, eh?"
            y "Well then that's no surprise, I guess."
            y "I mean, not that you would care for my input perhaps but.."
            $ show_chr("A-CEAAA-AAAL")
            y "Hm..."
            y "Well, I still hope you enjoyed playing... I guess."

        elif sanity() < 3 and karma() > 3:
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

        elif karma() == 3 and sanity() <= 2:
        #If K= 3 and S: 1-2
            $ show_chr("A-HLAAA-ALAL")
            y "Aww, you lost?"
            y "W-well hey don't feel bad and leave so soon..."
            y "We can stay here in this room together forever. Breathing in each others' scents as we sweat and play this wonderful classic together."
            $ show_chr("A-HCAAA-ALAL")
            y "Here in this room and no one else... I know you want to... And I want to also~"
            y "What do you say [player]? Doesn't that sound so heavenly?" #[maybe show this line as glitch text?]

        elif sanity() < 3 and karma() < 3:
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
    import pygame
    import math
    import copy
    import random
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
            self.hard_drop_occurred = False  # Flag to indicate a hard drop
            self.lines_reward = 3.0
            self.hole_penalty = -5.0
            self.height_penalty_multiplier = -0.1
            self.height_penalty_exponent = 1.8
            self.bumpiness_penalty = -0.3
            self.tetris_bonus = 4.0
            self.tspin_single_bonus = 8.0
            self.tspin_double_bonus = 12.0
            self.tspin_triple_bonus = 16.0
            self.combo = 0
            self.last_clear_type = None
            self.col_heights = []
            self.holes = []
            self.bumpiness = 0
            self.moves_to_execute = []  # Add moves_to_execute as an attribute
            self.oldst = None # Add this to the constructor to initialize the timer
            # Modified piece_list to a bag system
            self.piece_bag = [0, 1, 2, 3, 4, 5, 6]
            random.shuffle(self.piece_bag)
            # Base falling speed (adjust as needed)

            # Speed modifier for each AI level (adjust as needed)
            self.ai_speed_modifiers = {
                0: 0.6,     # Player (or very easy AI)
                1: 0.4,     # AI 1
                2: 0.3,     # AI 2
                3: 0.2,     # AI 3
                4: 0.1,     # AI 4
                5: 0.05,    # AI 5
                6: 0.015,   # AI 6 (or higher, if needed)
            }
            self.soft_drop_speed = 0.002
            # Next piece queue
            self.next_pieces = []
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

            # Initialize next_pieces and get the first pieces
            self.next_pieces = []
            self.get_next_pieces()

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
                # Added T-spin sound effects
                self.soundtspin = "sfx/t-spin.ogg"
                self.soundtspinsingle = "sfx/t-spin.ogg"
                self.soundtspindouble = "sfx/t-spin.ogg"
                self.soundtspintriple = "sfx/t-spin.ogg"
                self.soundtspinsinglemini = "sfx/t-spin.ogg"
                self.soundtspindoublemini = "sfx/t-spin.ogg"

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
                self.soundtspin = "sfx/t-spin.ogg"
                self.soundtspinsingle = "sfx/t-spin.ogg"
                self.soundtspindouble = "sfx/t-spin.ogg"
                self.soundtspintriple = "sfx/t-spin.ogg"
                self.soundtspinsinglemini = "sfx/t-spin.ogg"
                self.soundtspindoublemini = "sfx/t-spin.ogg"

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
                self.soundtspin = "sfx/t-spin.ogg"
                self.soundtspinsingle = "sfx/t-spin.ogg"
                self.soundtspindouble = "sfx/t-spin.ogg"
                self.soundtspintriple = "sfx/t-spin.ogg"
                self.soundtspinsinglemini = "sfx/t-spin.ogg"
                self.soundtspindoublemini = "sfx/t-spin.ogg"

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
                self.soundtspin = "sfx/t-spin.ogg"
                self.soundtspinsingle = "sfx/t-spin.ogg"
                self.soundtspindouble = "sfx/t-spin.ogg"
                self.soundtspintriple = "sfx/t-spin.ogg"
                self.soundtspinsinglemini = "sfx/t-spin.ogg"
                self.soundtspindoublemini = "sfx/t-spin.ogg"

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
                self.soundtspin = "sfx/t-spin.ogg"
                self.soundtspinsingle = "sfx/t-spin.ogg"
                self.soundtspindouble = "sfx/t-spin.ogg"
                self.soundtspintriple = "sfx/t-spin.ogg"
                self.soundtspinsinglemini = "sfx/t-spin.ogg"
                self.soundtspindoublemini = "sfx/t-spin.ogg"

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
                self.soundtspin = "/custom_tetris/t-spin.ogg"
                self.soundtspinsingle = "/custom_tetris/t-spin.ogg"
                self.soundtspindouble = "/custom_tetris/t-spin.ogg"
                self.soundtspintriple = "/custom_tetris/t-spin.ogg"
                self.soundtspinsinglemini = "/custom_tetris/t-spin.ogg"
                self.soundtspindoublemini = "/custom_tetris/t-spin.ogg"

            # SRS Rotation logic
            self.srs_offsets = {
                0: {  # O piece (does not rotate)
                    '0->1': ((0, 0),),
                    '1->0': ((0, 0),),
                    '1->2': ((0, 0),),
                    '2->1': ((0, 0),),
                    '2->3': ((0, 0),),
                    '3->2': ((0, 0),),
                    '3->0': ((0, 0),),
                    '0->3': ((0, 0),),
                },
                6: {  # I piece
                    '0->1': ((0, 0), (-2, 0), (+1, 0), (-2, -1), (+1, +2)),
                    '1->0': ((0, 0), (+2, 0), (-1, 0), (+2, +1), (-1, -2)),
                    '1->2': ((0, 0), (-1, 0), (+2, 0), (-1, +2), (+2, -1)),
                    '2->1': ((0, 0), (+1, 0), (-2, 0), (+1, -2), (-2, +1)),
                    '2->3': ((0, 0), (+2, 0), (-1, 0), (+2, +1), (-1, -2)),
                    '3->2': ((0, 0), (-2, 0), (+1, 0), (-2, -1), (+1, +2)),
                    '3->0': ((0, 0), (+1, 0), (-2, 0), (+1, -2), (-2, +1)),
                    '0->3': ((0, 0), (-1, 0), (+2, 0), (-1, +2), (+2, -1)),
                },
                "others": {
                    '0->1': ((0, 0), (-1, 0), (-1, +1), (0, -2), (-1, -2)),
                    '1->0': ((0, 0), (+1, 0), (+1, -1), (0, +2), (+1, +2)),
                    '1->2': ((0, 0), (+1, 0), (+1, -1), (0, +2), (+1, +2)),
                    '2->1': ((0, 0), (-1, 0), (-1, +1), (0, -2), (-1, -2)),
                    '2->3': ((0, 0), (+1, 0), (+1, +1), (0, -2), (+1, -2)),
                    '3->2': ((0, 0), (-1, 0), (-1, -1), (0, +2), (-1, +2)),
                    '3->0': ((0, 0), (-1, 0), (-1, -1), (0, +2), (-1, +2)),
                    '0->3': ((0, 0), (+1, 0), (+1, +1), (0, -2), (+1, -2)),
                }
            }

            class current_shape:
                shape = ""
                shape_number = ""
                shape_hold = ""
                new_shape_number = self.piece_bag.pop(0)
                next_shape = self.tetris_shapes[new_shape_number]
                x = 5
                y = 1
                move_time = 0.300
                speed = self.ai_speed_modifiers.get(self.AI, 0.6) # Add the speed attribute here
            self.was_it_hold = False
            self.temp_position = 3
            self.current_shape = current_shape()
            self.current_rotation = 0  # SRS rotation state (0, 1, 2, 3)
            self.last_move = "" # remember if last move was a rotation
            self.t_spin = False # true when last valid rotation is done with T piece
            self.level = 1
            self.allLines = 0
            self.oldst = None
            self.new_shape = True
            self.game_over = False
            self.winner = None
            self.Yuri_Face = 0

            # DAS/ARR settings (in seconds)
            self.das_delay = 0.167  # Adjust as needed
            self.arr_speed = 0.033  # Adjust as needed

            # Variables to track key presses for DAS/ARR
            self.left_held = False
            self.right_held = False
            self.left_das_timer = 0
            self.right_das_timer = 0
            self.left_last_move = 0  # For ARR
            self.right_last_move = 0  # For ARR

            # Lock down settings
            self.lock_delay = 0.5  # Lock down delay in seconds (adjust as needed)
            self.max_moves = 15    # Maximum moves/rotations allowed during lock down (adjust as needed)

            # Lock down variables
            self.lock_timer = 0
            self.move_count = 0
            self.is_locking = False  # Flag to indicate if piece is in lock down state

        def generateNewShape(self):
            self.was_it_hold = False
            self.current_shape.x = 5
            self.current_shape.y = 1
            self.current_rotation = 0
            self.current_shape.shape = self.current_shape.next_shape
            self.current_shape.shape_number = self.current_shape.new_shape_number
            # Update next pieces and get a new piece from the bag
            self.next_pieces.pop(0)
            while len(self.next_pieces) < 6: # Make sure there are always 6 pieces
                if len(self.piece_bag) == 0:  # Check if the bag is empty
                    self.piece_bag = [0, 1, 2, 3, 4, 5, 6]
                    random.shuffle(self.piece_bag)  # Reshuffle immediately
                self.next_pieces.append(self.piece_bag.pop(0))
            self.current_shape.new_shape_number = self.next_pieces[0]
            self.current_shape.next_shape = self.tetris_shapes[self.current_shape.new_shape_number]
            self.get_next_pieces()  # Ensure we have 6 pieces in preview
            self.new_shape = False
            self.temp_position = 1
            self.current_shape.speed = self.ai_speed_modifiers.get(self.AI, 0.6) #Also set speed here
            self.combo = 0  # Reset combo when generating a new shape
            self.moves_to_execute = []

        #Function which add shape to stage.
        #Arguments current x and y position of shape in stage
        def addShapeToStage(self, current_x, current_y):
            for idr, row in enumerate(self.current_shape.shape):
                for idc, column in enumerate(row):
                    if column != 0:
                        self.stage[current_y+idr][current_x+idc]=column

        # Function to get the next pieces for the preview
        def get_next_pieces(self):
            needed_pieces = 6 - len(self.next_pieces)
            for _ in range(needed_pieces):
                if len(self.piece_bag) == 0:
                    self.piece_bag = [0, 1, 2, 3, 4, 5, 6]
                    random.shuffle(self.piece_bag)
                self.next_pieces.append(self.piece_bag.pop(0))

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
                # Also play T-spin sounds if conditions are met
                if self.t_spin:
                    if numberOfFullLines == 1:
                        self.score += 400 * self.level # T-Spin Single
                        renpy.sound.play(self.soundtspinsingle)
                    elif numberOfFullLines == 2:
                        self.score += 1200 * self.level  # T-Spin Double
                        renpy.sound.play(self.soundtspindouble)
                    elif numberOfFullLines == 3:
                        self.score += 1600 * self.level  # T-Spin Triple
                        renpy.sound.play(self.soundtspintriple)
                    elif numberOfFullLines == 4:
                        self.score += 800 * self.level
                        renpy.sound.play(self.sound4line)
                elif numberOfFullLines == 1:
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

                self.allLines += numberOfFullLines
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
                self.generateNewShape()
                self.current_shape.speed = self.ai_speed_modifiers.get(self.AI, 0.6) # Set speed for the new shape
                if self.AI != 0:
                    temp_AI = True
                    for idc in range(1, 11):
                        if self.stage[2][idc] != 0:
                            temp_AI = False
                    if temp_AI:
                        self.moves_to_execute = self.Yuri_AI()
                        self.current_shape.y = 0
            if self.oldst is None:
                self.oldst = st
            if self.level > 19:
                speed_Y = 18
            else:
                speed_Y = self.level
            
            if self.temp_position == self.current_shape.y:
                # Check if the piece is in a locking state
                if not self.is_locking or self.move_count < self.max_moves:
                    # If not locking or still allowed to move, then process moves
                    if len(self.moves_to_execute) > 0:  # Use self.moves_to_execute
                        # Initialize horizontal_move to a default value
                        horizontal_move = 0
                        # Process AI-suggested moves (rotations and horizontal movements)
                        # Always process rotations first
                        if self.moves_to_execute[0] == "r":
                            self.current_shape.shape = self.rotateClockWise()
                            del self.moves_to_execute[0]
                            if self.is_locking:
                                self.move_count += 1  # Increment move count
                        # Process horizontal movements after rotations
                        elif self.moves_to_execute[0] == "1" or self.moves_to_execute[0] == "-1":
                            horizontal_move = int(self.moves_to_execute[0])
                            del self.moves_to_execute[0]
                            temp_can_move = True
                            for idr, row in enumerate(self.current_shape.shape):
                                for idc, column in enumerate(row):
                                    if column != 0:
                                        if self.stage[self.current_shape.y + idr][self.current_shape.x + horizontal_move + idc] != 0:
                                            temp_can_move = False
                                            break
                                if not temp_can_move:
                                    break  # Exit outer loop if collision detected
                            if temp_can_move:
                                self.current_shape.x += horizontal_move
                                if self.is_locking:
                                    self.move_count += 1
                        else:
                            print_debug("      Executing Horizontal Move:", horizontal_move)
                            del self.moves_to_execute[0]
                self.temp_position += 1

            dtime = st - self.oldst
            if self.oldst is not None:
                self.oldst = st  # Only update oldst if it's not the first call
            temp_can_go_down = True
            self.t_spin = False  # Reset t-spin flag
            if self.current_shape.move_time <= 0:
                # Check if bottom is empty
                temp_can_go_down = True
                for idr, row in enumerate(self.current_shape.shape):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if self.stage[self.current_shape.y + 1 + idr][self.current_shape.x + idc] != 0:
                                temp_can_go_down = False
                                break
                    if not temp_can_go_down:
                        break

                if temp_can_go_down:
                    self.current_shape.move_time = self.current_shape.speed
                    self.current_shape.y += 1
                    self.is_locking = False  # Reset lock down if piece moves down
                elif self.is_locking:  # Piece is in lock down
                    if st - self.lock_timer >= self.lock_delay or self.move_count >= self.max_moves:
                        # Lock down delay passed or move limit reached
                        self.last_move = ""
                        if not self.hard_drop_occurred:  # Check if hard drop already placed the piece
                            self.addShapeToStage(self.current_shape.x, self.current_shape.y)
                        self.is_locking = False  # Reset lock down flag
                        self.hard_drop_occurred = False # Reset hard drop flag
                        self.new_shape = True  # Generate a new shape
                        # Check for T-spin when piece lands
                        if self.last_move == "rotation" and self.current_shape.shape_number == 0:  # T piece
                            self.t_spin = self.is_t_spin()
                        if self.t_spin:
                            renpy.sound.play(self.soundtspin)
                        else:
                            renpy.sound.play(self.soundbdrop)
                else:
                    # Piece has just landed, but not in locking state
                    self.is_locking = True
                    self.lock_timer = st
                    self.move_count = 0

                if not temp_can_go_down:
                    # Check if we need to lock the piece in place
                    if not self.is_locking:
                        self.last_move = ""
                        # Check if piece can be placed (valid y position) before locking
                        if self.current_shape.y > 0:  # Allow placement if a valid final_y was found
                            self.addShapeToStage(self.current_shape.x, self.current_shape.y)
                            self.is_locking = False  # Reset lock down flag
                            self.hard_drop_occurred = False # Reset hard drop flag
                            self.new_shape = True
                            self.temp_position = 1  # Reset temp_position to 1 to start falling from the top for new shape

            else:
                self.current_shape.move_time -= dtime

            # DAS/ARR Movement
            if self.left_held:
                if st - self.left_das_timer > self.das_delay:  # DAS delay passed
                    if st - self.left_last_move > self.arr_speed:  # ARR speed
                        self.left_last_move = st  # Update last move time
                        temp_can_left = True
                        for idr, row in enumerate(self.current_shape.shape):
                            for idc, column in enumerate(row):
                                if column != 0:
                                    if self.stage[self.current_shape.y + idr][self.current_shape.x - 1 + idc] != 0:
                                        temp_can_left = False
                                        break
                        if temp_can_left:
                            self.current_shape.x -= 1
                            if self.is_locking:
                                self.move_count += 1  # Increment move count

            if self.right_held:
                if st - self.right_das_timer > self.das_delay:  # DAS delay passed
                    if st - self.right_last_move > self.arr_speed:  # ARR speed
                        self.right_last_move = st  # Update last move time
                        temp_can_right = True
                        for idr, row in enumerate(self.current_shape.shape):
                            for idc, column in enumerate(row):
                                if column != 0:
                                    if self.stage[self.current_shape.y + idr][self.current_shape.x + 1 + idc] != 0:
                                        temp_can_right = False
                                        break
                        if temp_can_right:
                            self.current_shape.x += 1
                            if self.is_locking:
                                self.move_count += 1  # Increment move count

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
                # Display next 6 pieces
                for i, next_piece_index in enumerate(self.next_pieces):
                    next_piece = self.tetris_shapes[next_piece_index]
                    draw_shape(-100, 40 + i * 70, next_piece, 0)  # Adjust vertical spacing
                i = "Hold:"
                j = Text(i)
                text_hold_render = renpy.render(j, width, height, st, at)
                r.blit(text_hold_render, (-120, 450))
                draw_shape(-100, 500, self.current_shape.shape_hold,0)
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
                    if self.Yuri_Face != 1 and self.allLines > PlayerForYuri:
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
                    elif self.Yuri_Face != 2 and self.allLines < PlayerForYuri:
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
                    if self.Yuri_Face != 1 and self.score > PlayerForYuri:
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
                    elif self.Yuri_Face != 2 and self.score < PlayerForYuri:
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
                # Display next 6 pieces
                for i, next_piece_index in enumerate(self.next_pieces):
                    next_piece = self.tetris_shapes[next_piece_index]
                    draw_shape(280, 40 + i * 70, next_piece, 0)  # Adjust vertical spacing

            draw_shape(0, 0, self.stage,0)
            draw_shape(self.current_shape.x*self.PIXEL_SIZE, self.current_shape.y*self.PIXEL_SIZE, self.current_shape.shape,1)

            renpy.redraw(self, 0)
            return r

############################################################################################################################
        # Check if the last rotation was a valid T-spin
        def is_t_spin(self):
            x = self.current_shape.x
            y = self.current_shape.y

            # Check at least 3 corners are occupied
            corners = 0
            if self.stage[y][x] != 0:
                corners += 1  # Top-left
            if self.stage[y][x + 2] != 0:
                corners += 1  # Top-right
            if self.stage[y + 2][x] != 0:
                corners += 1  # Bottom-left
            if self.stage[y + 2][x + 2] != 0:
                corners += 1  # Bottom-right

            if corners >= 3:
                return True
            else:
                return False

        # SRS Rotation logic
        def rotateClockWise(self):
            tempShape = self.current_shape.shape
            tempRow = tempShape
            tempX = self.current_shape.x
            tempY = self.current_shape.y
            ifRotation = True
            renpy.sound.play(self.soundrotate)
            self.last_move = "rotation"  # Remember last move
            lenRow = len(self.current_shape.shape)
            lenCol = len(self.current_shape.shape[0])
            
            # Determine offsets based on piece type
            if self.current_shape.shape_number == 0:
                offsets = self.srs_offsets[0]  # O piece offsets
            elif self.current_shape.shape_number == 6:
                offsets = self.srs_offsets[6]  # I piece offsets
            else:
                offsets = self.srs_offsets["others"]  # Offsets for other pieces

            # Get current rotation state string
            rotation_str = str(self.current_rotation) + "->" + str((self.current_rotation + 1) % 4)

            # Perform rotation
            tempRow = [[] for _ in range(lenCol)]
            for idr, row in enumerate(tempShape):
                for idc, column in enumerate(row):
                    tempRow[idc].insert(0, column)
            
            # Apply SRS offsets
            for offset in offsets[rotation_str]:
                ifRotation = True
                dx, dy = offset
                new_x = tempX + dx
                new_y = tempY + dy
                
                # Check if rotated piece with offset is valid
                for idr, row in enumerate(tempRow):
                    for idc, column in enumerate(row):
                        if column != 0:
                            if not (0 < new_x + idc < 11 and 0 < new_y + idr < 21 and self.stage[new_y + idr][new_x + idc] == 0):
                                ifRotation = False
                                break
                    if not ifRotation:
                        break

                if ifRotation:
                    self.current_shape.x = new_x
                    self.current_shape.y = new_y
                    self.current_shape.shape = tempRow
                    self.current_rotation = (self.current_rotation + 1) % 4  # Update rotation state
                    return tempRow  # Return the successfully rotated piece

            # If no valid rotation with offset, revert to original position and rotation state
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

        def event(self, ev, x, y, st):
            import pygame
            temp_can_left = True
            temp_can_right = True
            if ev.type == pygame.KEYDOWN and self.AI == 0:
                if ev.key == pygame.K_UP:
                    # Only allow rotation if not exceeding move limit during lock down
                    if not self.is_locking or self.move_count < self.max_moves:
                        self.current_shape.shape = self.rotateClockWise() # No arguments are passed
                        if self.is_locking:
                            self.move_count += 1  # Increment move count
                elif ev.key == pygame.K_w:
                    # Only allow rotation if not exceeding move limit during lock down
                    if not self.is_locking or self.move_count < self.max_moves:
                        self.current_shape.shape = self.rotate180(self.current_shape.shape)
                        if self.is_locking:
                            self.move_count += 1
                elif ev.key == pygame.K_LEFT:
                    self.left_held = True  # Mark key as held
                    self.left_das_timer = st  # Start DAS timer
                    self.left_last_move = st  # Initialize last move time
                    self.last_move = "left" # Remember last move
                    renpy.sound.play(self.soundmove)
                    # Move piece immediately (initial movement)
                    temp_can_left = True
                    for idr, row in enumerate(self.current_shape.shape):
                        for idc, column in enumerate(row):
                            if column != 0:
                                if self.stage[self.current_shape.y + idr][self.current_shape.x - 1 + idc] != 0:
                                    temp_can_left = False
                                    break
                    if temp_can_left:
                        self.current_shape.x -= 1
                        if self.is_locking:
                            self.move_count += 1
                elif ev.key == pygame.K_RIGHT:
                    self.right_held = True  # Mark key as held
                    self.right_das_timer = st  # Start DAS timer
                    self.right_last_move = st  # Initialize last move time
                    self.last_move = "right" # Remember last move
                    renpy.sound.play(self.soundmove)
                    # Move piece immediately (initial movement)
                    temp_can_right = True
                    for idr, row in enumerate(self.current_shape.shape):
                        for idc, column in enumerate(row):
                            if column != 0:
                                if self.stage[self.current_shape.y + idr][self.current_shape.x + 1 + idc] != 0:
                                    temp_can_right = False
                                    break
                    if temp_can_right:
                        self.current_shape.x += 1
                        if self.is_locking:
                            self.move_count += 1
                elif ev.key == pygame.K_DOWN:
                    self.current_shape.speed = self.soft_drop_speed # Set soft drop speed
                elif ev.key == pygame.K_SPACE:
                    renpy.sound.play(self.soundbdrop)
                    self.addShapeToStage(self.current_shape.x, self.find_bottom())
                    self.new_shape = True
                    self.hard_drop_occurred = True  # Set the flag when hard drop occurs
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

            elif ev.type == pygame.KEYUP:
                if ev.key == pygame.K_LEFT:
                    self.left_held = False  # Mark key as released
                    self.left_das_timer = 0  # Reset DAS timer
                elif ev.key == pygame.K_RIGHT:
                    self.right_held = False
                    self.right_das_timer = 0  # Reset DAS timer
                elif ev.key == pygame.K_DOWN:
                    self.current_shape.speed = self.ai_speed_modifiers.get(self.AI, 0.6)  # Reset to normal speed based on AI

        def rotate180(self, mat):
            # Rotate twice using existing rotateClockWise function
            tempRow = self.rotateClockWise(mat)
            tempRow = self.rotateClockWise(tempRow)
            return tempRow

        def rotateClockWiseAI(self, shape):
            # Implementation for AI rotation
            rotated_shape = []
            for i in range(len(shape[0])):
                new_row = [row[i] for row in reversed(shape)]
                rotated_shape.append(new_row)
            return rotated_shape

        def Yuri_AI(self):
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

        # Replace the Yuri_AI() function
        def Yuri_AI(self):
            def calculate_score(board, lines_cleared, last_move_was_t_spin, is_all_clear, combo):
                """
                Calculates the score of a given board state.

                Args:
                    board: The Tetris board represented as a 2D list.
                    lines_cleared: The number of lines cleared in the last move.
                    last_move_was_t_spin: Boolean indicating if the last move was a T-spin.
                    is_all_clear: Boolean indicating if the board is completely clear.
                    combo: The current combo count.

                Returns:
                    A score representing the desirability of the board state.
                """
                # Weights for different scoring features
                weights = {
                    'aggregate_height': -0.510066,
                    'complete_lines': 0.760666,
                    'holes': -0.35663,
                    'bumpiness': -0.184483,
                    't_spin': 2.0,
                    'combo': 0.5,
                    'all_clear': 10.0
                }

                # Scoring features
                aggregate_height = 0
                holes = 0
                bumpiness = 0

                # Calculate heights and holes
                heights = [0] * 10
                for col in range(1, 11):
                    for row in range(1, 21):
                        if board[row][col]:
                            heights[col - 1] = 21 - row
                            break

                # Calculate aggregate height
                aggregate_height = sum(heights)

                # Calculate holes and bumpiness
                for col in range(10):
                    is_counting_holes = False
                    for row in range(1, 21):
                        if board[row][col]:
                            is_counting_holes = True
                        elif is_counting_holes:
                            holes += 1
                    if col > 0:
                        bumpiness += abs(heights[col] - heights[col - 1])

                # Calculate score using weights
                score = (weights['aggregate_height'] * aggregate_height) + \
                        (weights['complete_lines'] * lines_cleared) + \
                        (weights['holes'] * holes) + \
                        (weights['bumpiness'] * bumpiness)

                # Add T-spin bonus
                if last_move_was_t_spin:
                    score += weights['t_spin']

                # Add combo bonus
                if combo > 0:
                    score += weights['combo'] * combo

                # Add All Clear bonus
                if is_all_clear:
                    score += weights['all_clear']

                return score

            def find_best_move(board, current_piece, next_piece, hold_piece):
                """
                Finds the best move for the current piece by evaluating all possible placements.

                Args:
                    board: The Tetris board.
                    current_piece: The piece to place.
                    next_piece: The next piece in the queue.
                    hold_piece: The currently held piece.

                Returns:
                    A tuple containing the best x-position, rotation, and score.
                """

                best_score = float('-inf')
                best_x = -1
                best_rotation = -1
                best_piece_used = None
                best_moves = []
                current_rotation = self.current_rotation  # Save current rotation state
                temp_moves = []

                def generate_moves(x, y, original_x, original_rotation, rotation_diff):
                    """Generates a list of moves to reach a specific x and rotation from the original."""
                    temp_moves = []

                    # Rotate to target rotation
                    for _ in range(rotation_diff):
                        temp_moves.append("r")

                    # Move horizontally to target x
                    horizontal_moves = x - original_x
                    if horizontal_moves > 0:
                        for _ in range(horizontal_moves):
                            temp_moves.append("1")
                    elif horizontal_moves < 0:
                        for _ in range(abs(horizontal_moves)):
                            temp_moves.append("-1")

                    # Hard drop (represented as "d")
                    temp_moves.append("d")

                    return temp_moves

                pieces_to_evaluate = [
                    (current_piece, "current"),
                ]
                if hold_piece is not None:
                    pieces_to_evaluate.append((hold_piece, "hold"))

                # Evaluate both using the current piece and the hold piece
                for (piece, piece_type) in pieces_to_evaluate:
                    for rotation in range(4):  # Test all 4 rotations
                        valid_xs = set()
                        self.current_shape.shape = piece
                        self.current_shape.x = 5  # Reset to center
                        self.current_shape.y = 1

                        # Rotate piece to target rotation
                        for _ in range(rotation):
                            self.current_shape.shape = self.rotateClockWiseAI(self.current_shape.shape)

                        # This gets the valid x postions on the stage by brute force.
                        min_x, max_x = 10, 1
                        for y in range(1, 21):
                            for x in range(1, 11):
                                if is_valid_move(board, self.current_shape.shape, x, y):
                                    min_x = min(min_x, x)
                                    max_x = max(max_x, x)
                                    valid_xs.add(x)

                        # Now iterate through the valid x ranges considering the rotation and limits.
                        for x in valid_xs:
                            temp_board = [row[:] for row in board]
                            temp_y = drop_piece(temp_board, self.current_shape.shape, x)

                            if temp_y is not None:  # If piece can be placed
                                lines_cleared = clear_lines(temp_board)
                                last_move_was_t_spin = False  # Not detecting T-spins in this AI
                                is_all_clear = all(all(cell == 0 for cell in row[1:11]) for row in temp_board[1:21])

                                rotation_diff = (rotation - current_rotation) % 4

                                current_moves = generate_moves(x, temp_y, 5, current_rotation, rotation_diff)
                                score = calculate_score(
                                    temp_board, lines_cleared, last_move_was_t_spin,
                                    is_all_clear, self.combo + (lines_cleared > 0)
                                )

                                if score > best_score:
                                    best_score = score
                                    best_x = x
                                    best_rotation = rotation
                                    best_piece_used = piece_type
                                    best_moves = current_moves

                # Use the best piece if needed
                if best_piece_used == "hold":
                    best_moves.insert(0, "h")

                self.current_rotation = current_rotation  # Reset rotation state
                self.current_shape.shape = self.tetris_shapes[self.current_shape.shape_number]  # Reset shape
                return best_moves

            def drop_piece(board, piece, x):
                """
                Drops the piece onto the board at the specified x position and finds its lowest valid y position.

                Args:
                    board: The Tetris board.
                    piece: The piece to drop.
                    x: The x-position to drop the piece at.

                Returns:
                    The final y-position of the piece after dropping, or None if the piece cannot be placed.
                """
                for y in range(1, 21 - len(piece) + 1):
                    if not is_valid_move(board, piece, x, y + 1):
                        place_piece(board, piece, x, y)  # Modify the board to place the piece
                        return y
                return None  # Piece cannot be placed

            def place_piece(board, piece, x, y):
                """Places a piece on the board at the specified coordinates."""
                for row_index, row in enumerate(piece):
                    for col_index, cell in enumerate(row):
                        if cell:
                            board[y + row_index][x + col_index] = cell

            def is_valid_move(board, piece, x, y):
                """
                Checks if a move (specified by piece, x, y) is valid on the board.
                """
                for row_index, row in enumerate(piece):
                    for col_index, cell in enumerate(row):
                        if cell:
                            board_x = x + col_index
                            board_y = y + row_index
                            # Check if the cell is outside the board or overlaps with an existing block
                            if not (0 < board_x < 11 and 0 < board_y < 21) or board[board_y][board_x]:
                                return False
                return True

            def clear_lines(board):
                """
                Clears full lines from the board and returns the number of lines cleared.

                Args:
                    board: The Tetris board.

                Returns:
                    The number of lines cleared.
                """
                lines_to_clear = []
                for y in range(1, 21):
                    if all(board[y][x] for x in range(1, 11)):
                        lines_to_clear.append(y)

                lines_cleared = len(lines_to_clear)

                if lines_cleared > 0:
                    # Remove the lines
                    for line_y in lines_to_clear:
                        del board[line_y]
                        board.insert(1, [9] + [0] * 10 + [9])  # Add a new empty line at the top

                return lines_cleared

            if self.new_shape:
                self.generateNewShape()
                self.current_shape.speed = self.ai_speed_modifiers.get(self.AI, 0.6)  # Set speed for the new shape

                if self.AI != 0:
                    temp_AI = True
                    for idc in range(1, 11):
                        if self.stage[2][idc] != 0:
                            temp_AI = False
                            break

                    if temp_AI:
                        self.moves_to_execute = find_best_move(
                            self.stage,
                            self.current_shape.shape,
                            self.tetris_shapes[self.next_pieces[0]],  # Pass next piece from the bag
                            self.current_shape.shape_hold,  # Include hold piece
                        )
                        self.current_shape.y = 0

            return self.moves_to_execute