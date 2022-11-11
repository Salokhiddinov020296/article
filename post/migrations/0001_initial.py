# Generated by Django 4.1.1 on 2022-11-12 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AFieldModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name="yo'nalishi")),
            ],
            options={
                'verbose_name': "A seriya Yo'nalishi",
                'verbose_name_plural': "A seriya Yo'nalishi",
            },
        ),
        migrations.CreateModel(
            name='BFieldModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name="yo'nalishi")),
            ],
            options={
                'verbose_name': "B seriya Yo'nalishi",
                'verbose_name_plural': "B seriya Yo'nalishi",
            },
        ),
        migrations.CreateModel(
            name='CFieldModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name="yo'nalishi")),
            ],
            options={
                'verbose_name': "C seriya Yo'nalishi",
                'verbose_name_plural': "C seriya Yo'nalishi",
            },
        ),
        migrations.CreateModel(
            name='DFieldModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name="yo'nalishi")),
            ],
            options={
                'verbose_name': "D seriya Yo'nalishi",
                'verbose_name_plural': "D seriya Yo'nalishi",
            },
        ),
        migrations.CreateModel(
            name='PropagandistModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name="Targ'ibotchi")),
            ],
            options={
                'verbose_name': "Targ'ibotchi",
                'verbose_name_plural': "Targ'ibotchilar",
            },
        ),
        migrations.CreateModel(
            name='WhichLanguageWriteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Qaysi tilda yozilgan')),
            ],
            options={
                'verbose_name': 'Yozilgan tili tanlsh',
                'verbose_name_plural': 'Yozilgan tili tanlash',
            },
        ),
        migrations.CreateModel(
            name='DclassModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.PositiveSmallIntegerField()),
                ('issue', models.PositiveSmallIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('language', models.CharField(choices=[("o'zbekcha", "o'zbekcha"), ('ruscha', 'ruscha'), ('inglizcha', 'inglizcha')], max_length=10, verbose_name='Qaysi tilda yozilgan')),
                ('pages', models.CharField(max_length=255, verbose_name='Sahifalar')),
                ('article_pdf', models.FileField(blank=True, null=True, upload_to='article/', verbose_name='Maqola (pdf)')),
                ('doi', models.URLField(max_length=255, verbose_name='DOI')),
                ('zenodo', models.URLField(max_length=255)),
                ('openair', models.URLField(verbose_name='OpenAire')),
                ('openaccess', models.URLField(max_length=255, verbose_name='OpenAccess')),
                ('cyberleninka', models.URLField(max_length=255, verbose_name='Cyberleninka')),
                ('google', models.URLField(verbose_name='Google Schoolar')),
                ('article_name_uz', models.TextField(blank=True, verbose_name='Maqola nomi (Asosiy til) (uz)')),
                ('article_name_en', models.TextField(blank=True, verbose_name='Maqola nomi (Asosiy til) (en)')),
                ('article_name_ru', models.TextField(blank=True, verbose_name='Maqola nomi (Asosiy til) (ru)')),
                ('annotation_uz', models.TextField(blank=True, verbose_name='Annotasiya (Asosiy til) (uz)')),
                ('annotation_en', models.TextField(blank=True, verbose_name='Annotasiya (Asosiy til) (en)')),
                ('annotation_ru', models.TextField(blank=True, verbose_name='Annotasiya (Asosiy til) (ru)')),
                ('key_word_uz', models.TextField(blank=True, verbose_name="Kalit so'zlar (uz)")),
                ('key_word_en', models.TextField(blank=True, verbose_name="Kalit so'zlar (en)")),
                ('key_word_ru', models.TextField(blank=True, verbose_name="Kalit so'zlar (ru)")),
                ('literature', models.TextField(blank=True, verbose_name='Adabiyotlar')),
                ('writer_document', models.ImageField(blank=True, null=True, upload_to='images/document/', verbose_name='Mualliflik Guvohnomasi')),
                ('greeting_card', models.ImageField(blank=True, null=True, upload_to='images/greeting_card/', verbose_name='Diplom')),
                ('greeting_card2', models.ImageField(blank=True, null=True, upload_to='images/greeting_card/', verbose_name='Diplom2')),
                ('greeting_card3', models.ImageField(blank=True, null=True, upload_to='images/greeting_card/', verbose_name='Diplom3')),
                ('greeting_card4', models.ImageField(blank=True, null=True, upload_to='images/greeting_card/', verbose_name='Diplom4')),
                ('handbook', models.ImageField(blank=True, null=True, upload_to='images/handbook/', verbose_name="Ma'lumotnoma")),
                ('certificate', models.ImageField(blank=True, null=True, upload_to='images/certificate/', verbose_name='Sertifikat')),
                ('author1', models.CharField(max_length=40, verbose_name='Muallif(1)')),
                ('author2', models.CharField(blank=True, max_length=40, null=True, verbose_name='Muallif(2)')),
                ('author3', models.CharField(blank=True, max_length=40, null=True, verbose_name='Muallif(3)')),
                ('author4', models.CharField(blank=True, max_length=40, null=True, verbose_name='Muallif(4)')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='post.dfieldmodel', verbose_name="Yo'nalishi")),
                ('promoter', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='post.propagandistmodel', verbose_name="Targ'ibotchi")),
            ],
            options={
                'verbose_name': 'D seriya',
                'verbose_name_plural': 'D seriya',
            },
        ),
        migrations.CreateModel(
            name='CclassModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.PositiveSmallIntegerField()),
                ('issue', models.PositiveSmallIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('language', models.CharField(choices=[("o'zbekcha", "o'zbekcha"), ('ruscha', 'ruscha'), ('inglizcha', 'inglizcha')], max_length=10, verbose_name='Qaysi tilda yozilgan')),
                ('pages', models.CharField(max_length=255, verbose_name='Sahifalar')),
                ('article_pdf', models.FileField(blank=True, null=True, upload_to='article/', verbose_name='Maqola (pdf)')),
                ('doi', models.URLField(max_length=255, verbose_name='DOI')),
                ('zenodo', models.URLField(max_length=255)),
                ('openair', models.URLField(verbose_name='OpenAire')),
                ('openaccess', models.URLField(max_length=255, verbose_name='OpenAccess')),
                ('cyberleninka', models.URLField(max_length=255, verbose_name='Cyberleninka')),
                ('google', models.URLField(verbose_name='Google Schoolar')),
                ('article_name_uz', models.TextField(blank=True, verbose_name='Maqola nomi (Asosiy til) (uz)')),
                ('article_name_en', models.TextField(blank=True, verbose_name='Maqola nomi (Asosiy til) (en)')),
                ('article_name_ru', models.TextField(blank=True, verbose_name='Maqola nomi (Asosiy til) (ru)')),
                ('annotation_uz', models.TextField(blank=True, verbose_name='Annotasiya (Asosiy til) (uz)')),
                ('annotation_en', models.TextField(blank=True, verbose_name='Annotasiya (Asosiy til) (en)')),
                ('annotation_ru', models.TextField(blank=True, verbose_name='Annotasiya (Asosiy til) (ru)')),
                ('key_word_uz', models.TextField(blank=True, verbose_name="Kalit so'zlar (uz)")),
                ('key_word_en', models.TextField(blank=True, verbose_name="Kalit so'zlar (en)")),
                ('key_word_ru', models.TextField(blank=True, verbose_name="Kalit so'zlar (ru)")),
                ('literature', models.TextField(blank=True, verbose_name='Adabiyotlar')),
                ('writer_document', models.ImageField(blank=True, null=True, upload_to='images/document/', verbose_name='Mualliflik Guvohnomasi')),
                ('greeting_card', models.ImageField(blank=True, null=True, upload_to='images/greeting_card/', verbose_name='Diplom')),
                ('greeting_card2', models.ImageField(blank=True, null=True, upload_to='images/greeting_card/', verbose_name='Diplom2')),
                ('greeting_card3', models.ImageField(blank=True, null=True, upload_to='images/greeting_card/', verbose_name='Diplom3')),
                ('greeting_card4', models.ImageField(blank=True, null=True, upload_to='images/greeting_card/', verbose_name='Diplom4')),
                ('handbook', models.ImageField(blank=True, null=True, upload_to='images/handbook/', verbose_name="Ma'lumotnoma")),
                ('certificate', models.ImageField(blank=True, null=True, upload_to='images/certificate/', verbose_name='Sertifikat')),
                ('author1', models.CharField(max_length=40, verbose_name='Muallif(1)')),
                ('author2', models.CharField(blank=True, max_length=40, null=True, verbose_name='Muallif(2)')),
                ('author3', models.CharField(blank=True, max_length=40, null=True, verbose_name='Muallif(3)')),
                ('author4', models.CharField(blank=True, max_length=40, null=True, verbose_name='Muallif(4)')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='post.cfieldmodel', verbose_name="Yo'nalishi")),
                ('promoter', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='post.propagandistmodel', verbose_name="Targ'ibotchi")),
            ],
            options={
                'verbose_name': 'C seriya',
                'verbose_name_plural': 'C seriya',
            },
        ),
        migrations.CreateModel(
            name='BclassModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.PositiveSmallIntegerField()),
                ('issue', models.PositiveSmallIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('language', models.CharField(choices=[("o'zbekcha", "o'zbekcha"), ('ruscha', 'ruscha'), ('inglizcha', 'inglizcha')], max_length=10, verbose_name='Qaysi tilda yozilgan')),
                ('pages', models.CharField(max_length=255, verbose_name='Sahifalar')),
                ('article_pdf', models.FileField(blank=True, null=True, upload_to='article/', verbose_name='Maqola (pdf)')),
                ('doi', models.URLField(max_length=255, verbose_name='DOI')),
                ('zenodo', models.URLField(max_length=255)),
                ('openair', models.URLField(verbose_name='OpenAire')),
                ('openaccess', models.URLField(max_length=255, verbose_name='OpenAccess')),
                ('cyberleninka', models.URLField(max_length=255, verbose_name='Cyberleninka')),
                ('google', models.URLField(verbose_name='Google Schoolar')),
                ('article_name_uz', models.TextField(blank=True, verbose_name='Maqola nomi (Asosiy til) (uz)')),
                ('article_name_en', models.TextField(blank=True, verbose_name='Maqola nomi (Asosiy til) (en)')),
                ('article_name_ru', models.TextField(blank=True, verbose_name='Maqola nomi (Asosiy til) (ru)')),
                ('annotation_uz', models.TextField(blank=True, verbose_name='Annotasiya (Asosiy til) (uz)')),
                ('annotation_en', models.TextField(blank=True, verbose_name='Annotasiya (Asosiy til) (en)')),
                ('annotation_ru', models.TextField(blank=True, verbose_name='Annotasiya (Asosiy til) (ru)')),
                ('key_word_uz', models.TextField(blank=True, verbose_name="Kalit so'zlar (uz)")),
                ('key_word_en', models.TextField(blank=True, verbose_name="Kalit so'zlar (en)")),
                ('key_word_ru', models.TextField(blank=True, verbose_name="Kalit so'zlar (ru)")),
                ('literature', models.TextField(blank=True, verbose_name='Adabiyotlar')),
                ('writer_document', models.ImageField(blank=True, null=True, upload_to='images/document/', verbose_name='Mualliflik Guvohnomasi')),
                ('greeting_card', models.ImageField(blank=True, null=True, upload_to='images/greeting_card/', verbose_name='Diplom')),
                ('greeting_card2', models.ImageField(blank=True, null=True, upload_to='images/greeting_card/', verbose_name='Diplom2')),
                ('greeting_card3', models.ImageField(blank=True, null=True, upload_to='images/greeting_card/', verbose_name='Diplom3')),
                ('greeting_card4', models.ImageField(blank=True, null=True, upload_to='images/greeting_card/', verbose_name='Diplom4')),
                ('handbook', models.ImageField(blank=True, null=True, upload_to='images/handbook/', verbose_name="Ma'lumotnoma")),
                ('certificate', models.ImageField(blank=True, null=True, upload_to='images/certificate/', verbose_name='Sertifikat')),
                ('author1', models.CharField(max_length=40, verbose_name='Muallif(1)')),
                ('author2', models.CharField(blank=True, max_length=40, null=True, verbose_name='Muallif(2)')),
                ('author3', models.CharField(blank=True, max_length=40, null=True, verbose_name='Muallif(3)')),
                ('author4', models.CharField(blank=True, max_length=40, null=True, verbose_name='Muallif(4)')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='post.bfieldmodel', verbose_name="Yo'nalishi")),
                ('promoter', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='post.propagandistmodel', verbose_name="Targ'ibotchi")),
            ],
            options={
                'verbose_name': 'B seriya',
                'verbose_name_plural': 'B seriya',
            },
        ),
        migrations.CreateModel(
            name='AclassModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.PositiveSmallIntegerField()),
                ('issue', models.PositiveSmallIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('language', models.CharField(choices=[("o'zbekcha", "o'zbekcha"), ('ruscha', 'ruscha'), ('inglizcha', 'inglizcha')], max_length=10, verbose_name='Qaysi tilda yozilgan')),
                ('pages', models.CharField(max_length=255, verbose_name='Sahifalar')),
                ('article_pdf', models.FileField(blank=True, null=True, upload_to='article/', verbose_name='Maqola (pdf)')),
                ('doi', models.URLField(max_length=255, verbose_name='DOI')),
                ('zenodo', models.URLField(max_length=255)),
                ('openair', models.URLField(verbose_name='OpenAire', max_length=255)),
                ('openaccess', models.URLField(max_length=255, verbose_name='OpenAccess')),
                ('cyberleninka', models.URLField(max_length=255, verbose_name='Cyberleninka')),
                ('google', models.URLField(verbose_name='Google Schoolar', max_length=255)),
                ('article_name_uz', models.TextField(blank=True, verbose_name='Maqola nomi (Asosiy til) (uz)')),
                ('article_name_en', models.TextField(blank=True, verbose_name='Maqola nomi (Asosiy til) (en)')),
                ('article_name_ru', models.TextField(blank=True, verbose_name='Maqola nomi (Asosiy til) (ru)')),
                ('annotation_uz', models.TextField(blank=True, verbose_name='Annotasiya (Asosiy til) (uz)')),
                ('annotation_en', models.TextField(blank=True, verbose_name='Annotasiya (Asosiy til) (en)')),
                ('annotation_ru', models.TextField(blank=True, verbose_name='Annotasiya (Asosiy til) (ru)')),
                ('key_word_uz', models.TextField(blank=True, verbose_name="Kalit so'zlar (uz)")),
                ('key_word_en', models.TextField(blank=True, verbose_name="Kalit so'zlar (en)")),
                ('key_word_ru', models.TextField(blank=True, verbose_name="Kalit so'zlar (ru)")),
                ('literature', models.TextField(blank=True, verbose_name='Adabiyotlar')),
                ('writer_document', models.ImageField(blank=True, null=True, upload_to='images/document/', verbose_name='Mualliflik Guvohnomasi')),
                ('greeting_card', models.ImageField(blank=True, null=True, upload_to='images/greeting_card/', verbose_name='Diplom')),
                ('greeting_card2', models.ImageField(blank=True, null=True, upload_to='images/greeting_card/', verbose_name='Diplom2')),
                ('greeting_card3', models.ImageField(blank=True, null=True, upload_to='images/greeting_card/', verbose_name='Diplom3')),
                ('greeting_card4', models.ImageField(blank=True, null=True, upload_to='images/greeting_card/', verbose_name='Diplom4')),
                ('handbook', models.ImageField(blank=True, null=True, upload_to='images/handbook/', verbose_name="Ma'lumotnoma")),
                ('certificate', models.ImageField(blank=True, null=True, upload_to='images/certificate/', verbose_name='Sertifikat')),
                ('author1', models.CharField(max_length=40, verbose_name='Muallif(1)')),
                ('author2', models.CharField(blank=True, max_length=40, null=True, verbose_name='Muallif(2)')),
                ('author3', models.CharField(blank=True, max_length=40, null=True, verbose_name='Muallif(3)')),
                ('author4', models.CharField(blank=True, max_length=40, null=True, verbose_name='Muallif(4)')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='post.afieldmodel', verbose_name="Yo'nalishi")),
                ('promoter', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='post.propagandistmodel', verbose_name="Targ'ibotchi")),
            ],
            options={
                'verbose_name': 'A seriya',
                'verbose_name_plural': 'A seriya',
            },
        ),
    ]
