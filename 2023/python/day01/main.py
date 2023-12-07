
translate = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def solve(inp: list[str]) -> int:
    result = 0
    for line in inp:
        
        for k, v in translate.items():
            if k in line:
                line = line.replace(k, v)
        start = ''
        end = ''
        for char in line:
            if char.isdigit():
                start = char
                break
        for char in reversed(line):
            if char.isdigit():
                end = char
                break
        breakpoint()
        result += int(f'{start}{end}')
    return result




if __name__ == '__main__':
    # test = '''1abc2
    #     pqr3stu8vwx
    #     a1b2c3d4e5f
    #     treb7uchet'''
    # if solve(test.split('\n')) == 142:
    #     print('Test case works ruiining real deal')
    # else:
    #     raise AssertionError('Test case failed: Expected result is not equal to actual result')
    
    # with open('input.txt', 'r') as file:
    #     content_list = file.read().splitlines()
    # print(solve(content_list))

    test = '''two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen'''
    print(solve(test.split('\n')))
    if solve(test.split('\n')) == 281:
        print('Test case works ruiining real deal')
    else:
        raise AssertionError('Test case failed: Expected result is not equal to actual result')
    
