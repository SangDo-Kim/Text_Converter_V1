"""# String to tree V1.1
This module get tab indented string and convert it into so-called hierarchy table (a nested list),
and then build hierarchy structure (a tree) using class methods and recursive calls,
and then make a dictionary out of it.

There are two classes:
TreeNode: Holds data of a node.
BuildTree: Create and hold a list of TreeNode instances and provides a method to return dictionary.
    BuildTree.tree_nodes -> a list of instances of TreeNode. The root is the list's first element.
    A dictionary is limited to 3 level nesting, while tree structure itself is not limited.

Methods in BuildTree:
string_to_table: Tab indented string -> hierarchy table (a nested list).
build_tree_from_table: Hierarchy table -> Tree structure (list of TreeNode instances)
make_dict: Tree structure -> dictionary
string_to_dict: Tab indented string -> dictionary (it calls a few methods mentioned above)

Pre-made instance in the module: build_tree
You can just from string_to_tree import build_tree.

V1.0
- Initial creation

V1.1
- Put functions into class.
- Bug fixes (Handles IndexError and others).
"""
import re


class TreeNode:
    def __init__(self, serial_no: int, name: str, level: int, parent=None):
        self.serial_no = serial_no
        self.name = name
        self.level = level
        self.parent = parent
        self.children = []


class BuildTree:
    def __init__(self):
        # Add root instance to tree node.
        self.tree_nodes = [TreeNode(0, "root", 0)]
        self.depth = 0

        # Hierarchy table, a nested list in which each sub-list is like [grandparent name, parent name, name].
        self.table = []

    def build_tree_from_table(self):
        self.tree_nodes = [TreeNode(0, "root", 0)]
        level = 0
        name = ""
        parent = 0
        parents_list = []

        # Get the depth of the table
        self.depth = len(max(self.table, key=len))

        # Build a tree
        for line_no, line in enumerate(self.table):
            for i in range(len(line) - 1, -1, -1):
                if line[i] is not None:
                    level = i + 1
                    name = line[i]
                    if level == 1:
                        parent = 0
                        parents_list = [line_no + 1]
                    else:
                        parent = parents_list[(level - 2)]

                    # Setting parents_list
                    if level > len(parents_list):
                        parents_list.append(line_no + 1)
                    elif level == len(parents_list):
                        parents_list[(level-1)] = line_no + 1
                    else:
                        parents_list = parents_list[:(level-1)]

                    break
            node = TreeNode(line_no + 1, name, level, parent)
            self.tree_nodes.append(node)

        # Populate children from the root
        self.make_children_list(0)

    def get_node(self, serial_no):
        return self.tree_nodes[serial_no]

    def string_to_table(self, string):
        # Make a 2-level nested list, so-called hierarchy table.
        # Each sub-list in the list is like ["parent's parent", "parent", "item", None] if it is a level 3 node,
        # or just ["item", None, None, None] if it is a level 1 node.

        self.table = []
        lines = string.strip().splitlines()
        if len(lines) == 0:
            return None

        # Determine the maximum depth of the tree structure.
        if string.find("\t") > 0:
            max_tabs = max(len(match) for match in re.findall(r'(\t+)', string))
            self.depth = max_tabs + 1
        elif len(string.strip()) > 0:
            self.depth = 1
        else:
            self.depth = 0

        # Specify parents in each line in lines
        list_with_parents = [None for i in range(self.depth)]
        lines_with_parents = []
        for line in lines:
            items = line.split("\t")
            items_level = len(items)
            # Ex: item == [parent, item]
            list_with_parents[items_level - 1] = items[-1]
            if items_level < self.depth:
                for i in range(items_level, self.depth):
                    list_with_parents[i] = None

            # Append a copy of a list
            lines_with_parents.append(list_with_parents[:])
        self.table = lines_with_parents

    def make_children_list(self, serial_no):
        children_list = []

        for node in self.tree_nodes:
            if node.parent == serial_no:
                children_list.append(node.serial_no)

        if len(children_list) == 0:
            return None
        else:
            self.tree_nodes[serial_no].children = children_list

        for child in self.tree_nodes[serial_no].children:
            self.make_children_list(child)

    def make_dict(self) -> {}:
        _dict = {}
        for node in self.tree_nodes[1:]:
            parent = self.get_node(node.parent)
            sibling_list = parent.children
            if node.level == 1:
                if len(node.children) > 0:
                    _dict[node.name] = {}
                else:
                    _dict[node.name] = None
            elif node.level == 2:
                if len(node.children) > 0:
                    _dict[parent.name][node.name] = {}
                else:
                    if len(sibling_list) > 1:
                        _dict[parent.name][node.name] = None
                    else:
                        _dict[parent.name] = node.name
            elif node.level == 3:
                grandparent = self.get_node(parent.parent)
                _dict[grandparent.name][parent.name] = node.name
            else:
                # If node.level > 3, this function doesn't support it.
                break

        return _dict

    def string_to_dict(self, string) -> {}:
        try:
            self.string_to_table(string)
        except IndexError:
            return {r"IndexError: The hierarchy structure of the source text may be invalid (string_to_table method)."
                    : None}

        try:
            self.build_tree_from_table()
        except IndexError:
            return {r"IndexError: The hierarchy structure of the source text may be invalid (build_tree_from_table)."
                    : None}

        try:
            _dict = self.make_dict()
        except TypeError:
            return {r"TypeError: The hierarchy structure of the source text may be invalid (make_dict).": None}

        return _dict


build_tree = BuildTree()


if __name__ == "__main__":
    sample_string = (
        "Kitchen\n\tCutting Board\n\tKnife Set\n\t\tShort knife\nLiving Room\n\tSofas\nBedroom"
    )

    my_dict = build_tree.string_to_dict(sample_string)
    print(my_dict)