import datetime

import models

"""
TYPES
01. Esperanto insert (esp_ins)
02. Esperanto update (esp_upd)
03. Esperanto delete (esp_del)
11. English insert (eng_ins)
12. English update (eng_upd)
13. English delete (eng_del)
21. User insert (use_ins)
22. User update (use_upd)
23. User delete (use_del)

"""
""" insert """
def log_change(type, change):
    models.init_db()
    models.ChangeLogEntry.create(change_type=type, change=change, time_of_entry=datetime.datetime.now())

""" read """
def get_changes(paginate_by=50, page_num=1, type="all", search=None):
    if search == None:
        if type=="all":
            return models.ChangeLogEntry.select().paginate(page_num, paginate_by)
        else:
            models.ChangeLogEntry.select(models.ChangeLogEntry.type == type).paginate(page_num, paginate_by)
