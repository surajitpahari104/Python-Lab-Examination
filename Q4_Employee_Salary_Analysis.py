# Question 4: Employee Salary Analysis

def salary_analysis(salaries):
    average = sum(salaries) / len(salaries)
    print("Average salary: Rs.", round(average, 2))
    print("Salaries above average:",
          [salary for salary in salaries if salary > average])
    print("Salaries after 10% increase:",
          [round(salary * 1.10, 2) for salary in salaries])

salary_analysis([25000, 30000, 40000, 50000, 35000])
