init -998 python:
    class ConfigAPI:
        configurations = {}
        mod_configurations = {}

        @staticmethod
        def process_config(config : Config):
            if type(config.id) != str:
                print_fatal("Tried to register a configuration with an invalid id. Should be a string")
            if type(config.name) != str:
                config.name = config.id
            final_options = []
            options = config.setup()

            for option in options:
                option_type = type(option)
                if not isinstance(option, Option):
                    print("  - Failed to add option " + type_str(option) + " as it is not a valid option type")
                    continue
                
                if option_type == OptionSeparator:
                    pass
                elif option_type == OptionTitle:
                    option_label_type = type(option.title)
                    print(str(type(option.title)))
                    if option_label_type != str and not is_callable(option.title):
                        print_error("  - Failed to add option " + type_str(option) + " as the title is not a valid type")
                elif option_type == OptionBar:
                    option_label_type = type(option.labels)
                    if option_label_type != str and option_label_type != tuple and not is_callable(option.labels):
                        print_error("  - Failed to add option " + type_str(option) + " as the label is not a valid type")
                elif option_type == OptionButton:
                    option_label_type = type(option.labels)
                    if option_label_type != tuple:
                        print_error("  - Failed to add option " + type_str(option) + " as the label is not a valid tuple")
                elif option_type == OptionCheckbox:
                    option_label_type = type(option.labels)
                    if option_label_type != str and option_label_type != tuple and not is_callable(option.labels):
                        print_error("  - Failed to add option " + type_str(option) + " as the label is not a valid type")
                elif option_type == OptionChecklist:
                    option_label_type = type(option.label)
                    if option_label_type != str and option_label_type != tuple and not is_callable(option.label):
                        print_error("  - Failed to add option " + type_str(option) + " as the label is not a valid type")
                else:
                    print("  - Failed to add option " + type_str(option) + " as it is not a valid option type")
                    continue

                final_options.append(option)

            if len(final_options) == 0:
                print_fatal("Tried to register a configuration with no valid options. Add options or fix erroring options")
            return final_options

        @staticmethod
        def register_config(config : Config):
            options = ConfigAPI.process_config(config)
            ConfigAPI.configurations[config] = options

        @staticmethod
        def register_mod_config(config : Config):
            if not config.id in submods.mods:
                print_error(KeyError("Tried to register a config to a non-existent mod. Skipping..."))
                return
            options = ConfigAPI.process_config(config)
            ConfigAPI.mod_configurations[config.id] = {config: options}
        
    class Option():
        def default_action(self):
            pass

    class OptionSeparator(Option):
        pass

    class OptionTitle(Option):
        title = None
        def __init__(self, title : str):
            self.title = title

    class OptionBar(Option):
        labels = None
        obj = None
        variable = None
        value = 0
        action = None
        offset = 0
        min = 0
        max = 2
        step = 1

        def __init__(self, obj, variable, labels, init_action=None, action=None, offset=0, min=0, max=2, step=1):
            self.obj = obj
            self.variable = variable
            self.labels = labels
            self.action = action
            self.offset = offset
            self.min = min
            self.max = max
            self.step = step
            self.init_action = init_action if init_action else self.default_init_action
            self.init_action(self)

        @staticmethod
        def default_init_action(self):
            value = getattr(self.obj, self.variable)
            if type(value) == float or type(value) == int:
                self.value = value
            else:
                self.value = self.min

        @staticmethod
        def default_action(self):
            setattr(self.obj, self.variable, self.value)

    class OptionButton(Option):
        labels = None
        obj = None
        variable = None
        value = None
        values = None
        action = None
        starting_index = 0

        def __init__(self, obj, variable, labels, values=None, init_action=None, action=None):
            self.obj = obj
            self.variable = variable
            self.labels = labels
            self.action = action
            self.values = values
            self.init_action = init_action if init_action else self.default_init_action
            self.init_action(self)

        @staticmethod
        def default_init_action(self):
            value = getattr(self.obj, self.variable)
            if type(value) == int:
                self.value = value
            else:
                self.value = 0
                
        @staticmethod
        def default_action(self):
            self.value += 1
            self.value = self.value % len(self.labels)
            setattr(self.obj, self.variable, self.values[self.value] if self.values else self.value)
            self.init_action(self)

    class OptionCheckbox(Option):
        labels = None
        obj = None
        variable = None
        value = None
        action = None
        values = None

        def __init__(self, obj, variable, labels, init_action=None, action=None):
            self.obj = obj
            self.variable = variable
            self.labels = labels
            self.action = action
            self.init_action = init_action if init_action else self.default_init_action
            self.init_action(self)

        @staticmethod
        def default_init_action(self):
            self.value = True if getattr(self.obj, self.variable) else False

        @staticmethod
        def default_action(self):
            self.value = not self.value
            setattr(self.obj, self.variable, self.value)

    class OptionChecklist(Option):
        label = None
        labels = None
        obj = None
        variable = None
        value = None
        init_action = None
        action = None

        def __init__(self, obj, variable, label, labels, values=None, init_action=None, action=None):
            self.obj = obj
            self.variable = variable
            self.label = label
            self.labels = labels
            self.values = values
            self.action = action
            self.init_action = init_action if init_action else self.default_init_action
            self.init_action(self)

        @staticmethod
        def default_init_action(self):
            value = getattr(self.obj, self.variable)
            self.value = value if type(value) == int else 0

        @staticmethod
        def default_action(self, index):
            self.value = index
            setattr(self.obj, self.variable, self.values[self.value] if self.values else self.value)
            
    class ScreenSpacer():
        pass

    class ActionButton(Action):
        option = None
        callback = None

        def __init__(self, option : Option):
            self.option = option
            self.callback = option.action if option.action else option.default_action
        def __call__(self):
            self.callback(self.option)
            renpy.restart_interaction()

    class ActionCheckbox(Action):
        option = None
        callback = None

        def __init__(self, option : Option):
            self.option = option
            self.callback = option.action if option.action else option.default_action
        def __call__(self):
            self.callback(self.option)
            renpy.restart_interaction()
        def get_selected(self):
            return self.option.value

    class ActionChecklist(Action):
        option = None
        callback = None
        index = 0

        def __init__(self, option : Option, index: int):
            self.option = option
            self.callback = option.action if option.action else option.default_action
            self.index = index
        def __call__(self):
            if self.get_selected():
                return
            self.callback(self.option, self.index)
            renpy.restart_interaction()
        def get_selected(self):
            return self.option.value == self.index
            
init -999 python:
    class Config:
        id = None
        name = None
        def setup():
            pass

        

