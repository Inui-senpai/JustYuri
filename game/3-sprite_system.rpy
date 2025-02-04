init -996 python:
    class SpriteObject:
        id = None

        def show_code(self, expression):
            pass

    class YuriSit(SpriteObject):
        id = "yuri_sit"
        hair = None
        outfit = None

        head = None
        eyes = eyes_alpha = eyes_beta = None
        mouth = None
        eyebrows = None
        head_cover_1 = head_cover_2 = None
        torso = None
        left_arm = None
        left_arm_behind = False
        right_arm = None
        right_arm_behind = False
        extras = {"book": None}

        def show(self, head=None, eyes=None, eyes_alpha=None, eyes_beta=None, mouth=None, eyebrows=None, head_cover_1=None, head_cover_2=None, torso=None, left_arm=None, left_arm_behind=None, right_arm=None, right_arm_behind=None, extras=None):
            self.head = self.head if head == None else head
            self.eyes = self.eyes if eyes == None else eyes
            self.eyes_alpha = self.eyes_alpha if eyes_alpha == None else eyes_alpha
            self.eyes_beta = self.eyes_beta if eyes_beta == None else eyes_beta
            self.mouth = self.mouth if mouth == None else mouth
            self.eyebrows = self.eyebrows if eyebrows == None else eyebrows
            self.head_cover_1 = self.head_cover_1 if head_cover_1 == None else head_cover_1
            self.head_cover_2 = self.head_cover_2 if head_cover_2 == None else head_cover_2
            self.torso = self.torso if torso == None else torso
            self.left_arm = self.left_arm if left_arm == None else left_arm
            self.left_arm_behind = self.left_arm_behind if left_arm_behind == None else left_arm_behind
            self.right_arm = self.right_arm if right_arm == None else right_arm
            self.right_arm_behind = self.right_arm_behind if right_arm_behind == None else right_arm_behind

    class SpriteAPI:
        current_sprite = None

        @staticmethod
        def show_code(expression):

            yuri_sit = {
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
