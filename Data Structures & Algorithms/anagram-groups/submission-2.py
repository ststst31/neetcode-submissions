class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #firstly we create a hash dictionary. defaultdict
        #then we iterate thru strs and declare a count map
        # then we interate from each letter in each word in strs and then incremenet the count of particular letter in the map 
        #then we append the outter iterator to the map 
        # then we return the list 
        result = defaultdict(list)
        for i in strs:
            count = [0]*26
            for c in i:
                count[ord(c)-ord("a")]+=1
            result[tuple(count)].append(i)
        return list(result.values())


        