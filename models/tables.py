# coding: utf8
from datetime import datetime

#Typical stuff thinking of just adding rep(reputation of the user returning stuff) on to auth user. maybe a profile icon too.
db.define_table('person',
                Field('name', 'string'),
                Field('email', 'string', requires=IS_EMAIL()),
                Field('a_id', db.auth_user, default=auth.user_id), #a_id is the auth user, will be used in items table
                Field('rep', 'float', default=10.00),
                
                )

#We will search through items to find the user's items
db.define_table('items',
                Field('item_owner', db.auth_user, default=auth.user_id),
                Field('start_date', 'datetime', default=datetime.utcnow()),
                Field('end_date', 'datetime'),
                Field('borrower', 'string', default=None),
                Field('item_image', 'upload'),
                Field('description', 'text'),
                Field('tag', 'string'),

            )

#This is how we will keep track of the users friends
db.define_table('friend',
                Field('pOne', db.auth_user, default=None),
                Field('pTwo', db.auth_user, default=None),
                
               )
