from django.db import models
from core.models import TimeStampedModel

class Reference(TimeStampedModel):
    uploader = models.ForeignKey("user.User", on_delete=models.SET_NULL, null=True, related_name="uploader") # 업로더
    album = models.ForeignKey("album.Album", on_delete=models.SET_NULL, null=True) # 디폴트 album 하나 만들기
    picture = models.FileField(upload_to="%Y/%m/%d") # 이미지
    url = models.URLField() # url
    movie = models.FileField(upload_to="%Y/%m/%d") # 동영상 파일
    text = models.TextField() # 설명
    report_cnt = models.IntegerField(default=0) # 신고 수
    report_users = models.ManyToManyField("user.User", related_name="report_users") # 신고한 사람들

    def __str__(self):
        return self.album