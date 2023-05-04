from rest_framework import serializers
from .models import HomePageSlider


class HomePageSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePageSlider
        fields = '__all__'