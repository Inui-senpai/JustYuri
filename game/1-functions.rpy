#Currently in the process of making these functions to replace the mess located in classes.rpy
###################
#DEFAULT VARIABLES#
###################
define time_tracker = None
default torso_costume2 = "nothing"
#Sort these... like soon. Now-ish if possible.
default currentpos = 0
default face_mask = "nothing"
default face_mask_2 = "nothing"
default faint_effect = None
default repeat_dialogue_ask = False
default loop_again = False
default hide_yuri_sit = False
default hide_yuri_sleep = True
#Quick additions for the button addition on the Preferences screen. #Courtesy of Terra#2060

default mouse_move_dict = {
    "A":[265, 360],
    "B":[335, 320],
    "C":[395, 300],
    "D":[455, 280],
    "E":[515, 265],
    "F":[574, 260],
    "G":[630, 255],
    "H":[695, 260],
    "I":[750, 270],
    "J":[790, 275],
    "K":[860, 295],
    "L":[925, 320],
    "M":[985, 350],
    "N":[280, 480],
    "O":[330, 440],
    "P":[385, 410],
    "Q":[440, 385],
    "R":[500, 370],
    "S":[565, 355],
    "T":[620, 350],
    "U":[685, 355],
    "V":[750, 360],
    "W":[815, 385],
    "X":[885, 410],
    "Y":[935, 440],
    "Z":[990, 480],
    "1":[375, 530],
    "2":[420, 530],
    "3":[480, 530],
    "4":[530, 530],
    "5":[600, 530],
    "6":[660, 530],
    "7":[715, 530],
    "8":[770, 530],
    "9":[830, 530],
    "0":[890, 530],
    "YES":[375, 130],
    "NO":[895,130],
    "SUN":[225,125],
    "MOON":[1035,130],
    "EYE":[630,135]}

#Dialogue specific variables (Used to control dialogue, tie to activation requirements later)
default philosophy = True

#Yuri Sprite Variables
default default_yuri_dict = {#base, face1, face2, head1, head2, hands, eyebrows, blush, cry, eyes, mouth
    0:"base",
    1:"nothing",
    2:"nothing",
    3:"nothing",
    4:"nothing",
    5:"chest_arm",
    6:"eyebrows_b",
    7:"nothing",
    8:"nothing",
    9:"eyes_0",
    10:"mouth_b"}
default special_costume = ""
default costume = persistent.costume
default yuri_state = {
    "head_pos": "front",
    "eyes": "",
    "eyes_alpha": "",
    "eyes_beta": "",
    "mouth": "",
    "eyebrows": "",
    "head_cover_1": "",
    "head_cover_2": "",

    "backarms_behind_desk": False,
    "downarm_left": "",
    "uparm_left": "",
    "downarm_right": "",
    "uparm_right": "",
    "downarm_both": "",

    "held_object_1": "banner_space",

    "downarm_left_costume": "",
    "uparm_left_costume": "",
    "downarm_right_costume": "",
    "uparm_right_costume": "",
    "downarm_both_costume": ""
}

#KS Variables
default temp_sanity = 0 #temporary sanity booster, resets on each new play session.
default temp_karma = 0
default ks_variance = 15 #ks_variance is the variation within her points (She sometimes doesn't stay within her level on each reading.)
default number_of_lvls = float(5)
default points_per_level = float(40)
default max_points = float(100)

###########
#FUNCTIONS#
###########

init -998 python:
    import rstr
    import random
    import re
