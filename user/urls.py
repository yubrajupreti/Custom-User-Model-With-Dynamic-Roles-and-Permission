from django.urls import path, include

from rest_framework import routers

from .views import *

router=routers.DefaultRouter()
router.register('users', UserView, basename='users')
router.register('permission', PermissionView, basename='permissions')
router.register('group', GroupView, basename='group')
router.register('content', ContentTypeView, basename='content')




urlpatterns = [

	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework)')),
	# path("permission", PermissionView.as_view()),

]