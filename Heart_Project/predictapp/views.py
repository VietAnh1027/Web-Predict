from django.shortcuts import render, HttpResponse
from django.views import View
from django.conf import settings
import numpy as np
from joblib import load


# Create your views here.

def load_model(name):
    model_path = "predictapp/media/ml_model/heart-predict-model.joblib"
    model = load(model_path)
    return model

class heart_predict(View):
    def get(self, request):
        return render(request, "predictapp/myversion.html")
    
    def post(self, request):
        try:
            age = int(request.POST.get("age"))
            sex = int(request.POST.get("sex"))
            cp = int(request.POST.get("cp"))
            trestbps = int(request.POST.get("trestbps"))
            restecg = int(request.POST.get("restecg"))
            thalach = int(request.POST.get("thalach"))
            exang = int(request.POST.get("exang"))
            oldpeak = float(request.POST.get("oldpeak"))
            slope = int(request.POST.get("slope"))
            ca = int(request.POST.get("ca"))
            thal = int(request.POST.get("thal"))

            data = [[age, sex, cp, trestbps, restecg, thalach, exang, oldpeak, slope, ca, thal]]
            model = load_model("heart-predict-model.joblib")
            result = model.predict(data)
            if result[0] == 0: return HttpResponse("Bạn không có nguy cơ mắc bệnh tim!")
            else: return HttpResponse("Bạn có khả năng cao mắc bệnh tim!")

        except:
            return HttpResponse("Có dữ liệu không phải số, hãy nhập lại!")
