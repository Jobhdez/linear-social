from django.db import models
from django.contrib.auth.models import AbstractUser

"""Module that corresponds to the models of the server.

Models include: 

         - `User` which inherits from AbstractUser to extend the fields with `friends`
     which store the number of friends each user has.
     
         - `FriendRequest` which stores the friendship connection.
         
         - `LinearAlgebraExpression` which stores the linear algebra expression we will be evaluating.

Usage:
    >>> from api.models import User
    >>> Users.object.get(id=<id>)
    >>> <User>
"""


from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Inherits `AbstractUser` to allow the friendship between
    two users or more."""
    friends = models.ManyToManyField("User", blank=True)
    study_groups = models.ManyToManyField("BookStudy")
    class Meta:
        app_label = 'api'
   
class FriendRequest(models.Model):
    """Class that enables a connection between two users."""
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.from_user} wants to befriend {self.to_user}.'


class LinearAlgebraExpression(models.Model):
    """Class for the main character of the backend system, namely, the linear
    algebra expression `exp` and the evaluated exp `eval_exp`"""
    exp = models.CharField(max_length=200)
    eval_exp = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=200)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'the evaluation of the linear algebra expression {self.exp} is {self.eval_exp}'

class BookStudy(models.Model):
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    members = models.ManyToManyField(User)
    name = models.CharField(max_length=500, unique=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'the {self.name} study group whose ownner is {self.owner.first_name}'
