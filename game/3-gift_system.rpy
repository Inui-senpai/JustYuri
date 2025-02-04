init -996 python:
    # GiftObjects simplify the gift system by allowing developers to get a gift object based on a gift id
    # They can also add labels or set labels to any gift in the game
    class GiftObject:
        # The Internal id of this gift
        id = None 
        # A string that is executed upon executing Gift.find() to determine whether detection of this gift can happen
        expression = "current_label != \"giftgiving\""
        gifts = []
        labels = []
        intro_labels = []

        def __init__(self, id, intro_label, label, *filenames):
            self.id = id
            self.gifts = []

            if type(filenames[0] == str):
                for filename in filenames:
                    self.gifts.append(filename)
            if intro_label == None:
                self.intro_labels = []
            else:
                self.intro_labels = [intro_label]
            if label == None:
                self.labels = []
            else:
                self.labels = [label]
        
        def is_enabled(self):
            return len(self.labels) > 0 and eval(self.expression)

        def match(self, filename):
            for gift in self.gifts:
                if gift == filename:
                    return True
            return False
        
        def call_intro(self):
            if len(self.intro_labels) > 0:
                renpy.call(random.choice(self.intro_labels))

        def call(self):
            if len(self.labels) > 0:
                renpy.call(random.choice(self.labels))

        def set_expression(self, expression):
            self.expression = expression
            return self

        # Adds one or more labels to this gift. If more than one, then a random label is executed
        def add_label(self, *labels):
            if type(items[0] == str):
                for label in labels:
                    self.labels.append(label)
            return self

        # Clears the list of labels for this gift and sets it to just the specified label for execution
        def set_label(self, label):
            if label == None:
                self.labels = []
            else:
                self.labels = [label]
            return self

        def add_intro(self, *intro_labels):
            if type(items[0] == str):
                for label in intro_labels:
                    self.intro_labels.append(label)
            return self

        def set_intro(self, label):
            if label == None:
                self.intro_labels = []
            else:
                self.intro_labels = [label]
            return self

        def size(self):
            return len(self.intro_labels)

    # The gift API
    class Gift:
        gifts = {
            "black_roses": GiftObject("black_roses", None, "blackroses", "blackroses", "blackrose"),
            "red_roses": GiftObject("red_roses", None, "redroses", "redroses", "redrose", "rose", "roses"),
            "white_roses": GiftObject("white_roses", None, "whiteroses", "whiteroses", "whiterose"),
            "sandal_wood_oil": GiftObject("sandal_wood_oil", None, "sandalwood", "sandalwoodoil", "woodoil"),
            "lavender_oil": GiftObject("lavender_oil", None, "lavender_oil", "lavenderoil"),
            "sweet_dream_oil": GiftObject("sweet_dream_oil", None, "sweet_dream_oil", "sweetdreamoil", "blackrose"),
            "hershey": GiftObject("hershey", None, "hershey", "hershey", "hersheychocolate", "hersheyschocolate", "hersheysbar", "hersheybar", "hersheychocolatebar", "hersheyschocolatebar", "chocolate", "chocolatebar"),
            "lavender_chocolate": GiftObject("lavender_chocolate", None, "lavender_choco", "lavenderchocolate", "lavenderchocolatebar"),
            "mint_chocolate": GiftObject("mint_chocolate", None, "mint_choco", "mintchocolate", "mintchocolatebar"),
            "crane_origami": GiftObject("crane_origami", None, "crane_origami", "craneorigami", "blackrose"),
            "rose_origami": GiftObject("rose_origami", None, "rose_origami", "roseorigami", "blackrose"),
            "bunny_origami": GiftObject("bunny_origami", None, "bunny_origami", "bunnyorigami", "blackrose"),
            "raccoon_plushie": GiftObject("raccoon_plushie", None, "raccoon_plush", "raccoonplush", "raccoonplushie", "raccoon", "plush", "plushie"),
            "diffuser": GiftObject("diffuser", None, "diffuser", "diffuser", "oildiffuser"),
            "horror_book_set": GiftObject("horror_book_set", None, "horror_book_set", "horrorbookset", "horrorbook", "horrorbooks"),
            "high_mountain_tea": GiftObject("high_mountain_tea", None, "tea", "highmountaintea").set_expression("current_label==\"giftgiving\""),
            "imperial_tea": GiftObject("imperial_tea", None, "tea", "imperialtea").set_expression("current_label==\"giftgiving\""),
            "tienchi_tea": GiftObject("tienchi_tea", None, "tea", "tienchitea").set_expression("current_label==\"giftgiving\"")
        }
        last_gifts = []
        intro_labels = ["gift_intro"]

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
            Gift.last_gifts = []
            for id, gift in Gift.gifts.items():
                #if not renpy.exists("game/" + id + ".jy"): # Place a copy of a gift into the game folder
                    #Gift.place_gift(id + ".jy")

                if gift.is_enabled():
                    for potential_gift in os.listdir(Gift.path): 
                        normalized_gift = regex.sub("\.*[^\.]*$", "", potential_gift.lower())
                        normalized_gift = re.sub('[^a-z0-9]', '', normalized_gift)
                        if gift.match(normalized_gift):
                            results.append(gift)
                            Gift.last_gifts.append(gift)
                            os.remove(os.path.join(Gift.path, potential_gift))
            return results
