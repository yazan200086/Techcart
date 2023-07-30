from contextlib import _RedirectStream
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken  #pre-def login ApiView
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated,AllowAny    # or use IsAuthenticated to prevent no auth to show even the object
from techcart.serializers import get_cartSer,  cartSer,get_review , reviews_Ser , productSer , UserProfileSer,search,Forget_pass,catSer,orderSer,ChangePasswordSerializer,orderPostSer,favoriteSer
from techcart import models
from rest_framework.authentication import TokenAuthentication   #gen a token(type of authentication) when the user login and send it with each request to the api to auth the user with the api
from techcart import permissions 
from .models import product
import smtplib
import random
from rest_framework.authtoken.models import Token
# from techcart import pop
# from techcart import collaborative as co
from django.http.response import JsonResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.shortcuts import render
# from experta import *
from django.views import View
import time 
from threading import Event, Thread
# from . import project_final as ps
from django.http import HttpResponse





class UserProfileViewSets(viewsets.ModelViewSet):  #ViewSet to manage a model
     '''handle createing and update user '''
     serializer_class=UserProfileSer
     queryset=models.UserProfile.objects.all()
    #  authentication_classes=(TokenAuthentication,)
    #  permission_classes=(permissions.UpdateOwnProfile,)




'''-------------------------------------------------------'''

    

    
class UserLogInApiView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'name':user.name,
            'date of birth':user.date_of_birth
                    })
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES     #to make it visual in the browser








class productViewset(viewsets.ModelViewSet):
    serializer_class=productSer
    def get_queryset(self):
        p=models.product.objects.all()
       
        return p



# class popularity(viewsets.ModelViewSet):
#     serializer_class=productSer
#     def get_queryset(self):
#         q=models.product.objects.all()
#         user_id = self.request.query_params.get('user_id')
#         p1=pop.recommend_pop(user_id)['product_id'].values[0]
#         p2=pop.recommend_pop(user_id)['product_id'].values[1]
#         p3=pop.recommend_pop(user_id)['product_id'].values[2]
#         p4=pop.recommend_pop(user_id)['product_id'].values[3]
#         p5=pop.recommend_pop(user_id)['product_id'].values[4]

#         q=models.product.objects.filter(pk__in=[p1, p2, p3, p4, p5])
#         return q





# class collaborative(viewsets.ModelViewSet):
#     serializer_class=productSer
#     def get_queryset(self):
#         p=models.product.objects.all()
#         user_id = self.request.query_params.get('user_id')
#         p1=co.recommend_items(user_id,co.pivot_df,co.preds_df)[0]
#         p2=co.recommend_items(user_id,co.pivot_df,co.preds_df)[1]
#         p3=co.recommend_items(user_id,co.pivot_df,co.preds_df)[2]
#         p4=co.recommend_items(user_id,co.pivot_df,co.preds_df)[3]
#         p5=co.recommend_items(user_id,co.pivot_df,co.preds_df)[4]
        
#         p=models.product.objects.filter(pk__in=[p1, p2, p3, p4, p5])
#         return p













class reviewPost(viewsets.ModelViewSet):
    serializer_class=reviews_Ser
    # permission_classes = (IsAuthenticated,)
    # authentication_classes=(TokenAuthentication,)
    def get_queryset(self):
        queryset=models.reviews.objects.all()
        product__id = self.request.query_params.get('product')
        if product__id is not None:
             queryset = queryset.filter(product=product__id)
         #lookup_field = 'product__id'
        return queryset


class search(viewsets.ModelViewSet):
    serializer_class=productSer

    queryset=models.product.objects.all()
    filter_backends=(filters.SearchFilter,)


    search_fields=('name',)


class catViewSet(viewsets.ModelViewSet):
    serializer_class=catSer
    def get_queryset(self):
        cat=models.catiegorys.objects.all()
        return cat



class orderView(viewsets.ModelViewSet):
    serializer_class=orderSer
    permission_classes = (IsAuthenticated,)
    authentication_classes=(TokenAuthentication,)
    def get_queryset(self):
        user = self.request.user
        return models.order.objects.filter(user=user)





class forget_passView(APIView):
    serializer_class=Forget_pass
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email=serializer.validated_data.get('email')
            code = random.randrange(1000, 100000, 5)
            sent_code=f'{code}'
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login('techcartsy@gmail.com','aqvqrwltvxmohhmz' )
            server.sendmail('techcartsy@gmail.com', email, sent_code)
            return Response({'code':code})

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)











class ChangePasswordView(generics.UpdateAPIView):

        serializer_class = ChangePasswordSerializer
        model = models.UserProfile
        permission_classes = (AllowAny,)

        def update(self, request, *args, **kwargs):
            object_id = request.query_params['email']
            user=models.UserProfile.objects.get(email=object_id)

            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # set_password also hashes the password that the user will get
                user.set_password(serializer.data.get("new_password"))
                user.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class catViewSet(viewsets.ModelViewSet):
    serializer_class=catSer
    def get_queryset(self):
        cat=models.catiegorys.objects.all()
        return cat






