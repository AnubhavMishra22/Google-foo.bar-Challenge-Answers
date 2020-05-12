def solution(s):
    l = len(s)
    if l<1:
        return 0
    
    a1 = 0
    a2 = l-1
    pat1, pat2 = '', ''
    while a1<a2:
        pat1 = pat1+s[a1]
        pat2 = s[a2]+pat2
        if pat1 == pat2 and pat1 == s[a1+1:a1+len(pat1)+1]:
            return l/len(pat1)
        a1+=1
        a2-=1
        
    return 1
print("Test case 1 : ")
print(solution("abccbaabccba"))

print("\nTest case 2 : ")
print(solution("abcabcabcabc"))t