from rest_framework import serializers
from app1.models import student_Data

# Create serializers 
class serializers_data(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=student_Data
        fields='__all__'