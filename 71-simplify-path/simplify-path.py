class Solution:
    def simplifyPath(self, path: str) -> str:
        # stack = []
        # for ele in path.split('/'):
        #     if stack and ele == '..':
        #         stack.pop()
        #     if ele not in ['.','..','']:
        #         stack.append(ele)

        # return '/'+'/'.join(stack)


        stack = []
        for char in path.split('/'):
            if stack and char == '..':
                stack.pop()
            elif char == '' or char == '.' or char == '..':
                continue
            else:
                stack.append(char)

        return '/'+'/'.join(stack)