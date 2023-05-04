import pymysql
import mysql.connector
from datetime import date, datetime


class ItemDatabase:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Shu123@123",
            database="medical_records"
        )
        self.cursor = self.mydb.cursor()

    # this function gets all the entries from students_records table

    def get_details_all(self):
        result = []
        query = "SELECT * FROM students_records"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            student = {}
            student["enrollment"] = row[0]
            student["name"] = row[1]
            student["school"] = row[2]
            student["course"] = row[3]
            student["batch"] = row[4]
            student["hostel"] = row[5]
            student["mobile"] = row[6]
            student["email"] = row[7]
            result.append(student)
        return result

    # this function takes one enrollment number and get the details of
    # the student from student_records table

    def get_details_roll(self, enroll_num):
        enrollId = int(enroll_num)
        query = f"SELECT * FROM students_records WHERE enrollment_id = '{enrollId}'"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            student = {}
            student["enrollment"] = row[0]
            student["name"] = row[1]
            student["school"] = row[2]
            student["course"] = row[3]
            student["batch"] = row[4]
            student["hostel"] = row[5]
            student["mobile"] = row[6]
            student["email"] = row[7]
            return [student]

    # getting all the medical records from student_medical_history table

    def get_all_med(self):
        result = []
        query = "SELECT * FROM student_medical_history"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            med_history = {}
            med_history["enrollment"] = row[0]
            med_history["date"] = row[1]
            med_history["time"] = row[2]
            med_history["symptoms"] = row[3]
            med_history["disease"] = row[4]
            med_history["treatment"] = row[5]
            med_history["referred"] = row[6]
            med_history["critical"] = row[7]
            result.append(med_history)
        return result

    # Adding medical record of the student (student_medical_history table)

    def add_record(self, id, body):
        now = datetime.now()
        today = date.today()
        current_time = now.strftime("%H:%M:%S")
        query = f"INSERT INTO student_medical_history VALUES ({id}, '{today}', '{current_time}', '{body['symptoms']}', '{body['disease']}',  '{body['treatment']}', '{body['referred']}', '{body['critical']}')"
        self.cursor.execute(query)
        self.mydb.commit()
        # print(query)

    # getting all medical records of a particular enrollment number

    def get_med_roll(self, enroll_num):
        enrollId = int(enroll_num)
        query = f"SELECT * FROM student_medical_history WHERE enrollment_id = '{enrollId}'"
        self.cursor.execute(query)
        med_rec = []
        for row in self.cursor.fetchall():
            med_rec_enroll = {}
            med_rec_enroll["enrollment"] = row[0]
            med_rec_enroll["date"] = row[1]
            med_rec_enroll["time"] = row[2]
            med_rec_enroll["symptoms"] = row[3]
            med_rec_enroll["disease"] = row[4]
            med_rec_enroll["treatment"] = row[5]
            med_rec_enroll["referred"] = row[6]
            med_rec_enroll["critical"] = row[7]
            med_rec.append(med_rec_enroll)
        return med_rec

    # getting all medical records of a particular date

    def get_med_date(self, date):
        query = f"SELECT * FROM student_medical_history WHERE date = '{date}'"
        self.cursor.execute(query)
        med_rec = []
        for row in self.cursor.fetchall():
            med_rec_date = {}
            med_rec_date["enrollment"] = row[0]
            med_rec_date["date"] = row[1]
            med_rec_date["time"] = row[2]
            med_rec_date["symptoms"] = row[3]
            med_rec_date["disease"] = row[4]
            med_rec_date["treatment"] = row[5]
            med_rec_date["referred"] = row[6]
            med_rec_date["critical"] = row[7]
            med_rec.append(med_rec_date)
        return med_rec

    # create a post api to to update the medical inventory

    def put_med_inventory(self, body):
        # batch, medicinw, quantity, expiry, create variable for each of them
        batch = body['batch']
        medicine = body['medicine']
        quantity = body['quantity']
        expiry = body['expiry']
        # expiry = datetime.strptime(body['expiry'], "%d/%m/%Y")
        # expiry = expiry.strftime('%Y-%m-%d')
        print(expiry)
        today = date.today()
        # if (expiry < today):
        #     status = 'EXPIRED'
        # # medicine, quantity, expiry
        # elif (body['quantity'] == 0):
        #     status = 'OUT OF STOCK'
        # else:
        #     status = 'AVAILABLE'
        # insert the data into inventory table
        query = f"INSERT INTO inventory VALUES ('{batch}', '{medicine}', '{quantity}', '{expiry}')"
        self.cursor.execute(query)
        self.mydb.commit()

    # get information from inverntory table of a particular medicine
    def get_medicine_info(self, medicine):
        query = f"SELECT * FROM inventory WHERE medicine = '{medicine}'"
        self.cursor.execute(query)
        inventory_info = []
        for row in self.cursor.fetchall():
            # multiple entries of one medicine will be because of different batch numbers
            batches = {}
            batches["batch"] = row[0]
            batches["medicine"] = row[1]
            batches["quantity"] = row[2]
            batches["expiry"] = row[3]
            inventory_info.append(batches)
        return inventory_info

# create a function to get all the details of inventory
    def get_all_inventory(self):
        query = "SELECT * FROM inventory"
        self.cursor.execute(query)
        inventory_info = []
        for row in self.cursor.fetchall():
            # multiple entries of one medicine will be because of different batch numbers
            batches = {}
            batches["batch"] = row[0]
            batches["medicine"] = row[1]
            batches["quantity"] = row[2]
            batches["expiry"] = row[3]
            inventory_info.append(batches)
        return inventory_info

    # function to get top 5 diseases from medical_students_record table
    def top_diseases(self):
        query = f"SELECT disease, COUNT(*) as count FROM medical_records.student_medical_history GROUP BY disease ORDER BY count DESC LIMIT 5;"
        self.cursor.execute(query)
        diseases = []
        for row in self.cursor.fetchall():
            disease = {}
            disease['disease'] = row[0]
            disease['count'] = row[1]
            diseases.append(disease)
        return diseases

    # function to get top 5 students from medical_students_record table
    def top_students(self):
        query = f"SELECT students_records.name, COUNT(*) AS count FROM medical_records.student_medical_history JOIN medical_records.students_records ON medical_records.student_medical_history.enrollment_id = medical_records.students_records.enrollment_id GROUP BY medical_records.student_medical_history.enrollment_id ORDER BY count DESC LIMIT 5;"
        self.cursor.execute(query)
        students = []
        for row in self.cursor.fetchall():
            student = {}
            student['name'] = row[0]
            student['count'] = row[1]
            students.append(student)
        return students


# db = ItemDatabase()
# db.add_record(id=200197, body={'symptoms': 'Fever, cold, headache', 'disease': 'Viral',
#              'treatment': 'Accolate', 'referred': 'y', 'critical': 'H'})
# db.getOne(200197)
