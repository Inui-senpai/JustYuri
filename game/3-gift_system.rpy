init -996 python:
    # GiftObjects simplify the gift system by allowing developers to get a gift object based on a gift id
    # They can also add labels or set labels to any gift in the game
    class GiftObject:
        # The Internal id of this gift
        id = None 
        # A string that is executed upon executing Gift.find() to determine whether detection of this gift can happen
        expression = "True"
        gifts = []
        labels = []
        intro_labels = []

        def __init__(self, id, intro_label, label, *filenames):
            self.id = id
            for filename in filenames:
                self.gifts.append(filename)
            self.labels.append(label)
            if label == None:
                self.intro_labels = []
            else:
                self.intro_labels = [label]
        
        def is_enabled():
            return eval(expression)

        def match(filename):
            for gift in self.gifts:
                if gift == filename:
                    return True
            return False
        
        def set_expression(thingy):
            self.expression = thingy
            return self

        # Adds one or more labels to this gift. If more than one, then a random label is executed
        def add_label(*items):
            for item in items:
                self.labels.append(item)
            return self

        # Clears the list of labels for this gift and sets it to just the specified label for execution
        def set_label(label):
            if label == None:
                self.labels = []
            else:
                self.labels = [label]
            return self

        def add_intro(*items):
            for item in items:
                self.intro_labels.append(item)
            return self

        def set_intro(label):
            if label == None:
                self.intro_labels = []
            else:
                self.intro_labels = [label]
            return self

    # The gift API
    class Gift:
        gifts = {
            "black_roses": GiftObject("black_roses", None, "", "blackroses", "blackrose"),
            "red_roses": GiftObject("red_roses", None, "", "redroses", "redrose", "rose", "roses"),
            "white_roses": GiftObject("white_roses", None, "", "whiteroses", "whiterose"),
            "sandal_wood_oil": GiftObject("sandal_wood_oil", None, "", "sandalwoodoil", "woodoil"),
            "lavender_oil": GiftObject("lavender_oil", None, "", "lavenderoil"),
            "sweet_dream_oil": GiftObject("sweet_dream_oil", None, "", "sweetdreamoil", "blackrose"),
            "hershey": GiftObject("hershey", None, "", "hershey", "hersheychocolate", "hersheyschocolate", "hersheysbar", "hersheybar", "hersheychocolatebar", "hersheyschocolatebar", "chocolate", "chocolatebar"),
            "lavender_chocolate": GiftObject("lavender_chocolate", None, "", "lavenderchocolate", "lavenderchocolatebar"),
            "mint_chocolate": GiftObject("mint_chocolate", None, "", "mintchocolate", "mintchocolatebar"),
            "crane_origami": GiftObject("crane_origami", None, "", "craneorigami", "blackrose"),
            "rose_origami": GiftObject("rose_origami", None, "", "roseorigami", "blackrose"),
            "bunny_origami": GiftObject("bunny_origami", None, "", "bunnyorigami", "blackrose"),
            "raccoon_plushie": GiftObject("raccoon_plushie", None, "", "raccoonplush", "raccoonplushie", "raccoon", "plush", "plushie"),
            "diffuser": GiftObject("diffuser", None, "", "diffuser", "oildiffuser"),
            "horror_book_set": GiftObject("horror_book_set", None, "", "horrorbookset", "horrorbook", "horrorbooks")
        }

        path = os.path.join(config.basedir, "characters")

        @staticmethod
        def place_gift(gift, contents = None, directory = os.path.join(config.basedir, "game")):
            path = os.path.join(directory, gift)
            if not os.path.isfile(path):
                try:
                    with open(path, "wb") as file:
                        if contents != None:
                            file.write(str(contents))
                except:
                    pass

        @staticmethod
        def find():
            results = []

            for id, gift in gift_list:
                if not renpy.exists("game/" + id + ".jy"): # Place a copy of a gift into the game folder
                    place_gift(id + ".jy")
                if gift.is_enabled():
                    for potential_gift in os.listdir(path): 
                        normalized_gift = potential_gift.lower()
                        normalized_gift = re.sub('[^a-z0-9]', '', normalized_gift)
                        if gift.match(normalized_gift):
                            results.append(gift)
                            os.remove(os.path.join(path, potential_gift))
            return results
