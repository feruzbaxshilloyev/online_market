from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Comment, Rating, Savat, SavatMahsulot, Xabar
from django.db.models import Avg


# Create your views here.

def home(request):
    prs = Product.objects.all().order_by('-created_at')
    ctx = {
        'prs': prs
    }

    return render(request, 'home.html', ctx)


def detail(request, id):
    pr = get_object_or_404(Product, id=id)
    user = pr.author
    comments = Comment.objects.filter(product=pr)
    ratings = Rating.objects.filter(product=pr)
    user_rating = Rating.objects.filter(product=pr, user=request.user).first()
    pr.views += 1
    user1 = request.user
    avg_rating = ratings.aggregate(Avg('score'))['score__avg'] if ratings.exists() else 0

    if request.method == 'POST':
        if 'comment' in request.POST:
            comment_text = request.POST.get('comment')
            Comment.objects.create(product=pr, user=request.user, text=comment_text)

        if request.method == 'POST':
            if 'rating' in request.POST:
                score = int(request.POST['rating'])
                if not Rating.objects.filter(product=pr, user=request.user).exists():
                    Rating.objects.create(product=pr, user=request.user, score=score)
                else:
                    Rating.objects.filter(product=pr, user=request.user).update(score=score)

        if avg_rating is not None:
            avg_rating = round(avg_rating, 2)

    ctx = {
        'product': pr,
        'comments': comments,
        'ratings': ratings,
        'avg_rating': avg_rating,
        'user': user,
        'user1': user1
    }

    return render(request, 'detail.html', ctx)


def comments(request, id):
    product = get_object_or_404(Product, id=id)
    coms = Comment.objects.filter(product=product).order_by('-created_at')

    context = {
        'product': product,
        'com': coms,
    }

    return render(request, 'comments.html', context)


@login_required
def savat_u(request):
    savat = Savat.objects.filter(user=request.user).first()

    if savat:
        savat_mahsulotlar = SavatMahsulot.objects.filter(savat=savat)
        products = [i.product for i in savat_mahsulotlar]
    else:
        products = []

    return render(request, 'savat.html', {'products': products})


def savat_rem(request, id):
    savat_mahsulot = get_object_or_404(SavatMahsulot, id=id)
    savat_mahsulot.delete()

    return redirect('app:savat_u')


@login_required
def add_savat(request, id):
    product = Product.objects.get(id=id)
    savat, created = Savat.objects.get_or_create(user=request.user)
    savat_mahsulot, created = SavatMahsulot.objects.get_or_create(savat=savat, product=product)
    if not created:
        savat_mahsulot.quantity += 1
        savat_mahsulot.save()

    return redirect('app:savat_u')


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        product = Product.objects.create(
            name=name,
            desc=desc,
            price=price,
            image=image,
            author=request.user
        )

        return redirect('app:home')

    return render(request, 'add_product.html')


def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    paginator = Paginator(products, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'products.html', {'products': page_obj})


@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, id=id, author=request.user)

    if request.method == 'POST':
        product.delete()
        return redirect('app:list')

    return render(request, 'confirm_del.html', {'product': product})


@login_required
def my_products(request):
    user = request.user
    products = Product.objects.filter(author=user).order_by('-created_at')
    return render(request, 'my_product.html', {'products': products})


def about(request):
    return render(request, 'about.html')


def contact(request):
    context = {}

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            if request.user.is_authenticated:
                Xabar.objects.create(
                    author=request.user,
                    desc=message
                )
                context['success_message'] = "Xabaringiz muvaffaqiyatli yuborildi!"
            else:
                context['error_message'] = "Xabar yuborish uchun iltimos tizimga kiring."
        else:
            context['error_message'] = "Iltimos, barcha maydonlarni to‘ldiring."

    return render(request, 'contact.html', context)


def xabarlar(request):
    if request.method == 'POST':
        if 'mark_as_read' in request.POST:
            Xabar.objects.update(is_view=True)
            return redirect('app:xabarlar')

        xabar_id = request.POST.get('xabar_id')
        if xabar_id:
            xabar = Xabar.objects.get(id=xabar_id)
            xabar.is_view = True
            xabar.save()

    xab = Xabar.objects.order_by('-created_at')
    user = request.user
    u_id = user.id
    return render(request, 'admin_mes.html', {'xabarlar': xab, 'u_id': u_id})


def my_comments(request):
    comments = Comment.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'my_com.html', {'comments': comments})
