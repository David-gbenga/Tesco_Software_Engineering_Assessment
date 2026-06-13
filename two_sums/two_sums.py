from typing import List


def two_sum(taskDurations: List[int], slotLength: int) -> List[int]:
    """
    Return the indices of two elements whose values sum to slotLength.

    If no such pair exists, return [-1, -1].

    Args:
        taskDurations: List of positive integers.
        slotLength: Target sum.

    Returns:
        A list containing two indices, or [-1, -1] if no pair exists.
    """

    # Dictionary to store numbers we have already seen.
    # Key: task duration
    # Value: index of that task duration
    seen = {}

    # Loop through the list with both index and value.
    for index, duration in enumerate(taskDurations):

        # Calculate the value needed to reach the target.
        complement = slotLength - duration

        # If the complement already exists in seen,
        # we have found two values that sum to slotLength.
        #Note that the code does not return the [seen[complement], index ] on the first go
        #Because the seen dict is empty
        if complement in seen:
            return [seen[complement], index]

        # Store the current duration and its index for future checks.
        seen[duration] = index

    # If the loop finishes without finding a pair, return [-1, -1].
    return [-1, -1]