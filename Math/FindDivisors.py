# not finished

def get_div(div_required):
    triangle = 0
    t = 1
    divs = 0
    
    while divs < div_required:
        triangle += t
        divs = 0
        for n in range(1, (triangle // 2) + 1):
            if triangle % int(n) == 0:
                divs += 1
        
        t += 1
    
    return triangle

print(get_div(500))