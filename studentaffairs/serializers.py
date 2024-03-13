from rest_framework import serializers
from .models import Activity, Disciplinary, Damages, Hostel, Games

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"

class DisciplinarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplinary
        fields = "__all__"

class DamagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Damages
        fields = "__all__"

class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = "__all__"

class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = "__all__"

