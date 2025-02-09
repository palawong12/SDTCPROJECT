from django.urls import path
from . import views

urlpatterns = [
	path('', views.Home, name='home-page'),
	path('about/', views.AboutPage, name='about-page'),
	path('contact/', views.ContactUs, name='contact-page'),
	path('student/', views.Student, name='student-page'),
	path('posts/', views.posts, name="posts"),
	path('post/<slug:slug>/', views.post, name="post"),

		#Login
	path('login/', views.loginPage, name="login"),
	path('register/', views.registerPage, name="register"),
	path('logout/', views.logoutUser, name="logout"),
	path('account/', views.userAccount, name="account"),
	path('update_profile/', views.updateProfile, name="update_profile"),

		#UPDATE PATHS
	path('create_post/', views.createPost, name="create_post"),
	path('update_post/<slug:slug>/', views.updatePost, name="update_post"),
	path('delete_post/<slug:slug>/', views.deletePost, name="delete_post"),
	path('send_email/', views.sendEmail, name="send_email"),


]