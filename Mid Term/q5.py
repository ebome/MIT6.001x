'''
Write a Python function that returns a list of keys in aDict with the value target. 
The list of keys you return should be sorted in increasing order. The keys and values in aDict are both integers. 
(If aDict does not contain the value target, you should return an empty list.)

This function takes in a dictionary and an integer and returns a list.
 '''
def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    
    returns a list of keys in aDict with the value target
    '''
    key_list=[]
    value_list=[]
    for key,value in aDict.items():
        key_list.append(key)
        value_list.append(value)
 
    get_value_index=[]
    for elt in value_list:
        if elt==target:
            value_index = value_list.index(elt) # index() 函数用于从列表中找出某个值第一个匹配项的索引位置。
            get_value_index.append(value_index)
            value_list[value_index] = value_list[value_index]-1    # 让elt变个数字，下一次loop就不会找到index了
    
    if len(get_value_index)==0:
        return []
    
    correspond_keys=[]
    for target_index in get_value_index:
        a = key_list[target_index]
        correspond_keys.append(a)
    
    ans=sorted(correspond_keys)    
    return ans  
 # correct  
