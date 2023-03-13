from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Plasma', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xFF0000, 'REC', [Keycode.CONTROL, Keycode.ALT, '1']),
        (0xD4D900, 'PAUSE', [Keycode.CONTROL, Keycode.ALT, '2']),
        (0x00D900, 'STREAM', [Keycode.CONTROL, Keycode.ALT, '3']),
        # 2nd row ----------
        (0x101010, 'Pre-', [Keycode.CONTROL, Keycode.ALT, '4']),
        (0x101010, 'Appeal', [Keycode.CONTROL, Keycode.ALT, '5']),
        (0x101010, 'Title', [Keycode.CONTROL, Keycode.ALT, '6']),
        # 3rd row ----------
        (0x101010, 'Me ^', [Keycode.CONTROL, Keycode.ALT, '7']),
        (0x101010, 'Game ^', [Keycode.CONTROL, Keycode.ALT, '8']),
        (0x101010, 'Med', [Keycode.CONTROL, Keycode.ALT, '9']),
        # 4th row ----------
        (0x000000, 'BRB', [Keycode.CONTROL, Keycode.ALT, '0']),
        (0x800000, 'none', [Keycode.CONTROL, Keycode.ALT, '!']), 
        (0x101010, 'none', [Keycode.CONTROL, Keycode.ALT, '@']), 
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w']) # Close tab
    ]
}
