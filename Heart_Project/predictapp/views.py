from django.shortcuts import render, HttpResponse
from django.views import View
from django.conf import settings
import numpy as np
from joblib import load
from .models import HeartUser


# Create your views here.

def load_model(name):
    model_path = "predictapp/media/ml_model/heart-predict-model.joblib"
    model = load(model_path)
    return model

class heart_predict(View):
    def get(self, request):
        return render(request, "predictapp/heart-web.html")
    
    def post(self, request):
        try:
            name = request.POST.get("name")
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

            HeartUser.objects.create(
                name=name,
                age=age,
                sex=sex,
                cp=cp,
                trestbps=trestbps,
                restecg=restecg,
                thalach=thalach,
                exang=exang,
                oldpeak=oldpeak,
                slope=slope,
                ca=ca,
                thal=thal,
                dial = result
            )

            if result[0] == 0: return render(request, "predictapp/fine.html")
            else: return render(request, "predictapp/not-fine.html")

        except:
            return HttpResponse("Có dữ liệu không phải số, hãy nhập lại!")
