# Unicode Slugify (with Turkish Hack)

Unicode Slugify is a slugifier that generates unicode slugs.  It was originally
used in the Firefox Add-ons web site to generate slugs for add-ons and add-on
collections.  Many of these add-ons and collections had unicode characters and
required more than simple transliteration.

## Usage

    >>> import slugify

    >>> slugify.slugify(u'Bän...g (bang)')
    u'bäng-bang'


## Turkish Hack

- Replaces special Turkish chars with similar ascii codes.
- Problem: I want Turkish users with English keyboards to be able to search through my Turkish strings.
- Solution: Slugify that Turkish string by enabling Turkish replacement, and match this string with the slugified search word.
- Example: Strore "Sabancı Üniversitesi" as "sabanci-universitesi" and then users will be able to search with any combination.
- Note: Do not forget to slugify both string with replace_turkish=True

## Example

    >>> import slugify

    >>> string_without_turkish = slugify.slugify(u'ıspanaklı boğaz turşusu', replace_turkish=True)
    u'ispanakli-bogaz-tursusu'

    >>> slugify.slugify(u'Ispanakli Bogaz Tursusu') == string_without_turkish
    True

    >>> u'Bogazici'.lower() in slugify.slugify(u'boğaziçi', replace_turkish=true)
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
