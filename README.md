[![Build Status](https://travis-ci.org/eminbugrasaral/unicode-slugify-turkish.svg?branch=master)](https://travis-ci.org/eminbugrasaral/unicode-slugify-turkish)

# Unicode Slugify (with Turkish Hack)

Unicode Slugify is a slugifier that generates unicode slugs.  It was originally
used in the Firefox Add-ons web site to generate slugs for add-ons and add-on
collections.  Many of these add-ons and collections had unicode characters and
required more than simple transliteration.

## Install

    pip install unicode-slugify-turkish

## Usage

    >>> import slugify

    >>> slugify.slugify(u'Bän...g (bang)')
    u'bäng-bang'

## Turkish Hack

- Replaces special Turkish chars with similar ascii codes.
- Problem: I want Turkish users with English keyboards to be able to search through my Turkish strings.
- Solution: Slugify that Turkish string by enabling Turkish replacement, and match this string with the slugified search word.
- Example: Strore "Sabancı Üniversitesi" as "sabanci-universitesi" and then users will be able to search with any combination like "Sabanci", "Sabancı" and "SABANCI".
- Note: Do not forget to slugify both strings with replace_turkish=True

## Example

    >>> from slugify import slugify

    >>> string_without_turkish = slugify(u'ıspanaklı boğaz turşusu', replace_turkish=True)
    u'ispanakli-bogaz-tursusu'

    >>> slugify(u'Ispanakli Bogaz Tursusu') == string_without_turkish
    True

    >>> u'Bogazici'.lower() in slugify(u'boğaziçi', replace_turkish=True)
    True
    
    >>> slugify(u'çiçek', replace_turkish=True) in slugify(u'ÇİÇEK', replace_turkish=True)
    True
    
    >>> u'cicek' in slugify(u'ÇİÇEK', replace_turkish=True)
    True

## List of common Turkish latin letters to be replaced

- ı -> i
- İ -> I
- ş -> s
- Ş -> S
- ç -> c
- Ç -> C
- ğ -> g
- Ğ -> G
- ö -> o
- Ö -> O
- ü -> u
- Ü -> U

## Extra Parameters

- replace_turkish: Replace common Turkish latin letters to be replaced with similar ascii representation.
- unicode_pair: You can give a dictionary of unicode characters with their replacement values. Like: {u'\xe9', 'e'} - é will be replaced with e


## TODO

- Tests for Turkish hack is missing.
- Add tests for unicode_pair

## Sponsors

- This library is being used in The Volt Ride Sharing App (http://thevoltapp.com)
- Hippo Foundry (http://hipolabs.com)

## Contact

- Website: http://www.eminbugrasaral.com
