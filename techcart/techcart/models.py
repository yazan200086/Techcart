from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from django.core.validators import *



def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)





class UserProfileManger(BaseUserManager):
    '''manger for the next class'''
    def create_user(self,email,name,date_of_birth,photo,password=None):
        if not email:
            raise ValueError ('user must have email')
        email =self.normalize_email(email)
        user=self.model(email=email,name=name,date_of_birth=date_of_birth,photo=photo)
        user.set_password(password)   #Good practice not field in the DB
        user.save(using=self._db)
        return user

    def create_superuser(self,email,name,date_of_birth,photo,password):
        user=self.create_user(email,name,date_of_birth,photo,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self.db)
        return user





class UserProfile(AbstractBaseUser,PermissionsMixin):
    """model database for user"""
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    date_of_birth = models.DateField()
    photo=models.ImageField(upload_to=upload_to,null=True,blank=True)


    objects=UserProfileManger()



    USERNAME_FIELD='email'
    REQUIRED_FIELDS =['name','date_of_birth','photo']

    def __str__(self):
        return f'{self.email}     ID={self.id}'





class reviews(models.Model):

    rating=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True)
    # product=models.ManyToManyField(
    #     'product',
    #     # on_delete=models.CASCADE,
    #     related_name='review',
    #     blank=False,
    #     #null=True,
    #     unique=False,
    # )
    product=models.ForeignKey('product',on_delete=models.CASCADE,null=True)



    def __str__(self):
        return f'({self.rating}) {self.user}'





class product(models.Model):
    name=models.CharField(max_length=20)
    catiegory=models.CharField(max_length=20)
    details=models.TextField()
    is_bestselling=models.BooleanField(default=False)
    #reviews=models.ManyToManyField(reviews,blank=True, related_name='reviews')
    #favorite_users=models.ManyToManyField(UserProfile,blank=True,related_name='favorite_users')
    photo=models.ImageField(upload_to=upload_to,null=True,blank=True)
    #users=models.ManyToManyField(UserProfile,blank=True)
    price = models.FloatField(null=True,blank=True)
    Ram=models.CharField(max_length=25,null=True,blank=True)
    Capacity=models.CharField(max_length=25,null=True,blank=True)

    def __str__(self):
        return f'({self.name})__{self.id}'


    def get_id(self):
        return self.id




class forget(models.Model):
    email=models.EmailField()



class catiegorys(models.Model):
    name=models.CharField(max_length=20)
    products=models.ManyToManyField(product,blank=True)

    def __str__(self):
        return self.name


class order(models.Model):
    delivery_option=models.TextField(null=True)
    payment_method=models.TextField(null=True)
    address=models.TextField(null=True)
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True)
    cart=models.ManyToManyField('cart')
    total_price=models.IntegerField(null=True)

    def __str__(self):
        return f'({self.id}) {self.user}'

#
# class token(models.Model):
#     user=models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True,blank=True)
#     token=models.CharField(max_length=100,null=True,blank=True)
#
#     def __str__(self):
#         return self.user.email



class favorite(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True,blank=True)
    products=models.ManyToManyField(product,blank=True)


    def __str__(self):
        return f'({self.id}) {self.user}'



class cart(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE,null=True,)
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True)
    #delivery_option=models.TextField(null=True)
    # payment_method=models.TextField(null=True)
    # address=models.TextField(null=True)
    quantity=models.IntegerField(null=True)
    is_deleted=models.BooleanField(default=False)
    





