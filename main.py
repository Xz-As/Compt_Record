from functions import db_func as db1
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox


e2c = {
    'uid':'学号',
    'tid':'队号',
    'mid':'比赛ID',
    'uname':'姓名',
    'utype':'用户种类',
    'dept':'学院',
    'gender':'性别',
    'tleader':'队长',
    'ttype':'参赛类别',
    'tlv':'最高名次',
    'mlv':'比赛级别',
    'mred':'先红队号',
    'mblue':'先蓝队号',
    'mwinner':'胜方先手',
    'mjudge':'裁判ID',
    'mnum':'比赛场次',
    'loss':'剩余分',
    'wipe':'歼灭分',
    'ctrl':'夺控分',
    'scr':'总胜分'
}


def outp(qq):
    print(qq)

class ids:
    tid = 1
    mid = 1

print('开始')


def menu_put(wd_name):
    fmenu = tk.Menu(wd_name, tearoff = 0)
    fmenu.add_command(label = '退出',  command = lambda : exit(0))
    menus = tk.Menu(wd_name)
    #menus.add.add_command(label = '文件')
    menus.add_cascade(label='文件',menu=fmenu)
    wd_name['menu']=menus


def ent(host, user, passwd, name):
    global db, entered
    entered = False
    db = db1(host = host, user = user, passwd = passwd, name = name)
    if db.ent:
        entered = True
        wd1.destroy()


def regist(user, passwd):
    global dbm
    dbm = db1(host = '139.9.119.34', user = 's2018300150', passwd = 'GaussDB@123', name = '2018300150')
    dbm.grant(user, passwd)
    global db, entered
    entered = False
    db = db1(host = '139.9.119.34', user = user, passwd = passwd, name = '2018300150')
    if db.ent:
        entered = True
        wd1.destroy()


def log_in():
        button = tk.Button(text = '登录', command =lambda : ent(host = '139.9.119.34', user = entryId.get(), passwd = entrypswd.get(), name = '2018300150'))
        button.grid(row = 4, column = 0)
        button = tk.Button(text = '默认', command =lambda : ent(host = '139.9.119.34', user = 's2018300150', passwd = 'GaussDB@123', name = '2018300150'))
        button.grid(row = 4, column = 1)
        button = tk.Button(text = '注册', command =lambda : regist(user = entryId.get(), passwd = entrypswd.get()))
        button.grid(row = 4, column = 2)
        wd1.mainloop()


def shutd(wds):
    wds.destroy()


def ins_user_func(wbinsuser):
    lbid = tk.Label(wbinsuser, text = '学号：')
    lbid.grid(row = 1, column = 0)
    entryid = tk.Entry(wbinsuser)
    entryid.grid(row = 1, column = 1)

    lbname = tk.Label(wbinsuser, text = '姓名：')
    lbname.grid(row = 2, column = 0)
    entryname = tk.Entry(wbinsuser)
    entryname.grid(row = 2, column = 1)

    lbdept = tk.Label(wbinsuser, text = '学院：')
    lbdept.grid(row = 3, column = 0)
    entrydept = tk.Entry(wbinsuser)
    entrydept.grid(row = 3, column = 1)

    lbadmin = tk.Label(wbinsuser, text = '用户类别：')
    lbadmin.grid(row = 4, column = 0)
    utype = [
    ('裁判', 1),
    ('选手', 0)]
    vutype = tk.IntVar()
    vutype.set(1)
    i = 0
    for lang,num in utype:
        b = tk.Radiobutton(wbinsuser, text=lang, value=num, variable=vutype, takefocus = True, command = lambda : vutype.set(num))
        b.grid(row = 4 + i, column = 1)
        i += 1

    lbgend = tk.Label(wbinsuser, text = '性别：')
    lbgend.grid(row = 6, column = 0)
    gtype = [
    ('男', 0),
    ('女', 1)]
    vgtype = tk.IntVar()
    vgtype.set(1)
    b1 = tk.Radiobutton(wbinsuser, text=gtype[0][0], value=gtype[0][1], variable=vgtype, takefocus = True, command = lambda :     vgtype.set(0))
    b1.grid(row = 6, column = 1)
    b1 = tk.Radiobutton(wbinsuser, text=gtype[1][0], value=gtype[1][1], variable=vgtype, takefocus = True, command = lambda :     vgtype.set(1))
    b1.grid(row = 7, column = 1)
    button1 = tk.Button(wbinsuser, text = '插入', command = lambda : db.insert(tab_name = 'user', values = (int(entryid.get()), int(vutype.get()), entryname.get(), entrydept.get(), int(vgtype.get()))))
    button1.grid(row = 8, column = 0)
    button2 = tk.Button(wbinsuser, text = '取消', command = lambda : shutd(wbinsuser))
    button2.grid(row = 8, column = 1)


