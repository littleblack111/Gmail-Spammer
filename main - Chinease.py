from email import message
import smtplib
import sys
from time import time
import time
import sys
import itertools
import threading

done = False

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
            
        sys.stdout.write('\r[' + c + '] 攻击中')
        sys.stdout.flush()
        time.sleep(0.1)

def command():
    while True:
        command = input('\n>>>')
        if command == 'exit' or 'q' or 'quit' or 'ex' or 'stop':
            done = True
            sys.exit()
            exit()
        elif command == 'timeout_20':
            done = True
            print('[*] 等待二十秒')
            print('[*] 等待中')
            time.sleep(20)
            print('[*] 成功')
        elif command == 'restart':
            print('[*] 正在重启')
            done = True
            time.sleep(5)
            done = False
            print('[*] 重启成功')
        elif command == 'timeout':
            done = True
            print('[*] 等待五秒')
            print('[*] 等待中')
            time.sleep(5)
            print('[*] 成功')
        elif command == 'timeout_10':
            print('[*] 等待十秒')
            print('[*] 等待中')
            time.sleep(10)
            print('[*] 成功')
        elif command == 'timeout_5':
            done = True
            print('[*] 等待五秒')
            print('[*] 等待中')
            time.sleep(5)
            print('[*] 成功')
        else:
            print('[*] 无效指令')
cmd = threading.Thread(target=command)
        
me = sys.argv

fromaddrs = input(str('[*] 请输入自己的邮箱: '))
while len(fromaddrs) == 0:
    fromaddrs = input(str('[*] 请输入自己的邮箱: '))

    
toaddrs = input(str('[*] 请输入要"发给"的人: '))
while len(toaddrs) == 0:
    toaddrs = input(str('[*] 请输入要"发给"的人: '))

    
message = input(str('[*] 请输入信息: '))
while len(message) == 0:
    message = input(str('[*] 请输入信息: '))

apppass = input(str('[*] 请输入应用专用密码: '))
while len(apppass) == 0:
    apppass = input(str('[*] 请输入应用专用密码: '))


times = input('[*] 发送多少次(-1 = 永久): ')
while len(times) == 0:
    times = input('[*] 发送多少次(-1 = 永久): ') 
times = int(times)
loop = 0
cmd.start()


while loop == 0:
    try:
        with smtplib.SMTP('smtp.gmail.com', '587') as smtpserver:
            done = False
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo()
            smtpserver.login(fromaddrs, apppass)
            if times >= 0:
                for i in range(times):
                    th = threading.Thread(target=animate)
                    th.start()
                    smtpserver.sendmail(fromaddrs, toaddrs, message)
                    print(f'\r[*] 发送了 {i}')


            elif times == -1:
                i = -1
                while True:
                    i += 1
                    th = threading.Thread(target=animate)
                    th.start()
                    smtpserver.sendmail(fromaddrs, toaddrs, message)
                    print('\r[*] 发送了', i)


    except smtplib.SMTPSenderRefused:
        print('\n[警告] 服务器 拒绝了发送请求(SMTPSenderRefused), 20秒后重试')
        done = True
        print('[*] 等待中')
        time.sleep(20)
        loop = 1
    except smtplib.SMTPServerDisconnected:
        print('\n[警告] 服务器 断开了发送请求的连接(SMTPServerDisconnected), 正在重试')
        print('[*] 等待中')
        time.sleep(1)
        loop = 1
    except KeyboardInterrupt:
        print('\n[*] KeyboardInterrupt')
        done = True
        sys.exit()
        exit()
    except smtplib.SMTPDataError:
        print('\n[错误] 数据异常(SMTPDataError) 或 服务商 拒绝了发送请求, 即将重试')
        print('[*] 等待中')
        time.sleep(1)
        loop = 1
            
    while loop == 1:
        while True:
            try:
                with smtplib.SMTP('smtp.gmail.com', '587') as smtpserver:
                    loop = 0
                    done = False
                    smtpserver.ehlo()
                    smtpserver.starttls()
                    smtpserver.ehlo()
                    smtpserver.login(fromaddrs, apppass)
                    if times >= 0:
                        for i in range(times):
                            th = threading.Thread(target=animate)
                            th.start()
                            smtpserver.sendmail(fromaddrs, toaddrs, message)
                            print(f'\r[*] 发送了 {i}')


                    elif times == -1:
                        i = -1
                        while True:
                            i += 1
                            th = threading.Thread(target=animate)
                            th.start()
                            smtpserver.sendmail(fromaddrs, toaddrs, message)
                            print(f'\r[*] 发送了 {i}')
                    if might_limit >= 150:
                        print('[警告] 你可能已经到达每天发送限制的极限了')
                        print('[警告] 你可能已经到达每天发送限制的极限了')
                        print('[警告] 你可能已经到达每天发送限制的极限了')


            except smtplib.SMTPSenderRefused:
                print('\n[警告] 服务器 拒绝了发送请求(SMTPSenderRefused), 20秒后重试')
                done = True
                print('[*] 等待中')
                time.sleep(20)
                done = False
                loop = 1
            except smtplib.SMTPServerDisconnected:
                print('\n[警告] 服务器 断开了发送请求的连接(SMTPServerDisconnected), 正在重试')
                print('[*] 等待中')
                done = True
                cmd.start()
                time.sleep(1)
                done = False
                loop = 1
            except KeyboardInterrupt:
                print('\n[*] KeyboardInterrupt')
                done = True
                sys.exit()
            except smtplib.SMTPDataError:
                print('\n[错误] 数据异常(SMTPDataError) 或 服务器 拒绝了发送请求, 即将重试')
                done = True
                might_limit = 0
                might_limit += 1
                print('[*] 等待中')
                time.sleep(1)
                done = False
                loop = 1

 
 
done = True
sys.exit()
exit()
# Gmail Spammer script ends
