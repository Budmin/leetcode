class Solution:
    def countOdds(self, low: int, high: int) -> int:
 
        output = 0

        if low % 2 == 1:
            output += 1
            low += 1

        if high % 2 == 1:
            output += 1
            high -= 1

        
        output += (high - low) // 2
        
        return output




