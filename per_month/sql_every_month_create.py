# -*-coding:utf-8-*-


import csv

csvfile = file('/Users/zhengpingzhang/Desktop/yiwuqiyemeiyue.csv', 'r')
txtfile = file('/Users/zhengpingzhang/Desktop/newtable.txt','w')
tablename = 'per_month_company'

# newfile = file('result.csv', 'a')
reader = csv.reader(csvfile)
for line in reader:
    # print line
    # line.remove(line[18])
    txtfile.write('insert into ')
    txtfile.write('`'+tablename+'` ')

    txtfile.write('values(')

    txtfile.write(line[0]+',')      # field  0：统一社会信用代码/企业工商注册号
    txtfile.write('\''+line[1]+'\'' + ',')    # field 1:企业名称
    txtfile.write('\''+line[2]+'\'' + ',')      # field 2:统计月份
    txtfile.write(line[3] + ',')    #field 3:利润总额    #(万元)
    txtfile.write(line[4]+',')      #field 4:纳税总额    #(万元)
    txtfile.write(line[5] + ',')    #field 5:税后工资总额  #（万元）
    txtfile.write(line[6]+',')      #field 6:月初固定资产总额  #(万元)
    txtfile.write(line[7] + ',')    #field 7:月末固定资产总额  #(万元)
    txtfile.write(line[8]+',')      #field 8:社保增加总额   #（万元）
    txtfile.write(line[9] + ',')    #field 9:用水费用  #(万元)
    txtfile.write(line[10]+',')      #field 10:用电费用 #(万元)
    txtfile.write(line[11] + ',')    #field 11:用地费用  #(万元)
    txtfile.write(line[12]+',')      #field 12:排污费用 #(万元)
    txtfile.write(line[13] + ',')    #field 13:贷款融资总额  #（万元）
    txtfile.write(line[14]+',')      #field 14:员工风险  #（分）
    txtfile.write(line[15] + ',')    #field 15:火灾风险   #（分）
    txtfile.write(line[16]+',')      #field 16:资产风险  #（分）
    txtfile.write(line[17])    #field 17:健康指数  #（分）

    txtfile.write(');')

    txtfile.write('\n')
    # print line

csvfile.close()