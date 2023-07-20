
def menu() -> int:
    main_menu = ''':Главное меню
    1. Расчет размещения
    2. БО ограждения
    3. БО изоляции холодного коридора
    4. БО системы мониторинга питания
    5. БО системы видеонаблюдения
    6. Выход'''
    print(main_menu)
    while True:
        select = input('Выберете пункт меню: ')
        if select.isdigit() and 0<int(select)<9:
            return int(select)
        print('Ошибка ввода, ввдите число от 1 до 8')

# def colo(n):
#     написать функцию

def cage(n):
    start_money = 87000
    fin_money = start_money * n
    print('='*192 +'\n')
    print(f'БО ограждения для {n} стоек = {fin_money}р. с НДС')
    print('='*192 +'\n')

def insulation(n):
    start_money = 30000
    fin_money = start_money * n
    print('='*192 +'\n')
    print(f'БО изоляции холодного коридора для {n} стоек = {fin_money}р. с НДС')
    print('='*192 +'\n')

def mon(n):
    ports = n*2
    if ports<49:
        commut_small=2
    elif ports%24 ==0:
        commut_small=ports/24
    else:
        commut_small = ports//24+1
    if commut_small<25:
        commut_big=1
    elif commut_small%24 ==0:
        commut_big=commut_small/24
    else:
        commut_big=commut_small//24+1
    cs_cost = commut_small* 39000
    cb_cost = commut_big* 67000
    all_cost_start = 30000
    all_cost=all_cost_start*n
    cost= cs_cost + cb_cost + all_cost
    print('='*192 +'\n')
    print(f'БО на организацию системы мониторинга питания для {n} стоек = {cost}р. с НДС')
    print('='*192 +'\n')

    



server_cabinet = int(input('Введите необходимое количество шкафов: '))

while True:
    select = menu()
    match select:
        case 1:
            pass
        case 2:
            cage(server_cabinet)
        case 3:
            insulation(server_cabinet)
        case 4:
            mon(server_cabinet)
        case 5:
            pass
        case 6:
            print('До свидания!')
            break