from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Plasma', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xFF0000, 'Audio', [Keycode.CONTROL, Keycode.ALT, '1']),
        (0xD4D900, 'Books', [Keycode.CONTROL, Keycode.ALT, '2']),
        (0x00D900, 'Comics', [Keycode.CONTROL, Keycode.ALT, '3']),
        # 2nd row ----------
        (0x101010, 'Comms', [Keycode.CONTROL, Keycode.ALT, '4']),
        (0x101010, 'Main', [Keycode.CONTROL, Keycode.ALT, '5']),
        (0x101010, 'Photo', [Keycode.CONTROL, Keycode.ALT, '6']),
        # 3rd row ----------
        (0x101010, 'Prog', [Keycode.CONTROL, Keycode.ALT, '7']),
        (0x101010, 'Vid Ed', [Keycode.CONTROL, Keycode.ALT, '8']),
        (0x101010, 'Games', [Keycode.CONTROL, Keycode.ALT, '9']),
        # 4th row ----------
        (0x000000, 'Vids', [Keycode.CONTROL, Keycode.ALT, '0']),
        (0x800000, 'Virt', [Keycode.CONTROL, Keycode.ALT, '!']), 
        (0x101010, 'Web', [Keycode.CONTROL, Keycode.ALT, '@']), 
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w']) # Close tab
    ]
}