def ins_user(db_name):
    wbinsuser = tk.Tk()
    wbinsuser.title('插入用户信息')
    wbinsuser.maxsize(1080, 960)
    wbinsuser.minsize(800, 600)
    menu_put(wbinsuser)
    ins_user_func(wbinsuser = wbinsuser)
    

def tidplus(tab_name, id1, type1):
    ids.tid += 1
    res = db.search('team', tg_cols = 'tid', order = 'tid')
    print(res[1:])
    tids = [i[0] for i in res[1:]]
    while ids.tid in tids:
        ids.tid += 1
    if db.insert(tab_name = tab_name, values = (ids.tid, id1, type1, 0)):
        db.insert(tab_name = 'ut', values = (int(id1), int(ids.tid)))


def midplus(tab_name, idr, idb, win, jg, lv):
    ids.mid += 1
    while not db.insert(tab_name = tab_name, values = (ids.mid, lv, idr, idb, win, jg)):
        ids.mid += 1


def ins_team(db_name):
    wbinsuser = tk.Tk()
    wbinsuser.title('插入队伍信息')
    wbinsuser.maxsize(1080, 960)
    wbinsuser.minsize(800, 600)
    menu_put(wbinsuser)
    lbid = tk.Label(wbinsuser, text = '队长学号：')
    lbid.grid(row = 1, column = 0)
    entryid = tk.Entry(wbinsuser)
    entryid.grid(row = 1, column = 1)

    lbtype = tk.Label(wbinsuser, text = '参赛种类：')
    lbtype.grid(row = 2, column = 0)
    mtype = [
    ('编队赛', 1),
    ('个人赛', 0)]
    vtype = tk.IntVar()
    vtype.set(1)
    b1 = tk.Radiobutton(wbinsuser, text=mtype[0][0], value=0, variable=vtype, takefocus = True, command = lambda : vtype.set(0))
    b1.grid(row = 2, column = 1)
    b1 = tk.Radiobutton(wbinsuser, text=mtype[1][0], value=1, variable=vtype, takefocus = True, command = lambda : vtype.set(1))
    b1.grid(row = 3, column = 1)

    button = tk.Button(wbinsuser, text = '插入', command = lambda : tidplus('team', int(entryid.get()), int(vtype.get())))
    button.grid(row = 4, column = 0)
    button = tk.Button(wbinsuser, text = '取消', command = lambda : shutd(wbinsuser))
    button.grid(row = 4, column = 1)


def ins_ut(db_name):
    wbinsuser = tk.Tk()
    wbinsuser.title('插入队员')
    wbinsuser.maxsize(1080, 960)
    wbinsuser.minsize(800, 600)
    menu_put(wbinsuser)
    lbid = tk.Label(wbinsuser, text = '队伍编号：')
    lbid.grid(row = 1, column = 0)
    entryid = tk.Entry(wbinsuser)
    entryid.grid(row = 1, column = 1)

    lbuid = tk.Label(wbinsuser, text = '队员编号：')
    lbuid.grid(row = 2, column = 0)
    entryuid = tk.Entry(wbinsuser)
    entryuid.grid(row = 2, column = 1)


    button = tk.Button(wbinsuser, text = '插入', command = lambda : db.insert(tab_name = 'ut', values = (int(entryuid.get()), int(entryid.get()))))
    button.grid(row = 3, column = 0)
    button = tk.Button(wbinsuser, text = '取消', command = lambda : shutd(wbinsuser))
    button.grid(row = 3, column = 1)


