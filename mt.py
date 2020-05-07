#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019\2\27 0027 11:46
# @Author  : luf
import pymysql

# try:
#     db = pymysql.connect('localhost', "root", "", "mysql")
#     # 使用 cursor() 方法创建一个游标对象 cursor
#     cursor = db.cursor()
#
#     # 使用 execute() 方法执行 SQL，如果表存在则删除
#     # cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
#
#     # 使用预处理语句创建表
#     sql = """select * from user """
#
#     cursor.execute(sql)
#     ret = cursor.fetchall()
# except Exception as e:
#     pass
# # 关闭数据库连接
# finally:
#     if db:
#         db.close()


from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    name = Column(String(20))


if __name__ == '__main__':
    try:
        # 初始化数据库连接:
        engine = create_engine('mysql+pymysql://test:test@localhost:3306/testdb')
        Base.metadata.create_all(engine, checkfirst=True)

        # 创建DBSession类型:
        DBSession = sessionmaker(bind=engine)

        # 创建session对象:
        session = DBSession()
        # 创建新User对象:
        # new_user = User(name='eason')
        # 添加到session:
        # session.add(new_user)
        # 提交即保存到数据库:
        ret = session.query(User)
        for user in ret:
            print(user.name)
        # ret = session.delete(User(id='5', name='Bob'))
        # session.commit()

    except Exception as e:
        pass
    finally:
        # 关闭session:
        session.close()
#i change something