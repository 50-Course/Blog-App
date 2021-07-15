from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Post
# Create your tests here

class BlogTests(TestCase):
    def setup(self):
        self.user = get_user_model().objects.create_user(
        username='testuser', 
        email='testuser@email.com', 
        password='secret')

    self.post = Post.objects.create(
        title='A good title here',
        body='nice body content',
        author= self.user,
    )

    def test_string_rep(self):
        post = Post(title='A sample title'),
        self.assertEqual(str(post), post.title)
    
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}, A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'A good content')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/10000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')