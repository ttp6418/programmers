def solution(wallpaper):
    min_x = len(wallpaper) + 1
    min_y = len(wallpaper[0]) + 1
    max_x = 0
    max_y = 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                if i <= min_x: min_x = i
                if j <= min_y: min_y = j
                if i >= max_x: max_x = i + 1
                if j >= max_y: max_y = j + 1
    
    return [min_x, min_y, max_x, max_y]