# Day 5

## Today's Goal

I still want to do more list comprehension exercises. Hopefully I can find some that are more advanced.

I want to figure out how to get VS Code to auto-format my Python code.

## My Approach

[Google](https://www.google.com/search?hl=en&as_q=list+comprehension++python&as_epq=&as_oq=challenges+exercises) is my friend, hopefully.

## Solution

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

The solution was found [here](https://donjayamanne.github.io/pythonVSCodeDocs/docs/formatting/). I continue to be impressed with VS Code, particularly all the options available in it. 

### List Comprehension

- [Python List Comprehension (With Examples)](https://www.programiz.com/python-programming/list-comprehension)

*More forthcoming...*

## What I Learned

### Blog CSS

My CSS knowledge is very limited. Fortunately there are lots of great resources available to help when needed.

### Auto-formatting Python in VS Code

These are the settings I had to change:

```
"editor.formatOnSave": true`
"python.formatting.provider": "autopep8"
```
[[Source](https://donjayamanne.github.io/pythonVSCodeDocs/docs/formatting/)]

### List Comprehension

*forthcoming...*

## Consider

Any links to add to [Links.md](..\..\Links.md)? (delete this section afterwards)
