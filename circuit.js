// ----- Form spanning tree

function GetSpanningTree(graph) {
    const spannigTree = new Map();

    graph.vertices.forEach((node) => {
        spannigTree.set(node.vertex, new Set());
    });

    let visitedVertices = new Set();

    graph.vertices.forEach((node) => {
        node.adjList.forEach((child) => {
            if (!visitedVertices.has(child)) {
                visitedVertices.add(child);
                spannigTree.get(node.vertex).add(child);
                spannigTree.get(child).add(node.vertex);
            }
        });
    });
    return spannigTree;
}

// ----- Find rejected edges Method

function GetRejectedEdges(graph, spannigTree) {
    let rejectedEdges = new Set();

    graph.vertices.forEach((node) => {
        if (spannigTree.has(node.vertex)) {
            node.adjList.forEach((child) => {
                if (!spannigTree.get(node.vertex).has(child)) {
                    if (!rejectedEdges.has(child + "-" + node.vertex)) {
                        rejectedEdges.add(node.vertex + "-" + child);
                    }
                }
            });
        }
    });

    return rejectedEdges;
}

// ----- Find Cycle Method

function FindCycle(
    start,
    end,
    spannigTree,
    visited = new Set(),
    parents = new Map(),
    current_node = start,
    parent_node = " "
) {
    let cycle = null;
    visited.add(current_node);
    parents.set(current_node, parent_node);
    const destinations = spannigTree.get(current_node);
    for (const destination of destinations) {
        if (destination === end) {
            cycle = GetCyclePath(start, end, current_node, parents);
            return cycle;
        }
        if (destination == parents.get(current_node)) {
            continue;
        }
        if (!visited.has(destination)) {
            cycle = FindCycle(
                start,
                end,
                spannigTree,
                visited,
                parents,
                destination,
                current_node
            );
            if (!!cycle) return cycle;
        }
    }
    return cycle;
}

// ----- Get all cycles from the input graph

function GetAllCycles(graph, spannigTree) {
    let cycles = [];
    let rejectedEdges = GetRejectedEdges(graph, spannigTree);
    rejectedEdges.forEach((edge) => {
        ends = edge.split("-");
        let start = ends[0];
        let end = ends[1];
        let cycle = FindCycle(start, end, spannigTree);
        if (!!cycle) {
            cycles.push(cycle);
        }
    });
    return cycles;
}

// ----- Get Cycle path by backtracking

function GetCyclePath(start, end, current, parents) {
    let cycle = [end];
    while (current != start) {
        cycle.push(current);
        current = parents.get(current);
    }
    cycle.push(start);
    return cycle;
}

// ----- Sort vertices by decreasing order of number of edges

function GetSortedVertices(graph2) {
    graph2.vertices.sort(function (a, b) {
        return b.adjList.length - a.adjList.length;
    });
    return graph2;
}

// ----- main function that find Circuits

function FindCircuits(graph) {
    let sortedGraph = GetSortedVertices(graph);
    let spannigTree = GetSpanningTree(sortedGraph);
    return GetAllCycles(graph, spannigTree);
}

// --------------- Input -----------------

let vertices = [
    {
        vertex: "A",
        adjList: ["B", "D"],
    },
    {
        vertex: "B",
        adjList: ["A", "C", "D"],
    },
    {
        vertex: "C",
        adjList: ["B", "D"],
    },
    {
        vertex: "D",
        adjList: ["A", "B", "C"],
    },
];

// ---------- Driver Code -----------

let graph = {
    vertices: vertices2,
};

let circuits = FindCircuits(graph);

circuits.forEach((circuit) => {
    let path = "";
    circuit.forEach((node) => {
        path += node + " -> ";
    });
    console.log(path);
});