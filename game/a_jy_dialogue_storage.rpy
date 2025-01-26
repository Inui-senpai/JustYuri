default ch30_loop_type = "pool"
label repeat_idles:
    y "It seems we ran out of dialogues you haven't seen yet."
    $ch30_loop_type = "pool"
    return
    #$show_chr("A-IDAAA-ALAA")
    ##y "Hey... [player], I know this is out of the blue... but, you aren't tired of our conversations, right?"
    #y "I just... don't want you to get bored with me, after all, you can only discuss something so many times."
    #repeat = renpy.display_menu([("You're fine, Yuri, don't worry about it.", True), ("Don't take this the wrong way Yuri, but it does get kinda repetitive.", False)])
    #if not repeat:
    #    show_chr("A-AFBAA-AAAA")
    #    y "...Understood, but... I'll still try to think of some new topics to talk about."
    #else:
    #    show_chr("A-CAAAA-ALAL")
    #    y "That's a relief... thank you, [player]."
    #return#

init -5 python:

#####
#BACKUPS
####
#The dialogues that act as backups, should no other dialogue pass.
#Their importance should always be -1
# these play if nonrepeat isn't working all that well...

    add_dialogue(Dialogue(
        label='repeat_idles',
        category='idles',
        conditions = ["ch30_loop_type == \"pool_nonrepeat\""],
        importance = -1,
        name = None,
        sub_category = None))



