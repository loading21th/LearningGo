# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-25 14:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import golearnApp.gomodels.BaseTable


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('abbreviation', models.CharField(max_length=10)),
                ('stage', models.CharField(max_length=40)),
                ('logo', models.ImageField(upload_to=golearnApp.gomodels.BaseTable.get_image_path)),
                ('bio', models.TextField()),
                ('pupose', models.TextField()),
                ('can_createclass', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('abbreviation', models.CharField(max_length=10)),
                ('teacher', models.CharField(max_length=40)),
                ('stage', models.IntegerField()),
                ('logo', models.ImageField(upload_to=golearnApp.gomodels.BaseTable.get_image_path)),
                ('bio', models.TextField()),
                ('time', models.TextField()),
                ('price', models.IntegerField()),
                ('rtmpaddr', models.CharField(max_length=40)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='golearnApp.Campus')),
            ],
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('homework', models.FileField(upload_to=golearnApp.gomodels.BaseTable.get_upfile_path)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='golearnApp.Campus')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='golearnApp.Classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Students_classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='golearnApp.Classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher_classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='golearnApp.Classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Ustudentinfo',
            fields=[
                ('id', models.IntegerField(default=golearnApp.gomodels.BaseTable.get_id, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('upasswd', models.CharField(max_length=40)),
                ('uemail', models.EmailField(max_length=40)),
                ('ubirth', models.DateField(max_length=40)),
                ('uimage', models.ImageField(upload_to=golearnApp.gomodels.BaseTable.get_image_path)),
                ('umoney', models.IntegerField()),
                ('usex', models.CharField(max_length=40)),
                ('can_upgrade', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Uteacherinfo',
            fields=[
                ('id', models.IntegerField(default=golearnApp.gomodels.BaseTable.get_id, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('upasswd', models.CharField(max_length=40)),
                ('uemail', models.EmailField(max_length=40)),
                ('ubirth', models.DateField(max_length=40)),
                ('uimage', models.ImageField(upload_to=golearnApp.gomodels.BaseTable.get_image_path)),
                ('umoney', models.IntegerField()),
                ('usex', models.CharField(max_length=40)),
                ('uGo_credential', models.ImageField(upload_to=golearnApp.gomodels.BaseTable.get_image_path)),
                ('uTeach_credential', models.ImageField(upload_to=golearnApp.gomodels.BaseTable.get_image_path)),
                ('udescripition', models.TextField()),
                ('can_createschool', models.BooleanField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.IntegerField()),
                ('name', models.CharField(max_length=40)),
                ('logo', models.ImageField(upload_to=golearnApp.gomodels.BaseTable.get_image_path)),
                ('addr', models.FileField(upload_to=golearnApp.gomodels.BaseTable.get_video_path)),
            ],
        ),
        migrations.AddField(
            model_name='teacher_classes',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='golearnApp.Uteacherinfo'),
        ),
        migrations.AddField(
            model_name='students_classes',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='golearnApp.Ustudentinfo'),
        ),
        migrations.AddField(
            model_name='campus',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='golearnApp.Uteacherinfo'),
        ),
    ]
