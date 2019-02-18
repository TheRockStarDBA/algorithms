""" 68. Text Justification - Hard
Topic: string

Given an array of words and a width maxWidth, format the text such that each line
has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as
you can in each line. Pad extra spaces ' ' when necessary so that each line has
exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the
number of spaces on a line do not divide evenly between words, the empty slots
on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is
inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Example 1:
Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains
             only one word.

Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
 """


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        start, end = 0, 0
        numChar, numSpace = 0, 0
        for i, word in enumerate(words):
            if len(word) + numChar + end - start > maxWidth:
                if end - start == 1:  # if there is only one word in a line.
                    result.append(words[start] + ' ' * (maxWidth - numChar))
                else:
                    numSpace = maxWidth - numChar
                    space, extra = divmod(numSpace, end - start - 1)
                    for j in range(extra):
                        words[start + j] += ' '
                    result.append((' ' * space).join(words[start:end]))
                numChar = 0
                start = end = i
            end += 1
            numChar += len(word)
        result.append(' '.join(words[start:end]) + ' ' * (maxWidth - numChar -
                                                          (end - start - 1)))

        return result


if __name__ == "__main__":
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    result = Solution().fullJustify(words, maxWidth=16)
    print(result)