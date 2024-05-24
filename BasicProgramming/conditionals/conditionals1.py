from datetime import date


def check_validity_to_vote(birth_year, voting_age=18):
    """
    Checks if a person is old enough to vote based on their birth year.

    Args:
        birth_year (int): The birth year of the person.
        voting_age (int, optional): The minimum voting age. Default is 18.

    Returns:
        str: A message indicating whether the person is allowed to vote or not.
    """
    try:
        today = date.today()
        age = today.year - int(birth_year)

        if age >= voting_age:
            return "Congrats. You are allowed to vote"
        else:
            return "Sorry. You are too young to vote"
    except ValueError:
        return "Invalid input. Please enter a valid birth year as a number."
