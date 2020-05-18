from django.urls import path, include
from blogging.views import detail_view, list_view, PostViewSet, CategoryViewSet
from rest_framework import routers
from blogging.feeds import LatestPostsFeed

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'posts', PostViewSet)


urlpatterns = [
	path('', list_view, name='blog_index'),
	path('posts/<int:post_id>/', detail_view, name='blog_detail'),
	path('', include(router.urls)),
	path('latest/feed/', LatestPostsFeed()),
]