#eyebrow variations complete
#default eyebrows = "eyebrows_b"
#default hands = "chest_arm"
#default eyes = "eyes_0"
#default mouth = "mouth_a"
#default blush = "nothing" #"blush"
#default cry = "nothing" #"cry" or "cry_yandere"
#old 5 characters for example Aa-A0a or 5 character + bases for example Aa-A0a|[base,face1,face2,head1,head2]
    def base64_to_index(character):
        string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
        return string.find(character)

    def base64_to_letter(character):
        return character.lower()

    def yuri_say(regex, condition = None):
        if condition is None or condition:
            y(rstr.xeger(regex))


    def default_yuri():
        #default_ks_dict = {
        #}
        if karma() == 1 and sanity() == 1:
            show_chr("A-NFCAA-ANAG")
        elif karma() == 1 and sanity() == 2:
            show_chr("A-HECAA-AEAB")
        elif karma() == 1 and sanity() == 3:
            show_chr("A-CFCAA-AAAA")
        elif karma() == 1 and sanity() == 4:
            show_chr("A-BFBAA-AEAB")
        elif karma() == 1 and sanity() == 5:
            show_chr("A-CEBAA-AEAB")
        elif karma() == 2 and sanity() == 1:
            show_chr("A-DGFAA-ABAB")
        elif karma() == 2 and sanity() == 2:
            show_chr("A-AFFAA-ABAB")
        elif karma() == 2 and sanity() == 3:
            show_chr("A-KFCAA-ABAB")
        elif karma() == 2 and sanity() == 4:
            show_chr("A-AEAAA-ABAB")
        elif karma() == 2 and sanity() == 5:
            show_chr("A-AFAAA-ABAB")
        elif karma() == 3 and sanity() == 1:
            show_chr("A-CFGAA-AIAI")
        elif karma() == 3 and sanity() == 2:
            show_chr("A-IFBAA-ALAA")
        elif karma() == 3 and sanity() == 3:
            show_chr("A-AFBAA-ALAA")
        elif karma() == 3 and sanity() == 4:
            show_chr("A-AFAAA-AAAA")
        elif karma() == 3 and sanity() == 5:
            show_chr("A-AAAAA-AAAA")
        elif karma() == 4 and sanity() == 1:
            show_chr("A-DABAA-ABAB")
        elif karma() == 4 and sanity() == 2:
            show_chr("A-DAAAA-ABAB")
        elif karma() == 4 and sanity() == 3:
            show_chr("A-GCBAA-AEAB")
        elif karma() == 4 and sanity() == 4:
            show_chr("A-BCAAA-ABAB")
        elif karma() == 4 and sanity() == 5:
            show_chr("A-AAAAA-ABAB")
        elif karma() == 5 and sanity() == 1:
            show_chr("A-HABBA-ABAB")
        elif karma() == 5 and sanity() == 2:
            show_chr("A-HAAAA-ABAB")
        elif karma() == 5 and sanity() == 3:
            show_chr("A-AAAAA-ABAB")
        elif karma() == 5 and sanity() == 4:
            show_chr("A-AAAAA-ALAL")
        elif karma() == 5 and sanity() == 5:
            show_chr("A-AABAA-ALAL")
        if karma() and sanity() == 5 and persistent.lovecheck:
            show_chr("A-CABBA-ALAL")
        if karma() and sanity() == 5 and persistent.lovecheck and persistent.yuri_nickname == "Lily":
            show_chr("A-CABBA-AMAM")
        if karma() and sanity() == 5 and persistent.yuri_nickname == "Lily":
            show_chr("A-AABAA-AMAM")

    class yuri_display():

        values = {
            "position": "sit",
            "head": "front",
            "eyes": 0,
            "mouth": "a",
            "eyebrows": "a",
            "blush": False,
            "cry": False,
            "both arms": 0,
            "left arm": 0,
            "right arm": 0
        }

        @staticmethod
        def position(index):
            position = ["sit", "stand"]
            yuri_display.values["position"] = position[index]
            return yuri_display

        @staticmethod
        def head(index):
            head = ["front", "down", "side"]
            yuri_display.values["head"] = head[index]
            return yuri_display

        @staticmethod
        def eyes(index):
            yuri_display.values["eyes"] = index
            return yuri_display

        @staticmethod
        def mouth(index):
            mouth = "abcdefghijkl"
            yuri_display.values["mouth"] = mouth[index]
            return yuri_display

        @staticmethod
        def eyebrows(index):
            eyebrows = "abcdefg"
            yuri_display.values["eyebrows"] = eyebrows[index]
            return yuri_display

        @staticmethod
        def blush(bool):
            yuri_display.values["blush"] = bool
            return yuri_display

        @staticmethod
        def cry(bool):
            yuri_display.values["cry"] = bool
            return yuri_display

        @staticmethod
        def arms(index):
            yuri_display.values["both arms"] = index
            return yuri_display

        @staticmethod
        def arms(index1, index2):
            yuri_display.values["left arm"] = index1
            yuri_display.values["right arm"] = index2
            return yuri_display

        @staticmethod
        def reset():
            yuri_display.values = {
                "position": "sit",
                "head": "front",
                "eyes": 0,
                "mouth": "a",
                "eyebrows": "a",
                "blush": False,
                "cry": False,
                "both arms": 0,
                "left arm": 0,
                "right arm": 0
            }
            return yuri_display

        @staticmethod
        def show():
            global sprite_type
            global yuri_sit
            global yuri_stand
            global yuri_state
            global yuri_sleep
            global activated
            #costume
            if renpy.has_image("torso_" + persistent.costume + "_day") or renpy.has_image("torso_" + persistent.costume):
                torso_costume = "torso_" + persistent.costume
            else:
                torso_costume = "nothing"

            #special eyes
            eyes = "eyes_" + str(yuri_display.values["eyes"]) + "_" + yuri_display.values["head"]
            if eyes == "eyes_13_front": #special case
                eyes = "eyes_12_front"
                eyes_alpha = "yuri_sit_eyes_standard"
                eyes_beta = "insanepupils"
            elif yuri_display.values["head"] == "front": #if the eyes are facing forward
                if yuri_display.values["eyes"] in [0, 3, 7, 8, 9]:
                    eyes_alpha = "yuri_sit_blink_1"
                elif yuri_display.values["eyes"] in [1, 4, 5, 10]:
                    eyes_alpha = "yuri_sit_blink_2"
                else:
                    eyes_alpha = "yuri_sit_eyes_standard"
                eyes_beta = "nothing"
            else: #if the eyes are not facing forward (probably to the side.)
                eyes_alpha = "yuri_sit_eyes_standard"
                eyes_beta = "nothing"

            #mouth
            mouth = "mouth_" + yuri_display.values["mouth"] + "_" + yuri_display.values["head"]

            #eyebrows
            eyebrows = "eyebrows_" + yuri_display.values["eyebrows"] + "_" + yuri_display.values["head"]

            #blush
            if yuri_display.values["blush"]:
                head_cover_1 = "blush" + "_" + str(yuri_display.values["head"])
            else:
                head_cover_1 = "nothing"

            #cry
            if yuri_display.values["cry"]:
                tears_type = ["open","open","closed","open","squint","squint","happy","open","open","open","squint","open","open","open"]
                if yuri_display.values["eyes"] >= 0 and yuri_display.values["eyes"] < len(tears_type):
                    head_cover_2 = tears_type[yuri_display.values["eyes"]] + "-eyes-crying"
                else:
                    head_cover_2 = "open-eyes-crying"
            else:
                head_cover_2 = "nothing"

            #up arms
            uparms_exist = False
            downarm_both = ""
            uparm_both = ""
            downarm_left = ""
            uparm_left = ""
            downarm_right = ""
            uparm_right = ""
            if yuri_display.values["both arms"]:
                downarm_both = "downarm_both_arms_" + str(yuri_display.values["both arms"])
                #if the following both arms has up arms already implemented in down arms
                if yuri_display.values["both arms"] == 2:
                    uparms_exist = True
                else:
                    uparm_both = "uparm_both_1"
            else:
                downarm_left = "downarm_left_" + str(yuri_display.values["left arm"])
                uparm_left = "uparm_left_0"
                downarm_right = "downarm_right_" + str(yuri_display.values["right arm"])
                uparm_right = "uparm_right_0"

            #arms behind table
            leftdownarmbehind = True
            rightdownarmbehind = True
            if yuri_display.values["left arm"] in [5, 6, 7, 11, 12, 15, 18]:
                leftdownarmbehind = False
            if yuri_display.values["right arm"] in [5, 6, 7, 11, 12, 15, 18]:
                rightdownarmbehind = False

            #arms costume
            downarm_left_costume = ""
            uparm_left_costume = "uparm_left_0_" + persistent.costume
            downarm_right_costume = ""
            uparm_right_costume = "uparm_right_0_" + persistent.costume
            downarm_both_costume = ""
            uparm_both_costume = "uparm_both_0_" + persistent.costume

            if yuri_display.values["both arms"]:
                downarm_both_costume = downarm_both + "_" + persistent.costume
            else:
                downarm_left_costume = downarm_left + "_" + persistent.costume
                downarm_right_costume = downarm_right + "_" + persistent.costume


            #book
            book = ""
            if downarm_both and yuri_display.values["both arms"] == 1:
                book = "book1"
            elif downarm_both and yuri_display.values["both arms"] == 2:
                book = "book2"

            #check position
            if yuri_display.values["position"] == "sit":
                #yuri_sit = [head, [eyes, eyes_alpha, eyes_beta], mouth, eyebrows, head_cover_1, head_cover_2, uparm_left, downarm_left, uparm_right, downarm_right, torso_costume, uparm_left_costume, downarm_left_costume, uparm_right_costume, downarm_right_costume, downarm_both, book, leftdownarmbehind, rightdownarmbehind]
                yuri_sit = {
                    "head": yuri_display.values["head"],
                    "eyes": [
                        eyes,
                        eyes_alpha,
                        eyes_beta
                    ],
                    "mouth": mouth,
                    "eyebrows": eyebrows,
                    "head_cover_1": head_cover_1,
                    "head_cover_2": head_cover_2,
                    "arms": {
                        "both": {
                            "down": downarm_both,
                            "costume": {
                                "down": downarm_both_costume
                            },
                            "has_up_arms": uparms_exist
                        },
                        "left": {
                            "isBehind": leftdownarmbehind,
                            "up": uparm_left,
                            "down": downarm_left,
                            "costume": {
                                "up": uparm_left_costume,
                                "down": downarm_left_costume
                            }
                        },
                        "right": {
                            "isBehind": rightdownarmbehind,
                            "up": uparm_right,
                            "down": downarm_right,
                            "costume": {
                                "up": uparm_right_costume,
                                "down": downarm_right_costume
                            }
                        }
                    },
                    "torso": {
                        "costume": torso_costume
                    },
                    "extras": {
                        "book": book
                    }
                }
                renpy.show_screen("yuri_sit")
                #renpy.show("yuri_sit", zorder = 11)#, at_list = position, zorder = 11)
            elif yuri_display.values["position"] == "stand":
                torso_costume = "nothing"
                yuri_stand = [
                    yuri_display.values["head"],
                    eyes,
                    mouth,
                    eyebrows,
                    head_cover_1,
                    head_cover_2,
                    uparm_left,
                    downarm_left,
                    uparm_right,
                    downarm_right,
                    torso_costume,
                    uparm_left_costume,
                    downarm_left_costume,
                    uparm_right_costume,
                    downarm_right_costume
                ]
                position_list = ""
                for element in ["t11"]:
                    position_list += element + ","
                position_list = position_list[:-1]
                exec('renpy.show("yuri_stand", at_list = [' + position_list + '], zorder = 12)')#at_list = position, zorder = 12)
            return yuri_display

    def show_chr(expression, chr = "yuri_sit", position = ["t11"]):#Head-eye,mouth,eyebrow,blush,cry-Larmup, Larmdown, Rarmup, Larmdown
    #Note TO SELF, FUCKING RETOOL THIS WHOLE FUCKING THING. Post-Valentines is replacement of all code time.
        global sprite_type
        global yuri_sit
        global yuri_sleep
        global yuri_stand
        global yuri_state
        global torso_costume2

        """
        #Defaults
        head = "front"
        eyes = "eyes_0_front"
        mouth = "mouth_a_front"
        eyebrows = "eyebrows_b_front"
        blush = "nothing"
        cry = "nothing"
        uparm_left = "uparm_left_a"
        downarm_left = "downarm_left_1"
        uparm_right = "uparm_right_a"
        downarm_right = "downarm_right_1"
        """
        if expression == "default":
            default_yuri()
            return

        # If head position is not given, for example, AAAAA-AAAA.
        if(expression.count('-') == 1):
            expression = 'A-' + expression

        if(list(map(lambda x: len(x), expression.split('-'))) != [1, 5, 4]):
            expression = "A-AAAAA-AAAA"

        #0 Head Position
        if expression[0] == "A":
            head = "front"
        elif expression[0] == "B":
            head = "side"

        #2 Eyes
        #eyes_alpha - back layer of her blink
        #eyes_beta - front layer of her blink (usually for the insane pupils to move around mostly)
        eyes = "eyes_" + str(base64_to_index(expression[2])) + "_" + head
        if eyes == "eyes_13_front": #special case
            eyes = "eyes_12_front"
            eyes_alpha = "yuri_sit_eyes_standard"
            eyes_beta = "insanepupils"
        elif head == "front": #if the eyes are facing forward
            if int(base64_to_index(expression[2])) in [0, 3, 7, 8, 9]:
                eyes_alpha = "yuri_sit_blink_1"
            elif int(base64_to_index(expression[2])) in [1, 4, 5, 10]:
                eyes_alpha = "yuri_sit_blink_2"
            else:
                eyes_alpha = "yuri_sit_eyes_standard"
            eyes_beta = "nothing"
        else: #if the eyes are not facing forward (probably to the side.)
            eyes_alpha = "yuri_sit_eyes_standard"
            eyes_beta = "nothing"

        #3 Mouth
        mouth = "mouth_" + expression[3].lower() + "_" + head
        #4 Eyebrows
        eyebrows = "eyebrows_" + expression[4].lower() + "_" + head
        #5 blush
        if expression[5] == "B":
            head_cover_1 = "blush" + "_" + head
        elif expression[5] == "C":
            head_cover_1 = "sweatbead" + "_" + head
        else:
            head_cover_1 = "nothing"
        #6 cry
        express_6_dict = {
            "C": "closed",
            "E": "squint",
            "F": "squint",
            "G": "happy",
            "K": "squint"}
        if expression[6] == "B":
            if expression[2] in express_6_dict:
                head_cover_2 = express_6_dict[expression[2]] + "-eyes-crying"
            else:
                head_cover_2 = "open-eyes-crying"
        else:
            head_cover_2 = "nothing"

        #8-9 Left Arm and Hand
        botharms = False
        has_up_arms = False
        if expression[8:10] == "ZZ" and expression[10] == "A":
            botharms = True
            if expression[11] in ["B"]:#, "R"]:
                has_up_arms = True

        uparm_left = "uparm_left_" + str(base64_to_index(expression[8]))  if not botharms else "uparm_left_" + str(base64_to_index(expression[10]))
        downarm_left = "downarm_left_" + str(base64_to_index(expression[9])) if not botharms else "nothing"

        #10-11 Right Arm and Hand
        uparm_right = "uparm_right_" + str(base64_to_index(expression[10]))  #if not botharms else "nothing"
        downarm_right = "downarm_right_" + str(base64_to_index(expression[11]))  if not botharms else "nothing"

        downarm_both = "downarm_both_arms_" + str(base64_to_index(expression[11]) + 1) if botharms else ""

        #Book handling
        book = ""
        if downarm_both != "" and base64_to_index(expression[11]) + 1 == 1:
            book = "book1"
        elif downarm_both != "" and base64_to_index(expression[11]) + 1 == 2:
            book = "book2"

        #Is behind table
        leftdownarmbehind = True
        rightdownarmbehind = True
        if expression[9] in ["F", "G", "H", "L", "M", "P", "S"]: #left arm
            leftdownarmbehind = False
        if expression[11] in ["F", "G", "H", "L", "M", "P", "S"]: #right arm
            rightdownarmbehind = False
        if expression[11] == "D" and botharms:
            rightdownarmbehind = False
            leftdownarmbehind = False

        downarm_both_costume = "nothing"
        #Gonna change exec() to globals().
        #Costume Screening
        if botharms:
            #downarm_both_arms_2_school_day
            if renpy.has_image("downarm_both_arms_1_" + persistent.costume + "_day") and downarm_both != "":
                globals()['downarm_both'] = downarm_both #ask slovenly_dilettante to remove if necessary
                downarm_both_costume = globals()['downarm_both'] + '_' + persistent.costume
                #exec("downarm_both_costume = '" + downarm_both + "_" + persistent.costume + "'")
        for i in range(0, 4):
            element = ['uparm_left', 'downarm_left', 'uparm_right', 'downarm_right']
            if renpy.has_image((element[i]) + "_0_" + persistent.costume + "_day") and not botharms:
                #globals()['plug_in'] = element[i]
                #exec("plug_in = " + element)
                globals()[(element[i]) + '_costume'] = (element[i]) + '_' + str(base64_to_index(expression[8 + i])) + '_' + persistent.costume
                #exec(element + "_costume = '" + plug_in + "_" + persistent.costume + "'")
            else:
                if persistent.costume != "valentines" and  persistent.costume != "bikini":
                    globals()[(element[i]) + '_costume'] = (element[i]) + '_' + '0' + '_' + persistent.costume
                else:
                    globals()[(element[i]) + '_costume'] = 'nothing'  #slovenly_dilettante changed var nothing to string 'nothing', which should resolve
                #if i % 2 == 0: #if index is even = generate upper sleeves variable; otherwise lower sleeves
                    #globals()[(element[i]) + '_costume'] = (element[i]) + '_' + '0' + '_' + persistent.costume #slovenly_dilettante changed var nothing to string 'nothing', which should resolve
                #else:
                #    globals()[(element[i]) + '_costume'] = (element[i]) + '_' + '3' + '_' + persistent.costume
                #exec(element + "_costume = 'nothing'")
        #Because the costume arms don't align normally with the normal ones for botharms 3
        if downarm_both == "downarm_both_arms_3" and persistent.costume != "valentines":
            downarm_both = "downarm_both_arms_5"

        #Because the costume arms don't align normally with the normal ones for botharms 3
        if downarm_both == "downarm_both_arms_3" and persistent.costume != "valentines":
            downarm_both = "downarm_both_arms_5"

        #Sprite Type
        if chr == "yuri_sit":
            if renpy.has_image("torso_" + persistent.costume + "_day") or renpy.has_image("torso_" + persistent.costume):
                torso_costume = "torso_" + persistent.costume
            else:
                torso_costume = "nothing"

            #yuri_sit = [head, [eyes, eyes_alpha, eyes_beta], mouth, eyebrows, head_cover_1, head_cover_2, uparm_left, downarm_left, uparm_right, downarm_right, torso_costume, uparm_left_costume, downarm_left_costume, uparm_right_costume, downarm_right_costume, downarm_both, book, leftdownarmbehind, rightdownarmbehind]

            yuri_sit = {
                "head": head,
                "eyes": [
                    eyes,
                    eyes_alpha,
                    eyes_beta
                ],
                "mouth": mouth,
                "eyebrows": eyebrows,
                "head_cover_1": head_cover_1,
                "head_cover_2": head_cover_2,
                "arms": {
                    "both": {
                        "down": downarm_both,
                        "costume": {
                            "down": downarm_both_costume
                        },
                        "has_up_arms": has_up_arms
                    },
                    "left": {
                        "isBehind": leftdownarmbehind,
                        "up": uparm_left,
                        "down": downarm_left,
                        "costume": {
                            "up": uparm_left_costume,
                            "down": downarm_left_costume
                        }
                    },
                    "right": {
                        "isBehind": rightdownarmbehind,
                        "up": uparm_right,
                        "down": downarm_right,
                        "costume": {
                            "up": uparm_right_costume,
                            "down": downarm_right_costume
                        }
                    }
                },
                "torso": {
                    "costume": torso_costume,
                    "costume2": torso_costume2
                },
                "extras": {
                    "book": book
                }
            }
            renpy.show_screen("yuri_sit")
            #renpy.show("yuri_sit", zorder = 11)#, at_list = position, zorder = 11)
        elif chr == "yuri_stand":
            torso_costume = "nothing"

            yuri_stand = [head, eyes, mouth, eyebrows, head_cover_1, head_cover_2, uparm_left, downarm_left, uparm_right, downarm_right, torso_costume, uparm_left_costume, downarm_left_costume, uparm_right_costume, downarm_right_costume]
            jojo_reference = True
            position_list = ""
            for element in position:
                position_list += element + ","
            position_list = position_list[:-1]
            renpy.show('yuri_stand', at_list = position, zorder = 12)
            #exec('renpy.show("yuri_stand", at_list = [' + position_list + '], zorder = 12)')#at_list = position, zorder = 12)
        else:
            return

    def show_hdy(new_hdy_image):
        global old_hdy_image

        if old_hdy_image != None:
            renpy.hide(old_hdy_image)
        if new_hdy_image != None:
            renpy.show(new_hdy_image, zorder = 100)
        old_hdy_image = new_hdy_image

    def randomplayername():
        names = [
            'Josh',
            'Ryan',
            'Megan',
            'Kathy',
            'Steve',
            'Brian',
            'Waldo',
            'Weege',
            'Nail',
            'Creg',
            'Dan',
            'Board',
            'JoJo',
            'Bucket',
            'Juan',
            'DIO',
            'John',
            'Oleg',
            'Dandy',
            'Bitch Tits Megee',
            '[Name Missing]',
            'Arial size 12',
            'Cornelius',
            'Link',
            'Morshu',
            'Rick Roll',
            'Trump - no wait',
            'Esteban',
            'Pepe',
            'lemur',
            'Bartholomew',
            'what' + "'" + 's your name again',
            'Timothy',
            'SANS',
            'Another original name',
            'Times new roman 14',
            'Alecksander',
            'NameNotFoundException',
            'kiddo',
            'Keyboard smash',
            'monikammmmmmmmm',
            '<Name>',
            'Putin',
            'Evergreen boat',
            'Slavyori',
            'Bakuretsu',
            'Zuckerberg',
            'Shrek',
            'Trollface',
            'Impostor',
            'ValueError: Failed to recognize str',
            'PlayerNameValue',
            'Dalek',
            'Cabos',
            'Sheila',
            'Bagel',
            'Chorch',
            'Mestr chof',
            'Orbitr',
            'Sgt. Jensen',
            'Loopenzio',
            'Viktor',
            'Sorge',
            'Envy',
            'iulaerhguñlearhn',
            'Scott the Wozz',
            'Gopher',
            'Obi Wan Kenobi',
            'Waluigi'
            ]

        return random.choice(names)


    ####################################
    #UNARCHIVE AND FILE COMPARISON CODE#
    ####################################
    def isValidFile(path):
        return not regex.match("\.DS_Store$", path) and not regex.match("thumbs\.db$", path)
    # Unpacks a directory within the game folder or in .rpa files
    def unpack(directory, new_directory):
        # directory: Location relative to the game folder
        # new_directory: path relative to the base directory
        n_dir = os.path.join(config.basedir, new_directory)
        if not os.path.exists(n_dir):
            os.makedirs(n_dir)

        from shutil import copyfileobj
        for path in paths.all:
            if directory in path:
                file_path = path.replace(directory + "/", "", 1).replace("/", os.sep)
                file_dir = os.path.join(n_dir, regex.sub("[/]*[^/]*$", "", file_path.replace(os.sep, "/")).replace("/", os.sep))
                if not isValidFile(file_path):
                    continue
                with renpy.open_file(path) as file:
                    file_result = os.path.join(n_dir,  file_path)
                    if not os.path.exists(file_dir):
                        os.makedirs(file_dir)
                    with open(file_result, "wb") as new_file:
                        copyfileobj(file, new_file)

    def unarchive(original_filename, new_filename):
        # original_filename is the name the file has when stored in the archive, including any
        # leading paths.

        # new_filename is the name the file will have when extracted, relative to the base directory.

        import os
        import os.path

        new_filename = config.basedir + "/" + new_filename
        dirname = os.path.dirname(new_filename)

        if not os.path.exists(dirname):
            os.makedirs(dirname)

        orig = renpy.file(original_filename)
        new = open(new_filename, "wb")

        from shutil import copyfileobj
        copyfileobj(orig, new)

        new.close()
        orig.close()

    def file_detect(scan_folder="characters", target_folder="images/gifts", target_filename = "fuckyou.png"): #unarchive likes /, filecmp likes \\
        import os
        import filecmp
        if not renpy.exists("game\\" + target_filename):
            unarchive(target_folder + "/" + target_filename, "game/" + target_filename)
        is_file_found = False
        for file in os.listdir(config.basedir + "\\" + scan_folder):
            if filecmp.cmp(config.basedir + "\\" + scan_folder + "\\" + file, config.basedir + "\\game\\" + target_filename):
                is_file_found = True
        os.remove(config.basedir + "\\game\\" + target_filename)
        return is_file_found

    def file_detect_delete(scan_folder="characters", target_folder="images/gifts", target_filename = "fuckyou.png"):
        import os
        import filecmp
        if not renpy.exists("game\\" + target_filename):
            unarchive(target_folder + "/" + target_filename, "game/" + target_filename)
        is_file_found = False
        for file in os.listdir(config.basedir + "\\" + scan_folder):
            if filecmp.cmp(config.basedir + "\\" + scan_folder + "\\" + file, config.basedir + "\\game\\" + target_filename):
                is_file_found = True
                os.remove(config.basedir + "\\" + scan_folder + "\\" + file)
        os.remove(config.basedir + "\\game\\" + target_filename)
        return is_file_found

    def gift_detect():
        cur_gifts = []
        import os

        gift_list = ["blackroses.jy","redroses.jy", "whiteroses.jy", "sandalwoodoil.jy", "lavenderoil.jy", "sweetdreamoil.jy","hershey.jy", "lavenderchocolate.jy", "mintchocolate.jy", "craneorigami.jy", "roseorigami.jy",
        "bunnyorigami.jy", "raccoonplush.jy", "diffuser.jy", "horrorbookset.jy"] #"high_mountain_tea.jpg", "imperial_tea.jpg", "tienchi_tea.jpg"]


        for gift in gift_list: #for every gift
            if not renpy.exists("game/" + gift):
                unarchive("images/gifts/" + gift, "game/" + gift)
            for potential_gift in os.listdir(config.basedir + "\\characters"): #and for every file in character folder
                normalized_gift = potential_gift.lower()
                normalized_gift = re.sub('[^.,a-z0-9\n\.]', '', normalized_gift)
                if normalized_gift == gift: # if the file is in the character folder
                    cur_gifts.append([gift, True]) #add it to the list of gifts available
                    os.remove(os.path.join(config.basedir, "characters", potential_gift))
                else:
                    cur_gifts.append([gift, False])
        return cur_gifts

    #allowed_gifts = list of gifts you can give in a certain dialogue; available_gifts: list of gifts detected on folder

    def define_gift_scenario(allowed_gifts, available_gifts):
        gift_scenario = None
        for gift in range(len(available_gifts)): #for every gift on folder
            normalized_gift = available_gifts[gift][0].lower()
            normalized_gift = re.sub('[^.,a-zA-Z0-9\n\.]', '', normalized_gift)
            if available_gifts[gift][1]: #if the gift has 'existance' flag on True i.e [["blackroses.jy", True],...]
                gift_scenario = allowed_gifts.index(normalized_gift) #define number of scenario based on index of
                break
        return gift_scenario

