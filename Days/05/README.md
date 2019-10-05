# Day 5

## Contents

- [Today's Goal](#today-s-goal)
- [My Approach](#my-approach)
- [Solutions](#solutions)
  * [Blog CSS](#blog-css)
  * [Auto-formatting Python in VS Code](#auto-formatting-python-in-vs-code)
  * [List Comprehension](#list-comprehension)
- [What I Learned](#what-i-learned)
  * [Blog CSS](#blog-css-1)
  * [Auto-formatting Python in VS Code](#auto-formatting-python-in-vs-code-1)
  * [List Comprehension](#list-comprehension-1)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## Today's Goal

I still want to do more list comprehension exercises. Hopefully I can find some that are more advanced.

I want to figure out how to get VS Code to auto-format my Python code.

## My Approach

[Google](https://www.google.com/search?hl=en&as_q=list+comprehension++python&as_epq=&as_oq=challenges+exercises) is my friend, hopefully.

## Solutions

### Blog CSS

I got a little distracted today playing with the CSS on my blog. Headers had too much spacing around them. With some research, I added this CSS to the appearance section of my WordPress blog:

```css
.entry-content h2 {
    color: #000000;
	margin-top: -30px;
	margin-bottom: 0px;
    line-height: 2;
}

.entry-content h3 {
    color: #000000;
	margin-top: -30px;
	margin-bottom: 0px;
    line-height: 2;
}

.entry-content p {
    color: #000000;
	margin-top: 4px;
	margin-bottom: 20px;
    line-height: 2;
}
```

### Auto-formatting Python in VS Code

This wasn't on my goal list for today but it was frustrating me that I couldn't auto-format my Python code like could in PyCharm.

The solution was found [here](https://donjayamanne.github.io/pythonVSCodeDocs/docs/formatting/). I continue to be impressed with VS Code, particularly all the options available in it. 

### List Comprehension

- [Python List Comprehension (With Examples)](https://www.programiz.com/python-programming/list-comprehension)

*More forthcoming...*

## What I Learned

### Blog CSS

My CSS knowledge is very limited. Fortunately there are lots of great resources available to help when needed.

### Auto-formatting Python in VS Code

These are the settings I changed to get VS Code to auto-format my Python code:

```
"editor.formatOnSave": true`
"python.formatting.provider": "autopep8"
```
[[Source](https://donjayamanne.github.io/pythonVSCodeDocs/docs/formatting/)]

### List Comprehension

I came across this great animation that is perfect for demonstrating how list comprehensions are assembled:

> ![list comprehension](list-comprehension-condition.gif)
<br>[[Credit](https://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/)]

This site helped me tremendously with flattening and recreating matrices:

- [Python List Comprehensions: Explained Visually - Trey Hunner](https://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/)

This site helped me add the individual elements of each list:

- [Nested list comprehension with two lists](https://stackoverflow.com/questions/16568056/nested-list-comprehension-with-two-lists)

With these resources I was able to make great progress on my Day 2 challenge but it's not quite perfect yet. It will add matrices with sub-lists of len=2 but not others. I'll work on that next day...

View my updated Jupyter notebook of exercises [here](https://colab.research.google.com/drive/1fbmH9yDS5fzFcxEZMnUzmb3qCqGQoaEv). See the Resource 2 section for the code applicable to what I did today.

View my Python code for the Day 2 challenge here in the Day 2 folder. Remember, as of today, it's incomplete.

