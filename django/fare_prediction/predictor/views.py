from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FarePredictionSerializer
from predictor.predictor_logic import predict_fare
from fare_prediction.predictor.predictor_logic import predict_fare



class FarePredictionView(APIView):
    def post(self, request):
        serializer = FarePredictionSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data
            features = [
                data["passenger_count"], data["trip_distance"], data["fare_amount"],
                data["extra"], data["tip_amount"], data["total_amount"]
            ]
            prediction = predict_fare(features, model_type=data["model_type"])
            return Response({"predicted_fare": prediction})
        
        return Response(serializer.errors, status=400)
