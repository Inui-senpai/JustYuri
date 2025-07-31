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

init -3 python:

#####
#BACKUPS
####
#The dialogues that act as backups, should no other dialogue pass.
#Their importance should always be -1
# these play if nonrepeat isn't working all that well...

    add_dialogue(Dialogue(
        label = 'repeat_idles',
        category = DialogueAPI.category_idle,
        conditions = ["ch30_loop_type == \"pool_nonrepeat\""],
        importance = -1,
        name = None,
        sub_category = None))



#####
#IDLES
####
#Characterized by being chosen via the player waiting in the ch30_loop
    add_dialogue(Dialogue(
        label = 'idle_1',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_2',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_1')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_3',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.game_session >= 5'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_4',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_5',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label(idle_4)"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_6',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.game_session >= 10'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_7',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_8',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_6')", "not renpy.seen_label('idle_8')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_9',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_10',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.game_session >= 20'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_11',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_12',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_6')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_13',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = None,
        sub_category = None))


    add_dialogue(Dialogue(
        label = 'idle_14',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_10')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_15',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_2')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_16',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_10')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_17',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_18',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_8')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_19',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_20',
        category = DialogueAPI.category_idle,
        conditions = ['karma_lvl() >= 4', 'philosophy == True'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_21',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_20')", 'philosophy == True'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_22',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_18')", "renpy.seen_label('a18')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_23',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_15')", "not renpy.seen_label('idle_22')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_24',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.game_session >= 30'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_25',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.game_session >= 5'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_26',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_27',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_28',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_2')", "renpy.seen_label('idle_3')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_29',
        category = DialogueAPI.category_idle,
        conditions = ["not renpy.seen_label('idle_29')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_30',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_29')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_31',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_32',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_33',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_25')", "renpy.seen_label('a24')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_34',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_35',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label(idle_4)", "renpy.seen_label(idle_5)"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_36',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_37',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_38',
        category = DialogueAPI.category_idle,
        conditions = ['karma_lvl() >= 4'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_39',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.game_session >= 5'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_40',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.game_session >= 20'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_41',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_12')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_42',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_43',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.game_session >= 2', 'persistent.head1 != "cat_ears"'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_44',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_12')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_45',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_10')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_46',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_15')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_47',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_45')", "not renpy.seen_label('idle_47')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_48',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_45')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_49',
        category = DialogueAPI.category_idle,
        conditions = ["not renpy.seen_label('idle_49')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_50',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_51',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    #add_dialogue(Dialogue(
    #    label = 'idle_52',
    #    category = DialogueAPI.category_idle,
    #    conditions = [],
    #    importance = 0,
    #    name = None,
    #    sub_category = None))

    #add_dialogue(Dialogue(
        #label = 'idle_53',
        #category = DialogueAPI.category_idle,
        #conditions = [],
        #importance = 0,
        #name = None,
        #sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_54',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_55',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_3')", "renpy.seen_label('idle_45')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_56',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.lovecheck', "renpy.seen_label('idle_55')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_57',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_56')"],
        importance = 0,
        name = None,
        sub_category = None))

    #add_dialogue(Dialogue(
    #    label = 'idle_58',
    #    category = DialogueAPI.category_idle,
    #    conditions = [],
    #    importance = 0,
    #    name = None,
    #    sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_59',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_60',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_44')", "not check_memory('idle_60', 'first_boop')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_61',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.game_session >= 40'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_62',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('a1')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_63',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('a1')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_64',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_14')", "renpy.seen_label('idle_22')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_65',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_66',
        category = DialogueAPI.category_idle,
        conditions = ['karma_lvl() <= 4', "renpy.seen_label('a1')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_67',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_68',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_69',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_70',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_71',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_72',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.game_session >= 10'],
        importance = 0,
        name = None,
        sub_category = None))

    #add_dialogue(Dialogue(
    #    label = 'idle_73',
    #    category = DialogueAPI.category_idle,
    #    conditions = [],
    #    importance = 0,
    #    name = None,
    #    sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_74',
        category = DialogueAPI.category_idle,
        conditions = ['karma_lvl() == 5', "not renpy.seen_label('idle_74')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_75',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_32')", "not renpy.seen_label('idle_75')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_76',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.game_session >= 4', 'philosophy == True'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_77',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.game_session >= 10'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_78',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.game_session >= 3'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_79',
        category = DialogueAPI.category_idle,
        conditions = ['persistent.lovecheck', "renpy.seen_label('idle_34')"],
        importance = 0,
        name = None,
        sub_category = None))


    add_dialogue(Dialogue(
        label = 'idle_80',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('a11')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_81',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_82',
        category = DialogueAPI.category_idle,
        conditions = ["((persistent.ingame_time.seconds // 3600) >= 5)"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_83',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_72')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_84',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('idle_74'), 'philosophy == True'"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_85',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('Halloween_2021') or renpy.seen_label('hobbies')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_86',
        category = DialogueAPI.category_idle,
        conditions = ["karma_lvl()>3", "not renpy.seen_label('idle_84')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_87',
        category = DialogueAPI.category_idle,
        conditions = ["karma_lvl()>3", "renpy.seen_label('idle_84')", "not renpy.seen_label('idle_85')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_88',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('tropical_date')", "not renpy.seen_label('idle_88')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_89',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('tropical_date')", "not renpy.seen_label('idle_89')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_90',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    #add_dialogue(Dialogue(
    #    label = 'idle_91',
    #    category = DialogueAPI.category_idle,
    #    conditions = [],
    #    importance = 0,
    #    name = None,
    #    sub_category = None))

    #add_dialogue(Dialogue(
    #    label = 'idle_92',
    #    category = DialogueAPI.category_idle,
    #    conditions = [],
    #    importance = 0,
    #    name = None,
    #    sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_93',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_94',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_95',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_96',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_97',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_98',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_99',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_100',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_101',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_102',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_103',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_104',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_105',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_106',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label(idle_4)", "renpy.seen_label(idle_5)", "ren.seen_label(idle_35)"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_107',
        category = DialogueAPI.category_idle,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'idle_108',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label(idle_4)", "renpy.seen_label(idle_5)", "ren.seen_label(idle_35)", "renpy.seen_label(idle_106)"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'gaming_2',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('gaming')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'poetry_2',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('poetry')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'fantsci_2',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('fantsci')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'noliteratureatall_2',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('noliteratureatall')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'tcg_2',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('tcg')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'folklore_and_myths',
        category = DialogueAPI.category_idle,
        conditions = ['karma_lvl() >= 3', 'sanity_lvl() >= 3'],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'origami',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('gifting_intro')"],
        importance = 0,
        name = None,
        sub_category = None))


    add_dialogue(Dialogue(
        label = 'gifting_intro',
        category = DialogueAPI.category_idle,
        conditions = ["not renpy.seen_label('gifting_intro')"],
        importance = 15,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'horrorbookHint',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('gifting_intro')", "not renpy.seen_label('horrorbookHint')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'raccoonHint',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('gifting_intro')", "not renpy.seen_label('raccoonHint')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'diffuserHint',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('gifting_intro')",  "not renpy.seen_label('diffuserHint')"],
        importance = 0,
        name = None,
        sub_category = None))

    #add_dialogue(Dialogue(
    #    label = 'chessintro',
    #    category = DialogueAPI.category_idle,
    #    conditions = [],
    #    importance = 0,
    #    name = None,
    #    sub_category = None))


    add_dialogue(Dialogue(
        label = 'table_organization',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('gifting_revamp')", "not renpy.seen_label('table_organization')"],
        importance = 15,
        name = None,
        sub_category = None))


    add_dialogue(Dialogue(
        label = 'diffuser_enable',
        category = DialogueAPI.category_idle,
        conditions = ["renpy.seen_label('diffuser')", "renpy.seen_label('table_organization')", "not renpy.seen_label('diffuser_enable')"],
        importance = 0,
        name = None,
        sub_category = None))


    add_dialogue(Dialogue(
        label = 'ouija',
        category = DialogueAPI.category_idle,
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
        label = "a1",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "How are you feeling today?",
        sub_category = "Small Talk"))

    add_dialogue(Dialogue(
        label = "a2",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "You look nice today, [persistent.yuri_nickname].",
        sub_category = "Small Talk"))

    add_dialogue(Dialogue(
        label = "a3",
        category = DialogueAPI.category_talk,
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = "How do you feel about our relationship so far?",
        sub_category = "Small Talk"))

    add_dialogue(Dialogue(
        label = "a4",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "What are you thinking about?",
        sub_category = "Small Talk"))

    add_dialogue(Dialogue(
        label = "a5",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "Hey [persistent.yuri_nickname], how is your eyesight?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "a6",
        category = DialogueAPI.category_talk,
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = "I love you, [persistent.yuri_nickname].",
        sub_category = "Love"))

    add_dialogue(Dialogue(
        label = "a7",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "Do you miss me when I'm gone, [persistent.yuri_nickname]?",
        sub_category = "Love"))

    add_dialogue(Dialogue(
        label = "a8",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "What are your love preferences?",
        sub_category = "Love"))

    add_dialogue(Dialogue(
        label = "a9",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "A-About placing that chocolate I put in your mouth back then...",
        sub_category = "DDLC"))

    add_dialogue(Dialogue(
        label = "a10",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "We never did get into reading Portrait of Markov together, have we?",
        sub_category = "DDLC"))

    add_dialogue(Dialogue(
        label = "a11",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "I like knives too. Which one's your favorite?",
        sub_category = "[persistent.yuri_nickname]'s Interests"))

    add_dialogue(Dialogue(
        label = "a12",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('idle_1')", "not renpy.seen_label('a12')"],
        importance = 0,
        name = "What you did to the rest of the girls was WRONG.",
        sub_category = "DDLC"))

    add_dialogue(Dialogue(
        label = "a13",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "Hey, [persistent.yuri_nickname], how about a kiss?",
        sub_category = "Love"))

    add_dialogue(Dialogue(
        label = "a14",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "What's your favorite kind of weather in my world?",
        sub_category = "[persistent.yuri_nickname]'s Interests"))

    add_dialogue(Dialogue(
        label = "a15",
        category = DialogueAPI.category_talk,
        conditions = ["not renpy.seen_label('a15')"],
        importance = 0,
        name = "Have you ever eaten anything, [persistent.yuri_nickname]?",
        sub_category = "[persistent.yuri_nickname]'s Interests"))

    add_dialogue(Dialogue(
        label = "a16",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "Do you have access to television from where you are?",
        sub_category = "[persistent.yuri_nickname]'s World"))

    add_dialogue(Dialogue(
        label = "a17",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "W-What are your fetishes?",
        sub_category = "Awkward Topics"))

    add_dialogue(Dialogue(
        label = "a18",
        category = DialogueAPI.category_talk,
        conditions = ["not renpy.seen_label('a18')"],
        importance = 0,
        name = "What would it take for you to be real?",
        sub_category = "[persistent.yuri_nickname]'s World"))

    add_dialogue(Dialogue(
        label = "a19",
        category = DialogueAPI.category_talk,
        conditions = ["not renpy.seen_label('a19')"],
        importance = 0,
        name = "Do you play sports?",
        sub_category = "[persistent.yuri_nickname]'s Interests"))

    add_dialogue(Dialogue(
        label = "a20",
        category = DialogueAPI.category_talk,
        conditions = ['persistent.game_session >= 6'],
        importance = 0,
        name = "What are your feelings on... living in the Space Classroom?",
        sub_category = "[persistent.yuri_nickname]'s World"))

    add_dialogue(Dialogue(
        label = "a21",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('idle_11')"],
        importance = 0,
        name = "Want to read some poetry with me, [persistent.yuri_nickname]?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "a22",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "What have you been doing with my pen, [persistent.yuri_nickname]?",
        sub_category = "Awkward Topics"))

    add_dialogue(Dialogue(
        label = "a23",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('idle_44')"],
        importance = 0,
        name = "Do you think we would make a good family, [persistent.yuri_nickname]?",
        sub_category = "Love"))

    add_dialogue(Dialogue(
        label = "a24",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('a1')"],
        importance = 0,
        name = "Mind if I talk about how I'm feeling?",
        sub_category = "Small Talk"))

    add_dialogue(Dialogue(
        label = "a25",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('idle_45')"],
        importance = 0,
        name = "So... about those lewd images...",
        sub_category = "Awkward Topics"))

    add_dialogue(Dialogue(
        label = "a26",
        category = DialogueAPI.category_talk,
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = "Let's drink some tea, [persistent.yuri_nickname]",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "a27",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('idle_76')"],
        importance = 0,
        name = "Is it okay if I give you a nickname?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "a28",
        category = DialogueAPI.category_talk,
        conditions = ['tc_class.cur_time()[1] == 12'],
        importance = 0,
        name = "Do you know any good Christmas songs, [persistent.yuri_nickname]?",
        sub_category = "[persistent.yuri_nickname]'s Interests"))

    add_dialogue(Dialogue(
        label = "a29",
        category = DialogueAPI.category_talk,
        conditions = ['persistent.lovecheck'],
        importance = 0,
        name = "How would you feel about a bit of cuddling, [persistent.yuri_nickname]?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "a30",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "So, how do you feel about nature?",
        sub_category = "[persistent.yuri_nickname]'s Interests"))

    add_dialogue(Dialogue(
        label = "a31",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "Are there any books you currently enjoy?",
        sub_category = "Books"))

    add_dialogue(Dialogue(
        label = "a32",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "I don't really understand what your .chr file is about.",
        sub_category = "Misc."))

    add_dialogue(Dialogue(
        label = "a33",
        category = DialogueAPI.category_talk,
        conditions = ['karma_lvl()==5', 'not persistent.lovecheck'],
        importance = 0,
        name = "Hey... [persistent.yuri_nickname], do you have something important to tell me?",
        sub_category = "Love"))

    add_dialogue(Dialogue(
        label = "a34",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "Hey [persistent.yuri_nickname], can you call me by something different?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "a35",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "Hey [persistent.yuri_nickname], can I change my personal information? I may have made a typo somewhere.",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "a36",
        category = DialogueAPI.category_talk,
        conditions = ['((persistent.ingame_time.seconds // 3600) >= 20) or (persistent.ingame_time.days > 0)'],
        importance = 0,
        name = "[persistent.yuri_nickname], I think I need time to think about our relationship... Let's take a break...",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "a37",
        category = DialogueAPI.category_talk,
        conditions = ['persistent.ingame_time.days > 14'],
        importance = 0,
        name = "Hey [persistent.yuri_nickname].... can we talk about your.... cutting?",
        sub_category = "Awkward Topics"))

    add_dialogue(Dialogue(
        label = "a38",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('idle_53')"],
        importance = 0,
        name = "You spoke about SCPs before. Which is your favourite?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "a39",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('krampusnacht')"],
        importance = 0,
        name = "You said something about a special SCP you had in store.",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "a40",
        category = DialogueAPI.category_talk,
        conditions = ['persistent.ingame_time.days > 0'],
        importance = 0,
        name = "Can we talk about what happened to you and the other girls?",
        sub_category = "DDLC"))

    add_dialogue(Dialogue(
        label = "a41",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('hobbies')"],
        importance = 0,
        name = "Have you thought about writing your own novel?",
        sub_category = "Books"))

    add_dialogue(Dialogue(
        label = "a42",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('Halloween_2021') or renpy.seen_label('Roomchange')"],
        importance = 0,
        name = "What do you think of Dr. Frankenstein in the book?",
        sub_category = "Books"))

    add_dialogue(Dialogue(
        label = "a43",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('a42')"],
        importance = 0,
        name = "What do you think of Frankenstein's monster?",
        sub_category = "Books"))

    add_dialogue(Dialogue(
        label = "purple_a1",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('purpleroomintro')"],
        importance = 0,
        name = "Can you show me your knife collection?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "purple_a2",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('purpleroomintro')"],
        importance = 0,
        name = "Can we switch places?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "a_tetris",
        category = DialogueAPI.category_talk,
        conditions = ['persistent.game_session >= 5'],
        importance = 0,
        name = "Hey [persistent.yuri_nickname], have you been coding anything while I'm away?",
        sub_category = "[persistent.yuri_nickname]'s World"))

    add_dialogue(Dialogue(
        label = "a_hdy_statue",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('hdy_statue_greeting')"],
        importance = 0,
        name = "Hey [persistent.yuri_nickname], can you take the hdy plushie?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "a_halloween_cupcake",
        category = DialogueAPI.category_talk,
        conditions = ['persistent.ouija_done'],
        importance = 0,
        name = "Hey [persistent.yuri_nickname], can you take the cupcake?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "Roomchange",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('a20')"],
        importance = 0,
        name = "Can you change the room?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "Halloween_2021",
        category = DialogueAPI.category_talk,
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
        label = "potion_mixing",
        category = DialogueAPI.category_talk,
        conditions = ["persistent.bg == 'laboratory'"],
        importance = 0,
        name = "How about we mix some 'potions'?",
        sub_category = "Misc."))

    add_dialogue(Dialogue(
        label = "table_items",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('table_organization')"],
        importance = 0,
        name = "Can I reorganize the table [persistent.yuri_nickname]?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "diffuser_mist_enable",
        category = DialogueAPI.category_talk,
        conditions = ['persistent.diffuser_is_enabled'],
        importance = 0,
        name = "Could you turn on the diffuser [persistent.yuri_nickname]?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "diffuser_mist_disable",
        category = DialogueAPI.category_talk,
        conditions = ['persistent.sandalwood_oil_mist_is_enabled or persistent.lavenderO_mist_is_enabled or persistent.sweet_dream_oil_mist_is_enabled'],
        importance = 0,
        name = "Could you turn off the diffuser [persistent.yuri_nickname]?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "gifting_revamp",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('gifting_intro')"],
        importance = 0,
        name = "I have a gift for you [persistent.yuri_nickname]!",
        sub_category = "Love"))

    add_dialogue(Dialogue(
        label = "gifting_ideas",
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('gifting_intro')"],
        importance = 0,
        name = "Anything specific you wanted [persistent.yuri_nickname]?",
        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "sleepy_yuri",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "I'm tired [persistent.yuri_nickname]...",
        sub_category = "Requests"))

