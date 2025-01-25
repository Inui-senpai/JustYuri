define Khet_winner = 0
default explain = 0

label Khet:
    python:
        DisableTalk()
        boopable = False
        Khet_winner = 0
    menu:
        y "Oh, so you'd like to play some Khet, hm?"
        "Yes.":
            y "Oh, good."
        "No.":
            y "I see..."
            y "Perhaps some other time, then."
            jump ch30_loop

    menu:
        y "Do you want me to explain the rules?"
        "Yes.":
            y "Okay. It might take a while but bare with me."
            jump ExplainRules
        "No.":
            y "I see."
            jump StartKhet

label ExplainRules:
    y "Khet is a chess-like abstract strategy board game using lasers that was formerly known as Deflexion."
    y "Players take turns moving Egyptian-themed pieces around the playing field, firing their low-powered laser diode after each move."
    y "Most of the pieces are mirrored on one or more sides, allowing the players to alter the path of the laser through the playing field. "
    y "When a piece is struck by a laser on a non-mirrored side, it is eliminated from the game."
    y "Let's start with the basics. There are two colors, Silver and Red."
    y "The Silver pieces always take the first turn of the game."
    y "Let me show you the pieces we will be using."
    transform test:
        xpos 0.15
        ypos 0.5
    image temp1 = "images/khet/Silver/pharaoh.png"
    show temp1 at test
    y "At your left you can see the \"Pharaoh\". It's the most important piece, like the King in chess."
    y "If any of the lasers hit it, you lose, so keep it safe!"
    hide temp1
    image temp2 = "images/khet/Silver/anubis.png"
    show temp2 at test
    y "The next piece is called the \"Anubis\". Think of it as the Pharaoh's bodyguard."
    y "If it is hit from front, it negates the laser. However, if it is hit anywhere else, it will be destroyed."
    hide temp2
    image temp3 = "images/khet/Silver/pyramid.png"
    show temp3 at test
    y "This piece is called the \"Pyramid\", which you might've guessed from its looks."
    y "The Pyramid can deflect the laser beam at a 90 degree angle depending on its rotation."
    y "However, if it is hit on a non-mirrored side, it gets destroyed."
    hide temp3
    image temp4 = "images/khet/Silver/scarab.png"
    show temp4 at test
    y "Next is the \"Scarab\". It can deflect laser beams from both sides, Which essentially means it can't be destroyed."
    hide temp4
    image temp5 = "images/khet/Silver/sphinx.png"
    show temp5 at test
    y "And the last piece is called the \"Sphinx\". It's the piece that shoots the laser beam."
    y "It's the only piece which can't move and can be only rotated to shoot vertically or horizontally."
    y "Also, since it's the piece that shoots lasers, it can't be destroyed, like the Scarab."
    hide temp5
    y "You can move your pieces by left-clicking on them and then selecting the target field. The fields the piece can move to will be highlighted in red."
    y "You can also rotate pieces by using arrow keys while the piece is selected: left arrow key to rotate 90 degrees clockwise, right arrow key - to rotate counterclockwise."
    y "You can only move or rotate one piece on your turn, and then your Sphinx will automatically fire according to its rotation."
    y "All pieces except the Sphinx can be moved by one in every direction if the target field is empty. However, Scarab is a little more sneaky because it can SWAP places with the Anubis and Pyramid."
    y "Even the opponent's one! Which makes it a very strategic piece."
    y "As I already hinted above, the main objective of player is to destroy the opponent's Pharaoh using either your or your opponent's laser beam."
    y "I am not really good at explaining things... however I used {a=https://www.boardspace.net/khet/rules_english.pdf}this page{/a} as a guide, which you might find very helpful."
    menu:
        y "Did you understand everything, or would you like me to explain it again?"
        "Yes, I'd like to hear an explanation again.":
            if explain == 0:
                y "Okay."
                $ explain = explain + 1
                jump ExplainRules
            elif explain > 3:
                y "Well alright, but please listen carefully. I don't want to explain it again."
                jump ExplainRules
            else:
                y "..."
                y "[player], I've explained the rules several times now..."
                y "It might be better for you to go to {a=https://www.boardspace.net/khet/rules_english.pdf}this{/a} site and read the rules there..."
                y "I'm sorry, I'm really not the best at explaining things."
                y "Just come back when you feel you are ready to play."
                jump ch30_loop
        "No, I'm fine.":
            y "Okay, then let the game begin."
            jump StartKhet

