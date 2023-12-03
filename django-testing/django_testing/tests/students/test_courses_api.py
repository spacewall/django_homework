import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student

@pytest.fixture
def client() -> APIClient:
    return APIClient()

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    
    return factory

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    
    return factory

@pytest.mark.django_db
def test_get_first_course(client: APIClient, course_factory):
    # Arrange
    course = course_factory()

    # Act
    response = client.get('/api/v1/courses/')

    # Assert
    response_data = response.json()
    assert response.status_code == 200
    assert response_data[0]['id'] == course.id

@pytest.mark.django_db
def test_get_courses_list(client: APIClient, course_factory):
    # Arrange
    courses = course_factory(_quantity=12)
    
    # Act
    response = client.get('/api/v1/courses/')

    # Assert
    assert response.status_code == 200
    for number, course in enumerate(response.json()):
        assert course['id'] == courses[number].id

@pytest.mark.django_db
def test_course_id_filtration(client: APIClient, course_factory):
    # Arrange
    course = course_factory()
    
    # Act
    response = client.get(f'/api/v1/courses/?id={course.id}')

    # Assert
    assert response.status_code == 200
    assert response.json()[0]['id'] == course.id

@pytest.mark.django_db
def test_course_name_filtration(client: APIClient, course_factory):
    # Arrange
    course = course_factory()

    # Act
    response = client.get(f'/api/v1/courses/?name={course.name}')

    # Assert
    assert response.status_code == 200
    assert response.json()[0]['name'] == course.name

@pytest.mark.django_db
def test_course_creation(client: APIClient):
    # Arrange
    data = {'name': 'test'}

    # Act
    response = client.post('/api/v1/courses/', data=data)

    # Assert
    assert response.status_code == 201

@pytest.mark.django_db
def test_course_updation(client: APIClient, course_factory):
    # Arrange
    course = course_factory()
    data = {'name': 'test'}

    # Act
    response = client.patch(f'/api/v1/courses/{course.id}/', data=data)

    # Assert
    assert response.status_code == 200

@pytest.mark.django_db
def test_course_destroying(client: APIClient, course_factory):
    # Arrange
    course = course_factory()

    # Act
    response = client.delete(f'/api/v1/courses/{course.id}/')

    # Assert
    assert response.status_code == 204
