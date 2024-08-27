# Generated by Django 5.1 on 2024-08-27 13:33

import django.contrib.auth.models
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fabrica',
            fields=[
                ('id', models.AutoField(db_column='ID_Fabrica', primary_key=True, serialize=False, verbose_name='ID da Fábrica')),
                ('nome_fabrica', models.CharField(db_column='Nome_Fabrica', max_length=255, verbose_name='Nome da Fábrica')),
                ('endereco_fabrica', models.CharField(db_column='Endereço_Fabrica', max_length=255, verbose_name='Endereço Completo da Fábrica')),
                ('telefone_fabrica', models.CharField(db_column='Telefone_Fabrica', max_length=15, verbose_name='Número de Telefone da Fábrica')),
                ('email_fabrica', models.EmailField(db_column='Email_Fabrica', max_length=255, verbose_name='Endereço de Email da Fábrica')),
            ],
            options={
                'verbose_name': 'Fábrica',
                'verbose_name_plural': 'Fábricas',
                'db_table': 'fabrica',
                'ordering': ['nome_fabrica'],
            },
        ),
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('id', models.AutoField(db_column='D_Motorista', primary_key=True, serialize=False, verbose_name='ID do Motorista')),
                ('nome', models.CharField(db_column='Nome', max_length=255, verbose_name='Nome Completo')),
                ('cpf', models.CharField(db_column='CPF', max_length=50, unique=True, verbose_name='CPF')),
                ('cnh', models.CharField(db_column='CNH', max_length=50, verbose_name='Carteira Nacional de Habilitação')),
                ('data_nascimento', models.DateField(db_column='Data_Nascimento', verbose_name='Data de Nascimento')),
                ('endereco', models.CharField(db_column='Endereço', max_length=255, verbose_name='Endereço Completo')),
                ('telefone', models.CharField(db_column='Telefone', max_length=15, verbose_name='Número de Telefone')),
                ('email', models.EmailField(db_column='Email', max_length=255, verbose_name='Endereço de Email')),
            ],
            options={
                'verbose_name': 'Motorista',
                'verbose_name_plural': 'Motoristas',
                'db_table': 'motorista',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(db_column='tx_username', max_length=64, unique=True, verbose_name='Nome de Usuário')),
                ('password', models.CharField(db_column='tx_password', max_length=104, verbose_name='Senha')),
                ('name', models.CharField(blank=True, db_column='tx_name', max_length=256, null=True, verbose_name='Nome Completo')),
                ('email', models.CharField(blank=True, db_column='tx_email', max_length=256, null=True, verbose_name='E-mail')),
                ('last_login', models.DateTimeField(db_column='dt_last_login', null=True, verbose_name='Último Login')),
                ('is_active', models.BooleanField(db_column='cs_active', default=True, verbose_name='Ativo')),
                ('is_superuser', models.BooleanField(db_column='cs_superuser', default=False, verbose_name='Superusuário')),
                ('is_staff', models.BooleanField(db_column='cs_staff', default=False, verbose_name='Membro da Equipe')),
                ('is_default', models.BooleanField(db_column='cs_default', default=False, verbose_name='Padrão')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
                'db_table': 'auth_user',
                'ordering': ['username'],
                'managed': True,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
