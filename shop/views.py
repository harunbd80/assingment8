from django.shortcuts import render

# Create your views here.
def shop_def(request):
    return render(request,'shop/index.html')