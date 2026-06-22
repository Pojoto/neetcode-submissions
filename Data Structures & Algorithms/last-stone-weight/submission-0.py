class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones.sort()


        while len(stones) >= 1:
            if len(stones) == 1:
                return stones[0]
            
            stone1 =  stones[len(stones) - 2]
            stone2 = stones[len(stones) - 1]
            
            if stone1 == stone2:
                stones.pop()
                stones.pop()
            else:
                new_weight = stone2 - stone1 if stone1 < stone2 else stone1 - stone2
                stones.pop()
                stones.pop()

                insert_index = 0
                for stone_weight in stones:
                    if new_weight > stone_weight:
                        insert_index += 1
                    else:
                        break
                
                stones.insert(insert_index, new_weight)
        
        return 0

            
        




        