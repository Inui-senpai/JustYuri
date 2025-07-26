define persistent.skin = 0
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
                y "Alright."
                y "Which theme would you like this time?"
                $pass
            "No.":
                y "I see..."
                $ show_chr("A-AAAAA-AAAA")
                y "Perhaps some other time, then."
                jump ch30_loop
    elif sanity_lvl() > 2 and karma_lvl() < 3:
        menu:
            y "You... want to play Tetris...?"
            "Yes.":
                $ show_chr("A-AFAAA-ALAA")
                y "Oh..."
                $ show_chr("A-BFAAA-ALAA")
                y "Well, sure, I guess I wouldn't really mind."
                $ show_chr("A-AFCAA-ALAA")
                y "I have to wonder if you'll mock me for losing."
                $ show_chr("A-CFCAA-ALAA")
                y "Judging from how much pleasure you derive from my misery I assume you will."
                y "Anyway, just pick a theme and let's get on with it."
                $pass
            "No.":
                y "Oh..."
                $ show_chr("A-AFAAA-ALAA")
                y "Perhaps... some other time, then."
                jump ch30_loop
    elif sanity_lvl() < 3 and karma_lvl() > 2:
        menu:
            y "Y-you want to play Tetris, yes?"
            "Yes.":
                $ show_chr("A-HBAAA-AAAA")
                y "Uhuhuhu~!"
                y "Which theme would you like this time?"
                $ show_chr("A-HBAAA-ALAA")
                y "It doesn't matter which one you'll choose, I'm sure you'll still dominate me no matter what you choose!~"
                $pass
            "No.":
                $ show_chr("A-AEBAA-AAAA")
                y "O-oh..."
                $ show_chr("A-BFBAA-AAAA")
                y "Well..."
                y "Alright..."
                y "Perhaps some other time, then..."
                jump ch30_loop
    elif sanity_lvl() < 3 and karma_lvl() < 3:
        menu:
            y "You want to play Tetris, hm?"
            "Yes.":
                $ show_chr("A-AFCAA-ALAA")
                y "I'm sure you'll somehow find a way to make even such a trivial matter into a nightmare for me..."
                y "Somehow you'll still find a way to humiliate me..."
                $ show_chr("A-BFCAA-AAAA")
                y "Right..."
                y "Anyway, which theme do you want?"
                $pass
            "No.":
                y "Oh..."
                $ show_chr("A-CDAAA-AAAA")
                y "Well... I see..."
                $ show_chr("A-BFCAA-AAAA")
                y "Perhaps some other time when you learn to make up your mind."
                jump ch30_loop

    if current_timecycle_marker == "_night":
        menu:

            "Default Theme.":
                $ show_chr("A-CCAAA-ALAA")
                y "A clean, classic look. Sometimes the simplest approach is the most elegant. I like it."
                $ persistent.skin = 1

            "Tetris 99 Theme.":
                $ show_chr("A-ABAAA-ALAA")
                y "Ah, the battle royale style. Fast-paced and aggressive."
                $ show_chr("A-CCAAA-ALAA")
                y "It makes the game feel much more... competitive, doesn't it?"
                y "Let's see if we can create some sparks."
                extend " Ehehe..."
                $ persistent.skin = 2

            "GameBoy Tetris Theme.":
                $ show_chr("A-CCAAA-ALAA")
                y "The original, right from 1989. It's amazing how timeless this game is."
                y "This brings back a certain... nostalgic feeling. It's comforting, in a way."
                $ persistent.skin = 3

            "Mega Drive Tetris Theme.":
                $ show_chr("A-ABAAA-ALAA")
                y "Oh, this one is a bit of a rare gem, isn't it? Very vibrant and punchy."
                y "The music for this one is particularly energetic. I hope you can keep up, [player]."
                $ persistent.skin = 4

            "M1ND BEND3R Theme.":
                $ show_chr("A-AJAAA-ALAA")
                y "{b}This one...{/b}"
                $ show_chr("A-ADAAA-ALAA")
                y "It feels... different. The colors are so intense. The shadows seem to move on their own."
                $ show_chr("A-CBAAA-ALAA")
                y "It's... unsettling. But in a thrilling way. A perfect theme for us, don't you think?"
                $ persistent.skin = 5

            "Custom Theme.":
                call custom_tetris_checkpoint_start

    else:
        menu:

            "Default Theme.":
                $ show_chr("A-CCAAA-ALAA")
                y "A clean, classic look. Sometimes the simplest approach is the most elegant. I like it."
                $ persistent.skin = 1

            "Tetris 99 Theme.":
                $ show_chr("A-ABAAA-ALAA")
                y "Ah, the battle royale style. Fast-paced and aggressive."
                $ show_chr("A-CCAAA-ALAA")
                y "It makes the game feel much more... competitive, doesn't it?"
                y "Let's see if we can create some sparks."
                extend " Ehehe..."
                $ persistent.skin = 2

            "GameBoy Tetris Theme.":
                $ show_chr("A-CCAAA-ALAA")
                y "The original, right from 1989. It's amazing how timeless this game is."
                y "This brings back a certain... nostalgic feeling. It's comforting, in a way."
                $ persistent.skin = 3

            "Mega Drive Tetris Theme.":
                $ show_chr("A-ABAAA-ALAA")
                y "Oh, this one is a bit of a rare gem, isn't it? Very vibrant and punchy."
                y "The music for this one is particularly energetic. I hope you can keep up, [player]."
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
                    "40 Lines":
                        $ LineLimit = 40
                    "100 Lines":
                        $ LineLimit = 100
                    "150 Lines":
                        $ LineLimit = 150
                    "200 Lines":
                        $ LineLimit = 200
                    "250 Lines":
                        $ LineLimit = 250
                    "300 Lines":
                        $ LineLimit = 300
                    "400 Lines":
                        $ LineLimit = 400
                jump tetris_difficulty
            elif karma_lvl() >= 3:
                #If K = 3-5 regardless of S value
                $ show_chr("A-ACEAA-AMAM")
                y "Oh, lovely choice, [player]~"
                y "W-well, hopefully I will prove a worthy challenge..."
                y "Uhuhuhu..."
                y "Well whoever gets to the specific amount of lines wins..."
                menu:
                    "40 Lines":
                        $ LineLimit = 40
                    "100 Lines":
                        $ LineLimit = 100
                    "150 Lines":
                        $ LineLimit = 150
                    "200 Lines":
                        $ LineLimit = 200
                    "250 Lines":
                        $ LineLimit = 250
                    "300 Lines":
                        $ LineLimit = 300
                    "400 Lines":
                        $ LineLimit = 400
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
                    "40 Lines":
                        $ LineLimit = 40
                    "100 Lines":
                        $ LineLimit = 100
                    "150 Lines":
                        $ LineLimit = 150
                    "200 Lines":
                        $ LineLimit = 200
                    "250 Lines":
                        $ LineLimit = 250
                    "300 Lines":
                        $ LineLimit = 300
                    "400 Lines":
                        $ LineLimit = 400
                jump tetris_difficulty

        "Score":
            if persistent.lovecheck and karma_lvl() > 3 and sanity_lvl() < 2:
                #[If K = 3-5 and lovecheck == true, S = 1-2]
                $ show_chr("A-KLAAA-AKAK")
                y "And maybe you will win me as a prize to be cherished... Forever~"
                y "Or maybe I would win you. Hehe. Either way, everyone wins!"
                menu:
                    "50,000 Points":
                        $ TetrisScore = 20000
                    "100,000 Points":
                        $ TetrisScore = 100000
                    "200,000 Points":
                        $ TetrisScore = 200000
                    "250,000 Points":
                        $ TetrisScore = 250000
                    "500,000 Points":
                        $ TetrisScore = 500000
                    "750,000 Points":
                        $ TetrisScore = 750000
                    "1,000,000 Points":
                        $ TetrisScore = 1000000
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
                    "50,000 Points":
                        $ TetrisScore = 20000
                    "100,000 Points":
                        $ TetrisScore = 100000
                    "200,000 Points":
                        $ TetrisScore = 200000
                    "250,000 Points":
                        $ TetrisScore = 250000
                    "500,000 Points":
                        $ TetrisScore = 500000
                    "750,000 Points":
                        $ TetrisScore = 750000
                    "1,000,000 Points":
                        $ TetrisScore = 1000000
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
                    "50,000 Points":
                        $ TetrisScore = 20000
                    "100,000 Points":
                        $ TetrisScore = 100000
                    "200,000 Points":
                        $ TetrisScore = 200000
                    "250,000 Points":
                        $ TetrisScore = 250000
                    "500,000 Points":
                        $ TetrisScore = 500000
                    "750,000 Points":
                        $ TetrisScore = 750000
                    "1,000,000 Points":
                        $ TetrisScore = 1000000
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

        "Endless": # --- NEW GAME MODE ---
            if karma_lvl() >= 3:
                $ show_chr("A-ADDAA-ALAA")
                y "Just... playing until one of us can't go on? A true battle of endurance."
                $ show_chr("A-AACAA-ALAA")
                y "Very well."
            else:
                $ show_chr("A-AEEAA-ALAA")
                y "So, you just want to see me suffer until I make a mistake?"
                $ show_chr("A-CECAA-ALAA")
                y "Fine."

            jump tetris_difficulty

