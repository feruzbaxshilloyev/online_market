from django.shortcuts import render
from app.models import Product


def search(request):
    query = request.GET.get('q', '')
    results = Product.objects.filter(name__icontains=query, desc__icontains=query)
    return render(request, 'search.html', {'results': results, 'query': query})