def ins_match(db_name):
    wbinsuser = tk.Tk()
    wbinsuser.title('插入比赛结果')
    wbinsuser.maxsize(1080, 960)
    wbinsuser.minsize(800, 600)
    menu_put(wbinsuser)
    fmenu = tk.Menu(wbinsuser, tearoff = 0)
    fmenu.add_command(label = '退出',  command = lambda : exit(0))
    menus = tk.Menu(wbinsuser)
    #menus.add.add_command(label = '文件')
    menus.add_cascade(label='文件',menu=fmenu)
    wbinsuser['menu']=menus
    lbidr = tk.Label(wbinsuser, text = '先红方队：')
    lbidr.grid(row = 1, column = 0)
    #ids.thing_list.append(lbid)
    entryidr = tk.Entry(wbinsuser)
    entryidr.grid(row = 1, column = 1)

    lbidb = tk.Label(wbinsuser, text = '先蓝方队：')
    lbidb.grid(row = 2, column = 0)
    #ids.thing_list.append(lbuid)
    entryidb = tk.Entry(wbinsuser)
    entryidb.grid(row = 2, column = 1)
    
    lbwin = tk.Label(wbinsuser, text = '胜者：')
    lbwin.grid(row = 3, column = 0)
    mtype = [
    ('先红队', 1),
    ('先蓝队', 0)]
    winner = tk.IntVar()
    b1 = tk.Radiobutton(wbinsuser, text = mtype[0][0], value = 0, variable = winner, takefocus = True, command = lambda : winner.set(0))
    b1.grid(row = 3, column = 1)
    b1 = tk.Radiobutton(wbinsuser, text = mtype[1][0], value = 1, variable = winner, takefocus = True, command = lambda : winner.set(1))
    b1.grid(row = 4, column = 1)


    lbjg = tk.Label(wbinsuser, text = '裁判：')
    lbjg.grid(row = 5, column = 0)
    #ids.thing_list.append(lbuid)
    entryjg = tk.Entry(wbinsuser)
    entryjg.grid(row = 5, column = 1)

    lblv = tk.Label(wbinsuser, text = '比赛级别：')
    lblv.grid(row = 6, column = 0)
    #ids.thing_list.append(lbuid)
    entrylv = tk.Entry(wbinsuser)
    entrylv.grid(row = 6, column = 1)

    button = tk.Button(wbinsuser, text = '插入', command = lambda : midplus('match', int(entryidr.get()), int(entryidb.get()), int(winner.get()), int(entryjg.get()), int(entrylv.get())))
    button.grid(row = 7, column = 0)
    button = tk.Button(wbinsuser, text = '取消', command = lambda : shutd(wbinsuser))
    button.grid(row = 7, column = 1)


def ins_mr_func(wbinsuser):
    lbmid = tk.Label(wbinsuser, text = '比赛ID：')
    lbmid.grid(row = 1, column = 0)
    entrymid = tk.Entry(wbinsuser)
    entrymid.grid(row = 1, column = 1)

    lbmid = tk.Label(wbinsuser, text = '局数：')
    lbmid.grid(row = 2, column = 0)
    mn = tk.IntVar()
    b1 = tk.Radiobutton(wbinsuser, text = '1', value = 0, variable = mn, takefocus = True, command = lambda : mn.set(0))
    b1.grid(row = 2, column = 1)
    b1 = tk.Radiobutton(wbinsuser, text = '2', value = 1, variable = mn, takefocus = True, command = lambda : mn.set(1))
    b1.grid(row = 3, column = 1)

    
    lbloss = tk.Label(wbinsuser, text = '红兵力分：')
    lbloss.grid(row = 4, column = 0)
    entryloss = tk.Entry(wbinsuser)
    entryloss.grid(row = 4, column = 1)

    lbwipe = tk.Label(wbinsuser, text = '红歼灭分：')
    lbwipe.grid(row = 5, column = 0)
    entrywipe = tk.Entry(wbinsuser)
    entrywipe.grid(row = 5, column = 1)

    lbctrl = tk.Label(wbinsuser, text = '红夺控分：')
    lbctrl.grid(row = 6, column = 0)
    entryctrl = tk.Entry(wbinsuser)
    entryctrl.grid(row = 6, column = 1)

    button = tk.Button(wbinsuser, text = '插入', command = lambda : db.insert(tab_name = 'mr', values = (int(entrymid.get()), int(mn.get()), int(entryloss.get()), int(entrywipe.get()), int(entryctrl.get()), int(entryloss.get()) + int(entryctrl.get()) + int(entrywipe.get()))))
    button.grid(row = 7, column = 0)
    button = tk.Button(wbinsuser, text = '取消', command = lambda : shutd(wbinsuser))
    button.grid(row = 7, column = 1)
    wbinsuser.mainloop()


