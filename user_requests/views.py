from django.shortcuts import render
from django.http import JsonResponse, FileResponse, HttpResponse
from . import services


def get_all_dictionaries(request):
    return JsonResponse(services.get_dictionaries())

def check_iin(request):
    id = request.GET['id']
    status = request.GET['status']
    db = request.GET['db']
    iin = request.GET['iin']
    return JsonResponse(services.check_iin(id, status, db, iin))

def check_phone(request):
    id = request.GET['id']
    status = request.GET['status']
    db = request.GET['db']
    phone = request.GET['phone']
    return JsonResponse(services.check_phone(id, status, db, phone))

def print_vedomost(request):
    ids = request.GET.getlist('ids')

    file = services.get_report(ids)

    response = FileResponse(file)

    return response

def send_vedomost(request):
    ids = request.GET.getlist('ids')
    to_addr = request.GET['to_addr']
    zip_pas = request.GET['zip_pas']

    services.send_report(ids, to_addr, zip_pas)

    response = HttpResponse(status=200)
    
    return response

def get_addr_list(request):
    return JsonResponse(services.get_addr_list())