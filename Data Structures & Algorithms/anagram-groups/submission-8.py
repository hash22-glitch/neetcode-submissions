class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = {}

        alphabet="abcdefghijklmnopqrstuvwxyz"


        for string in strs:
            frequency = tuple(string.count(i) for i in alphabet )

            if frequency not in dic:
                dic[frequency] = [string]
            else:
                dic[frequency].append(string)
            
        return list(dic.values())