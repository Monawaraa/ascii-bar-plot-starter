from rich.console import Console
from rich.text import Text

bar_char = "█"
colors = ["green", "yellow", "magenta", "blue", "red", "cyan"]


def scale_bar(value, maximum, width=40):
    if maximum <= 0:
        return 0
    return round(value / maximum * width)

def render_bar_chart(values, width=40):

    console = Console()
    maximum = max(value for _, value in values)
    label_width = max(len(str(label)) for label, _ in values)

    for i, (label, value) in enumerate(values):
        color = colors[i % len(colors)]
        length = scale_bar(value, maximum, width)

        line = Text()
        line.append(f"{str(label):<{label_width}} ", style="bold")
        line.append(bar_char * length, style=color)
        line.append(" " * (width - length))
        line.append(f" {value:.2f}", style="dim")
        console.print(line)

if __name__ == "__main__":
    values = [
        ("A", 2.16),
        ("B", 4.33),
        ("C", 6.57),
        ("D", 8.71),
    ]
    render_bar_chart(values)
