def balance_checks(s):

    if len(s)%2 != 0:
        return False
    


    items = []
    opening = set('[{(')
    #match = {'[':']', '{':'}', '(':')'}
    matches = [('(',')'),('[',']'),('{','}')]

    for ch in s:

        #if ch == '[' or ch == '{' or ch == '(':
        if ch in opening: 
            items.append(ch)
        else:
            if len(items)==0:
                return False
            last_open = items.pop()
            if (last_open,ch) not in matches:
                return false
  
    if items == []:
        return True
    
print(balance_checks('({}{}{[][]})'))




        
         
             





