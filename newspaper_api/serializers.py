from rest_framework import serializers
from .models import Newspaper

class NewsPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newspaper
        fields = '__all__'