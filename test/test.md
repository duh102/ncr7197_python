# Header tests

These tests are for the various levels of header

# Header 1

Some text

## Header 2

Some more text 

### Header 3

Yet more text

#### Header 4

I don't think we support any further than 4

##### Header 5

But we'll try it!

# Lists and Wrapping

In these tests we'll verify lists and nesting, as well as line wrapping. Because the NCR7197 is limited to 44 columns, we have to wrap often when we start in on lists and large paragraphs. This description is much wider than the 44 columns that the NCR7197 can print, so it should be wrapped and indented properly.

This is a new paragraph, which is also too long for the 44 columns, so it should be wrapped appropriately.

Meanwhile, here's a list:
* Item 1
* Item 2
* Item 3
  1. Item 3's subitem 1
  2. Item 3's subitem 2
  3. A particularly long subitem that will wrap because it's a paragraph. This will render as a nicely formatted paragraph where the second and subsequent lines will be aligned to the first line's start.
    * Deeper nesting!
      * Even deeper
        * The deepest
* Item 4
  * Item 4's subitem

# Text Styling

This is a bunch of tests around various types of text styling.

For example, this text should be **bold**, while this should be *italic*, and this `code` should be rendered a bit special.
Finally, here's a ***bold and italic*** section.

If you want, you can visit [this link](www.google.com) to go to Google.

# Quotes and Code Tags

> This quote should be indented and have a decoration to the side the indicate that it's a quote

```
Whereas this is code and should be centered
```

# Horizontal line

This ends the test

---

If there's not a line above this text, you've failed!
