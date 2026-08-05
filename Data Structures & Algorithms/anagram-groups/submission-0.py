class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        answer = {}

        for i in range(len(strs)):
            x = "".join(sorted(strs[i]))
            if x in answer:
                answer[x].append(strs[i])

            else:
                answer[x] = [(strs[i])]

        return list(answer.values())