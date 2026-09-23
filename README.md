# Vigenere Cipher CLI

A beginner-friendly Python command-line program that encrypts and decrypts text with the Vigenere cipher. Unlike the Caesar cipher, it uses a repeating keyword, so different letters can be shifted by different amounts.

> **Educational use only:** the Vigenere cipher is historically interesting, but it is not secure enough for passwords, private messages, or real-world data protection.

## Features

- encrypt and decrypt from the terminal;
- preserve uppercase and lowercase letters;
- leave spaces, punctuation, and numbers unchanged;
- validate the keyword;
- use only the Python standard library;
- include automated tests.

## Requirements

- Python 3.9 or newer

## Usage

```bash
python3 main.py encrypt "Attack at Dawn!" LEMON
python3 main.py decrypt "Lxfopv ef Rnhr!" LEMON
```

## Run tests

```bash
python3 -m unittest -v
```

## How it works

Each key letter represents a shift from 0 to 25. The key repeats until every English letter in the message has a matching shift. Non-letter characters do not consume a key position. Decryption applies the same shifts in reverse.

## Project structure

```text
main.py           command-line interface
vigenere.py       cipher logic and key validation
test_vigenere.py  unit tests
```

## Ideas for further practice

- add an interactive menu;
- read input from a text file;
- support a custom alphabet;
- display a step-by-step explanation of each shifted letter.

## License

This project is available under the MIT License.
