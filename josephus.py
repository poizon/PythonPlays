#
"""
1-й круг: 1 2 (3) 4 5 (6) 7 8 (9) 10
2-й круг:                            1 (2) 4 5 (7) 8 10
3-й круг:                                                (1) 4 5 (8) 10
4-й круг:                                                               4 (5) 10
5-й круг:                                                                        4 (10)
"""

def kill_3d (ppls):
    if len(ppls) == 1:
        return (ppls)

    result = list(set(ppls[::13]) ^ set(ppls))
    result.reverse()    
    return(kill_3d(result))

army = list(range(0,72))
print (kill_3d(army)[0])
