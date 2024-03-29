from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Products
from store.models.category import Category
from django.views import View
from django.views.decorators.cache import cache_control


# Create your views here.
class Index(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return HttpResponseRedirect('store')

    def get(self , request):
        # print()
        request.session.clear()
        return HttpResponseRedirect('/login')
    

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def store(request):
    if (request.session.get('customer')):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Products.get_all_products_by_categoryid(categoryID)
        else:
            products = Products.get_all_products();

        data = {}
        data['products'] = products
        data['categories'] = categories

        print('you are : ', request.session.get('email'))
        return render(request, 'index.html', data)
    else:
        return redirect('login')