from cgitb import text
import tkinter

class tft_gui(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        def change_label(event):
            lb_tier_lvl.config(text=om_tier_level.get())
            lb_titan_lvl.config(text=om_titan_level.get())
        
        # tk Variables
        om_titan_level = tkinter.StringVar()
        om_tier_level = tkinter.StringVar()

        # label creation & position
        lb_tier_lvl = tkinter.Label(self, text=om_tier_level)
        lb_tier_lvl.pack()

        lb_titan_lvl = tkinter.Label(self, text=om_titan_level)
        lb_titan_lvl.pack()

        # option menu's
        titan_level_options = ["Level_3","Level_4","Level_5","Level_6","Level_7","Level_8","Level_9"]
        self.op_titan_lvl = tkinter.OptionMenu(self, om_titan_level, *titan_level_options, command=change_label).pack()
        
        champ_tier_options = ["Tier1","Tier2","Tier3","Tier4","Tier5"]
        self.om_tier_lvl = tkinter.OptionMenu(self, om_tier_level, *champ_tier_options, command=change_label).pack()
        
        # append to the parent widget
        self.pack()

if __name__ == "__main__":
    top = tkinter.Tk()
    gui = tft_gui(top)
    
    top.mainloop()
