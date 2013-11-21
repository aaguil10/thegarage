# a table to link two people
db.define_table('link',
    Field('friender','reference auth_user'),
    Field('target','reference auth_user'),
    Field('accepted','boolean',default=False))

# and define some global variables that will make code more compact
User, Link = db.auth_user, db.link
me, a0, a1 = auth.user_id, request.args(0), request.args(1)
myfriends = db(Link.friender==me)(Link.accepted==True)
alphabetical = User.first_name|User.last_name
def name_of(user): return '%(first_name)s %(last_name)s' % user
