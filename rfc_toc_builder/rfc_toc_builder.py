#!/usr/bin/env python3
"""
To build Table of contents(toc) for older RFCs
:author: Vasanthakumar K
"""

import re, os

InFile = 'RFC3376.html'
OutFile = 'Updated_'+InFile
    
def get_toc():
    '''
    To get the toc content by using regex
    :return: headlineno (Line number which is used to insert toc content), content (toc content)
    '''
    pageNo = 1
    toc = ['<B>Table of Contents</B>\n']

    with open(InFile, 'r') as infile:
        lineno = 0
        for line in infile:
            lineno += 1
            page = re.match(r'.*Page ([0-9]*).*</span></pre>', line)
            if page:
                pageNo = int(page.group(1)) + 1
            match = re.match(r'<span class="h\d"><a class="selflink" name="(section-[0-9.]*)" href="#section-[0-9.]*">([0-9.]*)</a>([\w\W. ]*)</span>', line)
            if match:
                temp = '<a href="#section-{}">{}</a>{}...............<a href="#page-{}">{}</a>'.format(match.group(2), match.group(2), match.group(3), pageNo, pageNo)
                toc.append(temp)
                if (match.group(1) == 'section-1'):
                    headlineno = lineno
            appendix = re.match(r'<span class="h\d"><a class="selflink" name="(appendix-[A-Za-z0-9.]*)" href="#appendix-[A-Za-z0-9.]*">([\sA-Za-z0-9.]*)</a>([\w\W. ]*)</span>', line)
            if appendix:
                temp = '<a href="#appendix-{}">{}</a>{}...............<a href="#page-{}">{}</a>'.format(appendix.group(2), appendix.group(2), appendix.group(3), pageNo, pageNo)
                toc.append(temp)
                #print(temp)
            #if line == "</head>\n":
                #headline = lineno
        toc.append('\n')
        content = '\n'.join(toc)
        lengthofcontent = len(content)
        lengthoftoc = len(toc)
    return headlineno, content

def break_content(brekline):
    '''
    To break the file content as two halfs to insert toc content
    :return: contentfirst (before content of brekline), contentsecond (after content of brekline)
    '''
    with open (InFile, 'r') as re:
        lines = re.readlines()
        first = []
        second = []
        no = 1
        for line in lines:
            if no <= (brekline-1):
                first.append(line)
                no += 1
            else:
                second.append(line)
                no += 1
        contentfirst = '\n'.join(first).replace('\n\n', '\n')
        contentsecond = '\n'.join(second).replace('\n\n', '\n')
    return contentfirst, contentsecond

def update_toc(before_toc, toc_content, after_toc):
    '''
    To update the contents in new file
    '''
    with open(OutFile, 'w+') as w:
        w.write(before_toc)
        w.write(toc_content)
        w.write(after_toc)
    return "Updated Sucessfully...!"

if __name__=='__main__':
    brekline, toc_content = get_toc()
    before_toc, after_toc = break_content(brekline)
    print(update_toc(before_toc, toc_content, after_toc))
    
    

