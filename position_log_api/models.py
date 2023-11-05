from django.db import models
import uuid
from django.contrib.auth.models import User


class UserType(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class Position(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class CustomUser(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + " : " + self.position.title


class Session(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True)
    users = models.JSONField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.users) + " : " + self.position.title


class CheckIn(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True)
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE)
    date = models.DateTimeField()


class CheckOut(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True)
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE)
    date = models.DateTimeField()
