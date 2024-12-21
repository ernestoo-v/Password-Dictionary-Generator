import itertools
import argparse

# Function to generate password combinations based on known information
def generate_passwords(name, surname, dni, birth_date, output_file):
    # Extract parts of the birth date
    day, month, year = birth_date.split("-")

    # Base password components
    bases = [
        name, surname, dni, year,
        day + month + year,  # Full date without dashes
        day + month,  # Day and month
        name + year,  # Juan1983
        surname + year,  # Quierito1983
        name.lower() + surname[0].lower() + year,  # juanq1983
        name + surname[0].lower() + year,  # Juanq1983
        surname[:3].lower() + name.lower() + year,  # quiJuan1983
        name + surname[:3].lower() + year,  # Juanqui1983
        name.lower() + surname.lower() + year,  # juanquierito1983
        name.lower() + surname.lower() + year[-2:],  # juanquierito83
        dni[:8] + name[0].lower(),  # 56345247Juan
        name + surname[0].lower() + year + "!",  # Juanq1983!
        surname + "@" + name,  # Quierito@Juan
        surname + "!" + name,  # Quierito!Juan
        surname + name,  # QuieritoJuan
    ]

    # Variants with uppercase and lowercase letters
    variants_name = [name, name.lower(), name.upper(), name.capitalize()]
    variants_surname = [surname, surname.lower(), surname.upper(), surname.capitalize()]

    # Common suffixes and prefixes
    suffixes = ["123", "1", "!", "1234", "q", surname[0].lower(), surname[:3].lower(), "!!", "00", "2023"]
    prefixes = ["@", "#", "$", "!", "q", surname[:2], name[:2]]

    # Generate combinations
    combinations = set()

    # Base combinations with suffixes and prefixes
    for base in bases:
        combinations.add(base)
        for suffix in suffixes:
            combinations.add(base + suffix)
            combinations.add(suffix + base)

    # Prefixes and suffixes with different combinations
    for base in bases:
        for prefix in prefixes:
            combinations.add(prefix + base)
            combinations.add(base + prefix)

    # Variants with uppercase/lowercase letters
    for n in variants_name:
        for a in variants_surname:
            combinations.add(n + a)
            combinations.add(n + a[0].lower() + year)
            combinations.add(n + a + year)
            combinations.add(a + n + year)

    # Generate combinations with different formats
    for comb in itertools.permutations(bases, 2):
        combinations.add("".join(comb))  # Juan1983Quierito
        combinations.add("".join(reversed(comb)))  # QuieritoJuan1983

    # Combinations with special characters and numbers
    for comb in itertools.permutations(bases + suffixes, 3):
        combinations.add("".join(comb))
        combinations.add("".join(reversed(comb)))
        combinations.add("".join(comb) + "@")

    # Write the generated passwords to a file
    with open(output_file, "w") as file:
        for password in combinations:
            file.write(password + "\n")

    print(f"Generated {len(combinations)} passwords. Saved in {output_file}")


# Main function to parse command-line arguments
def main():
    parser = argparse.ArgumentParser(description="Generate a password dictionary based on known user information.")
    parser.add_argument("-n", "--name", required=True, help="User's first name")
    parser.add_argument("-s", "--surname", required=True, help="User's surname")
    parser.add_argument("-d", "--dni", required=True, help="User's DNI (National ID)")
    parser.add_argument("-b", "--birthdate", required=True, help="User's birth date in format DD-MM-YYYY")
    parser.add_argument("-o", "--output", required=True, help="Output file name for the generated password dictionary")

    args = parser.parse_args()

    generate_passwords(args.name, args.surname, args.dni, args.birthdate, args.output)


if __name__ == "__main__":
    main()
