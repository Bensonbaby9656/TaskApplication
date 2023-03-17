from rest_framework import serializers
from api.models import Tasks
from django.contrib.auth.models import User

# localhost:8000/user/
# post
# data=("user_name":"abc","password":"pwsd","email":"abc@gmail.com","first_name":"bsn","last_name":"ngdf")

class TaskSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    created_date=serializers.DateTimeField(read_only=True)
    status=serializers.BooleanField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Tasks
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=User
        fields=["id","username","password","email","first_name","last_name"]