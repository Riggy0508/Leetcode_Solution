// https://leetcode.com/problems/goat-latin

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        
        word=sentence.split()
        goat=[]

        for i,word in enumerate(word):
            if word[0].lower() in "aeiou":
                goat_word= word + "ma"

            else:
                goat_word=word[1:]+word[0]+"ma"

            goat_word=goat_word+"a" * (i+1)
            goat.append(goat_word)

        return " ".join(goat)