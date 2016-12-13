from django.db  import model

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField()
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now =True)

class Message(models.Model):
    message = models.TextField()
    user_id = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
    comment = TextField()
    message_id = models.ForeignKey(Message)
    user_id = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


# SOLUTION
# class User(models.Model):
#       first_name = models.CharField(max_length=200)
#       last_name = models.CharField(max_length=200)
#       email = models.EmailField()
#       password = models.CharField(max_length=200)
#       created_at = models.DateTimeField(auto_now_add=True)
#       updated_at = models.DateTimeField(auto_now=True)
#
#
#   class Message(models.Model):
#       message = models.TextField()
#       user = models.ForeignKey(User)
#       created_at = models.DateTimeField(auto_now_add=True)
#       updated_at = models.DateTimeField(auto_now=True)
#
#   class Comment(models.Model):
#       comment = models.TextField()
#       user = models.ForeignKey(User)
#       message = models.ForeignKey(Message)
#       created_at = models.DateTimeField(auto_now_add=True)
#       updated_at = models.DateTimeField(auto_now=True)
