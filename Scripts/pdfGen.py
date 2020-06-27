import io
import os

from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import date

Yfirst = 480
lineGapY = -12

row = {
    "InvoiceDate": 45,
    "InvoiceNumber": 100,
    "ConsignmentNumber": 190,
    "VehicleNumber": 265,
    "InvoiceQuantity": 353,
    "ChargableQuantity": 405,
    "Rate": 452,
    "Amount": 510,
}

pos = {
    "BillNumber": {"x": 460, "y": 602},
    "Date": {"x": 440, "y": 590},
    "ClientName": {"x": 53, "y": 602},
    "Address": {"x": 53, "y": 590},
    "GstNumber": {"x": 100, "y": 578},
    "Origin": {"x": 285, "y": 536},
    "Destination": {"x": 50, "y": 524},
    "Total": {"x": 510, "y": 266},
    "SGST": {"x": 353, "y": 400},
    "CGST": {"x": 353, "y": 388},
    "IGST": {"x": 353, "y": 376},
    "TGST": {"x": 353, "y": 364},
}


def saveBill(consignments, client, billDetails):
    packet = io.BytesIO()
    # create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)

    can.setFont("Helvetica-Bold", 9)
    # Add Bill number and Date
    can.drawString(
        pos["BillNumber"]["x"], pos["BillNumber"]["y"], billDetails["BillNumber"]
    )
    can.drawString(
        pos["Date"]["x"], pos["Date"]["y"], date.today().strftime("%m/%d/%y")
    )

    # Adding Client Details
    can.drawString(pos["ClientName"]["x"], pos["ClientName"]["y"], client["Name"])
    can.drawString(pos["Address"]["x"], pos["Address"]["y"], client["Address"])
    can.drawString(pos["GstNumber"]["x"], pos["GstNumber"]["y"], client["GstNumber"])

    # Adding Description
    can.drawString(pos["Origin"]["x"], pos["Origin"]["y"], consignments[0]["Origin"])
    can.drawString(
        pos["Destination"]["x"], pos["Destination"]["y"], consignments[0]["Destination"]
    )

    can.setFont("Helvetica", 9)
    # Adding Table Data
    y = Yfirst

    total = 0
    for d in consignments:
        for key in row.keys():
            if key != "Amount":
                can.drawString(row[key], y, str(d[key]))
        a = d["Rate"] * d["ChargableQuantity"]

        total += a
        can.drawString(row["Amount"], y, str(a))

        y += lineGapY

    can.setFont("Helvetica-Bold", 9)
    tgst = 0.00
    if billDetails["SGST"] == True:
        can.drawString(pos["SGST"]["x"], pos["SGST"]["y"], str(total // 40))
        tgst += total // 40
    else:
        can.drawString(pos["SGST"]["x"], pos["SGST"]["y"], "-")

    if billDetails["CSGT"] == True:
        can.drawString(pos["CGST"]["x"], pos["CGST"]["y"], str(total // 40))
        tgst += total // 40
    else:
        can.drawString(pos["CGST"]["x"], pos["CGST"]["y"], "-")

    if billDetails["IGST"] == True:
        can.drawString(pos["IGST"]["x"], pos["IGST"]["y"], str(total // 20))
        tgst += total // 20
    else:
        can.drawString(pos["IGST"]["x"], pos["IGST"]["y"], "-")

    can.drawString(pos["TGST"]["x"], pos["TGST"]["y"], str(tgst))
    can.drawString(pos["Total"]["x"], pos["Total"]["y"], str(total))

    can.save()

    # move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)

    # read your existing PDF
    templatePath = os.getcwd() + "/Resources/invoice.pdf"
    existing_pdf = PdfFileReader(open(templatePath, "rb"))
    output = PdfFileWriter()

    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)

    # finally, write "output" to a real file
    outputStream = open("bill.pdf", "wb")
    output.write(outputStream)
    outputStream.close()


Data = [
    {
        "InvoiceDate": "12/6/2019",
        "InvoiceNumber": "PKTC/19-20/497",
        "ConsignmentNumber": "KOL - 2642",
        "VehicleNumber": "WB39B 2692",
        "InvoiceQuantity": 22.970,
        "ChargableQuantity": 22.970,
        "Rate": 2850.00,
        "Origin": "Kolkata",
        "Destination": "Siliguri",
    },
    {
        "InvoiceDate": "12/5/2019",
        "InvoiceNumber": "PKTC/19-20/498",
        "ConsignmentNumber": "KOL - 2643",
        "VehicleNumber": "WB39B 2691",
        "InvoiceQuantity": 23.160,
        "ChargableQuantity": 23.160,
        "Rate": 2850.00,
    },
]

cons = {
    "Name": "Ashwin Ginoria",
    "Address": "2 Kali Krishna Tagore Street, Kolkata - 700007",
    "GstNumber": "234681742",
}

BillDetails = {"BillNumber": "12532457t348", "CSGT": True, "SGST": True, "IGST": False}

if __name__ == "__main__":
    saveBill(Data, cons, BillDetails)
