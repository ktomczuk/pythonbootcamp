from django.shortcuts import render, HttpResponse

# Create your views here.

def hello_world(request):
    return HttpResponse('Helllllo')


def hello_world_name(request, name):
    return HttpResponse('Helllllo' + name)



def product_list(request):
    products = Product.objects.all()
    return render(
        request=request,
        context=(),
        template_name='products_list.html'
    )
