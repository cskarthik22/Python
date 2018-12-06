
def reverse(strval,res):
 
    #BASE CASE:
    if(len(strval) == 0):
        print res;
    else:
    # Logic    
        res = strval[0] + res
        strval = strval[1:]
        return reverse(strval,res)

def reverse_new(strval):
 
    #BASE CASE:
    if(len(strval) <= 1):
        return strval;
    else:
    # Logic    
        return reverse_new(strval[1:]) + strval[0]

reverse('karthik','')
print(reverse_new('karthik'))








