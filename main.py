from net import enable_reconnect,disable_reconnect
from apscheduler.schedulers.background import BackgroundScheduler

def show_menu(stat):
    print('自动重连脚本')
    print('当前状态：',end = '')
    if stat == 0: 
        print('自动重连已关闭')
    else:
        print('自动重连已开启')
    print('------------------')
    print('[1] 开启自动重连')
    print('[2] 关闭自动重连')
    print('[3] 状态查询')

def check_stat(sched):
    if sched.get_job('reconnect'):
        return 1
    else:
        return 0
        
if __name__ == '__main__':
    sched = BackgroundScheduler()
    show_menu(check_stat(sched))
    while 1:
        select = input('>> ')
        if not (select == '1' or select == '2' or select == '3'):
            print('输入有误')
            continue
        elif select == '1':
            enable_reconnect(sched)
        elif select == '2':
            disable_reconnect(sched)
        elif select == '3':
            show_menu(check_stat(sched))