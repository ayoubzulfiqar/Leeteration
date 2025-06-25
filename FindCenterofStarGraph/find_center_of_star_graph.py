```python
def findCenter(edges):
    """
    Find the center of a star graph.

    Args:
        edges (list of list of int): A list of edges in the star graph.

    Returns:
        int: The center of the star graph.
    """
    return edges[0][0] if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1] else edges[0][1]

```