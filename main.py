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
            
        sys.stdout.write('\r[' + c + '] Attacking')
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
            print('[*] waiting for 20 seconds')
            print('[*] waiting')
            time.sleep(20)
            print('[*] succeed')
        elif command == 'restart':
            print('[*] restarting')
            done = True
            time.sleep(5)
            done = False
            print('[*] restart succeed')
        elif command == 'timeout':
            done = True
            print('[*] waiting for 5 seconds')
            print('[*] waiting')
            time.sleep(5)
            print('[*] succeed')
        elif command == 'timeout_10':
            print('[*] waiting for 10 seconds')
            print('[*] waiting')
            time.sleep(10)
            print('[*] succeed')
        elif command == 'timeout_5':
            done = True
            print('[*] waiting for 5 seconds')
            print('[*] waiting')
            time.sleep(5)
            print('[*] succeed')
        elif command == 'help':
            print('[*] Commands:\ntimeout\ntimeout_5\ntimeout_10\ntimeout_20\nexit\nquit\nrestart')
        elif command == 'h':
            print('[*] Commands:\ntimeout\ntimeout_5\ntimeout_10\ntimeout_20\nexit\nquit\nrestart')
        else:
            print('[*] Unknown Command type help to get a list of commands')
cmd = threading.Thread(target=command)
        
me = sys.argv

fromaddrs = input(str('[*] Enter you gmail address: '))
while len(fromaddrs) == 0:
    fromaddrs = input(str('[*] Enter you gmail address: '))

    
toaddrs = input(str('[*] Enter the gmail address that you want to spam: '))
while len(toaddrs) == 0:
    toaddrs = input(str('[*] Enter the gmail address that you want to spam: '))

    
message = input(str('[*] Enter the message that you are going to spam: '))
while len(message) == 0:
    message = input(str('[*] Enter the message that you are going to spam: '))

apppass = input(str('[*] Enter your application password(https://support.google.com/accounts/answer/185833?hl=en): '))
while len(apppass) == 0:
    apppass = input(str('[*] Enter your application password(https://support.google.com/accounts/answer/185833?hl=en): '))


times = input('[*] How many time you want to spam(-1 = forever): ')
while len(times) == 0:
    times = input('[*] How many time you want to spam(-1 = forever): ') 
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
                    print(f'\r[*] Spamed {i} times')


            elif times == -1:
                i = -1
                while True:
                    i += 1
                    th = threading.Thread(target=animate)
                    th.start()
                    smtpserver.sendmail(fromaddrs, toaddrs, message)
                    print(f'\r[*] Spamed {i}')


    except smtplib.SMTPSenderRefused:
        print('\n[Warning] Server Rejected to sent gmail(attempt to block spam)(SMTPSenderRefused), Retrying in next 20 seconds')
        done = True
        print('[*] Waiting')
        time.sleep(20)
        loop = 1
    except smtplib.SMTPServerDisconnected:
        print('\n[Warning] Server Disconnected our reqest(SMTPServerDisconnected), Retrying')
        print('[*] Waiting')
        time.sleep(1)
        loop = 1
    except KeyboardInterrupt:
        print('\n[*] KeyboardInterrupt')
        done = True
        sys.exit()
        exit()
    except smtplib.SMTPDataError:
        print('\n[ERROR] Sending Error Data(SMTPDataError) or Server is attempting to block spam, Retrying')
        print('[*] Waiting')
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
                            print(f'\r[*] Spamed {i}')
                        break


                    elif times == -1:
                        i = -1
                        while True:
                            i += 1
                            th = threading.Thread(target=animate)
                            th.start()
                            smtpserver.sendmail(fromaddrs, toaddrs, message)
                            print('\r[*] Spamed', i)
                    if might_limit >= 150:
                        print('[Warning] You might rate the daily limit of SMTP gmail sender')
                        print('[Warning] You might rate the daily limit of SMTP gmail sender')
                        print('[Warning] You might rate the daily limit of SMTP gmail sender')


            except smtplib.SMTPSenderRefused:
                print('\n[Warning] Server Rejected to sent gmail(attempt to block spam)(SMTPSenderRefused), Retrying in next 20 seconds')
                done = True
                print('[*] Waiting')
                time.sleep(20)
                done = False
                loop = 1
            except smtplib.SMTPServerDisconnected:
                print('\n[Warning] Server Disconnected our reqest(SMTPServerDisconnected), Retrying')
                print('[*] Waiting')
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
                print('\n[ERROR] Sending Error Data(SMTPDataError) or Server is attempting to block spam, Retrying')
                done = True
                might_limit = 0
                might_limit += 1
                print('[*] Waiting')
                time.sleep(1)
                done = False
                loop = 1

                
                    
done = True
sys.exit()
exit()

# Gmail Spammer script ends
