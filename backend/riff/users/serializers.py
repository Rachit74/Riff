# Rest Framework imports
from rest_framework import serializers

# App imports
from .models import Client

"""
Client Serializer
used to serialize and deserialize the data of Client (custom user model)
"""
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
        """
        Returns the user with validated data and hashed password
        """
        return user