def ins_mr(da_name):
    wbinsuser = tk.Tk()
    wbinsuser.title('插入比赛得分')
    wbinsuser.maxsize(1080, 960)
    wbinsuser.minsize(800, 600)
    menu_put(wbinsuser)
    ins_mr_func(wbinsuser)


def output_res(tab_name, eq_cols = [], values = [], tg_cols = '*', special_cond = [], conne = [], sep = '', order = ''):
    res = db.search(tab_name, eq_cols = eq_cols, values = values, tg_cols = tg_cols, special_cond = special_cond, conne = conne, sep = sep, order = order)
    for i in res:
        print(i)
    wd_res = tk.Tk()
    wd_res.title('查询结果')
    menu_put(wd_res)
    if tg_cols == '*':
        col0 = ''
        cols = []
        for i in res[0]:
            if i != ',':
                col0 += i
            else:
                cols.append(col0)
                col0 = ''
        cols.append(col0)
        col0 = ''
    else:
        print(tg_cols)
        col0 = ''
        cols = []
        for i in tg_cols:
            if i != ',':
                col0 += i
            else:
                cols.append(col0)
                col0 = ''
        cols.append(col0)
        col0 = ''
    tree = tk.ttk.Treeview(wd_res, show="headings", columns = cols)
    ck = 0
    tgt = -1
    for i in cols:
        j = e2c[i]
        tree.column(i, width = 120)
        tree.heading(i, text = j)
    for i in res[1:]:
        j = [jj for jj in i]
        if tab_name == 'user' and tg_cols == '*':
            if j[1] == 0:
                j[1] = '普通选手'
            else:
                j[1] = '裁判'
            if j[4] == 0:
                j[4] = '男'
            else:
                j[4] = '女'
        elif tab_name == 'team' and tg_cols == '*':
            if j[2] == 0:
                j[2] = '个人赛'
            else:
                j[2] = '编队赛'
                ck += 1
                tgt = j[0]
        elif tab_name == 'match' and tg_cols == '*':
            if j[4] == 0:
                j[4] = '蓝'
            else:
                j[4] = '红'
        elif tab_name == 'mr' and tg_cols == '*':
            if j[1] == 0:
                j[1] = '第一场'
            else:
                j[1] = '第二场'
        tree.insert('', 'end', value = j)
    tree.pack(side = 'left', fill = 'y')
    scr = tk.Scrollbar(wd_res)
    tree.config(yscrollcommand = scr.set)
    scr.config(command = tree.yview)
    scr.pack(side= 'right')
    if ck == 1:
        b1 = tk.Button(wd_res, text = '查询全部队员', command = lambda : output_res('user', tg_cols = 'uid,uname', eq_cols = ['uid'], values = ['select uid from ut where tid = ' + str(tgt)], special_cond = ['in']))
        b1.pack(side= 'right')


