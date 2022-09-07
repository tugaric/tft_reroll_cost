import tkinter as tk
from functools import partial
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

        languages = popu
        popularity = lang
        val = [0,1,2,3,4,5,8,2,1,4]
        update_btn = tk.Button(self, text="Update values", command=lambda : self.change_plot(val))
        update_btn.pack()
        # create a figure # figsize=(6, 4), dpi=100
        self.figure = Figure()
        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(self.figure, self)
        # create axes
        axes = self.figure.add_subplot()
        # create the barchart
        self.line, = axes.plot(lang,popu, "b-")
        figure_canvas.get_tk_widget().pack()    #side=tk.TOP, fill=tk.BOTH, expand=1

    def change_plot(self, values):
            self.line.set_ydata(values)
            self.figure.canvas.draw()
            self.figure.canvas.flush_events()

if __name__ == "__main__":
    top = tk.Tk()
    foo_plot = ric_plot(top,"Level_6", "Tier3")
    foo_plot.pack()
    top.mainloop()