
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index, name='index'),
    path('', views.landing_page, name='landing_page'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('login/', views.login, name='login'),


#     path('base/', views.base, name='base'),
#     path('beauty_and_personal_care/', views.beauty_and_personal_care, name='beauty_and_personal_care'),
#     path('blog/', views.blog, name='blog'),
#     path('books/', views.books, name='books'),
#     path('buy/', views.buy, name='buy'),
#     path('cart/', views.cart, name='cart'),
#     path('categories/', views.categories, name='categories'),
#     path('clothings/', views.clothings, name='clothings'),
#     path('contacts/', views.contacts, name='contacts'),
#     path('electronics', views.electronics, name='electronics'),
#     path('faq/', views.faq, name='faq'),
#     path('featured_deals/', views.featured_deals, name='featured_deals'),
#     path('furniture/', views.furniture, name='furniture'),
#     path('groceries/', views.groceries, name='groceries'),
#     path('health_and_wellnes/', views.health_and_wellnes, name='health_and_wellnes'),
#     path('home_appliances/', views.home_appliances, name='home_appliances'),


#     path('office_supplies/', views.office_supplies, name='office_supplies'),
#     path('search', views.search, name='search'),
#     path('services/', views.services, name='services'),
#     path('shop_now/', views.shop_now, name='shop_now'),

#     path('sports_and_indoors/', views.sports_and_indoors, name='sports_and_indoors'),
#     path('toys/', views.toys, name='toys'),
#     path('track/', views.track, name='track'),
#
]
