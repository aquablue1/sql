# -*-coding:utf-8-*-



import csv

csvfile = file('/Users/zhengpingzhang/Desktop/企业静态字段表.csv', 'r')
txtfile = file('/Users/zhengpingzhang/Desktop/newtable2.txt','w')
tablename = 'company_static'

# newfile = file('result.csv', 'a')
reader = csv.reader(csvfile)
for line in reader:
    # print line
    # line.remove(line[18])

    txtfile.write('insert into ')
    txtfile.write('`'+tablename+'` ')

    txtfile.write('values(')

    txtfile.write(line[0]+',')      # field  0：统一社会信用代码/企业工商注册号
    txtfile.write('\''+line[1]+'\'' + ',')
    txtfile.write('\''+line[2]+'\'' + ',')
    txtfile.write(line[3]+',')
    txtfile.write('\''+line[4]+'\'' + ',')
    txtfile.write('\''+line[5]+'\'' + ',')
    txtfile.write('\''+line[6]+'\'' + ',')
    txtfile.write(line[7]+ ',')
    txtfile.write('\''+line[8]+'\'' + ',')
    txtfile.write('\''+line[9]+'\'' + ',')
    txtfile.write('\''+line[10]+'\'' + ',')
    txtfile.write('\''+line[11]+'\'' + ',')
    txtfile.write('\''+line[12]+'\'' + ',')
    txtfile.write(line[13]+ ',')
    txtfile.write('\''+line[14]+'\'' + ',')
    txtfile.write(line[15]+ ',')
    txtfile.write('\''+line[16]+'\'' + ',')
    txtfile.write('\''+"null"+'\'' + ',')
    txtfile.write('\''+line[18]+'\'' + ',')
    txtfile.write('\''+line[19]+'\'' + ',')
    txtfile.write('\''+line[20]+'\'' + ',')
    txtfile.write(line[21]+ ',')
    txtfile.write(line[22]+ ',')
    txtfile.write(line[23]+ ',')
    txtfile.write(line[24]+ ',')


    txtfile.write(');')

    txtfile.write('\n')
    # print line

csvfile.close()