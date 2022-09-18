import tkinter
import tkinter.ttk as ttk
import odds_calc as oc
from matplotlib.figure import Figure

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg
)

class tft_gui(tkinter.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        # tk Variables
        champ_tier_options = ["Tier1","Tier2","Tier3","Tier4","Tier5"]
        titan_level_options = ["Level_3","Level_4","Level_5","Level_6","Level_7","Level_8","Level_9"]
        
        self.n = 1
        self.om_titan_level = tkinter.StringVar()
        self.om_tier_level = tkinter.StringVar()
        # spinboxvariable = number of champions out of pool
        self.sb_nbr_champ_out = tkinter.StringVar()

        # option menu's self.op_titan_lvl =  self.om_tier_lvl = 
        tkinter.OptionMenu(self, self.om_titan_level, *titan_level_options, command=self.change_plot).pack()
        tkinter.OptionMenu(self, self.om_tier_level, *champ_tier_options, command=self.change_plot).pack()
        
        ttk.Spinbox(self, from_=0, to=18, textvariable=self.sb_nbr_champ_out).pack()

        # create a clear plot button
        self.clear = tkinter.Button(self, text="clear plot", command=self.clear_plot).pack()
        
        # create FigureCanvasTkAgg object
        self.figure = Figure()
        figure_canvas = FigureCanvasTkAgg(self.figure, self)

        self.axes = self.figure.add_subplot()
        figure_canvas.get_tk_widget().pack()

    def clear_plot(self, *event):
        self.axes.clear()
        self.n = 1
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

    def change_plot(self, *event):
        values = []
        x_axe = []
        width = 0.25
        if self.n == 3:
            self.clear_plot()

        for i in range(1,5):
            values.append(oc.get_odds(self.om_titan_level.get(), 
            self.om_tier_level.get(), 
            shop_rerolls=i, 
            nbr_of_champs_out_of_pool=int(self.sb_nbr_champ_out.get())))
            x_axe.append(i + ((-1)**(self.n)) * (width/2))
        
        values = [val*100 for val in values]
        # .bar(values in x, values in y, width of the bar, label of the plot)
        line = self.axes.bar(x_axe, values , width, label="{} {} {}".format(self.om_titan_level.get(), self.om_tier_level.get()
        , self.sb_nbr_champ_out.get()))
        # draw the legend label
        self.axes.legend()
        self.axes.set_ylabel('Percentage [%]')  # write the y label
        self.axes.set_xlabel("shop rerolls")    # write the x label
        self.axes.set_title('Odds of finding champions')    # set the title of the plot
        #self.axes.set_xticks(x_axe, labels) # put label in position x 
        self.axes.bar_label(line)
        self.n += 1
        self.figure.canvas.draw()           # redraw the plot
        self.figure.canvas.flush_events()   # wait for the gui to draw before allowing inputs

if __name__ == "__main__":

    top = tkinter.Tk()
    tft_gui(top).pack()
    top.mainloop()

