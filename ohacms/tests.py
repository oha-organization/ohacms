import time

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium.webdriver.firefox.webdriver import WebDriver
from .models import Post
from .models import Option


class PostTestCase(TestCase):

    def setUp(self):
        Post.objects.create(name='Welcome', title='WelcomeTitle', description='Welcome description',
                            content='Welcome content', status='y', post_type='sayfa', order=1)
        Post.objects.create(name='About', title='AboutTitle', description='About description',
                            content='About content', status='y', post_type='sayfa', order=2)
        Option.objects.create(name='Title', description='Site Title', content='This is the site title')
        Option.objects.create(name='Description', description='Site Description', content='This is the description')
        Option.objects.create(name='Footer', description='Footer', content='Copyright 2020')

    def test_string_representation(self):
        post = Post(name='A sample name')
        self.assertEqual(str(post), post.name)

    def test_post_content(self):
        self.post = Post.objects.get(id=1)
        self.assertEqual(f'{self.post.name}', 'Welcome')
        self.assertEqual(f'{self.post.title}', 'WelcomeTitle')
        self.assertEqual(f'{self.post.description}', 'Welcome description')
        self.assertEqual(f'{self.post.content}', 'Welcome content')
        self.assertEqual(f'{self.post.status}', 'y')
        self.assertEqual(f'{self.post.post_type}', 'sayfa')
        self.assertEqual(f'{self.post.order}', '1')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1')
        no_response = self.client.get('/post/10000')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Welcome')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_context_processor_returns_posts(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # Total number of posts
        self.assertEqual(len(response.context['posts']), 2)
        self.assertEqual(response.context['posts'][0].name, 'Welcome')
        self.assertEqual(response.context['posts'][1].name, 'About')


class AdminLoginSeleniumTestCase(StaticLiveServerTestCase):
    #fixtures = ['user-data.json']

    def setUp(self):
        self.user = get_user_model().objects.create_superuser(
            username='testadmin',
            email='test@email.com',
            password='secret',
        )

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get(f'{self.live_server_url}/admin/')
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('testadmin')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('secret')
        # time.sleep(3)
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
        # time.sleep(3)
        # self.selenium.find_element_by_xpath('//*[@id="content-main"]/div[2]/table/tbody/tr/th/a').click()
        time.sleep(3)
