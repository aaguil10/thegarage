# coding: utf8
from datetime import datetime

db.define_table('itemList',
             Field('To_Do', 'string'),
             #Field('file', 'upload'),
             #Field('image_id', 'reference image'),
             #Field('author'),
             Field('description', 'text'),
             #Field('random', default=randNum),
             Field('for_user', requires=IS_EMAIL()),
             Field('from_user'),
             Field('status', 'string', default='In Progress'),
             Field('accepted', 'string', default='waiting')
             #Field('numviews', 'integer', default=0),
             )

db.define_table('person',
                Field('name', 'string'),
                Field('email', 'string', requires=IS_EMAIL()),
                Field('a_id', db.auth_user, default=auth.user_id), #a_id is the auth user, will be used in items table
                
                )

db.define_table('items',
            Field('item_owner', db.auth_user, default=auth.user_id),
            Field('start_date', 'datetime', default=datetime.utcnow()),
            Field('end_date', 'datetime'),
            Field('borrower', 'string', default=None),
            Field('description', 'text'),
            Field('tag', 'string'),

    )



db.itemList.accepted.writable = db.itemList.accepted.readable = False
db.itemList.status.writable = db.itemList.status.readable = False
db.itemList.from_user.writable = db.itemList.from_user.readable = False
db.itemList.for_user.requires = [IS_IN_DB(db, db.auth_user.email)]
db.itemList.description.requires = IS_NOT_EMPTY()
db.itemList.To_Do.requires = IS_NOT_EMPTY()
