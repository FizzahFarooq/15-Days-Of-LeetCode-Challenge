class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}

        for word in strs:
            key = ''.join(sorted(word))   # sorted characters become the key

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return groups.values()
