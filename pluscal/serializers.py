from dataclasses import field
from rest_framework import serializers
from pluscal.models import calc

class calsSerializer(serializers.ModelSerializer):
    class Meta:
        model = calc
        fields = "__all__"

