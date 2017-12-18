from django.db import models

# 사용자 정보 테이블
class UserInfo(models.Model):
    name = models.CharField(verbose_name="사용자 이름", max_length=45)
    email = models.EmailField("사용자 이메일", max_length=45, unique=True)
    password = models.CharField("사용자 패스워드", max_length=45)
    part_name = models.CharField("사용자 소속부서", max_length=45, blank=True)
    valid_yn = models.CharField("활성화 여부", max_length=1, default='Y')
    mobile_num = models.CharField("핸드폰 번호", max_length=11, blank=True)
    create_date = models.DateTimeField("생성일시", auto_now_add=True)
    update_date = models.DateTimeField("수정일시", auto_now=True, null=True)

    class Meta:
        db_table = 'res_user'

    def __str__(self):
        part_name = self.part_name
        if (self.part_name is None) or self.part_name == "":
            part_name = "-"
        return self.name + "/" + part_name

# 회의실 정보 테이블
class RoomInfo(models.Model):
    room_name = models.CharField("회의실 이름", max_length=45, unique=True)
    room_desc = models.CharField("회의실 설명", max_length=200, blank=True)
    room_capacity = models.IntegerField(verbose_name="수용 인원", default=0)
    create_date = models.DateTimeField("생성일시", auto_now_add=True)
    update_date = models.DateTimeField("수정일시", auto_now=True, null=True)

    class Meta:
        db_table = 'res_room_info'


    def __str__(self):
        return self.room_name

# 회의 설정 테이블
class ConferenceInfo(models.Model):
    room = models.ForeignKey(RoomInfo)
    user = models.ForeignKey(UserInfo)
    conference_title = models.CharField("회의 제목", max_length=45)
    conference_description = models.TextField("회의 내용", blank=True)
    start_date = models.DateTimeField("회의 시작일시")
    end_date = models.DateTimeField("회의 종료일시")
    create_date = models.DateTimeField("생성일시", auto_now_add=True)
    update_date = models.DateTimeField("수정일시", auto_now=True, null=True)

    class Meta:
        db_table = 'res_conference_info'

    def __str__(self):
        return self.conference_title


# 회의 참석자 설정 테이블
class ConferenceMember(models.Model):
    conference = models.ForeignKey(ConferenceInfo)
    user = models.ForeignKey(UserInfo)
    etc_member = models.CharField("그외 참석자", max_length=45)
    create_date = models.DateTimeField("생성일시", auto_now_add=True)
    update_date = models.DateTimeField("수정일시", auto_now=True, null=True)


    class Meta:
        db_table = 'res_conference_member'

    def __str__(self):
        return ConferenceInfo(self.conference)




