from django.contrib.auth.models import User
from django.db import models

class Friendship(models.Model):
    user = models.ForeignKey(User, related_name='%(class)s_user1', on_delete=models.CASCADE)
    friend = models.ForeignKey(User, related_name='%(class)s_player',  on_delete=models.CASCADE)

    status = models.CharField(max_length=10, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username + ' ' + self.friend.username + ' ' + self.status

    class Meta:
        unique_together = ('user', 'friend')
    
