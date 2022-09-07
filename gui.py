from cgitb import text
import tkinter
import odds_calc as oc
from matplotlib.figure import Figure

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg
)


class tft_gui(tkinter.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        # tk Variables
        self.n = 1
        self.om_titan_level = tkinter.StringVar()
        self.om_titan_level.set("Level_3")
        self.om_tier_level = tkinter.StringVar()
        self.om_tier_level.set("Tier2")


        # label creation & position

        lb_tier_lvl = tkinter.Label(self, text=self.om_tier_level)
        lb_tier_lvl.pack()

        lb_titan_lvl = tkinter.Label(self, text=self.om_titan_level)
        lb_titan_lvl.pack()

        # option menu's
        titan_level_options = ["Level_3","Level_4","Level_5","Level_6","Level_7","Level_8","Level_9"]
        self.op_titan_lvl = tkinter.OptionMenu(self, self.om_titan_level, *titan_level_options, command=self.change_plot).pack()
        
        champ_tier_options = ["Tier1","Tier2","Tier3","Tier4","Tier5"]
        self.om_tier_lvl = tkinter.OptionMenu(self, self.om_tier_level, *champ_tier_options, command=self.change_plot).pack()

        self.figure = Figure()

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(self.figure, self)

        self.axes = self.figure.add_subplot()
        figure_canvas.get_tk_widget().pack()


    def change_plot(self, *event):
        values = []
        x_axe = []
        labels = ["a","b","c","d","e","f","g","h","i","j"]
        width = 0.75
        for i in range(10):
            values.append(oc.get_odds(self.om_titan_level.get(), self.om_tier_level.get(),i))
            x_axe.append(i - (width/5)*self.n)
        
        values = [val*100 for val in values]
        line = self.axes.bar(x_axe, values , width/5, label="{} {}".format(self.om_titan_level.get(), self.om_tier_level.get()))
        self.axes.legend()
        self.axes.set_ylabel('Percentage [%]')
        self.axes.set_title('Odds of finding champions')
        self.axes.set_xticks(x_axe, labels)
        #self.axes.bar_label(line)
        self.n += 1
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()


if __name__ == "__main__":

    top = tkinter.Tk()
    tft_gui(top).pack()

    #myplot.ric_plot(top).pack()
    top.mainloop()

