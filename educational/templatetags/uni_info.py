from .imports import *


@register.filter(name='get_uni_docs')
def get_uni_docs(uni, doc_or_com):
    if doc_or_com == '':
        return ''
    docs = ''
    doc_list = doc_or_com.split('\r\n')
    i = 0
    while i < len(doc_list):
        if i < len(doc_list):
            docs += '\r\n'
        docs += doc_list[i]
        i += 1
    return docs
