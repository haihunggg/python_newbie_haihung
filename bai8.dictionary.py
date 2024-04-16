data= {
    "vender": "CN=Viettel­CA, O=Viettel Group,L=Hà Nội, C=VN",
    "subjectName": "OID.0.9.2342.19200300.100.1.1=MST:2300104684, CN=CÔNG TY CỔ PHẦN THƯƠNG MẠI VÀ DU LỊCH BẮC NINH, O=CÔNG TY CỔ PHẦN THƯƠNG MẠI VÀ DU LỊCH BẮC NINH Thành phố Bắc Ninh, S=Bắc Ninh, C=VN",
    "serialNumber": "5404FFFEB7033FB316D672201B8B03A2",
    "dateFrom": "2022-02-25T13:38:41",
    "expireDate": "2024-05-13T13:38:41",
    "form": 1,
    "tokenType": 1,
    "used": True,
}
data["form"]= True
del data["tokenType"]
del data["form"]
#print(data["form"])
#print(data["vender"])
print(data)