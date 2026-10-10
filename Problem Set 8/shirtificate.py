
from fpdf import FPDF


def main():
    name = input("Name: ").strip()

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Add the title at the top
    pdf.set_font("helvetica", style="B", size=36)
    pdf.cell(w=210, h=30, text="CS50 Shirtificate", align="C")
    pdf.ln(20)

    # Add the shirt image, centered horizontally
    pdf.image("shirtificate.png", x=10, y=60, w=190)

    # Print the user's name in white over the shirt
    pdf.set_font("helvetica", style="B", size=24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(0, 140)
    pdf.cell(w=210, h=15, text=f"{name} took CS50", align="C")

    # Save the PDF
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
