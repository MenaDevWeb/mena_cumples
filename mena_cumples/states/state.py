import reflex as rx

class State(rx.State):
    
        #navigation
    def navigate_to_15(self):
        return rx.redirect("/pack_15_pax")
    
    def navigate_to_20(self):
        return rx.redirect("/pack_20_pax")
    
    def navigate_to_25(self):
        return rx.redirect("/pack_25_pax")
    
    def navigate_to_30(self):
        return rx.redirect("/pack_30_pax")
    



