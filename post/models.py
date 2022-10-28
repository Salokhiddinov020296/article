from tabnanny import verbose
from django.db import models
from django.utils.translation import get_language
from django.utils.translation import gettext_lazy as _


class FieldModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("yo'nalishi"))

    class Meta:
        verbose_name = "Yo'nalishi"
        verbose_name_plural = "Yo'nalishi"

    def __str__(self):
        return self.name


class WhichLanguageWriteModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Qaysi tilda yozilgan"))

    class Meta:
        verbose_name = "Yozilgan tili tanlsh"
        verbose_name_plural = "Yozilgan tili tanlash"

    def __str__(self):
        return self.name


class PropagandistModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Targ'ibotchi"))

    class Meta:
        verbose_name = "Targ'ibotchi"
        verbose_name_plural = "Targ'ibotchilar"

    def __str__(self):
        return self.name


class AclassModel(models.Model):
    volume = models.PositiveSmallIntegerField()
    issue = models.PositiveSmallIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    field = models.ForeignKey(FieldModel, on_delete=models.RESTRICT, verbose_name=_("Yo'nalishi"))
    language = models.ForeignKey(WhichLanguageWriteModel, on_delete=models.RESTRICT,
                                 verbose_name=_('Qaysi tilda yozilgan'))
    pages = models.CharField(max_length=255, verbose_name=_("Sahifalar"))
    article_pdf = models.FileField(blank=True, null=True, upload_to='article/', verbose_name=_("Maqola (pdf)"))
    doi = models.URLField(max_length=255, verbose_name = "DOI")
    zenodo = models.URLField(max_length=255)
    openair = models.URLField(max_length=200, verbose_name = "OpenAire")
    # writer = models.CharField(max_length=255, verbose_name=_("Mualliflar"))
    article_name_uz = models.TextField(blank=True, verbose_name=_("Maqola nomi (Asosiy til) (uz)"))
    article_name_en = models.TextField(blank=True, verbose_name=_("Maqola nomi (Asosiy til) (en)"))
    article_name_ru = models.TextField(blank=True, verbose_name=_("Maqola nomi (Asosiy til) (ru)"))
    annotation_uz = models.TextField(blank=True, verbose_name=_("Annotasiya (Asosiy til) (uz)"))
    annotation_en = models.TextField(blank=True, verbose_name=_("Annotasiya (Asosiy til) (en)"))
    annotation_ru = models.TextField(blank=True, verbose_name=_("Annotasiya (Asosiy til) (ru)"))
    key_word_uz = models.TextField(blank=True, verbose_name=_("Kalit so'zlar (uz)"))
    key_word_en = models.TextField(blank=True, verbose_name=_("Kalit so'zlar (en)"))
    key_word_ru = models.TextField(blank=True, verbose_name=_("Kalit so'zlar (ru)"))
    literature = models.TextField(blank=True, verbose_name=_("Adabiyotlar"))
    promoter = models.ForeignKey(PropagandistModel, on_delete=models.RESTRICT,
                                 verbose_name=_("Targ'ibotchi"))
    writer_document = models.ImageField(upload_to='images/document/', verbose_name=_("Mualliflik Guvohnomasi"), null=True, blank=True)
    greeting_card = models.ImageField(upload_to='images/greeting_card/', verbose_name=_("Diplom"), null=True, blank=True)
    greeting_card2 = models.ImageField(upload_to='images/greeting_card/', verbose_name=_("Diplom2"), null=True, blank=True)
    greeting_card3 = models.ImageField(upload_to='images/greeting_card/', verbose_name=_("Diplom3"), null=True, blank=True)
    greeting_card4 = models.ImageField(upload_to='images/greeting_card/', verbose_name=_("Diplom4"), null=True, blank=True)
    handbook = models.ImageField(upload_to='images/handbook/', verbose_name=_("Ma'lumotnoma"), null=True, blank=True)
    certificate = models.ImageField(upload_to='images/certificate/', verbose_name=_("Sertifikat"), null=True, blank=True)
    author1 = models.CharField(verbose_name = _("Muallif(1)"), max_length = 40, null=False, blank=False)
    author2 = models.CharField(verbose_name = _("Muallif(2)"), max_length = 40, null=True, blank=True)
    author3 = models.CharField(verbose_name = _("Muallif(3)"), max_length = 40, null=True, blank=True)
    author4 = models.CharField(verbose_name = _("Muallif(4)"), max_length = 40, null=True, blank=True)

    # def __str__(self):
    #     return f"{self.article_pdf} ({self.volume}/{self.issue}) {self.pages} {self.writer} " \
    #            f"{self.article_name_uz} {self.article_name_en} {self.article_name_ru}... " \
    #            f"{self.field} " \
    #            f"{self.language} {self.date} {self.promoter}"

    class Meta:
        verbose_name = 'A seriya'
        verbose_name_plural = 'A seriya'

    @property
    def article_name(self):
        return getattr(self, f"article_name_{get_language()}")

    @property
    def annotation(self):
        return getattr(self, f"annotation_{get_language()}")

    @property
    def key_word(self):
        return getattr(self, f"key_word_{get_language()}")
