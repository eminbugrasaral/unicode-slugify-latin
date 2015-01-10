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
    'keys': [u'\u0131', u'\u015f', u'\xe7', u'\u011f', u'\xf6', u'\xfc'],
    'values': ['i', 's', 'c', 'g', 'o', 'u']
}

ALL_TURKISH_LETTERS = {
    'keys': [u'\u0131', u'\u0130', u'\u015f', u'\u015e', u'\xe7', u'\xc7', u'\u011f', u'\u011e', u'\xf6', u'\xd6', u'\xfc', u'\xdc'],
    'values': ['i', 'I', 's', 'S', 'c', 'C', 'g', 'G', 'o', 'O' 'u', 'U']
}

def slugify(s, ok=SLUG_OK, lower=True, spaces=False, replace_turkish=False):
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
    result = new.lower() if lower else new

    # Turkish hack
    if replace_turkish:
        if lower:
            for letter in TURKISH_LETTERS['keys']:
                new_letter = TURKISH_LETTERS['values'][TURKISH_LETTERS['keys'].index(letter)]
                result = result.replace(letter, new_letter)
        else:
            for letter in ALL_TURKISH_LETTERS:
                new_letter = ALL_TURKISH_LETTERS['values'][ALL_TURKISH_LETTERS['keys'].index(letter)]
                result = result.replace(letter, new_letter)

    return result
