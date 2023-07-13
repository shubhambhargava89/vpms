from django.contrib import admin  # Register your models here.
from .models import (
    Customer,
    Product,
    Cart,
    OrderPlaced,
    Feedback,
    MonthlyReport,
    DailyReport,
)
from django.utils.html import format_html
from django.urls import reverse


# admin.site.register(Customer)


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'mobile', 'locality', 'city',
                    'zipcode', 'state']


@admin.register(Feedback)
class FeedbackModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'mobile', 'city',
                    'pincode', 'state', 'description']


@admin.register(MonthlyReport)
class MonthlyReportModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'month', 'total_sales', 'total_orders', 'new_customers']


@admin.register(DailyReport)
class DailyReportModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'total_sales', 'total_orders', 'new_customers']


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price',
                    'discounted_price', 'description', 'brand', 'category',
                    'product_image']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']


@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'customer_info', 'product', 'product_info',
                    'quantity', 'ordered_date', 'status']

    def customer_info(self, obj):
        link = reverse("admin:vehicle_customer_change", args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>', link, obj.customer.name)

    def product_info(self, obj):
        link = reverse("admin:vehicle_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.description)
