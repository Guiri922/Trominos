import numpy as np

# Rotates a position counter clockwise
def rotate(size:int, pos, times)-> tuple:
    size_tuple = (2**size-1,2**size-1)
    if times == 1:
        return tuple(np.add((-pos[1],pos[0]),size_tuple))
    if times == 2:
        return tuple(np.add((-pos[0],-pos[1]),size_tuple))
    
    # This is the case times == 3
    return tuple(np.add((pos[1], -pos[0]), size_tuple))

if __name__ == '__main__':
    print(rotate(2,(0,0),1))
    print(rotate(3,(5,0),2))