label custom_tetris_checkpoint_start:
    $ show_chr("A-ACAAA-ABAB")
    y "Oh, you'd like to try your hand on a custom Tetris build?"
    y "Well, let me give you a quick walkthrough of how it's done or do you already have it all figure out?"
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
    y "For the Relaxed, Focused and Intense difficulties it has to be 220 x 420 pixels image. Use the {b}background.png{/b} file from the folder \"game\\images\\tetris\\tetris\" as an example..."
    $ show_chr("A-ACAAA-ABAD")
    y "For the same modes but in the Unyielding, Maniacal and Hopeless difficulties, it is the exact same procedure, but this time you have to delete the grids and name it {b}backgrund_no_grind{/b}... oh yes, and it still has to be a .png file!"
    y "The Co-op mode shares the same procedure, but this time it is 421 x 420 pixels and you name it {b}grids (coop).png{/b}. It's in the same folder again."
    y "Now we come to the blocks."
    y "Fun fact, did you know that a single block is called a Tetromino?"
    y "There are 7 pieces in Tetris which usually have diffrent colors. You could make them the same colors"
    y "But that would be kind of boring. Don't you think?"
    $ show_chr("A-ACAAA-AFAD")
    y "Each pieces is build from individual blocks which are number from 1 to 7."
    y "Also in newer version of Tetris. You can see where the piece will land. We refer it as {b}shadow pieces{/b} "
    y "They also need to have their own colors which are usually transparency of nomral blocks"
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
    y "Is everything good? If not let me know and I will reapet the step again"
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
    y "Pehraps I should explain all steps again"
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

    python:
        # renpy.random.random() returns a float between 0.0 and 1.0.
        # This condition will be true 0.5% of the time.
        show_singularity = (renpy.random.random() < 0.005)

    if show_singularity:
        menu:
            "Relaxed":
                $ AI_difficulty = 1

                if karma_lvl() >= 3:
                    y "A Relaxed pace sounds lovely."
                    y "You just want to enjoy the game without any pressure, don't you? I'm happy to oblige, [player]!"

                elif karma_lvl() < 3:
                    #[If K= 1 or 2 regardless of S value]
                    $ show_chr("A-BEAAA-AMAM")
                    y "..."
                    y "Relaxed? Are you mocking me?"
                    y "To play at such an infantile level... It feels like a jest at my expense."
                    $ show_chr("A-CEBAA-AAAD")
                    y "Whatever... Let us proceed."


            "Focused":
                $ AI_difficulty = 2

                if karma_lvl() >= 3:
                #[If K= 3-5 and S: 3-5]
                    $ show_chr("A-ABABA-AAAJ")
                    y "Oh, a Focused game? A nice, standard challenge."
                    y "Well then, I'd like to see how you do! It's good to get out of your comfort zone a bit."

                elif karma_lvl() < 3:
                #[If K = 1 or 2 regardless of S value]
                    $ show_chr("A-ADCAA-AAAL")
                    y "Hm... A Focused game?"
                    y "I'm surprised you didn't pick something harder just to prove a point. Why bother with such a simple difficulty with me?"
                    y "If this is meant to be a joke, I quite frankly do not understand it."
                    $ show_chr("A-CECAA-ALAL")
                    y "Whatever... Let's just begin."


            "Intense":
                $ AI_difficulty = 3

                if karma_lvl() >= 3:
                #[If K = 3-5 and S = 3-5]
                    $ show_chr("A-ACCAA-AMAM")
                    y "Feeling Intense, are we, [player]? Uhuhu..."
                    y "Well, I do like it when you get a bit more daring. It's rather inspiring."
                    y "Alright then, let the games begin! But don't push yourself too hard... Eheheh."

                elif karma_lvl() < 3:
                #[If K = 1-2]
                    $ show_chr("A-CECAA-ALAL")
                    y "An Intense match... So you really want to rub it in my face just to prove a point."
                    y "Very well then... Let the games begin, I suppose. Hmph."


            "Unyielding":
                $ AI_difficulty = 4

                if karma_lvl() >= 3:
                    $ show_chr("A-DCCBA-AAAD")
                    y "Mmm... Unyielding?"
                    y "Oh dear, [player]. That sounds like a Herculean task. Are you sure?"
                    $ show_chr("A-ABAAA-ALAL")
                    y "Ehehehe... Well, alright, if you insist."
                    y "Prepare your mind for a truly relentless challenge, my dear [player]!"

                elif karma_lvl() > 3 and sanity_lvl() < 3:
                #[If K= 3-5 and S= 2 or 1]
                    $ show_chr("A-DLCBA-AMAM")
                    y "Oh, oh my, yes! Unyielding!"
                    y "A glutton for punishment, aren't you, [player]?"
                    y "Whatever scars you may carry from this, I will bear them with you!"
                    $ show_chr("A-DCAAA-AFAG")
                    y "Show them all what you are made of, sweet [player]!!!"

                elif karma_lvl() < 3:
                #[If K= 2 or 1, regardless of S value]
                    $ show_chr("A-DEDAA-ABAB")
                    y "I see... you chose Unyielding."
                    y "I suppose you just want to jest with me then..."
                    $ show_chr("A-BEABB-AMAM")
                    y "Maybe to prove your point further? To rub it in my face just a little more?"
                    $ show_chr("A-CEAAA-AMAM")
                    y "N-nevermind... It wouldn't matter what I said. Let the games begin."


            "Maniacal":
                $ AI_difficulty = 5

                $ show_chr("A-ACBAA-AIAI")
                y "Feeling Maniacal, are we? You're in for a bumpy ride, [player]..."
                if persistent.lovecheck:
                    $ show_chr("A-ACCBA-AIAI")
                    y "...but I guess you like it that way, don't you..."
                else:
                    if karma() >= 3:
                        $ show_chr("A-ACBAA-ABAL")
                        y "Very well. I'll try my best to offer you a suitable challenge."
                        y "Just keep in mind, it is just a game. It doesn't matter who wins, as long as we are having a good time."
                    elif karma() < 3:
                        $ show_chr("A-AFBAA-ABAL")
                        y "On Maniacal... perhaps I can finally teach you a lesson."


            "Hopeless":
                $ AI_difficulty = 6
                $ show_chr("A-ACAAA-ABAL")
                y "The Hopeless difficulty... I see..."
                y "I'm not even sure if I'm good enough to pull this off but... let's give it a try."


            "Your choice, Yuri":
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
                            y "Oh, how polite of you to let me choose. Why don't we keep it Relaxed for now then, darling~"
                        else:
                            y "Oh, how polite of you to let me choose, [player]. Why don't we keep it Relaxed for now then?"

                    else:
                        # Medium.
                        $ AI_difficulty = 2

                        $ show_chr("A-IAABA-AAAC")
                        if persistent.lovecheck == True:
                            y "Oh, how polite of you to let me choose. Why don't we keep it Focused for now then, darling~"
                        else:
                            y "Oh, how polite of you to let me choose, [player]. Why don't we keep it Focused for now then?"

                # K&S are high.
                elif(abs(karma_lvl() + sanity_lvl() - 8) < 2):
                    if(randomMood == -1):
                        # Relaxed.
                        $ AI_difficulty = 1

                        $ show_chr("A-CCAAA-AAAC")
                        y "Hmm..."
                        $ show_chr("A-ICAAA-AAAC")
                        y "I'm feeling something just a bit less challenging if that's alright with you."
                        y "Relaxed should work just fine for us then."

                    elif(randomMood == 0):
                        # Focused.
                        $ AI_difficulty = 2

                        $ show_chr("A-CCAAA-AAAC")
                        y "Hmm..."
                        $ show_chr("A-ICAAA-AAAC")
                        y "I'm feeling something just a bit challenging if that's alright with you."
                        y "Focused should work just fine for us then."

                    else:
                        # Intense.
                        $ AI_difficulty = 3

                        $ show_chr("A-CCAAA-AAAC")
                        y "Hmm..."
                        $ show_chr("A-ICAAA-AAAC")
                        y "I'm feeling something with a decent bit of challenge if that's alright with you."
                        y "Intense should work just fine for us then."

                # K&S are neutral.
                # Or.
                # K|S is high.
                elif(abs(karma_lvl() + sanity_lvl() - 6) < 2):
                    if(randomMood == -1):
                        # Focused.
                        $ AI_difficulty = 2

                        if(abs(karma_lvl() - sanity_lvl()) < 2):
                            # K&S are neutral.
                            $ show_chr("A-BCAAA-AMAM")
                            y "I-If you're comfortable with that, [player]."
                            y "Don't expect me to give you a free pass though."
                            $ show_chr("A-IAAAA-AMAM")
                            y "Focused should suffice."

                        elif(karma_lvl() < sanity_lvl()):
                            # Low K, High S.
                            $ show_chr("A-CECAA-AAAA")
                            y "..."
                            $ show_chr("A-CDCAA-AAAA")
                            y "Could you at least have put in the effort to choose your own difficulty setting?"
                            y "Let's just get this over with. Focused it is."

                        else:
                            # Low S, High K.
                            $ show_chr("A-DBAAA-AAAA")
                            y "{b}It would be quite fun if you were always this passive towards me [player].{/b}"
                            $ show_chr("A-CAABA-ADAA")
                            y "..."
                            $ show_chr("A-CBABA-ADAA")
                            y "I still need to go ahead and choose a difficulty don't I? Focused should do just fine then, correct?"

                    elif(randomMood == 0):
                        # Intense.
                        $ AI_difficulty = 3

                        if(abs(karma_lvl() - sanity_lvl()) < 2):
                            # K&S are neutral.
                            $ show_chr("A-BCAAA-AMAM")
                            y "I-If you're comfortable with that, [player]."
                            y "Don't expect me to give you a free pass though."
                            $ show_chr("A-IAAAA-AMAM")
                            y "Intense should suffice."

                        elif(karma_lvl() < sanity_lvl()):
                            # Low K, High S.
                            $ show_chr("A-CECAA-AAAA")
                            y "..."
                            $ show_chr("A-CDCAA-AAAA")
                            y "Could you at least have put in the effort to choose your own difficulty setting?"
                            y "Let's just get this over with. Intense it is."

                        else:
                            # Low S, High K.
                            $ show_chr("A-DBAAA-AAAA")
                            y "{b}It would be quite fun if you were always this passive towards me [player].{/b}"
                            $ show_chr("A-CAABA-ADAA")
                            y "..."
                            $ show_chr("A-CBABA-ADAA")
                            y "I still need to go ahead and choose a difficulty don't I? Intense should do just fine then, correct?"

                    else:
                        # Unyielding.
                        $ AI_difficulty = 4

                        if(abs(karma_lvl() - sanity_lvl()) < 2):
                            # K&S are neutral.
                            $ show_chr("A-BCAAA-AMAM")
                            y "I-If you're comfortable with that, [player]."
                            y "Don't expect me to give you a free pass though."
                            $ show_chr("A-IAAAA-AMAM")
                            y "Unyielding should suffice."

                        elif(karma_lvl() < sanity_lvl()):
                            # Low K, High S.
                            $ show_chr("A-CECAA-AAAA")
                            y "..."
                            $ show_chr("A-CDCAA-AAAA")
                            y "Could you at least have put in the effort to choose your own difficulty setting?"
                            y "Let's just get this over with. Unyielding it is."

                        else:
                            # Low S, High K.
                            $ show_chr("A-DBAAA-AAAA")
                            y "{b}It would be quite fun if you were always this passive towards me [player].{/b}"
                            $ show_chr("A-CAABA-ADAA")
                            y "..."
                            $ show_chr("A-CBABA-ADAA")
                            y "I still need to go ahead and choose a difficulty don't I? Unyielding should do just fine then, correct?"

                # K&S are lower than average.
                # Or.
                # K|S is neutral.
                elif(abs(karma_lvl() + sanity_lvl() - 4) < 2):
                    if(randomMood == -1):
                        # Intense.
                        $ AI_difficulty = 3

                        if(abs(karma_lvl() - sanity_lvl()) < 2):
                            # K&S lower than average.
                            $ show_chr("A-CEAAA-AAAC")
                            y "I d-don't really know..."
                            y "Does it really even matter what difficulty we play on?"
                            y "I guess I'll just go for Intense, You'll probably just boast about it afterwards regardless."

                        elif(karma_lvl() < sanity_lvl()):
                            # Low K, Neutral S.
                            $ show_chr("A-CEAAA-AAAC")
                            y "I d-don't really know..."
                            y "Does it really even matter what difficulty we play on?"
                            y "I guess I'll just go for Intense, You'll probably just boast about it afterwards regardless..."
                            $ show_chr("A-CEAAB-AAAJ")
                            y "What did I do to deserve this kind of treatment anyways?"
                            y "..."
                            $ show_chr("A-CEAAA-AAAK")
                            y "Let's just get on with it already."

                        else:
                            # Low S, Neutral K.
                            y "How about we go for Intense if you're willing?"
                            $ show_chr("A-DAAAA-AAAD")
                            y "It would be quite fun to pressure you just a bit."
                            y "Not to mention it's cute to watch you squirm around trying to keep up with me."

                    elif(randomMood == 0):
                        # Unyielding.
                        $ AI_difficulty = 4

                        if(abs(karma_lvl() - sanity_lvl()) < 2):
                            # K&S lower than average.
                            $ show_chr("A-CEAAA-AAAC")
                            y "I d-don't really know..."
                            y "Does it really even matter what difficulty we play on?"
                            y "I guess I'll just go for Unyielding, You'll probably just boast about it afterwards regardless."

                        elif(karma_lvl() < sanity_lvl()):
                            # Low K, Neutral S.
                            $ show_chr("A-CEAAA-AAAC")
                            y "I d-don't really know..."
                            y "Does it really even matter what difficulty we play on?"
                            y "I guess I'll just go for Unyielding, You'll probably just boast about it afterwards regardless..."
                            $ show_chr("A-CEAAB-AAAJ")
                            y "What did I do to deserve this kind of treatment anyways?"
                            y "..."
                            $ show_chr("A-CEAAA-AAAK")
                            y "Let's just get on with it already."

                        else:
                            # Low S, Neutral K.
                            y "How about we go for Unyielding if you're willing?"
                            $ show_chr("A-DAAAA-AAAD")
                            y "It would be quite fun to pressure you just a bit."
                            y "Not to mention it's cute to watch you squirm around trying to keep up with me."

                    else:
                        # Maniacal.
                        $ AI_difficulty = 5

                        if(abs(karma_lvl() - sanity_lvl()) < 2):
                            # K&S lower than average.
                            $ show_chr("A-CEAAA-AAAC")
                            y "I d-don't really know..."
                            y "Does it really even matter what difficulty we play on?"
                            y "I guess I'll just go for Maniacal, You'll probably just boast about it afterwards regardless."

                        elif(karma_lvl() < sanity_lvl()):
                            # Low K, Neutral S.
                            $ show_chr("A-CEAAA-AAAC")
                            y "I d-don't really know..."
                            y "Does it really even matter what difficulty we play on?"
                            y "I guess I'll just go for Maniacal, You'll probably just boast about it afterwards regardless..."
                            $ show_chr("A-CEAAB-AAAJ")
                            y "What did I do to deserve this kind of treatment anyways?"
                            y "..."
                            $ show_chr("A-CEAAA-AAAK")
                            y "Let's just get on with it already."

                        else:
                            # Low S, Neutral K.
                            y "How about we go for Maniacal if you're willing?"
                            $ show_chr("A-DAAAA-AAAD")
                            y "It would be quite fun to pressure you just a bit."
                            y "Not to mention it's cute to watch you squirm around trying to keep up with me."

                # K&S are low.
                # Or.
                # K|S is minimal.
                elif(abs(karma_lvl() + sanity_lvl() - 2) < 2):
                    if(randomMood == -1):
                        # Unyielding.
                        $ AI_difficulty = 4

                        if(karma_lvl() < sanity_lvl()):
                            $ show_chr ("A-AECAA-AAAF")
                            y "I couldn't honestly care less what difficulty we play at by this point."
                            y "N-No wait, you know what?"
                            y "This would make for a good opportunity to put you in your place, and I won't waste it."
                            y "Let's set it to Unyielding and see just how well you do."

                        else:
                            $ show_chr("A-AECAA-AAAF")
                            y "I couldn't honestly care less what difficulty we play at by this point."
                            y "N-No wait, you know what?"
                            y "This would make for a good opportunity to put you in your place, and I won't waste it."
                            $ show_chr ("A-AECAA-AAAG")
                            y "Let's set it to Unyielding and see just how well you do."

                    elif(randomMood == 0):
                        # Maniacal.
                        $ AI_difficulty = 5

                        if(karma_lvl() < sanity_lvl()):
                            $ show_chr ("A-AECAA-AAAF")
                            y "I couldn't honestly care less what difficulty we play at by this point."
                            y "N-No wait, you know what?"
                            y "This would make for a good opportunity to put you in your place, and I won't waste it."
                            y "Let's set it to Maniacal and see just how well you do."

                        else:
                            $ show_chr("A-AECAA-AAAF")
                            y "I couldn't honestly care less what difficulty we play at by this point."
                            y "N-No wait, you know what?"
                            y "This would make for a good opportunity to put you in your place, and I won't waste it."
                            $ show_chr ("A-AECAA-AAAG")
                            y "Let's set it to Maniacal and see just how well you do."

                    else:
                        # Hopeless.
                        $ AI_difficulty = 6

                        if(karma_lvl() < sanity_lvl()):
                            $ show_chr ("A-AECAA-AAAF")
                            y "I couldn't honestly care less what difficulty we play at by this point."
                            y "N-No wait, you know what?"
                            y "This would make for a good opportunity to put you in your place, and I won't waste it."
                            y "Let's set it to Hopeless and see just how well you do."

                        else:
                            $ show_chr("A-AECAA-AAAF")
                            y "I couldn't honestly care less what difficulty we play at by this point."
                            y "N-No wait, you know what?"
                            y "This would make for a good opportunity to put you in your place, and I won't waste it."
                            $ show_chr ("A-AECAA-AAAG")
                            y "Let's set it to Hopeless and see just how well you do."

                # K&S are almost minimal.
                elif(abs(karma_lvl() + sanity_lvl()) < 2):
                    if(randomMood == -1):
                        # Maniacal.
                        $ AI_difficulty = 5

                        $ show_chr("A-DBCAA-AAAF")
                        y "{b}HA HA...{/b}"
                        y "You want me to choose the difficulty?"
                        y "Fine [player], your wish is my command."
                        $ show_chr("A-DBCAA-AAAC")
                        y "How about Maniacal hmm? Seems like a fair competition don't you think?"
                        $ show_chr("A-CBCAA-AAAC")
                        y "I just hope you'll be able to keep up the pace. It would be quite a shame if I decimated the scoreboard."

                    else:
                        # Hopeless.
                        $ AI_difficulty = 6

                        $ show_chr("A-DBCAA-AAAF")
                        y "{b}HA HA...{/b}"
                        y "You want me to choose the difficulty?"
                        y "Fine [player], your wish is my command."
                        $ show_chr("A-DBCAA-AAAC")
                        y "How about Hopeless hmm? Seems like a fair competition don't you think?"
                        $ show_chr("A-CBCAA-AAAC")
                        y "I just hope you'll be able to keep up the pace. It would be quite a shame if I decimated the scoreboard."

            "??????????":
                $ AI_difficulty = 7
                $ show_chr("A-AFAAA-ALAA")
                y "..."
                $ show_chr("A-ADAAA-ALAA")
                y "You weren't supposed to see that."
                $ show_chr("A-DDAAA-ALAA")
                y "What... are you?"
                $ show_chr("A-ADAAA-ALAA")
                y "..."
                $ show_chr("A-AJDAA-ALAA")
                y "Let's see what happens when we break the rules."

    else:
        menu:
            "Relaxed":
                $ AI_difficulty = 1

                if karma_lvl() >= 3:
                    y "A Relaxed pace sounds lovely."
                    y "You just want to enjoy the game without any pressure, don't you? I'm happy to oblige, [player]!"

                elif karma_lvl() < 3:
                    #[If K= 1 or 2 regardless of S value]
                    $ show_chr("A-BEAAA-AMAM")
                    y "..."
                    y "Relaxed? Are you mocking me?"
                    y "To play at such an infantile level... It feels like a jest at my expense."
                    $ show_chr("A-CEBAA-AAAD")
                    y "Whatever... Let us proceed."


            "Focused":
                $ AI_difficulty = 2

                if karma_lvl() >= 3:
                #[If K= 3-5 and S: 3-5]
                    $ show_chr("A-ABABA-AAAJ")
                    y "Oh, a Focused game? A nice, standard challenge."
                    y "Well then, I'd like to see how you do! It's good to get out of your comfort zone a bit."

                elif karma_lvl() < 3:
                #[If K = 1 or 2 regardless of S value]
                    $ show_chr("A-ADCAA-AAAL")
                    y "Hm... A Focused game?"
                    y "I'm surprised you didn't pick something harder just to prove a point. Why bother with such a simple difficulty with me?"
                    y "If this is meant to be a joke, I quite frankly do not understand it."
                    $ show_chr("A-CECAA-ALAL")
                    y "Whatever... Let's just begin."


            "Intense":
                $ AI_difficulty = 3

                if karma_lvl() >= 3:
                #[If K = 3-5 and S = 3-5]
                    $ show_chr("A-ACCAA-AMAM")
                    y "Feeling Intense, are we, [player]? Uhuhu..."
                    y "Well, I do like it when you get a bit more daring. It's rather inspiring."
                    y "Alright then, let the games begin! But don't push yourself too hard... Eheheh."

                elif karma_lvl() < 3:
                #[If K = 1-2]
                    $ show_chr("A-CECAA-ALAL")
                    y "An Intense match... So you really want to rub it in my face just to prove a point."
                    y "Very well then... Let the games begin, I suppose. Hmph."


            "Unyielding":
                $ AI_difficulty = 4

                if karma_lvl() >= 3:
                    $ show_chr("A-DCCBA-AAAD")
                    y "Mmm... Unyielding?"
                    y "Oh dear, [player]. That sounds like a Herculean task. Are you sure?"
                    $ show_chr("A-ABAAA-ALAL")
                    y "Ehehehe... Well, alright, if you insist."
                    y "Prepare your mind for a truly relentless challenge, my dear [player]!"

                elif karma_lvl() > 3 and sanity_lvl() < 3:
                #[If K= 3-5 and S= 2 or 1]
                    $ show_chr("A-DLCBA-AMAM")
                    y "Oh, oh my, yes! Unyielding!"
                    y "A glutton for punishment, aren't you, [player]?"
                    y "Whatever scars you may carry from this, I will bear them with you!"
                    $ show_chr("A-DCAAA-AFAG")
                    y "Show them all what you are made of, sweet [player]!!!"

                elif karma_lvl() < 3:
                #[If K= 2 or 1, regardless of S value]
                    $ show_chr("A-DEDAA-ABAB")
                    y "I see... you chose Unyielding."
                    y "I suppose you just want to jest with me then..."
                    $ show_chr("A-BEABB-AMAM")
                    y "Maybe to prove your point further? To rub it in my face just a little more?"
                    $ show_chr("A-CEAAA-AMAM")
                    y "N-nevermind... It wouldn't matter what I said. Let the games begin."


            "Maniacal":
                $ AI_difficulty = 5

                $ show_chr("A-ACBAA-AIAI")
                y "Feeling Maniacal, are we? You're in for a bumpy ride, [player]..."
                if persistent.lovecheck:
                    $ show_chr("A-ACCBA-AIAI")
                    y "...but I guess you like it that way, don't you..."
                else:
                    if karma() >= 3:
                        $ show_chr("A-ACBAA-ABAL")
                        y "Very well. I'll try my best to offer you a suitable challenge."
                        y "Just keep in mind, it is just a game. It doesn't matter who wins, as long as we are having a good time."
                    elif karma() < 3:
                        $ show_chr("A-AFBAA-ABAL")
                        y "On Maniacal... perhaps I can finally teach you a lesson."


            "Hopeless":
                $ AI_difficulty = 6
                $ show_chr("A-ACAAA-ABAL")
                y "The Hopeless difficulty... I see..."
                y "I'm not even sure if I'm good enough to pull this off but... let's give it a try."


            "Your choice, Yuri":
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
                            y "Oh, how polite of you to let me choose. Why don't we keep it Relaxed for now then, darling~"
                        else:
                            y "Oh, how polite of you to let me choose, [player]. Why don't we keep it Relaxed for now then?"

                    else:
                        # Medium.
                        $ AI_difficulty = 2

                        $ show_chr("A-IAABA-AAAC")
                        if persistent.lovecheck == True:
                            y "Oh, how polite of you to let me choose. Why don't we keep it Focused for now then, darling~"
                        else:
                            y "Oh, how polite of you to let me choose, [player]. Why don't we keep it Focused for now then?"

                # K&S are high.
                elif(abs(karma_lvl() + sanity_lvl() - 8) < 2):
                    if(randomMood == -1):
                        # Relaxed.
                        $ AI_difficulty = 1

                        $ show_chr("A-CCAAA-AAAC")
                        y "Hmm..."
                        $ show_chr("A-ICAAA-AAAC")
                        y "I'm feeling something just a bit less challenging if that's alright with you."
                        y "Relaxed should work just fine for us then."

                    elif(randomMood == 0):
                        # Focused.
                        $ AI_difficulty = 2

                        $ show_chr("A-CCAAA-AAAC")
                        y "Hmm..."
                        $ show_chr("A-ICAAA-AAAC")
                        y "I'm feeling something just a bit challenging if that's alright with you."
                        y "Focused should work just fine for us then."

                    else:
                        # Intense.
                        $ AI_difficulty = 3

                        $ show_chr("A-CCAAA-AAAC")
                        y "Hmm..."
                        $ show_chr("A-ICAAA-AAAC")
                        y "I'm feeling something with a decent bit of challenge if that's alright with you."
                        y "Intense should work just fine for us then."

                # K&S are neutral.
                # Or.
                # K|S is high.
                elif(abs(karma_lvl() + sanity_lvl() - 6) < 2):
                    if(randomMood == -1):
                        # Focused.
                        $ AI_difficulty = 2

                        if(abs(karma_lvl() - sanity_lvl()) < 2):
                            # K&S are neutral.
                            $ show_chr("A-BCAAA-AMAM")
                            y "I-If you're comfortable with that, [player]."
                            y "Don't expect me to give you a free pass though."
                            $ show_chr("A-IAAAA-AMAM")
                            y "Focused should suffice."

                        elif(karma_lvl() < sanity_lvl()):
                            # Low K, High S.
                            $ show_chr("A-CECAA-AAAA")
                            y "..."
                            $ show_chr("A-CDCAA-AAAA")
                            y "Could you at least have put in the effort to choose your own difficulty setting?"
                            y "Let's just get this over with. Focused it is."

                        else:
                            # Low S, High K.
                            $ show_chr("A-DBAAA-AAAA")
                            y "{b}It would be quite fun if you were always this passive towards me [player].{/b}"
                            $ show_chr("A-CAABA-ADAA")
                            y "..."
                            $ show_chr("A-CBABA-ADAA")
                            y "I still need to go ahead and choose a difficulty don't I? Focused should do just fine then, correct?"

                    elif(randomMood == 0):
                        # Intense.
                        $ AI_difficulty = 3

                        if(abs(karma_lvl() - sanity_lvl()) < 2):
                            # K&S are neutral.
                            $ show_chr("A-BCAAA-AMAM")
                            y "I-If you're comfortable with that, [player]."
                            y "Don't expect me to give you a free pass though."
                            $ show_chr("A-IAAAA-AMAM")
                            y "Intense should suffice."

                        elif(karma_lvl() < sanity_lvl()):
                            # Low K, High S.
                            $ show_chr("A-CECAA-AAAA")
                            y "..."
                            $ show_chr("A-CDCAA-AAAA")
                            y "Could you at least have put in the effort to choose your own difficulty setting?"
                            y "Let's just get this over with. Intense it is."

                        else:
                            # Low S, High K.
                            $ show_chr("A-DBAAA-AAAA")
                            y "{b}It would be quite fun if you were always this passive towards me [player].{/b}"
                            $ show_chr("A-CAABA-ADAA")
                            y "..."
                            $ show_chr("A-CBABA-ADAA")
                            y "I still need to go ahead and choose a difficulty don't I? Intense should do just fine then, correct?"

                    else:
                        # Unyielding.
                        $ AI_difficulty = 4

                        if(abs(karma_lvl() - sanity_lvl()) < 2):
                            # K&S are neutral.
                            $ show_chr("A-BCAAA-AMAM")
                            y "I-If you're comfortable with that, [player]."
                            y "Don't expect me to give you a free pass though."
                            $ show_chr("A-IAAAA-AMAM")
                            y "Unyielding should suffice."

                        elif(karma_lvl() < sanity_lvl()):
                            # Low K, High S.
                            $ show_chr("A-CECAA-AAAA")
                            y "..."
                            $ show_chr("A-CDCAA-AAAA")
                            y "Could you at least have put in the effort to choose your own difficulty setting?"
                            y "Let's just get this over with. Unyielding it is."

                        else:
                            # Low S, High K.
                            $ show_chr("A-DBAAA-AAAA")
                            y "{b}It would be quite fun if you were always this passive towards me [player].{/b}"
                            $ show_chr("A-CAABA-ADAA")
                            y "..."
                            $ show_chr("A-CBABA-ADAA")
                            y "I still need to go ahead and choose a difficulty don't I? Unyielding should do just fine then, correct?"

                # K&S are lower than average.
                # Or.
                # K|S is neutral.
                elif(abs(karma_lvl() + sanity_lvl() - 4) < 2):
                    if(randomMood == -1):
                        # Intense.
                        $ AI_difficulty = 3

                        if(abs(karma_lvl() - sanity_lvl()) < 2):
                            # K&S lower than average.
                            $ show_chr("A-CEAAA-AAAC")
                            y "I d-don't really know..."
                            y "Does it really even matter what difficulty we play on?"
                            y "I guess I'll just go for Intense, You'll probably just boast about it afterwards regardless."

                        elif(karma_lvl() < sanity_lvl()):
                            # Low K, Neutral S.
                            $ show_chr("A-CEAAA-AAAC")
                            y "I d-don't really know..."
                            y "Does it really even matter what difficulty we play on?"
                            y "I guess I'll just go for Intense, You'll probably just boast about it afterwards regardless..."
                            $ show_chr("A-CEAAB-AAAJ")
                            y "What did I do to deserve this kind of treatment anyways?"
                            y "..."
                            $ show_chr("A-CEAAA-AAAK")
                            y "Let's just get on with it already."

                        else:
                            # Low S, Neutral K.
                            y "How about we go for Intense if you're willing?"
                            $ show_chr("A-DAAAA-AAAD")
                            y "It would be quite fun to pressure you just a bit."
                            y "Not to mention it's cute to watch you squirm around trying to keep up with me."

                    elif(randomMood == 0):
                        # Unyielding.
                        $ AI_difficulty = 4

                        if(abs(karma_lvl() - sanity_lvl()) < 2):
                            # K&S lower than average.
                            $ show_chr("A-CEAAA-AAAC")
                            y "I d-don't really know..."
                            y "Does it really even matter what difficulty we play on?"
                            y "I guess I'll just go for Unyielding, You'll probably just boast about it afterwards regardless."

                        elif(karma_lvl() < sanity_lvl()):
                            # Low K, Neutral S.
                            $ show_chr("A-CEAAA-AAAC")
                            y "I d-don't really know..."
                            y "Does it really even matter what difficulty we play on?"
                            y "I guess I'll just go for Unyielding, You'll probably just boast about it afterwards regardless..."
                            $ show_chr("A-CEAAB-AAAJ")
                            y "What did I do to deserve this kind of treatment anyways?"
                            y "..."
                            $ show_chr("A-CEAAA-AAAK")
                            y "Let's just get on with it already."

                        else:
                            # Low S, Neutral K.
                            y "How about we go for Unyielding if you're willing?"
                            $ show_chr("A-DAAAA-AAAD")
                            y "It would be quite fun to pressure you just a bit."
                            y "Not to mention it's cute to watch you squirm around trying to keep up with me."

                    else:
                        # Maniacal.
                        $ AI_difficulty = 5

                        if(abs(karma_lvl() - sanity_lvl()) < 2):
                            # K&S lower than average.
                            $ show_chr("A-CEAAA-AAAC")
                            y "I d-don't really know..."
                            y "Does it really even matter what difficulty we play on?"
                            y "I guess I'll just go for Maniacal, You'll probably just boast about it afterwards regardless."

                        elif(karma_lvl() < sanity_lvl()):
                            # Low K, Neutral S.
                            $ show_chr("A-CEAAA-AAAC")
                            y "I d-don't really know..."
                            y "Does it really even matter what difficulty we play on?"
                            y "I guess I'll just go for Maniacal, You'll probably just boast about it afterwards regardless..."
                            $ show_chr("A-CEAAB-AAAJ")
                            y "What did I do to deserve this kind of treatment anyways?"
                            y "..."
                            $ show_chr("A-CEAAA-AAAK")
                            y "Let's just get on with it already."

                        else:
                            # Low S, Neutral K.
                            y "How about we go for Maniacal if you're willing?"
                            $ show_chr("A-DAAAA-AAAD")
                            y "It would be quite fun to pressure you just a bit."
                            y "Not to mention it's cute to watch you squirm around trying to keep up with me."

                # K&S are low.
                # Or.
                # K|S is minimal.
                elif(abs(karma_lvl() + sanity_lvl() - 2) < 2):
                    if(randomMood == -1):
                        # Unyielding.
                        $ AI_difficulty = 4

                        if(karma_lvl() < sanity_lvl()):
                            $ show_chr ("A-AECAA-AAAF")
                            y "I couldn't honestly care less what difficulty we play at by this point."
                            y "N-No wait, you know what?"
                            y "This would make for a good opportunity to put you in your place, and I won't waste it."
                            y "Let's set it to Unyielding and see just how well you do."

                        else:
                            $ show_chr("A-AECAA-AAAF")
                            y "I couldn't honestly care less what difficulty we play at by this point."
                            y "N-No wait, you know what?"
                            y "This would make for a good opportunity to put you in your place, and I won't waste it."
                            $ show_chr ("A-AECAA-AAAG")
                            y "Let's set it to Unyielding and see just how well you do."

                    elif(randomMood == 0):
                        # Maniacal.
                        $ AI_difficulty = 5

                        if(karma_lvl() < sanity_lvl()):
                            $ show_chr ("A-AECAA-AAAF")
                            y "I couldn't honestly care less what difficulty we play at by this point."
                            y "N-No wait, you know what?"
                            y "This would make for a good opportunity to put you in your place, and I won't waste it."
                            y "Let's set it to Maniacal and see just how well you do."

                        else:
                            $ show_chr("A-AECAA-AAAF")
                            y "I couldn't honestly care less what difficulty we play at by this point."
                            y "N-No wait, you know what?"
                            y "This would make for a good opportunity to put you in your place, and I won't waste it."
                            $ show_chr ("A-AECAA-AAAG")
                            y "Let's set it to Maniacal and see just how well you do."

                    else:
                        # Hopeless.
                        $ AI_difficulty = 6

                        if(karma_lvl() < sanity_lvl()):
                            $ show_chr ("A-AECAA-AAAF")
                            y "I couldn't honestly care less what difficulty we play at by this point."
                            y "N-No wait, you know what?"
                            y "This would make for a good opportunity to put you in your place, and I won't waste it."
                            y "Let's set it to Hopeless and see just how well you do."

                        else:
                            $ show_chr("A-AECAA-AAAF")
                            y "I couldn't honestly care less what difficulty we play at by this point."
                            y "N-No wait, you know what?"
                            y "This would make for a good opportunity to put you in your place, and I won't waste it."
                            $ show_chr ("A-AECAA-AAAG")
                            y "Let's set it to Hopeless and see just how well you do."

                # K&S are almost minimal.
                elif(abs(karma_lvl() + sanity_lvl()) < 2):
                    if(randomMood == -1):
                        # Maniacal.
                        $ AI_difficulty = 5

                        $ show_chr("A-DBCAA-AAAF")
                        y "{b}HA HA...{/b}"
                        y "You want me to choose the difficulty?"
                        y "Fine [player], your wish is my command."
                        $ show_chr("A-DBCAA-AAAC")
                        y "How about Maniacal hmm? Seems like a fair competition don't you think?"
                        $ show_chr("A-CBCAA-AAAC")
                        y "I just hope you'll be able to keep up the pace. It would be quite a shame if I decimated the scoreboard."

                    else:
                        # Hopeless.
                        $ AI_difficulty = 6

                        $ show_chr("A-DBCAA-AAAF")
                        y "{b}HA HA...{/b}"
                        y "You want me to choose the difficulty?"
                        y "Fine [player], your wish is my command."
                        $ show_chr("A-DBCAA-AAAC")
                        y "How about Hopeless hmm? Seems like a fair competition don't you think?"
                        $ show_chr("A-CBCAA-AAAC")
                        y "I just hope you'll be able to keep up the pace. It would be quite a shame if I decimated the scoreboard."


