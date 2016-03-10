#!/usr/bin/env python
# coding=utf-8

import pdfkit


css = ['reset.css', 'base.css', 'common.css',
 'body.css', 'main.css', 'custom.css', 'global.css',
 'validationEngine.jquery.css', 'template.css',
 'uploadify.css', 'zTreeStyle.css']


def main():
    print 'begin'
    pdfkit.from_file('test.html', 'out.pdf')
    pdfkit.from_file('per pagae.html', 'out2.pdf')
    print 'end'


if __name__ == '__main__':
    main()
