#!/usr/bin/env python3
""" changes all topics of a school document """


def update_topics(mongo_collection, name, topics):
    """
    Update the topics of a school document in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The
        MongoDB collection.
        name (str): The name of the school document to update.
        topics (list): The new list of topics for the school document.

    Returns:
        None
    """
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
