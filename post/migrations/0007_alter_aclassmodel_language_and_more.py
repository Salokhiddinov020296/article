# Generated by Django 4.1 on 2022-11-02 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_aclassmodel_cyberleninka_aclassmodel_google_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aclassmodel',
            name='language',
            field=models.CharField(choices=[("o'zbekcha", "o'zbekcha"), ('ruscha', 'ruscha'), ('inglizcha', 'inglizcha')], max_length=10, verbose_name='Qaysi tilda yozilgan'),
        ),
        migrations.AlterField(
            model_name='bclassmodel',
            name='language',
            field=models.CharField(choices=[("o'zbekcha", "o'zbekcha"), ('ruscha', 'ruscha'), ('inglizcha', 'inglizcha')], max_length=10, verbose_name='Qaysi tilda yozilgan'),
        ),
        migrations.AlterField(
            model_name='cclassmodel',
            name='language',
            field=models.CharField(choices=[("o'zbekcha", "o'zbekcha"), ('ruscha', 'ruscha'), ('inglizcha', 'inglizcha')], max_length=10, verbose_name='Qaysi tilda yozilgan'),
        ),
        migrations.AlterField(
            model_name='dclassmodel',
            name='language',
            field=models.CharField(choices=[("o'zbekcha", "o'zbekcha"), ('ruscha', 'ruscha'), ('inglizcha', 'inglizcha')], max_length=10, verbose_name='Qaysi tilda yozilgan'),
        ),
    ]
