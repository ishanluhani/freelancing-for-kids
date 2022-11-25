import time, random, pyautogui, pyttsx3
from threading import Thread
from win10toast import ToastNotifier

n = ToastNotifier()


def get_order():
    while True:
        time.sleep(random.randint(2400, 9000))
        orders.append(random.choice(order_list)[4:])
        n.show_toast('You got a order', 'go and complete your order when possible')

points = 0
orders = []
order_list = open('data.txt').read().split(',')
order_data_unchanged = open('point_data.txt')
a = Thread(target=get_order)
a.start()
while True:
    print('-'*30)
    print('What do you want to access')
    print('0: Load Progress')
    print('1: Your Points')
    print('2: Your Orders')
    print('3: Quit')
    main_selection = input()
    print('-' * 30)
    if main_selection == '0':
        points = int(order_data_unchanged.readline())
        orders = order_data_unchanged.readline().split(',')
    elif main_selection == '1':
        print(f'Your Points: {points}')
    elif main_selection == '2':
        for i, x in enumerate(orders):
            print(f'{i}: {x}')
        print('-' * 30)
        if input('Want to complete any order (Yes or No): ').lower() == 'yes':
            inp = int(input('Which Order: '))
            print('Submit a Photo Proof')
            print("Switch to problem's submission tab in 10 seconds")
            time.sleep(10)
            if pyautogui.locateOnScreen('Screenshot 2022-11-25 221246.png') and len(orders) != 0:
                print('Accepted, Your points have been updated')
                pyttsx3.speak('Accepted')
                points += 10
                orders.remove(orders[inp])
            else:
                pyttsx3.speak('Decline')
                points -= 5
    elif main_selection == '3':
        order_data = open('point_data.txt', 'w')
        order_data.write(f'{points}\n{",".join(orders)}')
        order_data.close()
        quit()
