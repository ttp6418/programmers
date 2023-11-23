def solution(new_id):
    special = ['-', '_', '.']
    
    new_id = list(new_id)
    
    for [alphabet_index, alphabet] in enumerate(new_id):
        if alphabet.isalpha() == True:
            if ord(alphabet) >= 65 and ord(alphabet) <= 90:
                new_id[alphabet_index] = chr(ord(new_id[alphabet_index]) + 32)
        elif alphabet.isdigit() == True: pass
        elif alphabet not in special:
            new_id[alphabet_index] = ''
    new_id = "".join(new_id)
    while(new_id != new_id.replace("..", ".")):
        new_id = new_id.replace("..", ".")
    new_id = new_id.lstrip('.').rstrip('.')
    if new_id == "": new_id = 'a'
    new_id = new_id[:15]
    new_id = new_id.lstrip('.').rstrip('.')
    
    while(len(new_id) <= 2):
        new_id = new_id + new_id[-1:]
    return new_id