# Generated by Django 4.2.2 on 2023-06-28 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plataforma', models.CharField(max_length=255)),
                ('taxa_plataforma', models.DecimalField(decimal_places=2, max_digits=8)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=255, unique=True)),
                ('limite_hospedes', models.IntegerField()),
                ('quantidade_banheiros', models.IntegerField()),
                ('aceita_animais', models.BooleanField()),
                ('valor_limpeza', models.DecimalField(decimal_places=2, max_digits=8)),
                ('data_ativacao', models.DateField(auto_now_add=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_reserva', models.CharField(max_length=255, unique=True)),
                ('data_checkin', models.DateField()),
                ('data_checkout', models.DateField()),
                ('preco_total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('comentario', models.TextField(blank=True)),
                ('numero_hospedes', models.IntegerField()),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('anuncio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sea_app.anuncio')),
            ],
        ),
        migrations.AddField(
            model_name='anuncio',
            name='imovel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sea_app.imovel'),
        ),
    ]
