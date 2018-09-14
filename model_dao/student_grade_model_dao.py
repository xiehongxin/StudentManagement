# coding:UTF-8

from playhouse.shortcuts import dict_to_model
from model.student_grade_model import StuGradeModel
from peewee import DoesNotExist


class StuGradeModelDao:
    def __init__(self):
        pass

    # 检查学号是否存在
    @staticmethod
    def check_stu_num(stu_num):
        try:
            StuGradeModel.get(StuGradeModel.stu_num == stu_num)
            return 1
        except DoesNotExist:
            return 0

    # 检查班级是否存在
    @staticmethod
    def check_class_num(stu_class):
        try:
            StuGradeModel.get(StuGradeModel.stu_class == stu_class)
            return 1
        except DoesNotExist:
            return 0

    # 检查学期是否存在
    @staticmethod
    def check_term_num(stu_term):
        try:
            StuGradeModel.get(StuGradeModel.stu_term == stu_term)
            return 1
        except DoesNotExist:
            return 0

    # 获取学号所对应的学期信息
    @staticmethod
    def get_stu_term(stu_term):
        try:
            term = StuGradeModel.select().where(StuGradeModel.stu_term == stu_term).execute()
            return term
        except DoesNotExist:
            return 0

    # 插入一条数据
    @staticmethod
    def insert_stu_info(req):
        stu_num = req["stu_num"]
        stu_term = req["stu_term"]
        stu_class = req["stu_class"]
        stu_name = req["stu_name"]
        math_grade = req["math_grade"]
        chinese_grade = req["chinese_grade"]
        english_grade = req["english_grade"]
        all_grade = req["all_grade"]
        aver_grade = req["aver_grade"]
        StuGradeModel.insert(stu_num=stu_num, stu_term=stu_term, stu_class=stu_class, stu_name=stu_name,
                             math_grade=math_grade, chinese_grade=chinese_grade, english_grade=english_grade,
                             all_grade=all_grade, aver_grade=aver_grade).execute()


    # 求学生的三科分数
    @staticmethod
    def get_stu_grade(stu_num):

        try:
            grade = StuGradeModel.select().where(StuGradeModel.stu_num == stu_num).execute()
            return grade
        except DoesNotExist:
            return None

    # 按班级统计学生的成绩
    @staticmethod
    def get_class_grade(stu_class):

        try:
            grade = StuGradeModel.select().order_by(StuGradeModel.aver_grade.desc())\
                .where(StuGradeModel.stu_class == stu_class).execute()
            return grade
        except DoesNotExist:
            return None

    #
    # # 修改学生的成绩
    # @staticmethod
    # def modify_stu_grade(stu_num, req):
    #     model = dict_to_model(StuGradeModel, req)
    #     try:
    #         model.save().where(StuGradeModel.stu_num == stu_num).execute()
    #         return True
    #     except Exception as error:
    #         print(error)
    #         return False

    # 根据学号修改学生信息
    @staticmethod
    def modify_stu_info(req):
        stu_num = req["stu_num"]
        stu_term = req["stu_term"]
        math_grade = req["math_grade"]
        chinese_grade = req["chinese_grade"]
        english_grade = req["english_grade"]
        all_grade = req["all_grade"]
        aver_grade = req["aver_grade"]

        StuGradeModel.update(math_grade=math_grade, chinese_grade=chinese_grade, english_grade=english_grade,
                             all_grade=all_grade, aver_grade=aver_grade).\
                    where((StuGradeModel.stu_num == stu_num) & (StuGradeModel.stu_term == stu_term)).execute()

    # 删除学生信息
    @staticmethod
    def delete_stu_info(id):
        try:
            StuGradeModel.get(stu_num=id).delete_instance()
        except Exception as error:
            return error


