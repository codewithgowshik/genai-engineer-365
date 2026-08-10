from src.tools.pdf_reader import read_pdf


def test_pdf_reader():

    text = read_pdf("uploads/Report.pdf")

    assert text.strip() != ""