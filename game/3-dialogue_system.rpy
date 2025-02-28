#persistent.dialogue_memory will house the main persistent info on dialogues
default blocked_dialogues = []

#use renpy.has_seen to determine if something has been seen before.
init -998 python:
    #can_talk = True
    #can_interrupt = True

    class DialogueAPI:
        dialogues = {}
        categories = {}
        queued_dialogues = []

        category_talk = "actives"
        category_goodbye = "farewells"
        category_greetings = "greetings"
        category_idle = "idles"
        category_hdy = "hdy"

        @staticmethod
        def register(*dialogue_options):
            for dialogue in dialogue_options:
                if isinstance(dialogue, Dialogue): 
                    if type(dialogue.label) != str:
                        print_fatal(TypeError("Label needs to be a string type"))
                        continue
                    dialogues[dialogue.label] = dialogue
                    category = dialogue.get_category()
                    if category in categories:
                        categories[category].append(dialogue)
                    else:
                        categories[category] = [dialogue]
                    print_debug(" - Registered dialogue with the id " + dialogue.label)
                else:
                    print_error(TypeError("Dialogue option " + type_str(dialogue) + " is not an instance of Dialogue"))
        
        @staticmethod
        def call(id : str = "idles", call_dialogue : bool = False, interrupt : bool = False):
            """
            Calls a specific dialogue based on the id provided.
            By default, the id represents a dialogue category that should be called.
            If call_dialogue is set to True, then it will directly call a registered dialogue based on the id
            If interrupt is set to True, then it will interrupt any dialogue that may be already running
            """
            selected_dialogue = None
            if call_dialogue: # If we only want to call a dialogue directly
                if not id in DialogueAPI.dialogues:
                    print_error(NameError("Dialogue " + id + " has not been registered yet. Skipping..."))
                    return False
                
                DialogueAPI.dialogues[id].call(interrupt)
            else: # If we want to call a specific category based on conditions
                if id == category_talk:
                    # First, we are going to scan the categories registry for any dialogue to execute
                    selected_dialogues = []
                    ordered_dialogues = {}
                    for dialogue in DialogueAPI.categories[id]:
                        if dialogue.is_available():
                            selected_dialogues.append(dialogue)
                    
                    # Second, populate the ordered_dialogues dictionary with every sub-category and dialogue option available to us
                    for dialogue in selected_dialogues:
                        categories = dialogue.get_sub_categories()
                        if not categories: # If it does not have any categories, just throw it in the base category
                            ordered_dialogues[dialogue.name] = dialogue
                        else: # Populate the ordered_dialogues with every sub_category of this dialogue + the dialogue itself
                            parent_category = None
                            for category in categories:
                                if not parent_category:
                                    if not ordered_dialogues[category]:
                                        ordered_dialogues[category] = []
                                    parent_category = ordered_dialogues[category]
                                else:
                                    if not parent_category[category]:
                                        parent_category[category] = []
                                    parent_category = parent_category[category]
                            parent_category[dialogue.name] = dialogue

                    # Open the talk dialogue menu
                    renpy.call_screen("talk_menu", ordered_dialogues)
                else:

                    # First, we are going to scan the categories registry for any dialogue to execute
                    selected_dialogues = []
                    importance = -sys.maxsize
                    if not id in DialogueAPI.categories: # If the primary dialogue category has not been registered, throw an error
                        print_error(NameError("Dialogue category " + id + " has not been registered yet. Skipping..."))
                        return False

                    for dialogue in DialogueAPI.categories[id]:
                        if dialogue.is_available():
                            if dialogue.importance > importance:
                                selected_dialogues.clear()
                                selected_dialogues.append(dialogue)
                                inportance = dialogue.importance
                            elif dialogue.importance == importance:
                                selected_dialogues.append(dialogue)

                    if not selected_dialogues: # If the primary dialogue category does not have any available dialogues after processing, throw an error
                        print_error(NameError("Dialogue category " + id + " does not have any available dialogue options. Skipping..."))
                        return False

                    selected_dialogue = controlled_random(dialogue_list, selection_detail)

                    if selection_detail == "idles":
                        persistent.current_yuriidle = selected_dialogue
                    # Next, call the dialogue based on what parent category it is under
                    
                    if selection_detail in ["idles", "greetings", "hdy"]:
                        selected_dialogue = controlled_random(dialogue_list, selection_detail)

                    if selection_detail == "idles":
                        persistent.current_yuriidle = selected_dialogue
                    
                    elif selection_detail == category_goodbye:
                        farewell_options = []
                        for dialogue_name in dialogue_list:
                            farewell_options.append((dialogue_db[dialogue_name].name, dialogue_name))
                        if len(dialogue_list) > 3:
                            farewell_options = random.sample(farewell_options, k=3)
                        farewell_options.append(("Nevermind", "return"))
                        selected_dialogue = renpy.display_menu(farewell_options)

                    #Activation
                    if selected_dialogue != "return":
                        print_debug("calling: " + selected_dialogue)
                        renpy.call(selected_dialogue)

                    #Post-Activation
                    if selection_detail == "idles" or selection_detail == "hdy":
                        persistent.current_yuriidle = 0
                    loop_again = True
                    return
                    # else:
                    print_debug(selection_method)
                    y("Selection method not found")
                    return True
    
    # works with a list of the 5 most recent dialogues (blocked_dialogues) and chooses a random dialogue from the list that isn't in the blocked_dialogues category.
    #def controlled_random(selected_dialogues, category):
        #if not selected_dialogues:
            #print_fatal(NameError("Attempted to get a random dialogue from an empty dialogue list for category " + category))
            #return None

        #global blocked_dialogues
        #selected_dialogue = random.choice(selected_dialogues)
        #selectable_dialogues = set(selected_dialogues) - blocked_dialogues

        #if not selectable_dialogues:
            #blocked_dialogues.clear()
            #selectable_dialogues = set(selected_dialogues)
        
        #chosen_dialogue = random.choice(selectable_dialogues)

        #if len(blocked_dialogues) > 5:
            #blocked_dialogues.pop(-1)
        #blocked_dialogues.insert(0, chosen_dialogue)
        #return selected_dialogue
    
    #works with a list of the 3 most recent dialogues (blocked_dialogues) and chooses a random dialogue from the list that isn't in the blocked_dialogues category.
    def controlled_random(dlist, selection_detail):
        global blocked_dialogues
        size_of_blocked_dialogues = 5

        dlist_no_block = list(set(dlist) - set(blocked_dialogues))
        if dlist_no_block == []:
            if blocked_dialogues == []:
                renpy.error("No dialogues left! category type: " + selection_detail)
            else:
                chosen_dialogue = blocked_dialogues.pop(-1)

        else:
            chosen_dialogue = random.choice(dlist_no_block)

        if len(blocked_dialogues) > size_of_blocked_dialogues:
            blocked_dialogues.pop(-1)
        blocked_dialogues.insert(0, chosen_dialogue)
        return chosen_dialogue

