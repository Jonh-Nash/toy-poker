from django.db import models

# ユーザー名、今のターン、得点、デッキ:
class UserInfo(models.Model):
    user = models.CharField(max_length=10)
    turn = models.IntegerField()
    tokuten = models.IntegerField()
    deck = models.CharField(max_length=100)
    bot_deck = models.CharField(max_length=200)

# ユーザー名、ポジション、カード、アクション、得点、ターン
class ActionHistory(models.Model):
    user = models.CharField(max_length=10)
    posi = models.CharField(max_length=10)
    card = models.CharField(max_length=1)
    action = models.CharField(max_length=10)
    tokuten = models.IntegerField()
    turn = models.IntegerField()
