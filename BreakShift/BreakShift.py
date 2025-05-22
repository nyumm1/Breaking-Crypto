from collections import Counter

# Top 3 most frequent letters by language
LANGUAGE_TOP_LETTERS = {
    "en": ["E", "T", "A"],
    "fr": ["E", "A", "S"],
    "de": ["E", "N", "I"],
    "es": ["E", "A", "O"],
    "hr": ["A", "I", "O"],
    "it": ["E", "A", "I"],
    "pt": ["A", "E", "O"],
    "nl": ["E", "N", "A"],
    "pl": ["A", "I", "E"],
    "sv": ["E", "A", "N"],
    "fi": ["A", "I", "T"],
    "no": ["E", "T", "A"],
    "da": ["E", "R", "N"],
    "tr": ["A", "E", "I"],
    "cs": ["E", "A", "N"],
    "ro": ["E", "A", "I"],
    "sk": ["A", "E", "O"],
    "sl": ["E", "A", "I"],
    "hu": ["E", "A", "T"],
    "ru": ["О", "Е", "А"],
    "uk": ["О", "А", "І"],
    "el": ["Α", "Ε", "Ο"],
}

def decrypt_shift(ciphertext: str, shift: int) -> str:
    """
    Decrypts a Caesar ciphered text using the given shift.
    """
    result = []
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base - shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

def shift_frequency_attack(ciphertext: str, language_code: str) -> None:
    """
    Attempts to break a Caesar cipher using frequency analysis based on the given language.
    """
    language_code = language_code.lower()
    top_letters = LANGUAGE_TOP_LETTERS.get(language_code)

    if not top_letters:
        print(f"[Error] Unknown language code: '{language_code}'")
        return

    freq = Counter(c.upper() for c in ciphertext if c.isalpha())

    if not freq:
        print("[Error] No alphabetic characters found in ciphertext.")
        return

    cipher_most_common = [char for char, _ in freq.most_common(3)]

    print(f"\n[Analysis] Top letters in ciphertext: {cipher_most_common}")
    print(f"[Target] Mapping to top letters in {language_code.upper()}: {top_letters}")

    candidates = []

    for cipher_letter in cipher_most_common:
        for lang_letter in top_letters:
            if cipher_letter.isalpha() and lang_letter.isalpha():
                shift = (ord(cipher_letter) - ord(lang_letter.upper())) % 26
                decrypted = decrypt_shift(ciphertext, shift)
                candidates.append((shift, decrypted))

    print("\n[Decryption Candidates]\n" + "-" * 30)
    for shift, decrypted_text in candidates:
        print(f"[Shift {shift:2}] {decrypted_text}")

def main():
    lang = input("Enter the suspected language code (e.g., 'en', 'fr'): ").strip()
    text = input("Enter the ciphertext: ").strip()
    shift_frequency_attack(text, lang)

if __name__ == "__main__":
    main()
