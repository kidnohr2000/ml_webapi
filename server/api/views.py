from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer
from api.serializers import IrisSerializer

from .core.iris_classify import predict as iris_predict
from .engine.query import Response


@csrf_exempt
def get_iris_label(request):
    """
    List all code snippets, or create a new snippet.
    """
    res = Response()

    if request.method == 'GET':
        data = request.GET

    elif request.method == 'POST':
        data = JSONParser().parse(request)

    serializer = IrisSerializer(data=data)
    if serializer.is_valid():
        label = iris_predict(serializer.data)
        return JsonResponse(
            res(serializer.data, label),
            status=200
        )
    return JsonResponse(serializer.errors, status=400)
