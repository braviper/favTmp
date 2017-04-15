from peewee import *
from playhouse import shortcuts
import json

database = SqliteDatabase('../db/template.db')


class BaseModel(Model):
    class Meta:
        database = database

    def tojson(self):
        r = {}
        for k in self._data.keys():
            try:
                r[k] = str(getattr(self, k))
            except:
                r[k] = json.dumps(getattr(self, k))
        return str(r)


class menu(BaseModel):
    value = CharField()
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


def init_db():
    import os

    if not os.path.isdir("../db"):
        os.mkdir('../db')
    database.connect()
    database.drop_tables([menu, admin])
    database.create_tables([menu, admin])

    adm = admin.create(account="admin", password="1", nickname='超级管理员', role=-1)
    adm.save()
    me = menu.create(value='管理员', content='admin', icon="user", sort_num=1)
    me.save()
    me = menu.create(value='菜单', content='menu', icon="bars", sort_num=2)
    me.save()
    for i in menu.select().where(menu.id == 1):
        print(shortcuts.model_to_dict(i))

    for i in menu.select():
        print(shortcuts.model_to_dict(i))

    database.close()


if __name__ == '__main__':
    init_db()
