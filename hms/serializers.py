from rest_framework import serializers
from .models import *

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
    
    def validate(self, data):
        if data['age'] < 0 or data['age'] > 120:
            raise serializers.ValidationError("Age must be between 0 and 120.")
        return data
       
    def validate_phone_number(self, value):
        if value is not None and len(str(value)) > 11:
            raise serializers.ValidationError("Phone number must be 11 digits or less.")
        return value
    