# Generated by Django 3.2.3 on 2021-05-21 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rightsandobligations'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProceduresOneWindow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('ProceduresOneWindow_doc', models.FileField(upload_to='ProceduresOneWindow/')),
                ('times', models.DateField()),
            ],
        ),
    ]
