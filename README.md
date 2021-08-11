# Macropad RP2040 - Hotkeys Project

I had to modify the default code from Adafruit ever so slightly for it to work with OBS if OBS didn't have focus. I had to add a sleep of 0.05. (This was also needed in my [QTPy Streamdeck](https://github.com/djotaku/qtpy_streamdeck)) This seems to have a curious side effect of requiring a double tap to change scenes. But Record and Pause seem to work just fine with just one tap.

## Current Custom Macros

- OBS - this contains a macropad setup for the OBS I use most often. Before this I was using a hacked-together Macropad/Streamdeck using a [QTPy](https://github.com/djotaku/qtpy_streamdeck) with only 2 buttons so I hadn't thought about what I might do with 12 buttons. As of 20210801, it only makes use of the top 9 keys. It also does not do anything with the Encoder button press. 
