import numpy as np

def solution(operations):
    lists = []
    for op in operations:
        if op == 'D 1': 
            try: del lists[np.argmax(lists)] 
            except: pass
        elif op == 'D -1': 
            try: del lists[np.argmin(lists)] 
            except: pass
        else: lists.append(int(op.split(' ')[-1]))
    try: return [max(lists), min(lists)]
    except: return[0,0]