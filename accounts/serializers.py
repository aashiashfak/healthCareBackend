from rest_framework import serializers

class userLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    