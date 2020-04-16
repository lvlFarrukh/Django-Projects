from django.shortcuts import render
from django.http import HttpResponse
from .models import product, banner, contact_us, order, order_update
import math, json

# Create your views here.
def index(request):
    banners = banner.objects.all()
    products = product.objects.all()
    all_product = {}
    category = []
    for i in products:
        if i.category.lower() not in category:
            category.append(i.category.lower())
            all_product[i.category] = product.objects.filter(category = i.category)
    all_prod = []
    for item in all_product.items():
        prod = item[1]
        no_of_slides = range(1,math.ceil(len(prod)/4))
        # slide_range = range(len(item[1][1:]))
        all_prod.append([prod, no_of_slides])

    return render(request, 'shop/index.html', {'banner1': banners[0], 'banner2': banners[1:],
                                               'lenght': range(1,len(banners[1:])+1), 'no_of_slide': range(1,math.ceil(len(products)/4)),
                                               'product': all_prod})

def contact(request):
    if request.method == 'POST' and len(request.POST.get('name')) > 0:
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        contact = contact_us(name=name, email=email, msg=msg)
        contact.save()
    return render(request, 'shop/contact.html')

def Product(request, id):
    item = product.objects.get(product_id=id);
    # print(item.name)
    return render(request, 'shop/products.html',{'data': item});


def about(request):
    return render(request, 'shop/about.html')

def check_out(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        cnic = request.POST.get('cnic')
        p_number = request.POST.get('number')

        Order = order(name=name, email=email, address=address,
                      city=city, state=state, zip=zip, cnic=cnic, phone_number=p_number)
        Order.save()

        id = Order.order_id
        update = order_update(order_id=id, email=email)
        update.save()


        return render(request, 'shop/order_id.html', {'order_id': id})
    else:
        return render(request, 'shop/checkout.html')


def tracker(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('id')
            email = request.POST.get('email')
            data = order_update.objects.filter(order_id=id, email=email)
            all_data = []
            if len(data) > 1:
                for items in data:
                    all_data.append({'order_id': items.order_id, 'update_description': items.update_description,
                                     'date': items.update_time})
                response = json.dump(all_data)
                return HttpResponse(response)
        except:
            pass

    return render(request, 'shop/tracker.html');




