from rest_framework import serializers
from .models import Doctor, Department, DoctorAvailability, MedicalNote

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
    
class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailability
        fields = '__all__'

class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = '__all__'
        
        # Lo siguiente son mejores prácticas para definir los campos
        
        # Opción 1: Lista explícita de campos
        #fields = ['id', 'first_name', 'last_name', 'email', 'phone']
        
        # Opción 2: Lista explícita + exclude
        #fields = ['id', 'first_name', 'last_name', 'email']
        #exclude = ['password', 'secret_token']
    

