# Generated by Django 4.1.1 on 2023-03-10 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.everestkitchenpa.com%2Fassets%2Fpages%2FcoldBeverages.html&psig=AOvVaw2Uw-kUBeKYMFdypbaXcxEB&ust=1678526361013000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCPj0yI6E0f0CFQAAAAAdAAAAABAE', max_length=500),
        ),
    ]