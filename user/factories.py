from django.contrib.auth.models import User

import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'user{}'.format(n))
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