init -2 python:
    import datetime
    import math
    import random

    ##############
    #KS FUNCTIONS#
    ##############

    # Note: k = Karma, s = Sanity for this section.

    # Add/Subtract Points and Set Levels
    def add_k(points): #add sanity points
        global temp_karma
        persistent.karma_points = ks_limiter(persistent.karma_points + points)
        temp_karma += points
    def add_s(points): #add karma points
        global temp_sanity
        persistent.sanity_points = ks_limiter(persistent.sanity_points + points)
        temp_sanity += points
    def set_k_lvl(lvl):
        persistent.karma_points = lvl_to_point(lvl)
        temp_karma = 0
    def set_s_lvl(lvl):
        persistent.sanity_points = lvl_to_point(lvl)
        temp_sanity = 0

    # Return current Karma/Sanity lvl with small randomness added (ks_variance + random.uniform)
    # - lvls go from 1 to 5, each one being points_per_level large, currently at 40.
    # - This spans the number of points from -100 to +100
    def karma(ks_variance_1 = 15):
        global ks_variance
        try: ks_variance
        except NameError:
            ks_variance = ks_variance_1
        karma = float(persistent.karma_points + random.uniform(-ks_variance, ks_variance))
        return point_to_lvl(karma)

    def sanity(ks_variance_1 = 15):
        global ks_variance
        try: ks_variance
        except NameError:
            ks_variance = ks_variance_1
        sanity = float(persistent.sanity_points + random.uniform(-ks_variance, ks_variance))
        return point_to_lvl(sanity)

    def invariant_karma():
        return point_to_lvl(persistent.karma_points)

    def invariant_sanity():
        return point_to_lvl(persistent.sanity_points)

    # Converts points to lvl or lvl to points
    def point_to_lvl(points):
        import math
        points_per_level_1 = float(40)
        number_of_lvls_1 = float(5)

        global number_of_lvls
        global points_per_level
        try: number_of_lvls
        except NameError:
            number_of_lvls = number_of_lvls_1
        try: points_per_level
        except NameError:
            points_per_level = points_per_level_1

        level = math.ceil((points/points_per_level) + (number_of_lvls/2))

        if level > number_of_lvls:
            level = number_of_lvls

        elif level <= 0:
            level = 1

        return int(level)

    def lvl_to_point(lvl):
        global number_of_lvls
        global points_per_level
        global max_points
        return int((lvl * points_per_level) - max_points - (points_per_level/2))

    # Limiter used to prevent too much KS points.
    def ks_limiter(points):
        global max_points

        if points > max_points:
            return max_points
        elif points < -max_points:
            return -max_points
        else:
            return points




    #TIME TRACKER FUNCTION
    def time_tracker_start(): #start can either be True or False
        global time_tracker
        time_tracker = datetime.datetime.now()
        if persistent.previous_time != None:
            if persistent.previous_time > time_tracker:
                return True
                #if renpy.seen_label('TimeCheat1') and not renpy.seen_label('TimeCheat2'):
                #    renpy.jump("TimeCheat2")
                #elif renpy.seen_label('TimeCheat2') and not renpy.seen_label('TimeCheat3'):
                #    renpy.jump ("TimeCheat3")
                #elif renpy.seen_label('TimeCheat3'):
                #    renpy.error("You CHEATER")
                #    renpy.quit()
                #else:
                #    renpy.jump("TimeCheat1")
            else:
                return False

    def time_tracker_update():
        global time_tracker
        if time_tracker == None:
            time_tracker_start()
        else:
            if time_tracker > datetime.datetime.now(): #if the past is later than the present
                return True
                #if renpy.seen_label('TimeCheat1') and not renpy.seen_label('TimeCheat2'):
                #    renpy.jump("TimeCheat2")
                #elif renpy.seen_label('TimeCheat2') and not renpy.seen_label('TimeCheat3'):
                #    renpy.jump ("TimeCheat3")
                #elif renpy.seen_label('TimeCheat3'):
                #    renpy.error("You CHEATER")
                #    renpy.quit()
                #else:
                #    renpy.jump("TimeCheat1")

            else:
                persistent.previous_time = datetime.datetime.now()
                persistent.ingame_time = persistent.ingame_time + (datetime.datetime.now() - time_tracker)
                time_tracker = persistent.previous_time

    def time_in_game():
        days = persistent.ingame_time.days
        hours = persistent.ingame_time.seconds // (3600)
        return {"days": days, "hours": hours}

    def timecycle_transition(bg="space", speed = "normal", bypass=False, sprite_present=True, forced_timecycle = None):
        tc_class.transition(bg, speed, bypass, sprite_present, forced_timecycle)
        return

    #TIMECYCLE FUNCTIONS

    class Timecycles:
        bg_timecycle = {
            "space": False,
            "timecycle": True,
            "purple_knives": True,
            "purple_table": True,
            "purple_view": True,
            "yuri_knives": True,
            "yuri_table": True,
            "yuri_bed": True,
            "yuri_desk": True,
            "yuri_kotatsu_1": True,
            "yuri_kotatsu_2": True,
            "laboratory": False,
            "nothing": False}

        def bg_list_dict(self):
            if persistent.high_gpu == 0:
                return {
                    "nothing": ["nothing"],
                    "space": ["mask_2", "mask_3", "yuri_room"],
                    "timecycle": ["jy_bg_back", "jy_bg_fore"],
                    "purple_knives": ["room_p_knives"],
                    "purple_table": ["room_p_table"],
                    "purple_view": ["room_p_view"],
                    "yuri_knives": ["knives"],
                    "yuri_bed": ["bed"],
                    "yuri_desk": ["desk"],
                    "yuri_kotatsu_1": ["kotatsu_1"],
                    "yuri_kotatsu_2": ["kotatsu_2"],
                    "laboratory": ["lab"]
                }
            elif persistent.high_gpu == 1:
                return {
                    "nothing": ["nothing"],
                    "space": ["mask_2", "mask_3", "yuri_room"],
                    "timecycle": ["jy_bg_back", "jy_bg_fore"],
                    "purple_knives": ["room_p_knives"],
                    "purple_table": ["room_p_table"],
                    "purple_view": ["room_p_view"],
                    "yuri_knives": ["knives"],
                    "yuri_bed": ["bed"],
                    "yuri_desk": ["desk"],
                    "yuri_kotatsu_1": ["kotatsu_1"],
                    "yuri_kotatsu_2": ["kotatsu_2"],
                    "laboratory": ["lab"]
                }

            elif persistent.high_gpu == 2:
                return {
                    "nothing": ["nothing"],
                    "space": ["vid_mask_2", "vid_mask_3", "yuri_room"],
                    "timecycle": ["jy_bg_back", "jy_bg_fore"],
                    "purple_knives": ["room_p_knives"],
                    "purple_table": ["room_p_table"],
                    "purple_view": ["room_p_view"],
                    "yuri_knives": ["knives"],
                    "yuri_bed": ["bed"],
                    "yuri_desk": ["desk"],
                    "yuri_kotatsu_1": ["kotatsu_1"],
                    "yuri_kotatsu_2": ["kotatsu_2"],
                    "laboratory": ["lab"]
                }



        def __init__(self):
            global year, month, day, hour, minute, second, current_timecycle_marker
            year, month, day, hour, minute, second = self.cur_time()
            current_timecycle_marker = self.time_to_timecycle(hour, persistent.bg)

        def cur_time(self):
            x = str(datetime.datetime.today())
            month = x[5:7]
            day = x[8:10]
            year = x[0:4]
            hour = x[11:13]
            minute = x[14:16]
            second = x[17:19]
            return year, month, day, hour, minute, second

        def cur_month_day(self):
            return int(str(self.cur_time()[1]) + str(self.cur_time()[2]))

        def time_to_timecycle(self, time, bg):
            if self.bg_timecycle[bg]:
                return "_" + TimeCycle.time_id
            elif persistent.bg == "laboratory":
                return "_night"

            return "_space"

        def cur_time_to_tc(self, bg):
            return self.time_to_timecycle(self.cur_time()[3], bg)

        def update_tc(self, bg):
            global current_timecycle_marker, bg_list
            persistent.bg = bg
            current_timecycle_marker = self.cur_time_to_tc(persistent.bg)
            bg_list = self.bg_list_dict()[persistent.bg]

        def transition(self, bg="space", speed = "normal", bypass=False, sprite_present=True, forced_timecycle = None):
            global past_yuri_sit, past_timecycle_marker, past_bg, past_bg_list
            global yuri_sit, current_timecycle_marker, bg_list, is_sprite_present
            past_bg = ""
            past_bg_list = ""
            past_timecycle_marker = ""

            is_sprite_present = sprite_present

            if not "bg_list" in globals():
                #persistent.bg = bg
                self.update_tc(bg)
                renpy.show_screen("jy_bg")
                return
            if persistent.bg == bg and current_timecycle_marker == self.cur_time_to_tc(bg) and not bypass and forced_timecycle == None:
                return
            if speed == "now":
                #redefine the current persistent variables.
                persistent.bg = bg
                bg_list = self.bg_list_dict()[persistent.bg]
                if forced_timecycle != None:
                    current_timecycle_marker = forced_timecycle
                else: #if the timecycle has changed
                    current_timecycle_marker = self.cur_time_to_tc(bg)
            else:
                #establish past values
                past_bg = persistent.bg
                persistent.marker = past_bg
                #if past_bg == "space":
                #    current_timecycle_marker = ""
                past_timecycle_marker = current_timecycle_marker
                if sprite_present:
                    past_yuri_sit = yuri_sit
                past_bg_list = self.bg_list_dict()[past_bg]

                #show old sprite on top of new ones
                renpy.show_screen("jy_past")#, zorder = 50)
                renpy.hide_screen("jy_bg")
                if sprite_present:
                    renpy.hide_screen("yuri_sit")

                #redefine the current persistent variables.
                persistent.bg = bg
                bg_list = self.bg_list_dict()[persistent.bg]
                if forced_timecycle != None:
                    current_timecycle_marker = forced_timecycle
                else: #if the timecycle has changed
                    current_timecycle_marker = self.cur_time_to_tc(bg)

                #activate transition to disappear the past version
                renpy.call("tc_transition")
            return

    tc_class = Timecycles()

