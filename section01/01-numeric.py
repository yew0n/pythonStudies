# -*- coding: utf-8 -*-

# 변수 만들기
a=123
b=-456
print(a)
print(b)

#한번 할당된 변수는 다른 값으로 변경 가능
a=10000
print(a)


#실수형 변수 만들기
c=1.2
d=-3.45
print(c)
print(d)

#지수형태 (알파벳 e 혹은 E 사용)
e=4.24e10   #4.24*(10의 10제곱)
f=4.24e-10   #4.24*(10의 -10제곱)
print(e)
print(f)

# 8진수 표현 (숫자0 + 알파벳o + 숫자값)
g=0o177
print(g)

# 16 진수 표현 (숫자0 + 알파벳 x + 숫자값)
h=0xABC
print(h)

#복소수 (알파벳 j)
i= 1+2j
print(i)

#복소수의 실수부분 조회 -> 객체 i에 포함되는 하위변수에 접근
print(i.real)

#복소수의 허수부분 조회 -> 객체 i에 포함되는 하위변수에 접근
print(i.imag)

#복소수의 켤레복소수 -> 객체 i에 포함되는 하위함수에 접근
print(i.conjugate())

#복소수의 절대값 -> 파이썬에 내장된 abs() 함수 사용
print(abs(a))


