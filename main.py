import time, random, pyautogui, pyttsx3, warnings
from threading import Thread
from win10toast import ToastNotifier

n = ToastNotifier()


def get_order():
    while True:
        if not break_:
            time.sleep(random.randint(1500, 8900))
            if random.randint(1, 10) == 1:
                n.show_toast('You received VIP a order')
                pyttsx3.speak('You received; a VIP; order')
                orders_vip.append(random.choice(hard_order_list)[4:])
            else:
                pyttsx3.speak('You received; a order')
                orders_vip.append(random.choice(order_list)[4:])

points = 0
orders = []
orders_vip = []
break_ = False
order_list = open('data.txt').read().split(',')
hard_order_list = open('data_for_me.txt').read().split(',')
order_data_unchanged = open('point_data.txt')
a = Thread(target=get_order)
a.start()
warnings.filterwarnings("module")
while True:
    print('-'*30)
    print('What do you want to access')
    print('0: Load Progress')
    print('1: Your Points')
    print('2: Your Orders')
    print('3: Take a break')
    print('4: Quit')
    main_selection = input()
    print('-' * 30)
    if main_selection == '0':
        points = int(order_data_unchanged.readline())
        orders = order_data_unchanged.readline().split(',')
    elif main_selection == '1':
        print(f'Your Points: {points}')
    elif main_selection == '2':
        for i, x in enumerate(orders):
            print(f'{i}: {x}, link: https://www.codechef.com/problems/{x}')
        print('-' * 15, 'VIP', '-' * 15)
        for i, x in enumerate(orders_vip):
            print(f'{i}: {x}, link: https://www.codechef.com/problems/{x}')
        print('-' * 30)
        if input('Want to complete any order (Yes or No): ').lower() == 'yes':
            inp = int(input('Which Order: '))
            i = input('is it VIP: ').lower()
            print('Submit a Photo Proof')
            print("Switch to problem's submission tab in 10 seconds")
            time.sleep(10)
            if pyautogui.locateOnScreen('Screenshot 2022-11-25 221246.png') and len(orders) != 0:
                print('Accepted, Your points have been updated')
                pyttsx3.speak('Accepted')
                if i == 'yes':
                    points += 20
                    orders_vip.remove(orders_vip[inp])
                else:
                    points += 10
                    orders.remove(orders[inp])
            else:
                pyttsx3.speak('Decline')
            if i == 'yes':
                points -= 20
            else:
                points -= 5
    elif main_selection == '3':
        break_ = not break_
    elif main_selection == '4':
        order_data = open('point_data.txt', 'w')
        order_data.write(f'{points}\n{",".join(orders)}')
        order_data.close()
        quit()
