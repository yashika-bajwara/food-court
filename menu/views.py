from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, FoodItem, Order, OrderItem, ContactMessage


def home(request):
    featured_foods = FoodItem.objects.filter(
        is_available=True,
        is_featured=True
    )[:6]

    categories = Category.objects.all()

    return render(request, 'menu/home.html', {
        'featured_foods': featured_foods,
        'categories': categories,
    })


def menu(request):
    categories = Category.objects.all()
    foods = FoodItem.objects.filter(is_available=True)

    category_id = request.GET.get('category')

    if category_id:
        foods = foods.filter(category_id=category_id)

    return render(request, 'menu/menu.html', {
        'foods': foods,
        'categories': categories,
    })


def order(request):

    if request.method == 'POST':

        food_id = request.POST.get('food_id')
        quantity = int(request.POST.get('quantity', 1))

        food = get_object_or_404(
            FoodItem,
            id=food_id,
            is_available=True
        )

        customer_name = request.POST.get('customer_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        table_number = request.POST.get('table_number')
        address = request.POST.get('address')

        total = food.price * quantity

        new_order = Order.objects.create(
            customer_name=customer_name,
            phone=phone,
            email=email,
            table_number=table_number,
            address=address,
            total_amount=total
        )

        OrderItem.objects.create(
            order=new_order,
            food=food,
            quantity=quantity,
            price=food.price
        )

        return redirect('success', order_id=new_order.id)

    foods = FoodItem.objects.filter(is_available=True)

    selected_food = request.GET.get('food')

    return render(request, 'menu/order.html', {
        'foods': foods,
        'selected_food': selected_food,
    })


def success(request, order_id):
    order_data = get_object_or_404(Order, id=order_id)

    return render(request, 'menu/success.html', {
        'order': order_data
    })


def contact(request):

    if request.method == 'POST':

        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )

        return render(request, 'menu/contact.html', {
            'success': True
        })

    return render(request, 'menu/contact.html')