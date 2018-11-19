import DataProcess

q=1
while q!=4:
    print('####################数据库操作####################')
    print("1:建立数据库\t2:添加数据\t3:导出数据\t4:退出")
    q = int(input('请选择所需操作:\n'))
    if q == 1:
        DataProcess.Builtdatabase()
        print("#####数据库建立完成#######")
        q=0
    elif q == 2:
        f = open('AlreadyIn.txt', 'a')
        print("################数据库扩容操作################")
        a = int(input('请输入起始视频号:\n'))
        b = int(input("请输入终止视频号:\n"))
        for i in range(a, b):
            try:
                DataProcess.InsertData(i)
            except:
                pass
        print("导入数据完成")
        f.write('%d\t%d\n' % (a, b))
        f.close()
        q=0

    elif q == 3:
        print('####################数据库导出操作####################')
        aiv = int(input('请输入视频编号：\n'))
        l = DataProcess.ExportData(aiv)
        print(l)
        print('导出数据完成')
        q=0