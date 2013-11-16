# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simple replace the two lines below with:
    return auth.wiki()
    """
    return dict()

def editprofile():
    form = SQLFORM(db.person)
    if form.process().accepted:
        session.flash = 'Profile edited!'
        redirect(URL('index'))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill the form'
    return dict(form=form)

@auth.requires_login()
def profilepg():
    nickname = request.args[0]
    response.title = nickname + "'s Profile"
    result = db(db.auth_user.nickname == nickname).select()[0]
    name = result.first_name + " " + result.last_name
    image = result.image
    currentUser = get_uemail()
    q = (db.items.email == get_uemail())
    record = db().select(db.person.ALL)
    record = SQLTABLE(db().select(db.person.ALL),
                       upload = URL('download'), # allows pics preview
                       headers='fieldname:capitalize')
    """
    form = SQLFORM(db.person, upload=URL(r=request, c='default', f='download'))
    currentUser = get_uemail()
    q = (db.items.email == get_uemail())
    grid = SQLFORM.grid(q, create=True, csv=False, searchable=True,
        fields=[db.items.item_owner, db.items.title, db.items.description],
        details=True, editable=True, deletable=True)
    q2 = (db.items.borrower == get_uemail())
    grid2 = SQLFORM.grid(q2, create=False, csv=False, searchable=True,
        fields=[db.items.item_owner, db.items.title, db.items.description],
        details=True, editable=False)
    """
    return dict(nickname=nickname, name=name, image=image, record=record)


def profile():
    person = db.person(request.args(0)) or redirect(URL('index'))
    form = SQLFORM(db.person, upload=URL(r=request, c='default', f='download'))
    currentUser = get_uemail()
    q = (db.items.email == get_uemail())
    grid = SQLFORM.grid(q, create=True, csv=False, searchable=True,
        fields=[db.items.item_owner, db.items.title, db.items.description],
        details=True, editable=True, deletable=True)
    q2 = (db.items.borrower == get_uemail())
    grid2 = SQLFORM.grid(q2, create=False, csv=False, searchable=True,
        fields=[db.items.item_owner, db.items.title, db.items.description],
        details=True, editable=False)
    q3 = (db.items.item_owner == currentUser)
    grid3 = SQLFORM.grid(q3, create=False, csv=False, searchable=True,
        fields=[db.items.item_owner, db.items.title, db.items.description],
        details=True, editable=True, deletable=True)

    return dict(grid = grid, grid2=grid2, grid3=grid3, form=form, person=person)



@auth.requires_login()
def create():
    form = SQLFORM(db.items)
    if form.process().accepted:
        session.flash = 'Item added!'
        redirect(URL('profile'))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill the form'
    return dict(form=form)


def About_us():
    return dict()


def available():
    avacontent = URL('default', 'friStuff', )
    
    listfrd1 = db(db.friend.pOne == auth.user_id).select()
    listfrd2 = db(db.friend.pTwo == auth.user_id).select()

    
    return dict(avacontent=avacontent, listfrd1=listfrd1, listfrd2=listfrd2, )

def Borrowed():
    return dict()

def inst_fri():
    return dict()

def friStuff():
    #this will be in charge of diplays friends stuff
    if request.args(0) == None:
        redirect(URL('default', 'inst_fri', )) 
    client_id = request.args(0)
    idref = db.person(request.args(0))
    name = idref.name
    pic_list = []
    
    list_items = db(db.items.item_owner == client_id).select()
    for r in list_items:
        imgti = r.item_image
        #imgti[17:]
        pic_list.append(URL('download', args=[imgti]))

    return dict(list_items=list_items, client_id=client_id, pic_list=pic_list, name=name, )

def checkdebuger():
    q = db.items
    grid = SQLFORM.grid(q,
        searchable=True,
        fields=[db.items.item_owner, db.items.borrower, db.items.item_image, db.items.tag],
        csv=True, details=True, create=True, editable=True, deletable=True,
        )
    
    f = db.friend
    fgrid = SQLFORM.grid(f,
        searchable=True,
        fields=[db.friend.pOne, db.friend.pTwo],
        csv=True, details=True, create=True, editable=True, deletable=True,
        )
        
    p = db.person
    pgrid = SQLFORM.grid(p,
        searchable=True,
        fields=[db.person.name, db.person.a_id, db.person.email, db.person.rep, ],
        csv=True, details=True, create=True, editable=True, deletable=True,
        )
    
    return dict(grid=grid, fgrid=fgrid,pgrid=pgrid )


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
