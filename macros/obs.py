from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'OBS', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xFF0000, 'REC', [Keycode.CONTROL, Keycode.ALT, Keycode.R]),
        (0xD4D900, 'PAUSE', [Keycode.CONTROL, Keycode.ALT, Keycode.P]),
        (0x00D900, 'STREAM', [Keycode.CONTROL, Keycode.ALT, Keycode.E]),
        # 2nd row ----------
        (0x101010, 'Pre-', [Keycode.CONTROL, Keycode.ALT, '1']),
        (0x101010, 'Appeal', [Keycode.CONTROL, Keycode.ALT, '2']),
        (0x101010, 'Title', [Keycode.CONTROL, Keycode.ALT, '3']),
        # 3rd row ----------
        (0x101010, 'Me ^', [Keycode.CONTROL, Keycode.ALT, '4']),
        (0x101010, 'Game ^', [Keycode.CONTROL, Keycode.ALT, '5']),
        (0x101010, 'Med', [Keycode.CONTROL, Keycode.ALT, '6']),
        # 4th row ----------
        (0x000000, 'BRB', [Keycode.CONTROL, Keycode.ALT, '7']),
        (0x800000, 'none', [Keycode.CONTROL, 'n', -Keycode.COMMAND,
                            'www.digikey.com\n']),   # Digi-Key in new window
        (0x101010, 'none', [Keycode.CONTROL, 'n', -Keycode.COMMAND,
                             'www.hackaday.com\n']), # Hack-a-Day in new win
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w']) # Close tab
    ]
}