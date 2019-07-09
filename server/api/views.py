from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .rest_framework_jsonp import JSONPRenderer
# from rest_framework.renderers import JSONRenderer
from django.db import connection
from django.conf import settings

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
        if serializer.data.get(settings.CALLBACK) is not None:
            return HttpResponse(
                JSONPRenderer().render(
                    res(serializer.data, label),
                    params=serializer.data, callback_parameter=settings.CALLBACK
                ),
                status=200
            )
        else:
            return JsonResponse(
                res(serializer.data, label),
                status=200
            )
    return JsonResponse(serializer.errors, status=400)


def sanity_check(request):
    with connection.cursor() as cur:
        cur.execute("select 1")
        one = cur.fetchone()[0]
        if one != 1:
            raise Exception('The site did not pass the health check')
    return HttpResponse('server is alive')
