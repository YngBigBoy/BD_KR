from django.db import models

# Define a model for a Blog Post
class BlogPost(models.Model):
    """
    A model representing a blog post.

    This model has the following fields:
     - title (models.CharField): The title of the blog post.
     - content (models.TextField): The content of the blog post.
     - created_at (models.DateTimeField): The date and time the blog post was created.
     - updated_at (models.DateTimeField): The date and time the blog post was last updated.
     - author (models.ForeignKey): A foreign key relationship to the User model representing the author of the blog post.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

# Define a model for a Comment on a Blog Post
class Comment(models.Model):
    """
    A model representing a comment on a blog post.

    This model has the following fields:
     - content (models.TextField): The content of the comment.
     - created_at (models.DateTimeField): The date and time the comment was created.
     - author (models.ForeignKey): A foreign key relationship to the User model representing the author of the comment.
     - post (models.ForeignKey): A foreign key relationship to the BlogPost model representing the blog post the comment is associated with.
    """
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
