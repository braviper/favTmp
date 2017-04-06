from peewee import *

database = SqliteDatabase('../db/template.db')

class BaseModel(Model):
    class Meta:
        database = database

class menu(BaseModel):
    name = CharField()
    content = CharField()
    icon = CharField()
    sort_num = IntegerField()

class admin(BaseModel):
    account = CharField(unique=True)
    nickname = CharField()
    password = CharField()
    role = IntegerField()
    create_date = DateTimeField(null=True)
    update_date = DateTimeField(null=True)
    last_login_date = DateTimeField(null=True)




if __name__ == '__main__':
    import os
    if not os.path.isdir("../db"):
        os.mkdir('../db')
    database.connect()
    database.drop_tables([menu,admin])
    database.create_tables([menu,admin])

    adm = admin.create(account="admin",password="1",nickname='超级管理员',role=-1)
    adm.save()

    me = menu.create(name='菜单',content='menu',icon="bars",sort_num=2)
    me2 = menu.create(name='管理员', content='admin',icon="user", sort_num=1)
    me.save()
    me2.save()
    database.close()