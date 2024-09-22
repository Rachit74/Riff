from rest_framework import serializers

from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    """
    override the default create method to hash the password
    
    validated_data is used to validate each field for constraints and dublicates
    """
    def create(self, validated_data):
        user = Client(
            username=validated_data['username'],
            email=validated_data['email'],
            artist=validated_data.get('artist', False)  # Default to False if not provided
        )
        user.set_password(validated_data['password'])
        user.save()
        return user