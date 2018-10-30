import requests
from typing import Tuple, Optional, List

from breathe.exceptions import ObjectDoesNotExist


class Employee():
    def __init__(self, client):
        self.client = client

    def all(self) -> List[dict]:
        """
        Gets all employees
        :return: a list of dictionaries
        """
        endpoint = "employees"
        response = self.client.request("GET", endpoint)
        if requests.codes.ok:
            return response.json()[endpoint]
        else:
            return {}

    def get(self, id=None, email=None) -> dict:
        """
        Gets an employee by their id or email
        :param id: the Breathe ID of the employee to lookup
        :param email: the work email of the employee to lookup
        :return: dict containing the employee
        :raises: ObjectDoesNotExist
        """
        if not id and not email:
            raise TypeError("One of employee id or email must be specified")

        if id:
            endpoint = f"employees/{id}"
            response = self.client.request("GET", endpoint)
            if "employees" in response.json():
                return response.json()["employees"][0]
            else:
                raise ObjectDoesNotExist("Employee does not exist")

        else:
            employees = self.all()
            for employee in employees:
                if employee["email"] == email:
                    return employee
            raise ObjectDoesNotExist("Employee does not exist")

    def create(self, employee: dict) -> Tuple[bool, dict]:
        """
        Creates a new employee
        :param employee: A dict representing the employee to add. Required keys:
        first_name, last_name, email and join_date
        :return: A tuple containing a boolean whether the employee was created and a dict containing the reply
        """
        endpoint = "employees"
        required_employee_fields = ['first_name', 'last_name', 'email', 'join_date',]

        for key in required_employee_fields:
            if key not in employee:
                raise TypeError("Missing required employee field: " + key)

        data = {"employee": employee}
        # response = self.client.post(endpoint, data=data)
        response = self.client.request("POST", endpoint, json=data)

        if response and requests.codes.ok:
            return True, response.text
        else:
            return False, response.text

    def count(self) -> int:
        """
        Counts how many employees there are
        :return: int
        """
        return len(self.all())
