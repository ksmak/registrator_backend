from django.test import TestCase
from .models import UserRequest
from datetime import datetime
from django.contrib.auth.models import User
import json


class UserRequestTestCase(TestCase):
    def setUp(self):
        self.data = {
            'id': 1,
            'status': 1,
            'iin': 111111111111,
            'first_name': 'FirstName',
            'middle_name': 'MiddleName',
            'last_name': 'LastName',
            'phone': 77000000000,
            'department': 1,
            'management': 1,
            'job': 'Job',
            'login': 'Login',
            'password': 'Password',
            'db': 1,
            'request_date': '2022-07-20'
        }
        self.username = 'TestUser'
        self.password = '12345'
        self.dictionaries = {
            'statuses': [list(n) for n in UserRequest.STATUS],
            'managements': [list(n) for n in UserRequest.MANAGEMENT],
            'departments': [list(n) for n in UserRequest.DEPARTMENT],
            'dbs': [list(n) for n in UserRequest.DB]
        }
  
    def test_user_request_model(self):
        UserRequest.objects.create(
            status=self.data['status'],
            iin=self.data['iin'],
            first_name=self.data['first_name'],
            middle_name=self.data['middle_name'],
            last_name=self.data['last_name'],
            phone=self.data['phone'],
            department=self.data['department'],
            management=self.data['management'],
            job=self.data['job'],
            login=self.data['login'],
            password=self.data['password'],
            db=self.data['db'],
            request_date=datetime.strptime(self.data['request_date'], "%Y-%m-%d").date()
        )
        ur = UserRequest.objects.get(iin=self.data['iin'])
        self.assertEqual(ur.status, self.data['status'])
        self.assertEqual(ur.iin, self.data['iin'])
        self.assertEqual(ur.first_name, self.data['first_name'])
        self.assertEqual(ur.middle_name, self.data['middle_name'])
        self.assertEqual(ur.last_name, self.data['last_name'])
        self.assertEqual(ur.phone, self.data['phone'])
        self.assertEqual(ur.department, self.data['department'])
        self.assertEqual(ur.management, self.data['management'])
        self.assertEqual(ur.job, self.data['job'])
        self.assertEqual(ur.login, self.data['login'])
        self.assertEqual(ur.password, self.data['password'])
        self.assertEqual(ur.db, self.data['db'])
        self.assertEqual(ur.request_date, datetime.strptime(self.data['request_date'], "%Y-%m-%d").date())
        ur.delete()

    def test_user_request_client(self):
        user = User.objects.create_user(username=self.username, password=self.password)
        self.assertEqual(user.is_active, 1, 'Active User')
        # get token
        response = self.client.post('/api/token/', {'username': self.username, 'password': self.password}, content_type='application/json')
        self.assertEqual(response.status_code, 200, response.content)
        access = response.data['access']
        refresh = response.data['refresh']
        # refresh token
        response = self.client.post('/api/token/refresh/', {'refresh': refresh}, content_type='application/json')
        self.assertEqual(response.status_code, 200, response.content)
        access = response.data['access']
        # test list
        response = self.client.get('/user_requests/', content_type='application/json', HTTP_AUTHORIZATION='Bearer ' + access)
        self.assertEqual(response.status_code, 200, response.content)
        # test create
        response = self.client.post('/user_requests/', self.data, content_type='application/json', HTTP_AUTHORIZATION='Bearer ' + access)
        self.assertEqual(response.status_code, 201, response.content)
        ur = response.data
        # test update
        response = self.client.put(f"/user_requests/{ur['id']}/", ur, content_type='application/json', HTTP_AUTHORIZATION='Bearer ' + access)
        self.assertEqual(response.status_code, 200, response.content)
        # test get
        response = self.client.get(f"/user_requests/{ur['id']}/", content_type='application/json', HTTP_AUTHORIZATION='Bearer ' + access)
        self.assertEqual(response.status_code, 200, response.content)
        # test delete
        response = self.client.delete(f"/user_requests/{ur['id']}/", ur, content_type='application/json', HTTP_AUTHORIZATION='Bearer ' + access)
        self.assertEqual(response.status_code, 204, response.content) 
        # test get dictionaries
        response = self.client.get('/user_requests/get_dicts/', content_type='application/json', HTTP_AUTHORIZATION='Bearer ' + access)
        self.assertEqual(response.status_code, 200, response.content)
        self.assertDictEqual(json.loads(response.content), self.dictionaries)