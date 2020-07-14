from django.shortcuts import render


def store(request):
    context = {}
    return render(request, 'store/main.html', context)


def order(request):
    context = {}
    return render(request, 'store/order.html', context)


def pay(request):
    context = {}
    return render(request, 'store/pay.html', context)


def contact(request):
    context = {}
    return render(request, 'store/contact.html', context)


def search(request):
    context = {}
    return render(request, 'store/search.html', context)
