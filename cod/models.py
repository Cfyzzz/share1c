from django.db import models


# Create your models here.
class Tags(models.Model):
    name = models.CharField(default="",
                            max_length=20,
                            unique=True)

    def __unicode__(self):
        return self.name

    class Mets:
        verbose_name = "tag"
        verbose_name_plural = "tags"


class Cod(models.Model):
    row_code = models.TextField("code")
    create_date = models.DateTimeField(u"Дата создания", auto_now_add=True)
    uid = models.TextField(null=True,
                           blank=True,
                           db_column="uid")
    tegs = models.ForeignKey(Tags,
                             on_delete=models.CASCADE,
                             null=True,
                             blank=True,
                             db_column="tags")

    def __unicode__(self):
        return self.row_code

    class Meta:
        verbose_name = "code"
        verbose_name_plural = "code"
