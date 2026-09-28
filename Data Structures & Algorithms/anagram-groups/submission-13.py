class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        alphabet_hash = {}
        for i in range(26):
            alphabet_hash[alphabet[i]] = i


        frequencies = {}

        for i in strs:
            frequency_list = [0 for i in range(26)]

            for j in i:
                frequency_list[alphabet_hash[j]] += 1
            
            frequency = tuple(frequency_list)

            if frequency in frequencies:
                frequencies[frequency].append(i)
            else:
                frequencies[frequency] = [i]
        return list(frequencies.values())