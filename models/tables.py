# coding: utf8

from datetime import datetime


#Typical stuff thinking of just adding rep(reputation of the user returning stuff) on to auth user. maybe a profile icon too.

db.define_table('person',
                Field('email', 'string', requires=IS_EMAIL()),
                Field('your_items', 'reference items'),
                Field('your_friends', 'reference friend'),
                Field('a_id', db.auth_user, default=auth.user_id), #a_id is the auth user, will be used in items table
                Field('rep', 'float', default=10.00),
                Field('profile_pic', 'upload'))


def get_uemail():
    if auth.user:
        return auth.user.email
    else:
        return 'None'

#We will search through items to find the user's items
db.define_table('items',
                Field('title', 'text', IS_NOT_EMPTY()),
                Field('email', 'string', default=get_uemail()),
               # Field('item_owner', db.auth_user, default=auth.user_id),
                Field('item_owner', 'string'),
                Field('start_date', 'datetime', default=datetime.utcnow()),
                Field('end_date', 'datetime'),
                Field('borrower', 'string'),
                Field('item_image', 'upload'),
                Field('description', 'text'),
                Field('tag', 'list:reference tag'),
            )

db.items.borrower.requires = [IS_IN_DB(db, db.auth_user.email)]
# many to many relationship, items can have many tags, tags can belong to many items.
db.define_table('tag',
               Field('Name', unique=True),
               format = '%(Name)s')

# store relationship between item and tag
db.define_table('item_tag',
                Field('title', 'reference items'),
                Field('tag', 'reference tag')
                )

# many to many relationship, you can borrow items from different users
db.define_table('borrowed_items',
                Field('title', 'reference items'),
                Field('borrower', db.auth_user, default=auth.user_id),
                Field('item_owner', 'reference items'),
                )

# many to many relationship, you can lend items from different users
db.define_table('lent_items',
                Field('title', 'reference items'),
                Field('borrower', 'reference items'),
                Field('item_owner', 'reference items'),
                )

#This is how we will keep track of the users friends
db.define_table('friend',
                Field('pOne', db.auth_user, default=None),
                Field('pTwo', db.auth_user, default=None),
               )

db.items.item_owner.requires = IS_NOT_IN_DB(db, db.items.item_owner), IS_NOT_EMPTY()
db.items.description.requires = IS_NOT_EMPTY()
db.items.title.requires = IS_NOT_EMPTY()
db.person.a_id.writable = db.person.a_id.readable = False
db.person.rep.writable = db.person.rep.readable = False
db.person.your_items.writable = db.person.your_items.readable = False
db.person.your_friends.writable = db.person.your_friends.readable = False
db.person.email.writable = db.person.email.readable = False
db.items.email.writable = False
db.items.item_owner.writable = db.items.item_owner.readable = False
db.items.tag.writable = db.items.tag.readable = True
