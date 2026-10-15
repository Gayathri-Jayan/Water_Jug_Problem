
import matplotlib.pyplot as plt
import networkx as nx

from matplotlib.patches import Patch
from solver import get_next_states


# Match the dark navy and blue style of the Streamlit app.
BG = "#081321"
PANEL = "#102238"
TEXT = "#EAF4FF"
MUTED = "#91A9C3"
GRID = "#24384E"

COLORS = {
    "start": "#83E6A0",
    "goal": "#FFD166",
    "solution": "#63C7F2",
    "normal": "#33475D",
    "edge": "#66809A",
    "path_edge": "#49B9FF",
}


def build_state_graph(capacity_a, capacity_b):
    """Build every state reachable from (0, 0)."""
    graph = nx.DiGraph()
    start = (0, 0)
    queue = [start]
    visited = {start}
    head = 0

    while head < len(queue):
        current = queue[head]
        head += 1
        graph.add_node(current)

        for next_state, operation in get_next_states(
            current, capacity_a, capacity_b
        ):
            graph.add_edge(current, next_state, label=operation)

            if next_state not in visited:
                visited.add(next_state)
                queue.append(next_state)

    return graph


def _is_goal(state, target):
    return state[0] == target or state[1] == target


def _solution_edges(solution_path):
    return [
        (
            solution_path[i]["state"],
            solution_path[i + 1]["state"]
        )
        for i in range(len(solution_path) - 1)
    ]


def _node_color(state, target, solution_states):
    """Colors for the complete state-space graph."""
    if state == (0, 0):
        return COLORS["start"]
    if _is_goal(state, target):
        return COLORS["goal"]
    if state in solution_states:
        return COLORS["solution"]
    return COLORS["normal"]


def _style_axes(fig, ax):
    """Apply a consistent dark theme to Matplotlib figures."""
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)

    ax.tick_params(colors=MUTED, labelsize=9)
    ax.xaxis.label.set_color(TEXT)
    ax.yaxis.label.set_color(TEXT)
    ax.title.set_color(TEXT)

    ax.grid(
        True,
        color=GRID,
        linestyle=":",
        linewidth=0.7,
        alpha=0.65
    )
    ax.set_axisbelow(True)

    for spine in ax.spines.values():
        spine.set_color(GRID)


def _style_legend(legend):
    if legend is None:
        return

    legend.get_frame().set_facecolor(PANEL)
    legend.get_frame().set_edgecolor(GRID)
    legend.get_frame().set_alpha(0.98)

    for label in legend.get_texts():
        label.set_color(TEXT)


def draw_state_graph(
    capacity_a,
    capacity_b,
    target,
    solution_path=None
):
    """Draw all reachable states and highlight BFS transitions."""
    graph = build_state_graph(capacity_a, capacity_b)
    solution_path = solution_path or []

    solution_states = {
        item["state"] for item in solution_path
    }
    path_edges = _solution_edges(solution_path)

    # State coordinates correspond to the quantities in each jug.
    positions = {
        state: (state[0], state[1])
        for state in graph.nodes()
    }

    fig, ax = plt.subplots(figsize=(13, 8))
    _style_axes(fig, ax)

    ordinary_edges = [
        edge for edge in graph.edges()
        if edge not in path_edges
    ]

    nx.draw_networkx_edges(
        graph,
        positions,
        edgelist=ordinary_edges,
        arrows=True,
        arrowsize=12,
        edge_color=COLORS["edge"],
        alpha=0.32,
        width=0.9,
        connectionstyle="arc3,rad=0.12",
        min_source_margin=15,
        min_target_margin=15,
        ax=ax
    )

    # Highlight only transitions belonging to the BFS solution.
    if path_edges:
        nx.draw_networkx_edges(
            graph,
            positions,
            edgelist=path_edges,
            arrows=True,
            arrowsize=20,
            edge_color=COLORS["path_edge"],
            width=2.8,
            alpha=1.0,
            connectionstyle="arc3,rad=-0.16",
            min_source_margin=17,
            min_target_margin=17,
            ax=ax
        )

    nx.draw_networkx_nodes(
        graph,
        positions,
        node_color=[
            _node_color(state, target, solution_states)
            for state in graph.nodes()
        ],
        node_size=1250,
        edgecolors="#91AAC3",
        linewidths=1.3,
        ax=ax
    )

    nx.draw_networkx_labels(
        graph,
        positions,
        labels={
            state: f"({state[0]}, {state[1]})"
            for state in graph.nodes()
        },
        font_size=8,
        font_weight="bold",
        font_color="#102033",
        ax=ax
    )

    legend_items = [
        Patch(facecolor=COLORS["start"], label="Initial state"),
        Patch(facecolor=COLORS["goal"], label="All goal states"),
        Patch(facecolor=COLORS["solution"], label="Other solution states"),
        Patch(facecolor=COLORS["normal"], label="Other reachable states"),
        Patch(facecolor=COLORS["path_edge"], label="BFS solution transitions"),
    ]

    legend = ax.legend(
        handles=legend_items,
        loc="upper left",
        bbox_to_anchor=(1.01, 1),
        fontsize=9,
        frameon=True
    )
    _style_legend(legend)

    ax.set_title(
        f"Water Jug State-Space Graph\n"
        f"Jug A = {capacity_a} L  |  "
        f"Jug B = {capacity_b} L  |  "
        f"Target = {target} L\n"
        f"{graph.number_of_nodes()} states  ·  "
        f"{graph.number_of_edges()} transitions",
        fontsize=13,
        fontweight="bold",
        color=TEXT,
        pad=18
    )

    ax.set_xlabel("Water in Jug A (litres)", labelpad=9)
    ax.set_ylabel("Water in Jug B (litres)", labelpad=9)

    ax.set_xticks(range(capacity_a + 1))
    ax.set_yticks(range(capacity_b + 1))
    ax.set_xlim(-0.7, capacity_a + 0.7)
    ax.set_ylim(-0.7, capacity_b + 0.7)
    ax.set_aspect("equal", adjustable="box")

    fig.tight_layout()
    return fig


