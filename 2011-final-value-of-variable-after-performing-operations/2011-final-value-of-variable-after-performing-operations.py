class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for opp in operations:
            if '++' in opp:
                x += 1
            if '--' in opp:
                x -= 1
        return x
        