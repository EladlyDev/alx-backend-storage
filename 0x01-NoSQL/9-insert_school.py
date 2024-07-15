#!/usr/bin/env python3
""" inserts a new document """


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into the specified MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
        collection to insert the document into.
        **kwargs: Additional keyword arguments representing the
        fields and values of the document to be inserted.

    Returns:
        The _id of the newly inserted document.

    """
    return mongo_collection.insert_one(kwargs).inserted_id
