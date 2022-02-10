class Solution:
    def romanToInt(self, s: str) -> int:
        romenArray = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        numberArray=[0]*len(s)
        for i in range(len(s)):
            numberArray[i]=romenArray[s[i]]
        sums = 0
        subs = 0
        for i in range(len(s)-1):
            if numberArray[i] == numberArray[i+1]:
                sums+=numberArray[i]
            elif numberArray[i] < numberArray[i+1]:
                subs+= numberArray[i]
            else:
                sums+=numberArray[i]
        sums+=numberArray[-1]
        last_sum=sums-subs
        return last_sum