#left sum right sum
# n=map(int,input().split())
# g=n.copy()
# m=[]
# for i in n:
#     e=n.index(i)
#     rightsum=0
#     leftsum=0
#     l=n[e+1::]
#     for i in l:
#         rightsum=rightsum+i
#     f=n.index(i)
#     k=g[f:0]
#     for i in k:
#         leftsum=leftsum+i
#     m.append(leftsum-rightsum)
# print(m)


#valid panranthesis and count the brackets
# open_list = ["[","{","("]
# close_list = ["]","}",")"]
# n=input()
# def valid(n):
#     stack = []
#     for i in n:
#         if i in open_list:
#             stack.append(i)
#         elif i in close_list:
#             pos = close_list.index(i)
#             if ((len(stack) > 0) and
#                 (open_list[pos] == stack[len(stack)-1])):
#                 stack.pop()
#             else:
#                 return False
#     if len(stack) == 0:
#         return True
#     else:
#         return False
    
    
# if(valid(n)):
#   #d={'()':value1,'[]':value2,'{}':value3}
#     d={}
#     s=0
#     b=0
#     c=0
#     for i in n:
#         if(i=='('):
#             b=n.count(i)
#         elif(i=='['):
#             s=n.count(i)
#         elif(i=='{'):
#             c=n.count(i)
#         else:
#             continue
#     d['()']=b
#     d['[]']=s
#     d['{}']=c
#     print(d)
# else:
#     print('NULL')

#group anagrams problem[eat,ate,tea,tan,nat,bat]
# n=['eat','ate','tea','tan','nat','bat']
# dic={}
# for i in n:
#     s=''.join(sorted(i))
#     if s in dic:
#         dic[s].append(i)
#     else:
#         dic[s]=[i]
# print(list(dic.values()))

#voting machine
# n=input().split()
# dic={}
# s=list(set(n))
# s.sort()
# for i in s:
#         dic[i]=n.count(i)
# print(s[0],dic[s[0]])


#two sum
# n=input()
# t=int(input())
# l=[]
# k=[]
# for i in n:
#     if i.isdigit():
#         l.append(int(i))
# for i in l:
#     if len(k)==2:
#         break
#     c=l.index(i)
#     for j in range(c+1,len(l)):
#         s=i+l[j]
#         if s==t:
#             k.append(l.index(i))
#             k.append(j)
#             break
#     c+=1
# print(k)


#majority element

# n=input().split()
# s=list(set(n))
# m=0
# for i in s:
#     c=n.count(i)
#     if c>m:
#         m=c
#         k=s.index(i)
# print(s[k])
            


#best time to buy and sell the stock
# n=input().split()
# m=min(n)
# i=n.index(m)
# l=n[i:]
# if len(l)==0:
#     print('0')
# else:
#     print(int(max(l))-int(m))

#roman integer

# m={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

# n=input()
# s=0
# for i in range(len(n)):
#     if i<len(n)-1 and m[n[i]]<m[n[i+1]]:
#         s-=m[n[i]]
#     else:
#         s+=m[n[i]]
# print(s)

#palindrome

# n=input()
# r=n[::-1]
# if n==r:
#    print('true')
# else:
#     print('false')

# maximum subarray

# n=input().split(',')
# sum=0
# max=0
# l=[]
# for i in n:
#     sum+=int(i)
#     if sum<0:
#         sum=0
#     else:
#         if sum>max:
#             max=sum
# s=0
# for i in n:
#     s+=int(i)
#     if s<0:
#         s=0
#         l.clear()
#     else:
#         if s>0:
#             l.append(i)
#             if s==max:
#                 break
# print(max,l)


#longest common prefix

# n=input().split()
# n.sort()
# f=n[0]
# l=n[-1]
# a=''
# for i in range(min(len(f),len(l))):
#     if f[i]==l[i]:
#         a+=f[i]
# print(a)

# index of second occurance of the String

# n=input()
# h=input()
# l=[]
# if h not in n:
#     print('-1')
# else:
#     for i in range(len(n)):
#         if n[i]==h[0]:
#             l.append(i)
# print(l[1])


#alphabet rangoli
            

# n=int(input())
# a=list('abcdefghijklmnopqrstuvwxyz')
# l=a[:n]
# r=l[::-1]
# k=[]
# g=[]
# for i in r:
#     k.append(i)
#     j=k.copy()
#     x=j[::-1]
#     h=k+x[1:]
#     g.append('-'.join(h))
# z=len(g[-1])
# for i in range(len(r)-1):
#     r.remove(r[-1])
#     b=r.copy()
#     q=b[::-1]
#     v=r+q[1:]
#     g.append('-'.join(v))
# for i in g:
#     print(i.center(z,'-'))

# designer mat

# n=input().split()
# l=n[0]
# w=int(n[-1])
# o=[]
# for i in range(1,int(l)//2+1):
#         c='.|.'*i
#         o.append(c)
#         print(c.center(w,'-'))
# print('WELCOME'.center(w,'-'))
# r=o[::-1]
# for i in r:
#         print(i.center(w,'-'))     
    
    
#choclate distribution
# n=input().split()
# mo=int(input())
# n=[int(i) for i in n]
# n.sort()
# print(n)
# mi=n[-1]-n[0]
# for i in range((len(n)-mo)+1):
#     k=n[i+mo-1]-n[i]
#     mi=min(mi,k)
# print(mi)

# search in sorted array

# n=list(map(int,input().split()))
# n.sort()
# tar=int(input())
# l=n[tar:]+n[0:tar]
# print(l)

#next permutation
#2 1 5 4 3 0 0
# n=list(map(int,input().split()))
# l=len(n)
# p=-1
# for i in range(l-2,0,-1):
#     if n[i]<n[i+1]:
#         p=i
#         break
# if p==-1:
#     print(n[::-1])
#     exit()
# for i in range(l-1,p,-1):
#     if n[i]>n[p]:
#         t=n[p]
#         n[p]=n[i]
#         n[i]=t
#         break
# q=n[p+1:]
# q.sort()
# g=n[0:p+1]+q
# print(g)

# repeat and missing no array

# n=list(map(int,input().split()))
# n.sort()
# l=[]
# for i in range(min(n),max(n)+1):
#     if n.count(i)>1 or i not in n:
#         l.append(i)
# print(l)


# valid palindrome
# s=''.join(input().split())
# if s[::-1]==s:
#     print('true')
# else:
#     print('false')


#probable word

# n=input().split()
# ar=input().split()
# lo=[]
# for i in n:
#     l=len(i)
#     s=''
#     for k in range(l):
#         if i[k] in ar:
#             s=s+i[k]
#     if s==i:
#         a=str(i)
#         lo.append(a)
# print(lo)

#balanced parantisis
# def bal(n):
#     stack=[]
#     for i in n:
#         if i in "{[(":
#             stack.append(i)
#         else:
#             if not stack:
#                 return False
#             c=stack.pop()
#             if c=='{':
#                 if i !='}':
#                     return False
#             if c=='[':
#                 if i !=']':
#                     return False
#             if c=='(':
#                 if i !=')':
#                     return False
#     if stack:
#         return False
#     else:
#         return True
# print(bal(input()))

#minimum window substring

s=input()
su=input()
l=len(su)
re=0
le=0
r=''
k=[]
lo=len(s)
for i in range(lo):
    if i ==lo-l:
        break
    for j in range(i,lo):
        if s[j] in su:
            l-=1

        r=r+s[j]
        if l==0:
            k.append(r)
            r=''
            l=len(su)
            break
print(k)
v=len(k[0])
for i in k:
    if v>len(i):
        v=len(i)
        m=i
print(m)
        