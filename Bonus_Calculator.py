#Calculate the bonus for an employee based on their performance and salary
def calculate_bonus(salary, performance_rating):
    if performance_rating == 'A':
        bonus_percentage = 0.10
    elif performance_rating == 'B':
        bonus_percentage = 0.05
    elif performance_rating == 'C':
        bonus_percentage = 0.02
    else:
        bonus_percentage = 0.00
    bonus = salary * bonus_percentage
    return bonus
print("Welcome to the Employee Bonus Calculator!")
Name = input("\nEnter the Employee's Name: ")
Salary = float(input(f"Enter {Name}'s salary: "))
Performance_Rating = input(f"Enter {Name}'s performance rating (A, B, C, or D): ").upper()
bonus = calculate_bonus(Salary, Performance_Rating)
print(f"{Name}'s bonus is: ₹{bonus:.2f}")
print(f"{Name}'s total compensation is: ₹{Salary + bonus:.2f}")
