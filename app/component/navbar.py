from app.component.bar_chart import bar_chart
from app.component.line_chart import line_chart
from app.component.scatter_plot import scatter_plot

pages = {
    "Bar Chart": {
        "title": "Bar Chart",
        "description": "Welcome to the home page! This page features a bar chart.",
        "function": bar_chart
    },
    "Line Chart": {
        "title": "Line Chart",
        "description": "This is page 2, showcasing a line chart.",
        "function": line_chart
    },
    "Scatter Plot": {
        "title": "Scatter Plot",
        "description": "You've reached page 3, which displays a scatter plot.",
        "function": scatter_plot
    }
}