from rotations import rotate

def solution(n:int,pos:tuple) -> list:
    # Verify if the position is valid
    if (pos[0] >= 2**n or pos[1]>=2**n or not isinstance(pos[0],int) or not
    isinstance(pos[1],int)):
        print("Invalid input")
        return []

    # Base case
    if n == 0:
        return []

    if n == 1:
        board = [[(0,0),(0,1),(1,0),(1,1)]]
        board[0].remove(pos)
        return board

    if pos[1] < 2 ** (n - 1):
        if pos[0] < 2**(n-1):
            quad_with_space = solution(n-1,pos)
            print(quad_with_space)
            quad_to_complete = solution(n-1,(2**(n-1)-1,0))
            print(quad_to_complete)
            return ["a"]

        quad_with_space = solution(n-1,(pos[0]-2**(n-1),pos[1]))
        print(quad_with_space)
        quad_to_complete = solution(n-1, (2**(n-1)-1,2**(n-1)-1))
        print(quad_to_complete)
        return ["b"]

    if pos[0] < 2**(n-1):
        quad_with_space = solution(n-1,(pos[0],pos[1]-2**(n-1)))
        print(quad_with_space)
        quad_to_complete = solution(n-1,(0,0))
        print(quad_to_complete)
        return ["c"]

    quad_with_space = solution(n-1,(pos[0]-2**(n-1),pos[1]-2**(n-1)))
    print(quad_with_space)
    quad_to_complete = solution(n-1,(0,2**(n-1)-1))
    print(quad_to_complete)
    return ["d"]

if __name__ == "__main__":
    print(solution(3,(1,3)))