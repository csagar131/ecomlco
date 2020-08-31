from django.db import migrations
from api.user.models import User


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = User(name ='sagar',
        email = 'chouhansagar131@gmail.com',
        is_staff = True,
        is_superuser = True,
        )
        user.set_password('12345')
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
