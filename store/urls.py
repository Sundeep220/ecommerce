from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('logout_request', views.logout_request, name="logout_request"),
	path('login_request', views.login_request, name="login_request"),
	path('register', views.register, name="register"),
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

]