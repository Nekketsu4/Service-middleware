from rest_framework import serializers


class RegAuthSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=32)
    password = serializers.CharField(min_length=5, write_only=True)