#Timecycle/Room Variables
define slow_dissolve = Dissolve(5)


label tc_transition:
    show black zorder 100 with Dissolve(2.5)
    show screen jy_bg
    show screen yuri_sit
    pause 1.0
    hide screen jy_past
    hide black zorder 100 with Dissolve(2.5)
    #with slow_dissolve
    return

screen jy_bg():
    #zorder 1
    layer "master"
    imagemap:
        idle "jy_bg"

        #if persistent.bg == "space" and persistent.high_gpu == 0:
        #    $ renpy.call("mask_windows")
        
        if persistent.bg == "timecycle" and hide_yuri_sit == False:
            hotspot (153, 0, 438, 341)action Function(boop_init, "boop_window")

        if hide_yuri_sit == True:
            hotspot (478, 335, 324, 174) action Function(boop_init, "sleepy_headpat")

        if persistent.bg == "laboratory":
            if persistent.costume != "lab": #Since the screen constantly repeats, we have to add this to keep track of the previous costume and not have it replaced with the labcoat
                $persistent.previous_costume = persistent.costume
                $persistent.hairstyle = "tied_up"
                $persistent.costume = "lab"
                $show_chr("A-AAAAA-AAAA")
        elif persistent.costume == "lab":
            $persistent.hairstyle = "default"
            $persistent.costume = persistent.previous_costume
            $show_chr("A-AAAAA-AAAA")


