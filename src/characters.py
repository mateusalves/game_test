from time import sleep
import sys, select, os
import select


class Character():
    def __init__(self, name):
        self.name = name

    def intro(self):
        pass

    def talk(self, msg, dramatic_pause=0.05):
        print(f"[{self.name}]: ", end='')
        for char in msg:
            print(char, end='')
            sys.stdout.flush()
            sleep(dramatic_pause)
            if char in ['?', '.', '!']:
                sleep(0.4)
            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                os.system('clear') #unix only
                _line = input()
                print(f"[{self.name}]: ", end='')
                print(msg, end='')
                break
        print('\n')
        sleep(1)

    def battle(self):
        pass

    def defeated(self):
        pass

    def victorious(self):
        pass


