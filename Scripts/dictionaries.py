def Vehicle_Dict():
    return {"Num": None, "Model": None, "Current_Location": None, "Status": None}


def Consignor_Consignee_Dict():
    return {
        "ID": None,
        "Name": None,
        "Contact": None,
        "Address": None,
        "Email": None,
        "GST_Number": None,
    }


def Consignment_Dict():
    return {
        "ID": None,
        "Consignor_ID": None,
        "Consignee_ID": None,
        "Vehicle_Num": None,
        "Loading_Date": None,
        "To": None,
        "From": None,
        "Weight": None,
        "Rate": None,
        "Misc_Charges": None,
        "Amount": None,
        "Chargeable_Qty": None,
        "Invoice_No.": None,
        "Invoice_Date": None,
        "Invoice_Qty": None,
        "Bill_Num": None,
    }


def Repair_Log_Dict():
    return {
        "Repair_ID": None,
        "Vehicle_ID": None,
        "Repair_Date": None,
        "Amount": None,
        "From": None,
    }


def Bills_Dict():
    return {"Num": None, "Consignments": None, "BIll_Date": None, "Amount": None}
