#the parameter, cursorlist, expects a list of list containg an image, a pos, and an offset, with the exception that the default cursor should have "default" instead of a position


#found from this post: https://lemmasoft.renai.us/forums/viewtopic.php?t=20703

init python:
    
    class custom_cursor(renpy.Displayable):
        
        def __init__(self, cursorlist, dark=False, **kwargs):
            super(custom_cursor, self).__init__(**kwargs)
            
            self.x = 0
            self.y = 0
            self.cursorlist = cursorlist
            
            self.child = None
            self.dark = dark
            if dark:
                self.fl = renpy.displayable("no_flashlight.png")
            renpy.timeout(1)
            return
            
        def render(self, width, height, at, st):
            if self.child:
                rc = renpy.render(self.child, width, height, at, st)
                r = renpy.Render(config.screen_width, config.screen_height)
                r.blit(rc, (self.x - self.xoff, self.y - self.yoff))
                if self.dark:
                    rd = renpy.render(self.fl, width, height, at, st)
                    r.blit(rd, (self.x - config.screen_width, self.y - config.screen_height))
            else:
                if self.dark:
                    r = renpy.Render(config.screen_width, config.screen_height)
                    rd = renpy.render(self.fl, width, height, at, st)
                    r.blit(rd, (0, 0))
                else:
                    r = renpy.Render(0, 0)
            return r
            
        def event(self, ev, x, y, st):
            self.child = None
            if 0 <= x <= config.screen_width and 0 <= y <= config.screen_height:
                if self.dark:
                    self.fl = renpy.displayable("flashlight.png")
                for c in self.cursorlist:
                    if c[1] == "default":
                        self.child = renpy.displayable(c[0])
                        self.xoff = c[2][0]
                        self.yoff = c[2][1]
                        break
                        
                for c in self.cursorlist:
                    if c[1] != "default":
                        if c[1][0] <= x <= c[1][2] + c[1][0] and c[1][1] <= y <= c[1][3] + c[1][1]:
                            self.child = renpy.displayable(c[0])
                            self.xoff = c[2][0]
                            self.yoff = c[2][1]
                self.x = x
                self.y = y
            elif self.dark:
                self.fl = renpy.displayable("no_flashlight.png")
            renpy.redraw(self, 0)
            return
                        
        def visit(self):
            if self.dark:
                return [self.child, self.fl]
            return [self.child]
            
            
