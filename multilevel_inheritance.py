
"""
This program is based on the leave management of the company.
When an employee applies for leave, it goes to the manager and after that hr processes with holiday.
This is an example of multilevel Inheritance.
"""


# Define jr class
class JuniorEmployee(object):
    def __init__(self, leave_status):
        self.leave_status = leave_status

    def leave_application_status(self):
        return f"Junior employee leave application status: {self.leave_status}"


# Definition of master class
class ManagerEmployee(JuniorEmployee):
    def __init__(self, leave_status, approval_status):
        # Calling JuniorEmployee class constructor
        JuniorEmployee.__init__(self, leave_status)
        self.approval_status = approval_status

    def leave_approval_status(self):
        return f"Manager approval status on junior employee leave: {self.approval_status}"


# Definition of hr class.
class HrEmployee(ManagerEmployee):
    def __init__(self, leave_status, approval_status, leave_processing_status):
        # Calling ManagerEmployee constructor
        ManagerEmployee.__init__(self, leave_status, approval_status)
        self.leave_processing_status = leave_processing_status

    def leave_deduction_status(self):
        return f"Hr processing status on junio employee leave: {self.leave_processing_status}"


hr_emp_obj = HrEmployee("Applied", "Approved", "Processed")
print(f"{hr_emp_obj.leave_application_status()}\n"
      f"{hr_emp_obj.leave_approval_status()}\n"
      f"{hr_emp_obj.leave_deduction_status()}")
