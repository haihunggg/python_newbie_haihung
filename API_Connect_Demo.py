from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def connect_to_database():
    try:
        # Kết nối đến cơ sở dữ liệu chứa thông tin kết nối của các tenant
        tenant_connection = psycopg2.connect(
            dbname="MinvoiceCloud",
            user="minvoice",
            password="Minvoice@123",
            host="103.61.122.194",
            port="5432"
        )
        tenant_cursor = tenant_connection.cursor()

        # Truy vấn để lấy thông tin kết nối của một tenant cụ thể
        sql_query = """
            SELECT "Value"
            FROM "AbpTenantConnectionStrings"
            WHERE "Name" = %s
        """
        
        # Định nghĩa tên của tenant bạn muốn kết nối
        tenant_name = "tendatabase"
        tenant_cursor.execute(sql_query, (tenant_name,))
        row = tenant_cursor.fetchone()

        if row:
            # Lấy chuỗi kết nối của tenant từ kết quả truy vấn
            tenant_connection_string = row[0]

            # Kết nối đến cơ sở dữ liệu của tenant
            connection = psycopg2.connect(tenant_connection_string)
            return connection
        else:
            print("Không tìm thấy thông tin kết nối cho tenant này")
            return None

    except psycopg2.Error as e:
        print("Lỗi khi kết nối đến cơ sở dữ liệu:", e)
        return None
    finally:
        tenant_cursor.close()
        tenant_connection.close()

@app.route('/api/invoices', methods=['GET'])
def get_invoices():
    try:
        connection = connect_to_database()
        if connection:
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
        else:
            return jsonify({"error": "Không thể kết nối đến cơ sở dữ liệu của tenant"}), 500

    except psycopg2.Error as e:
        print("Lỗi khi thực hiện câu lệnh SQL:", e)
        return jsonify({"error": "Đã xảy ra lỗi khi truy vấn cơ sở dữ liệu"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
