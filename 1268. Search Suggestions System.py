class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        suggestions, i = [], 0
        for c in range(1, len(searchWord) + 1):
            i = bisect_left(products, searchWord[:c], i)
            suggestions.append([w for w in products[i:i + 3] if w.startswith(searchWord[:c])])
        return suggestions
