class Solution:

    def encode(self, strs: List[str]) -> str:
       #declare an empty string to store encode
       res = ''
       #iterate over word in the strs list
       for s in strs:
       #create a length of string with a delimitor to describe and seperate incoming string
        res += str(len(s)) + '#' + s
       #return encoded string
       return res
    def decode(self, s: str) -> List[str]:
        #declare empty result array
        #we also want to track our place with i
        res, i = [], 0
        #set a boundary for our result
        while i < len(s):
            #set another variable j to i
            j = i
            #find the delimitor 
            while s[j] != '#':
                j += 1
            #use the integar before delim to remember the length of encoded string
            length = int(s[i:j])
            #check the word based on the length 
            #append that to res
            res.append(s[j + 1 : j + 1 + length])
            #increment i
            i = j + 1 + length
        return res