# -*- coding: utf-8 -*-


"""
Created on Mon May 20 22:55:10 2019

@author: GladYouCame

5. 最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"


"""
s= "cbbd"
countList = []
for i in range(len(s)):
    countList.append(1)
    j =1
    while (i-j>-1) and (i+j<len(s)):
        if s[i-j] == s[i+j]:
            j+=1
            countList[i] =  j
        else: break
print(countList)    


countList2 = []
for i in range(len(s)):
    countList2.append(0)
    j ,k= 0,1
    while (i-j>-1) and (i+k<len(s)):
        if s[i-j] == s[i+k]:
            j+=1
            k+=1
            countList2[i] =  j
        else: break
print(countList2 )

if max(countList)>max(countList2):
    print(s[countList.index(max(countList))-max(countList)+1:countList.index(max(countList))+max(countList)])
else:
    print(s[countList2.index(max(countList2))-max(countList2)+1 : countList2.index(max(countList2))+max(countList2)+1])
    
    
#        if len(s)<2:
#            return s
#        countList = []
#        for i in range(len(s)):
#            countList.append(1)
#            j =1
#            while (i-j>-1) and (i+j<len(s)):
#                if s[i-j] == s[i+j]:
#                    j+=1
#                    countList[i] =  j
#                else: break
#        #print(countList)    
#
#
#        countList2 = []
#        for i in range(len(s)):
#            countList2.append(0)
#            j ,k= 0,1
#            while (i-j>-1) and (i+k<len(s)):
#                if s[i-j] == s[i+k]:
#                    j+=1
#                    k+=1
#                    countList2[i] =  j
#                else: break
#        #print(countList2 )
#
#        if max(countList)>max(countList2):
#            return(s[countList.index(max(countList))-max(countList)+1:countList.index(max(countList))+max(countList)])
#            
#        else:
#            return(s[countList2.index(max(countList2))-max(countList2) +1: countList2.index(max(countList2)) + max(countList2)+1])
    
        n = len(s)
        self.res = ""
        def helper(i,j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            if len(self.res) < j - i -1 :
                self.res = s[i+1:j]
        for i in range(n):
            helper(i,i)
            helper(i,i+1)
        return self.res