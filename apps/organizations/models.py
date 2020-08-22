from django.db import models

from apps.users.models import BaseModel


# 如果直接在CourseOrg里定义city字段然后加choices的话，以后要多加城市就很难维护, 可以将城市作为外键
class City(BaseModel):
    name = models.CharField(verbose_name='城市名', max_length=20)
    desc = models.CharField(verbose_name='城市描述', max_length=200)

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name


class CourseOrg(BaseModel):
    name = models.CharField(verbose_name='机构名称', max_length=50)
    desc = models.TextField(verbose_name='机构描述', default='')
    tag = models.CharField(verbose_name='机构标签', max_length=10, default='全国知名')
    category = models.CharField(verbose_name='机构类别', max_length=4, choices=(('pxjg', '培训机构'), ('gr', '个人'), ('gx', '高校')), default='pxjg')
    click_nums = models.IntegerField(verbose_name='点击数', default=0)
    fav_nums = models.IntegerField(verbose_name='收藏数', default=0)
    image = models.ImageField(verbose_name='logo', upload_to='org/%Y/%m', max_length=100)
    address = models.CharField(verbose_name='机构地址', max_length=150)
    students = models.IntegerField(verbose_name='学习人数', default=0)
    course_nums = models.IntegerField(verbose_name='课程数', default=0)
    city = models.ForeignKey(City, verbose_name='所在城市', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name


class Teacher(BaseModel):
    org = models.ForeignKey(CourseOrg, verbose_name='所属机构', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='教师名', max_length=50)
    work_years = models.IntegerField(verbose_name='工作年限', default=0)
    work_company = models.CharField(verbose_name='工作单位', max_length=50)
    work_position = models.CharField(verbose_name='工作职位', max_length=50)
    points = models.CharField(verbose_name='教学特点', max_length=50)
    click_nums = models.IntegerField(verbose_name='点击数', default=0)
    fav_nums = models.IntegerField(verbose_name='收藏数', default=0)
    age = models.IntegerField(verbose_name='年龄', default=18)
    image = models.ImageField(verbose_name='头像', upload_to='teacher/%Y/%m', max_length=100, default='')

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name
