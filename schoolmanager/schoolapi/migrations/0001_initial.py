# Generated by Django 3.2.9 on 2021-11-23 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('section', models.CharField(max_length=50)),
                ('room', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('meeting_time', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('priority', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=50)),
                ('time_limit', models.CharField(max_length=50)),
                ('room', models.CharField(max_length=50)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolapi.class')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=50)),
                ('faculty', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=50)),
                ('program', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('priority', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=50)),
                ('no_questions', models.IntegerField(blank=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolapi.class')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initialBudget', models.FloatField()),
                ('income', models.FloatField()),
                ('tuition', models.FloatField()),
                ('equipment', models.CharField(blank=True, max_length=1000)),
                ('books', models.CharField(blank=True, max_length=1000)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='schoolapi.student')),
            ],
        ),
        migrations.CreateModel(
            name='ExamPrep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prep_type', models.CharField(choices=[('prac_exam', 'Practice Exam'), ('review_sess', 'Review Session'), ('prep_event', 'Exam Prep Event')], max_length=100)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolapi.exam')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('host', models.CharField(blank=True, max_length=50)),
                ('type', models.CharField(choices=[('Network', 'Networking'), ('InfoSess', 'Information Session'), ('Speaker', 'Career Fair'), ('Party', 'Party'), ('Workshop', 'Workshop'), ('Sports', 'Sports'), ('Conference', 'Conference'), ('Other', 'Other')], max_length=50)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolapi.club')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolapi.student')),
            ],
        ),
        migrations.AddField(
            model_name='club',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolapi.student'),
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('priority', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=50)),
                ('group_members', models.CharField(blank=True, max_length=1000)),
                ('module', models.CharField(blank=True, max_length=50)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolapi.class')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
