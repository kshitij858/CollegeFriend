from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from .models import Professor, Course
from .serializer import ProfessorSerializer, CourseSerializer
from rest_framework.views import APIView
# Create your views here.

'''
class CoursesList(APIView):
    def get(self, request):
        courses = Courses.objects.all()
        serializer = CoursesSerializer(courses, many=True)
        return Response(serializer.data)
'''


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    #def get_queryset(self):
    #    querysetself.request.query_params.get('code')


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ProfessorList(generics.ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class ProfessorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
