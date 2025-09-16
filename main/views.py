from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import FitForm
from main.models import Fit

def show_xml_by_id(request, produk_id):
   try:
        fit_item = Fit.objects.filter(pk=produk_id)
        xml_data = serializers.serialize("xml", fit_item)
        return HttpResponse(xml_data, content_type="application/xml")
   except Fit.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, produk_id):
   try:
       fit_item = Fit.objects.get(pk=produk_id)
       json_data = serializers.serialize("json", [fit_item])
       return HttpResponse(json_data, content_type="application/json")
   except Fit.DoesNotExist:
       return HttpResponse(status=404)

def show_json(request):
    fit_list = Fit.objects.all()
    json_data = serializers.serialize("json", fit_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml(request):
     fit_list = Fit.objects.all()
     xml_data = serializers.serialize("xml", fit_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_main(request):
    fit_list = Fit.objects.all()

    context = {
        'npm' : '2406423282',
        'name': 'Keira Nuzahra Anjani',
        'class': 'PBP D',
        'fit_list': fit_list
    }

    return render(request, "main.html", context)

def create_produk(request):
    form = FitForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_produk.html", context)

def show_produk(request, id):
    produk = get_object_or_404(Fit, pk=id)
    produk.increment_views()

    context = {
        'produk': produk
    }

    return render(request, "produk_detail.html", context)