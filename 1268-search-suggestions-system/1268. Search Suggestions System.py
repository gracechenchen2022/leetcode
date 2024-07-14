class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        n = len(products)

        left = 0
        right = n - 1
        res = []

        for i in range(len(searchWord)):
            while left <= right and (len(products[left])<= i or products[left][i] != searchWord[i]):
                left += 1
            while left <= right and (len(products[right]) <= i or products[right][i] != searchWord[i]):
                right -= 1
            tmp = []
            for k in range(left, min(left+3, right + 1)):
                tmp.append(products[k])
            
            res.append(tmp)
        return res

        '''
        1.two pointers: sort
        2.iterate searchWord
        tc: onlogn+mn
        sc:o1
        '''