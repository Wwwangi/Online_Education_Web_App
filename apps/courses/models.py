# 原生库
from datetime import datetime

# 第三方库
from django.db import models

# 自己定义的库函数
from apps.users.models import BaseModel
from apps.organizations.models import Teacher

# 1. 确定实体，一个实体一张表，关系型数据库
# 实体1 <关系> 实体2
# 课程 <1对多> 章节 <1对多> 视频
# 课程 <1对多> 课程资源

# 2. 确定实体的具体字段

# 3. 确定每一个字段的类型，是否必填


class Course(BaseModel):
    teacher = models.ForeignKey(Teacher, verbose_name='授课讲师', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='课程名', max_length=50)
    description = models.CharField(verbose_name='课程简介', max_length=300)
    learn_time = models.IntegerField(verbose_name='学习时长(分钟数)', default=0)
    degree = models.CharField(verbose_name='课程难度', choices=(('cj', '初级'), ('zj', '中级'), ('gj', '高级')), max_length=2)
    students = models.IntegerField(verbose_name='学习人数', default=0)
    fav_nums = models.IntegerField(verbose_name='收藏人数', default=0)
    click_nums = models.IntegerField(verbose_name='点击数', default=0)
    category = models.CharField(verbose_name='课程类别', max_length=20, default=u'后端开发')
    # 可以用标签做相关推荐，比如两门课都有django
    tag = models.CharField(verbose_name='课程标签', max_length=10, default='')
    need_know = models.CharField(verbose_name='课程须知', max_length=300, default='')
    teacher_tell = models.CharField(verbose_name='老师的话', max_length=300, default='')

    # TextField()不限制最大长度
    detail = models.TextField(verbose_name='课程详情')
    image = models.ImageField(verbose_name='封面图', upload_to='courses/%Y/%m', max_length=100)

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name


class Lesson(BaseModel):
    # 这里的course是主表Course的外键
    # on_delete表示对应的外键数据被删除后（这里指对应的课程），当前的数据（这里指章节）应该也跟着被删除
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u'章节名', max_length=100)
    learn_time = models.IntegerField(verbose_name=u'学习时长(分钟数)', default=0)

    class Meta:
        verbose_name = '课程章节'
        verbose_name_plural = verbose_name


class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, verbose_name='章节', on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u'视频名', max_length=100)
    learn_time = models.IntegerField(verbose_name=u'学习时长(分钟数)', default=0)
    url = models.CharField(verbose_name=u'访问地址', max_length=200)

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u'资源名称', max_length=100)
    file = models.FileField(verbose_name='资源链接', upload_to='courses/resources/%Y/%m', max_length=200)

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name

