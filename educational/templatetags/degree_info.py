from .imports import *


@register.filter(name='get_degree_doc')
def get_degree_doc(degree):
    docs = ''
    doc_list = json.loads(degree.document)
    i = 0
    while i < len(doc_list):
        if i < len(doc_list):
            docs += '\r\n'
        docs += doc_list[i]
        i += 1
    return docs
