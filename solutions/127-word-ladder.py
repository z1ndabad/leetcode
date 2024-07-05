from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:

        # Generate a list of each possible character replacement position for a word
        # e.g. 'hot' -> ['*ot', 'h*t', 'ho*']
        def get_templates(word) -> list[str]:
            res = []
            for i in range(len(word)):
                letter_change = word[:i] + '*' + word[i + 1:]
                res.append(letter_change)
            
            return res
        
        swap_templates = defaultdict(list)
        
        for word in wordList:
            templates = get_templates(word)
            for template in templates:
                swap_templates[template].append(word)

        # BFS, where we find neighbors by finding words with templates in common with
        # the current node -- i.e. changing one letter in the current word gets us to
        # the neighboring word
        queue = deque()
        visited = set()
        current_layer = 1
        next_layer = 0
        depth = 1


        queue.appendleft(beginWord)
        visited.add(beginWord)

        while queue:
            current = queue.pop()
            current_templates = get_templates(current)
            current_layer -= 1

            for template in current_templates:
                for neighbor in swap_templates[template]:
                    if neighbor == endWord:
                        return depth + 1

                    if neighbor not in visited:
                        queue.appendleft(neighbor)
                        visited.add(neighbor)
                        next_layer += 1

            if current_layer == 0:
                current_layer = next_layer
                next_layer = 0
                depth += 1
    
        return 0

# Woof! Given a beginWord, an endWord, and a list of possible intermediary
# words, return the length of the shortest sequence to transform beginWord
# into endWord, where at every stage you can only change a single letter
# to transform the current word into one of wordList
#
# i.e. beginWord = 'cat', endWord = 'bar', wordList = [car, mat]
# Shortest path is cat -> car -> bar, return 3
#
# We're talking about shortest paths so this is a graph question. Every word
# in nodeList is a node, and edges exist where there is a legal move from one
# word to the next. Transitions are bidirectional and have no cost, so the
# graph is undirected and unweighted.
#
# We need to (1) build this graph and (2) find the shortest path via BFS from
# startWord to endWord.
#
# NOTICE that every neighbor of the current word is a word you can create by
# changing 1 letter in the word. We need a way to identify which words you
# can create from a given word.
#
# NOTICE that if two words are adjacent, they must have all characters except
# the one being swapped in common. 'Cat' and 'Cot' have 'C*t' in common, 'Cat'
# and 'Bat' have '*at' in common. So we need to enumerate these intermediate
# states for every word. Then while processing each word in BFS, we need to
# see which words share the same intermediate state.
#
# i.e. wordList is an IMPLICIT GRAPH, the same way a grid is an implicit graph
# where the neighbors are the current cell + all legal movement vectors. Here
# neighbors are all words in wordsList that share an intermediate state with
# the current word. Look at grid-bfs.py for the grid algo.
#
# Helper function get_templates returns a list of all possible templates for
# a given word. It iterates len(word) times per call and uses substrings to
# replace characters in the word, which is equivalent to a nested loop. So
# the helper takes O(M^2) where M is the length of each word.
#
# We create a dict mapping every possible intermediate state in wordList to the
# list of words described by that state -- 'c*t': ['cat', 'cut', 'cot']. This
# takes N iterations where N is the length of wordList. O(M^2 * N) so far.
#
# Then we run a normal BFS starting from beginWord. We find neighbors by
# finding the intermediary states of the current node, iterating over
# all of them, and doing a nested iteration over the words mapped to each
# intermediary state in the dict. 
# 
# If an intermediary state is shared with endWord, we can return. We use
# variables to track the # words to be explored in the current layer of the
# graph, # words in the next layer, and the depth. For every neighbor found,
# increment next_layer by 1. When current_layer == 0, set current_layer to
# next_layer and increment depth. 
# 
# Depth will always track the distance of
# the current node from the origin, so return depth + 1 since we return
# before processing (popping) the end node. Look at 
# https://www.youtube.com/watch?v=KiCBXu4P-2Y for the same approach applied
# to a grid.
# 
# In the BFS, getting the intermed. states takes M^2, and in the worst case we
# visit every word for N while loop iterations, so BFS takes O(M^2 * N) as 
# well.
#
# Time complexity = O(NM^2) to build the dict, O(NM^2) to perform BFS, for
# a result of O(NM^2).