def search_user():
    wd_su = tk.Tk()
    wd_su.title('查询选项')
    menu_put(wd_su)
    l1 = tk.Label(wd_su, text = '选手学号或姓名')
    l1.grid(row = 1, column = 1)
    fid = tk.Entry(wd_su)
    fid.grid(row = 1, column = 2)
    btninsuser = tk.Button(wd_su, text = '查询选定用户信息', command = lambda : output_res('user', eq_cols = ['uid', 'uname'], values = ['\'' + fid.get() + '\'', '\'' + fid.get() + '\''], special_cond = ['in',  'in'], conne = ['or'], order = 'uid'))
    btninsuser.grid(row = 3, column = 1)
    btnsuall = tk.Button(wd_su, text = '查询全部用户信息', command = lambda : output_res('user', order = 'uid'))
    btnsuall.grid(row = 3, column = 2)


def search_team():
    wd_su = tk.Tk()
    wd_su.title('查询选项')
    menu_put(wd_su)
    l1 = tk.Label(wd_su, text = '队长学号或姓名')
    l1.grid(row = 1, column = 1)
    fid = tk.Entry(wd_su)
    fid.grid(row = 1, column = 2)
    btninsuser = tk.Button(wd_su, text = '查询选定队伍信息',command = lambda : output_res('team', eq_cols = ['tleader', 'tleader'], values = ['\'' + fid.get() +'\'', 'select uid from user where user.uname = \'' + fid.get() + '\''], special_cond = ['in', 'in'], conne = ['or'], order = 'tid'))
    btninsuser.grid(row = 3, column = 1)
    btnsuall = tk.Button(wd_su, text = '查询全部队伍信息',command = lambda : output_res('team', order = 'tid'))
    btnsuall.grid(row = 3, column = 2)


def search_match():
    wd_su = tk.Tk()
    wd_su.title('查询选项')
    menu_put(wd_su)
    l1 = tk.Label(wd_su, text = '比赛ID或参赛队号')
    l1.grid(row = 1, column = 1)
    fid = tk.Entry(wd_su)
    fid.grid(row = 1, column = 2)
    btninsuser = tk.Button(wd_su, text = '查询选定比赛信息',command = lambda : output_res('match', eq_cols = ['mid', 'mred', 'mblue'], values = ['\'' + fid.get() + '\'', '\'' + fid.get() + '\'', '\'' + fid.get() + '\''], special_cond = ['in', 'in', 'in'], conne = ['or', 'or'], order = 'mid'))
    btninsuser.grid(row = 3, column = 1)
    btnsuall = tk.Button(wd_su, text = '查询全部比赛信息',command = lambda : output_res('match', order = 'mid'))
    btnsuall.grid(row = 3, column = 2)


def search_mr():
    wd_su = tk.Tk()
    wd_su.title('查询选项')
    menu_put(wd_su)
    l1 = tk.Label(wd_su, text = '比赛ID')
    l1.grid(row = 1, column = 1)
    fid = tk.Entry(wd_su)
    fid.grid(row = 1, column = 2)
    btninsuser = tk.Button(wd_su, text = '查询选定比赛信息',command = lambda : output_res('mr', eq_cols = ['mid'], values = ['\'' + fid.get() + '\''], special_cond = ['in'], conne = ['or'], order = 'mid'))
    btninsuser.grid(row = 3, column = 1)
    btnsuall = tk.Button(wd_su, text = '查询全部比赛信息',command = lambda : output_res('mr', order = 'mid'))
    btnsuall.grid(row = 3, column = 2)


def search():
    wbsea = tk.Tk()
    wbsea.title('查询')
    wbsea.maxsize(1080, 960)
    wbsea.minsize(800, 600)
    menu_put(wbsea)
    l = tk.Label(wbsea, text = '   ')
    l.grid(row = 0, column = 0)
    btninsuser = tk.Button(wbsea, text = '查询用户信息',command = search_user)
    btninsuser.grid(row = 1, column = 1)
    l = tk.Label(wbsea, text = '   ')
    l.grid(row = 1, column = 2)
    btninsuser = tk.Button(wbsea, text = '查询编队信息',command = search_team)
    btninsuser.grid(row = 1, column = 3)
    l = tk.Label(wbsea, text = '   ')
    l.grid(row = 1, column = 4)
    btninsuser = tk.Button(wbsea, text = '查询比赛信息',command = search_match)
    btninsuser.grid(row = 1, column = 5)
    l = tk.Label(wbsea, text = '   ')
    l.grid(row = 1, column = 6)
    btninsuser = tk.Button(wbsea, text = '查询比赛得分',command = search_mr)
    btninsuser.grid(row = 1, column = 7)


