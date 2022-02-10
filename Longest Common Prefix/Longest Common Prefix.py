class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        count_List = len(strs)
        prefix_List = [""] * count_List
        strs.sort()
        longest = min(strs)
        longest_strs=len(min(strs))


        for i in range(0,longest_strs):
            object = longest[i]
            count = 0
            for j in range(1,count_List):
                if object == strs[j][i]:
                    count +=1
                else:
                    if prefix_List[0]== "":
                        return ""
                    else:
                        return prefix_List[0]
            if count == count_List-1:
                for m in range(0,count_List):
                    prefix_List[m]+=object


        return prefix_List[0]