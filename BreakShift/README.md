Another quick and easy decipher using "frequency analysis" for a simple Ceasar Shift 


# Caesar Cipher Frequency Attack

This Python script performs a basic **frequency analysis attack** on a Caesar cipher, using known letter frequency patterns from various languages.

##  What It Does

- **Analyzes a ciphertext** and finds the most frequent letters.
- **Compares** these frequencies to known top letters in a target language.
- **Attempts decryption** using estimated Caesar shift values.
- Outputs multiple **decryption candidates** based on frequency matches.

##  How It Works

The Caesar cipher is vulnerable to frequency analysis because each letter is shifted consistently throughout the message. This script:

1. **Accepts a language code** (e.g., `en` for English, `fr` for French).
2. Looks up the top 3 most common letters in that language.
3. Compares them to the 3 most common letters in the ciphertext.
4. Calculates potential shift values.
5. Attempts decryption using each shift.
6. Prints out all the resulting texts for human evaluation.

##  Requirements

This script requires only the Python standard library. No external dependencies.