layeredimage jy_bg:
    if len(bg_list) > 0 and not bg_list[0] == "mask_2":
        "[bg_list[0]][current_timecycle_marker]"
    if len(bg_list) > 0 and bg_list[0] == "mask_2":
        "[bg_list[0]]"
    if len(bg_list) > 1 and not bg_list[1] == "mask_3":
        "[bg_list[1]][current_timecycle_marker]"
    if len(bg_list) > 1 and bg_list[1] == "mask_3":
        "[bg_list[1]]"
    if len(bg_list) > 2 and bg_list[2] == "room_mask":
        "[bg_list[2]]"
    if len(bg_list) > 2 and not bg_list[2] == "room_mask":
        "[bg_list[2]][current_timecycle_marker]"
    if len(bg_list) > 3 and bg_list[3] == "room_mask2":
        "[bg_list[3]]"
    if len(bg_list) > 3 and not bg_list[3] == "room_mask2":
        "[bg_list[3]][current_timecycle_marker]"
    if len(bg_list) > 4:
        "[bg_list[4]][current_timecycle_marker]"
    if persistent.bg == "timecycle" and persistent.boop_locations[4] == 2 and not renpy.seen_label("annoyed_boop_window"):
        "window_crack_2"
    elif persistent.bg == "timecycle" and persistent.boop_locations[4] == 3 and not renpy.seen_label("annoyed_boop_window"):
        "window_crack_3"
    elif persistent.bg == "timecycle" and persistent.boop_locations[4] >= 4 and not renpy.seen_label("annoyed_boop_window"):
        "window_crack_4"

screen jy_past():
    zorder 100
    layer "master"
    add "past_jy_bg"
    if is_sprite_present:
        add "past_yuri_sit"

