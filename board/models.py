from django.db import models

# Create your models here.


class Board(models.Model):
    title = models.CharField("제목", max_length=100)
    contents = models.CharField("본문내용", max_length=500)
    cre_user = models.CharField("작성자", max_length=50)
    cre_date = models.DateTimeField("작성일자", auto_now_add=True, null=False)
    upd_date = models.DateTimeField("수정일자", auto_now=True, null=True)

    class Meta:
        db_table = 'board'
        ordering = ('-cre_date',)

    def __str__(self):
        return self.title
