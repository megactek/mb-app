from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.


class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='just a test')
        Post.objects.create(text='just a test 2')
        Post.objects.create(text='just a test 3')
    
    def test_text_content(self):
        post=Post.objects.get(id=1)
        posta=Post.objects.get(id=2)
        postb=Post.objects.get(id=3)
        expected_object_name = f'{post.text}'
        expecteda_object_name = f'{posta.text}'
        expectedb_object_name = f'{postb.text}'
        self.assertEqual(expected_object_name, 'just a test')
        self.assertEqual(expecteda_object_name, 'just a test 2')
        self.assertEqual(expectedb_object_name, 'just a test 3')


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='this is another test')

    def test_view_url_exist_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')