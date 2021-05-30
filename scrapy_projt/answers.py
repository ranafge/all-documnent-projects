## What happens? ##

You grab all the `<li>` and try to print a `title`, but `<li>` do not have a `title`

It is the `<a>` that contains a `title`, so print:

    print(b.a["title"])


**Example**

    import requests
    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    res = requests.get('https://en.wikipedia.org/wiki/List_of_programming_languages')

    soup = BeautifulSoup(res.text, 'lxml')

    for a in soup.find_all('div',{'class':'div-col'}):
        for b in a.find_all('li'):
            print(b.a["title"])

**Output**

    A Sharp (.NET)
    A-0 System
    A+ (programming language)
    ABAP
    ABC (programming language)
    ABC ALGOL
    ACC (programming language)
    Accent (programming language)
    Distributed Application Specification Language
    Action! (programming language)
    ActionScript
    Actor (programming language)
    ...

## Alternativ ##

To avoid the second loop use [css selectors](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors):

    for a in soup.select('div.div-col  li  a'):
        print(a['title'])bv


## What happens? ##

The text you are looking for is not part of the `<li>` it is an separate `text node` so you wont get it.

## How to fix that? ##

To get the text node use `next_sibling` on your `find()` and to avoid spaces,... `strip()` the result.

    soup.find('i', class_='material-icons').next_sibling.strip()


**Minimal example**

    from bs4 import BeautifulSoup

    html = '''
    <li class="some-class">
        <i class="material-icons">location_on</i>     some text
    </li>
    '''
    soup = BeautifulSoup(html, 'lxml')

    soup.find('i', class_='material-icons').next_sibling.strip()

**Output**

> some text


