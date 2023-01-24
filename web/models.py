from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Token(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    token=models.CharField(max_length=48)
    def __str__(self) :
        return "{}-token".format(self.user)

class Expense(models.Model):
    text=models.CharField(max_length=255,verbose_name="متن")
    date=models.DateTimeField(verbose_name="تاریخ")
    amount=models.BigIntegerField(verbose_name="مقدار")
    user=models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="کاربر")
    class Meta:
        verbose_name="خرج"
        verbose_name_plural="خرج ها"
        ordering=['date']
    def __str__(self):
        return "{}-{}".format(self.date,self.amount)
    
            
class Income(models.Model):
    text=models.CharField(max_length=255)
    date=models.DateTimeField()
    amount=models.BigIntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return "{}-{}".format(self.date,self.amount)
    class Meta:
        verbose_name="در آمد"
        verbose_name_plural="درآمدها"   