label tetris_rules:
    $ show_chr("A-GAGAA-AAAA")
    if persistent.tetris_first:
        y "Allow me to explain the controls..."
        y "You use the Left and Right arrows to move your piece. A quick tap moves it once, while holding the key will make it slide."
        y "Use the Up arrow to rotate your piece clockwise, and the Z key to rotate it counter-clockwise."
        y "Pressing the Down arrow will make the piece 'soft drop', or fall faster."
        y "The Spacebar will 'hard drop' the piece, instantly locking it at the bottom."
        y "Finally, you can press C to swap your current piece with the one in the 'Hold' slot. You can only do this once per piece!"
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
    # The player and AI Tetris instances now require a reference to each other
    # to compare scores for win conditions and dynamic events.
    if AI_difficulty != "CO_OP":
        fixed:
            area (150, 120, 600, 1100)
            # The player's Tetris instance.
            # Pass the AI_difficulty to the player's instance as well.
            default tetris_player = TetrisDisplayable(is_ai=False, ai_difficulty=AI_difficulty)

            # The AI opponent's instance.
            default tetris_Yuri = TetrisDisplayable(is_ai=True, ai_difficulty=AI_difficulty, opponent_game=tetris_player.game)
            # Give the player a reference to the AI's game state.
            $ tetris_player.set_opponent(tetris_Yuri.game)

            add tetris_player

        fixed:
            area (900, 120, 600, 1100)
            add tetris_Yuri
    else:
        fixed:
            area (50, 120, 600, 1100)
            default tetris_Co_OP = CoOpTetrisDisplayable() 
            add tetris_Co_OP

