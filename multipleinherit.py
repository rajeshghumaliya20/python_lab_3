class ContactInfo:
    def __init__(self, email, phone):
        self.email = email
        self.phone = phone
    def display_contact_info(self):
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
class JobDetails:
    def __init__(self, designation, salary):
        self.designation = designation
        self.salary = salary
    def display_job_details(self):
        print(f"Designation: {self.designation}")
        print(f"Salary: {self.salary:}")
class Employee(ContactInfo, JobDetails):
    def __init__(self, name, email, phone, designation, salary):
        ContactInfo.__init__(self, email, phone)
        JobDetails.__init__(self, designation, salary)
        self.name = name
    def display_employee_info(self):
        print(f"Employee Name: {self.name}")
        self.display_contact_info()
        self.display_job_details()
employee1 = Employee("RAJESH", "xyz@gmail.com", "1234567890", "Software Engineer", 75000)
employee1.display_employee_info()
