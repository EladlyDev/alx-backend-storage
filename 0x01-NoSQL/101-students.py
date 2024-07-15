#!/usr/bin/env python3
""" returns all students sorted by average score """


def top_students(mongo_collection):
    """
    Retrieves all students from the given MongoDB collection and returns them sorted by average score.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection containing student data.

    Returns:
        list: A list of dictionaries representing the students, sorted by average score.
    """
    res = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ])
    return res
