'''
Created on May 14, 2015

@author: rogier
'''
class unique_element:
    def __init__(self, value, occurrences):
        self.value = value
        self.occurrences = occurrences

def permutations_unique(elements):
        eset=set(elements)
        listunique = [unique_element(i,elements.count(i)) for i in eset]
        u=len(elements)
        return __permutations_unique_helper(listunique,[0]*u,u-1)
    
def __permutations_unique_helper(listunique,result_list,d):
    if d < 0:
        yield tuple(result_list)
    else:
        for i in listunique:
            if i.occurrences > 0:
                result_list[d]=i.value
                i.occurrences-=1
                for g in __permutations_unique_helper(listunique,result_list,d-1):
                    yield g
                i.occurrences+=1