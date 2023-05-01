from rest_framework import serializers
from .models import MyUser

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username', 'email')
