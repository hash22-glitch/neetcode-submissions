class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_t = set(t)
        set_s = set(s)

        hash_t = {i:t.count(i) for i in set(t)}
        hash_s = {i:s.count(i) for i in set(s)}

        if hash_t == hash_s:
            return True
        return False
            

        