# Runtime: 36 ms, faster than 95.38% of Python3 online submissions for Game of Life.
# Memory Usage: 13.1 MB, less than 5.79% of Python3 online submissions for Game of Life.
# 时间复杂度O(N^2)，空间复杂度O(1)。
class Solution:
    def gameOfLife(self, board: 'List[List[int]]') -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                live_num = 0
                if i-1 >= 0:
                    if board[i - 1][j] == 1 or board[i - 1][j] == 3:
                        live_num += 1
                    if j-1 >= 0:
                        if board[i-1][j-1] == 1 or board[i-1][j-1] == 3:
                            live_num += 1
                    if j+1 < len(board[0]):
                        if board[i-1][j+1] == 1 or board[i-1][j+1] == 3:
                            live_num += 1
                if i+1 < len(board):
                    if board[i + 1][j] == 1 or board[i+1][j] == 3:
                        live_num += 1
                    if j-1 >= 0:
                        if board[i+1][j-1] == 1 or board[i+1][j-1] == 3:
                            live_num += 1
                    if j+1 < len(board[0]):
                        if board[i+1][j+1] == 1 or board[i+1][j+1] == 3:
                            live_num += 1
                if j-1 >= 0 and (board[i][j - 1] == 1 or board[i][j - 1] == 3):
                    live_num += 1
                if j+1 < len(board[0]) and (board[i][j + 1] == 1 or board[i][j + 1] == 3):
                    live_num += 1

                if live_num < 2 or live_num > 3:
                    if board[i][j] == 1:
                        board[i][j] = 3
                if live_num == 3 and board[i][j] == 0:
                    board[i][j] = 2
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                if board[i][j] == 3:
                    board[i][j] = 0

S = Solution()
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
S.gameOfLife(board)
print(board)

# 289
# [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]