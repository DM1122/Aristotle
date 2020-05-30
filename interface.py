import os, sys
sys.path.append('./arsite')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arsite.settings')
import django
django.setup()
from library.models import Video, Tag

print(Video.objects.all())


API_KEY = 'AIzaSyBBn2qXrITsW3qGKi_Dyq_l2IJbESZnw60'