def del_func(tab_name, rows, data):
    deld = 0
    for r in rows:
        if not deld:
            deld = db.del_row(tab_name = tab_name, key_name = r, values = data)
    if not deld:
        print('错误数据')


def del_u():
    wbdu = tk.Tk()
    wbdu.title('删除用户')
    wbdu.maxsize(800, 600)
    wbdu.minsize(600, 400)
    menu_put(wbdu)
    l = tk.Label(wbdu, text = '请输入该选手学号')
    l.grid(row = 1, column = 1)
    data_ = tk.Entry(wbdu)
    data_.grid(row = 1, column = 2)
    button = tk.Button(wbdu, text = '删除', command = lambda : del_func(tab_name = 'user', rows = ('uid', 'uname'), data = int(data_.get())))
    button.grid(row = 7, column = 1)
    button = tk.Button(wbdu, text = '取消', command = lambda : shutd(wbdu))
    button.grid(row = 7, column = 2)


def del_t():
    wbdt = tk.Tk()
    wbdt.title('删除队伍')
    wbdt.maxsize(800, 600)
    wbdt.minsize(600, 400)
    menu_put(wbdt)
    l = tk.Label(wbdt, text = '请输入该队队长学号或队伍编号')
    l.grid(row = 1, column = 1)
    data_ = tk.Entry(wbdt)
    data_.grid(row = 1, column = 2)
    button = tk.Button(wbdt, text = '删除', command = lambda : del_func(tab_name = 'team', rows = ('tid', 'leader'), data = int(data_.get())))
    button.grid(row = 7, column = 1)
    button = tk.Button(wbdt, text = '取消', command = lambda : shutd(wbdt))
    button.grid(row = 7, column = 2)


def del_m():
    wbdu = tk.Tk()
    wbdu.title('删除比赛（慎用！！！）')
    wbdu.maxsize(800, 600)
    wbdu.minsize(600, 400)
    menu_put(wbdu)
    l = tk.Label(wbdu, text = '比赛id')
    l.grid(row = 1, column = 1)
    data_ = tk.Entry(wbdu)
    data_.grid(row = 1, column = 2)
    button = tk.Button(wbdu, text = '删除', command = lambda : del_func(tab_name = 'match', rows = ('mid'), data = int(data_.get())))
    button.grid(row = 7, column = 1)
    button = tk.Button(wbdu, text = '取消', command = lambda : shutd(wbdu))
    button.grid(row = 7, column = 2)


def delda():
    wbsea = tk.Tk()
    wbsea.title('删除')
    wbsea.maxsize(1080, 960)
    wbsea.minsize(800, 600)
    menu_put(wbsea)
    l = tk.Label(wbsea, text = '   ')
    l.grid(row = 0, column = 0)
    btninsuser = tk.Button(wbsea, text = '删除用户信息',command = del_u)
    btninsuser.grid(row = 1, column = 1)
    l = tk.Label(wbsea, text = '   ')
    l.grid(row = 1, column = 2)
    btninsuser = tk.Button(wbsea, text = '删除队伍信息',command = del_t)
    btninsuser.grid(row = 1, column = 3)
    l = tk.Label(wbsea, text = '   ')
    l.grid(row = 1, column = 4)
    btninsuser = tk.Button(wbsea, text = '删除比赛信息',command = del_m)
    btninsuser.grid(row = 1, column = 5)


