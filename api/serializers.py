from django.db.models import fields
from rest_framework import serializers
from .models import *


class OfficialSerializer(serializers.ModelSerializer):
    purok = serializers.CharField(source='purok.name')

    class Meta:
        model = Official
        fields = ('position', 'firstname', 'middlename',
                  'lastname', 'purok', 'contact', 'email')


class CaseSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField(source='resident.firstname')
    middlename = serializers.CharField(source='resident.middlename')
    lastname = serializers.CharField(source='resident.lastname')
    purok = serializers.CharField(source='resident.purok.name')

    class Meta:
        model = Case
        fields = ('id', 'firstname', 'middlename',
                  'lastname', 'purok', 'status', 'created_at')


class CasesCountSerializer(serializers.Serializer):
    total = serializers.IntegerField()
    active = serializers.IntegerField()
    recovered = serializers.IntegerField()
    deaths = serializers.IntegerField()


class PostSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField(source='official.firstname')
    position = serializers.CharField(source='official.position')

    class Meta:
        model = Post
        fields = ('position', 'firstname', 'hashtag',
                  'content', 'created_at')


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'
