def find_difference(list1, list2):
    """
    Find the difference between two lists.

    Args:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
        list: A list containing elements that are in list1 but not in list2.
    """
    return [item for item in list1 if item not in list2]    