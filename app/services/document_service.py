document = {"name": "Acme MSA", "year": 2026, "authorized": True}


def get_document_name(document):
    return document["name"]


def is_authorized(document):
    return document["authorized"]


def get_document_year(document):
    return document["year"]
