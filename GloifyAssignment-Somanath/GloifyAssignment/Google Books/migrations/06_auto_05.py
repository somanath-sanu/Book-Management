
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('googlebooks', '0004_auto_20190811_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='books',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2019, 8, 11, 15, 35, 12, 334867, tzinfo=utc)),
            preserve_default=False,
        ),
    ]