# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Data(models.Model):
    report_num = models.IntegerField(db_column='REPORT_NUM', blank=True, null=True)  # Field name made lowercase.
    event_property_name = models.TextField(db_column='EVENT_PROPERTY_NAME', blank=True, null=True)  # Field name made lowercase.
    event_type_id = models.IntegerField(db_column='EVENT_TYPE_ID', blank=True, null=True)  # Field name made lowercase.
    event_type_name = models.TextField(db_column='EVENT_TYPE_NAME', blank=True, null=True)  # Field name made lowercase.
    event_src_name = models.TextField(db_column='EVENT_SRC_NAME', blank=True, null=True)  # Field name made lowercase.
    district_id = models.IntegerField(db_column='DISTRICT_ID', blank=True, null=True)  # Field name made lowercase.
    intime_archive_num = models.IntegerField(db_column='INTIME_ARCHIVE_NUM', blank=True, null=True)  # Field name made lowercase.
    sub_type_id = models.IntegerField(db_column='SUB_TYPE_ID', blank=True, null=True)  # Field name made lowercase.
    district_name = models.TextField(db_column='DISTRICT_NAME', blank=True, null=True)  # Field name made lowercase.
    community_id = models.IntegerField(db_column='COMMUNITY_ID', blank=True, null=True)  # Field name made lowercase.
    rec_id = models.IntegerField(db_column='REC_ID', blank=True, null=True)  # Field name made lowercase.
    street_id = models.IntegerField(db_column='STREET_ID', blank=True, null=True)  # Field name made lowercase.
    overtime_archive_num = models.IntegerField(db_column='OVERTIME_ARCHIVE_NUM', blank=True, null=True)  # Field name made lowercase.
    operate_num = models.IntegerField(db_column='OPERATE_NUM', blank=True, null=True)  # Field name made lowercase.
    dispose_unit_id = models.IntegerField(db_column='DISPOSE_UNIT_ID', blank=True, null=True)  # Field name made lowercase.
    street_name = models.TextField(db_column='STREET_NAME', blank=True, null=True)  # Field name made lowercase.
    create_time = models.TextField(db_column='CREATE_TIME', blank=True, null=True)  # Field name made lowercase.
    event_src_id = models.IntegerField(db_column='EVENT_SRC_ID', blank=True, null=True)  # Field name made lowercase.
    intime_to_archive_num = models.IntegerField(db_column='INTIME_TO_ARCHIVE_NUM', blank=True, null=True)  # Field name made lowercase.
    sub_type_name = models.TextField(db_column='SUB_TYPE_NAME', blank=True, null=True)  # Field name made lowercase.
    event_property_id = models.IntegerField(db_column='EVENT_PROPERTY_ID', blank=True, null=True)  # Field name made lowercase.
    occur_place = models.TextField(db_column='OCCUR_PLACE', blank=True, null=True)  # Field name made lowercase.
    community_name = models.TextField(db_column='COMMUNITY_NAME', blank=True, null=True)  # Field name made lowercase.
    dispose_unit_name = models.TextField(db_column='DISPOSE_UNIT_NAME', blank=True, null=True)  # Field name made lowercase.
    main_type_name = models.TextField(db_column='MAIN_TYPE_NAME', blank=True, null=True)  # Field name made lowercase.
    main_type_id = models.IntegerField(db_column='MAIN_TYPE_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data'


class Dataversion(models.Model):
    version = models.IntegerField(primary_key=True)
    time = models.TextField()

    class Meta:
        managed = False
        db_table = 'dataversion'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class User(models.Model):
    username = models.CharField(max_length=256, blank=True, null=True)
    password = models.CharField(max_length=256, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    qq = models.CharField(max_length=64, blank=True, null=True)
    blog = models.CharField(max_length=64, blank=True, null=True)
    image = models.CharField(max_length=45, blank=True, null=True)
    checked = models.IntegerField(blank=True, null=True)
    maincolor = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'user'


class Userback(models.Model):
    teltype = models.CharField(max_length=50, blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    msg = models.TextField(blank=True, null=True)
    questiontype = models.CharField(max_length=50, blank=True, null=True)
    time = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userback'
