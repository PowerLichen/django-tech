import factory
from django.contrib.auth import get_user_model

from api.testcode.models import Notice

UserModel = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserModel
        django_get_or_create = ("username", )

    username = factory.Faker("user_name")
    password = factory.Faker("password")


class NoticeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Notice
    
    user = factory.SubFactory(UserFactory)
    title = factory.Faker("sentence")
    context = factory.Faker("text", max_nb_chars=20)
