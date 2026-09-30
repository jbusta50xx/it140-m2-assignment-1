 """Read a user's name and age and estimate their birth year.


Input:
       A name entered by the user as a string.
       An age entered by the user as an integer.
  
Process:
       Subtract the user's age from the current year.

Output:
       A personalized message with the name and approximate birth year.

Typical usage example:
       Enter your name: Alex
       Enter your age: 20
       Alex, you were born around 2006.
      (Example assumes the current year is 2026.)
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
       name = input("Enter your name: ")
       age = int(input("Enter your age: "))

    # Calculate user's approximate birth year.
       birth_year = CURRENT_YEAR - age

    # Output personalized message with user's name and birth year.
       print(f"{name}, you were born around {birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
# TODO: Replace with an APA-style reference for a source you used, or delete.
# TODO: Replace with another APA-style reference, or delete this TODO line.
