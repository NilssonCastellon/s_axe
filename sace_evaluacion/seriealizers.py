from rest_framework import serializers
from .models import EVALUACION

class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EVALUACION
        fields = '__all__'