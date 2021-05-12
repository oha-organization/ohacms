from django.test import TestCase
from .models import Post


class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(name='Welcome', title='WelcomeTitle', description='Welcome index',
                            content='Welcome content', status='y', post_type='sayfa', order=1)

    def test_post_name_is_equal_entered_name(self):
        """Is Post name equal entered name"""
        post1 = Post.objects.get(name='Welcome')
        self.assertEqual(post1.name, 'Welcome')
