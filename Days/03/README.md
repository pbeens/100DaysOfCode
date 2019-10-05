# Day 3

## Contents

- [Goal for Today](#goal-for-today)
- [What I Learned](#what-i-learned)
  * [GitHub Projects](#github-projects)
  * [Jupyter Notebooks and VS Code](#jupyter-notebooks-and-vs-code)
  * [List Comprehension](#list-comprehension)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## Goal for Today

I need to learn more about list comprehension in Python. I'll be watching videos and finding websites related to this and then trying (and making up) some examples to learn from.

## What I Learned

### GitHub Projects

I ended spent some time today learning about GitHub Projects (not a goal, I know!), which might be beneficial for this (#100DaysOfCode) and other projects I'm working on. Videos watched:

- [GitHub Project Management Tutorial - How To Use GitHub Projects & Automation](https://www.youtube.com/watch?v=ff5cBkPg-bQ)
- [Github Project Management 1](https://www.youtube.com/watch?v=RXEy6CFu9Hk)

I've discovered how to tie in GitHub Issues with Projects. Basically, you create a note in Projects and then turn it into an issue for tracking purposes. Nice. Now I just have to remember to use it.

### Jupyter Notebooks and VS Code

VS Code doesn't work nicely with Jupyter notebooks. Yes, it can work, but it's not friendly. (So I'm using [Colaboratory](https://colab.research.google.com/drive/1fbmH9yDS5fzFcxEZMnUzmb3qCqGQoaEv) instead.)

### List Comprehension

List comprehension is a valuable tool once you grasp it. The basic format is: 

```Python
new_list = [expression(i) for i in old_list if filter(i)]
```

List comprehension is not always more efficient than the traditional way of manipulating lists, but if you have to do anything with lists that can't be done in a single line (or two) you should consider using list comprehension.

List comprehension resource used:

- [List Comprehensions in Python](https://www.pythonforbeginners.com/basics/list-comprehensions-in-python)

I've created a [Jupyter notebook](https://colab.research.google.com/drive/1fbmH9yDS5fzFcxEZMnUzmb3qCqGQoaEv) to learn about list comprehension. The resources used are documented in the notebook as well as in the [links](../../Links.md) file.

I also used this resource to reinforce how to use `join()`:

- [Python | Merge list elements - GeeksforGeeks](https://www.geeksforgeeks.org/python-merge-list-elements/)
