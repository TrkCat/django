from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post
from datetime import datetime, time

class LatestPostsFeed(Feed):
	title = 'Latest Blog Posts'
	link = '/postfeed/'
	description = 'latest five posts from the blog'

	def items(self):
		return Post.objects.order_by('-published_date')[:5]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.text

	def item_author_name(self, item):
		return item.author

	def item_pubdate(self, item):
		return datetime.combine(item.published_date, time())

	def item_link(self, item):
		return reverse('blog_detail', args=[item.pk])
