from rest_framework import serializers

class FarePredictionSerializer(serializers.Serializer):
    model_type = serializers.ChoiceField(choices=["linear", "random_forest", "svm"])
    passenger_count = serializers.FloatField()
    trip_distance = serializers.FloatField()
    fare_amount = serializers.FloatField()
    extra = serializers.FloatField()
    tip_amount = serializers.FloatField()
    total_amount = serializers.FloatField()
