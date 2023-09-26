"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:

    """
    An object representing an employee.
    The object takes the employee's name, salary, and contract rate.
    If contract rate is 0, we assume the employee doesn't receive commission.
    If number of hours worked is given, then the employee is assumed to have an hourly salary.
    If the number of contracts worked is given, the employee is assumed to receive contract-based
    commission.
    """
    def __init__(self, name: str, salary: int, rate: int, hours: int = -1, contracts: int = 0) -> None:
        self.name = name
        self.salary = salary
        self.hours = hours
        self.contracts = contracts
        self.rate = rate

    def get_pay(self):
        total_pay = self.salary if self.hours < 0 else self.salary * self.hours
        if self.contracts > 0:
            total_pay += self.contracts * self.rate
            return total_pay

        total_pay += self.rate
        return total_pay

    def __str__(self):
        total_pay = self.get_pay()
        pay_str: str = f"{self.name} works on a"

        if self.hours >= 0:
            pay_str += f" contract of {self.hours} hours at {self.salary}/hour"
        else:
            pay_str += f" monthly salary of {self.salary}"

        if self.contracts > 0:
            pay_str += f" and receives a commission for {self.contracts} contract(s) at {self.rate}/contract. "
        elif self.rate > 0:
            pay_str += f" and receives a bonus commission of {self.rate}. "
        else:
            pay_str += f"."

        pay_str += f" Their total pay is {total_pay}."

        return pay_str


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee(name='Billie', salary=4000, rate=0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee(name='Charlie', salary=25, rate=0, hours=100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee(name='Renee', salary=3000, rate=200, contracts=4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee(name='Jan', salary=25, rate=220, hours=150, contracts=3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee(name='Robbie', salary=2000, rate=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee(name='Ariel', salary=30, rate=600, hours=120)
