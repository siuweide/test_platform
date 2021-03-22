from django.db import models

class Project(models.Model):
    name = models.CharField('项目名称', max_length=100)
    describe = models.TextField('描述')
    status = models.BooleanField('状态', default=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.name

class Module(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField('模块名称', max_length=100)
    describe = models.TextField('描述')
    status = models.BooleanField('状态', default=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.name
