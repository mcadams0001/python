def search4vowels(phrase: str) -> set:
    """Shows vowels found in text"""
    return search4letters(phrase)


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    return set(letters).intersection(set(phrase))
