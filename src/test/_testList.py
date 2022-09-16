data = [[1,2,3],[],[],[4],[5]]


def resizeList(list, width,height):
    for i in range(width):
        
        if i >= len(list):
            list.append([])
            
        tmp = list[i]
            
        for j in range(height):
            if j >= len(tmp):
                tmp.append(None)
    return list

dat = resizeList(data,1,3)

print(len(data))
print(len(data[0]))

for d in data:
    print(d)

##print( dir(data) )