label StartKhet:
    menu:
        y "What starting configuration would you like to play?"
        "Classic":
            $ temp1 = 0
        "Dynasty":
            $ temp1 = 1
        "Imhotep":
            $ temp1 = 2

    menu:
        y "Would you like me to go easy on you?"
        "Yes.":
            $ temp = 100
        "Maybe.":
            $ temp = 1000
        "No.":
            $ temp = 10000
        "Bring it on.":
            $ temp = 30000

    menu:
        y "Would you like to play first (Silver)?"
        "Silver.":
            $ temp2 = 0
        "Red.":
            $ temp2 = 1

    call screen KhetScreen(temp, temp1, temp2)

label Khet_over:
    if Khet_winner == 0:
        $ show_chr("A-ABAAA-AAAD")
        y "Oh, I won!"
        y "That was quite fun, [player]!"
        y "It's a very interesting game, there's no doubt about that."
        y "Maybe next time..."
    else:
        $ show_chr("A-BEBAA-AMAM")
        y "Congrats, [player]!"
        $ show_chr("A-ABAAA-AAAA")
        y "This is quite fun, I must admit!"
        y "Don't get too ahead of yourself, though. I may have a new trick or two for the next time we play."
    jump ch30_loop

screen KhetScreen(AI_difficulty, gameType, whoStarts):
    fixed:
        area (290, 160, 700, 540)
        default KhetGame = Khet(AI_difficulty, gameType, whoStarts)
        add KhetGame

