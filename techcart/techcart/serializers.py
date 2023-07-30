from rest_framework import serializers
from techcart import models
from rest_framework.serializers import ValidationError


class orderSer(serializers.ModelSerializer):
    class Meta:
        model=models.order
        #fields='__all__'
        exclude = ('user',)
        depth=2






class orderPostSer(serializers.ModelSerializer):
    class Meta:
        model=models.order
        fields='__all__'






class favoriteSer(serializers.ModelSerializer):
    class Meta:
        model=models.favorite
        fields='__all__'




class reviews_Ser(serializers.ModelSerializer):
    class Meta:
        model=models.reviews
        fields='__all__'
    def validate(self,data):
        product_ob=data['product']
        user=data['user']
        qs1=models.reviews.objects.filter(user=user)
        if qs1.exists():
            qs2=qs1.filter(product=product_ob)
            if qs2.exists():
                raise ValidationError('you Already have a comment')
        return data






class UserProfileSer(serializers.ModelSerializer):
    '''serializer a user profile object'''
    orders = orderSer(many=True,read_only=True)
    class Meta:      #point the serializer to a model
        model=models.UserProfile
        fields=['id','email','name','date_of_birth','photo','orders','password']
        extra_kwargs={
        'password':{
        'write_only': True,
        'style':{                               #not show the password
        'input_type':'password'
        }
        }
        }

    def create(self,validated_data):
        '''create and return new user'''


        user=models.UserProfile.objects.create_user(
        email=validated_data['email'],
        name=validated_data['name'],
        date_of_birth=validated_data['date_of_birth'],
        photo=validated_data['photo'],
        password=validated_data['password'],


        )
        return user



class get_review(serializers.ModelSerializer):
    class Meta:
        model=models.reviews
        fields= '__all__'
        depth=1





class productSer(serializers.ModelSerializer):
    class Meta:
        model=models.product
        fields= '__all__'
        depth=2







class search(serializers.Serializer):
    name=serializers.CharField(max_length=20)



class Forget_pass(serializers.ModelSerializer):
    class Meta:
        model=models.forget
        fields='__all__'








class catSer(serializers.ModelSerializer):
    class Meta:
        model=models.catiegorys
        fields='__all__'
        depth=1




class ChangePasswordSerializer(serializers.Serializer):
    model = models.UserProfile

    """
    Serializer for password change endpoint.
    """
    new_password = serializers.CharField(required=True)


#
# class tokenSer(serializers.ModelSerializer):
#     class Meta:
#         model=models.token
#         fields='__all__'
#         depth=1




class cartSer(serializers.ModelSerializer):
    class Meta:
        model=models.cart
        fields='__all__'
        







class get_cartSer(serializers.ModelSerializer):
    class Meta:
        model=models.cart
        #fields= '__all__'
        exclude = ('user',)
        depth=1
