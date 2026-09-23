"""A small educational implementation of the Vigenere cipher."""


def _validate_key(key: str) -> str:
    cleaned_key = key.strip()
    if not cleaned_key:
        raise ValueError("Key cannot be empty")
    if not cleaned_key.isascii() or not cleaned_key.isalpha():
        raise ValueError("Key must contain only English letters")
    return cleaned_key.lower()


def encrypt(text: str, key: str) -> str:
    """Encrypt text while preserving letter case and non-letter characters."""
    return _transform(text, key, decrypt=False)


def decrypt(text: str, key: str) -> str:
    """Decrypt text that was encrypted with the same key."""
    return _transform(text, key, decrypt=True)


def _transform(text: str, key: str, decrypt: bool) -> str:
    valid_key = _validate_key(key)
    result = []
    key_index = 0

    for character in text:
        if character.isascii() and character.isalpha():
            base = ord("A") if character.isupper() else ord("a")
            letter_number = ord(character) - base
            shift = ord(valid_key[key_index % len(valid_key)]) - ord("a")

            if decrypt:
                shift = -shift

            result.append(chr((letter_number + shift) % 26 + base))
            key_index += 1
        else:
            result.append(character)

    return "".join(result)