#    add_dialogue(Dialogue(
#        label = "AFK_[persistent.yuri_nickname]",
#        category = DialogueAPI.category_talk,
#        conditions = [],
#        importance = 0,
#        name = "I need to go do something [persistent.yuri_nickname]",
#        sub_category = "Requests"))

    add_dialogue(Dialogue(
        label = "webcam",
        category = DialogueAPI.category_talk,
        conditions = [],
        importance = 0,
        name = "About the webcam access...",
        sub_category = "Awkward Topics"))

    add_dialogue(Dialogue(
        label = "nnn",
        category = DialogueAPI.category_talk,
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
        category = DialogueAPI.category_talk,
        conditions = ["renpy.seen_label('vday_2024_revisit')"],
        importance = 0,
        name = "I'm ready to revisit the chocolate moment.",
        sub_category = "Love"))



    #add_dialogue(Dialogue(
    #    label = "krampuslore",
    #    category = DialogueAPI.category_talk,
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
        category = DialogueAPI.category_greetings,
        conditions = ["time_tracker_start()", "not renpy.seen_label('TimeCheat3')", "not renpy.seen_label('TimeCheat2')", "not renpy.seen_label('TimeCheat1')"],
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "TimeCheat2",
        category = DialogueAPI.category_greetings,
        conditions = ["time_tracker_start()", "not renpy.seen_label('TimeCheat3')", "not renpy.seen_label('TimeCheat2')", "renpy.seen_label('TimeCheat1')"],
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "TimeCheat3",
        category = DialogueAPI.category_greetings,
        conditions = ["time_tracker_start()", "not renpy.seen_label('TimeCheat3')", "renpy.seen_label('TimeCheat2')", "renpy.seen_label('TimeCheat1')"],
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "TimeCheat_error",
        category = DialogueAPI.category_greetings,
        conditions = ["time_tracker_start()", "renpy.seen_label('TimeCheat3')", "renpy.seen_label('TimeCheat2')", "renpy.seen_label('TimeCheat1')"],
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "ch30_reload_0",
        category = DialogueAPI.category_greetings,
        conditions = ['time_tracker_start() == False', 'persistent.game_session == 1'],
        importance = 0,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "ch30_reload_1",
        category = DialogueAPI.category_greetings,
        conditions = ['time_tracker_start() == False', 'persistent.game_session == 2'],
        importance = 0,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "ch30_reload_2",
        category = DialogueAPI.category_greetings,
        conditions = ['time_tracker_start() == False', 'persistent.game_session == 3'],
        importance = 0,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "ch30_reload_3",
        category = DialogueAPI.category_greetings,
        conditions = ['time_tracker_start() == False', 'persistent.game_session == 4'],
        importance = 0,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "featuregreetings",
        category = DialogueAPI.category_greetings,
        conditions = ['time_tracker_start() == False', 'persistent.game_session == 5 or persistent.game_session == 6'],
        importance = 0,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "ch30_reload_4",
        category = DialogueAPI.category_greetings,
        conditions = ['time_tracker_start() == False', 'persistent.game_session >= 8'],
        importance = 0,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "highkarinsrestart",
        category = DialogueAPI.category_greetings,
        conditions = ['time_tracker_start() == False', "check_memory('complements', 'highkarinsrestart')"],
        importance = 0,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "patheticcry",
        category = DialogueAPI.category_greetings,
        conditions = ['time_tracker_start() == False', "check_memory('complements', 'patheticcry')"],
        importance = 2,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "hdy_statue_greeting",
        category = DialogueAPI.category_greetings,
        conditions = ['time_tracker_start() == False', "not renpy.seen_label('hdy_statue_greeting')", "renpy.seen_label('hdy_has_been_seen')"],
        importance = 0,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "intro_mods",
        category = DialogueAPI.category_greetings,
        conditions = ['time_tracker_start() == False', "renpy.seen_label('ch30_intro2')", "not renpy.seen_label('startup_mods')", 'persistent.game_session >= 7'],
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "purpleroomintro",
        category = DialogueAPI.category_greetings,
        conditions = ["time_tracker_start() == False", "persistent.purpleroom", "renpy.seen_label('idle_30')", "karma_lvl()=5", "persistent.lovecheck", "persistent.game_session >= 20"],
        importance = 0,
        name = "None",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "vday_2024_revisit",
        category = DialogueAPI.category_greetings,
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
        label = "krampusnacht",
        category = DialogueAPI.category_greetings,
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
        label = "birthdaycake_2020_late",
        category = DialogueAPI.category_talk,
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
        label = "birthday_gift_2021",
        category = DialogueAPI.category_talk,
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
        label = "new_year_2021",
        category = DialogueAPI.category_greetings,
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
        label = "vday_choco_date_request",
        category = DialogueAPI.category_talk,
        conditions = ["""time_interval_check(
            {'month': 2,
                'day': 13},
            {'month': 2,
                'day': 20}
            )""",
            "renpy.seen_label('valentines')",
            "karma_lvl()>3"],
        importance = 0,
        name = "Anything special planned today, [persistent.yuri_nickname]?",
        sub_category = "Love"))
    add_dialogue(Dialogue(
        label = "valentines",
        category = DialogueAPI.category_talk,
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
        print_debug(hello)

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
        print_debug(hello)

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
        print_debug(hello)

    ########

    add_dialogue(Dialogue(
        label = "birthday_chocolate",
        category = DialogueAPI.category_greetings,
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
        label = "birthday_greeting_text",
        category = DialogueAPI.category_greetings,
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
        label = "a26_prelude",
        category = DialogueAPI.category_greetings,
        conditions = ["not renpy.seen_label('a26')", "persistent.lovecheck", "karma_lvl() > 3 and sanity_lvl() > 3"], #add requirement for 3 weeks of time
        importance = 8,
        name = "None",
        sub_category = None))
####
#FAREWELLS
####
#Characterized by them automatically playing at ends of game

    add_dialogue(Dialogue(
        label = "farewell_1",
        category = DialogueAPI.category_goodbye,
        conditions = [],
        importance = 0,
        name = "Goodbye, [persistent.yuri_nickname]!",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "farewell_2",
        category = DialogueAPI.category_goodbye,
        conditions = [],
        importance = 0,
        name = "Sorry, gotta go...",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "farewell_3",
        category = DialogueAPI.category_goodbye,
        conditions = [],
        importance = 0,
        name = "I'll see you later, [persistent.yuri_nickname].",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "farewell_4",
        category = DialogueAPI.category_goodbye,
        conditions = [],
        importance = 0,
        name = "Bye, [persistent.yuri_nickname], I'll miss you!",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "farewell_5",
        category = DialogueAPI.category_goodbye,
        conditions = [],
        importance = 0,
        name = "Sorry I can't stay. I love you!",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "farewell_6",
        category = DialogueAPI.category_goodbye,
        conditions = ['sanity == 2'],
        importance = 0,
        name = "Oh, hey, look at the time, this has been an awesome date!",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "farewell_7",
        category = DialogueAPI.category_goodbye,
        conditions = ['karma_lvl() == 2 or karma_lvl() == 1'],
        importance = 0,
        name = "Oh, whoops, someone's calling me, gotta run!",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "farewell_8",
        category = DialogueAPI.category_goodbye,
        conditions = ['sanity == 2'],
        importance = 0,
        name = "I have food... in the oven so...",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "farewell_9",
        category = DialogueAPI.category_goodbye,
        conditions = ['sanity_lvl() <= 2'],
        importance = 0,
        name = "I, uh, gotta go...",
        sub_category = None))

#missing farewell_9

    add_dialogue(Dialogue(
        label = "farewell_10",
        category = DialogueAPI.category_goodbye,
        conditions = ['sanity_lvl() == 2'],
        importance = 0,
        name = "I'm just going to... close the game now, okay?",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "farewell_11",
        category = DialogueAPI.category_goodbye,
        conditions = ['karma_lvl() >= 4'],
        importance = 0,
        name = "So long, farewell!",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "farewell_12",
        category = DialogueAPI.category_goodbye,
        conditions = ['karma_lvl() >= 4'],
        importance = 0,
        name = "I have to go. I already miss you!",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "farewell_13",
        category = DialogueAPI.category_goodbye,
        conditions = [],
        importance = 0,
        name = "I have to go now... I'll talk to you later, alright?",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "farewell_14",
        category = DialogueAPI.category_goodbye,
        conditions = [],
        importance = 0,
        name = "See you later!",
        sub_category = None))


    add_dialogue(Dialogue(
        label = "farewell_15",
        category = DialogueAPI.category_goodbye,
        conditions = [],
        importance = 0,
        name = "I hate having to put you through this, but it looks like it's time to say goodbye once again.",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "farewell_16",
        category = DialogueAPI.category_goodbye,
        conditions = [],
        importance = 0,
        name = "I have to go now, my love.",
        sub_category = None))

    add_dialogue(Dialogue(
        label = "farewell_17",
        category = DialogueAPI.category_goodbye,
        conditions = [],
        importance = 0,
        name = "Whatever happens, just remember that there is someone who loves you no matter what.",
        sub_category = None))

#####
#Hot Dog Yuri
####
#Characterized by being played while the player has HDY enabled.

    add_dialogue(Dialogue(
        label = 'HDY_eggnomancer',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_spookyscaryskeleton',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Alien_Friend',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_wallpaper',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Potionseller',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_teleported_hotdogs',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Sausage_mouth',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_philosophy',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_whyarewestillhere',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_frozen_cooking_eggs',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Hellskitchen',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_minion',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_airfryer',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Eternal',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Friedsweets',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Manga',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_War',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Inquisition',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Buns',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Witches',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Rocks',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Orangana',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Skinny',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_mum',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_frostless',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_PPAP',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_fuckingPlayer',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_why',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_portal',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_a',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_speen',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_crash',
        category = DialogueAPI.category_hdy,
        conditions = ["not renpy.seen_label('HDY_crash')", "renpy.seen_label('hdy_statue_geeting')"],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_mcspaghetti',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_fortnitecard',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_WordOfTheDay',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_8800bluelickroad',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_DarthPlagueis',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_violence',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_society',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_discordserver',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_sand',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_SithLords',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_fortnitegamer',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_replacementpog',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_passtime',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_dababy',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_jevil',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_getdawged',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_familyguy',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_nukes',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_shrek',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_sans',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_beemovie',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_lifeadvice',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_morshu',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_toughdawg',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_banana',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_pingas',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_electricity',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_swag',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_hmmmm',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_censorship',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_amogus',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_deadmeme',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_h',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_callout',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_movie',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_scottthewozz',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_windowsphone',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_DDR',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_bottomtext',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_favoritegame',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_ifunny',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_chubbyemu',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_brrrrrrr',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_thisaccountisnotfortheaverageman',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_chubbyemu2',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_searchhistory',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_youngsterjoey',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_100',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Chugjug',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_truth',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_MeMEbigboy',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_MakingHotdogs',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_jesusboxing',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_cthulhu',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_paydaygang',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_bluedabadee',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_cranberrysprite',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_amongus',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_rickroll',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_holdingbreath',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_sixtynine',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_acesleeve',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_wonderwall',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Hotdogspoem',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_eggnomancer',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_hotdogfact',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_lifeadvice2electricboogaloo',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_hotdogtea',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_areyounotentertained',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_wakeup',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_asadstory',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_scatman',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_tank',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_tankcommander',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Hbomb',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_spacedandy',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_it_was_me_dio',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Monkeys',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_WaspInTheRoom',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_AUSTRALIA',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Wasp',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_bald',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Dating',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_Space',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_gasstation',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_thebigquestion',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_somethingidunno',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_peepy',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))

    add_dialogue(Dialogue(
        label = 'HDY_kiss',
        category = DialogueAPI.category_hdy,
        conditions = [],
        importance = 0,
        name = None,
        sub_category = None))
