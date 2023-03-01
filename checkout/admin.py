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
                        'grand_total', 'membership_num',
                        'original_bag', 'stripe_pid',)

    fields = ('order_number', 'date', 'membership_num',
              'full_name', 'email', 'street_address1',
              'street_address2', 'town_or_city', 'county',
              'postcode', 'delivery_cost', 'order_total',
              'grand_total',)

    list_display = ('order_number', 'date',
                    'membership_num', 'full_name',
                    'delivery_cost', 'order_total',
                    'grand_total')

    ordering = ('-date', )


admin.site.register(Order, OrderAdmin)
