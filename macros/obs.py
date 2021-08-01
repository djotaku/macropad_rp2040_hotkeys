# MACROPAD Hotkeys example: Microsoft Edge web browser for Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'OBS', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xFF0000, 'REC', [Keycode.CONTROL, Keycode.ALT, Keycode.R]),
        (0xD4D900, 'PAUSE', [Keycode.CONTROL, Keycode.ALT, Keycode.P]),
        (0x00D900, 'STREAM', [Keycode.CONTROL, Keycode.ALT, Keycode.S]),      # Scroll up
        # 2nd row ----------
        (0x101010, 'Scn 1', [Keycode.CONTROL, Keycode.ALT, '1']),
        (0x101010, 'Scn 2', [Keycode.CONTROL, Keycode.ALT, '2']),
        (0x101010, 'Scn 3', [Keycode.CONTROL, Keycode.ALT, '3']),                     # Scroll down
        # 3rd row ----------
        (0x101010, 'Scn 4', [Keycode.CONTROL, Keycode.ALT, '4']),
        (0x101010, 'Scn 5', [Keycode.CONTROL, Keycode.ALT, '5']),
        (0x101010, 'Scn 6', [Keycode.CONTROL, Keycode.ALT, '6']),
        # 4th row ---------- (as of 20210801 these are unused for my OBS config)
        (0x000000, 'Ada', [Keycode.CONTROL, 'n', -Keycode.COMMAND,
                           'www.adafruit.com\n']),   # Adafruit in new window
        (0x800000, 'Digi', [Keycode.CONTROL, 'n', -Keycode.COMMAND,
                            'www.digikey.com\n']),   # Digi-Key in new window
        (0x101010, 'Hacks', [Keycode.CONTROL, 'n', -Keycode.COMMAND,
                             'www.hackaday.com\n']), # Hack-a-Day in new win
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w']) # Close tab
    ]
}
