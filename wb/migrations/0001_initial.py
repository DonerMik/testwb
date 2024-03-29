from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.IntegerField()),
                ('brand', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'brand_data',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='upload')),
                ('date_upload', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-date_upload',),
            },
        ),
    ]
