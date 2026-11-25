
import json
from pathlib import Path
from graphviz import Digraph

# 出力先
output_dir = Path("docs")
output_dir.mkdir(exist_ok=True)

# 元データを読み込み
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

nodes, edges = data

# Graphvizでグラフを作成
dot = Digraph("flowchart", format="svg")

dot.attr(
    rankdir="LR",
    splines="ortho",
    nodesep="0.5",
    ranksep="0.8",
)

dot.attr(
    "node",
    shape="box",
    style="rounded",
    fontname="Noto Sans CJK JP",
    fontsize="14",
)

dot.attr(
    "edge",
    fontname="Noto Sans CJK JP",
    fontsize="12",
)

# ノードを追加
for node_id, label in nodes:
    dot.node(str(node_id), str(label))

# エッジを追加
for source, target in edges:
    dot.edge(str(source), str(target))

# SVGを生成
dot.render(
    str(output_dir / "flowchart"),
    cleanup=True,
)

# HTMLを生成
html = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flowchart</title>

    <style>
        body {
            font-family: sans-serif;
            margin: 0;
            padding: 24px;
            background: #f5f5f5;
        }

        h1 {
            font-size: 24px;
        }

        .diagram {
            background: white;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 24px;
            overflow: auto;
            text-align: center;
        }

        .diagram img {
            max-width: 100%;
            height: auto;
        }
    </style>
</head>

<body>
    <h1>フロー図</h1>

    <div class="diagram">
        <img src="flowchart.svg" alt="フロー図">
    </div>
</body>
</html>
"""

(output_dir / "index.html").write_text(
    html,
    encoding="utf-8",
)

print("HTML and SVG generated.")
