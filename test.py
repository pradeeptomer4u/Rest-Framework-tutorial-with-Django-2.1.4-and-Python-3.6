import json

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from todos.models import Todo
from todos.todoserilizers import TodoSerializer


class TodoListCreateAPIViewTestCase(TestCase):
    url1 = reverse("todos:todo_create")
    def setUp(self):
        self.state = "done"
        self.due_date = "2018-09-20"
        self.todo_text = "I M Using Django 2.1"
        self.todo = Todo.objects.create(state=self.state, due_date=self.due_date,todo_text=self.todo_text)
        self.url = reverse("todos:todo_create")


    def test_create_todo(self):
        response = self.client.post(self.url, {"state": "done","due_date":"2018-09-20","todo_text":"I M Using Django 2.1"})

        self.assertEqual(201, response.status_code)



class TodoDetailAPIViewTestCase(TestCase):

    def setUp(self):
        self.state = "done"
        self.due_date = "2018-09-20"
        self.todo_text = "HI"
        self.todo = Todo.objects.create(state=self.state, due_date=self.due_date, todo_text=self.todo_text)
        self.url = reverse("todos:todo_list")
        self.url1 = reverse("todos:todo_update", kwargs={"pk": self.todo.pk})
        self.url2 = reverse("todos:delete_element", kwargs={"pk": self.todo.pk})



    def test_todo_object_bundle(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        todo_serializer_data = (TodoSerializer(instance=self.todo).data)
        response_data = json.loads(response.content)[0]
        self.assertEqual(todo_serializer_data, (response_data))

    def test_todo_object_update(self):
        response = self.client.put(self.url1, {"state":"in-progress","due_date":"2018-10-15","todo_text": "Call Dad!"},content_type='application/json')
        response_data = json.loads(response.content)
        todo = Todo.objects.get(id=self.todo.pk)
        self.assertEqual(response_data.get("todo_text"), todo.todo_text)

    def test_todo_object_delete(self):
        response = self.client.delete(self.url2)
        self.assertEqual(204, response.status_code)