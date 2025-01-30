from rest_framework import serializers

from doctors.models import Department, Doctor, DoctorAvailability


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class DoctorAvailabilitySerializer(serializers.Model):
    class Meta:
        model = DoctorAvailability
        fields = '__all__'
    

