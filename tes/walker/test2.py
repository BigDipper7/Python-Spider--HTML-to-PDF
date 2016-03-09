#!/usr/bin/env python
# coding=utf-8
import urllib2


def main():
    url = 'http://www.baidu.com'
    response = urllib2.urlopen(url)
    html = response.read()

    print 'begin saving'
    print html

    write_str_to_file(html, 'test2.html')

    print 'save finished'



def write_str_to_file(content,filename = None):
    with open(filename if not filename else 'test.html', 'w') as f_open:
        f_open.write(content)


if __name__ == '__main__':
    main()
