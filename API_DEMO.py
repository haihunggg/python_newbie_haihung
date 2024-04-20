from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def connect_to_database():
    try:
        # Thay đổi thông tin kết nối phù hợp với cơ sở dữ liệu của bạn
        connection = psycopg2.connect(
            dbname="MinvoiceCloud",
            user="minvoice",
            password="Minvoice@123",
            host="103.61.122.194",
            port="5432"
        )
        return connection
    except psycopg2.Error as e:
        print("Lỗi khi kết nối đến cơ sở dữ liệu:", e)

@app.route('/api/invoices', methods=['GET'])
def get_invoices():
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        sql_query = """
             SELECT "DateSign", "CreationTime", "SellerTaxCode", "SellerLegalName", "InvoiceSerial", "BuyerLegalName"
            FROM "MInvoice"."Invoice"
            WHERE "SendTaxStatus" = 1
        """
        
        cursor.execute(sql_query)
        rows = cursor.fetchall()

        invoices = []
        for row in rows:
            invoice = {
                "DateSign": row[0],
                "CreationTime": row[1],
                "SellerTaxCode": row[2],
                "SellerLegalName": row[3],
                "InvoiceSerial": row[4],
                "BuyerLegalName": row[5]
            }
            invoices.append(invoice)

        cursor.close()
        connection.close()

        return jsonify({"invoices": invoices})

    except psycopg2.Error as e:
        print("Lỗi khi thực hiện câu lệnh SQL:", e)
        return jsonify({"error": "Đã xảy ra lỗi khi truy vấn cơ sở dữ liệu"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
