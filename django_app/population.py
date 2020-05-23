from faker import Faker
import os, django
from sns.models import Message, Friend, Group, Good


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

fake = Faker('ja_JP')

for _ in range(10):
    print(fake.name())
