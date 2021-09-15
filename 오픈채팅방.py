def solution(record):
    answer = []

    record = [s.split(' ') for s in record]

    person = {}
    for s in record:
        if s[0] == 'Enter':
            person[s[1]] = s[2]
        elif s[0] == 'Change':
            person[s[1]] = s[2]

    for s in record:
        if s[0] == 'Enter':
            answer.append(f"{person[s[1]]}님이 들어왔습니다.")
        elif s[0] == 'Leave':
            answer.append(f"{person[s[1]]}님이 나갔습니다.")

    return answer
