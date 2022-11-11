# Generated by Django 4.1 on 2022-11-12 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_aclassmodel_article_pdf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aclassmodel',
            name='author1',
            field=models.CharField(max_length=60, verbose_name='Muallif(1)'),
        ),
        migrations.AlterField(
            model_name='aclassmodel',
            name='author2',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Muallif(2)'),
        ),
        migrations.AlterField(
            model_name='aclassmodel',
            name='author3',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Muallif(3)'),
        ),
        migrations.AlterField(
            model_name='aclassmodel',
            name='author4',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Muallif(4)'),
        ),
        migrations.AlterField(
            model_name='bclassmodel',
            name='author1',
            field=models.CharField(max_length=60, verbose_name='Muallif(1)'),
        ),
        migrations.AlterField(
            model_name='bclassmodel',
            name='author2',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Muallif(2)'),
        ),
        migrations.AlterField(
            model_name='bclassmodel',
            name='author3',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Muallif(3)'),
        ),
        migrations.AlterField(
            model_name='bclassmodel',
            name='author4',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Muallif(4)'),
        ),
        migrations.AlterField(
            model_name='cclassmodel',
            name='author1',
            field=models.CharField(max_length=60, verbose_name='Muallif(1)'),
        ),
        migrations.AlterField(
            model_name='cclassmodel',
            name='author2',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Muallif(2)'),
        ),
        migrations.AlterField(
            model_name='cclassmodel',
            name='author3',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Muallif(3)'),
        ),
        migrations.AlterField(
            model_name='cclassmodel',
            name='author4',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Muallif(4)'),
        ),
        migrations.AlterField(
            model_name='dclassmodel',
            name='author1',
            field=models.CharField(max_length=60, verbose_name='Muallif(1)'),
        ),
        migrations.AlterField(
            model_name='dclassmodel',
            name='author2',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Muallif(2)'),
        ),
        migrations.AlterField(
            model_name='dclassmodel',
            name='author3',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Muallif(3)'),
        ),
        migrations.AlterField(
            model_name='dclassmodel',
            name='author4',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Muallif(4)'),
        ),
    ]
