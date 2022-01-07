from rest_framework import serializers
from .models import *


"""
TODO:
Create the appropriate Serializer class(es) for implementing
Todo GET (List and Detail), PUT, PATCH and DELETE.
"""


class TodoCreateSerializer(serializers.ModelSerializer):

    

    '''def save(self, **kwargs):
        data = self.validated_data
        user = self.context['request'].user
        title = data['title']
        todo = Todo.objects.create(creator=user, title=title)
        return todo'''
    def create(self, validated_data): 

         data = self.validated_data
         user=self.context['request'].user
         title = data['title']
         todo = Todo.objects.create(creator=user, title=title)
         return todo

        

    
    class Meta:
        model = Todo
        fields = ('id', 'title',)



class TodoLISTSerializer(serializers.ModelSerializer):

    class Meta:
        model= Todo
        fields = ('id', 'title')


class addcontriserializer(serializers.ModelSerializer):


    
    def save(self, **kwargs):
        user = self.context['user']
        todo = self.context['todo']
        contri = contributer.objects.create(contributeing_user=user,todo=todo)
        return contri

    ''' def create(self, validated_data):
        user = self.context['user']
        todo = self.context['todo']
        print(user)
        print(todo)
        contri = contributer.objects.create(contributeing_user=user,todo=todo)
        return contri
    '''
    class Meta:
        model = contributer
        fields=('contributeing_user','todo')
        extra_kwargs = {
            'todo': {'required': False},
            'contributeing_user': {'required': False}
        }

    
        
