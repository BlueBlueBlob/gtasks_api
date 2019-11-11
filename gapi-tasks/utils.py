import iso8601


def parse_date(input_value):
    if input_value is None:
        return None
    return iso8601.parse_date(input_value)
