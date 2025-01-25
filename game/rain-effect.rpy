#Paste this at the bottom of definitions.rpy:

init python:
    renpy.music.register_channel("ambient","sfx",True,tight=True) #This creates a new sound channel called "ambient" with looping enable

define audio.rain = "<loop 0.0>/sfx/rain.ogg" #the sound file that will be player when it's raining
define audio.rainindoors = "<loop 0.0>/sfx/rain2.ogg" #a quieter version of the sound, if you want to use it while indoors use "play ambient rainindoors" isntead of "play sound rainindoors"

label rain: #use "call rain" to start the rain with a 5 seconds fade
    play ambient rain fadein 5.0
    show rain zorder 5 with Dissolve(5.0)
    return

label instant_rain: #use "call instant_rain" to start the rain immediately
    play ambient rain
    show rain zorder 5
    return

label rain_stop: #use call rain_stop to stop the rain with a 5 seconds fade
    stop ambient fadeout 5.0
    hide rain with Dissolve(5.0)
    return

label instant_rain_stop: #use call instant_rain_stop to stop the rain immediately
    stop ambient
    hide rain
    return
    
#------------------------------------------------

#Paste this anywhere in transforms.rpy:

define rain_alpha = .7  # rain alpha
define rain_speed = .05 # lower values makes the rain faster
image rain: #you can edit every line to use your own rain frames
    truecenter
    "/images/weather_system/rain/rain1.png"
    alpha rain_alpha
    rain_speed
    "/images/weather_system/rain/rain2.png"
    alpha rain_alpha
    rain_speed
    "/images/weather_system/rain/rain3.png"
    alpha rain_alpha
    rain_speed
    "/images/weather_system/rain/rain4.png"
    alpha rain_alpha
    rain_speed
    "/images/weather_system/rain/rain5.png"
    alpha rain_alpha
    rain_speed
    "/images/weather_system/rain/rain6.png"
    alpha rain_alpha
    rain_speed
    "/images/weather_system/rain/rain7.png"
    alpha rain_alpha
    rain_speed
    "/images/weather_system/rain/rain8.png"
    alpha rain_alpha
    rain_speed
    repeat
