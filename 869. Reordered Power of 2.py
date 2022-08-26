class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        power= [''.join(sorted(list(str(2**i)))) for i in range(31)]
        return ''.join(sorted(list(str(n)))) in power
