from .imports import *


@register.filter(name='get_uni_docs')
def get_uni_docs(uni, doc_or_com):
    docs = ''
    doc_list = json.loads(doc_or_com)
    i = 0
    while i < len(doc_list):
        if i < len(doc_list):
            docs += '\r\n'
        docs += doc_list[i]
        i += 1
    return docs
