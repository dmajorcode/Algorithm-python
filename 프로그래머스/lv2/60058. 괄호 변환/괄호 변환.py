'''
(계획) 3:18~3:38
(실제) 3:18~3:43
'''

# (오답노트) check 함수의 for i in range(0,len(p)): 여기에서 시작값을 0으로 주면 안된다.
# For loop 안에서 처음 변수를 선언하면 안된다. 함수 안이든 어디에서든 변수를 선언하고 해야 한다.
# u[1:-1]괄호 방향 뒤집는 것 하지 않았다. (4-4.)
# for i in range(1,len(p)): 여기에서 끝 범위를 len(p)+1로 해야 한다.

'''
균형잡힌 괄호 문자열
1) '('와 ')'의 갯수가 같다.

올바른 괄호 문자열
1) 모든 문자열에 대해서 slice를 했을 때, 닫힌 것의 갯수가 항상 열린 것 보다 작다.
2) 마지막에는 열린 것과 닫힌 것의 갯수가 같다.
'''

def balance(word):
    counta = 0
    countb = 0
    # print('word:',word)
    # print('len(word):',len(word))
    for i in range(len(word)):
        if word[i] == '(':
            counta+=1
        else:
            countb+=1
    # print('counta:',counta)
    # print('countb:',countb)
    if counta == countb:
        return True
    else:
        return False


def right(word):
    counta=0
    countb=0
    
    for i in range(len(word)):
        if word[i] == '(':
            counta += 1
        else:
            countb += 1
        if counta < countb:
            return False
    
    if counta == countb:
        return True
    else:
        return False

def reverse(p):
    q = ''
    for i in p:
        if i == '(':
            q += ')'
        else:
            q += '('
    return q

def check(p):
    # print('p:',p)
    # print('p[1:2]:',p[0:2])
    # print('len(p):',len(p))
    if p == '':
        return ''
    u = ''
    v = ''
    for i in range(1,len(p)+1):
        # print(i)
        # print('balance:',balance(p[0:i]))
        if balance(p[0:i]):
            u = p[0:i]
            v = p[i:]
            break
    # print('u:',u)
    # print('v:',v)
    if right(u):
        # print('True')
        return u+check(v)
    else:
        # print('False')
        return '('+check(v)+')'+reverse(u[1:-1])
    
    
def solution(p):    
    answer = check(p)
    # print("this is answer",answer)
    return answer

