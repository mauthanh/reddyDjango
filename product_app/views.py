from django.shortcuts import render


def products_view(request):
    return render(request, 'product_app/index.html')


def electronics_view(request):
    electronic_dict = {
        'product_1': 'Mac',
        'product_2': 'iPhone',
        'product_3': 'iPad',
    }
    return render(request, 'product_app/product_list.html', context=electronic_dict)


def toys_view(request):
    toy_dict = {
        'product_1': 'remote car',
        'product_2': 'chess board',
        'product_3': 'laser gun',
    }
    return render(request, 'product_app/product_list.html', context=toy_dict)


def shoe_view(request):
    shoe_dict = {
        'product_1': 'adidas',
        'product_2': 'nike',
        'product_3': 'thuong dinh',
    }
    return render(request, 'product_app/product_list.html', context=shoe_dict)
