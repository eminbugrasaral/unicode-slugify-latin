import re
import six
import unicodedata


def smart_text(s, encoding='utf-8', errors='strict'):
    if isinstance(s, six.text_type):
        return s

    if not isinstance(s, six.string_types):
        if six.PY3:
            if isinstance(s, bytes):
                s = six.text_type(s, encoding, errors)
            else:
                s = six.text_type(s)
        elif hasattr(s, '__unicode__'):
            s = six.text_type(s)
        else:
            s = six.text_type(bytes(s), encoding, errors)
    else:
        s = six.text_type(s)

    return s


# Extra characters outside of alphanumerics that we'll allow.
SLUG_OK = '-_~'

SLUG_REPLACE = ':;/'

TURKISH_LETTERS = {
    u'\N{LATIN SMALL LETTER DOTLESS I}': 'i',
    u'\N{LATIN SMALL LETTER S WITH CEDILLA}': 's',
    u'\N{LATIN SMALL LETTER C WITH CEDILLA}': 'c',
    u'\N{LATIN SMALL LETTER G WITH BREVE}': 'g',
    u'\N{LATIN SMALL LETTER O WITH DIAERESIS}': 'o',
    u'\N{LATIN SMALL LETTER U WITH DIAERESIS}': 'u',
    u'\xe2': 'a',
    u'\xee': 'i'
}

CAPITAL_TURKISH_LETTERS = {
    u'\N{LATIN CAPITAL LETTER I WITH DOT ABOVE}': 'I',
    u'\N{LATIN CAPITAL LETTER S WITH CEDILLA}': 'S',
    u'\N{LATIN CAPITAL LETTER C WITH CEDILLA}': 'C',
    u'\N{LATIN CAPITAL LETTER G WITH BREVE}': 'G',
    u'\N{LATIN CAPITAL LETTER O WITH DIAERESIS}': 'O',
    u'\N{LATIN CAPITAL LETTER U WITH DIAERESIS}': 'U',
    u'\xc2': 'A',
    u'\xce': 'I'
}

def slugify(s, ok=SLUG_OK, lower=True, spaces=False, replace_turkish=False, unicode_pairs=None):
    # L and N signify letter/number.
    # http://www.unicode.org/reports/tr44/tr44-4.html#GC_Values_Table

    rv = []
    for c in unicodedata.normalize('NFKC', smart_text(s)):
        cat = unicodedata.category(c)[0]
        if cat in 'LN' or c in ok:
            rv.append(c)
        elif c in SLUG_REPLACE:
            rv.append('')
        if cat == 'Z':  # space
            rv.append(' ')
    new = ''.join(rv).strip()
    if not spaces:
        new = re.sub('[-\s]+', '-', new)

    new = new.lower() if lower else new

    # Turkish hack
    if replace_turkish:

        for char, new_char in TURKISH_LETTERS.items():
            new = new.replace(char, new_char)

        if not lower:
            for char, new_char in CAPITAL_TURKISH_LETTERS.items():
                new = new.replace(char, new_char)

    # Replace with pair dictionary
    if isinstance(unicode_pairs, dict):
        for char, new_char in unicode_pairs.items():
            new = new.replace(char, new_char)

    return new