init python:
    base_path = config.basedir  # directory of the current module file, where all the FLAC bundled binaries are stored
    sys.path.append(base_path + "/game/python-packages/pykhet")
    # khetsearch.so is broken and crashes the game on Linux when called. Temporary workaround.
    if renpy.windows:
        from pykhet.components.types import Position, TeamColor, PieceType, Move, MoveType, Orientation
        from pykhet.games.game_types import ClassicGame, DynastyGame, ImhotepGame
        from pykhet.solvers.minmax import CMinMaxSolver
        import random
        import pygame
        from pykhet.solvers.minmax import MinmaxSolver
        class Khet(renpy.Displayable):
            #Save to file whole bored of game
            #def file(self):
            #    file = open('D:\Ble\map.txt', 'a')
            #    for x in range(0, 10, 1):
            #        file.write("\n")
            #        for y in range(0, 8, 1):
            #            file.write(str(self.game.squares[x][y].color) + "_" + str(self.game.squares[x][y].piece) + " - ")
            #    file.close()
            def __init__(self, AI, gameType, whoStarts):
                renpy.Displayable.__init__(self)
                self.AI = AI
                self.oldst = None
                if gameType == 0:
                    self.game = ClassicGame()
                elif gameType == 1:
                    self.game = DynastyGame()
                else:
                    self.game = ImhotepGame()
                self.laser_in_progress = False
                self.PIXEL_SIZE = 70
                self.laserPath = {}
                self.laser_speed = 0.15
                self.temp = []
                #General
                self.empty = Image("images/khet/empty.png")
                self.laser = Image("images/khet/laser.png")
                self.laserBounce = Image("images/khet/laser_bounce.png")
                self.target = Image("images/khet/target.png")
                self.moves = Image("images/khet/move.png")
                self.boom = Image("images/khet/aaa.png")
                self.destroy_piece = None
                self.winner = None
                self.current_piece = None
                self.board = Image("images/khet/board.png")
                if whoStarts == 0:
                    self.who_turn_is_it = 1
                    self.Yuri_color = TeamColor.red
                    self.Player_color = TeamColor.silver
                else:
                    self.who_turn_is_it = 0
                    self.Yuri_color = TeamColor.silver
                    self.Player_color = TeamColor.red
                self.current_color = TeamColor.silver

                #Silver team
                self.silver = [Image("images/khet/Silver/anubis.png"),Image("images/khet/Silver/pharaoh.png"),Image("images/khet/Silver/pyramid.png"),Image("images/khet/Silver/scarab.png"),Image("images/khet/Silver/sphinx.png")]

                #Red team
                self.red = [Image("images/khet/Red/anubis.png"),Image("images/khet/Red/pharaoh.png"),Image("images/khet/Red/pyramid.png"),Image("images/khet/Red/scarab.png"),Image("images/khet/Red/sphinx.png")]

            def get_mouse_pos(self):
                vw = config.screen_width * 10000
                vh = config.screen_height * 10000
                pw, ph = renpy.get_physical_size()
                dw, dh = pygame.display.get_surface().get_size()
                mx, my = pygame.mouse.get_pos()

                # converts the mouse coordinates from pygame to physical size
                # NEEDED FOR UI SCALING OTHER THAN 100%
                mx = (mx * pw) / dw
                my = (my * ph) / dh

                r = None
                # this part calculates the "true" position
                # it can handle weirdly sized screens
                if vw / (vh / 10000) > pw * 10000 / ph:
                    r = vw / pw
                    my -= (ph - vh / r) / 2
                else:
                    r = vh / ph
                    mx -= (pw - vw / r) / 2

                newx = (mx * r) / 10000
                newy = (my * r) / 10000

                return (newx, newy)

            def start_laser(self, color):
                self.laserPath = self.game.apply_laser(color)
                if "destroyed" in self.laserPath.keys():
                    self.destroy_piece = self.laserPath["destroyed"]
                if  "winner" in self.laserPath.keys():
                    self.winner  = self.laserPath["winner"]
                self.laser_in_progress = True

            def render(self, width, height, st, at):
                global PlayerForYuri
                #################################################################################
                #Check for winner
                global Khet_winner
                if self.winner is not None and self.destroy_piece is None:
                    if self.winner == self.Yuri_color:
                        Khet_winner = 0
                    else:
                        Khet_winner = 1
                    renpy.jump("Khet_over")

                if self.who_turn_is_it == 0 and self.laser_in_progress == False:
                    #Yuri AI
                    solver1 = CMinMaxSolver(max_evaluations=self.AI )
                    move = solver1.get_move(self.game, self.current_color)
                    self.game.apply_move(move)
                    self.start_laser(self.current_color)
                    self.current_color = self.Player_color
                    self.who_turn_is_it = 1

                r = renpy.Render(width, height)

                if self.oldst is None:
                    self.oldst = st

                dtime = st - self.oldst
                self.oldst = st

                def image_rotation(piece,image):
                    if piece.color == "silver":
                        if piece.orientation != 0:
                            t = Transform(self.silver[image], rotate = piece.orientation, rotate_pad = False)
                            shape = renpy.render(t, width, height, st, at)
                        else:
                            shape = renpy.render(self.silver[image], width, height, st, at)
                    else:
                        if piece.orientation != 0:
                            t = Transform(self.red[image], rotate = piece.orientation, rotate_pad = False)
                            shape = renpy.render(t, width, height, st, at)
                        else:
                            shape = renpy.render(self.red[image], width, height, st, at)
                    return shape

                def draw_shape(sx, sy):
                    for x in range(0, 10, 1):
                        for y in range(0, 8, 1):
                            if self.game.squares[x][y].piece is None:
                                shape = renpy.render(self.empty, width, height, st, at)
                                r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * x, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * y))
                            elif self.game.squares[x][y].piece.type == "anubis":
                                r.blit(image_rotation(self.game.squares[x][y].piece,0), (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * x, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * y))
                            elif self.game.squares[x][y].piece.type == "pharaoh":
                                r.blit(image_rotation(self.game.squares[x][y].piece,1), (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * x, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * y))
                            elif self.game.squares[x][y].piece.type == "pyramid":
                                r.blit(image_rotation(self.game.squares[x][y].piece,2), (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * x, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * y))
                            elif self.game.squares[x][y].piece.type == "scarab":
                                r.blit(image_rotation(self.game.squares[x][y].piece,3), (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * x, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * y))
                            elif self.game.squares[x][y].piece.type == "sphinx":
                                r.blit(image_rotation(self.game.squares[x][y].piece,4), (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * x, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * y))

                    if self.laserPath:
                        if len(self.laserPath["path"]) > 0:
                            if self.laser_speed <= 0:
                                self.laser_speed = 0.1
                                self.temp.insert(len(self.laserPath["path"]),self.laserPath["path"][0])
                                self.laserPath["path"].pop(0)
                            else:
                                self.laser_speed -= dtime
                        else:
                            self.laser_in_progress = False
                            self.temp = []
                            if self.destroy_piece is not None:
                                self.game.remove_piece(self.destroy_piece.position)
                                self.destroy_piece = None

                        draw_laser(self.temp,sx, sy)

                def draw_laser(path, sx, sy):
                    if(self.laser_in_progress == True):
                        for i in path:
                            if i.type == "pass":
                                if i.direction == 90 or i.direction == 270:
                                    t = Transform(self.laser, rotate = 90, rotate_pad = False)
                                    shape = renpy.render(t, width, height, st, at)
                                    r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * i.position.x, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * i.position.y))
                                else:
                                    shape = renpy.render(self.laser, width, height, st, at)
                                    r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * i.position.x, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * i.position.y))
                            elif i.type == "bounce":
                                if i.direction == 0:
                                    if PieceType.bounce_direction(self.game.squares[i.position.x][i.position.y].piece, i.direction) == 90:
                                        t = Transform(self.laserBounce, rotate = 270, rotate_pad = False)
                                        shape = renpy.render(t, width, height, st, at)
                                        r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * i.position.x, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * i.position.y))
                                    elif PieceType.bounce_direction(self.game.squares[i.position.x][i.position.y].piece, i.direction) == 270:
                                        shape = renpy.render(self.laserBounce, width, height, st, at)
                                        r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * i.position.x, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * i.position.y))
                                elif i.direction == 90:
                                    if PieceType.bounce_direction(self.game.squares[i.position.x][i.position.y].piece, i.direction) == 0:
                                        t = Transform(self.laserBounce, rotate = 90, rotate_pad = False)
                                        shape = renpy.render(t, width, height, st, at)
                                        r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * i.position.x, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * i.position.y))
                                    elif PieceType.bounce_direction(self.game.squares[i.position.x][i.position.y].piece, i.direction) == 180:
                                        shape = renpy.render(self.laserBounce, width, height, st, at)
                                        r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * i.position.x, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * i.position.y))
                                elif i.direction == 180:
                                    if PieceType.bounce_direction(self.game.squares[i.position.x][i.position.y].piece, i.direction) == 90:
                                        t = Transform(self.laserBounce, rotate = 180, rotate_pad = False)
                                        shape = renpy.render(t, width, height, st, at)
                                        r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * i.position.x, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * i.position.y))
                                    elif PieceType.bounce_direction(self.game.squares[i.position.x][i.position.y].piece, i.direction) == 270:
                                        t = Transform(self.laserBounce, rotate = 90, rotate_pad = False)
                                        shape = renpy.render(t, width, height, st, at)
                                        r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * i.position.x, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * i.position.y))
                                else:
                                    if PieceType.bounce_direction(self.game.squares[i.position.x][i.position.y].piece, i.direction) == 0:
                                        t = Transform(self.laserBounce, rotate = 180, rotate_pad = False)
                                        shape = renpy.render(t, width, height, st, at)
                                        r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * i.position.x, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * i.position.y))
                                    elif PieceType.bounce_direction(self.game.squares[i.position.x][i.position.y].piece, i.direction) == 180:
                                        t = Transform(self.laserBounce, rotate = 270, rotate_pad = False)
                                        shape = renpy.render(t, width, height, st, at)
                                        r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * i.position.x, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * i.position.y))
                            else:
                                shape = renpy.render(self.boom, width, height, st, at)
                                r.blit(shape, (int(sx - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * i.position.x, int(sy - self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * i.position.y))


                r.blit(renpy.render(self.board , width, height, st, at), (-46, -44))

                draw_shape(0, 0)

                def avaible_moves(pos):
                    shape = renpy.render(self.moves, width, height, st, at)
                    for x in range(pos[0]-1, pos[0]+2, 1):
                        for y in range(pos[1]-1, pos[1]+2, 1):
                            if x >= 0 and x < 10 and y >= 0 and y < 8 and (x <> pos[0] or y <> pos[1]):
                                if self.game.squares[x][y].piece is None:
                                    r.blit(shape, (int(0-self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * x, int(0-self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * y))
                                elif self.game.squares[pos[0]][pos[1]].piece.type == "scarab" and (self.game.squares[x][y].piece.type == "pyramid" or self.game.squares[x][y].piece.type == "anubis"):
                                    r.blit(shape, (int(0-self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * x, int(0-self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * y))

                if self.current_piece is not None and self.current_color == self.Player_color:
                    if self.game.squares[self.current_piece[0]][self.current_piece[1]].piece is not None:
                        if self.game.squares[self.current_piece[0]][self.current_piece[1]].piece.color == self.Player_color:
                            a = self.game.squares[self.current_piece[0]][self.current_piece[1]].piece.type
                            b = "Current selected piece: %(s1)s" % {"s1":a }
                            f = Text(b)
                            text_allLines_render = renpy.render(f, width, height, st, at)
                            r.blit(text_allLines_render, (-250, -150))

                    if self.game.squares[self.current_piece[0]][self.current_piece[1]].piece is not None and self.game.squares[self.current_piece[0]][self.current_piece[1]].piece.color == self.Player_color:
                        shape = renpy.render(self.target, width, height, st, at)
                        r.blit(shape, (int(0-self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * self.current_piece[0], int(0-self.PIXEL_SIZE / 2) + self.PIXEL_SIZE * self.current_piece[1]))
                        if self.game.squares[self.current_piece[0]][self.current_piece[1]].piece.type != PieceType.sphinx:
                            avaible_moves(self.current_piece)

                renpy.redraw(self, 0)
                return r

            def event(self, ev, x, y, st):
                import pygame

                def get_piece_pos():
                    mx, my = self.get_mouse_pos()
                    mx -= ((1280 - self.PIXEL_SIZE * 10) / 2) - 35
                    my -= (720 - self.PIXEL_SIZE * 8) - 35
                    px = mx / self.PIXEL_SIZE
                    py = my / self.PIXEL_SIZE
                    if py >= 0 and py < 8 and px >= 0 and px < 10:
                        return (px, py)
                    return None

                def check_move(selected_pos, move_pos):
                    temp1 = Position(selected_pos[0], selected_pos[1])
                    temp2 = Position(move_pos[0], move_pos[1])
                    try:
                        if self.game._on_board(temp2) and (move_pos[0]<>selected_pos[0] or move_pos[1]<>selected_pos[1]) and (move_pos[0]>selected_pos[0]-2 and move_pos[0]<selected_pos[0]+2 and move_pos[1]>selected_pos[1]-2 and move_pos[1]<selected_pos[1]+2):
                            if self.game.squares[move_pos[0]][move_pos[1]].piece is not None and self.game.squares[selected_pos[0]][selected_pos[1]].piece.type == "scarab" and (self.game.squares[move_pos[0]][move_pos[1]].piece.type == "pyramid" or self.game.squares[move_pos[0]][move_pos[1]].piece.type == "anubis"):
                                self.game.apply_move(Move(MoveType.swap, temp1, temp2))
                            else:
                                self.game.apply_move(Move(MoveType.move, temp1, temp2))
                        else:
                            self.current_piece = None
                            return
                    except:
                        self.current_piece = None
                        return

                    self.current_piece = None
                    self.who_turn_is_it = 0
                    self.start_laser(self.current_color)
                    self.current_color = self.Yuri_color

                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1 and self.current_color == self.Player_color and self.laser_in_progress == False:
                    if self.current_piece is None:
                        self.current_piece = get_piece_pos()
                    elif self.game.squares[self.current_piece[0]][self.current_piece[1]].piece is not None and self.game.squares[self.current_piece[0]][self.current_piece[1]].piece.color == self.Player_color:
                        temp_get_piece_pos = get_piece_pos()
                        if temp_get_piece_pos != None:
                            check_move(self.current_piece, get_piece_pos())
                    else:
                        self.current_piece = None

                def orientation_fix(orientation,way):
                    if way == 0:
                        temp = orientation + 90
                    else:
                        temp = orientation - 90

                    if temp > 270:
                        return Orientation.up
                    elif temp < 0:
                        return Orientation.left
                    elif temp == 0:
                        return Orientation.up
                    elif temp == 270:
                        return Orientation.left
                    elif temp == 180:
                        return Orientation.down
                    elif temp == 90:
                        return Orientation.right

                if ev.type == pygame.KEYDOWN and self.current_piece is not None and self.current_color == self.Player_color and self.laser_in_progress == False:
                    if ev.key == pygame.K_LEFT:
                        try:
                            self.game.apply_move(Move(MoveType.rotate, Position(self.current_piece[0],self.current_piece[1]), orientation_fix(self.game.squares[self.current_piece[0]][self.current_piece[1]].piece.orientation,0)))
                        except:
                            self.current_piece = None
                        else:
                            self.current_piece = None
                            self.who_turn_is_it = 0
                            self.start_laser(self.current_color)
                            self.current_color = self.Yuri_color
                    elif ev.key == pygame.K_RIGHT:
                        try:
                            self.game.apply_move(Move(MoveType.rotate, Position(self.current_piece[0],self.current_piece[1]), orientation_fix(self.game.squares[self.current_piece[0]][self.current_piece[1]].piece.orientation,1)))
                        except:
                            self.current_piece = None
                        else:
                            self.current_piece = None
                            self.who_turn_is_it = 0
                            self.start_laser(self.current_color)
                            self.current_color = self.Yuri_color