layeredimage past_jy_bg:
    if len(past_bg_list) > 0 and not past_bg_list[0] == "mask_2":
        "[past_bg_list[0]][past_timecycle_marker]"
    if len(past_bg_list) > 0 and past_bg_list[0] == "mask_2":
        "[past_bg_list[0]]"
    if len(past_bg_list) > 1 and not past_bg_list[1] == "mask_3":
        "[past_bg_list[1]][past_timecycle_marker]"
    if len(past_bg_list) > 1 and past_bg_list[1] == "mask_3":
        "[past_bg_list[1]]"
    if len(past_bg_list) > 2 and past_bg_list[2] == "room_mask":
        "[past_bg_list[2]]"
    if len(past_bg_list) > 2 and not past_bg_list[2] == "room_mask":
        "[past_bg_list[2]][past_timecycle_marker]"
    if len(past_bg_list) > 3 and past_bg_list[3] == "room_mask2":
        "[past_bg_list[3]]"
    if len(past_bg_list) > 3 and not past_bg_list[3] == "room_mask2":
        "[past_bg_list[3]][past_timecycle_marker]"
    if len(past_bg_list) > 4:
        "[past_bg_list[4]][past_timecycle_marker]"
    #do not add past_bg_list[2] and [3]! they are the glowing window in space effect

layeredimage past_yuri_sit:
    always "[persistent.head2][past_timecycle_marker]"#raccoon tail
    if persistent.hairstyle == "default":
        "backhair_frontface[current_timecycle_marker]"
    if not yuri_sit["arms"]["both"]["has_up_arms"]:
        "[yuri_sit['arms']['left']['up']]_base[past_timecycle_marker]" #uparm_left
    if not yuri_sit["arms"]["both"]["has_up_arms"]:
        "[yuri_sit['arms']['right']['up']]_base[past_timecycle_marker]" #uparm_right
    always "torso_base[past_timecycle_marker]"

    always "[yuri_sit['torso']['costume']][past_timecycle_marker]" #torso_costume
    if not yuri_sit["arms"]["both"]["has_up_arms"]:
        "[yuri_sit['arms']['left']['costume']['up']][past_timecycle_marker]" #uparm_left_costume
    if not yuri_sit["arms"]["both"]["has_up_arms"]:
        "[yuri_sit['arms']['right']['costume']['up']][past_timecycle_marker]" #uparm_right_costume
    always "[yuri_sit['head']]head[past_timecycle_marker]" #head
    always "yuri_sit_eyes" #eyes
    always "[yuri_sit['mouth']][past_timecycle_marker]" #mouth
    always "[yuri_sit['eyebrows']][past_timecycle_marker]" #eyebrows
    always "[yuri_sit['head_cover_1']][past_timecycle_marker]" #head_cover_1
    always "[yuri_sit['head_cover_2']][past_timecycle_marker]" #head_cover_2
    always "[persistent.face1][past_timecycle_marker]" #glasses
    if persistent.hairstyle == "default":
        "[yuri_sit['head']]hair_default[past_timecycle_marker]" #head_hair front
    elif persistent.hairstyle == "tied_up":
        "[yuri_sit['head']]hair_scientist[past_timecycle_marker]" #head_hair front

    always "[persistent.face2][current_timecycle_marker]" #old neko ears on expression hub
    always "[persistent.head1][current_timecycle_marker]" #neko/raccoon ears (always on top)

    if not yuri_sit["arms"]["left"]["isBehind"] and not yuri_sit["arms"]["right"]["isBehind"] and yuri_sit["extras"]["book"] != "":
        "[yuri_sit['extras']['book']][past_timecycle_marker]" #holding a book
    if not yuri_sit["arms"]["left"]["isBehind"] and not yuri_sit["arms"]["right"]["isBehind"] and yuri_sit["arms"]["both"]["down"] != "":
        "[yuri_sit['arms']['both']['down']]_base[past_timecycle_marker]" #downarm_both
    if not yuri_sit["arms"]["left"]["isBehind"] and yuri_sit["arms"]["both"]["down"] == "":
        "[yuri_sit['arms']['left']['down']]_base[past_timecycle_marker]" #downarm_left
    if not yuri_sit["arms"]["right"]["isBehind"] and yuri_sit["arms"]["both"]["down"] == "":
        "[yuri_sit['arms']['right']['down']]_base[past_timecycle_marker]" #downarm_right
    if not yuri_sit["arms"]["left"]["isBehind"] and yuri_sit["arms"]["both"]["down"] == "":
        "[yuri_sit['arms']['left']['costume']['down']][past_timecycle_marker]" #downarm_left_costume
    if not yuri_sit["arms"]["right"]["isBehind"] and yuri_sit["arms"]["both"]["down"] == "":
        "[yuri_sit['arms']['right']['costume']['down']][past_timecycle_marker]" #downarm_right_costume
    if not yuri_sit["arms"]["left"]["isBehind"] and not yuri_sit["arms"]["right"]["isBehind"] and yuri_sit["arms"]["both"]["down"] != "":
        "[yuri_sit['arms']['both']['costume']['down']][past_timecycle_marker]" #downarm_both_costume

    always "table[past_timecycle_marker]"

    if yuri_sit["arms"]["left"]["isBehind"] and yuri_sit["arms"]["right"]["isBehind"] and yuri_sit["extras"]["book"] != "":
        "[yuri_sit['extras']['book']][past_timecycle_marker]" #holding a book
    if yuri_sit["arms"]["left"]["isBehind"] and yuri_sit["arms"]["right"]["isBehind"] and yuri_sit["arms"]["both"]["down"] != "":
        "[yuri_sit['arms']['both']['down']]_base[past_timecycle_marker]" #downarm_both
    if yuri_sit["arms"]["left"]["isBehind"] and yuri_sit["arms"]["both"]["down"] == "":
        "[yuri_sit['arms']['left']['down']]_base[past_timecycle_marker]" #downarm_left
    if yuri_sit["arms"]["right"]["isBehind"] and yuri_sit["arms"]["both"]["down"] == "":
        "[yuri_sit['arms']['right']['down']]_base[past_timecycle_marker]" #downarm_right
    if yuri_sit["arms"]["left"]["isBehind"] and yuri_sit["arms"]["both"]["down"] == "":
        "[yuri_sit['arms']['left']['costume']['down']][past_timecycle_marker]" #downarm_left_costume
    if yuri_sit["arms"]["right"]["isBehind"] and yuri_sit["arms"]["both"]["down"] == "":
        "[yuri_sit['arms']['right']['costume']['down']][past_timecycle_marker]" #downarm_right_costume
    if yuri_sit["arms"]["left"]["isBehind"] and yuri_sit["arms"]["right"]["isBehind"] and yuri_sit["arms"]["both"]["down"] != "":
        "[yuri_sit['arms']['both']['costume']['down']][past_timecycle_marker]" #downarm_both_costume

label mask_windows:
    screen mask_windows():
        zorder 1
        modal False

        frame:
            xpos(30)
            ypos(200)
            xsize(320)
            ysize(180)
            background room_mask

        frame:
            xpos(935)
            ypos(200)
            xsize(320)
            ysize(180)
            background room_mask2

    show screen mask_windows()

label show_mask_timecycle:
    $renpy.show_screen("cur_jy_bg_back")
    if month == 12 and current_timecycle_marker == "_night":
        show snow zorder 1
    $renpy.show_screen("cur_jy_bg_fore")
    return

label timecycleswitch:
    menu:
        "Timecycle":
            $tc_class.transition("timecycle")
        "Classroom":
            $tc_class.transition("space")
        "Purple Room":
            $tc_class.transition("purple_table")
        "Yuri's Bedroom":
            menu:
                "Kotatsu 1":
                    $tc_class.transition("yuri_kotatsu_1")
                "Kotatsu 2":
                    $tc_class.transition("yuri_kotatsu_2")
                "Desk":
                    $tc_class.transition("yuri_desk")
    call screen make_expression
###################
#TIMECYCLE IMAGES##
###################
image room_glitch = "images/vfx/yuri_glitch/yuri_bg_glitch.png"

image vid_mask_2_space = Movie(play="images/bg/space_classroom/vid_mask_2.webm", xpos=20, ypos=115)

image vid_mask_3_space = Movie(play="images/bg/space_classroom/vid_mask_3.webm", xpos=800, ypos=115)

image mask_child:
    "images/bg/space_classroom/space_child_2.png"
    xtile 2

image mask_mask:
    "images/bg/space_classroom/space_mask.png"
    xtile 3

image mask_mask_flip:
    "images/bg/space_classroom/space_mask.png"
    xtile 3 xzoom -1

image maskb:
    "images/bg/space_classroom/space_maskb.png"
    xtile 3

image mask_test = AnimatedMask("#ff6000", "mask_mask", "maskb", 0.10, 32)
image mask_test2 = AnimatedMask("#ffffff", "mask_mask", "maskb", 0.03, 16)
image mask_test3 = AnimatedMask("#ff6000", "mask_mask_flip", "maskb", 0.10, 32)
image mask_test4 = AnimatedMask("#ffffff", "mask_mask_flip", "maskb", 0.03, 16)

image mask_2:
    "images/bg/space_classroom/space_mask_2.png"
    xtile 3 subpixel True
    block:
        xoffset 0
        linear 1200 xoffset -1280
        repeat

image mask_3:
    "images/bg/space_classroom/space_mask_3.png"
    xtile 3 subpixel True
    block:
        xoffset 0
        linear 180 xoffset -1280
        repeat

image room_mask = LiveComposite((1280, 720), (0, 0), "mask_test", (0, 0), "mask_test2")
image room_mask2 = LiveComposite((1280, 720), (0, 0), "mask_test3", (0, 0), "mask_test4")

