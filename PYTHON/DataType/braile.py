# Braille Dictionary
braille_dict = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
    'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
    'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽',
    'z': '⠵', ' ': ' ',  # Space
    '1': '⠂', '2': '⠆', '3': '⠒', '4': '⠲', '5': '⠢',
    '6': '⠖', '7': '⠶', '8': '⠦', '9': '⠔', '0': '⠴',
    '.': '⠄', ',': '⠂', ';': '⠆', ':': '⠒', '?': '⠦',
    '!': '⠖', '-': '⠤', '_': ' underscore ', '+': ' plus ',
    '=': ' equals ', '(': ' open parenthesis ', ')': ' close parenthesis ',
    '[': ' open bracket ', ']': ' close bracket ',
    '{': ' open brace ', '}': ' close brace ',
    '<': ' less than ', '>': ' greater than ',
    '/': ' slash ', '\\': ' backslash ',
    '|': ' vertical bar ', '*': ' asterisk ',
    '#': ' number sign ', '$': ' dollar sign ',
    '%': ' percent sign ', '@': ' at sign ',
    '^': ' caret ', '&': ' ampersand ',
    '~': ' tilde '
}
def text_to_braille(text):
    """Converts text to Braille representation."""
    braille_text = ""
    for char in text.lower():
        if char in braille_dict:
            braille_text += braille_dict[char]
        else:
            braille_text += f" unsupported character: {char} "  # Handle unsupported characters
    return braille_text
# Get input from the user
text_input = input("Enter text to convert to Braille: ")
# Convert to Braille
braille_output = text_to_braille(text_input)
# Display the result
print("Braille representation:")
print(braille_output)
