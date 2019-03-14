import pandas as pd
import sys
import csv
import gzip

file_name = sys.argv[1] #ファイルの名前(数字を含まない)
max_file_num =  int(sys.argv[2]) #ファイルの数字の最大値
output_file_name = sys.argv[3]
newline = '\n'

rh = gzip.open(file_name  + '_000000000000.csv.gz', 'rt', "utf-8")
#reader = csv.reader(rh)
header = rh.readline()
rh.close()

data = gzip.compress(header.encode("utf-8"))
wh = gzip.open(output_file_name+'.csv.gz', mode='wb')
wh.write(data)
wh.close()

for i in range(0, max_file_num + 1):
    i0 = str(i).zfill(12)
    r = gzip.open(file_name  + '_' + i0 + '.csv.gz', 'rt', "utf-8")
    #reader = csv.reader(r)
    header = r.readline()
    lines = r.readlines()
    r.close()
    w = gzip.open(output_file_name+'.csv.gz', mode='ab')
    for row in lines:
        w.write(gzip.compress(row.encode("utf-8")))
    #print(row)
    w.write(gzip.compress(newline.encode("utf-8")))
    w.close()

