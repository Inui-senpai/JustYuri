#default player_turn = True

label chess:
    python:
        DisableTalk()
        boopable = False
        show_chr("A-BFBAA-AAAC")

    if sanity_lvl() > 2 and karma_lvl() > 2:
        menu:
            y "Oh, so you'd like to play some chess, hm?"
            "Yes.":
                y "Oh, good."
                y "Which difficulty would you like this time?"
                $ pass
            "No.":
                y "I see..."
                y "Perhaps some other time, then."
                jump ch30_loop
    elif sanity_lvl() > 2 and karma_lvl() < 3:
        menu:
            y "You... want to play Chess...?"
            "Yes.":
                y "Oh..."
                y "Well, sure, I guess I wouldn't really mind."
                y "I have to wonder if you'll mock me for losing."
                y "Judging from how much pleasure you derive from my misery I assume you will."
                y "Anyway, just pick a difficulty and let's get on with it."
                $ pass
            "No.":
                y "Oh..."
                y "Perhaps... some other time, then."
                jump ch30_loop
    elif sanity_lvl() < 3 and karma_lvl() > 2:
        menu:
            y "Y-you want to play chess, yes?"
            "Yes.":
                y "Uhuhuhu~!"
                y "Which difficulty would you like this time?"
                y "It doesn't matter which one you'll choose, I'm sure you'll still dominate me no matter what you choose!~"
                $ pass
            "No.":
                y "O-oh..."
                y "Well..."
                y "Alright..."
                y "Perhaps some other time, then..."
                jump ch30_loop
    elif sanity_lvl() < 3 and karma_lvl() < 3:
        menu:
            y "You want to play chess, hm?"
            "Yes.":
                y "I'm sure you'll somehow find a way to make even such a trivial matter into a nightmare for me..."
                y "Somehow you'll still find a way to humiliate me..."
                y "Right..."
                y "Anyway, which difficulty do you want?"
                $ pass
            "No.":
                y "Oh..."
                y "Well... I see..."
                y "Perhaps some other time when you learn to make up your mind."
                jump ch30_loop


    $ fen = STARTING_FEN
    $ global_objects['STOCKFISH_ENGINE'] = chess.engine.SimpleEngine.popen_uci(STOCKFISH, startupinfo=STARTUPINFO)
    $ movetime = 2000

    menu:
        "Easy":
            $ show_chr("A-ACEAA-AMAM")
            y "Oh, I see."
            y "You'd like me to go easy on you this time, hm?"
            y "I'm happy to oblige, [player]!"
            $ depth = 1

        "Medium":
            $ show_chr("A-ACEAA-AMAM")
            y "Oh I see~ Trying to warm up with a slight challenge eh?"
            y "Well then. I would like to see how you do!"
            y "It is good to get out of your comfort zone a bit more."
            $ depth = 5

        "Hard":
            $ show_chr("A-ACEAA-AMAM")
            y "Oh huhuhehehe... Really turning the dial up are you now, [player]?"
            y "Well I do like it when you get a bit more daring~ It is rather inspiring."

            y "Well as people say nowadays, I guess, let these games begin!"
            y "O-oh but don't go too hard on yourself [player]... Eheheh."
            $ depth = 10

    menu:
        y "What color would you like to be?"

        "White":
            y "May the better player win!"
            $ player_color = WHITE # this constant is defined in chess_displayable.rpy
        "Black":
            y "May the better player win!"
            # board view flipped so that the player's color is at the bottom of the screen
            $ player_color = BLACK

    #window hide
    $ quick_menu = False

    # avoid rolling back and losing chess game state
    $ renpy.block_rollback()

    call screen chess(fen, player_color, movetime, depth)

    # avoid rolling back and entering the chess game again
    $ renpy.block_rollback()

    # restore rollback from this point on
    $ renpy.checkpoint()

    $ quick_menu = True
    window show


    # label chess_loop:
    #    $ keep_looping = True
    #    while keep_looping:
    #        $ global player_turn
    #        if player_turn:
    #            y "It's your turn, [player]!{fast}{nw}"
    #        else:
    #            y "I'm going to do this move{cps=1}...{/cps}{nw}"
    #            $ player_turn = True
    #        if _return == DRAW or _return == WHITE or _return == BLACK:
    #            hide screen Chess
    #            $ keep_looping = False

label chess_results:
    if _return == DRAW:
        y "Looks like it's a draw. Well played, [player]."
        jump ch30_loop
    else: # RESIGN or CHECKMATE
        $ winner = "White" if _return == WHITE else "Black"

        if player_color is not None: # PvC
            if _return == player_color:
                y "Congratulations, [player]!"
                jump ch30_loop
            else:
                y "Better luck next time, [player]."
                jump ch30_loop

    return
