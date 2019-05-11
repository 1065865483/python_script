import csv
# f=open('stu_info.txt','r')
# lines=f.readlines()
# print(lines)
#
# for line in lines:
#     print(line.split(',')[0],line.split(',')[1],line.split(',')[2])


# csv_file=csv.reader(open('stu_info.csv','r'))
# print(csv_file)
#
# for stu in csv_file:
#     print(stu)

stu=['herry','28','henan']
stu1=['rom','20','chengdu']
# 打开文件
out=open('stu_info.csv','w',newline='')
# 设定写入模式
csv_write=csv.writer(out,dialect='excel')
#写入具体内容
csv_write.writerow(stu)
csv_write.writerow(stu1)
print("write over")
