"""# String to tree V1.0
This module get tab indented string and convert it into so-called hierarchy table (which is a nested list),
and then build hierarchy structure using class and recursive calling it, so-called tree,
and then make a dictionary out of it.
"""


def string_to_hierarchy_table(string) -> list:
    # Make a 2-level nested list, so-called hierarchy table.
    # Each sub-list in the list is like ["parent's parent", "parent", "item", None] if it is a level 3 node,
    # or just ["item", None, None, None] if it is a level 1 node.

    # Determine the maximum depth of the tree structure. A depth can be 1 ~ 100.
    lines = string.splitlines()
    depth = 1
    fail_count = 0
    for i in range(99):
        tap_string = "\n" + "\t" * i
        if string.find(tap_string) >= 0:
            depth = i + 1
        else:
            fail_count += 1
        if fail_count > 5:
            # if searching for the depth fails a few times, then stop.
            break

    # Specify parents in each line in lines
    list_with_parents = [None for i in range(depth)]
    lines_with_parents = []
    for line in lines:
        items = line.split("\t")
        items_level = len(items)
        # Ex: item == [parent, item]
        list_with_parents[items_level - 1] = items[-1]
        if items_level < depth:
            for i in range(items_level, depth):
                list_with_parents[i] = None

        # Append a copy of a list
        lines_with_parents.append(list_with_parents[:])
    return lines_with_parents


def string_to_dict(string) -> {}:
    hierarchy_table = string_to_hierarchy_table(string)
    tree = BuildTree()
    try:
        tree.build_tree_from_hierarchy_table(hierarchy_table)
    except IndexError:
        return {r"IndexError: The hierarchy structure of the source text may be invalid.": None}
    dict1 = tree.make_dict()
    return dict1


class TreeNode:
    depth = 0
    def __init__(self, serial_no, name, level, parent=None):
        self.serial_no = serial_no
        self.name = name
        self.level = level
        self.parent = parent
        self.children = []


class BuildTree:
    def __init__(self):
        # Add root instance to tree node.
        self.tree_nodes = [TreeNode(0, "root", 0)]

    def build_tree_from_hierarchy_table(self, hierarchy_table: list):
        level = 0
        name = ""
        parent = 0
        depth = 0
        parents_list = []

        # Get the depth of the table
        depth = len(max(hierarchy_table, key=len))
        self.tree_nodes[0].depth = depth


        # Build a tree
        for line_no, line in enumerate(hierarchy_table):
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


if __name__ == "__main__":
    sample_string = (
        "Kitchen\n\tCutting Board\n\tKnife Set\n\t\tShort knife\nLiving Room\n\tSofas\nBedroom"
    )

    _dict = string_to_dict(sample_string)
    print(_dict)