init -999 python:
    class Dialoguee:
        def __init__(self, label, name = None, category = None, conditions = [], importance = 0):
            self.label = label
            self.name = name if name else label
            self.category = category.split("/") if category != None else []
            self.conditions = conditions
            self.importance = importance
        
        def call(self, interrupt = False):
            global can_talk

            if can_talk:
                print_debug("Calling dialogue: " + self.label)
                can_talk = False
                renpy.call(self.label)
            elif interrupt and can_interrupt:
                def run(self):
                    print_debug("Interrupting with dialogue: " + self.label)
                    can_talk = False
                    renpy.call(self.label)
                    pass
                renpy.invoke_in_main_thread(run, self)
            else:
                if self.can_queue():
                    print_debug("Queuing dialogue: " + self.label)
                    DialogueAPI.queued_dialogues.append(self.label)

        def get_category(self):
            return self.category[0] if len(self.category) > 0 else "unknown"

        def get_sub_categories(self):
            return self.category[1:]
        
        def can_queue(self):
            self.label in DialogueAPI.queued_dialogues

        def is_available(self):
            if not self.conditions:  # Check if the list is empty
                return True  # No conditions, so all are considered met

            for condition in self.conditions:
                try:
                    if not eval(condition):
                        print_debug("Condition not met for " + self.label + ": " + condition)
                        return False
                except Exception as e:
                    print("A fatal error has occured with one of the conditions for dialogue " + self.label)
                    print_fatal(e, False) # Crash if any errors happen so the mod creator can fix the issue
                    return False

            return True  # All conditions evaluated successfully


