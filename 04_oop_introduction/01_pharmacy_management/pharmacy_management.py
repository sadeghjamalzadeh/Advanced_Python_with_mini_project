class Drug:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price


class Pharmacy:

    def __init__(self, name):
        self.name = name
        self.drugs = []
        self.employees = []

    def add_drug(self, drug):
        self.drug = drug
        self.drugs.append(self.drug)

    def add_employee(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.employees.append({
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age})

    def total_value(self):
        total_value = 0
        for drug in self.drugs:
            total_value += int(drug.price) * int(drug.amount)
        return total_value

    def employees_summary(self):
        summary = "Employees:\n"
        for i, employee in enumerate(self.employees):
            summary += f"The employee number {i + 1} is {employee['first_name']} {employee['last_name']} who is {employee['age']} years old.\n"
        return summary
