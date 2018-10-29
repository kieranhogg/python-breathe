# from ..client import ERROR_TYPES, HTTP_OK

class Employees():

    def __init__(self, client):
        self.client = client

    def all(self):
        endpoint = "employees"
        response = self.client.get(endpoint)
        return response[endpoint]

    def get(self, id):
        endpoint = f"employees/{id}"
        response = self.client.get(endpoint)
        if "employees" not in response and "error" in response:
            return response["error"]
        elif "employees" not in response:
            return "Invalid response"
        else:
            return response["employees"][0]

    def create(self, employee: dict):
        required_employee_fields = ['first_name', 'last_name', 'email', 'join_date',]

        for key in required_employee_fields:
            if key not in employee:
                raise TypeError("Missing required employee field: " + key)

        endpoint = "employees"
        data = {"employee": employee}
        print(data)
        response = self.client.post(endpoint, data=data)
        if response and response.status_code == 200:
            return response
        else:
            print(response)
            # print(ERROR_TYPES[response.status_code])

    def count(self):
        return len(self.all())
