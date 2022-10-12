import datetime
import threading
import win10toast_click
import os
import simpleaudio as sa


class Alarm:
    def __init__(self, hour, minute, type_sound=1):
        self.__toaster = win10toast_click.ToastNotifier()
        self.__type = type_sound
        self.__stop = False
        self.__dt = datetime.datetime.today()
        self.set_hour(hour)
        self.set_minute(minute)
        self.set_type(type_sound)

    def play(self):
        self.__stop = True
        while True:
            if self.__stop:
                wave_obj = sa.WaveObject.from_wave_file(f'sounds/{self.__type}.wav')
                play_obj = wave_obj.play()
                self.__toaster.show_toast(f"{self.__dt.hour}:{self.__dt.minute}", "Нажмите чтобы отключить",
                                          icon_path=None, duration=None,
                                          threaded=True, callback_on_click=lambda: self.stop(play_obj))
                play_obj.wait_done()
            else:
                break

    def stop(self, *arr):
        self.__stop = False
        arr[0].stop()

    def set_type(self, type_sound):
        pass

    def set_hour(self, hour):
        pass

    def set_minute(self, minute):
        pass

    def get_type(self):
        return self.__type

    def get_hour(self):
        return self.__dt.hour

    def get_minute(self):
        return self.__dt.minute

    def check_time(self):
        dt_sys = datetime.datetime.today()
        return self.__dt.hour == dt_sys.hour and \
               self.__dt.minute == dt_sys.minute

    def __str__(self):
        return f'Будильник {self.__dt.hour}:{self.__dt.minute}'


def check_set_alarms(alarm, alarms_list):
    for al in alarms_list:
        if al.get_hour() == alarm.get_hour() and al.get_minute() == alarm.get_minute():
            return True

    return False


def check_alarm_times(alarms_list):
    while True:
        for alarm in alarms_list:
            if alarm.check_time():
                alarm.play()
                alarms_list.remove(alarm)
                break


def print_alarms(alarms_list):
    for i in range(len(alarms_list)):
        print(f'{i+1}.{alarms_list[i]}')


def print_menu():
    print("Выберите действие:\n "
          "1.Поставить будильник\n "
          "2.Вывести список установленных будильников\n "
          "3.Отключить будильник\n "
          "0.Выход\n "
          "Выбор: ", end="")


def main():
    alarms_list = []
    thr = threading.Thread(target=lambda: check_alarm_times(alarms_list)).start()
    menu = True
    while menu:
        print_menu()
        choice = input()

        if choice == '1':
            hour, minute = map(int, input("Введите время будильника(формат: 'часы' 'минуты'): ").split())
            type = int(input('Выберите мелодию:\n 1.Мелодия 1\n 2.Мелодия 2\n 3.Мелодия 3\nВыбор:'))
            alarm = Alarm(hour, minute, type)
            if check_set_alarms(alarm, alarms_list):
                print(f'{alarm} уже установлен')
            else:
                alarms_list.append(alarm)
                print(f'{alarm} успешно установлен')
        elif choice == '2':
            if alarms_list:
                print_alarms(alarms_list)
            else:
                print('Нет установленных будильников')
        elif choice == '3':
            if alarms_list:
                print_alarms(alarms_list)
                del_choice = int(input('Выберите будильник для отключения:'))
                if 0 < del_choice <= len(alarms_list):
                    del alarms_list[del_choice - 1]
                    print('Будильник успешно отключен')
                else:
                    if len(alarms_list) == 1:
                        print('Доступен только один будильник для отключения. Выберите 1')
                    else:
                        print(f'Выбор должен быть в диапазоне: 1 - {len(alarms_list)}')
            else:
                print('Нет установленных будильников')
        elif choice == '0':
            menu = False
            os._exit(0)


if __name__ == '__main__':
    main()
