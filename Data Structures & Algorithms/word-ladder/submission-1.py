class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # Let's find all the patterns using a "wild card" value *
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)
        
        # Now make sure we don't visit the same nodes again
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        # Begin BFS search
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res

                # Now get the words that form the pattern
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neighborWord in nei[pattern]:
                        if neighborWord not in visit:
                            q.append(neighborWord)
                            visit.add(neighborWord)

            res += 1
        
        return 0
                    

