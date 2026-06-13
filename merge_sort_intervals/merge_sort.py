from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merge overlapping intervals and return a sorted list of non-overlapping intervals.

    Two intervals overlap if the start of the current interval is less than or equal
    to the end of the previous merged interval.

    Example:
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        output = [[1, 6], [8, 10], [15, 18]]

    Args:
        intervals: A list of intervals, where each interval is [startTime, endTime].

    Returns:
        A sorted list of merged, non-overlapping intervals.

    Raises:
        TypeError: If intervals is not a list or if any interval is not a list.
        ValueError: If any interval does not contain exactly two values,
                    or if startTime is greater than endTime.
    """

    # Validate that the main input is a list.
    if not isinstance(intervals, list):
        raise TypeError("intervals must be a list of [startTime, endTime] pairs")

    # If there are no intervals, there is nothing to merge.
    if not intervals:
        return []

    # Validate every interval before processing.
    for interval in intervals:
        # Each interval should be a list, for example [1, 3].
        if not isinstance(interval, list):
            raise TypeError("each interval must be a list")

        # Each interval must contain exactly two values: startTime and endTime.
        if len(interval) != 2:
            raise ValueError("each interval must contain exactly two values")

        start_time, end_time = interval

        # Start and end times should be integers.
        if not isinstance(start_time, int) or not isinstance(end_time, int):
            raise TypeError("startTime and endTime must be integers")

        # An interval such as [5, 2] is invalid because it starts after it ends.
        if start_time > end_time:
            raise ValueError("startTime cannot be greater than endTime")

    # Sort intervals by start time.
    # Example:
    # [[8, 10], [1, 3], [2, 6]] becomes [[1, 3], [2, 6], [8, 10]]
    sorted_intervals = sorted(intervals, key=lambda interval: interval[0])

    # Initialize the merged list with the first sorted interval.
    # Use copy() so we do not mutate the original input interval object.
    merged = [sorted_intervals[0].copy()]

    # Start from the second interval and compare each one with the last merged interval.
    for current_start, current_end in sorted_intervals[1:]:

        # Get the most recently merged interval.
        last_merged = merged[-1]

        # If the current interval starts before or exactly when the last merged interval ends,
        # then the two intervals overlap or touch.
        if current_start <= last_merged[1]:
            # Merge by extending the end time if the current interval ends later.
            last_merged[1] = max(last_merged[1], current_end)

        else:
            # If there is no overlap, add the current interval as a new separate interval.
            merged.append([current_start, current_end])

    return merged



if __name__ == "__main__":
    k = [[1, 3], [2, 6], [8, 10], [15, 18]]
    
    result = merge_intervals(k)
    
    print(result)