def search_from(i, j, k):
    if k == len(s):
        return True
    if i < 0 or j < 0 or i >= n or j >= n or l[i][j] != s[k]:
        return False
    
    # Temporarily mark the cell as visited
    temp = l[i][j]
    l[i][j] = '#'
    
    # Explore all possible directions
    found = (search_from(i-1, j, k+1) or
             search_from(i+1, j, k+1) or
             search_from(i, j-1, k+1) or
             search_from(i, j+1, k+1))
    
    # Unmark the cell
    l[i][j] = temp
    
    return found

n = int(input())
l = []
for i in range(n):
    l.append(input().split())

s = input()

found = False
for i in range(n):
    for j in range(n):
        if l[i][j] == s[0]:
            if search_from(i, j, 1):
                print('yes')
                found = True
                break
    if found:
        break

if not found:
    print('no')
