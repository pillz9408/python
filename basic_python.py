#!/usr/bin/env python
# coding: utf-8

# In[1]:


string = "오늘 뭐 먹냐"
print(string)


# In[2]:


"점심" * 3


# "오늘 점심 뭐 먹지?"
# ### 모든 언어에는 순서가 있다. 
# 0. 오
# 1. 늘
# 3 " "
# 4. 점 
# ...

# In[4]:


"오늘 점심 뭐 먹지?"[6]


# In[5]:


"오늘 점심 뭐 먹지?"[3:5]


# In[6]:


"apple"[3]


# In[9]:


"오늘 점심 뭐 먹지?"[-4:]


# In[11]:


menu = "김치 볶음밥"

print("오늘 점심 메뉴는 %s 입니다." % menu)


# In[12]:


lyrics ="sorry sorry sorry sorry sorry sorry sorry 내가 내가 내가 내가 내가 네게 네게 네게"


# In[13]:


lyrics.count("sorry")


# In[14]:


lyrics.upper()


# In[15]:


lyrics.lower()


# In[16]:


lyrics.find("sorry")


# In[17]:


lyrics.replace("sorry","미안")


# In[18]:


lyrics.split()


# In[19]:


lyrics.split("가")


# ## 명제 = 참or 거짓 을 판별 할 수 있는 문장.
# ==, >, <, >=, <=, !=

# In[21]:


type(1+1 == 2)


# In[23]:


1+2 !=2


# 명제 and 명제 = 두 명제가 모두 참일때만 참 
# 명제 or 명제 = 두 명제중 하나만 참이여도 참

# ### 조건문

# if 명제 : 
#     명제가 참일 경우에 실행되는 코드
# else 명제:
#     명제가 거짓일 경우 실행되는 코드

# In[34]:


money = 5000
if money >= 2500:
    print("버스를 타고 간다")
else:
    print("걸어서 간다")


# In[36]:


money = 7000

if (oney >= 5000) and (money < 10000):
     print("편의점을 간다.")
elif money >= 10000:
    print("식당을 간다.")
else:
    print("굶어라")


# if 명제1 : 
#     명제1이 참일 경우에 실행되는 코드
#     
# elif 명제2:
#     명제 1은 거짓이지만 명제 2가 참일때 실행되는 코드
# else:
#     명제가 거짓일 경우 실행되는 코드

# ###리스트, 튜플
# 
# 리스트 : [] 조작이 가능하다.(수정이 가능) 
# 튜플 : () 조작이 불가능 (수정 불가능)

# In[37]:


a = [1,2,3,4,5]
b = ("가", "나")
c = [6,7,a]
print (a)
print (b)
print (c)


# In[ ]:





# ### 원소 추가

# In[38]:


"짜장" + "면"


# In[39]:


a = ["짜","장"]
a.append("면")
a


# In[43]:


a.insert(0,"간")
a


# In[40]:


b= [1,2,[3,4]]
b[2][1]


# In[47]:


### del , remove
del a[0]
a


# In[48]:


a.remove("면")
a


# In[49]:


### 교체 - 인덱스에 다른 값을 할당해 주면 알아서 교체.
a[1]= "왕"
a


# In[50]:


m= "간짜장면"
m.replace("간", "")


# In[52]:


k=["가","다","나","마","라"]
k


# In[54]:


k.reverse()
k


# In[56]:


k.sort()
k


# In[58]:


k.sort(reverse = True)
k


# In[61]:


len("짜장면은 맛있다.")


# In[63]:


len(k)


# In[66]:


fruit = ["사과","바나나","키위","망고","파인애플"]


# In[71]:


("사과" in fruit)and("바나나"in fruit)


# ### 반복문
# while 명제 : 
#     명제가 참인 한 실행되는 코드
#     if 명제
#     break 조건
# 
# for 변수 in 인덱싱이 가능한 자료형:
#     코드

# In[72]:


n = 1 
while n < 3:
    print(n)
    n = n + 1


# In[74]:


for i in [1,2,3,4,5]:
    print(i)


# In[83]:


for i in range(1,10):
    print( ("3 X {} = {}").format(i, 3*i))


# In[85]:


for i in range(1,10):
    for w in range(1,10):
        print("{} X {} = {}".format(i, w, i*w))


# ### EX 반복문
# - 10,000보다 큰 57과 83의 공배수 중 가장 작은수를 출력. 
# - 공배수 : 57과 83을 모두 약수로 가지는 수.

# In[96]:


n = 10000
while (n%57!= 0) or (n%83!=0):
    n= n+1
print(n)

    


# In[97]:


n = 10000
while True:
    if (n%57 == 0) and ( n%83 == 0):
        break
    else:
        n= n+1
print(n)


# ### 예외처리
# try:
#     코드
# except:
#     코드가 에러가 날 경우 실행되는 코드.

# In[99]:


for i in range(10):
    print(1/(i-7))


# In[100]:


for i in range(10):
    try:
        print(i/(i-7))
    except:
        print("beep")


# In[101]:


a= int(input("3의 배수를 입력하시오: "))
print(a)


# In[103]:


a= int(input("3의 배수를 입력하시오: "))
if a % 3 == 0:
    pass
else:
    raise Exception("3의 배수가 아닙니다.")
print(a)


# ### Dictonary
# { "Key": "Value"} : 키는 겹칠수 없고 하나의 키에는 하나의 값만 입력 가능.
# Key는 수정 불가 but Value 는 수정 가능.

# In[105]:


lst = {"A":"가", "B":"나", "C":"다", "D":"라", "E":"마"}


# In[110]:


lst["B"]


# In[112]:


csb ={"Name": ["홍길동","임꺽정","장길산"], "Age": [20,35,52], "Height": [180,175,190]}


# In[113]:


csb["Name"]


# In[114]:


csb.keys()


# In[116]:


csb.values()


# In[118]:


csb["sex"]= ["M","M","M"]
csb


# In[119]:


del csb["sex"]
csb


# In[120]:


for i in csb:
    print(i)


# In[123]:


csbs ={"Name": ["홍길동","임꺽정","장길산"], 
      "Age": [20,35,52], 
      "Height": [180,175,190],
      "FSize": [240,260,280]}
### for 문을 사용해 임꺽정, 홍길동, 장길산의 나이 평균, 키 평균, 발 사이즈 평군을 구해주세요.


# In[131]:


averages = []
for i in csbs:
    try:
        n = 0
        for w in csbs[i]:
            n = n + w
            averages.append(n/len(csbs[i]))
    except:
        pass
    
csbs["평균들"] = averages
csbs
        

    


# In[130]:


nai = [20,35,52]
n= 0
for i in nai:
    n = n + i
print(n/len(nai))


# In[ ]:


averages = []
for i in csbs:
    n = 0
    for w in csbs[i]:
        n = n + w
        averages.append(n/len(csbs[i]))
    
csbs["평균들"] = averages
csbs
        

