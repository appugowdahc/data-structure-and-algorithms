class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':  # Only process filled cells
                    # Calculate the box index
                    box_index = (i // 3) * 3 + (j // 3)
                    
                    # Check for duplicates in the row, column, or box
                    if (num in rows[i]) or (num in cols[j]) or (num in boxes[box_index]):
                        return False
                    
                    # Add the number to the corresponding sets
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box_index].add(num)
        
        return True
            