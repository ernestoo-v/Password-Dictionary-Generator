# Password Dictionary Generator

This Python script generates a comprehensive password dictionary based on known user information. The dictionary includes a wide range of password combinations such as variations of names, dates of birth, and common patterns, making it useful for password cracking or penetration testing tasks.

## Features

- Combines different variations of the user's name, surname, DNI, and birth date.
- Generates passwords with common suffixes and prefixes.
- Supports case variations for the name and surname (uppercase, lowercase, capitalized).
- Adds common special characters and numbers to combinations.
- Saves the generated dictionary in a text file.

## Usage

1. **Clone this repository:**

   ```bash
   git clone https://github.com/yourusername/password-dictionary-generator.git
   cd Password-Dictionary-Generator
   
2. Run the script:
   ```bash
   python passwordGenerator.py -n <FirstName> -s <Surname> -d <DNI> -b <BirthDate> -o <OutputFile>

3. Example
   ```bash
   python passwordGenerator.py -n Juan -s Querito -d 56345247O -b 26-06-1983 -o password_dict.txt
4. Help flag
   ```bash
   python passwordGenerator.py -h

## Combinations Explained

- -n : User's first name
- -s : User's surname
- -d : User's DNI (National ID)
- -b : User's birth date in DD-MM-YYYY format
- -o : Output file for the generated password dictionary (e.g., password_dict.txt)

The script creates the following types of combinations:

1. **Basic Combinations:**  
   - Direct combinations of name, surname, DNI, and birth year.
   - Examples: `Juan1983`, `Querito1983`, `56345247O`

2. **Date Variations:**  
   - Combinations that include the full date or individual parts (day, month, year).
   - Examples: `26061983`, `2606`, `1983`

3. **Case Variations:**  
   - Variations in uppercase, lowercase, and capitalized versions of the name and surname.
   - Examples: `juanq1983`, `JUANq1983`, `Juanq1983`

4. **Prefix and Suffix Variations:**  
   - Common suffixes (`123`, `!`, `q`, etc.) and prefixes (`@`, `#`, etc.) are added to the base combinations.
   - Examples: `Juanq1983!`, `Juanq1983@`

5. **Permutations and Special Characters:**  
   - Combinations of base information with special characters or numeric patterns.
   - Examples: `Juan1983!`, `Querito@Juan`, `Juan!!Querito1983`

## Requirements

- Python 3.x
- argparse library (comes pre-installed with Python)
