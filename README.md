# Password Generator

This is a secure, customizable command-line password generator written in Python. It lets you generate one or multiple strong, random passwords with configurable options for length, character sets, and exclusion of ambiguous characters.

## Features

- Select password length (4–128 characters)
- Choose number of passwords to generate (1–20)
- Includes lowercase, uppercase, digits, and punctuation by default
- Excludes ambiguous characters (`I`, `l`, `1`, `O`, `0`) for clarity
- Ensures each required character type is included at least once
- Displays estimated entropy for each password (measure of strength)
- Fully random using Python’s `secrets` module (suitable for cryptographic use)

## Requirements

- Python 3.6 or higher

## Usage

Run the script from your command line:

```bash
python passwordgenerator.py
```

You will be prompted for:
- Password length
- Number of passwords to generate

The program then generates passwords and prints them along with their estimated entropy.

## Example

```
Password generator
How many characters? (4-128) [16]: 
Number of passwords to generate? (1-20) [1]: 
Pool size: 66 characters — Estimated entropy per password: 94.4 bits

1: ngRDPkzYsjT36,]g
```

## Customization

Edit the script to further configure:
- Which types of characters to include (see the variables near the `if __name__ == "__main__"` line)
- Whether to exclude ambiguous characters

## Security

The generator uses Python's `secrets` module to ensure cryptographically secure random password generation.
