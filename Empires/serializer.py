from rest_framework import serializers

from .models import AgeofEmpries


#Serializers define the API representation.

class EmpriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeofEmpries
        fields = '__all__'