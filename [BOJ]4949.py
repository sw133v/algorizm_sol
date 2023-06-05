from re import sub
def sol_4949():
    def is_fine(str_data):
        result = 'yes'
        bracket_dict = {
            '[' : ']',
            '(' : ')',
        }
        stack = []
        for bracket in str_data:
            if bracket == '[' or bracket == '(':
                stack.append(bracket)
            else:
                if len(stack):
                    if bracket_dict[stack[-1]] == bracket:
                        stack.pop(-1)
                    else:
                        result = 'no'
                        break
                else:
                    result = 'no'
                    break
        if len(stack):
            result = 'no'
        return result
    
    filterd_word = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    input_data = None
    while input_data != '.':
        if input_data:
            temp_data = sub(r'[a-z]','', input_data.lower().replace(' ', '').replace('.', ''))
            print(is_fine(temp_data))
        input_data = input()
        

sol_4949()