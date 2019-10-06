# Day 6

## Contents

- [Today's Goal(s)](#today-s-goal-s-)
- [What I Learned](#what-i-learned)
  * [Maintaining This Site](#maintaining-this-site)
  * [List Comprehension](#list-comprehension)
  * [Day 2 Challenge](#day-2-challenge)
  * [Hackerrank](#hackerrank)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## Today's Goal(s)

1. To make maintaining this site more efficient.
1. To do more list comprehension lessons.
1. Finish the day 2 challenge!
1. Do some other challenges

## What I Learned

### Maintaining This Site

Maintaining this site was too time-consuming, with too much duplication of words and concepts, so I'm in the process of simplifying it. Namely, I'm reducing the sections on these pages from:

- Goal
- My Approach
- Solution, and
- What I Learned.

...to just:

- Goal(s), and
- What I Learned.

You'll notice Goal changed to Goal(s) because I often want to cover more than one topic in a day.

In addition, I'm greatly simplifying what I put on the main [README.md](../../README.md) file and just pointing the reader to these daily pages instead. The main page will have a very concise summary only.

### List Comprehension

I got sidetracked by the Hackerrank challenges. Perhaps I'll come back to this if the need arises.

### Day 2 Challenge

The [challenge website](https://www.pythonmorsels.com/exercises/cb8fbdd52cf14f8cb31df4f0634) (subscription needed) listed these resources to help with the two bonuses.

- [How to loop with indexes in Python](http://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/)
- [Multiple assignment and tuple unpacking improve Python code readability - Trey Hunner](https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/)
- [Python List Comprehensions: Explained Visually - Trey Hunner](https://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/)
- [Asterisks in Python: what they are and how to use them - Trey Hunner](https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/#Asterisks_for_packing_arguments_given_to_function)
- [What does ** (double star/asterisk) and * (star/asterisk) do for parameters?](https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters/36908#36908)
- [Manually raising (throwing) an exception in Python](https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python)

The last one proved beneficial to review how to throw exceptions.

I wrote a test program to develop a function to test for inconsistencies in matrix lengths. See [test-sublist-lengths.py](test-sublist-lengths.py).

I think I've got the program working to where I want it to. I'm having trouble with Bonus 2 because I'm not understanding how to use the test file they provided. I could ask about it in a forum I'm sure but I just want to get on with some other challenges.

### Hackerrank

For some other challenges, I've decided to use Hackerrank as it's a site I've used in the past and have been impressed with the quality of the challenges and the interface. 

Just for fun, I decided to start right at the beginning of their Python challenges which starts at Hello World but then ramps up fairly quickly. For me, it's an excellent review.

So far I've completed all the Introduction section and three of the Basic Data Types challenges. (See this [folder](../../Hackerrank/))

If you're wondering what the [filename.py](..\..\Hackerrank\filename.py) file is, it's a quick utility I wrote for generating filenames for the challenges and the screenshots I'm saving. You'll note that it uses [f-strings](https://realpython.com/python-f-strings/), which I'm a big fan of.
