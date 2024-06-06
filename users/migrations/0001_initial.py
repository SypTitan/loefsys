# Generated by Django 4.2.2 on 2024-06-06 15:16

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import localflavor.generic.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membership_type', models.CharField(choices=[('ACT', 'Active member'), ('PAS', 'Passive member'), ('ALM', 'Alumnus')], default='ACT', max_length=3, verbose_name='Membership type')),
                ('since', models.DateField(default=datetime.date.today, help_text="The date the member's membership started", verbose_name='Membership since')),
                ('until', models.DateField(blank=True, help_text="The date the member's membership stopped", null=True, verbose_name='Membership until')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=64, verbose_name='First name')),
                ('last_name', models.CharField(default='', max_length=64, verbose_name='Last name')),
                ('institution', models.CharField(blank=True, max_length=20, verbose_name='Educational institution')),
                ('programme', models.CharField(blank=True, max_length=20, verbose_name='Study programme')),
                ('student_number', models.CharField(blank=True, max_length=8, unique=True, validators=[django.core.validators.RegexValidator(message='Enter a valid student- or e/z/u-number.', regex='(s\\d{7}|[ezu]\\d{6,7})')], verbose_name='Student number')),
                ('RSC_number', models.CharField(blank=True, max_length=9, unique=True, verbose_name='RSC card number')),
                ('member_since', models.DateField()),
                ('member_until', models.DateField(blank=True, null=True)),
                ('alumni_since', models.DateField(blank=True, null=True)),
                ('payment_method', models.CharField(choices=[('IN', 'Collection')], max_length=2)),
                ('remark', models.TextField(blank=True, max_length=500)),
                ('address_street', models.CharField(max_length=100, null=True, validators=[django.core.validators.RegexValidator(message='please use the format <street> <number>', regex='^.+ \\d+.*')], verbose_name='Street and house number')),
                ('address_street2', models.CharField(blank=True, max_length=100, null=True, verbose_name='Second address line')),
                ('address_postal_code', models.CharField(max_length=10, null=True, verbose_name='Postal code')),
                ('address_city', models.CharField(max_length=40, null=True, verbose_name='City')),
                ('address_country', models.CharField(choices=[('AX', 'Åland Islands'), ('AL', 'Albania'), ('AD', 'Andorra'), ('AT', 'Austria'), ('BY', 'Belarus'), ('BE', 'Belgium'), ('BA', 'Bosnia and Herzegovina'), ('BG', 'Bulgaria'), ('HR', 'Croatia'), ('CZ', 'Czechia'), ('DK', 'Denmark'), ('EE', 'Estonia'), ('FO', 'Faroe Islands'), ('FI', 'Finland'), ('FR', 'France'), ('DE', 'Germany'), ('GI', 'Gibraltar'), ('GR', 'Greece'), ('GG', 'Guernsey'), ('VA', 'Vatican City'), ('HU', 'Hungary'), ('IS', 'Iceland'), ('IE', 'Ireland'), ('IM', 'Isle of Man'), ('IT', 'Italy'), ('JE', 'Jersey'), ('LV', 'Latvia'), ('LI', 'Liechtenstein'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('MK', 'Macedonia (FYROM)'), ('MT', 'Malta'), ('MD', 'Moldova'), ('MC', 'Monaco'), ('ME', 'Montenegro'), ('NL', 'Netherlands'), ('NO', 'Norway'), ('PL', 'Poland'), ('PT', 'Portugal'), ('RO', 'Romania'), ('RU', 'Russian Federation'), ('SM', 'San Marino'), ('RS', 'Serbia'), ('SK', 'Slovakia'), ('SI', 'Slovenia'), ('ES', 'Spain'), ('SJ', 'Svalbard and Jan Mayen'), ('SE', 'Sweden'), ('CH', 'Switzerland'), ('UA', 'Ukraine'), ('GB', 'United Kingdom')], max_length=2, null=True, verbose_name='Country')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('IBAN', localflavor.generic.models.IBANField(include_countries=None, max_length=34, use_nordea_extensions=False)),
                ('birthday', models.DateField(null=True, verbose_name='Birthday')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('U', 'Prefer not to say')], max_length=1)),
                ('receive_newsletter', models.BooleanField(default=True, help_text='Receive the Newsletter', verbose_name='Receive newsletter')),
                ('show_birthday', models.BooleanField(default=True, help_text='Show your birthday to other members on your profile page and in the birthday calendar', verbose_name='Display birthday')),
                ('profile_description', models.TextField(blank=True, help_text='Text to display on your profile', max_length=4096, verbose_name='Profile text')),
                ('initials', models.CharField(blank=True, max_length=20, null=True, verbose_name='Initials')),
                ('nickname', models.CharField(blank=True, max_length=30, null=True, verbose_name='Nickname')),
                ('display_name_preference', models.CharField(choices=[('full', 'Show full name'), ('nickname', 'Show only nickname'), ('firstname', 'Show only first name'), ('initials', 'Show initials and last name'), ('fullnick', 'Show name like "John \'nickname\' Doe"'), ('nicklast', 'Show nickname and last name')], default='full', max_length=10, verbose_name='How to display name')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
