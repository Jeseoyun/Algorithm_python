def solution(s):
    answer = ""
    num_chr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    tmp_chr = ""
    for val in s:
        if ord(val) >= 48 and ord(val) <= 57:
            answer += val
        else:
            tmp_chr += val
            if tmp_chr in num_chr:
                answer += str(num_chr.index(tmp_chr))
                tmp_chr = ""

    return int(answer)
    
    
    
# test case
print(solution("one4seveneight")) # 1478
print(solution("23four5six7")) # 234567
print(solution("2three45sixseven")) # 234567
print(solution("123")) # 123
