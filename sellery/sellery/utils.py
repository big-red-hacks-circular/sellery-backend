from rest_framework import status
from rest_framework.response import Response


def success_response(data=None, status=status.HTTP_200_OK):
    """Returns a Response with `status` (200 default) and `data` if provided."""
    if data is None:
        return Response({"success": True}, status=status)
    return Response({"success": True, "data": data}, status=status)


def failure_response(message=None, status=status.HTTP_404_NOT_FOUND):
    """Returns a Response with `status` (404 default) and `message` if provided."""
    if message is None:
        return Response({"success": False}, status=status)
    return Response({"success": False, "error": message}, status=status)