# library
import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd

import numpy as np


import timeit 


def main():


    #versao diferente do csv, sem aspas no nome das colunas
    trans = pd.read_csv("files/trans_train_py.csv", sep=';', usecols = ['account_id', 'balance'])

    loans = pd.read_csv("files/loan_train.csv", sep=';', usecols = ['account_id', 'status'])


    trans = trans.sort_values('balance')

    trans = trans.drop_duplicates(subset = 'account_id', keep = "first")
  

    final_frame = pd.merge(loans, trans, how ='inner', on ='account_id').sort_values('balance')

    final_frame.to_csv(r'min_balance.csv', index =False)




    colors = (0,0,1)
    area = np.pi*5

    plt.scatter(final_frame["balance"], final_frame["status"], s=area, c=colors, alpha=0.5)
    plt.title('Minimum balance')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.yticks(np.arange(-1, 1, 2.0))
    plt.show()



if __name__ == '__main__':
    main()