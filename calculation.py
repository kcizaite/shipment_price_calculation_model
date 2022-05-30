from tkinter.filedialog import askopenfile
import os


def open_file():
    shipment_data = open("shipments.txt", "r")
    new_shipment_data = shipment_data.read()
    shipment_list = new_shipment_data.split("\n")

    prices_list = []
    for line in shipment_list:
        prices_list.append(line.split())

    s_list = []
    for element in prices_list:
        if element[1] == "S":
            shipment = element[2]
            s_list.append(shipment)

    file_path = askopenfile(mode="r", filetypes=[("Text Files", "*txt")])
    if file_path is not None:
        content = file_path.read()
        content_list = content.split("\n")
        opa = []
        for content in content_list:
            opa.append(content.split())
        return module(opa, prices_list, s_list)


def module(shipments, prices, s_list):
    final_list = []
    discounts = 0.0
    counter = 0
    date = ""
    for shipment in shipments:
        if date != shipment[0][0:7]:
            date = shipment[0][0:7]
            counter = 0
            discounts = 0
        if (shipment[1] != "S") and (shipment[1] != "M") and (shipment[1] != "L"):
            shipment.append("Ignored")
            final_list.append(shipment)
        for price in prices:
            if (shipment[1] == price[1] == "S") and (shipment[2] == price[0]):
                current_discount = float(price[2]) - float(min(s_list))
                if discounts + current_discount <= 10:
                    discounts += float(price[2]) - float(min(s_list))
                    current_price = float(price[2]) - float(current_discount)
                    shipment.append(str(current_price) + " " + str(current_discount))
                    final_list.append(shipment)
                elif discounts < 10.0:
                    discount = 10.0 - discounts
                    new_discount = float(price[2]) - discount
                    shipment.append(str(round(new_discount, 1)) + " " + str(round(discount, 1)))
                    final_list.append(shipment)
            elif (shipment[1] == price[1] == "L") and (shipment[2] == price[0] == "SimoSiuntos"):
                counter += 1
                if counter == 3:
                    current_discount = float(price[2])
                    current_price = float(price[2]) - float(price[2])
                    discounts += current_discount
                    shipment.append(str(current_price) + " " + str(current_discount))
                    final_list.append(shipment)
                else:
                    shipment.append(str(price[2]) + " " + str(0.0))
                    final_list.append(shipment)
            elif (shipment[1] == price[1]) and (shipment[2] == price[0]):
                temp = price[2]
                shipment.append(str(temp) + " " + str(0.0))
                final_list.append(shipment)

    with open("output.txt", "w") as w_file:
        for lines in final_list:
            for line in lines:
                w_file.write(line + " ")
            w_file.write("\n")

    return final_list


def txt_file():
    file_path = askopenfile(mode="r", filetypes=[("Text Files", "*txt")])
    if file_path is not None:
        pass
    os.system(file_path.name)
