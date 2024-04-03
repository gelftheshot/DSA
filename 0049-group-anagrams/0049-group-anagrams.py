from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = defaultdict(list)
        
        for word in strs:
            count = [0] * 26;
            
            for let in word:
                
                count[ord(let) - ord("a")] += 1
            dic[tuple(count)].append(word)
        return(dic.values())