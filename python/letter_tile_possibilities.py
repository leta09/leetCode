from itertools import permutations
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        x = []
        for i in range(len(tiles)):
            x += set(list(permutations(tiles, i+1)))
            
        return len(x)