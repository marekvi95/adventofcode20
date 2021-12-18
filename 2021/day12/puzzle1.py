from igraph import Graph, plot, layout

g = Graph()
g.add_vertices("Start")
g.add_vertices("End")
g.add_vertices("A")
g.add_vertices("b")
g.add_vertices("c")
g.add_vertices("d")

g.add_edges(
    [
        ("Start", "A"),
        ("Start", "b"),
        ("A", "c"),
        ("A", "b"),
        ("b", "d"),
        ("A", "End"),
        ("b", "End"),
    ]
)

g.vs["label"] = g.vs["name"]
layout = g.layout("kk")
# plot(g, layout=layout)
print(g.summary())
# print(g.get_all_simple_paths("Start", "End"))
print("start->a", g.get_all_simple_paths("Start", "A"))
print("A->b", g.get_all_simple_paths("A", "b"))
print("b->A", g.get_all_simple_paths("b", "A"))
print("A->end", g.get_all_simple_paths("A", "End"))
print("b->end", g.get_all_simple_paths("b", "End"))


print("A->c", g.get_all_simple_paths("A", "c"))
print("c->A", g.get_all_simple_paths("c", "A"))

print("A->d", g.get_all_simple_paths("A", "d"))
print("d->A", g.get_all_simple_paths("d", "A"))


# simple_paths = []
# extra_paths = []

# for st in ["End", "A", "b", "c", "d"]:
#     simple_paths.append(g.get_all_simple_paths("Start", st))

# print(simple_paths)

# for st in ["A", "b", "c", "d"]:
#     # extra_paths.append(g.get_all_simple_paths("Start", st))
#     # extra_paths.append(g.get_all_simple_paths(st, "End"))

#     print("Start", g.get_all_simple_paths("Start", st))
#     print("End", g.get_all_simple_paths(st, "End"))

# print(extra_paths)
# print(simple_paths)
print("Start", g.neighbors("Start"))
print("A", g.neighbors("A"))
print("End", g.neighbors("End"))
