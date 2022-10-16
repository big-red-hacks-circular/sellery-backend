import json

from sellery.utils import failure_response
from sellery.utils import success_response
from food.models import Food
from rest_framework import generics
from rest_framework import status

from .controllers.create_food_controller import CreateFoodController
from .serializers import FoodSerializer


class FoodView(generics.GenericAPIView):
    serializer_class = FoodSerializer

    def get(self, request):
        """Get all food."""
        food = Food.objects.all()
        return success_response(
            self.serializer_class(food, many=True).data, status.HTTP_200_OK
        )

    def post(self, request):
        """Create food."""
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return failure_response("POST body must be in JSON format.", status.HTTP_400_BAD_REQUEST)
        return CreateFoodController(data, self.serializer_class).process()