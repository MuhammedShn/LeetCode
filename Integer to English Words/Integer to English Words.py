class Solution:       
    def numberToWords(self, num: int) -> str:
        dict = {0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
                10: "Ten", 11: "Eleven",
                12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen",
                19: "Nineteen",
                20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty",
                90: "Ninety", 100: "Hundred"}

        if num == 0:
            return "Zero"

        List = []
        Liste = []
        for i in range(int(((len(str(num)))/3)+0.99)):
            List.append(int(num) % 1000)
            num //= 1000

        last_string = ["", "", "", ""]
        for i in range(len(List)):
            Liste = []
            if List[i] != 0:
                last_two_digits = List[i] % 100
                first_two_digits = List[i] //10
                if (len(str(List[i]))) == 3:
                    for j in range(0, len(str(List[i]))):
                        Liste.append((str(List[i]))[j])
                    Liste = Liste[::-1]
                    if last_two_digits > 20:
                        if List[i] > 100 and List[i] < 1000 and int(first_two_digits%10) == 0:
                            last_string[i] += str(dict[int(Liste[2])]) + " Hundred" 
                            if int(List[i]%10) != 0 :                      
                                last_string[i] += " " + str(dict[int(Liste[0])])
                            else:
                                pass
                            
                        elif List[i] > 100 and List[i] < 1000 and int(first_two_digits%10) != 0:
                            last_string[i] += str(dict[int(Liste[2])]) + " Hundred " + str(dict[int(Liste[1]) * 10])
                            if last_two_digits%10 != 0:                      
                                last_string[i] += " " + str(dict[int(Liste[0])])
                            else:
                                pass
                        else:
                            pass
                            
                        
                    else:
                        if List[i] % 100 == 0:
                            last_string[i] = str(dict[int(Liste[2])]) + " Hundred"
                        elif List[i] > 100 and List[i] < 1000 and int(str(List[i])[1] != 0):
                            last_string[i] = str(dict[int(Liste[2])] + " Hundred " + dict[last_two_digits])

                else:
                    if (len(str(List[i]))) == 2:
                        for j in range(0, len(str(List[i]))):
                            Liste.append((str(List[i]))[j])
                        Liste = Liste[::-1]
                        if last_two_digits > 20:
                            if List[i] > 20 and List[i] < 100 and List[i]%10 == 0:
                                last_string[i] = str(dict[int(Liste[1]) * 10])
                            elif List[i] > 20 and List[i] < 100 and List[i]%10 != 0:
                                last_string[i] = str(dict[int(Liste[1]) * 10]) + " " + str(dict[int(Liste[0])])
                        else:
                            last_string[i] = str(dict[last_two_digits])

                    else:
                        last_string[i] = str(dict[last_two_digits])


        last_one = ""
        if last_string[3] != "":
            last_one += str(last_string[3]) + " Billion "
        if last_string[2] != "":
            last_one += str(last_string[2]) + " Million "
        if last_string[1] != "":
            last_one += last_string[1] + " Thousand "
        last_one += str(last_string[0])

        return last_one.strip()