from django.test import TestCase
from .models import student_Data

class StudentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        student_Data.objects.create(name='Test Student', school='Test School', roll=123, contact=1234567890)

    def test_name_label(self):
        student = student_Data.objects.get(id=1)
        field_label = student._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_roll_max_length(self):
        student = student_Data.objects.get(id=1)
        max_length = student._meta.get_field('roll').max_length
        self.assertEqual(max_length, 10)

    def test_object_name_is_name(self):
        student = student_Data.objects.get(id=1)
        expected_object_name = f'{student.name}'
        self.assertEqual(expected_object_name, str(student))
