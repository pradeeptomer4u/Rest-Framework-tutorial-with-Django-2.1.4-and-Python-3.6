from rest_framework import serializers, status, generics, mixins
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from todos.models import Todo , State

class TodoSerializer(serializers.Serializer):
    permission_classes = (AllowAny,)
    state = serializers.ChoiceField(choices=State)
    due_date = serializers.CharField(required=False)
    todo_text = serializers.CharField(required=False)
    def create(self, validated_data):
       data = Todo.objects.create(**validated_data)
       return data
    def update(self, instance, validated_data):
       instance.state = validated_data.get('state', instance.state)
       instance.due_date = validated_data.get('due_date', instance.due_date)
       instance.todo_text = validated_data.get('todo_text', instance.todo_text)
       instance.save()
       return instance

class TodoSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("state", "due_date", "todo_text")


