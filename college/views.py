from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from .models import Professors, Courses
from .serializer import ProfessorSerializer, CoursesSerializer
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
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

    #def get_queryset(self):
    #    querysetself.request.query_params.get('code')



class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer


class ProfessorList(generics.ListCreateAPIView):
    queryset = Professors.objects.all()
    serializer_class = ProfessorSerializer


class ProfessorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professors.objects.all()
    serializer_class = ProfessorSerializer
