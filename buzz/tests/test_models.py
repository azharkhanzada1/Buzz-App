from django.test import TestCase
from django.contrib.auth.models import User
from buzz.models import Post, Comment, View, Like
from datetime import datetime
from django.db.utils import IntegrityError

class PostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")

    def test_create_post(self):
        post = Post.objects.create(
            title = "Test Title",
            content = "Test Content",
            author = self.user
        )

        self.assertEqual(post.title, "Test Title")
        self.assertEqual(post.content, "Test Content")
        self.assertEqual(post.author, self.user)
        self.assertIsNotNone(post.created_at)
        self.assertIsNotNone(post.updated_at)

    def test_update_post(self):
        post = Post.objects.create(
            title="Initial Title",
            content="Initial Content",
            author=self.user
        )

        post.title = "Updated Title"
        post.content = "Updated Content"  # Corrected to match the expected value
        post.save()

        post.refresh_from_db()

        self.assertEqual(post.title, "Updated Title")
        self.assertEqual(post.content, "Updated Content")
        self.assertIsNotNone(post.created_at)
        self.assertNotEqual(post.created_at, post.updated_at)

    def test_post_str_representation(self):
            post = Post.objects.create(
                title='Test Title',
                content='Test Content',
                author=self.user
            )
            self.assertEqual(str(post), "Test Title")



class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password='testpassword')
        self.post = Post.objects.create(
            title = "Test Post",
            content = "Test Content",
            author = self.user
        )
    
    def test_create_comment(self):
        comment = Comment.objects.create(
            post = self.post,
            author = self.user,
            content = "Test Content"
        )

        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.author, self.user)
        self.assertEqual(comment.content, "Test Content")
        self.assertIsNotNone(comment.created_at)
        self.assertIsInstance(comment.created_at, datetime)

    def test_comment_str_representation(self):
        comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            content="Test Content"
        )
        self.assertEqual(str(comment), "Test Content")

    def test_comment_without_content(self):
        with self.assertRaises(IntegrityError):
            Comment.objects.create(
                post = self.post,
                author = self.user,
                content = None
            )
class LikeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.post = Post.objects.create(
            title= "Test Post",
            content =" Test Content",
            author=self.user
        )

    def test_create_like(self):
        like = Like.objects.create(
            post = self.post,
            user = self.user
        )
        self.assertEqual(like.post, self.post)
        self.assertEqual(like.user, self.user)
        self.assertIsNotNone(like.created_at)
        self.assertIsInstance(like.created_at, datetime)

    def test_like_str_representation(self):
        like = Like.objects.create(
            post = self.post,
            user = self.user
        )
        self.assertEqual(str(like), f"Like by {self.user.username} on {self.post.title}")

    def test_like_unique_constraint(self):
        Like.objects.create(
            post = self.post,
            user = self.user
        )
        with self.assertRaises(Exception):
            Like.objects.create(
                post = self.post,
                user = self.user  
            )

class ViewModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="username", password='testpassword')
        self.post = Post.objects.create(
            title = "Test Post",
            content = "Test Content",
            author = self.user
        )
    
    def test_create_view(self):
        view = View.objects.create(
            post = self.post,
            user = self.user
        )
        self.assertEqual(view.post, self.post)
        self.assertEqual(view.user, self.user)
        self.assertIsNotNone(view.created_at)
        self.assertIsInstance(view.created_at, datetime)

    def test_view_str_representation(self):
        view = View.objects.create(
            post = self.post,
            user = self.user
        )
        self.assertEqual(str(view), f"View by {self.user.username} on {self.post.title}")

    def test_view_unique_constraint(self):
        view = View.objects.create(
            post = self.post,
            user = self.user
        )
        with self.assertRaises(Exception):
            View.objects.create(
                post = self.post,
                user = self.user
            )

    def test_multiple_views(self):
        # Test multiple views by different users on the same post
        another_user = User.objects.create_user(username="anotheruser", password="anotherpassword")
        view1 = View.objects.create(post=self.post, user=self.user)
        view2 = View.objects.create(post=self.post, user=another_user)

        self.assertEqual(View.objects.count(), 2)
        self.assertEqual(view1.post, self.post)
        self.assertEqual(view2.post, self.post)
        self.assertNotEqual(view1.user, view2.user)