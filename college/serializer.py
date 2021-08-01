from rest_framework import serializers, generics
from .models import Professors, Courses


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professors
        fields = '__all__'


class ProfessorSerializerForCourse(serializers.ModelSerializer):
    class Meta:
        model = Professors
        fields = ['id']


class CoursesSerializer(serializers.ModelSerializer):
    #professors = ProfessorSerializerForCourse(many=True, read_only=True)

    def save(self, **kwargs):
        data = self.validated_data
        # pylint: disable=no-member
        course = Courses.objects.create(
            id=data['id'], name=data['name'], code=data['code']
        )
        course.professors.set(data.get('professors', []))
        return course

    class Meta:
        model = Courses
        fields = '__all__'

