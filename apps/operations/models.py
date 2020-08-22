from django.db import models

from django.contrib.auth import get_user_model

from apps.users.models import BaseModel
from apps.courses.models import Course

# 不直接从users.models中import UserProfile是因为如果以后要引用django自带的uer表会要改动很多，难以维护
UserProfile = get_user_model()


# 用于客户填写一张表格询问自己感兴趣的课程
class UserAsk(BaseModel):
    name = models.CharField(verbose_name='姓名', max_length=20)
    mobile = models.CharField(verbose_name='手机', max_length=11)
    course_name = models.CharField(verbose_name='课程名', max_length=50)

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name


# 用于给课程写评论
class CourseComments(BaseModel):
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE)
    comments = models.CharField(verbose_name='评论内容', max_length=200)

    class Meta:
        verbose_name = '课程评论'
        verbose_name_plural = verbose_name


# 用于客户收藏，喜欢的课程，教师，机构
# 如果全部用外键的话，当只收藏很多老师不收藏课程的时候，数据库会有很多空间上的浪费，不可取
class UserFavorite(BaseModel):
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    fav_id = models.IntegerField(verbose_name='数据id')
    fav_type = models.CharField(verbose_name='收藏类型', max_length=1, choices=((1, '课程'), (2, '课程机构'), (3, '讲师')), default=1)

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name


# 用于记录用户间发送的消息
class UserMessage(BaseModel):
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    message = models.CharField(verbose_name='消息内容', max_length=200)
    has_read = models.BooleanField(verbose_name='已读', default=False)

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name


# 记录用户学习的课程(目前1对多)
class UserCourse(BaseModel):
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name


