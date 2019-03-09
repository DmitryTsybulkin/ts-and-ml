import pandas as pd
import vk
from matplotlib import pyplot as plt
from pandas.plotting import scatter_matrix

df = pd.read_csv('litecoin_csv.csv', sep=',')

df = df.dropna()

df = df.drop(columns=['medianFee', 'blockCount', 'fees'])

# login = 'tsydimon@mail.ru'
# password = 'r6v9R86ret0R'
# app_id = '6658100'
#
# session = vk.AuthSession(app_id=app_id, user_login=login, user_password=password, scope='wall, messages')
#
# vkapi = vk.API(session)

