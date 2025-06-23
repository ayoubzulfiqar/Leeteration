class Solution:
    def employeeBonus(self, employee: list[dict], bonus: list[dict]) -> list[dict]:
        employee_map = {emp['empId']: emp for emp in employee}
        bonus_map = {b['empId']: b['bonus'] for b in bonus}

        result = []
        for emp_id, emp_data in employee_map.items():
            employee_name = emp_data['name']
            employee_bonus = bonus_map.get(emp_id)

            if employee_bonus is None or employee_bonus < 1000:
                result.append({"name": employee_name, "bonus": employee_bonus})
        
        return result