from django.contrib import admin
from .models import Category, FoodItem, Order, OrderItem, ContactMessage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'is_available',
        'is_featured'
    )

    list_filter = (
        'category',
        'is_available',
        'is_featured'
    )

    search_fields = (
        'name',
        'description'
    )


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer_name',
        'phone',
        'total_amount',
        'status',
        'created_at'
    )

    list_filter = (
        'status',
        'created_at'
    )

    search_fields = (
        'customer_name',
        'phone',
        'email'
    )

    inlines = [OrderItemInline]


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'subject',
        'created_at'
    )

    search_fields = (
        'name',
        'email',
        'subject'
    )