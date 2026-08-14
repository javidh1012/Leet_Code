class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for ele in path.split('/'):
            if stack and ele == '..':
                stack.pop()
            if ele not in ['.','..','']:
                stack.append(ele)

        return '/'+'/'.join(stack)
        