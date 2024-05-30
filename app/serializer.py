from rest_framework import serializers
from .models import Person, Ministry, MustardSeed, Member, FirstTimer, Visitor

class PersonSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Person
        fields = '__all__'

    def validate(self, data):
        email = data.get('email') or ''
        telephone = data.get('telephone') or ''

        if Person.objects.filter(email=email).exists():
            raise serializers.ValidationError('User with this email Exists')
        if Person.objects.filter(telephone = telephone).exists():
            raise serializers.ValidationError('User with this telephone exists')
        return data

class MinistrySerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Ministry 
        fields = '__all__'
    def validate(self, data):
        
        name = data.get('name') or ''
        if Ministry.objects.filter(name=name).exists():
            raise serializers.ValidationError('Ministry with the same name exists')

        return data
class MustardSeedSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = MustardSeed
        fields = '__all__'
    
    def validate(self, data):
        name = data.get('name') or ''
        location = data.get('location') or ''

        if MustardSeed.objects.filter(name = name).exists():
            raise serializers.ValidationError('Mustard Seed with the same name exists')
        if MustardSeed.objects.filter(location = location).exists():
            raise serializers.ValidationError('Mustard Seed with the same location exists')
        
        return data

        


