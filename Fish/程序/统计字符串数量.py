
def statistic(x):
    word=0
    number=0
    space=0
    other=0
    for n in range (len(x)):
        for i in x[n]:
            if i.isalpha():
                word+=1
            elif i.isdigit():
                number+=1
            elif i==' ':
                space+=1
            else:
                other+=1
        print('��',n+1,'���ַ������У�',\n\
        \t 'Ӣ����ĸ',word,'��,����',\n\
        \t number,'�����ո�',space,'���������ַ�',other,'��')



##def count(*param):
##    length = len(param)
##    print(param)
##    print('length�ĳ�����',length)
##    for i in range(length): #ȷ��Ԫ����ÿһ��Ԫ�ص���ţ��Ա�����ӡ
##        letters = 0
##        space = 0
##        digit = 0
##        others = 0
##        for each in param[i]:
##            if each.isalpha():
##                letters += 1
##            elif each.isdigit():
##                digit += 1
##            elif each == ' ':
##                space += 1
##            else:
##                others += 1
##        print('�� %d ���ַ������У�Ӣ����ĸ %d �������� %d �����ո� %d ���������ַ� %d ����' % (i+1, letters, digit, space, others)) #ԭ����ʽ���ǿ�����ô�õģ��ﱤ��
        
        
    
