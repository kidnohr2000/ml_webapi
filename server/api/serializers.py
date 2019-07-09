from rest_framework import serializers


class IrisSerializer(serializers.Serializer):
    sepal_length = serializers.FloatField()
    sepal_width = serializers.FloatField()
    petal_length = serializers.FloatField()
    petal_width = serializers.FloatField()
    callback = serializers.CharField(required=False, max_length=20)
