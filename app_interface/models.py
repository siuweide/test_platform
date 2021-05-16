from django.db import models
from app_manage.models import Module

class ApiCase(models.Model):
    REQUESTS_CHOICE = (
        ('POST', 'POST'),
        ('GET', 'GET'),
        ('PUT', 'PUT'),
        ('DELETE', 'DELETE'),
    )

    REQUEST_TYPE = (
        ('FORM-DATA', 'FORM-DATA'),
        ('JSON', 'JSON'),
    )

    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    name = models.CharField('名称', max_length=50, null=False)
    url = models.TextField('URL', null=False)
    header = models.TextField('请求头', null=True)
    method = models.CharField('请求方式', max_length=100, choices=REQUESTS_CHOICE, default='GET')
    request_type = models.CharField('请求类型', max_length=100, choices=REQUEST_TYPE, default='FORM-DATA')
    result = models.TextField('响应结果', null=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'apicase'