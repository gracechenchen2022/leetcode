class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        # 根据 Frobenius Coin Problem 的公式
        return primeOne * primeTwo - primeOne - primeTwo
