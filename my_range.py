def my_range(start, end, step=1):
    if start > end:
        while start > end:
            yield start
            start -= step
    elif start < end:
        while start < end:
            yield start
            start += step
    else:
        yield []
