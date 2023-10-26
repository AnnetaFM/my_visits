from rest_framework import serializers

from .models import SalePoint, Visit, Worker


class SalePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalePoint
        fields = '__all__'


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('shop', 'latitude', 'longitude')


class WorkerSerializer(serializers.Serializer):
    class Meta:
        model = Worker
        fields = '__all__'
