def decode_message(s: str, p: str) -> bool:

    if len(s) != len(p):
        return False

    for i in range(len(s)):
        message_char = s[i]
        key_char = p[i]
        
        if message_char == key_char or (key_char == '?' and message_char.isalpha()):
            continue
        elif key_char == '*':
            continue
        else:
            return False 

    return True