#
# class tokenView(generics.ListCreateAPIView):
#     serializer_class = tokenSer
#     def get_queryset(self):
#         token=models.token.objects.all()
#         return token
#






class orderPostView(viewsets.ModelViewSet):
    serializer_class=orderPostSer
    permission_classes = (IsAuthenticated,)
    authentication_classes=(TokenAuthentication,)
    def get_queryset(self):
        o=models.order.objects.all()
        return o





class favorite(viewsets.ModelViewSet):
    serializer_class=favoriteSer
    permission_classes = (IsAuthenticated,)
    authentication_classes=(TokenAuthentication,)
    def get_queryset(self):
        user = self.request.user
        return models.favorite.objects.filter(user=user)






class get_review(viewsets.ModelViewSet):
    serializer_class=get_review
 
    def get_queryset(self):
        queryset=models.reviews.objects.all()
        product__id = self.request.query_params.get('product')
        if product__id is not None:
             queryset = queryset.filter(product__id=product__id)
         #lookup_field = 'product__id'
        return queryset








class post_cart(viewsets.ModelViewSet):
    serializer_class=cartSer
    permission_classes = (IsAuthenticated,)
    authentication_classes=(TokenAuthentication,)
    def get_queryset(self):
        user = self.request.user
        return models.cart.objects.filter(user=user)
    


        

 

        






class get_cart(viewsets.ModelViewSet):
    serializer_class=get_cartSer
    permission_classes = (IsAuthenticated,)
    authentication_classes=(TokenAuthentication,)
    def get_queryset(self):
        user = self.request.user

        
        return models.cart.objects.filter(user=user,is_deleted=False)



 


class update_cart(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes=(TokenAuthentication,)
    def post(self, request, *args, **kwargs):
        #pro_id=int(request.POST.get('product_id'))
        cart_id=request.POST.get('cart_id')
        user = self.request.user
        if (models.cart.objects.filter(id=cart_id,user=user)):
            q=request.POST.get('quantity')
            c=models.cart.objects.get(id=cart_id,user=user)
            c.quantity=q
            c.save()
            return JsonResponse ({"status":'updated successfully'})
        else:
            return JsonResponse ({"status":'invalid product ID'})
            



class delete_cart(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes=(TokenAuthentication,)
    def post(self, request, *args, **kwargs):
        #pro_id=int(request.POST.get('product_id'))
        cart_id=request.POST.get('cart_id')

        user = self.request.user
        c=models.cart.objects.all()
        if (models.cart.objects.filter(user=user,id=cart_id)):
            c=models.cart.objects.get(user=user,id=cart_id)
            c.is_deleted=True
            c.save()
            
    
            
            return JsonResponse ({"status":'deleted successfully'})
        else:
            return JsonResponse ({"status":'invalid product ID'})







class delete_from_cart(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes=(TokenAuthentication,)
    def post(self, request, *args, **kwargs):
        #pro_id=int(request.POST.get('product_id'))
        cart_id=request.POST.get('cart_id')
        user = self.request.user
        c=models.cart.objects.all()
        if (models.cart.objects.filter(user=user,id=cart_id)):
            c=models.cart.objects.get(user=user,id=cart_id)
            c.delete()
            return JsonResponse ({"status":'deleted successfully'})
        else:
            return JsonResponse ({"status":'invalid  ID'})
            







# global expert_engine 
# expert_engine = None    

# global thread   



# class get_answers_class(View):
#     def get(self, request):
#         global expert_engine
#         global thread 
#         if expert_engine != None:
#              ps.user_answer="terminate"  
#              thread.join()  
#         thread = Thread(target=experta)
#         thread.start() 
#         time.sleep(500/1000)
#         return render(request,'setup_finder_UI/ui.html', {'qustion':ps.qustion, 'answers':ps.answers,  'range':range(len(ps.answers))}) 
    
#     def post(self, request):
#         ps.user_answer = request.POST.get('user_answer')
#         print(ps.user_answer)
#         time.sleep(500/1000)
#         if ps.output != '':
#             if type(ps.output) is  dict:
#                 print(ps.output)
#                 return render(request,'setup_finder_UI/sites.html', {'output':ps.output})
            
#             elif ' ' in ps.output:
#                 return render(request,'setup_finder_UI/string.html', {'output':ps.output})
#             else:
#                 return render(request,'setup_finder_UI/output.html', {'output':ps.output})
            

#         return render(request,'setup_finder_UI/ui.html', {'qustion':ps.qustion, 'answers':ps.answers, 'range':range(len(ps.answers)) }) 
    
    
# def experta():
#     print('experta started')
#     ps.output = ''
#     global expert_engine       
#     expert_engine = ps.Project()
#     expert_engine.reset()
#     expert_engine.run()
#     expert_engine = None
#     print('experta terminated')
