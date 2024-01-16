from django.shortcuts import render


# Create your views here
def render_template(request):
    my_dict = {'name': 'mauthanh'}
    return render(request, 'templates_app/first_template.html', context=my_dict)


def render_employee(request):
    employee_dict = {'id': '123', 'name': 'mauthanh', 'sal': '10000'}
    return render(request, 'templates_app/first_template.html', context=employee_dict)
