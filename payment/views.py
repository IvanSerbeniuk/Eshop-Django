from django.shortcuts import render
from .models import ShippingAddress, Order, OrderItem

from cart.cart import Cart
from django.views.decorators.csrf import csrf_protect 
from django.http import JsonResponse

@csrf_protect
def checkout(request):

    # Users with account -- Pre-fill the form
    if request.user.is_authenticated: #if user login

        try:
            # Authinticated users WITH shippping info
            shipping_address = ShippingAddress.objects.get(user=request.user.id)

            context = {'shipping': shipping_address}

            return render(request, 'payment/checkout.html', context=context)

        except:
            # Authenticated user without shipping info
            return render(request, 'payment/checkout.html')
    
    else: # Можно и без else :)
        # Guest users
        return render(request, 'payment/checkout.html')


@csrf_protect
def complete_order(request):

    if request.POST.get('action') == 'post':

        name = request.POST.get('name')
        email = request.POST.get('email')

        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')

        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')

        # All-in-one shipping address
        shipping_address = (address1 + '\n' + address2 + '\n' + city + '\n' + state + '\n' + zipcode)

        # Shopping cart info
        cart = Cart(request)

        # Get total price of items
        total_cost = cart.get_total()
               
    
    # 1) Creqte Order --> users with an account
    if request.user.is_authenticated:

        order = Order.objects.create(full_name=name, email=email, shipping_address=shipping_address,
        amount_paid=total_cost, user=request.user)

        order_id = order.pk

        for item in cart:
            
            OrderItem.objects.create(order_id=order_id, product=item['product'], quantity=item['qty'],
                                     price=item['price'], user=request.user)

    # 2) Create order --> Guest user without an account
    else:

        order = Order.objects.create(full_name=name, email=email, shipping_address=shipping_address,
        amount_paid=total_cost)                     #m Thank to blank=True, null=True in models we can not include  'user'

        order_id = order.pk
  
        for item in cart:
            
            OrderItem.objects.create(order_id=order_id, product=item['product'], quantity=item['qty'],
                                        price=item['price'])

    order_success = True 

    response = JsonResponse({'success':order_success})

    return response




@csrf_protect
def payment_success(request):
    # Clear shopping cart

    for key in list(request.session.keys()):

        if key == 'session_key':

            del request.session[key]

    return render(request, 'payment/payment-success.html')



@csrf_protect
def payment_failed(request):

    return render(request, 'payment/payment-failed.html')