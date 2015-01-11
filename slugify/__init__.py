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
    u'\u0131': 'i',
    u'\u015f': 's',
    u'\xe7': 'c',
    u'\u011f': 'g',
    u'\xf6': 'o',
    u'\xfc': 'u',
    u'\xe2': 'a',
    u'\xee': 'i'
}

CAPITAL_TURKISH_LETTERS = {
    u'\u0130': 'I',
    u'\u015e': 'S',
    u'\xc7': 'C',
    u'\u011e': 'G',
    u'\xd6': 'O',
    u'\xdc': 'U',
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

        for char, new_char in TURKISH_LETTERS.iteritems():
            new = new.replace(char, new_char)

        if not lower:
            for char, new_char in CAPITAL_TURKISH_LETTERS.iteritems():
                new = new.replace(char, new_char)

    # Replace with pair dictionary
    if isinstance(unicode_pairs, dict):
        for char, new_char in unicode_pairs.iteritems():
            new = new.replace(char, new_char)

    return new