init -999 python:
    #from datetime import datetime
    import datetime
    from time_module import time_shift, time_interval_check

    ####
    #Dialogue Scripts
    ###

    #dialogue_db will be the primary dictionary called on for information
    dialogue_db = {}
    queued_dialoguee = []

    #This is to make sure dialogue_memory is a dictionary, and not None, before the dialogues are added to dialogue_db
    if persistent.dialogue_memory == None:
        persistent.dialogue_memory = {}
    #This class is brought up at every initialization for each dialogue.

    #This data doesn't need to be persistently stored, just called on.
    class Dialogue:
        #Initiatlization of the class is mostly filling in variables
        def __init__(self, label, category, conditions = [], importance = 0, name = None, sub_category = None):
            #name of label which houses the dialogue
            self.label = label
            #type - idle, active, greeting, or farewell
            self.category = category
            #conditions, arbitrary, but must be written in form of python check for eval
            self.conditions = conditions
            #loads in the memory automatically when initialized
            if label in persistent.dialogue_memory:
                self.memory = persistent.dialogue_memory[label]
            else:
                self.memory = []
            #Importance is the degree to which a dialogue is important. Higher importance means it bypasses previous dialogues.
            #0 for normal dialogues
            #20 for absolutely necessary dialogues, must be a follow-up to something previous
            #10 for timed-events, like holidays.
            #-1 exclusively reserved for the dialogue where Yuri asks whether or not it's fine to bring up old topics (Asks for switching selection method from pool_nonrepeat to pool)
            self.importance = importance
            #name and sub_category are with relation to appearance in menus.
            self.name = name
            self.sub_category = sub_category
            #has to be in the form that can be inserted into time_interval_check, namely a list of two dictionaries that had stuff in it.
            # [{"year": 2000, "month": 1, "day": 1, "hour":1, "minute":32},
            # {"year": 2000, "month": 1, "day": 1, "hour":1, "minute":33}]
            #time condition now treated as normal condition in self.conditions
            
        #checks if the conditions have been met for this dialogue to trigger
        def conditions_met(self):
            if not self.conditions:  # Check if the list is empty
                return True  # No conditions, so all are considered met

            for condition in self.conditions:
                try:
                    if not eval(condition):
                        print_debug("Condition not met for " + self.label + ": " + condition)
                        return False
                except Exception as e:
                    return False  # Consider failure if evaluation fails

            return True  # All conditions evaluated successfully

    #adds the dialogue class to the database
    def add_dialogue(dialogue_class):
        dialogue_db[dialogue_class.label] = dialogue_class

    def call_dialogue(selection_method = "pool", selection_detail = "idles", screener = False):
        #selection methods range from "pool_nonrepeat" to "pool" to "specific"
        if selection_method == "specific":
            if renpy.has_label(selection_detail):
                if screener:
                    print(dialogue_db[selection_detail].conditions)
                    print(dialogue_db[selection_detail].conditions_met())
                else:
                    print_debug("calling: " + selection_detail)
                    renpy.call(selection_detail)
            else:
                print_debug(selection_detail + ": label does not exist")
                renpy.error(selection_detail + ": label does not exist")
                return
        
        elif selection_method == "pool":
            #The first thing is to scan the dialogue_db, and select out those dialogues which are 
            # within the right category and have conditions_met, then add said dialogues to a list
            dialogue_list = []
            importance_value = -100
            for dialogue_name in dialogue_db.keys():
                current_dialogue = dialogue_db[dialogue_name]
                if current_dialogue.category == selection_detail:
                    if current_dialogue.conditions_met():

                        #if selection_method == "pool" or renpy.seen_label(dialogue_name):

                        #if the dialogue is labelled as a higher importance than the current dialogue list, then the dialogue list resets to only contain the new entry
                        # Otherwise, if the dialogue is the same importance, it gets added to the current dialogue list
                        if current_dialogue.importance == importance_value:
                            dialogue_list.append(dialogue_name)
                        elif current_dialogue.importance > importance_value:
                            dialogue_list = [dialogue_name]
                            importance_value = current_dialogue.importance

            if screener:
                print(dialogue_list)
                return

            #Pre-Activation Selection
            if selection_detail in ["idles", "greetings", "hdy"]:
                selected_dialogue = controlled_random(dialogue_list, selection_detail)

                if selection_detail == "idles":
                    persistent.current_yuriidle = selected_dialogue
            
            elif selection_detail == "actives":
                active_dict = {}
                for dialogue_name in dialogue_list:
                    current_dialogue = dialogue_db[dialogue_name]
                    if current_dialogue.sub_category in active_dict:
                        # append to the dictionary's sub_category item the name (what is seen to player) and label (the label the code will call on the dialogue with.)
                        active_dict[current_dialogue.sub_category].append((current_dialogue.name, current_dialogue.label))
                    else:
                        active_dict[current_dialogue.sub_category] = [(current_dialogue.name, current_dialogue.label)]
                
                #converts all elements of scroll_button_items list into list of two-element list, 0th index being the name of the element, 1th element being 0.
                scroll_button_items = list(active_dict.keys()) 
                for i, item in enumerate(scroll_button_items):
                    scroll_button_items[i] = [item, 0]
                
                #send info to the custom active list.
                selected_dialogue = renpy.call_screen(
                    "three_choice_menu", 
                    active_dict, 
                    scroll_button_items, 
                    [("Would it be fine if I changed the music a little?", "change_music"), ("Nevermind", "prompt_menu"), ("Why don't you change outfits, Yuri?", "changeoutfit")],
                    random.sample(list(active_dict.keys()), len(active_dict)), # Changed this line
                    "no", 
                    0)
            
            elif selection_detail == "farewells":
                farewell_options = []
                for dialogue_name in dialogue_list:
                    farewell_options.append((dialogue_db[dialogue_name].name, dialogue_name))
                if len(dialogue_list) > 3:
                    farewell_options = random.sample(farewell_options, k=3)
                farewell_options.append(("Nevermind", "return"))
                selected_dialogue = renpy.display_menu(farewell_options)



            #Activation
            if selected_dialogue != "return":
                print_debug("calling: " + selected_dialogue)
                renpy.call(selected_dialogue)



            #Post-Activation
            if selection_detail == "idles" or selection_detail == "hdy":
                persistent.current_yuriidle = 0
            loop_again = True
            return
        else:
            print_debug(selection_method)
            y("Selection method not found")
            return
            
