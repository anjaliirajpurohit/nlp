def min_edit_distance(source, target):
    m = len(source)
    n = len(target)
    
    # Step 1: Create an empty grid (matrix) filled with zeros
    # Size will be (m+1) rows by (n+1) columns
    grid = [[0 for j in range(n + 1)] for i in range(m + 1)]
    
    # Step 2: Fill the first column (Cost of deleting letters one by one)
    for i in range(m + 1):
        grid[i][0] = i
        
    # Step 3: Fill the first row (Cost of inserting letters one by one)
    for j in range(n + 1):
        grid[0][j] = j
        
    # Step 4: Fill the rest of the grid using Dynamic Programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            
            # If the current letters match, no operation is needed!
            # We just copy the cost from the top-left diagonal cell.
            if source[i - 1] == target[j - 1]:
                grid[i][j] = grid[i - 1][j - 1]
                
            # If the letters DO NOT match, we calculate the cost of all 3 
            # possible operations and pick the cheapest (minimum) one.
            else:
                insert_cost = grid[i][j - 1]      # Look at the cell to the LEFT
                delete_cost = grid[i - 1][j]      # Look at the cell ABOVE
                substitute_cost = grid[i - 1][j - 1]  # Look at the DIAGONAL cell
                
                # Take the minimum of the three and add 1 (since the cost of the operation is 1)
                grid[i][j] = min(insert_cost, delete_cost, substitute_cost) + 1
                
    # The final minimum edit distance is always in the absolute bottom-right corner of the grid
    return grid[m][n]

# Test the program
source_string = "intention"
target_string = "execution"

distance = min_edit_distance(source_string, target_string)
print(f"Source: {source_string}")
print(f"Target: {target_string}")
print(f"Minimum Edit Distance: {distance}")