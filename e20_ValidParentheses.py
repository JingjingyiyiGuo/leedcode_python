# Runtime: 48 ms, faster than 32.11% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 13.2 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.
# class Solution:
#     def isValid(self, s: str) -> bool:
#         if len(s) == 0:
#             return True
#         stack = []
#         stack.append(s[0])
#         for i in range(1,len(s)):
#             if s[i] in "([{":
#                 stack.append(s[i])
#             elif len(stack) == 0:
#                 return False
#             else:
#                 if stack[len(stack)-1] == "(" and s[i] == ")" or stack[len(stack)-1] == "[" and s[i] == "]" or stack[len(stack)-1] == "{" and s[i] == "}":
#                     stack.pop()
#                 else:
#                     return False
#         if len(stack) == 0:
#             return True
#         else:
#             return False

# Runtime: 40 ms, faster than 47.54% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 13.1 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.
# 收获：
# 需要用if写很多匹配对的情况，可以用字典来代替，查找也很方便；
# 可以从一定的高度思考代码架构，设计如何分类最简洁。比如这里就可以分为左括号一种处理情况，右括号一种。所以大类只要分两类。
# 这种对特殊情况的处理归为哪一类的思考很重要。
# 最后列表为空则为True，可以把上面的四句话用一句话来写。
# class Solution:
#     def isValid(self, s: str) -> bool:
#         maping = {")":"(", "]":"[", "}":"{"}
#         stack = []
#         for char in s:
#             if char in maping:
#                 if stack:
#                     top_element = stack.pop()
#                 else:
#                     top_element = "#"
#                 if maping[char] != top_element:
#                     return False
#             else:
#                 stack.append(char)
#         return not stack

# Runtime: 36 ms, faster than 84.38% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 13.1 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.
# 将两个判断条件进一步整合成一起判断，减少赋值操作，速度提升了4ms。
# class Solution:
#     def isValid(self, s: str) -> bool:
#         maping = {")":"(", "]":"[", "}":"{"}
#         stack = []
#         for char in s:
#             if char in maping:
#                 if stack and maping[char] == stack[-1]:
#                     stack.pop()
#                 else:
#                     return False
#             else:
#                 stack.append(char)
#         return not stack

# Runtime: 40 ms, faster than 47.54% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 13.3 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.
# 这是答案里给的速度最快的方法，但是在我这里提交测却不是，看起来也不是很简洁（暂时不知道原因）
class Solution:
    def isValid(self, s: 'str') -> 'bool':
        if len(s)==0:
            return True
        t_s = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                t_s.append(i)
            if i ==")":
                if "(" not in t_s or t_s[-1] != "(":
                    return False
                else:
                    del t_s[-1]
            if i == "]":
                if "[" not in t_s or t_s[-1] != "[":
                    return False
                else:
                    del t_s[-1]
            if i == "}":
                if "{" not in t_s or t_s[-1] != "{":
                    return False
                else:
                    del t_s[-1]
        if len(t_s) == 0:
            return True
        else:
            return False

s = "["
S = Solution()
x = S.isValid(s)
print(x)