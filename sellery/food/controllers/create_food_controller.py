from sellery.utils import failure_response
from sellery.utils import success_response
from food.models import Food
from rest_framework import status
from .detect_web import detect_web

class CreateFoodController:
    def __init__(self, data, serializer):
        self._data = data
        self._serializer = serializer

    def process(self):
        # Verify that all required fields are provided
        base64_image = self._data.get("base64_image")
        if base64_image is None:
            return failure_response(
                "POST body is misformatted. Expecting JSON in the format {base64_image: [base64 string]}", 
                status.HTTP_400_BAD_REQUEST
            )

        name, labels = detect_web(base64_image)

        # Create and return food with the given fields
        food = Food.objects.create(
            name=name,
            labels=','.join(labels),
            img_url=base64_image # TODO: Store in AWS S3
        )
        food.save()
        return success_response(
            self._serializer(food).data, status.HTTP_201_CREATED
        )