#########################
## MEMORY FUNCTIONS #####
#########################

    #adds memory to the persistent.dialogue_memory dictionary
    def update_memory(memory_name, memory = ""):
        #store memory list into the persistent.dialogue_memory
        if memory_name in persistent.dialogue_memory:
            if memory != "":
                if persistent.dialogue_memory[memory_name] == [""]:
                    persistent.dialogue_memory[memory_name] = [memory]
                else:
                    persistent.dialogue_memory[memory_name].append(memory)
        else:
            persistent.dialogue_memory[memory_name] = [memory]

    def remove_memory(memory_name, memory = ""):
        if memory_name in persistent.dialogue_memory:
            #If the command is to delete the entire memory, delete it from the dictionary
            if memory == "":
                persistent.dialogue_memory.pop(memory_name, None)
            #Otherwise, if it's only one element of the memory, remove that item only, while leaving the rest of the memory intact.
            elif memory in persistent.dialogue_memory[memory_name]:
                persistent.dialogue_memory[memory_name].remove(memory)


    def check_memory(memory_name, memory = ""):
        if memory_name in persistent.dialogue_memory:
            if memory == "":
                return True
            elif memory in persistent.dialogue_memory[memory_name]:
                return True
            else:
                return False
        else:
            return False

    def return_memory(memory_name):
        if memory_name in persistent.dialogue_memory:
            return persistent.dialogue_memory[memory_name]
        else:
            print_error(memory_name + " not found in persistent.dialogue_memory. Could not return_memory.")

    def reset_memory():
        persistent.dialogue_memory = {}

