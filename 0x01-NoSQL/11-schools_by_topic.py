#!/usr/bin/env python3
""" returns the list of school having a specific topic """


def schools_by_topic(mongo_collection, topic):
    """
    Retrieve a list of schools that have a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The MongoDB collection to query.
        topic (str): The topic to search for.

    Returns:
        list: A list of school documents that have the specified topic.
    """
    return mongo_collection.find({'topics': topic})
