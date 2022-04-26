from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'products/index.html')

def products(request):
    return render(request, 'products/products.html')

def test_context(request):
    context = {
        'title': 'store',
        'header': 'Добро пожаловать в самый интересный интернет магазин',
        'username': 'Иван Иванов',
        'products': [
            {'name':'Худи черного цвета с монограммами adidas Originals','price': 6090.00},
            {'name': 'Синяя куртка The North Face', 'price': 23725.00},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390.00},
        ],
        'promotion': True,
        'products_of_promotion': [
            {'name': 'Черный рюкзак Nike Heritage', 'price': 2340.00},
        ]
    }
    return render(request,'products/test-context.html',context)

def chasis_all(request):
    store_chasis = {
        'title': 'store',
        'header': 'Добро пожаловать!',
        'username': 'Владимир',
        'products': [
            {'name': 'PBP 1083 - колодки тормозные ,задние', 'price': 35.00},
            {'name': 'OC47OF - фильтр масляный', 'price': 22.50},
            {'name': 'Растворитель 746', 'price': 9.99},
        ],
        'promotion': True,
        'products_of_promotion_chasis': [
            {'name': 'Бампер от ауди 100','price': 100.00},
        ]
    }
    return render(request,'products/chasis.html',store_chasis)