def alt_u():
    wbdu = tk.Tk()
    wbdu.title('修改用户')
    wbdu.maxsize(800, 600)
    wbdu.minsize(600, 400)
    menu_put(wbdu)
    l = tk.Label(wbdu, text = '用户原学号或姓名')
    l.grid(row = 1, column = 1)
    key_val = tk.Entry(wbdu)
    key_val.grid(row = 1, column = 2)
    l = tk.Label(wbdu, text = '新信息类别')
    l.grid(row = 3, column = 1)
    i2c = ['uid', 'uname', 'dept']
    gtype = [
    ('学号', 0),
    ('姓名', 1),
    ('学院', 2)]
    vgtype = tk.IntVar()
    b1 = tk.Radiobutton(wbdu, text=gtype[0][0], value=gtype[0][1], variable=vgtype, takefocus = True, command = lambda :     vgtype.set(gtype[0][1]))
    b1.grid(row = 3, column = 2)
    b1 = tk.Radiobutton(wbdu, text=gtype[1][0], value=gtype[1][1], variable=vgtype, takefocus = True, command = lambda :     vgtype.set(gtype[1][1]))
    b1.grid(row = 4, column = 2)
    b1 = tk.Radiobutton(wbdu, text=gtype[2][0], value=gtype[2][1], variable=vgtype, takefocus = True, command = lambda :     vgtype.set(gtype[2][1]))
    b1.grid(row = 5, column = 2)
    l = tk.Label(wbdu, text = '用户新信息')
    l.grid(row = 6, column = 1)
    tg_val = tk.Entry(wbdu)
    tg_val.grid(row = 6, column = 2)
    button = tk.Button(wbdu, text = '修改', command = lambda : db.alt_num(tab_name = 'user', tg_col = i2c[vgtype.get()], tg_value = tg_val.get(), key_cols = ['`uid`', '`uname`'], key_values = ['\'' + key_val.get() + '\'', '\'' + key_val.get() + '\''], conne = ['or']))
    button.grid(row = 7, column = 1)
    button = tk.Button(wbdu, text = '取消', command = lambda : shutd(wbdu))
    button.grid(row = 7, column = 2)


def alt_t():
    wbdu = tk.Tk()
    wbdu.title('修改队伍等级')
    wbdu.maxsize(800, 600)
    wbdu.minsize(600, 400)
    menu_put(wbdu)
    l = tk.Label(wbdu, text = '原队长学号或姓名')
    l.grid(row = 1, column = 1)
    key_val = tk.Entry(wbdu)
    key_val.grid(row = 1, column = 2)
    lbtype = tk.Label(wbdu, text = '参赛种类：')
    lbtype.grid(row = 2, column = 1)
    mtype = [
    ('编队赛', 0),
    ('个人赛', 1)]
    vtype = tk.IntVar()
    vtype.set(1)
    b1 = tk.Radiobutton(wbdu, text=mtype[0][0], value=0, variable=vtype, takefocus = True, command = lambda : vtype.set(0))
    b1.grid(row = 2, column = 2)
    b1 = tk.Radiobutton(wbdu, text=mtype[1][0], value=1, variable=vtype, takefocus = True, command = lambda : vtype.set(1))
    b1.grid(row = 3, column = 2)
    l = tk.Label(wbdu, text = '队伍新等级')
    l.grid(row = 6, column = 1)
    tg_val = tk.Entry(wbdu)
    tg_val.grid(row = 6, column = 2)
    button = tk.Button(wbdu, text = '修改', command = lambda : db.alt_num(tab_name = 'team', tg_col = 'tlv', tg_value = tg_val.get(), key_cols = ['(tleader', 'tleader', 'ttype'], key_values = ['\'' + key_val.get() + '\'', 'select uid from `user` where `uname` in (\'' + key_val.get() + '\')', vtype.get()], conne = ['or', ') and']))
    button.grid(row = 7, column = 1)
    button = tk.Button(wbdu, text = '取消', command = lambda : shutd(wbdu))
    button.grid(row = 7, column = 2)


