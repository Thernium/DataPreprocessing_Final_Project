import numpy as np
import requests

rng = np.random.default_rng(seed=26)

# ------------------------------------------ Identity -------------------------------------
# Employees IDs
numeric_part = rng.choice(np.arange(100000, 999999), size=500, replace=False)
employee_ids = np.array([f"EMP{n}" for n in numeric_part])

#using random-user generator API for "name"
# Get 500 random users in one call
response = requests.get("https://randomuser.me/api/", params={"results": 500})
data = response.json()["results"]
# Employees Names
employee_first_names = np.array([person["name"]["first"] for person in data])
employee_last_names = np.array([person["name"]["last"] for person in data])

#Employees Gender
employee_gender = np.random.choice(["Male", "Female"], size=500)

#Employees Date-Of-Birth
employee_dateOfBirth = np.array([f"{np.random.randint(1966, 2007)}-{np.random.randint(1, 12)}-{np.random.randint(1, 31)}" for i in range(500)])


# ------------------------------------------ Contact -------------------------------------
#Employees Email
employee_emails = np.array([])
for emp in range(500):
    first_name = employee_first_names[emp].lower()
    last_name = employee_last_names[emp].lower()
    email = f"{first_name}.{last_name}{np.random.randint(100, 999)}@email.com"
    employee_emails = np.append(employee_emails, email)

#Employees PhoneNumber               Example: +123 901 2345678
employee_phoneNumbers = np.array([f"+{np.random.randint(1, 203)} 0{np.random.randint(900, 999)}{np.random.randint(1000000, 9999999)}" for i in range(500)])


# ------------------------------------------ Employment -------------------------------------
#Employment: job_title, department, manager_id, hire_date, employment_status(active/terminated/on leave), 
# employment_type (full-time/part-time/contract)
departments_titles = {
    "Engineering": ["Software Engineer", "Senior Software Engineer", "DevOps Engineer", "QA Engineer", "Engineering Manager"],
    "Sales": ["Sales Representative", "Account Executive", "Sales Manager", "Business Development Rep"],
    "Marketing": ["Marketing Specialist", "Content Strategist", "SEO Analyst", "Marketing Manager"],
    "HR": ["HR Generalist", "Recruiter", "HR Manager", "Talent Acquisition Specialist"],
    "Finance": ["Financial Analyst", "Accountant", "Finance Manager", "Controller"],
}

#Employee Department
employee_department = np.random.choice(departments_titles.keys)
print(f"{len(employee_department)} | {type(employee_department)}")

# employee_jobTitle = 

