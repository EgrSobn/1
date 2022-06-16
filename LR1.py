def gen_bin_tree_rec(height: int, root: int) -> dict:
    if height == 0:
        return {root: []}

    return {
        str(root): [
            gen_bin_tree_rec(height - 1, root * 2),
            gen_bin_tree_rec(height - 1, root + 2)
        ]
    }

print(gen_bin_tree_rec(5, 1), "\n")