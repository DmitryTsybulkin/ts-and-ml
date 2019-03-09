import random as rand
import datetime as dt
from collections import OrderedDict


class Trader:
    def __init__(self, start_sum, start_price, actives):
        self.start_sum = start_sum
        self.start_price = start_price
        self.actives = actives

    def actions(self, history, current_sum, current_price, old_price):
        if current_price <= current_sum or self.actives != 0:
            if self.actives != 0 and current_sum < 20:
                return self.sellOne(current_sum, current_price)
            elif current_sum >= current_price:
                return self.buyOne(current_sum, current_price)
        return current_sum


    def is_future_increase(self, history, current_price):
        if len(history) == 0 or len(history) == 1:
            return False
        else:
            general = 0
            for i in history.values():
                general += i
            return general / len(history.values()) > current_price


    def is_future_decrease(self, history, current_price):
        if len(history) == 0 or len(history) == 1:
            return False
        else:
            general = 0
            for i in history.values():
                general += i
            return general / len(history.values()) < current_price


    def buyOne(self, current_sum, current_price):
        self.actives += 1
        return current_sum - current_price


    def sellOne(self, current_sum, current_price):
        self.actives -= 1
        return current_sum + current_price


    def generate_random(self):
        return round(rand.uniform(40, 70), 5)


    def trade(self):
        history = OrderedDict()
        current_sum = self.start_sum
        i = 0
        while i != 20:
            current_price = self.generate_random()
            history[dt.datetime.now()] = current_price
            if len(history) == 0:
                old_price = current_price
            else:
                old_price = list(history.values())[-1]
            # print(str(old_price) + ' ' + str(current_price) + ' ' + str(current_sum))
            current_sum = self.actions(history, current_sum, current_price, old_price)
            print('Price = ' + str(current_price))
            print('Sum = ' + str(current_sum))
            print('Actives = ' + str(self.actives))
            print('i = ' + str(i))
            if current_sum > 100.0:
                print('We are rich')
                break
            if i == 5 and current_sum < 30.0:
                print('We are poor')
                break
            i += 1