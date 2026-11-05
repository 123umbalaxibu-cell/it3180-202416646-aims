def search_by_category(items, category):
    """Return the DVDs that belong to a category."""
    return [dvd for dvd in items if category.lower() in dvd.category.lower()]


def search_by_title(items, keyword):
    """Return the DVDs whose title contains keyword."""
    return [dvd for dvd in items if keyword.lower() in dvd.title.lower()]