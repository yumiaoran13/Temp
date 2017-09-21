import pymysql.cursors
import random
import time


def rand_name():
    first_name = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
                  '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
                  '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
                  '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
                  '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
                  '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
                  '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']

    middle_name = ['子', '梓', '紫', '欣', '梦', '诗', '嘉', '雨', '可', '佳', '一', '心', '思', '静', '诺', '皓', '博', '宇', '泽', '明',
                   '俊', '文', '灏', '天', '沐', '若']

    last_name = ['涵', '怡', '熙', '曦', '琪', '萱', '彤', '馨', '欣', '瑶', '诺', '然', '轩', '佑', '泽', '墨', '硕', '航', '涵',
                 '宇', '辰', '楚', '言', '', '', '', '']

    full_name = random.choice(first_name) + random.choice(middle_name) + random.choice(last_name)
    return full_name


def connectdb():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='test',
                           charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    return conn


def insert(connection):
        # user_info 表
        cursor = connection.cursor()
        user_type = 2
        mobile = int('1880000' + str(random.randint(1000, 9999)))
        stu_no = random.randint(100000000, 999999999)
        pwd = 'e10adc3949ba59abbe56e057f20f883e'
        sex = 1
        logo = '/file/defaultHeadBoy.png'
        true_name = rand_name()
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        create_time = now
        value = (user_type, mobile, stu_no, pwd, sex, true_name, create_time, logo)
        sql = "INSERT INTO `user_info` (`type`, `mobile`, `stu_no`, `pwd`, `sex`, `true_name`, " \
              "`create_time`, `logo`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) "
        # 获取最后一条数据主键
        # user_id = int(connection.insert_id())
        try:
            cursor.execute(sql, value)
            connection.commit()
        except:
            connection.rollback()


if __name__ == '__main__':
    connect = connectdb()
    for i in range(100):
        insert(connect)
    connect.close()
