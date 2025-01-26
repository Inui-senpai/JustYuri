init -2 python:
    import random
    import math

    class Quit(Action, DictEquality):
        """
        :doc: menu_action

        Quits the game.

        `confirm`
            If true, prompts the user if he wants to quit, rather
            than quitting directly. If None, asks if and only if
            the user is not at the main menu.
        """

        def __init__(self, confirm=None):
            self.confirm = confirm

        def __call__(self):

            confirm = self.confirm

            if confirm is None:
                confirm = (not main_menu) and _confirm_quit

            if confirm:
                if config.autosave_on_quit:
                    renpy.force_autosave()
                if renpy.seen_label('ch30_main') == False:
                    layout.yesno_screen(layout.QUIT, Quit(False))
                else:
                    renpy.jump('random_farewell')
            else:
                renpy.jump("_quit")

    class Quit_no_farewell(Action, DictEquality):
        """
        :doc: menu_action

        Quits the game.

        `confirm`
            If true, prompts the user if he wants to quit, rather
            than quitting directly. If None, asks if and only if
            the user is not at the main menu.
        """

        def __init__(self, confirm=None):
            self.confirm = confirm

        def __call__(self):

            confirm = self.confirm

            if confirm is None:
                confirm = (not main_menu) and _confirm_quit

            if confirm:
                if config.autosave_on_quit:
                    renpy.force_autosave()
                if renpy.seen_label('ch30_main') == False:
                    layout.yesno_screen(layout.QUIT, Quit(False))
                else:
                    renpy.jump('save_and_quit_but_its_abrupt')
            else:
                renpy.jump("_quit")