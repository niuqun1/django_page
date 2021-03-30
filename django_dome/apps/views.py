from django.shortcuts import render,HttpResponse
from django.views.generic import View

# Create your views here.
# class index(View):
#     def get(self,request):
#         return HttpResponse('hello word')


# class index(View):
#     def get(self,request):
#         name = request.GET.get('name','')
#         age = request.GET.get('age',0)
#         return HttpResponse(f'hello word {name} {age}')

class index(View):
    def get(self,request,name,age):
        return HttpResponse(f'hello word {name} {age}')