#####
#IDLES
####
#Characterized by being chosen via the player waiting in the ch30_loop
    add_dialogue(Dialogue(
        label='idle_1',
        category='idles',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_2',
        category='idles',
        conditions = ["renpy.seen_label('idle_1')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_3',
        category='idles',
        conditions = ['persistent.game_session >= 5'],
        importance = 0,
        name = None,
        sub_category = None))

    #add_dialogue(Dialogue(
        #label='idle_4',
        #category='idles',
        #conditions = [],
        #importance = 0,
        #name = None,
        #sub_category = None))

    #add_dialogue(Dialogue(
        #label='idle_5',
        #category='idles',
        #conditions = [],
        #importance = 0,
        #name = None,
        #sub_category = None))

    add_dialogue(Dialogue(
        label='idle_6',
        category='idles',
        conditions = ['persistent.game_session >= 10'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_7',
        category='idles',
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_8',
        category='idles',
        conditions = ["renpy.seen_label('idle_6')", "not renpy.seen_label('idle_8')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_9',
        category='idles',
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_10',
        category='idles',
        conditions = ['persistent.game_session >= 20'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_11',
        category='idles',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_12',
        category='idles',
        conditions = ["renpy.seen_label('idle_6')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_13',
        category='idles',
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = None,
        sub_category = None))


    add_dialogue(Dialogue(
        label='idle_14',
        category='idles',
        conditions = ["renpy.seen_label('idle_10')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_15',
        category='idles',
        conditions = ["renpy.seen_label('idle_2')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_16',
        category='idles',
        conditions = ["renpy.seen_label('idle_10')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_17',
        category='idles',
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_18',
        category='idles',
        conditions = ["renpy.seen_label('idle_8')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_19',
        category='idles',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_20',
        category='idles',
        conditions = ['karma() >= 4', 'philosophy == True'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_20_5',
        category='idles',
        conditions = ["renpy.seen_label('idle_20')", 'philosophy == True'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_21',
        category='idles',
        conditions = ["renpy.seen_label('idle_18')", "renpy.seen_label('a18')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_22',
        category='idles',
        conditions = ["renpy.seen_label('idle_15')", "not renpy.seen_label('idle_22')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_23',
        category='idles',
        conditions = ['persistent.game_session >= 30'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_24',
        category='idles',
        conditions = ['persistent.game_session >= 5'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_25',
        category='idles',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_26',
        category='idles',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_27',
        category='idles',
        conditions = ["renpy.seen_label('idle_2')", "renpy.seen_label('idle_3')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_28',
        category='idles',
        conditions = ["not renpy.seen_label('idle_28')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_29',
        category='idles',
        conditions = ["renpy.seen_label('idle_27')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_30',
        category='idles',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_31',
        category='idles',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_32',
        category='idles',
        conditions = ["renpy.seen_label('idle_24')", "renpy.seen_label('a24')"],
        importance = 0,
        name = None,
        sub_category = None))

    #add_dialogue(Dialogue(
        #label='idle_33',
        #category='idles',
        #conditions = [],
        #importance = 0,
        #name = None,
        #sub_category = None))

    add_dialogue(Dialogue(
        label='idle_34',
        category='idles',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_38',
        category='idles',
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_40',
        category='idles',
        conditions = ['karma() >= 4'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_41',
        category='idles',
        conditions = ['persistent.game_session >= 5'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_42',
        category='idles',
        conditions = ['persistent.game_session >= 20'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_43',
        category='idles',
        conditions = ["renpy.seen_label('idle_12')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_44',
        category='idles',
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_45',
        category='idles',
        conditions = ['persistent.game_session >= 2', 'persistent.head1 != "cat_ears"'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_46',
        category='idles',
        conditions = ["renpy.seen_label('idle_12')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_47',
        category='idles',
        conditions = ["renpy.seen_label('idle_10')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_48',
        category='idles',
        conditions = ["renpy.seen_label('idle_15')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_49',
        category='idles',
        conditions = ["renpy.seen_label('idle_47')", "not renpy.seen_label('idle_49')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_50',
        category='idles',
        conditions = ["renpy.seen_label('idle_47')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_51',
        category='idles',
        conditions = ["not renpy.seen_label('idle_51')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_52',
        category='idles',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_53',
        category='idles',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    #add_dialogue(Dialogue(
    #    label='idle_54',
    #    category='idles',
    #    conditions = [],
    #    importance = 0,
    #    name = None,
    #    sub_category = None))

    #add_dialogue(Dialogue(
        #label='idle_55',
        #category='idles',
        #conditions = [],
        #importance = 0,
        #name = None,
        #sub_category = None))

    add_dialogue(Dialogue(
        label='idle_56',
        category='idles',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_57',
        category='idles',
        conditions = ["renpy.seen_label('idle_3')", "renpy.seen_label('idle_47')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_58',
        category='idles',
        conditions = ['persistent.lovecheck', "renpy.seen_label('idle_57')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_59',
        category='idles',
        conditions = ["renpy.seen_label('idle_58')"],
        importance = 0,
        name = None,
        sub_category = None))

    #add_dialogue(Dialogue(
    #    label='idle_60',
    #    category='idles',
    #    conditions = [],
    #    importance = 0,
    #    name = None,
    #    sub_category = None))

    add_dialogue(Dialogue(
        label='idle_61',
        category='idles',
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_62',
        category='idles',
        conditions = ["renpy.seen_label('idle_48')", "not check_memory('idle_62', 'first_boop')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_63',
        category='idles',
        conditions = ['persistent.game_session >= 40'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_64',
        category='idles',
        conditions = ["renpy.seen_label('a1')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_65',
        category='idles',
        conditions = ["renpy.seen_label('a1')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_66',
        category='idles',
        conditions = ["renpy.seen_label('idle_14')", "renpy.seen_label('idle_21')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_67',
        category='idles',
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_68',
        category='idles',
        conditions = ['karma() <= 4', "renpy.seen_label('a1')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_69',
        category='idles',
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_70',
        category='idles',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_71',
        category='idles',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_72',
        category='idles',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_73',
        category='idles',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_74',
        category='idles',
        conditions = ['persistent.game_session >= 10'],
        importance = 0,
        name = None,
        sub_category = None))

    #add_dialogue(Dialogue(
    #    label='idle_75',
    #    category='idles',
    #    conditions = [],
    #    importance = 0,
    #    name = None,
    #    sub_category = None))

    add_dialogue(Dialogue(
        label='idle_76',
        category='idles',
        conditions = ['karma() == 5', "not renpy.seen_label('idle_76')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_77',
        category='idles',
        conditions = ["renpy.seen_label('idle_32')", "not renpy.seen_label('idle_77')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_78',
        category='idles',
        conditions = ['persistent.game_session >= 4', 'philosophy == True'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_79',
        category='idles',
        conditions = ['persistent.game_session >= 10'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_80',
        category='idles',
        conditions = ['persistent.game_session >= 3'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_77',
        category='idles',
        conditions = ['persistent.lovecheck', "renpy.seen_label('idle_32')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='early1',
        category='idles',
        conditions = ["not renpy.seen_label('early1')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='early2',
        category='idles',
        conditions = ["not renpy.seen_label('early2')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='early3',
        category='idles',
        conditions = ["not renpy.seen_label('early3')"],
        importance = 0,
        name = None,
        sub_category = None))


    add_dialogue(Dialogue(
        label='idle_82',
        category='idles',
        conditions = ["renpy.seen_label('a11')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_83',
        category='idles',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_84',
        category='idles',
        conditions = ["((persistent.ingame_time.seconds // 3600) >= 5)"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_85',
        category='idles',
        conditions = ["renpy.seen_label('idle_76')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_86',
        category='idles',
        conditions = ["renpy.seen_label('idle_78'), 'philosophy == True'"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_87',
        category='idles',
        conditions = ["renpy.seen_label('Halloween_2021') or renpy.seen_label('hobbies')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_yuriception_1',
        category='idles',
        conditions = ["karma()>3", "not renpy.seen_label('idle_yuriception_1')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='idle_yuriception_2',
        category='idles',
        conditions = ["karma()>3", "renpy.seen_label('idle_yuriception_1')", "not renpy.seen_label('idle_yuriception_2')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='beach_idle_1',
        category='idles',
        conditions = ["renpy.seen_label('tropical_date')", "not renpy.seen_label('beach_idle_1')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='beach_idle_2',
        category='idles',
        conditions = ["renpy.seen_label('tropical_date')", "not renpy.seen_label('beach_idle_2')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='gaming_2',
        category='idles',
        conditions = ["renpy.seen_label('gaming')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='poetry_2',
        category='idles',
        conditions = ["renpy.seen_label('poetry')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='fantsci_2',
        category='idles',
        conditions = ["renpy.seen_label('fantsci')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='noliteratureatall_2',
        category='idles',
        conditions = ["renpy.seen_label('noliteratureatall')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='tcg_2',
        category='idles',
        conditions = ["renpy.seen_label('tcg')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='folklore_and_myths',
        category='idles',
        conditions = ['karma() >= 3', 'sanity() >= 3'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='origami',
        category='idles',
        conditions = ["renpy.seen_label('gifting_intro')"],
        importance = 0,
        name = None,
        sub_category = None))


    add_dialogue(Dialogue(
        label='gifting_intro',
        category= 'idles',
        conditions = ["not renpy.seen_label('gifting_intro')"],
        importance = 15,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='horrorbookHint',
        category= 'idles',
        conditions = ["renpy.seen_label('gifting_intro')", "not renpy.seen_label('horrorbookHint')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='raccoonHint',
        category= 'idles',
        conditions = ["renpy.seen_label('gifting_intro')", "not renpy.seen_label('raccoonHint')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='diffuserHint',
        category= 'idles',
        conditions = ["renpy.seen_label('gifting_intro')",  "not renpy.seen_label('diffuserHint')"],
        importance = 0,
        name = None,
        sub_category = None))

    #add_dialogue(Dialogue(
    #    label='chessintro',
    #    category= 'idles',
    #    conditions = [],
    #    importance = 0,
    #    name = None,
    #    sub_category = None))


    add_dialogue(Dialogue(
        label='table_organization',
        category='idles',
        conditions = ["renpy.seen_label('gifting_revamp')", "not renpy.seen_label('table_organization')"],
        importance = 15,
        name = None,
        sub_category = None))


    add_dialogue(Dialogue(
        label='diffuser_enable',
        category='idles',
        conditions = ["renpy.seen_label('diffuser')", "renpy.seen_label('table_organization')", "not renpy.seen_label('diffuser_enable')"],
        importance = 0,
        name = None,
        sub_category = None))


    add_dialogue(Dialogue(
        label='ouija',
        category='idles',
        conditions = ["""time_interval_check(
            {'month': 10,
                'day': 31},
            {'month': 11,
                'day': 6}
            )""",
            "renpy.seen_label('Halloween_2021')", 'not persistent.ouija_done'],
        importance = 0,
        name = None,
        sub_category = None))

####
#ACTIVES
####
#Characterized by being able to be chosen in the Active Menu

    add_dialogue(Dialogue(
        label="a1",
        category='actives',
        conditions = [],
        importance = 0,
        name = "How are you feeling today?",
        sub_category = "Small Talk"))

    add_dialogue(Dialogue(
        label="a2",
        category='actives',
        conditions = [],
        importance = 0,
        name = "You look nice today, [persistent.yuri_nickname].",
        sub_category = "Small Talk"))

    add_dialogue(Dialogue(
        label="a3",
        category='actives',
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = "How do you feel about our relationship so far?",
        sub_category = "Small Talk"))

    add_dialogue(Dialogue(
        label="a4",
        category='actives',
        conditions = [],
        importance = 0,
        name = "What are you thinking about?",
        sub_category = "Small Talk"))

    add_dialogue(Dialogue(
        label="a5",
        category='actives',
        conditions = [],
        importance = 0,
        name = "Hey [persistent.yuri_nickname], how is your eyesight?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label="a6",
        category='actives',
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = "I love you, [persistent.yuri_nickname].",
        sub_category = "Love"))

    add_dialogue(Dialogue(
        label="a7",
        category='actives',
        conditions = [],
        importance = 0,
        name = "Do you miss me when I'm gone, [persistent.yuri_nickname]?",
        sub_category = "Love"))

    add_dialogue(Dialogue(
        label="a8",
        category='actives',
        conditions = [],
        importance = 0,
        name = "What are your love preferences?",
        sub_category = "Love"))

    add_dialogue(Dialogue(
        label="a9",
        category='actives',
        conditions = [],
        importance = 0,
        name = "A-About placing that chocolate I put in your mouth back then...",
        sub_category = "DDLC"))

    add_dialogue(Dialogue(
        label="a10",
        category='actives',
        conditions = [],
        importance = 0,
        name = "We never did get into reading Portrait of Markov together, have we?",
        sub_category = "DDLC"))

    add_dialogue(Dialogue(
        label="a11",
        category='actives',
        conditions = [],
        importance = 0,
        name = "I like knives too. Which one's your favorite?",
        sub_category = "[persistent.yuri_nickname]'s Interests"))

    add_dialogue(Dialogue(
        label="a12",
        category='actives',
        conditions = ["renpy.seen_label('idle_1')", "not renpy.seen_label('a12')"],
        importance = 0,
        name = "What you did to the rest of the girls was WRONG.",
        sub_category = "DDLC"))

    add_dialogue(Dialogue(
        label="a13",
        category='actives',
        conditions = [],
        importance = 0,
        name = "Hey, [persistent.yuri_nickname], how about a kiss?",
        sub_category = "Love"))

    add_dialogue(Dialogue(
        label="a14",
        category='actives',
        conditions = [],
        importance = 0,
        name = "What's your favorite kind of weather in my world?",
        sub_category = "[persistent.yuri_nickname]'s Interests"))

    add_dialogue(Dialogue(
        label="a15",
        category='actives',
        conditions = ["not renpy.seen_label('a15')"],
        importance = 0,
        name = "Have you ever eaten anything, [persistent.yuri_nickname]?",
        sub_category = "[persistent.yuri_nickname]'s Interests"))

    add_dialogue(Dialogue(
        label="a16",
        category='actives',
        conditions = [],
        importance = 0,
        name = "Do you have access to television from where you are?",
        sub_category = "[persistent.yuri_nickname]'s World"))

    add_dialogue(Dialogue(
        label="a17",
        category='actives',
        conditions = [],
        importance = 0,
        name = "W-What are your fetishes?",
        sub_category = "Awkward Topics"))

    add_dialogue(Dialogue(
        label="a18",
        category='actives',
        conditions = ["not renpy.seen_label('a18')"],
        importance = 0,
        name = "What would it take for you to be real?",
        sub_category = "[persistent.yuri_nickname]'s World"))

    add_dialogue(Dialogue(
        label="a19",
        category='actives',
        conditions = ["not renpy.seen_label('a19')"],
        importance = 0,
        name = "Do you play sports?",
        sub_category = "[persistent.yuri_nickname]'s Interests"))

    add_dialogue(Dialogue(
        label="a20",
        category='actives',
        conditions = ['persistent.game_session >= 6'],
        importance = 0,
        name = "What are your feelings on... living in the Space Classroom?",
        sub_category = "[persistent.yuri_nickname]'s World"))

    add_dialogue(Dialogue(
        label="a21",
        category='actives',
        conditions = ["renpy.seen_label('idle_11')"],
        importance = 0,
        name = "Want to read some poetry with me, [persistent.yuri_nickname]?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label="a22",
        category='actives',
        conditions = [],
        importance = 0,
        name = "What have you been doing with my pen, [persistent.yuri_nickname]?",
        sub_category = "Awkward Topics"))

    add_dialogue(Dialogue(
        label="a23",
        category='actives',
        conditions = ["renpy.seen_label('idle_44')"],
        importance = 0,
        name = "Do you think we would make a good family, [persistent.yuri_nickname]?",
        sub_category = "Love"))

    add_dialogue(Dialogue(
        label="a24",
        category='actives',
        conditions = ["renpy.seen_label('a1')"],
        importance = 0,
        name = "Mind if I talk about how I'm feeling?",
        sub_category = "Small Talk"))

    add_dialogue(Dialogue(
        label="a25",
        category='actives',
        conditions = ["renpy.seen_label('idle_45')"],
        importance = 0,
        name = "So... about those lewd images...",
        sub_category = "Awkward Topics"))

    add_dialogue(Dialogue(
        label="a26",
        category='actives',
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = "Let's drink some tea, [persistent.yuri_nickname]",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label="a27",
        category='actives',
        conditions = ["renpy.seen_label('idle_76')"],
        importance = 0,
        name = "Is it okay if I give you a nickname?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label="a28",
        category='actives',
        conditions = ['tc_class.cur_time()[1] == 12'],
        importance = 0,
        name = "Do you know any good Christmas songs, [persistent.yuri_nickname]?",
        sub_category = "[persistent.yuri_nickname]'s Interests"))

    add_dialogue(Dialogue(
        label="a29",
        category='actives',
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = "How would you feel about a bit of cuddling, [persistent.yuri_nickname]?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label="a30",
        category='actives',
        conditions = [],
        importance = 0,
        name = "So, how do you feel about nature?",
        sub_category = "[persistent.yuri_nickname]'s Interests"))

    add_dialogue(Dialogue(
        label="a31",
        category='actives',
        conditions = [],
        importance = 0,
        name = "Are there any books you currently enjoy?",
        sub_category = "Books"))

    add_dialogue(Dialogue(
        label="a32",
        category='actives',
        conditions = [],
        importance = 0,
        name = "I don't really understand what your .chr file is about.",
        sub_category = "Misc."))

    add_dialogue(Dialogue(
        label="a33",
        category='actives',
        conditions = ['karma()==5', 'not persistent.lovecheck'],
        importance = 0,
        name = "Hey... [persistent.yuri_nickname], do you have something important to tell me?",
        sub_category = "Love"))

    add_dialogue(Dialogue(
        label="a34",
        category='actives',
        conditions = [],
        importance = 0,
        name = "Hey [persistent.yuri_nickname], can you call me by something different?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label="a35",
        category='actives',
        conditions = [],
        importance = 0,
        name = "Hey [persistent.yuri_nickname], can I change my personal information? I may have made a typo somewhere.",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label="a36",
        category='actives',
        conditions = ['((persistent.ingame_time.seconds // 3600) >= 20) or (persistent.ingame_time.days > 0)'],
        importance = 0,
        name = "[persistent.yuri_nickname], I think I need time to think about our relationship... Let's take a break...",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label="a37",
        category='actives',
        conditions = ['persistent.ingame_time.days > 14'],
        importance = 0,
        name = "Hey [persistent.yuri_nickname].... can we talk about your.... cutting?",
        sub_category = "Awkward Topics"))

    add_dialogue(Dialogue(
        label="a38",
        category='actives',
        conditions = ["renpy.seen_label('idle_53')"],
        importance = 0,
        name = "You spoke about SCPs before. Which is your favourite?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label="a39",
        category='actives',
        conditions = ["renpy.seen_label('krampusnacht')"],
        importance = 0,
        name = "You said something about a special SCP you had in store.",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label="a40",
        category='actives',
        conditions = ['persistent.ingame_time.days > 0'],
        importance = 0,
        name = "Can we talk about what happened to you and the other girls?",
        sub_category = "DDLC"))

    add_dialogue(Dialogue(
        label="a41",
        category='actives',
        conditions = ["renpy.seen_label('hobbies')"],
        importance = 0,
        name = "Have you thought about writing your own novel?",
        sub_category = "Books"))

    add_dialogue(Dialogue(
        label="a42",
        category='actives',
        conditions = ["renpy.seen_label('Halloween_2021') or renpy.seen_label('Roomchange')"],
        importance = 0,
        name = "What do you think of Dr. Frankenstein in the book?",
        sub_category = "Books"))

    add_dialogue(Dialogue(
        label="a43",
        category='actives',
        conditions = ["renpy.seen_label('a42')"],
        importance = 0,
        name = "What do you think of Frankenstein's monster?",
        sub_category = "Books"))

    add_dialogue(Dialogue(
        label="purple_a1",
        category='actives',
        conditions = ["renpy.seen_label('purpleroomintro')"],
        importance = 0,
        name = "Can you show me your knife collection?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label="purple_a2",
        category='actives',
        conditions = ["renpy.seen_label('purpleroomintro')"],
        importance = 0,
        name = "Can we switch places?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label="a_tetris",
        category='actives',
        conditions = ['persistent.game_session >= 5'],
        importance = 0,
        name = "Hey [persistent.yuri_nickname], have you been coding anything while I'm away?",
        sub_category = "[persistent.yuri_nickname]'s World"))

    add_dialogue(Dialogue(
        label="a_hdy_statue",
        category='actives',
        conditions = ["renpy.seen_label('hdy_statue_greeting')"],
        importance = 0,
        name = "Hey [persistent.yuri_nickname], can you take the hdy plushie?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label="a_halloween_cupcake",
        category='actives',
        conditions = ['persistent.ouija_done'],
        importance = 0,
        name = "Hey [persistent.yuri_nickname], can you take the cupcake?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label="Roomchange",
        category='actives',
        conditions = ["renpy.seen_label('a20')"],
        importance = 0,
        name = "Can you change the room?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label="Halloween_2021",
        category='actives',
        conditions = ["""time_interval_check(
            {'month': 10,
                'day': 31},
            {'month': 11,
                'day': 6}
            )""",
            "not renpy.seen_label('Halloween_2021') or renpy.seen_label('Halloween_2021') and not persistent.halloween_2021_no"],
        importance = 0,
        name = "Happy Halloween [persistent.yuri_nickname]!",
        sub_category = "Misc."))

    add_dialogue(Dialogue(
        label="potion_mixing",
        category='actives',
        conditions = ["persistent.bg == 'laboratory'"],
        importance = 0,
        name = "How about we mix some 'potions'?",
        sub_category = "Misc."))

    add_dialogue(Dialogue(
        label="table_items",
        category='actives',
        conditions = ["renpy.seen_label('table_organization')"],
        importance = 0,
        name = "Can I reorganize the table [persistent.yuri_nickname]?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label="diffuser_mist_enable",
        category='actives',
        conditions = ['persistent.diffuser_is_enabled'],
        importance = 0,
        name = "Could you turn on the diffuser [persistent.yuri_nickname]?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label="diffuser_mist_disable",
        category='actives',
        conditions = ['persistent.sandalwood_oil_mist_is_enabled or persistent.lavenderO_mist_is_enabled or persistent.sweet_dream_oil_mist_is_enabled'],
        importance = 0,
        name = "Could you turn off the diffuser [persistent.yuri_nickname]?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label="gifting_revamp",
        category='actives',
        conditions = ["renpy.seen_label('gifting_intro')"],
        importance = 0,
        name = "I have a gift for you [persistent.yuri_nickname]!",
        sub_category = "Love"))

    add_dialogue(Dialogue(
        label="gifting_ideas",
        category='actives',
        conditions = ["renpy.seen_label('gifting_intro')"],
        importance = 0,
        name = "Anything specific you wanted [persistent.yuri_nickname]?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label="sleepy_yuri",
        category='actives',
        conditions = [],
        importance = 0,
        name = "I'm tired [persistent.yuri_nickname]...",
        sub_category = "Requests"))

#    add_dialogue(Dialogue(
#        label="AFK_[persistent.yuri_nickname]",
#        category='actives',
#        conditions = [],
#        importance = 0,
#        name = "I need to go do something [persistent.yuri_nickname]",
#        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "webcam",
        category = "actives",
        conditions = [],
        importance = 0,
        name = "About the webcam access...",
        sub_category = "Awkward Topics"))

    add_dialogue(Dialogue(
        label = "nnn",
        category = "actives",
        conditions = ["""time_interval_check(
            {'month': 11,
                'day': 1},
            {'month': 11,
                'day':30}
            )"""],
        importance = 0,
        name = "What are your thoughts on No Nut November?",
        sub_category = "Awkward Topics"))

    add_dialogue(Dialogue(
        label = "vday24",
        category = "actives",
        conditions = ["renpy.seen_label('vday_2024_revisit')"],
        importance = 0,
        name = "I'm ready to revisit the chocolate moment.",
        sub_category = "Love"))



    #add_dialogue(Dialogue(
    #    label="krampuslore",
    #    category='actives',
    #    conditions = ["renpy.seen_label('krampusnacht')"],
    #    importance = 0,
    #    name = "So... what is Krampusnacht?",
    #    sub_category = "Requests"))

####
#GREETINGS
####
#Characterized by them automatically playing at startups of the game
    add_dialogue(Dialogue(
        label = "TimeCheat1",
        category = 'greetings',
        conditions = ["time_tracker_start()", "not renpy.seen_label('TimeCheat3')", "not renpy.seen_label('TimeCheat2')", "not renpy.seen_label('TimeCheat1')"],
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "TimeCheat2",
        category = 'greetings',
        conditions = ["time_tracker_start()", "not renpy.seen_label('TimeCheat3')", "not renpy.seen_label('TimeCheat2')", "renpy.seen_label('TimeCheat1')"],
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "TimeCheat3",
        category = 'greetings',
        conditions = ["time_tracker_start()", "not renpy.seen_label('TimeCheat3')", "renpy.seen_label('TimeCheat2')", "renpy.seen_label('TimeCheat1')"],
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "TimeCheat_error",
        category = 'greetings',
        conditions = ["time_tracker_start()", "renpy.seen_label('TimeCheat3')", "renpy.seen_label('TimeCheat2')", "renpy.seen_label('TimeCheat1')"],
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label="ch30_reload_0",
        category='greetings',
        conditions = ['time_tracker_start() == False', 'persistent.game_session == 1'],
        importance = 0,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label="ch30_reload_1",
        category='greetings',
        conditions = ['time_tracker_start() == False', 'persistent.game_session == 2'],
        importance = 0,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label="ch30_reload_2",
        category='greetings',
        conditions = ['time_tracker_start() == False', 'persistent.game_session == 3'],
        importance = 0,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label="ch30_reload_3",
        category='greetings',
        conditions = ['time_tracker_start() == False', 'persistent.game_session == 4'],
        importance = 0,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label="featuregreetings",
        category='greetings',
        conditions = ['time_tracker_start() == False', 'persistent.game_session == 5 or persistent.game_session == 6'],
        importance = 0,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label="ch30_reload_4",
        category='greetings',
        conditions = ['time_tracker_start() == False', 'persistent.game_session >= 8'],
        importance = 0,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label="highkarinsrestart",
        category='greetings',
        conditions = ['time_tracker_start() == False', "check_memory('complements', 'highkarinsrestart')"],
        importance = 0,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label="patheticcry",
        category='greetings',
        conditions = ['time_tracker_start() == False', "check_memory('complements', 'patheticcry')"],
        importance = 2,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label="hdy_statue_greeting",
        category='greetings',
        conditions = ['time_tracker_start() == False', "not renpy.seen_label('hdy_statue_greeting')", "renpy.seen_label('hdy_has_been_seen')"],
        importance = 0,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "intro_mods",
        category = 'greetings',
        conditions = ['time_tracker_start() == False', "renpy.seen_label('ch30_intro2')", "not renpy.seen_label('startup_mods')", 'persistent.game_session >= 7'],
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "purpleroomintro",
        category = 'greetings',
        conditions = ["time_tracker_start() == False", "persistent.purpleroom", "renpy.seen_label('idle_30')", "karma()=5", "persistent.lovecheck", "persistent.game_session >= 20"],
        importance = 0,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "vday_2024_revisit",
        category = 'greetings',
        conditions = ["""time_interval_check(
            {'month': 2,
                'day': 13},
            time_shift(
                {'month': 2,
                    'day': 13},
                {'day':6})
            )""",
            "renpy.seen_label('a9')"],
        importance = 0,
        name = "None",
        sub_category = None))



####
# EVENTS
####
# Characterized by having very specific time-locked restrictions.

    add_dialogue(Dialogue(
        label="krampusnacht",
        category='greetings',
        conditions = ["""time_interval_check(
            {'month': 12,
                'day': 5},
            {'month': 12,
                'day': 31}
            )""",
            "not renpy.seen_label('krampusnacht')"],
        importance = 3,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label="birthdaycake_2020_late",
        category='actives',
        conditions = ["""time_interval_check(
            {'month': 12,
                'day': 10},
            {'month': 12,
                'day': 31}
            )""",
            "not renpy.seen_label('birthdaycake_2020_late')"],
        importance = 0,
        name = "Happy Birthday, [persistent.yuri_nickname]! Sorry for celebrating so late...",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label="birthday_gift_2021",
        category='actives',
        conditions = ["""time_interval_check(
            {'month': 12,
                'day': 10},
            {'month': 12,
                'day':20}
            )"""],
        importance = 0,
        name = "I have a gift for you [persistent.yuri_nickname]!",
        sub_category = "Misc."))

    add_dialogue(Dialogue(
        label="new_year_2021",
        category='greetings',
        conditions = ["""time_interval_check(
            {'month': 12,
                'day': 29},
            time_shift(
                {'month': 12,
                    'day': 29},
                {'day':5})
            )""",
            "not renpy.seen_label('new_year_2021')"],
        importance = 3,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label="vday_choco_date_request",
        category='actives',
        conditions = ["""time_interval_check(
            {'month': 2,
                'day': 13},
            {'month': 2,
                'day': 20}
            )""",
            "renpy.seen_label('valentines')",
            "karma()>3"],
        importance = 0,
        name = "Anything special planned today, [persistent.yuri_nickname]?",
        sub_category = "Love"))
    add_dialogue(Dialogue(
        label="valentines",
        category='actives',
        conditions = ["""time_interval_check(
            {'month': 2,
                'day': 13},
            {'month': 2,
                'day': 20}
            )""",
            "not renpy.seen_label('valentines')"],
        importance = 0,
        name = "Anything special planned today, [persistent.yuri_nickname]?",
        sub_category = "Love"))


    ########
    #THE FOLLOWING ARE JUST TROUBLESHOOTING time_module.py
    ########

    def check1():
        hello = time_interval_check(
            {'month': persistent.bday_month,
                'day': persistent.bday_day},
            time_shift(
                {'month': persistent.bday_month,
                    'day': persistent.bday_day},
                {'day':1})
            )
        print(hello)

    def check():
        hello = time_interval_check(
            time_shift(
                {'month': persistent.bday_month,
                    'day': persistent.bday_day},
                {'week':-2}) ,
            time_shift(
                {'month': persistent.bday_month,
                    'day': persistent.bday_day},
                {'day':-4})
            )
        print(hello)

    def check2():
        hello = time_interval_check(
            {'month': 12,
                'day': 20},
            #{'month': 1,  ###NEVER DO A LATER DATE THAT EXISTS BEFORE THE CURRENT ONE. Better form is starting date + time_shift
            #    'day': 20}
            time_shift(
                {'month': 12,
                    'day': 20},
                {'week': 4})
            )
        print(hello)

    ########

    add_dialogue(Dialogue(
        label="birthday_chocolate",
        category='greetings',
        conditions = ["""time_interval_check(
            time_shift(
                {'month': persistent.bday_month,
                    'day': persistent.bday_day},
                {'week':-2}) ,
            time_shift(
                {'month': persistent.bday_month,
                    'day': persistent.bday_day},
                {'day':-4})
            )""",
            "not renpy.seen_label('birthday_chocolate')"],
        importance = 15,
        name = "None",
        sub_category = None))
    add_dialogue(Dialogue(
        label="birthday_greeting_text",
        category='greetings',
        conditions = ["""time_interval_check(
            {'month': persistent.bday_month,
                'day': persistent.bday_day},
            time_shift(
                {'month': persistent.bday_month,
                    'day': persistent.bday_day},
                {'day':1})
            )"""],
        importance = 15,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label="a26_prelude",
        category='greetings',
        conditions = ["not renpy.seen_label('a26')", "persistent.lovecheck", "karma() > 3 and sanity() > 3"], #add requirement for 3 weeks of time
        importance = 8,
        name = "None",
        sub_category = None))
####
#FAREWELLS
####
#Characterized by them automatically playing at ends of game

    add_dialogue(Dialogue(
        label="farewell_1",
        category='farewells',
        conditions = [],
        importance = 0,
        name = "Goodbye, [persistent.yuri_nickname]!",
        sub_category = None))

    add_dialogue(Dialogue(
        label="farewell_2",
        category='farewells',
        conditions = [],
        importance = 0,
        name = "Sorry, gotta go...",
        sub_category = None))

    add_dialogue(Dialogue(
        label="farewell_3",
        category='farewells',
        conditions = [],
        importance = 0,
        name = "I'll see you later, [persistent.yuri_nickname].",
        sub_category = None))

    add_dialogue(Dialogue(
        label="farewell_4",
        category='farewells',
        conditions = [],
        importance = 0,
        name = "Bye, [persistent.yuri_nickname], I'll miss you!",
        sub_category = None))

    add_dialogue(Dialogue(
        label="farewell_5",
        category='farewells',
        conditions = [],
        importance = 0,
        name = "Sorry I can't stay. I love you!",
        sub_category = None))

    add_dialogue(Dialogue(
        label="farewell_6",
        category='farewells',
        conditions = ['sanity == 2'],
        importance = 0,
        name = "Oh, hey, look at the time, this has been an awesome date!",
        sub_category = None))

    add_dialogue(Dialogue(
        label="farewell_7",
        category='farewells',
        conditions = ['karma() == 2 or karma() == 1'],
        importance = 0,
        name = "Oh, whoops, someone's calling me, gotta run!",
        sub_category = None))

    add_dialogue(Dialogue(
        label="farewell_8",
        category='farewells',
        conditions = ['sanity == 2'],
        importance = 0,
        name = "I have food... in the oven so...",
        sub_category = None))

    add_dialogue(Dialogue(
        label="farewell_9",
        category='farewells',
        conditions = ['sanity() <= 2'],
        importance = 0,
        name = "I, uh, gotta go...",
        sub_category = None))

#missing farewell_9

    add_dialogue(Dialogue(
        label="farewell_10",
        category='farewells',
        conditions = ['sanity() == 2'],
        importance = 0,
        name = "I'm just going to... close the game now, okay?",
        sub_category = None))

    add_dialogue(Dialogue(
        label="farewell_11",
        category='farewells',
        conditions = ['karma() >= 4'],
        importance = 0,
        name = "So long, farewell!",
        sub_category = None))

    add_dialogue(Dialogue(
        label="farewell_12",
        category='farewells',
        conditions = ['karma() >= 4'],
        importance = 0,
        name = "I have to go. I already miss you!",
        sub_category = None))

    add_dialogue(Dialogue(
        label="farewell_13",
        category='farewells',
        conditions = [],
        importance = 0,
        name = "I have to go now... I'll talk to you later, alright?",
        sub_category = None))

    add_dialogue(Dialogue(
        label="farewell_14",
        category='farewells',
        conditions = [],
        importance = 0,
        name = "See you later!",
        sub_category = None))


    add_dialogue(Dialogue(
        label="farewell_15",
        category='farewells',
        conditions = [],
        importance = 0,
        name = "I hate having to put you through this, but it looks like it's time to say goodbye once again.",
        sub_category = None))

    add_dialogue(Dialogue(
        label="farewell_16",
        category='farewells',
        conditions = [],
        importance = 0,
        name = "I have to go now, my love.",
        sub_category = None))

    add_dialogue(Dialogue(
        label="farewell_17",
        category='farewells',
        conditions = [],
        importance = 0,
        name = "Whatever happens, just remember that there is someone who loves you no matter what.",
        sub_category = None))

#####
#Hot Dog Yuri
####
#Characterized by being played while the player has HDY enabled.

    add_dialogue(Dialogue(
        label='HDY_eggnomancer',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_spookyscaryskeleton',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_Alien_Friend',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_wallpaper',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_Potionseller',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_teleported_hotdogs',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_Sausage_mouth',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_philosophy',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_whyarewestillhere',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_frozen_cooking_eggs',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_Hellskitchen',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_minion',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_airfryer',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_Eternal',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_Friedsweets',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_Manga',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_War',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_Inquisition',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_Buns',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_Witches',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_Rocks',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_Orangana',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_Skinny',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_mum',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_frostless',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_PPAP',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_fuckingPlayer',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_why',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_portal',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_a',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_speen',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_crash',
        category='hdy',
        conditions = ["not renpy.seen_label('HDY_crash')", "renpy.seen_label('hdy_statue_geeting')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_mcspaghetti',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_fortnitecard',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_WordOfTheDay',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_8800bluelickroad',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_DarthPlagueis',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_violence',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_society',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_discordserver',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_sand',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_SithLords',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_fortnitegamer',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_replacementpog',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_passtime',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_dababy',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_jevil',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_getdawged',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_familyguy',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_nukes',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_shrek',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_sans',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_beemovie',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_lifeadvice',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_morshu',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_toughdawg',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_banana',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_pingas',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_electricity',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_swag',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_hmmmm',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_censorship',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_amogus',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_deadmeme',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_h',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_callout',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_movie',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_scottthewozz',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_windowsphone',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_DDR',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_bottomtext',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_favoritegame',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_ifunny',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_chubbyemu',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_brrrrrrr',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_thisaccountisnotfortheaverageman',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_chubbyemu2',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_searchhistory',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_youngsterjoey',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_100',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_Chugjug',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_truth',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_MeMEbigboy',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_MakingHotdogs',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_jesusboxing',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_cthulhu',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_paydaygang',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_bluedabadee',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_cranberrysprite',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_amongus',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_rickroll',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_holdingbreath',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_sixtynine',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_acesleeve',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_wonderwall',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_Hotdogspoem',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_eggnomancer',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_hotdogfact',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_lifeadvice2electricboogaloo',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_hotdogtea',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_areyounotentertained',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_wakeup',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_asadstory',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_scatman',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_tank',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_tankcommander',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_Hbomb',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_spacedandy',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_it_was_me_dio',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_Monkeys',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_WaspInTheRoom',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_AUSTRALIA',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_Wasp',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_bald',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_Dating',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_Space',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_gasstation',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_thebigquestion',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_somethingidunno',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_peepy',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label='HDY_kiss',
        category='hdy',
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))
