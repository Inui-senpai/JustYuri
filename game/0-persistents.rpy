#==================================================#
#  Just Yuri Mod - Persistents
#==================================================#
#  This file contains all default values for the
#  persistent file.
#==================================================#

#==================================================#
# Base Variables
#==================================================#
default persistent.first_run = False
default persistent.seen_poem_raccoon = False
default persistent.playername = ""
default persistent.stutter_player = ""
default persistent.stutter_yuri = ""
default persistent.steam = ("steamapps" in config.basedir.lower())
default persistent.playthrough = 0
default persistent.yuri_kill = False
default persistent.seen_eyes = None
default persistent.seen_sticker = None
default persistent.ghost_menu = None
default persistent.seen_ghost_menu = None
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
default persistent.special_poems = None
default persistent.clearall = None
default persistent.menu_bg_m = None
default persistent.first_load = None
default persistent.first_poem = None
default persistent.seen_colors_poem = None
default persistent.monika_back = None
default persistent.HDY = False
default persistent.seen_halloween_no = False
default persistent.ouija_done = False
default persistent.book = False
default persistent.demo = False
default persistent.autoload = None

#==================================================#
# Dialogue Variables
#==================================================#
default persistent.memory = {}

#==================================================#
# Functional Variables
#==================================================#
default persistent.hdy_statue_is_enabled = False
default persistent.halloween_cupcake_is_enabled = False
default persistent.diffuser_is_enabled = False
default persistent.diffuser_mist_is_enabled = False
default persistent.lavender_o_is_enabled = None
default persistent.lavenderO_mist_is_enabled = False
default persistent.sandalwood_oil_is_enabled = None
default persistent.sandalwood_oil_mist_is_enabled = False
default persistent.sweet_dream_oil_is_enabled = None
default persistent.sweet_dream_oil_mist_is_enabled = False
default persistent.hershey_is_enabled = None
default persistent.lavenderC_is_enabled = None
default persistent.mint_is_enabled = None
default persistent.roseO_is_enabled = False
default persistent.raccoon_is_enabled = False
default persistent.bunnyO_is_enabled = False
default persistent.craneO_is_enabled = False
default persistent.ingame_time = datetime.timedelta(0)
default persistent.sleepy_yuri_is_enabled = False
default persistent.yuri_nickname = "Yuri"
default persistent.chibi_topic = 0
default persistent.monika_first = True
default persistent.eyecolor = "other"
default persistent.yuriidles = []
default persistent.yuri_reload = 0
default persistent.tried_skip = None
default persistent.monika_kill = None
default persistent.buttonvar = False
default persistent.gift_given = False
default persistent.current_yuriidle = 0
default persistent.room_items = ["nothing"] * 10
default persistent.costume = "school"
default persistent.previous_costume = None
default persistent.face1 = "nothing"
default persistent.face2 = "nothing"
default persistent.head1 = "nothing"
default persistent.head2 = "nothing"
default persistent.hairstyle = "default"
default persistent.game_session = None

#==================================================#
# Karma/Sanity Variables
#==================================================#
default persistent.lovecheck = False
default persistent.karma_points = None
default persistent.sanity_points = None

#==================================================#
# Tetris Variables
#==================================================#
default persistent.tetris_first = True
default persistent.best_co_op_tetris_score = 0
default persistent.skin = 0

#==================================================#
# Timecycle/Room Variables
#==================================================#
default persistent.bg = "space"
default persistent.marker = None
default persistent.previous_time = None

#==================================================#
# Boop Variables
#==================================================#
default persistent.boop = 0
default persistent.boop_locations = [0.] * 12

#==================================================#
# Date/Dream Variables
#==================================================#
default persistent.dates_taken = 0

#==================================================#
# Music Variables
#==================================================#
default persistent.custom_music = None

#==================================================#
# Screen Variables
#==================================================#
default persistent.idle_frequency_factor = 1
default persistent.high_gpu = 1

#==================================================#
# Script Variables
#==================================================#
default persistent.cake = "choco_candles"
default persistent.misclick = 0
default persistent.insult_counter = 0
default persistent.hobbies = {}
default persistent.bday_month = "1"
default persistent.bday_day = "1"
default persistent.saved_costume = None
default persistent.mod_count = 0

#==================================================#
# Unused Variables
#==================================================#
default persistent.alpha_save = None
default persistent.insanity_points = None
default persistent.temp_memory = None