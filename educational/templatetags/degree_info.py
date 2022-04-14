from .imports import *


@register.filter(name='get_degree_doc')
def get_degree_doc(degree):
    if degree.document == '':
        return ''
    docs = ''
    doc_list = degree.document.split('\r\n')
    i = 0
    while i < len(doc_list):
        if i < len(doc_list):
            docs += '\r\n'
        docs += doc_list[i]
        i += 1
    return docs
