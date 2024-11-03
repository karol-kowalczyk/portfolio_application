from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .stocks_database import stocks
import json
from django.utils.text import slugify

# Create your views here.
def stocks_overview(request):
    return HttpResponse("Hej")

def stocks_data(request, stocks_id):
    return JsonResponse({"result": slugify(stocks[stocks_id]['company_name'])})

def slug_data_view(request, slug_id):
    gadget_match = {"result":"nothing to show u!"}

    for stock in stocks:
        if slugify(stock["company_name"]) == slug_id:
            gadget_match = stock

    return JsonResponse(gadget_match)