from rest_framework import serializers

from .models import UserRequest

class UserRequestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserRequest
        fields = ['id', 'status', 'iin', 'first_name', 'middle_name', 'last_name', 'phone', 'department', 'management', 'job', \
            'db', 'login', 'password', 'request_date', 'create_date', 'create_author', 'change_date', 'change_author']