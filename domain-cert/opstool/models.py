from django.db import models
from account.models import User 
# Create your models here.

class EventRecord(models.Model):
    EVENT_STATUS_CHOICES = (
        ('w', '未开始'),
        ('p', '处理中'),
        ('f', '已完成'),
    )
    EVENT_LEVEL_CHOICES = (
        ('a', '警告'),
        ('b', '严重'),
        ('c', '灾难'),
    )
    id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=45, verbose_name="事件", null=False)
    event_status = models.CharField(max_length=4, choices=EVENT_STATUS_CHOICES, verbose_name="状态", null=False)
    event_level  = models.CharField(max_length=4, choices=EVENT_LEVEL_CHOICES, verbose_name="级别", null=False)
    # event_processor = models.CharField(max_length=10, verbose_name="处理人", null=False)
    event_processer = models.ForeignKey(User, default='1', verbose_name="处理人", null=False,  related_name='event_processer_user', on_delete=models.SET_DEFAULT) 
    event_start_time = models.DateField(verbose_name="开始时间", null=False)
    event_end_time = models.DateField(verbose_name="结束时间", null=False)
    create_at = models.DateTimeField(auto_now_add=True, null=False, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, null=False, verbose_name="更新时间")
    class Meta:
        db_table = "event"
        ordering = ['-id']
        default_permissions = ()
        permissions = (
            ("opstool_read_event", "查看事件权限"),
            ("opstool_add_event", "新建事件权限"),
            ("opstool_update_event", "更新事件权限"),
            ("opstool_delete_event", "删除时间权限"),
        )
        verbose_name = '事件管理'
        verbose_name_plural = '运维事件信息'

class FaultRecord(models.Model):
    FAULT_STATUS_CHOICES = (
        (0, '未开始'),
        (1, '处理中'),
    )
    FAULT_LEVEL_CHOICES = (
        ('a', '一级故障'),
        ('b', '二级故障'),
        ('c', '三级故障'),
        ('d', '四级故障'),
        ('e', '五级故障'),
    )
    
    id = models.AutoField(primary_key=True)
    fault_name = models.CharField(max_length=45, verbose_name="事件", null=False)
    fault_status = models.BooleanField(max_length=4, choices=FAULT_STATUS_CHOICES, verbose_name="状态", null=False)
    fault_level  = models.CharField(max_length=4, choices=FAULT_LEVEL_CHOICES, verbose_name="级别", null=False)
    # falut_person = models.CharField(max_length=10, verbose_name="责任人", null=True, blank=True)
    falut_person = models.ForeignKey(User, default='1', verbose_name="责任人", null=False, related_name='fault_person_user', on_delete=models.SET_DEFAULT)
    # fault_processer = models.CharField(User, verbose_name="处理人", null=True) 
    fault_processer = models.ForeignKey(User, default='1', verbose_name="处理人", null=False,  related_name='fault_processer_user', on_delete=models.SET_DEFAULT) 
    # fault_report = models.CharField(max_length=45, verbose_name="故障报告", null=True, blank=True)
    fault_report = models.FileField(upload_to='uploads/', verbose_name="故障报告", null=True, blank=True)
    fault_issue = models.CharField(max_length=200, verbose_name="故障原因", null=True, blank=True)
    fault_summary = models.CharField(max_length=500, verbose_name="故障总结", null=True, blank=True) 
    fault_start_time = models.DateField(verbose_name="开始时间", null=False)
    fault_end_time = models.DateField(verbose_name="结束时间", null=False)
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="更新时间")
    class Meta:
        db_table = "fault"
        ordering = ['-id']
        default_permissions = ()
        permissions = (
            ("opstool_read_fault", "查看故障权限"),
            ("opstool_add_fault", "新建故障权限"),
            ("opstool_update_fault", "更新故障权限"),
            ("opstool_delete_fault", "删除故障权限"),
        )
        verbose_name = '故障管理'
        verbose_name_plural = '运维故障信息'
