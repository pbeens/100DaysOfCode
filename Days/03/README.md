# Day 3

I need to learn more about list comprehension in Python.

## My Approach

I'll be watching videos and finding websites related to this and then trying (and making up) some examples to learn from.

## Solution

List comprehension resource used:

- [List Comprehensions in Python](https://www.pythonforbeginners.com/basics/list-comprehensions-in-python)

I've created a [Jupyter notebook](https://colab.research.google.com/drive/1fbmH9yDS5fzFcxEZMnUzmb3qCqGQoaEv) to learn about list comprehension. The resources used are documented in the notebook as well as in the [links](..\..\Links.md) file.

I also used this resource to reinforce how to use `join()`:

- [Python | Merge list elements - GeeksforGeeks](https://www.geeksforgeeks.org/python-merge-list-elements/)

## What I Learned

VS Code doesn't wort nicely with Jupyter notebooks. Yes, it can work, but it's not friendly. (So I'm using [Colaboratory](https://colab.research.google.com/drive/1fbmH9yDS5fzFcxEZMnUzmb3qCqGQoaEv) instead.)

List comprehension is a valuable tool once you grasp it. The basic format is: 

```Python
new_list = [expression(i) for i in old_list if filter(i)]
```

List comprehension is not always more efficient than the traditional way of manipulating lists, but if you have to do anything with lists that can't be done in a single line (or two) you should consider using list comprehension.

> **See my Jupyter notebook [here](https://colab.research.google.com/drive/1fbmH9yDS5fzFcxEZMnUzmb3qCqGQoaEv).**
