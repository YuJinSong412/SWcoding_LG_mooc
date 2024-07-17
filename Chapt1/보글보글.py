dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

def in_range(x, y):
    return 0 <= x < 5 and 0 <= y < 5

def has_word(board, x, y, word):
    if board[x][y] != word[0]:
        return False
   
    if len(word) == 1:
        return True
   
    temp, board[x][y] = board[x][y], '#'
   
    for direction in range(8):
        nx, ny = x + dx[direction], y + dy[direction]
        if in_range(nx, ny) and has_word(board, nx, ny, word[1:]):
            return True
   
    board[x][y] = temp
    return False

def find_word(board, word):
    for x in range(5):
        for y in range(5):
            if has_word(board, x, y, word):
                return True
    return False


board = [
    ['U', 'R', 'L', 'P', 'M'],
    ['X', 'P', 'R', 'E', 'T'],
    ['G', 'I', 'A', 'E', 'T'],
    ['X', 'T', 'N', 'Z', 'Y'],
    ['X', 'O', 'Q', 'R', 'S']
]

word = "PRETTY"
print(find_word(board, word))