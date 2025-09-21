from rotations import rotate
import numpy as np

def solution(n:int,pos:tuple) -> list:
    pos = list(pos)
    # Verify if the position is valid
    if (pos[0] >= 2**n or pos[1]>=2**n or not isinstance(pos[0],int) or not
    isinstance(pos[1],int)):
        print("Invalid input")
        return []

    # Base case
    if n == 0:
        return []

    if n == 1:
        board = [[[0,0],[0,1],[1,0],[1,1]]]
        board[0].remove(pos)
        return board

    if pos[1] < 2 ** (n - 1):
        if pos[0] < 2**(n-1):
            quad_a = solution(n-1,pos)
            quad_c = solution(n-1,(2**(n-1)-1,0))
            quad_b = []
            quad_d = []
            for i in range(len(quad_c)):
                quad_b.append([])
                quad_d.append([])
                for j in range(len(quad_c[i])):
                    obj_d = rotate(n-1,quad_c[i][j],1)
                    quad_d[i].append([x+y for x,y in zip(obj_d,
                                                         [2**(n-1),2**(n-1)])])
                    obj_b = rotate(n-1,quad_c[i][j],2)
                    quad_b[i].append([x+y for x,y in zip(obj_b,
                                                         [2**(n-1),0])])

                    quad_c[i][j] = [x+y for x,y in zip(quad_c[i][j],
                                                       [0,2**(n-1)])]

            extra_pz = [[2**(n-1),2**(n-1)-1],
                        [2**(n-1),2**(n-1)],
                        [2**(n-1)-1,2**(n-1)]]

        else:
            quad_b = solution(n-1,(pos[0]-2**(n-1),pos[1]))
            quad_a = solution(n-1, (2**(n-1)-1,2**(n-1)-1))
            quad_c = []
            quad_d = []
            for i in range(len(quad_a)):
                quad_c.append([])
                quad_d.append([])
                for j in range(len(quad_a[i])):
                    obj_c = rotate(n-1,quad_a[i][j],1)
                    obj_d = rotate(n-1,quad_a[i][j],2)
                    quad_c[i].append([x+y for x,y in zip(obj_c,
                                                         [0,2**(n-1)])])
                    quad_d[i].append([x+y for x,y in zip(obj_d,
                                                         [2**(n-1),2**(n-1)])])

                    quad_b[i][j] = [x+y for x,y in zip(quad_b[i][j],
                                                       [2**(n-1),0])]

            extra_pz = [[2**(n-1)-1,2**(n-1)-1],
                        [2**(n-1)-1,2**(n-1)],
                        [2**(n-1),2**(n-1)]]

    elif 2**(n - 1) > pos[0]:
        quad_c = solution(n-1,(pos[0],pos[1]-2**(n-1)))
        quad_d = solution(n-1,(0,0))
        quad_b = []
        quad_a = []
        for i in range(len(quad_d)):
            quad_b.append([])
            quad_a.append([])
            for j in range(len(quad_d[i])):
                obj_b = rotate(n-1,quad_d[i][j],1)
                quad_b[i].append([x+y for x,y in zip(obj_b,
                                                     [2**(n-1),0])])
                quad_a[i].append(rotate(n-1,quad_d[i][j],2))

                quad_c[i][j] = [x+y for x,y in zip(quad_c[i][j],
                                                   [0,2**(n-1)])]

                quad_d[i][j] = [x+y for x,y in zip(quad_d[i][j],
                                                   [2**(n-1), 2**(n-1)])]

            extra_pz = [[2**(n-1)-1,2**(n-1)-1],
                        [2**(n-1),2**(n-1)-1],
                        [2**(n-1),2**(n-1)]]


    else:
        quad_d = solution(n-1,(pos[0]-2**(n-1),pos[1]-2**(n-1)))
        quad_b = solution(n-1,(0,2**(n-1)-1))
        quad_a = []
        quad_c = []
        for i in range(len(quad_b)):
            quad_a.append([])
            quad_c.append([])
            for j in range(len(quad_b[i])):
                obj_c = rotate(n-1,quad_b[i][j],2)
                quad_a[i].append(rotate(n-1,quad_b[i][j],1))
                quad_c[i].append([x+y for x,y in zip(obj_c,
                                                     [0,2**(n-1)])])

                quad_b[i][j] = [x+y for x,y in zip(quad_b[i][j],
                                                   [2**(n-1),0])]

                quad_d[i][j] = [x+y for x,y in zip(quad_d[i][j],
                                                   [2**(n-1),2**(n-1)])]

            extra_pz = [[2**(n-1)-1,2**(n-1)-1],
                        [2**(n-1),2**(n-1)-1],
                        [2**(n-1)-1,2**(n-1)]]

    return quad_a + quad_b + quad_c + quad_d + [extra_pz]

if __name__ == "__main__":
    print(np.array(solution(4,(5,2))))
    print(np.array(solution(4,(5,2))).shape)