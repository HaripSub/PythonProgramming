from collections import Counter


class Person:
    def __init__(self, occupation):
        self.occupation = occupation

    def __hash__(self):
        return hash(self.occupation)

    def __eq__(self, other):
        return self.occupation == other.occupation

    def __repr__(self):
        return f"Person({self.occupation})"


doctor = Person("Doctor")
engineer = Person("Engineer")
scientist = Person("scientist")
teacher = Person("teacher")
accountant = Person("Accountant")


occupation = [doctor, engineer, doctor, teacher, accountant, scientist, teacher, engineer]
counter = Counter(occupation)
print(counter)

doctor_count = counter[doctor]
engineer_count = counter[engineer]
teacher_count = counter[accountant]

print(f"Count for {doctor}: {doctor_count}")
print(f"Count for {engineer}: {engineer_count}")
print(f"Count for {teacher}: {teacher_count}")
