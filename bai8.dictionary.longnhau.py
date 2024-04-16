json= {
   'data': {
    "vender": "CN=Viettel­CA, O=Viettel Group,L=Hà Nội, C=VN",
    "subjectName": "OID.0.9.2342.19200300.100.1.1=MST:2300104684, CN=CÔNG TY CỔ PHẦN THƯƠNG MẠI VÀ DU LỊCH BẮC NINH, O=CÔNG TY CỔ PHẦN THƯƠNG MẠI VÀ DU LỊCH BẮC NINH Thành phố Bắc Ninh, S=Bắc Ninh, C=VN",
    "serialNumber": "5404FFFEB7033FB316D672201B8B03A2",
    "dateFrom": "2022-02-25T13:38:41",
    "expireDate": "2024-05-13T13:38:41",
    "form": 1,
    "tokenType": 1,
    "used": True,
},
   'responde':{"typeInvoiceId": "fc057613-9499-47f0-bbeb-2181c254c159",
            "fieldName": "sellerTaxCode",
            "lable": "Mã số thuế",
            "lableWidth": 2,
            "controlWidth": 10,
            "dataType": "string",
            "required": True,
            "maxLength": 14,
            "fomat": '',
            "numberItemInLine": 2,
            "readOnly": False,
            "multipleFormula": False,
            "groupTypeCode": "01",
            "groupXML": None,
            "orders": 1,
            "defaultValue": None,
            "formula": None,
            "formulaExcel": None,
            "lableExportExcel": "",
            "typeFormat": None,
            "use": True,
            "ordersFormula": None,
            "formulas": [],
            "formulasExcel": [],
            "useFormula": False,
            "isDeleted": False,
            "deleterId": None,
            "deletionTime": None,
            "lastModificationTime": None,
            "lastModifierId": None,
            "creationTime": "2023-01-01T22:13:43.976359+07:00",
            "creatorId": "3a0851d3-2bb1-9a65-02f3-ce5a894297c8",
            "id": ""}
}
json['data']["form"]= True
del json['data']["tokenType"]
del json['data']["form"]
print(json["form"])
#print(data["vender"])
if (json["responde"]["id"] == "" and json["responde"]["readOnly"] == True): print(json["responde"]["creationTime"])
elif (json["responde"]["id"] == "" and json["responde"]["readOnly"] == True and json["responde"]["use"] == True): print('Không thành công')
else: print('{"code": "99", "message": "Tên đăng nhập hoặc mật khẩu không đúng", "ok": false, "error": "Tên đăng nhập hoặc mật khẩu không đúng"}')