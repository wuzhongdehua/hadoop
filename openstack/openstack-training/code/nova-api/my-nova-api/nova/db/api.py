#���ݲ���API�ṩ�ķ�������Nova API �������������Ӧ�Ĳ����� �������������������е���
def document_get(context, document_id):
    """Get a document or raise if it does not exist."""
    return IMPL.document_get(context, document_id)