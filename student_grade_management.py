#!/usr/bin/python
# encoding:utf-8

from model_dao.student_grade_model_dao import StuGradeModelDao
import re
import check_stu_num_format as csnf


def menu():
    print("========================================")
    print("按学期、按班级完成对学生成绩的录入:0")
    print("按班级统计学生的成绩，求学生的总分及平均分，并排序:1")
    print("查询学生成绩:2")
    print("按班级输出学生的成绩单:3")
    print("按学号删除学生纪录，成绩:4")
    print("按学号和学期修改成绩：5")
    print("退出:6")
    print("========================================")

# 测试数据
# 1,20152119,aa,10,40,60
# 1,201521191624,aa,10,40,60
# 2,201521191624,aa,10,50,70
# 1,201521191623,dd,20,50,70


# 插入学生信息
def add_info():
    # 这里不用输入班级，因为班级可通过学号获取
    request = input("请按顺序输入学生完整信息：学期,学号,姓名,课程分数等,以逗号分隔:\n")
    listOfTokens = re.split(r'\W', request)
    infoList = [tok for tok in listOfTokens if len(tok) > 0]

    if len(infoList) == 6:
        stu_term = infoList[0]
        stu_num = infoList[1]
        stu_class = stu_num[8:10]
        stu_name = infoList[2]
        math_grade = infoList[3]
        chinese_grade = infoList[4]
        english_grade = infoList[5]
        # 判断学号格式是否正确
        if csnf.check_num(stu_num):
            # 判断学号是否存在
            if not StuGradeModelDao.check_stu_num(stu_num):
                req = {}
                req["stu_num"] = int(stu_num)
                req["stu_term"] = int(stu_term)
                req["stu_class"] = stu_class
                req["stu_name"] = stu_name
                req["math_grade"] = int(math_grade)
                req["chinese_grade"] = int(chinese_grade)
                req["english_grade"] = int(english_grade)
                all_grade = int(math_grade) + int(chinese_grade) + int(english_grade)
                aver_grade = all_grade / 3.0
                req["all_grade"] = all_grade
                req["aver_grade"] = aver_grade

                StuGradeModelDao.insert_stu_info(req)
                print("录入成功")
            # 判断在学号存在的情况下，学期是否一致，不一致即可插入数据
            else:
                if not StuGradeModelDao.get_stu_term(stu_term):
                    req = {}
                    req["stu_num"] = int(stu_num)
                    req["stu_term"] = int(stu_term)
                    req["stu_class"] = stu_class
                    req["stu_name"] = stu_name
                    req["math_grade"] = int(math_grade)
                    req["chinese_grade"] = int(chinese_grade)
                    req["english_grade"] = int(english_grade)
                    all_grade = int(math_grade) + int(chinese_grade) + int(english_grade)
                    aver_grade = all_grade / 3.0
                    req["all_grade"] = all_grade
                    req["aver_grade"] = aver_grade
                    StuGradeModelDao.insert_stu_info(req)
                    print("录入成功")
                else:
                    print("该学生成绩已存在")

        else:
            print("学号格式错误")
    else:
        print("输入的格式错误")


# 按班级统计学生的成绩，求学生的总分及平均分，并能根据学生的平均成绩进行排序
def get_class_grade():
    stu_class = input("请输入要查询的班级")
    # 判断班级是否存在
    if StuGradeModelDao.check_class_num(stu_class):
        grade = StuGradeModelDao.get_class_grade(stu_class)
        for g in grade:
            # all_grade = g.math_grade + g.chinese_grade + g.english_grade
            # aver_grade = all_grade / 3.0
            print("%s 班学号为 %d 的学生的第 %d 学期的数学成绩为%d, 语文成绩为%d, 英语成绩为%d, 总分为%d, 平均分为%d"
                  % (stu_class, g.stu_num, g.stu_term, g.math_grade, g.chinese_grade, g.english_grade, g.all_grade, g.aver_grade))
    else:
        print("该班级未存在,请重新查询\n")


# 查询学生成绩，不及格科目及学生名单
def get_stu_grade():
    stu_num = int(input("请输入要查询的学生学号\n"))
    if StuGradeModelDao.check_stu_num(stu_num):
        grade = StuGradeModelDao.get_stu_grade(stu_num)

        for g in grade:
            failList = []
            if g.math_grade < 60:
                failList.append("数学")
            if g.chinese_grade < 60:
                failList.append("语文")
            if g.english_grade < 60:
                failList.append("英语")
            print("%s 班学号为 %d 的 %s同学第 %d 学期的数学成绩为%d, 语文成绩为%d, 英语成绩为%d, 不及格科目为%s"
                  %(g.stu_class, g.stu_num, g.stu_name, g.stu_term, g.math_grade, g.chinese_grade, g.english_grade, str(failList)))
    else:
        print("该学生未存在,请重新查询\n")


# 修改学生成绩
def modify_stu():
    request = input("请按顺序输入要修改成绩的学生完整信息：学期,学号,姓名,新的课程分数等,以逗号分隔:\n")
    listOfTokens = re.split(r'\W', request)
    infoList = [tok for tok in listOfTokens if len(tok) > 0]

    if len(infoList) == 6:
        stu_term = infoList[0]
        stu_num = infoList[1]
        stu_class = stu_num[8:10]
        stu_name = infoList[2]
        math_grade = infoList[3]
        chinese_grade = infoList[4]
        english_grade = infoList[5]
        # 判断学号格式是否正确
        if csnf.check_num(stu_num):
            # 判断学号和学期是否存在
            if (StuGradeModelDao.check_stu_num(stu_num) and StuGradeModelDao.check_term_num(stu_term)):
                req = {}
                req["stu_num"] = int(stu_num)
                req["stu_term"] = int(stu_term)
                req["stu_class"] = stu_class
                req["stu_name"] = stu_name
                req["math_grade"] = int(math_grade)
                req["chinese_grade"] = int(chinese_grade)
                req["english_grade"] = int(english_grade)
                all_grade = int(math_grade) + int(chinese_grade) + int(english_grade)
                aver_grade = all_grade / 3.0
                req["all_grade"] = all_grade
                req["aver_grade"] = aver_grade

                StuGradeModelDao.modify_stu_info(req)
                print("修改成功")

            else:
                print("该学生成绩不存在，请重新输入")
        else:
            print("学号格式错误")
    else:
        print("输入的格式错误")


# 删除学生的成绩
def delete_stu():
    stu_num = int(input("请输入要删除的学生学号"))
    if StuGradeModelDao.check_stu_num(stu_num):
        StuGradeModelDao.delete_stu_info(stu_num)
        print("已删除学号为%d的信息" % stu_num)
    else:
        print("该学生未存在,请重新输入\n")

while True:
    menu()
    number = input('请输入菜单项\n')
    if number == '0':   # 按学期、按班级完成对学生成绩的录入:0
        add_info()

    elif number == '1':  # 按班级统计学生的成绩:1
        get_class_grade()

    elif number == '2':  # 查询学生成绩:2
        get_stu_grade()

    elif number == '3':  # 按班级输出学生的成绩单:3
        get_class_grade()

    elif number == '4':  # 按学号删除学生纪录，成绩:4
        delete_stu()

    elif number == '5':
        modify_stu()

    else:
        exit()
