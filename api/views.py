from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from .models import Todo
from django.shortcuts import get_object_or_404


# knoww more about request and response 



"""
TODO:
Create the appropriate View classes for implementing
Todo GET (List and Detail), PUT, PATCH and DELETE.
"""

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user

class Iscontributor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
         if obj.creator == request.user:
             return True
         obj_new=contributer.objects.filter(contributeing_user=request.user,todo=obj)
         if obj_new.count():
             return True
         else:
            return False
        
        

        

     



class TodoCreateView(generics.GenericAPIView):

    permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadOnly)
    serializer_class = TodoCreateSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data,context={'request': request})
        print(serializer)
        serializer.is_valid(raise_exception=True)
        x=serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
        y=self.get_serializer(x)
        return Response(y.data,status=status.HTTP_200_OK)


class Todolistview(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = TodoLISTSerializer

    def get(self, request):
        x=Todo.objects.filter(creator=request.user)
        serializer=self.get_serializer(x,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TododetailView(generics.GenericAPIView):
     permission_classes = (permissions.IsAuthenticated,Iscontributor)
     serializer_class = TodoLISTSerializer
     def get(self, request,id,format=None):
        todo=get_object_or_404(Todo,id=id)
        serializer=self.get_serializer(todo)
        return Response(serializer.data,status=status.HTTP_200_OK)


     def put(self, request, id, format=None):
         todo=get_object_or_404(Todo,id=id)
         self.check_object_permissions(request,todo)
         serializer=self.get_serializer(todo,data={'title': request.data['title']}, partial=True)
         serializer.is_valid(raise_exception=True)
         x=serializer.save()
         return Response(serializer.data,status=status.HTTP_200_OK)

     def delete(self, request, id, format=None):
         
         todo=get_object_or_404(Todo,id=id)
         self.check_object_permissions(request,todo)
         todo.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)

class addcontributorsview(generics.GenericAPIView):

     permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
     serializer_class = addcontriserializer

     def post(self, request,id,format=None):
         todo=get_object_or_404(Todo,id=id)
         self.check_object_permissions(request,todo)
         data=request.data
         obj=get_object_or_404(User,id=request.data['user'])
         print(obj)
         obj_new=contributer.objects.filter(contributeing_user=obj,todo=todo)
         if obj_new.count():
              return Response({'contri': 'this user is aleardy a contributer in this todo'},status=status.HTTP_204_NO_CONTENT)

         serializer=self.get_serializer(data=request.data,context={'user':obj,'todo':todo})
         serializer.is_valid(raise_exception=True)
         y=serializer.save()
         x=self.get_serializer(y)
         return Response(x.data,status=status.HTTP_200_OK)

class delcontributorsview(generics.GenericAPIView):
     permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

     def post(self, request,id,format =None):
         todo=get_object_or_404(Todo,id=id)
         self.check_object_permissions(request,todo)
         data=request.data
         obj=get_object_or_404(User,id=request.data['user'])
         obj_new=contributer.objects.filter(contributeing_user=obj,todo=todo)
         if obj_new.count():
             x=obj_new[0]
             x.delete()
             return Response({'contri': 'sucessfully deleted '},status=status.HTTP_200_OK)
         else:
             return Response({'contri': 'notexist'},status=status.HTTP_204_NO_CONTENT)

class listofcontributers(generics.GenericAPIView):
     permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
     serializer_class = addcontriserializer

     def get(self, request, id, format=None):
           todo=get_object_or_404(Todo,id=id)
           self.check_object_permissions(request,todo)
           obj_contri=contributer.objects.filter(todo=todo)
           if obj_contri.count():
               serializer=self.get_serializer(obj_contri,many=True)
               return Response(serializer.data,status=status.HTTP_200_OK)
           else:
                return Response({'contri':'no contributer of this todo, lets create a new one'},status=status.HTTP_204_NO_CONTENT)


















   
         



