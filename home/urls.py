from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about_us.html', views.about_us, name='about_us'),
    # path('contact.html', views.contact, name='contact'),
    path('links.html', views.links, name='links'),
    path('membership.html', views.membership, name='membership'),
    path('publications.html', views.publications, name='publications'),
    path('sales.html', views.sales, name='sales'),
    path('admin/', views.admin, name='admin'),
    path('admin/news/post/add', views.add_post, name='add_post'),
    path('membership-type/tlb-lbm-world.html', views.TLWorld, name='tlworld'),  # noqa
    path('membership-type/tlb-world.html', views.TWorld, name='tworld'),  # noqa
    path('membership-type/lbm-world.html', views.LWorld, name='lworld'),  # noqa
    path('membership-type/lbm-europe.html', views.LEu, name='leu'),  # noqa
    path('membership-type/tlb-europe.html', views.TEu, name='teu'),  # noqa
    path('membership-type/tlb-lbm-europe.html', views.TLEu, name='tleu'),  # noqa
    path('membership-type/tlb-lbm-uk.html', views.TLUk, name='tluk'),  # noqa
    path('membership-type/tlb-uk.html', views.TUk, name='tuk'),  # noqa
    path('membership-type/lbm-uk.html', views.LUk, name='luk'),  # noqa
]
