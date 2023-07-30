from django.urls import path,include
from techcart import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()



#router.register('popularity',views.popularity,basename='popularity') 
router.register('get_cart',views.get_cart,basename='get_cart')
router.register('profile',views.UserProfileViewSets)
router.register('products',views.productViewset,basename='products')  
router.register('search',views.search,basename='search')
router.register('cat',views.catViewSet,basename='catViewSet')
router.register('orders',views.orderView,basename='orderView')

router.register('post_orders',views.orderPostView,basename='orderPostView')
router.register('favorite',views.favorite,basename='favorite')
router.register('postreview',views.reviewPost,basename='reviewPost')
router.register('get_review',views.get_review,basename='get_review')
router.register('post_cart',views.post_cart,basename='post_cart')
#router.register('collaborative',views.collaborative,basename='collaborative') 

urlpatterns=[

 path('login/',views.UserLogInApiView.as_view()),
 path('forget/',views.forget_passView.as_view()),
 path('changepass/',views.ChangePasswordView.as_view()),
 path('update_cart/',views.update_cart.as_view()),
 path('delete_cart/',views.delete_cart.as_view()),

 path('delete_from_cart/',views.delete_from_cart.as_view()),
 #path('set_up_finder/', views.get_answers_class.as_view()),

 path('',include(router.urls))




]