def draw_solution_path(
    solution_path,
    capacity_a,
    capacity_b,
    target
):
    """Draw the BFS path, highlighting only its final goal state."""
    graph = nx.DiGraph()
    states = [item["state"] for item in solution_path]

    for i in range(len(solution_path) - 1):
        current = solution_path[i]
        following = solution_path[i + 1]

        graph.add_edge(
            current["state"],
            following["state"],
            label=following["operation"]
        )

    graph.add_nodes_from(states)

    positions = {
        state: (index * 2.7, 0)
        for index, state in enumerate(states)
    }

    fig, ax = plt.subplots(
    figsize=(max(16, len(states) * 2.2), 6.5),
    facecolor="#081321")
    ax.set_facecolor("#081321")
    _style_axes(fig, ax)

    # Keep the ordered solution path readable.
    ax.grid(False)
    ax.set_yticks([])

    if graph.number_of_edges():
        nx.draw_networkx_edges(
            graph,
            positions,
            arrows=True,
            arrowsize=22,
            width=2.6,
            edge_color=COLORS["path_edge"],
            min_source_margin=25,
            min_target_margin=25,
            ax=ax
        )

    # Only the final state of the returned BFS path is gold.
    final_state = states[-1] if states else None
    node_colors = []

    for index, state in enumerate(states):
        if index == 0 and state == (0, 0):
            node_colors.append(COLORS["start"])
        elif state == final_state and _is_goal(state, target):
            node_colors.append(COLORS["goal"])
        else:
            node_colors.append(COLORS["solution"])

    nx.draw_networkx_nodes(
        graph,
        positions,
        node_color=node_colors,
        node_size=2600,
        edgecolors="#91AAC3",
        linewidths=1.4,
        ax=ax
    )

    nx.draw_networkx_labels(
        graph,
        positions,
        labels={
            state: f"({state[0]}, {state[1]})"
            for state in graph.nodes()
        },
        font_size=12,
        font_weight="bold",
        font_color="#102033",
        ax=ax
    )

    edge_labels = nx.get_edge_attributes(graph, "label")

    if edge_labels:
        label_artists = nx.draw_networkx_edge_labels(
            graph,
            positions,
            edge_labels=edge_labels,
            font_size=10,
            font_color=TEXT,
            rotate=False,
            label_pos=0.5,
            bbox={
                "alpha": 0.98,
                "facecolor": PANEL,
                "edgecolor": GRID,
                "boxstyle": "round,pad=0.3"
            },
            ax=ax
        )

        # Keep operation labels readable on the dark background.
        for artist in label_artists.values():
            artist.set_color(TEXT)

    operations = max(0, len(solution_path) - 1)

    ax.set_title(
        f"BFS Shortest Solution Path\n"
        f"A = {capacity_a} L | B = {capacity_b} L | "
        f"Target = {target} L | "
        f"Minimum operations = {len(solution_path) - 1}",
        fontsize=16,
        color="#EAF4FF",
        fontweight="bold",
        pad=25
    )

    ax.tick_params(
        left=False,
        bottom=False,
        labelleft=False,
        labelbottom=False
    )
    ax.margins(x=0.08, y=0.8)

    fig.tight_layout()
    return fig
