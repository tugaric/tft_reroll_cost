import tkinter as tk
import odds_calc as oc
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

class ric_plot(tk.Frame):
    def __init__(self,parent, titan_level, champ_tier):
        super().__init__(parent)
        lang = []
        popu = []

        for i in range(10):
            lang.append(oc.get_odds(titan_level, champ_tier,i))
            popu.append("{}".format(i))
        
        #data = {
        #    'Python': 11.27,
        #    'C': 11.16,
        #    'Java': 10.46,
        #    'C++': 7.5,
        #    'C#': 5.26
        #}

        languages = popu#data.keys()     # x values
        popularity = lang#data.values()  # y values

        # create a figure
        figure = Figure(figsize=(6, 4), dpi=100)

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, self)

        # create axes
        axes = figure.add_subplot()

        # create the barchart
        axes.bar(languages, popularity)
        #axes.set_title('Top 5 Programming Languages')
        #axes.set_ylabel('Popularity')

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

if __name__ == "__main__":
    top = tk.Tk()
    foo_plot = ric_plot(top,"Level_6", "Tier3")
    foo_plot.pack()
    top.mainloop()