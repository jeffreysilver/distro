def paginate(data, limit=None, offset=None):
    if offset:
        data = data[offset:]

    if limit:
        data = data[:limit]

    return data