#image room_mask = LiveComposite(
#    size=(1280, 720),
#    target_size=(320, 180),
#    positions=(30, 200),
#    images=["mask_test", "mask_test2"]
#    )

#image room_mask2 = LiveComposite(
#    size=(1280, 720),
#    target_size=(320, 180),
#    positions=(935, 200),
#    images=["mask_test3", "mask_test4"]
#    )

#####UNSORTED!!!!

screen yuri_sit():
    zorder 11
    layer "master"
    imagemap:

        if hide_yuri_sit:
            idle "nothing"
        else:
            idle "yuri_sit"

        if hide_yuri_sit == True:
            idle "nothing"
        else:
            idle "yuri_sit"

        #hotspot (x_left_side, y_top_side, width, length)

        hotspot (654, 225, 13, 13) action Function(boop_init, "boop_nose")
        hotspot (615, 440, 30, 50) action Function(boop_init, "boop_nose_chibi")#chibi version
        hotspot (585,216,50,50) action Function(boop_init, "boop_cheek")
        hotspot (693,216,50,50) action Function(boop_init, "boop_cheek")
        hotspot (578, 50, 186, 103) action Function(boop_init, "headpat")
        hotspot (478, 335, 13, 13) action Function(boop_init, "sleepy_headpat")
        #hotspot (615, 440, ) action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName)))
        #hotspot (126, 254, 191, 377)action Function(boop_init, "diffuser_boop")

screen yuri_sleep():
    zorder 11
    layer "master"
    imagemap:
        if hide_yuri_sleep:
            $ DisableTalk()
            idle "nothing"
        else:
            $ DisableTalk()
            $ set_boop_state(True)
            idle "yuri_sleep"

layeredimage yuri_sleep:

    if persistent.costume == "sweater":
        "yuri_resting_pyjama[current_timecycle_marker]"

    if persistent.costume == "school":
        "yuri_resting_school[current_timecycle_marker]"

    if persistent.costume == "valentines":
        "yuri_resting_pyjama[current_timecycle_marker]"


if hide_yuri_sleep == False:
    hide yuri_sit

#LiveComposite([base],[face1],[face2],[head1],[head2],[hands],[eyebrows],[blush],[cry],[eyes],[mouth])
layeredimage yuri_sit:
    always "[persistent.head2][current_timecycle_marker]"#raccoon tail
    if persistent.hairstyle == "default":
        "backhair_frontface[current_timecycle_marker]"
    if not yuri_sit["arms"]["both"]["has_up_arms"]:
        "[yuri_sit['arms']['left']['up']]_base[current_timecycle_marker]" #uparm_left
    if not yuri_sit["arms"]["both"]["has_up_arms"]:
        "[yuri_sit['arms']['right']['up']]_base[current_timecycle_marker]" #uparm_right
    if yuri_sit["torso"]["costume"] in ["torso_swimsuit", "torso_bikini"]:
        "torso_nude_base"
    else:
        "torso_base[current_timecycle_marker]"#
    if yuri_sit["torso"]["costume"] in ["torso_swimsuit", "torso_bikini"]:
        "[yuri_sit['torso']['costume']]"
    else:
        "[yuri_sit['torso']['costume']][current_timecycle_marker]" #torso_costume
    always "[yuri_sit['torso']['costume2']]"  # This is the fix
    if persistent.book: #Dandy flag: cheap way of doing the cthulhu implementation. Rework this when botharms are fixed.
        "cthulhu_book"
    if not yuri_sit["arms"]["both"]["has_up_arms"]:
        "[yuri_sit['arms']['left']['costume']['up']][current_timecycle_marker]" #uparm_left_costume
    if not yuri_sit["arms"]["both"]["has_up_arms"]:
        "[yuri_sit['arms']['right']['costume']['up']][current_timecycle_marker]" #uparm_right_costume
    #
    always "[yuri_sit['head']]head[current_timecycle_marker]" #head
    always "yuri_sit_eyes" #eyes
    always "[yuri_sit['mouth']][current_timecycle_marker]" #mouth
    always "[yuri_sit['eyebrows']][current_timecycle_marker]" #eyebrows
    always "[yuri_sit['head_cover_1']][current_timecycle_marker]" #head_cover_1
    always "[yuri_sit['head_cover_2']][current_timecycle_marker]" #head_cover_2
    always "[persistent.face1][current_timecycle_marker]" #glasses
    if persistent.hairstyle == "default":
        "[yuri_sit['head']]hair_default[current_timecycle_marker]" #head_hair front
    elif persistent.hairstyle == "tied_up":
        "[yuri_sit['head']]hair_scientist[current_timecycle_marker]" #head_hair front

    always "[persistent.face2][current_timecycle_marker]" #old neko ears on expression hub
    always "[persistent.head1][current_timecycle_marker]" #neko/raccoon ears (always on top)

    #Table not isBehind arms
    if not yuri_sit["arms"]["left"]["isBehind"] and not yuri_sit["arms"]["right"]["isBehind"] and yuri_sit["extras"]["book"] != "":
        "[yuri_sit['extras']['book']][current_timecycle_marker]" #holding a book
    if not yuri_sit["arms"]["left"]["isBehind"] and not yuri_sit["arms"]["right"]["isBehind"] and yuri_sit["arms"]["both"]["down"] != "":
        "[yuri_sit['arms']['both']['down']]_base[current_timecycle_marker]" #downarm_both
    if not yuri_sit["arms"]["left"]["isBehind"] and yuri_sit["arms"]["both"]["down"] == "":
        "[yuri_sit['arms']['left']['down']]_base[current_timecycle_marker]" #downarm_left
    if not yuri_sit["arms"]["right"]["isBehind"] and yuri_sit["arms"]["both"]["down"] == "":
        "[yuri_sit['arms']['right']['down']]_base[current_timecycle_marker]" #downarm_right
    if not yuri_sit["arms"]["left"]["isBehind"] and yuri_sit["arms"]["both"]["down"] == "":
        "[yuri_sit['arms']['left']['costume']['down']][current_timecycle_marker]" #downarm_left_costume
    if not yuri_sit["arms"]["right"]["isBehind"] and yuri_sit["arms"]["both"]["down"] == "":
        "[yuri_sit['arms']['right']['costume']['down']][current_timecycle_marker]" #downarm_right_costume
    if not yuri_sit["arms"]["left"]["isBehind"] and not yuri_sit["arms"]["right"]["isBehind"] and yuri_sit["arms"]["both"]["down"] != "":
        "[yuri_sit['arms']['both']['costume']['down']][current_timecycle_marker]" #downarm_both_costume

    always "table[current_timecycle_marker]"

    #Table isBehind arms
    #...this is like an opposite day convention. Flip the sign meanings in next build?
    if yuri_sit["arms"]["left"]["isBehind"] and yuri_sit["arms"]["right"]["isBehind"] and yuri_sit["extras"]["book"] != "":
        "[yuri_sit['extras']['book']][current_timecycle_marker]" #holding a book
    if yuri_sit["arms"]["left"]["isBehind"] and yuri_sit["arms"]["right"]["isBehind"] and yuri_sit["arms"]["both"]["down"] != "":
        "[yuri_sit['arms']['both']['down']]_base[current_timecycle_marker]" #downarm_both
    if yuri_sit["arms"]["left"]["isBehind"] and yuri_sit["arms"]["both"]["down"] == "":
        "[yuri_sit['arms']['left']['down']]_base[current_timecycle_marker]" #downarm_left
    if yuri_sit["arms"]["right"]["isBehind"] and yuri_sit["arms"]["both"]["down"] == "":
        "[yuri_sit['arms']['right']['down']]_base[current_timecycle_marker]" #downarm_right
    if yuri_sit["arms"]["left"]["isBehind"] and yuri_sit["arms"]["both"]["down"] == "":
        "[yuri_sit['arms']['left']['costume']['down']][current_timecycle_marker]" #downarm_left_costume
    if yuri_sit["arms"]["right"]["isBehind"] and yuri_sit["arms"]["both"]["down"] == "":
        "[yuri_sit['arms']['right']['costume']['down']][current_timecycle_marker]" #downarm_right_costume
    if yuri_sit["arms"]["left"]["isBehind"] and yuri_sit["arms"]["right"]["isBehind"] and yuri_sit["arms"]["both"]["down"] != "":
        "[yuri_sit['arms']['both']['costume']['down']][current_timecycle_marker]" #downarm_both_costume
    always "[face_mask]"
    always "[face_mask_2]"
    if persistent.hdy_statue_is_enabled:
        "hdy_statue"
    if persistent.halloween_cupcake_is_enabled:
        "cupcake_halloween"
    if persistent.diffuser_is_enabled:
        "diffuser"
    elif persistent.sandalwood_oil_is_enabled:
        "sandalwood_oil"
    elif persistent.lavender_o_is_enabled:
        "lavenderO"
    elif persistent.sweet_dream_oil_is_enabled:
        "sweet_dream_oil"
    elif persistent.diffuser_mist_is_enabled:
        "diffuser"
    elif persistent.hershey_is_enabled:
        "hershey"
    elif persistent.lavenderC_is_enabled:
        "lavenderC"
    elif persistent.mint_is_enabled:
        "mint"
    if persistent.craneO_is_enabled:
        "craneo"
    if persistent.bunnyO_is_enabled:
        "bunnyo"
    if persistent.raccoon_is_enabled:
        "raccoon"
    if persistent.roseO_is_enabled:
        "roseo"
    if persistent.sandalwood_oil_mist_is_enabled:
        "sandalwood_mist"
    if persistent.lavenderO_mist_is_enabled:
        "lavenderO_mist"


