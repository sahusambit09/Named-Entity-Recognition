from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
import csv
import json
import os
from django.db.models import Q
from django.core import serializers
from .models import *
class Index(APIView):
    def get(self,request):
        module_dir = os.path.dirname(__file__)  # get current directory
        file_path = os.path.join(module_dir, 'meddata.csv')
        print(file_path)
        with open(file_path) as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        if MedicineDetails.objects.filter(sku_name__contains="Zendol"):
            # med_table = MedicineDetails.objects.all().delete()
            print("reached if")
        else:
            print("reached else")
            med_table=MedicineDetails.objects.bulk_create([ MedicineDetails(**q) for q in rows ])
        try:
            med_id=MedicineDetails.objects.get(auto_increment_id=request.GET.get("medicine_id"))
            return render(request, "medicine-detail.html")
        except Exception as e:
            print(e)
            return render(request,"index.html")
class Search(APIView):
    def get(self,request):
        request_keyword=request.GET.get("nom")
        print("TERM PARAM",request_keyword)
        q = MedicineDetails.objects.filter(sku_name__contains=request_keyword)
        serialized_obj = serializers.serialize('json', q)
        serialized_obj=json.loads(serialized_obj)

        return JsonResponse(serialized_obj,safe=False)
        # print("stuff got searched!!")

class MedDetailView(APIView):
    def get(self, request):
        req_med_id=request.GET.get("medicine_id")
        print(req_med_id)
        med_detail= MedicineDetails.objects.get(auto_increment_id=req_med_id)
        print(med_detail.Pack_size)
        return render(request, "medicine-detail.html",{"data":med_detail})
