class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + "#" + string
        print(encoded_string)
        return encoded_string



    def decode(self, s: str) -> List[str]:

        pointer = 0

        decoded_string = []

        while pointer<len(s)-1:
            length_str = ""
            for i in s[pointer:]:
                if i == "#":
                    pointer+=1
                    break
                length_str += i
                pointer+=1
            current_string = ""

            start = pointer
            end = start+int(length_str)
            for i in s[start:end]:
                pointer+=1
                current_string += i
            decoded_string.append(current_string)

        return decoded_string
            
            
                
        
