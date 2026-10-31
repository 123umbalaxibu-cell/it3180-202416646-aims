def search_by_title(items, keyword):
    """Return the DVDs whose title contains keyword."""
    return [dvd for dvd in items if keyword in dvd.title]
