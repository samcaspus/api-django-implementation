from rest_framework import serializers

from .models import JobsList

class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JobsList
        fields = ('jobTitle', 'jobDescription','jobUrl','createdTime')