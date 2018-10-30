# python-breathe
A Python wrapper for the Breathe HR API.

## Installation
`pip install python-breathe`

## Usage
```
>>> from breathe.client import Client
>>> c = Client(api_key="123456", mode="sandbox")
>>> c.employees.all()
[{'length_of_service_in_months': 0, 'age': None, 'full_or_part_time': None, 'notice_period': None, 'photo_url': '', 'working_pattern': {'id': 2842, 'name': 'standard working week', 'total_hours': '37.5', 'default': True}, 'holiday_allowance': {'name': 'standard holiday allowance', 'id': 2913}, 'line_manager': None, 'holiday_approver': None, 'department': None, 'division': None, 'location': None, 'gender': None, 'statutory_holiday_country': None, 'receives_statutory_holidays': False, 'salary': None, 'status': 'Current employee', 'job_start_date': None, 'job_title': None, 'hr': True, 'custom_fields': None, 'id': 1795, 'account_id': 798, 'first_name': 'Joe', 'middle_name': None, 'last_name': 'Bloggs', 'email': 'jbloggs@acme.com', 'join_date': None, 'dob': None, 'known_as': None, 'marital_status': None, 'nationality': None, 'ethnicity': None, 'national_insurance_no': None, 'driving_license': None, 'ddi': None, 'work_ext': None, 'work_mobile': None, 'personal_mobile': None, 'home_telephone': None, 'personal_email': None, 'address1': None, 'address2': None, 'address3': None, 'city': None, 'county': None, 'postcode': None, 'country': None, 'linked_in': None, 'facebook': None, 'skype': None, 'twitter': None, 'bank_name': None, 'bank_branch': None, 'sort_code': None, 'account_number': None, 'building_society': None, 'ref_number': None, 'leaving_date': None, 'employee_ref': None, 'contract_provider': None, 'probation_date': None, 'remuneration_currency': {'id': 2, 'currency_code': 'GBP', 'currency_symbol': '£', 'description': 'British Pound', 'created_at': None, 'updated_at': None, 'deleted_at': None}, 'created_at': '2018-03-22T11:12:02+00:00', 'updated_at': '2018-03-22T11:12:02+00:00'},]
>>> c.employees.get(1795)
{'length_of_service_in_months': 0, 'age': None, 'full_or_part_time': None, 'notice_period': None, 'photo_url': '', 'working_pattern': {'id': 2842, 'name': 'standard working week', 'total_hours': '37.5', 'default': True}, 'holiday_allowance': {'name': 'standard holiday allowance', 'id': 2913}, 'line_manager': None, 'holiday_approver': None, 'department': None, 'division': None, 'location': None, 'gender': None, 'statutory_holiday_country': None, 'receives_statutory_holidays': False, 'salary': None, 'status': 'Current employee', 'job_start_date': None, 'job_title': None, 'hr': True, 'custom_fields': None, 'id': 1795, 'account_id': 798, 'first_name': 'Joe', 'middle_name': None, 'last_name': 'Bloggs', 'email': 'jbloggs@acme.com', 'join_date': None, 'dob': None, 'known_as': None, 'marital_status': None, 'nationality': None, 'ethnicity': None, 'national_insurance_no': None, 'driving_license': None, 'ddi': None, 'work_ext': None, 'work_mobile': None, 'personal_mobile': None, 'home_telephone': None, 'personal_email': None, 'address1': None, 'address2': None, 'address3': None, 'city': None, 'county': None, 'postcode': None, 'country': None, 'linked_in': None, 'facebook': None, 'skype': None, 'twitter': None, 'bank_name': None, 'bank_branch': None, 'sort_code': None, 'account_number': None, 'building_society': None, 'ref_number': None, 'leaving_date': None, 'employee_ref': None, 'contract_provider': None, 'probation_date': None, 'remuneration_currency': {'id': 2, 'currency_code': 'GBP', 'currency_symbol': '£', 'description': 'British Pound', 'created_at': None, 'updated_at': None, 'deleted_at': None}, 'created_at': '2018-03-22T11:12:02+00:00', 'updated_at': '2018-03-22T11:12:02+00:00'}
>>> c.employees.count()
1
>>> c.employees.create({"first_name": "Pete", "last_name":"Smith", "email": "psmith@acme.com", "join_date": "01/01/2000"})
```

## Supported Objects and Methods
* Employees
    * `get()`
    * `create()`
    * `all()`