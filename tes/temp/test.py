#!/usr/bin/env python
# coding=utf-8

import pdfkit


css = ['reset.css', 'base.css', 'common.css',
 'body.css', 'main.css', 'custom.css', 'global.css',
 'validationEngine.jquery.css', 'template.css',
 'uploadify.css', 'zTreeStyle.css']


def main():
    print 'begin'
    pdfkit.from_file('中国及多国专利审查信息查询.html', 'out.pdf', css = css)
    print 'end'


if __name__ == '__main__':
    main()
