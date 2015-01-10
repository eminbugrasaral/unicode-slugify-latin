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
    'keys': [unicode('\u0131'),
             unicode('\u015f', errors='replace'),
             unicode('\xe7', errors='replace'),
             unicode('\u011f', errors='replace'),
             unicode('\xf6', errors='replace'),
             unicode('\xfc', errors='replace')],
    'values': ['i', 's', 'c', 'g', 'o', 'u']
}

ALL_TURKISH_LETTERS = {
    'keys': [unicode('\u0131', errors='replace'),
             unicode('\u0130', errors='replace'),
             unicode('\u015f', errors='replace'),
             unicode('\u015e', errors='replace'),
             unicode('\xe7', errors='replace'),
             unicode('\xc7', errors='replace'),
             unicode('\u011f', errors='replace'),
             unicode('\u011e', errors='replace'),
             unicode('\xf6', errors='replace'),
             unicode('\xd6', errors='replace'),
             unicode('\xfc', errors='replace'),
             unicode('\xdc', errors='replace')],
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
                result = result.replace(unicode(letter, errors='replace'), new_letter)
        else:
            for letter in ALL_TURKISH_LETTERS:
                new_letter = ALL_TURKISH_LETTERS['values'][ALL_TURKISH_LETTERS['keys'].index(letter)]
                result = result.replace(unicode(letter, errors='replace'), new_letter)

    return result
