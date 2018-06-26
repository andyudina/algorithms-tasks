"""
Find shortest route from one node to another
"""
import unittest


def _find_shortest_route_recursive(
        graph, current_route, target_node):
    """
    Recursive function to find shortest route to taget node
    """
    def _get_min_route(routes):
        """
        Return shortest route or None if such route can
        can not be found
        """
        shortest_route = None
        for route in routes:
            if route is None:
                continue
            elif shortest_route is None or \
                    len(route) < len(shortest_route):
                shortest_route = route
        return shortest_route

    current_node = current_route[-1]
    possible_routes = []
    for node in graph[current_node]:
        # we found the route till the destination
        # and can return it
        if node == target_node:
            return current_route + [node, ]
        # we foound a loop
        # we should discard this route
        if node in current_route:
            continue
        possible_routes.append(current_route[:] + [node, ])
    return _get_min_route(
        [
            _find_shortest_route_recursive(
                graph, route, target_node)
            for route in possible_routes
        ])

def find_shortest_route(
        graph, current_node, target_node):
    """
    Find shortest route from one node to another. 
    Graph is a dictionary with nodes in keys and lists of 
    closest nodes as values
    Return list with nodes that form shortest path or None
    """
    return _find_shortest_route_recursive(
        graph,
        [current_node, ],
        target_node)


class TestFindShortestRoute(
        unittest.TestCase):
    """
    Test find_shortest_route function
    """

    def test_shortest_route_found(self):
        """
        We return valid shortest route
        """
        graph = {
            'Min'     : ['William', 'Jayden', 'Omar'],
            'William' : ['Min', 'Noam'],
            'Jayden'  : ['Min', 'Amelia', 'Ren', 'Noam'],
            'Ren'     : ['Jayden', 'Omar'],
            'Amelia'  : ['Jayden', 'Adam', 'Miguel'],
            'Adam'    : ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
            'Miguel'  : ['Amelia', 'Adam', 'Liam'],
            'Noam'    : ['Jayden', 'William'],
            'Omar'    : ['Ren', 'Min'],

        }
        self.assertListEqual(
            find_shortest_route(
                graph, 'Jayden', 'Adam'),
            ['Jayden', 'Amelia', 'Adam'])

    def test_shortest_route_found_loops_ignored(self):
        """
        We return valid shortest route and ignore loops
        """
        graph = {
            'a': ['c', 'b'],
            'b': ['a', 'g'],
            'g': ['b', 'k'],
            'k': ['g', 'l'],
            'l': ['k', ],
            'c': ['f', 'd'],
            'd': ['c', 'e'],
            'f': ['c', 'e'],
            'e': ['f', 'd'],
        }
        self.assertListEqual(
            find_shortest_route(
                graph, 'a', 'l'),
            [
                'a', 
                'b',
                'g',
                'k',
                'l',
            ])

    def test_no_route_found_none_returned(self):
        """
        We return None if no route found
        """
        graph = {
            'a': ['b', 'c'],
            'b': ['a', 'd'],
            'c': ['e', 'f'],
            'd': ['b', ],
            'e': ['c', ],
            'f': ['c', ],

            'g': ['k', ],
            'k': ['l', 'g'],
            'l': ['k', 'm', 'n'],
            'm': ['l', ],
            'n': ['l', ],
        }
        self.assertIsNone(
            find_shortest_route(
                graph, 'a', 'n'))

if __name__ == '__main__':
    unittest.main()
