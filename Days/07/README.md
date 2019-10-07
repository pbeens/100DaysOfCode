# Day 7

## Today's Goals

To do more Hackerrank challenges.

## What I Learned

Today I reinforced the basic data types including lists, dictionaries, and tuples by completing a number of [Hackerrank](https://www.hackerrank.com) challenges.

One thing that caught me in list processing was that `'10'` comes before `'2'` when sorted (because they're strings, not numbers), so I had to make sure to convert the numbers to integers (`int(n)`) before appending to or inserting into a list.

I learned that the `hash()` function only accepts immutable objects, so if you want to hash a list (which is mutable) you have to convert it to a tuple. [[006-Tuples](../../Hackerrank/02-Basic-Data-Types/006-Tuples.py)]

See the [Hackerrank folder](../../Hackerrank/) for today's work.
