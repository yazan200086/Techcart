from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):


    def has_object_permission(self,request,view,obj):   # obj=user
        print('aaaa')
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.id==request.user.id