def alt_m():
    wbdu = tk.Tk()
    wbdu.title('更换队员')
    wbdu.maxsize(800, 600)
    wbdu.minsize(600, 400)
    menu_put(wbdu)
    l = tk.Label(wbdu, text = '原队员学号或姓名')
    l.grid(row = 1, column = 1)
    key_val = tk.Entry(wbdu)
    key_val.grid(row = 1, column = 2)
    l = tk.Label(wbdu, text = '队号')
    l.grid(row = 2, column = 1)
    key_val1 = tk.Entry(wbdu)
    key_val1.grid(row = 2, column = 2)
    l = tk.Label(wbdu, text = '新队员学号')
    l.grid(row = 6, column = 1)
    tg_val = tk.Entry(wbdu)
    tg_val.grid(row = 6, column = 2)
    button = tk.Button(wbdu, text = '修改', command = lambda : db.alt_num(tab_name = 'ut', tg_col = 'uid', tg_value = tg_val.get(), key_cols = ['`uid`', '`tid`'], key_values = ['select uid from `user` where (`uid` = (\'' + key_val.get() + '\') or `uname` = (\'' + key_val.get() + '\'))', '\'' + key_val1.get() + '\''], conne = [ ' and']))
    button.grid(row = 7, column = 1)
    button = tk.Button(wbdu, text = '取消', command = lambda : shutd(wbdu))
    button.grid(row = 7, column = 2)


def altda():
    wbsea = tk.Tk()
    wbsea.title('更改')
    wbsea.maxsize(1080, 960)
    wbsea.minsize(800, 600)
    menu_put(wbsea)
    l = tk.Label(wbsea, text = '   ')
    l.grid(row = 0, column = 0)
    btninsuser = tk.Button(wbsea, text = '修改用户信息',command =alt_u)
    btninsuser.grid(row = 1, column = 1)
    l = tk.Label(wbsea, text = '   ')
    l.grid(row = 1, column = 2)
    btninsuser = tk.Button(wbsea, text = '修改队伍等级',command = alt_t)
    btninsuser.grid(row = 1, column = 3)
    l = tk.Label(wbsea, text = '   ')
    l.grid(row = 1, column = 4)
    btninsuser = tk.Button(wbsea, text = '修改编队队员',command = alt_m)
    btninsuser.grid(row = 1, column = 5)



entryId = 0
entrypswd = 0
wd1 = tk.Tk()
menu_put(wd1)
wd1.title('登录/注册')
lblId = tk.Label(text = '学号：')
lblId.grid(row = 0, column = 0)
entryId = tk.Entry()
entryId.grid(row = 0, column = 1)
lblpswd = tk.Label(text = '密码：')
lblpswd.grid(row = 1, column = 0)
entrypswd = tk.Entry(show = '*')
entrypswd.grid(row = 1, column = 1)
log_in()

windows = tk.Tk()
windows.title('兵推大赛信息管理')
windows.maxsize(1080, 960)
windows.minsize(1000, 618)
menu_put(windows)
l = tk.Label(text = '                                                     \n\n\n\n\n\n')
l.grid(row = 0, column = 0)
btninsuser = tk.Button(text = '添加报名信息',command = lambda : ins_user(db))
btninsuser.grid(row = 1, column = 1)
l = tk.Label(text = '   ')
l.grid(row = 1, column = 2)
btninsteam = tk.Button(text = '添加队伍信息',command = lambda : ins_team(db))
btninsteam.grid(row = 1, column = 3)
l = tk.Label(text = '   ')
l.grid(row = 1, column = 4)
btninstmember = tk.Button(text = '添加队伍队员',command = lambda : ins_ut(db))
btninstmember.grid(row = 1, column = 5)
l = tk.Label(text = '   ')
l.grid(row = 1, column = 6)
btnins = tk.Button(text = '添加比赛结果',command = lambda : ins_match(db))
btnins.grid(row = 1, column = 7)
l = tk.Label(text = '   ')
l.grid(row = 1, column = 8)
btnins = tk.Button(text = '添加比赛得分',command = lambda : ins_mr(db))
btnins.grid(row = 1, column = 9)
l = tk.Label(text = '   \n\n\n')
l.grid(row = 2, column = 0)
btnins = tk.Button(text = '查找',command = search)
btnins.grid(row = 3, column = 1)
btnins = tk.Button(text = '删除',command = delda)
btnins.grid(row = 3, column = 5)
btnins = tk.Button(text = '更改',command = altda)
btnins.grid(row = 3, column = 9)

windows.mainloop()
print('结束')