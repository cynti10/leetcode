class Solution(object):
    def summaryRanges(self, nums):
        a,b=0,0
        c=[]
        if len(nums)==0:
            return c
        while b<len(nums)-1:
            if nums[b]!=nums[b+1]-1:
                if b==a:
                    c.append(str(nums[a]))
                else:
                    c.append("".join([str(nums[a]),"->",str(nums[b])]))
                a=b+1
            b+=1
        if b==a:
            c.append(str(nums[a]))
        else:
            c.append("".join([str(nums[a]),"->",str(nums[b])]))
        return c


        
