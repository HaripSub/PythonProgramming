from datetime import date


def check_validity_to_vote(birth_year, voting_age=18):
    try:
        today = date.today()
        age = today.year - int(birth_year)

        if age >= voting_age:
            return "Congrats. You are allowed to vote"
        else:
            return "Sorry. You are too young to vote"
    except ValueError:
        return "Invalid input. Please enter a valid birth year as a number."
