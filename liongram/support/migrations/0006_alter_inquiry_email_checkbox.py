# Generated by Django 4.0.3 on 2022-04-18 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0005_inquiry_datetimeofupload_inquiry_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='email_checkbox',
            field=models.BooleanField(verbose_name='문자메시지로 답변을 받겠습니다.'),
        ),
    ]
