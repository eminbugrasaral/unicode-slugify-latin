[![Build Status](https://travis-ci.org/eminbugrasaral/unicode-slugify-latin.svg?branch=master)](https://travis-ci.org/eminbugrasaral/unicode-slugify-latin)

**Note**

Please use unicode-slugify instead of this library. This was created before I merged the ascii representation feature into the source repo.

**Links**

PyPi: https://pypi.python.org/pypi/unicode-slugify-latin

Github: https://github.com/eminbugrasaral/unicode-slugify-latin

# Unicode Slugify (with Latin Hack)

Unicode Slugify is a slugifier that generates unicode slugs.  It was originally
used in the Firefox Add-ons web site to generate slugs for add-ons and add-on
collections.  Many of these add-ons and collections had unicode characters and
required more than simple transliteration.

## Install

    pip install unicode-slugify-latin

## Usage

    >>> import slugify

    >>> slugify.slugify(u'Bän...g (bang)')
    u'bäng-bang'

## Latin Hack

- Replaces special Latin chars with similar ascii representations.
- Problem: I want users who speak Latin languages with English keyboards to be able to search through my Latin strings.
- Solution: Slugify that Latin string by enabling Latin replacement, and match this string with the slugified search word.
- Example: Strore "Sabancı Üniversitesi" as "sabanci-universitesi" and then users will be able to search with any combination like "Sabanci", "Sabancı" and "SABANCI".
- Note: Do not forget to slugify both strings with replace_latin=True

## Example

    >>> from slugify import slugify

    >>> string_without_latin_letters = slugify(u'ıspanaklı boğaz turşusu', replace_latin=True)
    u'ispanakli-bogaz-tursusu'

    >>> slugify(u'Ispanakli Bogaz Tursusu') == string_without_latin_letters
    True

    >>> u'Bogazici'.lower() in slugify(u'boğaziçi', replace_latin=True)
    True
    
    >>> slugify(u'çiçek', replace_turkish=True) in slugify(u'ÇİÇEK', replace_latin=True)
    True
    
    >>> u'cicek' in slugify(u'ÇİÇEK', replace_latin=True)
    True

## List of common latin letters to be replaced

- ı, ì, í, î, ï -> i
- İ, Ì, Í, Î, Ï -> I
- ö, ó, ò, ô, õ, ø -> o
- Ö, Ò, Ó, Ô, Õ, Ø -> O
- ü, ù, ú, û -> u
- Ü, Ù, Ú, Û -> U
- à, á, â, ã, ä, å -> a
- À, Á, Â, Ã, Ä, Å -> A
- æ -> ae
- Æ -> AE
- è, é, ê, ë -> e
- È, É, Ê, Ë -> E
- ñ -> n
- Ñ -> N
- ý, ÿ -> y
- Ý, Ÿ -> Y
- ş -> s
- Ş -> S
- ç -> c
- Ç -> C
- ğ -> g
- Ğ -> G

## New parameters after this fork

- replace_latin: Replace common Latin letters to be replaced with similar ascii representation.
- unicode_pairs: You can give a dictionary of unicode characters with their replacement values. Like: {u'\xe9', 'e'} - é will be replaced with e

## Sponsors

- This library is being used in The Volt Ride Sharing App (http://thevoltapp.com)
- Hippo Foundry (http://hipolabs.com)

## Contact

- Website: http://www.eminbugrasaral.com
