# -*- coding:utf-8 -*-
def check_num(num):
    a = "学号格式错误，第1-4位数字必须在2013-2018之间,第5-8位必须为2119,第9-10位必须在0-18之间,第11-12位必须在0-32之间"
    if '2013' < num[:4] < '2018':
        if num[4:8] == '2119':
            if '0' < num[8:10] < '18':
                if '0' < num[10:] < '32':
                    return num
                else:
                    print(a)
                    return 0
            else:
                print(a)
                return 0
        else:
            print(a)
            return 0
    else:
        print(a)
        return 0



