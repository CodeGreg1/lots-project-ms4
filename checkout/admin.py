from django.contrib import admin
from .models import Order, OrderLineItem
# Register your models here.


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'date',
                        'delivery_cost', 'order_total',  # noqa
                        'grand_total', 'membership_num')

    fields = ('order_number', 'date', 'full_name',
                'email', 'postcode',  # noqa
                'town_or_city', 'street_address1',
                'street_address2', 'county', 'delivery_cost',
                'order_total', 'grand_total',)

    list_display = ('order_number', 'date', 
                    'membership_num', 'full_name',
                    'delivery_cost', 'order_total',
                    'grand_total')

    ordering = ('-date', )


admin.site.register(Order, OrderAdmin)
