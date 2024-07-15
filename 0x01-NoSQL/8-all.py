#!/usr/bin/env python3
""" lists all documents """


def list_all(mongo_collection):
    """
    Retrieve all documents from the given MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
        collection to retrieve documents from.

    Returns:
        list: A list of documents retrieved from the collection.
        If no documents are found, an empty list is returned.
    """
    docs = mongo_collection.find()
    return docs if docs else []
