# // Time Complexity : O(n)
# // Space Complexity : O(h)
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        employee_map = {}
        for employee in employees:
            employee_map[employee.id] = employee
        
        def calculate_importance(employee_id):
            employee = employee_map[employee_id]
            total_importance = employee.importance
            
            for subordinate_id in employee.subordinates:
                total_importance += calculate_importance(subordinate_id)
            
            return total_importance
        
        return calculate_importance(id)
        