layeredimage yuri_stand:
    always "[yuri_stand[0]]head_sprite" #head
    always "[yuri_stand[1]]_sprite" #eyes
    always "[yuri_stand[2]]_sprite" #mouth
    always "[yuri_stand[3]]_sprite" #eyebrows
    always "torso_[persistent.costume]_sprite" #torso


image yuri_sit_eyes = LiveComposite((1280, 720), (0, 0), "[yuri_sit['eyes'][1]]", (0,0), "[yuri_sit['eyes'][2]]")

image yuri_sit_eyes_standard:
    "[yuri_sit['eyes'][0]]" + "[current_timecycle_marker]"

image yuri_sit_blink_1: #version that goes to half_open first.
    "[yuri_sit['eyes'][0]][current_timecycle_marker]" #normal eye position
    choice:
        pause 0.5
    choice:
        pause 4.2
    choice:
        pause 4.8
    choice:
        pause 6.0
    choice:
        pause 6.2
    "eyes_4_front[current_timecycle_marker]"
    pause 0.05
    "eyes_2_front[current_timecycle_marker]"
    pause 0.25
    "eyes_4_front[current_timecycle_marker]"
    pause 0.05
    repeat

image yuri_sit_blink_2: #goes only to eyes_2 first.
    "[yuri_sit['eyes'][0]][current_timecycle_marker]" #normal eye position
    choice:
        pause 0.5
    choice:
        pause 4.2
    choice:
        pause 4.8
    choice:
        pause 6.0
    choice:
        pause 6.2
    "eyes_2_front[current_timecycle_marker]"
    pause 0.25
    repeat

image insanepupils:
    "eyes_insane_pupils[current_timecycle_marker]"
    function insanepupils_function

init python:
    def insanepupils_function(trans, st, at):
        trans.xoffset = random.uniform(-5, 4)
        trans.yoffset = random.uniform(0, 6)
        return random.uniform(0.3, 1.5)

layeredimage yuri_prehug:
    if persistent.bg == "space" and renpy.has_image("prehug_" + persistent.costume + "_space"):
        "prehug_[persistent.costume]_space"
    elif persistent.bg != "space" and renpy.has_image("prehug_" + persistent.costume + current_timecycle_marker):
        "prehug_[persistent.costume][current_timecycle_marker]"
    else:
        "prehug_[persistent.costume]_day"
    always "[persistent.face1]_prehug[current_timecycle_marker]"
    always "[persistent.head1]_prehug[current_timecycle_marker]"
#layeredimage yuri_prehug_insane:
    #always "prehug_[persistent.costume][current_timecycle_marker]" #base
    #always "[image_state[1]]_prehug[special_costume][current_timecycle_marker]" #glasses
    #always "[image_state[3]]_prehug[special_costume][current_timecycle_marker]" #neko
    #always "[image_state[4]]_prehug[special_costume][current_timecycle_marker]" #hat
    #always "prehug_yandere[current_timecycle_marker]" #yandere variant
layeredimage yuri_hug:#
    if persistent.bg == "space" and renpy.has_image("hug_" + persistent.costume + "_space"):
        "hug_[persistent.costume]_space"
    elif persistent.bg != "space" and renpy.has_image("hug_" + persistent.costume + current_timecycle_marker):
        "hug_[persistent.costume][current_timecycle_marker]"
    else:
        "hug_[persistent.costume]_space"
    if persistent.face1 == "hat":
        "nothing"
    else:
        "[persistent.face1]_hug[current_timecycle_marker]"
    always "[persistent.head1]_hug[current_timecycle_marker]"
layeredimage yuri_lewdhug:
    if persistent.bg == "space" and renpy.has_image("lewdhug_" + persistent.costume + "_space"):
        "lewdhug_[persistent.costume]_space"
    elif persistent.bg != "space" and renpy.has_image("lewdhug_" + persistent.costume + current_timecycle_marker):
        "lewdhug_[persistent.costume][current_timecycle_marker]"
    else:
        "lewdhug_[persistent.costume]_day"#currently missing for valentines outfit

layeredimage yuri_sleepy:
    if persistent.bg == "space" and renpy.has_image ("yuri_sleepy" + persistent.costume + "_space"):
        "yuri_sleepy_[persistent.costume]_space"
    elif persistent.bg != "space" and renpy.has_image("=" + persistent.costume + current_timecycle_marker):
        "yuri_sleepy_[persistent.costume][current_timecycle_marker]"
    else:
        "yuri_sleepy_[persistent.costume]_day"


layeredimage yuri_resting:
    if persistent.bg == "space" and renpy.has_image ("yuri_resting_" + persistent.costume + "_space"):
        "yuri_resting_[persistent.costume]_space"
    elif persistent.bg != "space" and renpy.has_image("yuri_resting_" + persistent.costume + current_timecycle_marker):
        "yuri_resting_[persistent.costume][current_timecycle_marker]"
    else:
        "yuri_resting_[persistent.costume]_day"


image birthdaybanner = "banner[current_timecycle_marker]"
#layeredimage giftarm:
#    always "[persistent.brand][persistent.costume[0]]_[persistent.state]"
layeredimage giftarm:
    always "[persistent.brand][persistent.state[0]]" #can be hershey, gb, and wicked
    always "giftarm[persistent.costume][persistent.state[1]]" #can be _wrapper, _open, _break1, and break2 #represents arm (arm above because witch costume)
layeredimage yuri_kiss:
    if persistent.bg == "space" and renpy.has_image("yuri_kiss_" + persistent.costume + "_space"):
        "yuri_kiss_[persistent.costume]_space"
    elif persistent.bg != "space" and renpy.has_image("yuri_kiss_" + persistent.costume + current_timecycle_marker):
        "yuri_kiss_[persistent.costume][current_timecycle_marker]"
    else:
        "yuri_kiss_[persistent.costume]_day"

    if persistent.face1 != "nothing":
        "[persistent.face1]_kissing[current_timecycle_marker]"
    #always "yuri_kiss_[persistent.costume][current_timecycle_marker]" #hair
    #always "kiss_base[current_timecycle_marker]" #base
    #always "kiss_[persistent.costume][current_timecycle_marker]" #costume
    #always "kiss_head[current_timecycle_marker]" #head
    #always "kiss_face[current_timecycle_marker]" #face

# Objects on top of her desk
image cake = "cake_[persistent.cake][current_timecycle_marker]"
image cake2 = "cake_[persistent.cake]2[current_timecycle_marker]"
image chocoanimation = "[persistent.frame][persistent.costume]"
image teacup = "[persistent.brand]_cup"
image teabag = "[persistent.brand]_bag"
image holidaycup = "holiday_cup[persistent.costume]"
image flowervase = "rosevase_[persistent.flower][current_timecycle_marker]"
image held_object = "[persistent.heldobject]_hand"
image winehand = "wineglass_hand[persistent.costume]"
image flowerhand = "[persistent.flower][persistent.costume]"
image pumpkin_back:
    "pumpkin_inside[current_timecycle_marker]" with Dissolve(0.15, alpha=True)
    random.randint(4,20) * .2
    im.MatrixColor("pumpkin_inside.png", im.matrix.brightness(-1)) with Dissolve(0.15, alpha=True)
    repeat
image pumpkin_back_old:
    "pumpkin_inside[old_timecycle_marker]" with Dissolve(0.15, alpha=True)
    random.randint(4,20) * .2
    im.MatrixColor("pumpkin_inside.png", im.matrix.brightness(-1)) with Dissolve(0.15, alpha=True)
    repeat

init -100 python:
    def GuideMouse(x_target=config.screen_width/2, y_target=config.screen_height/2, speed=.9):
        targetpos = [int(x_target), int(y_target)]
        currentpos = renpy.get_mouse_pos()
        diffpos = [currentpos[0]-targetpos[0], currentpos[1]-targetpos[1]]
        while abs(diffpos[0]) > 20 or abs(diffpos[1]) > 20:
            renpy.set_mouse_pos(targetpos[0]+speed*diffpos[0], targetpos[1]+speed*diffpos[1], .1)
            renpy.pause(.1)
            currentpos = renpy.get_mouse_pos()
            diffpos = [abs(currentpos[0]-targetpos[0]), abs(currentpos[1]-targetpos[1])]
    def mouse_move(symbol, speed = .9):
        symbol = str(symbol)
        global mouse_move_dict
        if symbol in mouse_move_dict:
            dict_result = mouse_move_dict[symbol]
            GuideMouse(dict_result[0], dict_result[1], speed)
