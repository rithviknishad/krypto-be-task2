import os
from django.http import HttpRequest, HttpResponse, HttpResponseNotAllowed, JsonResponse
from rest_framework.parsers import JSONParser

from core.models import Order
from django.db.models import Count
from django.conf import settings


def stats_view(request: HttpRequest):
    if request.method == "GET":
        query = Order.objects.values("currency").annotate(count=Count("currency"))
        stats = dict((x["currency"], x["count"]) for x in query)
        if "security" not in request.headers:
            raise Exception("No security token")
        # TODO: take token from settings which takes from env.
        if request.headers["security"] != settings.SECURITY_TOKEN:
            raise Exception("Invalid security token")
        return JsonResponse(stats, safe=False)

    return HttpResponseNotAllowed()
