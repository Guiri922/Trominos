# Rotates a position counter clockwise
def rotate(size:int, pos, times)-> list:
    size_tuple = [2**size-1,2**size-1]
    if times == 1:
        return [x+y for x,y in zip([pos[1],-pos[0]],[0,2**size-1])]

    if times == 2:
        return [x+y for x,y in zip([-pos[0],-pos[1]],size_tuple)]

    return []

if __name__ == '__main__':
    print(rotate(2,(0,0),1))
    print(rotate(3,(5,0),2))