init python:
    import pygame
    import random
    import copy

    # (The configuration constants and the TetrisGame class from the previous step
    # are assumed to be here. They are included again for completeness.)

    # --- NEW CONTROL CONSTANTS ---
    DAS_DELAY = 0.16  # 160ms before auto-shift starts
    ARR_DELAY = 0.03  # 30ms between movements during auto-shift (very fast)
    # --- END NEW CONSTANTS ---

    #-----------------------------------------
    # MODERN TETRIS CONFIGURATION
    #-----------------------------------------
    BOARD_WIDTH = 10
    BOARD_HEIGHT = 22
    VISIBLE_BOARD_HEIGHT = 20
    PIXEL_SIZE = 20
    LOCK_DELAY = 0.5

    TETROMINOES = {
        'T': {'shape': [[1, 1, 1], [0, 1, 0]], 'color_id': 1},
        'S': {'shape': [[0, 2, 2], [2, 2, 0]], 'color_id': 2},
        'Z': {'shape': [[3, 3, 0], [0, 3, 3]], 'color_id': 3},
        'J': {'shape': [[4, 0, 0], [4, 4, 4]], 'color_id': 4},
        'L': {'shape': [[0, 0, 5], [5, 5, 5]], 'color_id': 5},
        'I': {'shape': [[6, 6, 6, 6]], 'color_id': 6},
        'O': {'shape': [[7, 7], [7, 7]], 'color_id': 7}
    }
    
    JLSTZ_KICKS = { '0-1': [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)], '1-0': [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)], '1-2': [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)], '2-1': [(0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2)], '2-3': [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)], '3-2': [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)], '3-0': [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)], '0-3': [(0, 0), (1, 0), (1, 1), (0, -2), (1, -2)]}
    I_KICKS = { '0-1': [(0, 0), (-2, 0), (1, 0), (-2, -1), (1, 2)], '1-0': [(0, 0), (2, 0), (-1, 0), (2, 1), (-1, -2)], '1-2': [(0, 0), (-1, 0), (2, 0), (-1, 2), (2, -1)], '2-1': [(0, 0), (1, 0), (-2, 0), (1, -2), (-2, 1)], '2-3': [(0, 0), (2, 0), (-1, 0), (2, 1), (-1, -2)], '3-2': [(0, 0), (-2, 0), (1, 0), (-2, -1), (1, 2)], '3-0': [(0, 0), (1, 0), (-2, 0), (1, -2), (-2, 1)], '0-3': [(0, 0), (-1, 0), (2, 0), (-1, 2), (2, -1)]}

    SKINS = {1: {"path": "images/tetris/tetris/", "sfx_suffix": ".ogg"}, 2: {"path": "images/tetris/tetris_99/", "sfx_suffix": "(99).ogg"}, 3: {"path": "images/tetris/tetris_gb/", "sfx_suffix": ".ogg"}, 4: {"path": "images/tetris/tetris_gmd/", "sfx_suffix": "(g).ogg"}, 5: {"path": "images/tetris/tetris_mb/", "sfx_suffix": "(mb).ogg"}, 6: {"path": "/custom_tetris/", "sfx_suffix": ".ogg"}}

    # --- AI Difficulty Scaling ---
    # Multiplier for the natural gravity affecting the AI's pieces.
    # A higher number means a faster fall speed.
    AI_GRAVITY_MULTIPLIERS = {
        1: 1.0,   # Relaxed: Normal speed
        2: 1.2,   # Focused: 20% faster
        3: 1.5,   # Intense: 50% faster
        4: 2.0,   # Unyielding: 2x faster
        5: 3.0,   # Maniacal: 3x faster
        6: 5.0,   # Hopeless: 5x faster
        7: 8.0    # Singularity: 8x faster
    }

    # Delay in seconds between each of the AI's physical actions (move, rotate).
    # A lower number means the AI executes its plan much faster.
    AI_ACTION_DELAY = {
        1: (0.12, 0.08),  # Relaxed: Starts slow, gets moderately slow.
        2: (0.10, 0.06),  # Focused: Starts moderately slow, gets reasonably fast.
        3: (0.08, 0.04),  # Intense: Starts fast, gets very fast.
        4: (0.06, 0.02),  # Unyielding: Starts very fast, gets extremely fast.
        5: (0.04, 0.01),  # Maniacal: Starts extremely fast, becomes nearly instant.
        6: (0.0, 0.0),    # Hopeless: Is always instant.
        7: (0.0, 0.0),    # Singularity: Is always instant.
    }

    # The level at which an AI is considered to have reached its "peak" skill.
    # Its reaction speed will scale progressively until it reaches this level.
    AI_PERFECTION_LEVEL = 20.0 # Use a float for accurate division

    #-----------------------------------------
    # CORE TETRIS GAME LOGIC CLASS (Unchanged)
    #-----------------------------------------
    class TetrisGame:
        # This class is identical to the one from the previous response.
        # It handles all game state, rules, and logic internally.
        def __init__(self, difficulty=0): # difficulty=0 for player, 1-6 for AI
            self.board = [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
            self.score = 0
            self.level = 1
            self.lines_cleared = 0
            self.difficulty = difficulty # Store the difficulty setting
            self.game_over = False
            self.bag = []
            self.next_pieces = []
            self.fill_bag()
            for _ in range(5): self.next_pieces.append(self.draw_from_bag())
            self.current_piece = None
            self.hold_piece_type = None
            self.can_hold = True
            self.spawn_new_piece()
            self.last_move_was_rotation = False
            self.last_clear_info = None
            self.lock_timer = 0
            self.is_landed = False
            self.time_since_fall = 0.0

        def fill_bag(self):
            self.bag = list(TETROMINOES.keys())
            random.shuffle(self.bag)

        def draw_from_bag(self):
            if not self.bag: self.fill_bag()
            return self.bag.pop(0)

        def spawn_new_piece(self):
            piece_type = self.next_pieces.pop(0)
            self.next_pieces.append(self.draw_from_bag())
            shape_info = TETROMINOES[piece_type]
            self.current_piece = {'type': piece_type, 'shape': shape_info['shape'], 'x': (BOARD_WIDTH - len(shape_info['shape'][0])) // 2, 'y': 0, 'rotation': 0}
            self.can_hold = True
            self.is_landed = False
            self.lock_timer = 0
            self.last_move_was_rotation = False # --- RESET THE FLAG ---
            if self.check_collision(self.current_piece['shape'], self.current_piece['x'], self.current_piece['y']):
                self.game_over = True
        
        def update(self, dt):
            if self.game_over:
                return

            # --- Gravity Calculation ---
            # Get the speed multiplier based on the game's difficulty setting
            speed_multiplier = AI_GRAVITY_MULTIPLIERS.get(self.difficulty, 1.0)

            # High-level 20G gravity remains the same for everyone
            if self.level >= 20:
                self.move(0, 1, reset_lock=False)
            else:
                self.time_since_fall += dt
                base_interval = max(0.05, 0.5 - ((self.level - 1) * 0.022))
                gravity_interval = base_interval / speed_multiplier
                if self.time_since_fall >= gravity_interval:
                    self.time_since_fall = 0
                    self.move(0, 1, reset_lock=False)

            if self.is_landed:
                self.lock_timer += dt
                if self.lock_timer >= LOCK_DELAY:
                    self.lock_piece()
            
            # --- STATE 2: The piece is actively falling. ---
            # If the piece is not landed, we only care about gravity.
            else:
                # Handle "20G" instant-fall gravity for high levels.
                if self.level >= 20:
                    self.current_piece['y'] = self.get_ghost_y()
                    self.is_landed = True # The piece has now landed, so the lock delay will start next frame.
                    self.time_since_fall = 0
                
                # Handle standard, progressive gravity for levels 1-19.
                else:
                    # Get the base speed multiplier for the current difficulty.
                    speed_multiplier = AI_GRAVITY_MULTIPLIERS.get(self.difficulty, 1.0)
                    
                    # Calculate the fall interval based on the current level.
                    base_interval = max(0.05, 0.5 - ((self.level - 1) * 0.022))
                    
                    # Apply the difficulty multiplier.
                    gravity_interval = base_interval / speed_multiplier

                    self.time_since_fall += dt
                    if self.time_since_fall >= gravity_interval:
                        self.time_since_fall = 0
                        # move() will set self.is_landed to True if it fails to move down.
                        self.move(0, 1, reset_lock=False)

        def check_collision(self, shape, x, y):
            for r, row in enumerate(shape):
                for c, cell in enumerate(row):
                    if cell != 0:
                        board_x, board_y = x + c, y + r
                        if not (0 <= board_x < BOARD_WIDTH and 0 <= board_y < BOARD_HEIGHT) or self.board[board_y][board_x] != 0:
                            return True
            return False

        def get_ghost_y(self):
            if not self.current_piece: return -1
            ghost_y = self.current_piece['y']
            while not self.check_collision(self.current_piece['shape'], self.current_piece['x'], ghost_y + 1):
                ghost_y += 1
            return ghost_y

        def lock_piece(self):
            """Locks the current piece, then checks for clears before spawning the next."""
            if not self.current_piece: return

            shape, x, y = self.current_piece['shape'], self.current_piece['x'], self.current_piece['y']
            color_id = TETROMINOES[self.current_piece['type']]['color_id']
            for r, row in enumerate(shape):
                for c, cell in enumerate(row):
                    if cell != 0: self.board[y + r][x + c] = color_id

            # --- MODIFICATION ---
            # Call clear_lines FIRST, while we still know about the piece that was just locked.
            self.clear_lines()
            self.spawn_new_piece()

        def _is_t_spin_full(self):
            """
            Checks for a full T-Spin using the 3-corner rule.
            A full T-Spin requires 3 of the 4 corners around the T piece to be occupied.
            """
            if not self.current_piece or self.current_piece['type'] != 'T':
                return False

            p = self.current_piece
            # The four corners relative to the T piece's 3x3 bounding box
            corners = [(p['y'], p['x']), (p['y'], p['x'] + 2), (p['y'] + 2, p['x']), (p['y'] + 2, p['x'] + 2)]
            occupied_corners = 0
            for r, c in corners:
                # Check if the corner is off-board or if the board cell is not empty
                if not (0 <= c < BOARD_WIDTH and 0 <= r < BOARD_HEIGHT) or self.board[r][c] != 0:
                    occupied_corners += 1
            
            return occupied_corners >= 3

        def clear_lines(self):
            """
            --- COMPLETE OVERHAUL ---
            Checks for and clears completed lines with full modern T-Spin scoring rules.
            This method will now set self.last_clear_info for the displayable to read.
            """
            self.last_clear_info = None # Reset before checking
            
            was_rotation = self.last_move_was_rotation
            is_t_piece = self.current_piece and self.current_piece['type'] == 'T'
            
            is_full_tspin = False
            is_mini_tspin = False

            # 1. Determine if the move was a T-Spin of any kind
            if was_rotation and is_t_piece:
                if self._is_t_spin_full():
                    is_full_tspin = True
                else:
                    is_mini_tspin = True

            # 2. Find completed lines
            lines_to_clear = [r for r, row in enumerate(self.board) if all(cell != 0 for cell in row)]
            num_cleared = len(lines_to_clear)
            
            # 3. Apply score and set clear info based on the type of clear
            score_to_add = 0
            clear_type = "NONE"

            if is_full_tspin:
                score_map = {0: 400, 1: 800, 2: 1200, 3: 1600} # T-Spin 0, Single, Double, Triple
                score_to_add = score_map.get(num_cleared, 0)
                clear_type = f"T_SPIN_FULL_{num_cleared}"

            elif is_mini_tspin:
                score_map = {0: 100, 1: 200, 2: 400} # Mini T-Spin 0, Single, Double
                score_to_add = score_map.get(num_cleared, 0)
                clear_type = f"T_SPIN_MINI_{num_cleared}"

            elif num_cleared > 0: # Standard clear (not a T-Spin)
                score_map = {1: 100, 2: 300, 3: 500, 4: 800} # Single, Double, Triple, Tetris
                score_to_add = score_map.get(num_cleared, 0)
                clear_type = f"NORMAL_{num_cleared}"
            
            if score_to_add > 0:
                self.score += score_to_add * self.level
                self.last_clear_info = {'type': clear_type, 'lines': num_cleared}

            # 4. Update board state if lines were cleared
            if num_cleared > 0:
                self.lines_cleared += num_cleared
                self.level = (self.lines_cleared // 10) + 1

                new_board = [row for r, row in enumerate(self.board) if r not in lines_to_clear]
                for _ in range(num_cleared):
                    new_board.insert(0, [0] * BOARD_WIDTH)
                self.board = new_board
        
        def move(self, dx, dy, reset_lock=True):
            if self.game_over: return False
            new_x, new_y = self.current_piece['x'] + dx, self.current_piece['y'] + dy
            if not self.check_collision(self.current_piece['shape'], new_x, new_y):
                self.current_piece['x'], self.current_piece['y'] = new_x, new_y
                if reset_lock: self.is_landed, self.lock_timer = False, 0
                self.last_move_was_rotation = False # --- RESET THE FLAG ---
                return True
            else:
                if dy > 0: self.is_landed = True
                return False

        def rotate(self, clockwise=True):
            if self.game_over or self.current_piece['type'] == 'O': return
            p = self.current_piece
            original_rotation = p['rotation']
            new_shape = list(zip(*p['shape'][::-1])) if clockwise else list(zip(*p['shape']))[::-1]
            new_rotation = (original_rotation + 1) % 4 if clockwise else (original_rotation - 1 + 4) % 4
            rotation_key = f"{original_rotation}-{new_rotation}"
            kick_table = I_KICKS if p['type'] == 'I' else JLSTZ_KICKS
            for dx, dy in kick_table.get(rotation_key, []):
                test_x, test_y = p['x'] + dx, p['y'] - dy
                if not self.check_collision(new_shape, test_x, test_y):
                    p['shape'], p['x'], p['y'], p['rotation'] = new_shape, test_x, test_y, new_rotation
                    self.is_landed, self.lock_timer = False, 0
                    self.last_move_was_rotation = True # --- SET THE FLAG ---
                    return

        def hard_drop(self):
            if self.game_over: return
            ghost_y = self.get_ghost_y()
            self.score += (ghost_y - self.current_piece['y'])
            self.current_piece['y'] = ghost_y
            self.last_move_was_rotation = False # --- RESET THE FLAG ---
            self.lock_piece()

        def hold(self):
            if not self.can_hold or self.game_over: return

            # Reset the landed state and lock timer IMMEDIATELY.
            # This cancels any pending lock from the previous piece.
            self.is_landed = False
            self.lock_timer = 0
            
            self.last_move_was_rotation = False
            self.can_hold = False # A hold action can only be done once per piece.

            if self.hold_piece_type is None:
                # If hold is empty, the current piece goes into hold, and a new piece spawns.
                self.hold_piece_type = self.current_piece['type']
                self.spawn_new_piece()
            else:
                # If hold is full, swap the current piece with the held piece.
                held_type, self.hold_piece_type = self.hold_piece_type, self.current_piece['type']
                shape_info = TETROMINOES[held_type]
                self.current_piece = {'type': held_type, 'shape': shape_info['shape'], 'x': (BOARD_WIDTH - len(shape_info['shape'][0])) // 2, 'y': 0, 'rotation': 0}

    #-----------------------------------------
    # ARTIFICIAL INTELLIGENCE CLASS
    #-----------------------------------------
    class TetrisAI:
        # Heuristic weights for scoring a board state.
        WEIGHTS = {
            'height': -0.51,
            'lines': 0.76,
            'holes': -0.35,
            'bumpiness': -0.18,
            't_spin_bonus': 2.0 # A massive bonus to incentivize the move.
        }

        def find_best_move(self, game):
            """
            Analyzes the board and current piece to find the optimal placement.
            Returns a dictionary with the target x, rotation, and resulting score.
            """
            best_move = {'score': -float('inf'), 'x': -1, 'rotation': 0}
            temp_piece = copy.deepcopy(game.current_piece)
            
            for rotation in range(4): # 4 possible rotations
                # Find all possible x positions for this rotation
                min_x = -min(c for r in temp_piece['shape'] for c, cell in enumerate(r) if cell)
                max_x = BOARD_WIDTH - max(c + 1 for r in temp_piece['shape'] for c, cell in enumerate(r) if cell)

                for x in range(min_x, max_x + 1):
                    sim_board = copy.deepcopy(game.board)
                    
                    # Find landing position (hard drop)
                    y = temp_piece['y']
                    while not self._check_collision_sim(sim_board, temp_piece['shape'], x, y + 1):
                        y += 1
                    
                    # Store the final landing position for the T-Spin check.
                    final_x, final_y = x, y
                    self._place_piece_sim(sim_board, temp_piece['shape'], final_x, final_y, TETROMINOES[temp_piece['type']]['color_id'])
                    
                    # Call the evaluation function with all necessary parameters.
                    score = self._evaluate_board(sim_board, temp_piece['type'], final_x, final_y)

                    if score > best_move['score']:
                        best_move = {'score': score, 'x': x, 'rotation': rotation}

                # Rotate the temporary piece for the next loop
                if temp_piece['type'] != 'O':
                    temp_piece['shape'] = list(zip(*temp_piece['shape'][::-1]))
            return best_move

        def _evaluate_board(self, board, piece_type, piece_x, piece_y):
            """
            Calculates the score of a given board state.
            This definition now correctly accepts all 5 arguments.
            """
            heights = [0] * BOARD_WIDTH
            for c in range(BOARD_WIDTH):
                for r in range(BOARD_HEIGHT):
                    if board[r][c] != 0:
                        heights[c] = BOARD_HEIGHT - r
                        break

            agg_height = sum(heights)
            completed_lines = sum(1 for row in board if all(cell != 0 for cell in row))
            holes = sum(1 for c in range(BOARD_WIDTH) for r in range(BOARD_HEIGHT - heights[c], BOARD_HEIGHT) if board[r][c] == 0)
            bumpiness = sum(abs(heights[i] - heights[i+1]) for i in range(len(heights) - 1))

            t_spin_bonus = 0
            if piece_type == 'T' and completed_lines > 0:
                if self._check_t_spin_sim(board, piece_x, piece_y):
                    t_spin_bonus = self.WEIGHTS['t_spin_bonus']

            score = (self.WEIGHTS['height'] * agg_height +
                     self.WEIGHTS['lines'] * completed_lines +
                     self.WEIGHTS['holes'] * holes +
                     self.WEIGHTS['bumpiness'] * bumpiness +
                     t_spin_bonus)
            return score

        def _check_t_spin_sim(self, board, piece_x, piece_y):
            """
            Checks if a T-piece placement qualifies as a T-Spin using the 3-corner rule.
            """
            corners = [(piece_y, piece_x), (piece_y, piece_x + 2), (piece_y + 2, piece_x), (piece_y + 2, piece_x + 2)]
            occupied_corners = 0
            for r, c in corners:
                if not (0 <= c < BOARD_WIDTH and 0 <= r < BOARD_HEIGHT) or board[r][c] != 0:
                    occupied_corners += 1
            return occupied_corners >= 3

        def _check_collision_sim(self, board, shape, x, y):
            for r, row in enumerate(shape):
                for c, cell in enumerate(row):
                    if cell != 0:
                        board_x, board_y = x + c, y + r
                        if not (0 <= board_x < BOARD_WIDTH and 0 <= board_y < BOARD_HEIGHT) or board[board_y][board_x] != 0:
                            return True
            return False

        def _place_piece_sim(self, board, shape, x, y, value_to_place):
            """
            Places a piece on a simulated board using a given value.
            """
            for r, row in enumerate(shape):
                for c, cell in enumerate(row):
                    if cell != 0:
                        board[y + r][x + c] = value_to_place

    #-----------------------------------------
    # REN'PY DISPLAYABLE CLASS (Completed)
    #-----------------------------------------
    class TetrisDisplayable(renpy.Displayable):
        def __init__(self, is_ai=False, ai_difficulty=0, opponent_game=None, **kwargs):
            super(TetrisDisplayable, self).__init__(**kwargs)
            self.game = TetrisGame(difficulty=ai_difficulty)
            self.is_ai = is_ai
            self.ai_difficulty = ai_difficulty
            self.opponent_game = opponent_game
            self.yuri_face_state = 0
            self.music_swapped = False
            self.VALID_SOUND_KEYS = { pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_z }

            if self.is_ai:
                self.ai = TetrisAI()
                self.ai_target_move = None
                self.ai_move_timer = 0.0
                self.ai_delay_range = AI_ACTION_DELAY.get(self.ai_difficulty, (0.1, 0.05))

            else:
                self.held_key = None      # Which key is being held ('left', 'right')
                self.das_timer = 0.0      # Timer for the DAS delay
                self.arr_timer = 0.0      # Timer for the ARR speed
            
            self.load_assets()
            self.last_update_time = 0
            self.yuri_face_state = 0
            self.put_shadow = not is_ai or ai_difficulty < 4

            # --- NEW DAS/ARR STATE VARIABLES ---
            if not self.is_ai:
                self.das_key = None      # The key currently being evaluated for DAS ('left' or 'right')
                self.das_timer = 0.0     # The timer for the initial DAS delay
                self.arr_timer = 0.0     # The timer for the faster Auto-Repeat Rate

        def set_opponent(self, opponent_game):
            """A method to link the opponent after both objects are created."""
            self.opponent_game = opponent_game

        def load_assets(self):
            skin_id = getattr(persistent, 'skin', 1)
            skin = SKINS.get(skin_id, SKINS[1])
            path, sfx = skin['path'], skin['sfx_suffix']
            self.background_img = Image(path + "background.png")
            self.colors = {i: Image(path + f"cube_{i}.png") for i in range(1, 8)}
            self.colors[9] = Image(path + "cube_8.png")
            self.shadow_colors = {i: Image(path + (f"shadow_{i}.png" if skin_id in [5, 6] else f"cube_{i}.png")) for i in range(1, 8)}
            self.sounds = {
                'drop': f"sfx/t-drop{sfx}",
                'move': f"sfx/t-move{sfx}",
                'rotate': f"sfx/t-rotate{sfx}",
                '1line': f"sfx/t-fl{sfx}",
                '2line': f"sfx/t-2fl{sfx}",
                '3line': f"sfx/t-3fl{sfx}",
                '4line': f"sfx/t-4fl{sfx}",
                'tspin': f"sfx/t-spin{sfx}",
            }

        def render(self, width, height, st, at):
            if self.last_update_time == 0: self.last_update_time = st
            dtime = st - self.last_update_time
            self.last_update_time = st

            if not self.is_ai and self.held_key is not None:
                self.das_timer += dtime
                # If the initial DAS delay is over...
                if self.das_timer > DAS_DELAY:
                    self.arr_timer += dtime
                    # ...start moving at the faster ARR speed.
                    if self.arr_timer > ARR_DELAY:
                        # This -= trick handles cases where the frame rate is low
                        self.arr_timer -= ARR_DELAY
                        self.game.move(-1 if self.held_key == 'left' else 1, 0)
                        renpy.sound.play(self.sounds['move'])

            # The rest of the render method is unchanged
            if not self.game.game_over:
                self.game.update(dtime)
                if self.is_ai: self.ai_update(dtime)
                self.check_win_conditions()

            # --- NEW SOUND LOGIC ---
            # Check the info flag that TetrisGame sets for us.
            if self.game.last_clear_info:
                info = self.game.last_clear_info
                clear_type = info['type']
                
                # Play sound based on the type of clear
                if "T_SPIN_FULL" in clear_type:
                    renpy.sound.play(self.sounds['tspin'])
                elif "T_SPIN_MINI" in clear_type:
                    renpy.sound.play(self.sounds['tspin'])
                elif "NORMAL_4" in clear_type:
                    renpy.sound.play(self.sounds['4line'])
                elif "NORMAL_3" in clear_type:
                    renpy.sound.play(self.sounds['3line'])
                elif "NORMAL_2" in clear_type:
                    renpy.sound.play(self.sounds['2line'])
                elif "NORMAL_1" in clear_type:
                    renpy.sound.play(self.sounds['1line'])
                
                # IMPORTANT: Reset the flag so the sound doesn't play on every frame.
                self.game.last_clear_info = None

            r = renpy.Render(width, height)
            r.blit(renpy.render(self.background_img, width, height, st, at), (0, 0))
            
            playfield_width = BOARD_WIDTH * PIXEL_SIZE
            playfield_x_offset = 10
            playfield_y_offset = 10

            self.draw_board(r, playfield_x_offset, playfield_y_offset, st, at)
            if self.put_shadow:
                self.draw_ghost_piece(r, playfield_x_offset, playfield_y_offset, st, at)
            self.draw_current_piece(r, playfield_x_offset, playfield_y_offset, st, at)
            
            # --- THE FIX ---
            # Call draw_ui with the correct 6 arguments.
            self.draw_ui(r, playfield_x_offset, playfield_y_offset, st, at)
            # --- END THE FIX ---
            
            self.check_dynamic_events()
            renpy.redraw(self, 0.016)
            return r

        def draw_board(self, r, x_off, y_off, st, at):
            """
            Draws the walls and the locked pieces directly onto the main render object 'r'.
            """
            # --- Draw the Walls ---
            wall_texture = self.colors.get(9)
            if wall_texture:
                wall_render = renpy.render(wall_texture, PIXEL_SIZE, PIXEL_SIZE, st, at)
                # Left and Right Walls
                for y in range(VISIBLE_BOARD_HEIGHT):
                    r.blit(wall_render, (x_off - PIXEL_SIZE, y_off + y * PIXEL_SIZE)) # Left
                    r.blit(wall_render, (x_off + BOARD_WIDTH * PIXEL_SIZE, y_off + y * PIXEL_SIZE)) # Right
                # Bottom Wall
                for x in range(-1, BOARD_WIDTH + 1):
                    r.blit(wall_render, (x_off + x * PIXEL_SIZE, y_off + VISIBLE_BOARD_HEIGHT * PIXEL_SIZE))

            # --- Draw the Locked Pieces (existing logic) ---
            board_offset = BOARD_HEIGHT - VISIBLE_BOARD_HEIGHT
            for y in range(VISIBLE_BOARD_HEIGHT):
                for x in range(BOARD_WIDTH):
                    cell = self.game.board[y + board_offset][x]
                    if cell != 0 and self.colors.get(cell):
                        render_obj = renpy.render(self.colors[cell], PIXEL_SIZE, PIXEL_SIZE, st, at)
                        screen_x = x_off + (x * PIXEL_SIZE)
                        screen_y = y_off + (y * PIXEL_SIZE)
                        r.blit(render_obj, (screen_x, screen_y))

        def draw_piece(self, r, x_off, y_off, piece, is_ghost, st, at):
            """Generic function to draw a piece directly onto the main render object 'r'."""
            color_id = TETROMINOES[piece['type']]['color_id']
            img_dict = self.shadow_colors if is_ghost else self.colors
            base_img = img_dict.get(color_id)
            if not base_img:
                return

            if is_ghost:
                displayable_to_render = im.Alpha(base_img, 0.4)
            else:
                displayable_to_render = base_img

            piece_y_offset = piece['y'] - (BOARD_HEIGHT - VISIBLE_BOARD_HEIGHT)

            for row_idx, row in enumerate(piece['shape']):
                for col_idx, cell in enumerate(row):
                    if cell != 0:
                        # Calculate the final screen position for this block of the piece.
                        screen_x = x_off + ((piece['x'] + col_idx) * PIXEL_SIZE)
                        screen_y = y_off + ((piece_y_offset + row_idx) * PIXEL_SIZE)
                        
                        # Only draw if it's within the visible part of the board area.
                        if screen_y >= y_off:
                            render_obj = renpy.render(displayable_to_render, PIXEL_SIZE, PIXEL_SIZE, st, at)
                            r.blit(render_obj, (screen_x, screen_y))
        
        # These are helper functions that call the main 'draw_piece' method.
        def draw_current_piece(self, r, x_off, y_off, st, at):
            if self.game.current_piece and not self.game.game_over:
                self.draw_piece(r, x_off, y_off, self.game.current_piece, False, st, at)

        def draw_ghost_piece(self, r, x_off, y_off, st, at):
            if self.game.current_piece and not self.game.game_over:
                ghost_piece = copy.deepcopy(self.game.current_piece)
                ghost_piece['y'] = self.game.get_ghost_y()
                self.draw_piece(r, x_off, y_off, ghost_piece, True, st, at)
        
        def draw_ui(self, r, x_off, y_off, st, at):
            """
            Draws the UI elements. This definition now correctly takes 6 arguments.
            """
            is_player = not self.is_ai
            text_size = 22
            width, height = r.width, r.height

            playfield_width = BOARD_WIDTH * PIXEL_SIZE
            
            # Layout for the Player's screen (left instance)
            player_layout = {
                "text_anchor_x": x_off - 140, # Position text to the left of the playfield
                "queue_anchor_x": x_off + playfield_width + 20, # Position queues to the right
            }

            # Layout for the AI's screen (right instance)
            ai_layout = {
                "text_anchor_x": x_off - 140,
                "queue_anchor_x": x_off + playfield_width + 20,
            }
            
            layout = player_layout if is_player else ai_layout
            text_x = layout["text_anchor_x"]
            queue_x = layout["queue_anchor_x"]
            
            r.blit(renpy.render(Text(f"Score: {self.game.score}", size=text_size), width, height, st, at), (text_x, y_off))
            r.blit(renpy.render(Text(f"Level: {self.game.level}", size=text_size), width, height, st, at), (text_x, y_off + 30))
            r.blit(renpy.render(Text(f"Lines: {self.game.lines_cleared}", size=text_size), width, height, st, at), (text_x + 130, y_off + 30))
            
            r.blit(renpy.render(Text("Next:", size=text_size), width, height, st, at), (queue_x, y_off + 90))
            for i, p_type in enumerate(self.game.next_pieces[:5]):
                 self.draw_ui_piece(r, p_type, (queue_x, y_off + 120 + i * 60), st, at)

            if is_player:
                r.blit(renpy.render(Text("Hold:", size=text_size), width, height, st, at), (text_x, y_off + 90))
                if self.game.hold_piece_type:
                    self.draw_ui_piece(r, self.game.hold_piece_type, (text_x, y_off + 120), st, at)
                
                win_text = None
                if LineLimit != 0:
                    win_text = f"Lines to Win: {max(0, LineLimit - self.game.lines_cleared)}"
                elif TetrisScore != 0:
                    win_text = f"Score Goal: {TetrisScore}"
                
                if win_text:
                    r.blit(renpy.render(Text(win_text, size=text_size), width, height, st, at), (text_x, y_off + 60))

        def draw_ui_piece(self, r, piece_type, pos, st, at):
            """Draws a piece in the UI (Next/Hold) with centering for large pieces like 'I'."""
            info = TETROMINOES[piece_type]
            img = self.colors.get(info['color_id'])
            if not img: return

            # Center the piece horizontally within a 4-block wide area.
            piece_width = len(info['shape'][0]) * PIXEL_SIZE
            x_offset = ( (4 * PIXEL_SIZE) - piece_width ) / 2

            for y, row in enumerate(info['shape']):
                for x, cell in enumerate(row):
                    if cell != 0:
                        r.blit(renpy.render(img, PIXEL_SIZE, PIXEL_SIZE, st, at), (pos[0] + x_offset + x*PIXEL_SIZE, pos[1] + y*PIXEL_SIZE))

        def ai_update(self, dtime):
            if self.game.current_piece and not self.ai_target_move:
                self.ai_target_move = self.ai.find_best_move(self.game)
            
            if self.ai_target_move:
                # --- NEW: Special "Singularity" AI Behavior ---
                if self.ai_difficulty == 7:
                    p = self.game.current_piece
                    target_rot = self.ai_target_move['rotation']
                    target_x = self.ai_target_move['x']
                    
                    # 1. Rotate the piece in memory until it matches the target rotation.
                    while p['rotation'] != target_rot:
                        p['shape'] = list(zip(*p['shape'][::-1])) # Perform one clockwise rotation
                        p['rotation'] = (p['rotation'] + 1) % 4
                    
                    # 2. Instantly set the piece's horizontal position.
                    p['x'] = target_x
                    
                    # 3. Hard drop it. This all happens in a single frame.
                    self.game.hard_drop()
                    renpy.sound.play(self.sounds['drop'])
                    self.ai_target_move = None
                    
                # --- This is the existing logic for all other difficulties ---
                else:
                    progress = min(1.0, (self.game.level - 1) / (AI_PERFECTION_LEVEL - 1))
                    start_delay, end_delay = self.ai_delay_range
                    current_action_delay = start_delay + (end_delay - start_delay) * progress
                    
                    self.ai_move_timer += dtime
                    if self.ai_move_timer >= current_action_delay:
                        self.ai_move_timer = 0
                        p = self.game.current_piece
                        target_rot = self.ai_target_move['rotation']
                        target_x = self.ai_target_move['x']

                        if p['rotation'] != target_rot:
                            self.game.rotate()
                        elif p['x'] < target_x:
                            self.game.move(1, 0)
                        elif p['x'] > target_x:
                            self.game.move(-1, 0)
                        else:
                            self.game.hard_drop()
                            renpy.sound.play(self.sounds['drop'])
                            self.ai_target_move = None
        
        def check_win_conditions(self):
            global TetrisWinner # Use global to signal winner to Ren'Py script
            if self.opponent_game is None: return
            
            # Condition: This instance has topped out.
            if self.game.game_over and not self.opponent_game.game_over:
                # If this instance is the player, the player LOST. AI is the winner.
                if not self.is_ai:
                    TetrisWinner = 1 # AI Wins
                # If this instance is the AI, the AI LOST. Player is the winner.
                else:
                    TetrisWinner = 0 # Player Wins
                # Also end the opponent's game to freeze their screen too.
                self.opponent_game.game_over = True
                return

            # Condition: The opponent has topped out.
            if self.opponent_game.game_over and not self.game.game_over:
                # If this instance is the player, the opponent (AI) LOST. Player is the winner.
                if not self.is_ai:
                    TetrisWinner = 0 # Player Wins
                # If this instance is the AI, the opponent (player) LOST. AI is the winner.
                else:
                    TetrisWinner = 1 # AI Wins
                # End this instance's game to freeze the screen.
                self.game.game_over = True
                return
            # --- END OF FIX 2 ---

            # Score/Line limit conditions remain the same.
            if LineLimit != 0 and self.game.lines_cleared >= LineLimit:
                TetrisWinner = 0 if not self.is_ai else 1
                self.game.game_over = True
            elif TetrisScore != 0 and self.game.score >= TetrisScore:
                TetrisWinner = 0 if not self.is_ai else 1
                self.game.game_over = True

        def check_dynamic_events(self):
            # This logic only applies to the AI instance with skin 1
            if not self.is_ai or self.opponent_game is None or getattr(persistent, 'skin', 1) != 1:
                return

            # Determine if the intensity threshold has been passed
            threshold_passed = False
            if LineLimit > 0 and (self.game.lines_cleared > LineLimit/6 or self.opponent_game.lines_cleared > LineLimit/6):
                threshold_passed = True
            elif TetrisScore > 0 and (self.game.score > TetrisScore/6 or self.opponent_game.score > TetrisScore/6):
                threshold_passed = True

            if threshold_passed:
                # --- MUSIC SWAP LOGIC ---
                # This block now has two conditions:
                # 1. Has the threshold been passed?
                # 2. Have we NOT swapped the music yet?
                if not self.music_swapped:
                    # If both are true, play the music...
                    renpy.music.stop(channel="music")
                    renpy.music.play("<loop 1.81>/music/tetris (b).ogg", channel="music")
                    # ...and immediately set the flag to True. This ensures this
                    # block will never, ever run again for this instance.
                    self.music_swapped = True

                # --- EXPRESSION CHANGE LOGIC (Now safely decoupled from the music) ---
                # This logic can run as many times as needed without affecting the BGM.
                if self.game.score > self.opponent_game.score and self.yuri_face_state != 1:
                    self.yuri_face_state = 1
                    renpy.show("A-ABDAA-AAAJ", tag="yuri_face")
                elif self.game.score < self.opponent_game.score and self.yuri_face_state != 2:
                    self.yuri_face_state = 2
                    renpy.show("A-DEBAA-AMAM", tag="yuri_face")

        def event(self, ev, x, y, st):
            # The AI completely ignores all events.
            if self.is_ai:
                return

            # --- PLAYER EVENT HANDLING ---
            # On game over, only a key press to exit is allowed. No sounds.
            if self.game.game_over:
                if ev.type == pygame.KEYDOWN:
                    renpy.jump("tetris_over")
                return

            # --- SIMPLIFIED KEYDOWN LOGIC ---
            if ev.type == pygame.KEYDOWN:
                # Handle horizontal movement start
                if ev.key == pygame.K_LEFT:
                    # Check if this is a fresh press, not an OS-level repeat
                    if self.held_key != 'left':
                        self.game.move(-1, 0) # Initial move
                        renpy.sound.play(self.sounds['move'])
                        self.held_key = 'left'
                        self.das_timer = 0.0 # Reset timers for the new hold
                        self.arr_timer = 0.0
                elif ev.key == pygame.K_RIGHT:
                    if self.held_key != 'right':
                        self.game.move(1, 0) # Initial move
                        renpy.sound.play(self.sounds['move'])
                        self.held_key = 'right'
                        self.das_timer = 0.0 # Reset timers for the new hold
                        self.arr_timer = 0.0

                # --- Other keys are unchanged ---
                elif ev.key == pygame.K_UP:
                    renpy.sound.play(self.sounds['rotate'])
                    self.game.rotate(clockwise=True)
                elif ev.key == pygame.K_z:
                    renpy.sound.play(self.sounds['rotate'])
                    self.game.rotate(clockwise=False)
                elif ev.key == pygame.K_SPACE:
                    self.game.hard_drop()
                    renpy.sound.play(self.sounds['drop'])
                elif ev.key in [pygame.K_c, pygame.K_q, pygame.K_e]:
                    self.game.hold()
                elif ev.key == pygame.K_DOWN:
                    self.game.time_since_fall = 1.0

            elif ev.type == pygame.KEYUP:
                # If the player releases the key they were holding, clear the state.
                if (ev.key == pygame.K_LEFT and self.held_key == 'left') or \
                   (ev.key == pygame.K_RIGHT and self.held_key == 'right'):
                    self.held_key = None

    #-----------------------------------------
    # MODERN CO-OP GAME LOGIC CLASS
    #-----------------------------------------
    class CoOpTetrisGame:
        """
        Manages the game state for a double-wide, shared-board co-op game.
        It controls two pieces simultaneously on one large playfield.
        """
        CO_OP_BOARD_WIDTH = 20 # Double the standard width
        
        def __init__(self):
            self.board = [[0] * self.CO_OP_BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
            self.score = 0
            self.level = 1
            self.lines_cleared = 0
            self.game_over = False

            # --- Player State ---
            self.player_bag = []
            self.player_next = []
            self.player_piece = None
            self.player_hold = None
            self.player_can_hold = True
            self.player_is_landed = False
            self.player_lock_timer = 0
            self.player_time_since_fall = 0.0
            
            # --- AI State ---
            self.ai_bag = []
            self.ai_next = []
            self.ai_piece = None
            self.ai_hold = None
            self.ai_can_hold = True
            self.ai_is_landed = False
            self.ai_lock_timer = 0
            self.ai_time_since_fall = 0.0
            
            # Initialize both players' piece supplies
            self.fill_bag(is_player=True)
            self.fill_bag(is_player=False)
            for _ in range(5):
                self.player_next.append(self.draw_from_bag(True))
                self.ai_next.append(self.draw_from_bag(False))

            self.spawn_new_piece(is_player=True)
            self.spawn_new_piece(is_player=False)

            self.last_clear_info = None

        def fill_bag(self, is_player):
            bag = list(TETROMINOES.keys())
            random.shuffle(bag)
            if is_player: self.player_bag = bag
            else: self.ai_bag = bag

        def draw_from_bag(self, is_player):
            if is_player:
                if not self.player_bag: self.fill_bag(True)
                return self.player_bag.pop(0)
            else:
                if not self.ai_bag: self.fill_bag(False)
                return self.ai_bag.pop(0)

        def spawn_new_piece(self, is_player):
            piece_type = self.draw_from_bag(is_player)
            shape_info = TETROMINOES[piece_type]

            # Player spawns on the left, AI on the right
            start_x = 3 if is_player else 13
            new_piece = {'type': piece_type, 'shape': shape_info['shape'], 'x': start_x, 'y': 0, 'rotation': 0}

            if self.check_collision(new_piece['shape'], new_piece['x'], new_piece['y']):
                self.game_over = True
            
            if is_player:
                self.player_piece = new_piece
                self.player_can_hold = True
                self.player_is_landed = False
                self.player_lock_timer = 0
                self.player_next.append(self.draw_from_bag(True))
            else:
                self.ai_piece = new_piece
                self.ai_can_hold = True
                self.ai_is_landed = False
                self.ai_lock_timer = 0
                self.ai_next.append(self.draw_from_bag(False))

        def update(self, dt):
            if self.game_over: return

            # --- THE FIX: Added a fall interval to control speed ---
            # You can change 0.6 to any number. Higher = Slower.
            fall_interval = max(0.05, 0.3 - ((self.level - 1) * 0.025))
            # --- END THE FIX ---

            # --- Handle Player Gravity and Lock ---
            if self.player_piece:
                if self.player_is_landed:
                    self.player_lock_timer += dt
                    if self.player_lock_timer >= LOCK_DELAY:
                        self.lock_piece(True)
                else:
                    # Timer-based gravity for the player
                    self.player_time_since_fall += dt
                    if self.player_time_since_fall >= fall_interval:
                        self.player_time_since_fall = 0
                        self.move(0, 1, is_player=True, reset_lock=False)

            # --- Handle AI Gravity and Lock ---
            if self.ai_piece:
                if self.ai_is_landed:
                    self.ai_lock_timer += dt
                    if self.ai_lock_timer >= LOCK_DELAY:
                        self.lock_piece(False)
                else:
                    # Timer-based gravity for the AI
                    self.ai_time_since_fall += dt
                    if self.ai_time_since_fall >= fall_interval:
                        self.ai_time_since_fall = 0
                        self.move(0, 1, is_player=False, reset_lock=False)

        def check_collision(self, shape, x, y):
            for r, row in enumerate(shape):
                for c, cell in enumerate(row):
                    if cell != 0:
                        board_x, board_y = x + c, y + r
                        if not (0 <= board_x < self.CO_OP_BOARD_WIDTH and 0 <= board_y < BOARD_HEIGHT) or self.board[board_y][board_x] != 0:
                            return True
            return False

        def lock_piece(self, is_player):
            piece_to_lock = self.player_piece if is_player else self.ai_piece
            if not piece_to_lock: return

            shape, x, y = piece_to_lock['shape'], piece_to_lock['x'], piece_to_lock['y']
            color_id = TETROMINOES[piece_to_lock['type']]['color_id']

            for r, row in enumerate(shape):
                for c, cell in enumerate(row):
                    if cell != 0: self.board[y + r][x + c] = color_id
            
            self.clear_lines()
            self.spawn_new_piece(is_player)

        def clear_lines(self):
            lines_to_clear = [r for r, row in enumerate(self.board) if all(cell != 0 for cell in row)]
            num_cleared = len(lines_to_clear)

            if num_cleared > 0:
                self.lines_cleared += num_cleared
                score_map = {1: 100, 2: 300, 3: 500, 4: 800} # Standard scoring
                self.score += score_map.get(num_cleared, 0) * self.level
                self.level = (self.lines_cleared // 10) + 1
                self.last_clear_info = {'lines': num_cleared}

                new_board = [row for r, row in enumerate(self.board) if r not in lines_to_clear]
                for _ in range(num_cleared):
                    new_board.insert(0, [0] * self.CO_OP_BOARD_WIDTH)
                self.board = new_board
        
        def move(self, dx, dy, is_player, reset_lock=True):
            piece = self.player_piece if is_player else self.ai_piece
            if self.game_over or not piece: return False
            
            new_x, new_y = piece['x'] + dx, piece['y'] + dy
            if not self.check_collision(piece['shape'], new_x, new_y):
                piece['x'], piece['y'] = new_x, new_y
                if reset_lock:
                    if is_player: self.player_is_landed, self.player_lock_timer = False, 0
                    else: self.ai_is_landed, self.ai_lock_timer = False, 0
                return True
            else:
                if dy > 0:
                    if is_player: self.player_is_landed = True
                    else: self.ai_is_landed = True
                return False

        def rotate(self, is_player, clockwise=True):
            piece = self.player_piece if is_player else self.ai_piece
            if self.game_over or not piece or piece['type'] == 'O': return
            
            original_rotation = piece['rotation']
            new_shape = list(zip(*piece['shape'][::-1])) if clockwise else list(zip(*piece['shape']))[::-1]
            new_rotation = (original_rotation + 1) % 4 if clockwise else (original_rotation - 1 + 4) % 4
            rotation_key = f"{original_rotation}-{new_rotation}"
            kick_table = I_KICKS if piece['type'] == 'I' else JLSTZ_KICKS
            
            for dx, dy in kick_table.get(rotation_key, []):
                test_x, test_y = piece['x'] + dx, piece['y'] - dy
                if not self.check_collision(new_shape, test_x, test_y):
                    piece['shape'], piece['x'], piece['y'], piece['rotation'] = new_shape, test_x, test_y, new_rotation
                    if is_player: self.player_is_landed, self.player_lock_timer = False, 0
                    else: self.ai_is_landed, self.ai_lock_timer = False, 0
                    return

        def get_ghost_y(self, is_player):
            piece = self.player_piece if is_player else self.ai_piece
            if not piece: return -1
            ghost_y = piece['y']
            while not self.check_collision(piece['shape'], piece['x'], ghost_y + 1):
                ghost_y += 1
            return ghost_y

        def hard_drop(self, is_player):
            piece = self.player_piece if is_player else self.ai_piece
            if self.game_over or not piece: return
            ghost_y = self.get_ghost_y(is_player)
            self.score += (ghost_y - piece['y']) # Shared score bonus
            piece['y'] = ghost_y
            self.lock_piece(is_player)

        def hold(self, is_player):
            if self.game_over: return
            if is_player:
                if not self.player_can_hold: return
                held_type, self.player_hold = self.player_hold, self.player_piece['type']
                self.player_can_hold = False
                if held_type is None: self.spawn_new_piece(True)
                else:
                    shape_info = TETROMINOES[held_type]
                    self.player_piece = {'type': held_type, 'shape': shape_info['shape'], 'x': 3, 'y': 0, 'rotation': 0}
            else: # AI hold
                if not self.ai_can_hold: return
                held_type, self.ai_hold = self.ai_hold, self.ai_piece['type']
                self.ai_can_hold = False
                if held_type is None: self.spawn_new_piece(False)
                else:
                    shape_info = TETROMINOES[held_type]
                    self.ai_piece = {'type': held_type, 'shape': shape_info['shape'], 'x': 13, 'y': 0, 'rotation': 0}

    #-----------------------------------------
    # MODERN CO-OP DISPLAYABLE CLASS
    #-----------------------------------------
    class CoOpTetrisDisplayable(renpy.Displayable):
        def __init__(self, **kwargs):
            super(CoOpTetrisDisplayable, self).__init__(**kwargs)
            self.game = CoOpTetrisGame()
            self.ai = TetrisAI()
            self.ai_target_move = None
            self.ai_move_timer = 0.0
            self.ai_delay_range = AI_ACTION_DELAY.get(3) # Let's fix AI difficulty to Hard (3) for co-op

            # Player DAS/ARR control state
            self.held_key = None
            self.das_timer = 0.0
            self.arr_timer = 0.0

            self.load_assets()
            self.last_update_time = 0

        def load_assets(self):
            # This is the streamlined asset loader from the versus mode
            skin_id = getattr(persistent, 'skin', 1)
            skin = SKINS.get(skin_id, SKINS[1])
            path, sfx = skin['path'], skin['sfx_suffix']
            self.background_img = Image(path + "background_co_op.png") # Use co-op background
            self.colors = {i: Image(path + f"cube_{i}.png") for i in range(1, 8)}
            self.shadow_colors = {i: Image(path + (f"shadow_{i}.png" if skin_id in [5, 6] else f"cube_{i}.png")) for i in range(1, 8)}
            self.sounds = {'drop': f"sfx/t-drop{sfx}", 'move': f"sfx/t-move{sfx}", 'rotate': f"sfx/t-rotate{sfx}", '1line': f"sfx/t-fl{sfx}", '4line': f"sfx/t-4fl{sfx}"}

        def render(self, width, height, st, at):
            global TetrisWinner # Use global to signal winner to Ren'Py script

            if self.last_update_time == 0: self.last_update_time = st
            dtime = st - self.last_update_time
            self.last_update_time = st

            # Handle player input for auto-repeat
            if self.held_key is not None:
                self.das_timer += dtime
                if self.das_timer > DAS_DELAY:
                    self.arr_timer += dtime
                    if self.arr_timer > ARR_DELAY:
                        self.arr_timer -= ARR_DELAY
                        self.game.move(-1 if self.held_key == 'left' else 1, 0, is_player=True)
                        renpy.sound.play(self.sounds['move'])
            
            # Update game state
            if not self.game.game_over:
                self.game.update(dtime)
                self.ai_update(dtime)
            else: # Handle game over condition
                if persistent.best_co_op_tetris_score < self.game.score:
                    persistent.best_co_op_tetris_score = self.game.score
                    TetrisWinner = 2 # New high score
                else:
                    TetrisWinner = 3 # No new high score
                renpy.jump("tetris_over")

            # Play sounds for line clears
            if self.game.last_clear_info:
                info = self.game.last_clear_info
                if info['lines'] >= 4: renpy.sound.play(self.sounds['4line'])
                else: renpy.sound.play(self.sounds['1line'])
                self.game.last_clear_info = None

            # --- Drawing ---
            r = renpy.Render(width, height)
            r.blit(renpy.render(self.background_img, width, height, st, at), (0, 0))
            
            playfield_x_offset = 0
            playfield_y_offset = 0

            self.draw_board(r, playfield_x_offset, playfield_y_offset, st, at)
            # Draw ghosts first
            self.draw_ghost_piece(r, playfield_x_offset, playfield_y_offset, is_player=True, st=st, at=at)
            self.draw_ghost_piece(r, playfield_x_offset, playfield_y_offset, is_player=False, st=st, at=at)
            # Draw solid pieces on top
            self.draw_piece(r, self.game.player_piece, playfield_x_offset, playfield_y_offset, st, at)
            self.draw_piece(r, self.game.ai_piece, playfield_x_offset, playfield_y_offset, st, at)
            self.draw_ui(r, width, height, st, at)

            renpy.redraw(self, 0)
            return r

        def draw_board(self, r, x_off, y_off, st, at):
            board_offset = BOARD_HEIGHT - VISIBLE_BOARD_HEIGHT
            for y in range(VISIBLE_BOARD_HEIGHT):
                for x in range(self.game.CO_OP_BOARD_WIDTH):
                    cell = self.game.board[y + board_offset][x]
                    if cell != 0 and self.colors.get(cell):
                        render_obj = renpy.render(self.colors[cell], PIXEL_SIZE, PIXEL_SIZE, st, at)
                        r.blit(render_obj, (x_off + x * PIXEL_SIZE, y_off + y * PIXEL_SIZE))

        def draw_piece(self, r, piece, x_off, y_off, st, at, is_ghost=False):
            if not piece: return
            color_id = TETROMINOES[piece['type']]['color_id']
            img_dict = self.shadow_colors if is_ghost else self.colors
            img = img_dict.get(color_id)
            if not img: return
            
            displayable_to_render = im.Alpha(img, 0.4) if is_ghost else img
            piece_y_offset = piece['y'] - (BOARD_HEIGHT - VISIBLE_BOARD_HEIGHT)

            for row_idx, row in enumerate(piece['shape']):
                for col_idx, cell in enumerate(row):
                    if cell != 0:
                        screen_x = x_off + (piece['x'] + col_idx) * PIXEL_SIZE
                        screen_y = y_off + (piece_y_offset + row_idx) * PIXEL_SIZE
                        if screen_y >= y_off:
                            r.blit(renpy.render(displayable_to_render, PIXEL_SIZE, PIXEL_SIZE, st, at), (screen_x, screen_y))
        
        def draw_ghost_piece(self, r, x_off, y_off, is_player, st, at):
            piece = self.game.player_piece if is_player else self.game.ai_piece
            if not piece: return
            ghost_piece = copy.deepcopy(piece)
            ghost_piece['y'] = self.game.get_ghost_y(is_player)
            self.draw_piece(r, ghost_piece, x_off, y_off, st, at, is_ghost=True)
            
        def draw_ui(self, r, width, height, st, at):
            text_size = 22
            # Shared Stats (Centered)
            r.blit(renpy.render(Text(f"Score: {self.game.score}", size=text_size), width, height, st, at), (width/2 - 50, 20))
            r.blit(renpy.render(Text(f"Lines: {self.game.lines_cleared}", size=text_size), width, height, st, at), (width/2 - 50, 50))
            r.blit(renpy.render(Text(f"Level: {self.game.level}", size=text_size), width, height, st, at), (width/2 - 50, 80))

            # Player UI (Left Side)
            player_ui_y = 300
            r.blit(renpy.render(Text("Hold", size=text_size), width, height, st, at), (player_ui_x, 150))
            if self.game.player_hold: self.draw_ui_piece(r, self.game.player_hold, (player_ui_x, 180), st, at)
            r.blit(renpy.render(Text("Next", size=text_size), width, height, st, at), (player_ui_x, 280))
            for i, p_type in enumerate(self.game.player_next[:3]):
                 self.draw_ui_piece(r, p_type, (player_ui_x, 310 + i * 60), st, at)

            # AI UI (Right Side)
            ai_ui_y = 300
            r.blit(renpy.render(Text("Yuri's Next", size=text_size), width, height, st, at), (ai_ui_x, 280))
            for i, p_type in enumerate(self.game.ai_next[:3]):
                 self.draw_ui_piece(r, p_type, (ai_ui_x, 310 + i * 60), st, at)

        def draw_ui_piece(self, r, piece_type, pos, st, at):
            # Copied directly from the modernized versus mode displayable
            info = TETROMINOES[piece_type]
            img = self.colors.get(info['color_id'])
            if not img: return
            piece_width = len(info['shape'][0]) * PIXEL_SIZE
            x_offset = ( (4 * PIXEL_SIZE) - piece_width ) / 2
            for y, row in enumerate(info['shape']):
                for x, cell in enumerate(row):
                    if cell != 0: r.blit(renpy.render(img, PIXEL_SIZE, PIXEL_SIZE, st, at), (pos[0] + x_offset + x*PIXEL_SIZE, pos[1] + y*PIXEL_SIZE))

        def ai_update(self, dtime):
            # This is the AI control logic, adapted for the co-op game
            if self.game.ai_piece and not self.ai_target_move:
                # We must tell the AI about the AI's piece and that its world is wider
                self.ai_target_move = self.ai.find_best_move(self.game, is_co_op=True)
            
            if self.ai_target_move:
                start_delay, end_delay = self.ai_delay_range
                current_action_delay = start_delay # In co-op, AI speed doesn't ramp up
                
                self.ai_move_timer += dtime
                if self.ai_move_timer >= current_action_delay:
                    self.ai_move_timer = 0
                    p = self.game.ai_piece
                    target_rot = self.ai_target_move['rotation']
                    target_x = self.ai_target_move['x']

                    if p['rotation'] != target_rot: self.game.rotate(is_player=False)
                    elif p['x'] < target_x: self.game.move(1, 0, is_player=False)
                    elif p['x'] > target_x: self.game.move(-1, 0, is_player=False)
                    else:
                        self.game.hard_drop(is_player=False) 
                        renpy.sound.play(self.sounds['drop'])
                        self.ai_target_move = None
        
        def event(self, ev, x, y, st):
            # This is our robust, modern event handler for player input
            if self.game.game_over: return
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_LEFT:
                    if self.held_key != 'left':
                        self.game.move(-1, 0, is_player=True)
                        renpy.sound.play(self.sounds['move'])
                        self.held_key = 'left'
                        self.das_timer = 0.0
                elif ev.key == pygame.K_RIGHT:
                    if self.held_key != 'right':
                        self.game.move(1, 0, is_player=True)
                        renpy.sound.play(self.sounds['move'])
                        self.held_key = 'right'
                        self.das_timer = 0.0
                elif ev.key == pygame.K_UP: self.game.rotate(is_player=True, clockwise=True)
                elif ev.key == pygame.K_z: self.game.rotate(is_player=True, clockwise=False)
                elif ev.key == pygame.K_SPACE: self.game.hard_drop(is_player=True)
                elif ev.key in [pygame.K_c, pygame.K_q, pygame.K_e]: self.game.hold(is_player=True)
                elif ev.key == pygame.K_DOWN: self.game.move(0, 1, is_player=True) # Soft Drop
            elif ev.type == pygame.KEYUP:
                if (ev.key == pygame.K_LEFT and self.held_key == 'left') or \
                   (ev.key == pygame.K_RIGHT and self.held_key == 'right'):
                    self.held_key = None

    # --- MODIFICATION TO TetrisAI CLASS ---
    # We need to make the AI aware of the wider co-op board.
    class TetrisAI:
        WEIGHTS = {'height': -0.51, 'lines': 0.76, 'holes': -0.35, 'bumpiness': -0.18, 't_spin_bonus': 0.5} # T-Spins are less important in co-op

        def find_best_move(self, game, is_co_op=False):
            best_move = {'score': -float('inf'), 'x': -1, 'rotation': 0}
            
            current_piece = game.ai_piece if is_co_op else game.current_piece
            board_width = game.CO_OP_BOARD_WIDTH if is_co_op else BOARD_WIDTH
            board_height = BOARD_HEIGHT
            board_state = game.board
            
            if not current_piece: return best_move
            temp_piece = copy.deepcopy(current_piece)
            
            for rotation in range(4):
                min_x = -min(c for r in temp_piece['shape'] for c, cell in enumerate(r) if cell)
                max_x = board_width - max(c + 1 for r in temp_piece['shape'] for c, cell in enumerate(r) if cell)

                for x in range(min_x, max_x + 1):
                    sim_board = copy.deepcopy(board_state)
                    y = temp_piece['y']
                    while not self._check_collision_sim(sim_board, temp_piece['shape'], x, y + 1, board_width, board_height):
                        y += 1
                    
                    self._place_piece_sim(sim_board, temp_piece['shape'], x, y, TETROMINOES[temp_piece['type']]['color_id'])
                    score = self._evaluate_board(sim_board, board_width, board_height)

                    if score > best_move['score']:
                        best_move = {'score': score, 'x': x, 'rotation': rotation}

                if temp_piece['type'] != 'O':
                    temp_piece['shape'] = list(zip(*temp_piece['shape'][::-1]))
            return best_move

        def _evaluate_board(self, board, board_width, board_height):
            heights = [0] * board_width
            for c in range(board_width):
                for r in range(board_height):
                    if board[r][c] != 0:
                        heights[c] = board_height - r
                        break
            agg_height = sum(heights)
            completed_lines = sum(1 for row in board if all(cell != 0 for cell in row))
            holes = sum(1 for c in range(board_width) for r in range(board_height - heights[c], board_height) if board[r][c] == 0)
            bumpiness = sum(abs(heights[i] - heights[i+1]) for i in range(len(heights) - 1))
            score = (self.WEIGHTS['height'] * agg_height + self.WEIGHTS['lines'] * completed_lines + self.WEIGHTS['holes'] * holes + self.WEIGHTS['bumpiness'] * bumpiness)
            return score

        def _check_collision_sim(self, board, shape, x, y, board_width, board_height):
            for r, row in enumerate(shape):
                for c, cell in enumerate(row):
                    if cell != 0:
                        board_x, board_y = x + c, y + r
                        if not (0 <= board_x < board_width and 0 <= board_y < board_height) or board[board_y][board_x] != 0:
                            return True
            return False
            
        # --- THIS IS THE MISSING METHOD THAT CAUSED THE CRASH ---
        def _place_piece_sim(self, board, shape, x, y, value_to_place):
            """
            Places a piece on a simulated board using a given value.
            """
            for r, row in enumerate(shape):
                for c, cell in enumerate(row):
                    if cell != 0:
                        board[y + r][x + c] = value_to_place
