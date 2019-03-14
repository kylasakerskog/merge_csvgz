import pandas as pd
import sys

file_name = sys.argv[1] #ファイルの名前(数字を含まない)
max_file_num =  int(sys.argv[2]) #ファイルの数字の最大値
output_file_name = sys.argv[3]

df_list = []
data = pd.read_csv(file_name  + '_000000000000.csv.gz', header=None, nrows=1, compression='gzip')
columns_name = data.values.tolist() #カラム名をcsvヘッダから取ってくる

for i in range(0, max_file_num):
    i0 = str(i).zfill(12) #0埋めしたファイルの数字 i0:str型
    data = pd.read_csv(file_name + '_' + i0 + '.csv.gz', header=None, skiprows=1, compression='gzip') #ファイル名によって変更
    df_list.append(data)
#print(i) #debug

data2 = pd.concat(df_list)

data2.columns = columns_name
data2 = data2.reset_index(drop=True)

data2.to_csv(output_file_name + '.csv.gz', compression='gzip')
