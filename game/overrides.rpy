## This file is for overriding specific declarations from DDLC
## Use this if you want to change a few variables, but don't want
## to replace entire script files that are otherwise fine.

## Normal overrides
## These overrides happen after any of the normal init blocks in scripts.
## Use these to change variables on screens, effects, and the like.
init 10 python:
    #####################################
    #TURNS ON AND OFF THE DEV TOOLS######
    #####################################
    config.developer = "auto"
    dev_access = config.developer
    config.rollback_enabled = False
    #####################################
    #TURNS ON AND OFF THE DEV TOOLS######
    #####################################
    #Overrides definitions.rpyc
    # for some reason, the framerate is maxing out to like 300 fps jfc.
    renpy.maximum_framerate(60)
    pass

## Early overrides
## These overrides happen before the normal init blocks in scripts.
## Use this in the rare event that you need to overwrite some variable
## before it's called in another init block.
## You likely won't use this.
init -10 python:
    pass

## Super early overrides
## You'll need a block like this for creator defined screen language
## Don't use this unless you know you need it
python early:
    pass
