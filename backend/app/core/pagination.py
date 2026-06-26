def paginate(
    page: int,
    size: int
):

    offset = (
        page - 1
    ) * size

    return offset, size