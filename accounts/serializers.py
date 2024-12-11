from rest_framework import serializers

class userLoginSerializer():
    email = serializers.EmailField(required=True)
    