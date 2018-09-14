
from peewee import CharField,  IntegerField, BigIntegerField
from config import db_config

from peewee import Model, MySQLDatabase
from playhouse.shortcuts import RetryOperationalError


class MyRetryDb(RetryOperationalError, MySQLDatabase):
    pass

db_config = db_config.db_config_data
db = MyRetryDb(db_config['db_name'], user=db_config['db_user'], password=db_config['db_password'],
               host=db_config['db_host'], port=db_config['db_port'])


class baseModel(Model):

    class Meta:
        database = db


class StuGradeModel(baseModel):
    stu_id = IntegerField(primary_key=True)
    stu_num = BigIntegerField(20)
    stu_term = IntegerField(11)
    stu_class = CharField(20)
    stu_name = CharField(20)
    math_grade = IntegerField(11)
    chinese_grade = IntegerField(11)
    english_grade = IntegerField(11)
    all_grade = IntegerField(11)
    aver_grade = IntegerField(11)

    class Meta:
        db_table = 'stugrademodel'

# db.connect()
#
# db.create_table(StuGradeModel)
# print(db.get_tables())

