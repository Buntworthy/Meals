# Meals

Meals is a small command line program written in Python to help keep, organise, and search a list of meals.

## Motivation

This is not a recipe organiser, instead it serves as a small, searchable list of meal ideas. Meals can be tagged, searched, or suggested at random (soon). This is all currently done via a command line interface, (but maybe one day a small flask app to serve a web interface might be something I'll do).

## Usage

### Add an item

Add a meal idea using the `add` keyword. Type the title and a series of extra
tags following a comma. Meals are stored with a numeric index which can be used
to refer to that entry.

```python
>>> add Super tasty meal, delicious vegetarian
Added: [45] - Super tasty meal
```

### Searching

#### Searching by tag

The `search` command will search for a list of words in the tags and titles
of all the entries. (Actually all the words from the title are added to the
list of tags, so this is just a tag search). Search terms are combined in
an *and* sense

```python
>>> search aubergine tomato

Results:
[1] - Some meal
[2] - Some other meal
[5] - A different aubergine meal

```
Use the `-v` modifier to display all the (non title) tags associated with each
of the entries

```python
>>> search -v aubergine tomato

Results:
[1] - Some meal, aubergine pasta vegetarian tomato
[2] - Some other meal, tomato dessert aubergine
[5] - A different aubergine meal, pie aubergine vegetarian tomato

```

#### Searching by title

Search only titles using the `search_title` command.

```python
>>> search_title different aubergine meal

Results:
[5] - A different aubergine meal, pie aubergine vegetarian tomato

```

### Edit an item

```python
>>> search aubergine

Results:
[1] - Some meal
[2] - Some other meal
[5] - A different aubergine meal

>>> add_tag 1 pasta dinner
>>> remove_tag 1 pasta
```

Only adding and removing tags is available. To change a title, you have to
delete the item and make a new one for now.

### Delete an item

```python
>>> search aubergine

Results:
[1] - Some meal
[2] - Some other meal
[5] - A different aubergine meal

>>> delete 1
Are you sure? (y/n)
>>> y
Item 1 deleted.

Results:
[2] - Some other meal
[5] - A different aubergine meal

```
