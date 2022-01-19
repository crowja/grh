#! /usr/bin/env python3

import sys


def print_groups(v, e):
    count = 0
    groups = []
    u = v.copy()
    while len(u) > 0:
        uu = u.pop()
        r = {uu}  # reachable vertices
        a = {uu}  # dynamic list of vertices to explore
        while len(a) > 0:
            aa = a.pop()
            new_neighbors = edges[aa] - r
            a = a.union(new_neighbors)
            r.add(aa)
        groups.append(r)
        u = u - r

    for group in groups:
        print("\t".join(group))


if __name__ == "__main__":

    import argparse

    ap = argparse.ArgumentParser()
    args = ap.parse_args()

    vertices = set()
    edges = {}
    for line in sys.stdin:
        text = line.strip()
        if not text or text.startswith("#"):
            continue
        vals = text.split("\t")
        if len(vals) < 2:
            print("BARF", file=sys.stderr)
            exit(1)

        vertices.add(vals[0])
        vertices.add(vals[1])
        if vals[0] not in edges:
            edges[vals[0]] = set()
        if vals[1] not in edges:
            edges[vals[1]] = set()
        edges[vals[0]].add(vals[1])
        edges[vals[1]].add(vals[0])

    print_groups(vertices, edges)
