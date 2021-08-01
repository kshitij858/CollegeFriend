from rest_framework import serializers, generics
from .models import Professor, Course


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'


class ProfessorSerializerForCourse(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['id']


class CourseSerializer(serializers.ModelSerializer):
    #professors = ProfessorSerializerForCourse(many=True, read_only=True)

    def save(self, **kwargs):
        data = self.validated_data
        # pylint: disable=no-member
        course = Course.objects.create(
            id=data['id'], name=data['name'], code=data['code']
        )
        course.professors.set(data.get('professors', []))
        return course

    class Meta:
        model = Course
        fields = '__all__'

