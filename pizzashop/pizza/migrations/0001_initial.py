# Generated by Django 2.2.2 on 2019-06-10 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price_small', models.DecimalField(decimal_places=2, max_digits=8)),
                ('price_large', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaTopping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pizza.Pizza')),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping_type', models.CharField(max_length=60)),
                ('on_top_of', models.ManyToManyField(through='pizza.PizzaTopping', to='pizza.Pizza')),
            ],
        ),
        migrations.AddField(
            model_name='pizzatopping',
            name='topping',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pizza.Topping'),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(through='pizza.PizzaTopping', to='pizza.Topping'),
        ),
    ]
