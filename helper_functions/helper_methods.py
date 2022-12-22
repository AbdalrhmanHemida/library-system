def numbering_items(items):
    items = [f'{idx + 1}) {msg}' for idx, msg in enumerate(items)]
    return items


