from fpdf import FPDF

class Shirtificate(FPDF):
    def __init__(self, name:str):
        self.__name = name.title() + " took CS50"
        self.__title = "CS50 Shirtificate"

    def create_pdf(self):
        font = "helvetica"
        super().__init__(orientation="portrait", format="A4")
        self.add_page()
        self.image("./shirtificate.png",x=15,y=75,w=185)
        self.set_font(family=font, size=45)
        self.cell(195, 70, text=self.__title, align="C")

        self.set_font(family=font, size=30, style="b")
        self.set_text_color(255,255,255)
        self.cell(-195, 255, text=self.__name, align="C")
        self.output("shirtificate.pdf")
    
    @classmethod
    def get_pdf(cls):
        return Shirtificate(input("Name: "))

if __name__ == "__main__":
    shirtificate = Shirtificate.get_pdf()
    shirtificate.create_pdf()