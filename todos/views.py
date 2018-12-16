from django.http import HttpResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import serializers, status, generics, mixins
from todos.models import Todo
from todos.todoserilizers import TodoSerializer1,TodoSerializer




class todoCreateView(generics.CreateAPIView):
    serializer_class = TodoSerializer

    @renderer_classes((JSONRenderer, HttpResponse))
    @api_view(["POST"])
    def create_todo(request):
        serializer = TodoSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            context = {"status": "success","record":"created",
                       }
            return Response(serializer.data,context)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

class todoDetailView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @renderer_classes((JSONRenderer, HttpResponse))
    @api_view(["GET"])
    def todo_details(request, pk):
        data = Todo.objects.get(id=pk)
        serializer = TodoSerializer(data)
        aa = HttpResponse(serializer.data, content_type='application/json')
        return Response(serializer.data)

class todoUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @renderer_classes((JSONRenderer, HttpResponse))
    @api_view(["GET", "PUT"])
    def todo_update(request, pk):
        query = Todo.objects.get(id=pk)
        if request.method == "PUT":
            serializer = TodoSerializer(query, data=request.data)
            if serializer.is_valid():
                serializer.save()
                aa = HttpResponse(serializer.data, content_type='application/json')
                return Response(serializer.data)
            else:
                return Response({"error": serializer.errors, "error": True})
        serializer = TodoSerializer(query)
        return Response(serializer.data)

class todoListView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @api_view(["GET"])
    def todo_list(request):
        query = Todo.objects.all()
        serializer = TodoSerializer(query, many=True)
        data = serializer.json()
        return Response(serializer.data)


    def get_queryset(self):
        queryset = Todo.objects.all()
        state = self.request.query_params.get('state', None)
        due_date = self.request.query_params.get('due_date', None)
        if state is not None:
            queryset = queryset.filter(state=state)
        if due_date is not None:
            queryset = queryset.filter(due_date=due_date)
        return queryset


@api_view(['DELETE'])
def delete_element(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
    except Todo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

