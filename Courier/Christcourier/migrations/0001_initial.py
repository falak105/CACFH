# Generated by Django 5.0.1 on 2024-02-05 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New_admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_name', models.CharField(max_length=200)),
                ('a_email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='New_staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=200)),
                ('s_email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='New_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('reg_no', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='P_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rec_id', models.CharField(max_length=50)),
                ('rec_email', models.CharField(max_length=200)),
                ('rec_name', models.CharField(max_length=200)),
                ('rec_phone', models.CharField(max_length=200)),
                ('reg_date', models.DateField()),
                ('rec_company', models.CharField(choices=[('amazon', 'amazon'), ('flipkart', 'flipkart'), ('myntra', 'myntra'), ('nykaa', 'nykaa'), ('meesho', 'meesho'), ('others', 'others')], max_length=200)),
            ],
        ),
    ]
