
import psycopg2 as sql

connection = sql.connect(
    host='localhost',
    dbname='Vit_Odev',
    user='postgres',  # dbuser yerine user kullanın
    password='1234',
    port='5434'       # Portunuzun doğru olduğundan emin olun
)
cursor = connection.cursor()

# # Test için bir sorgu çalıştırabilirsiniz
# cursor.execute("SELECT  * from film;")  # Basit bir test sorgusu
# records = cursor.fetchall()     # Çıktıyı kontrol edin
# tel = 0
# for row in records:
#     tel += 1
#     print("\n", row)

# # Bağlantıyı kapat
# conn.commit()
# cursor.close()
# conn.close()
# print("\n", tel)

# Tablo olusturmak
# cursor.execute("""CREATE TABLE IF NOT EXISTS public.employees (
#                     emp_ID INT PRIMARY KEY,
#                     first_name TEXT NOT NULL,
#                     last_name TEXT NOT NULL,
#                     salary INT NOT NULL,
#                     job_title TEXT NOT NULL,
#                     gender TEXT NOT NULL,
#                     hire_date DATE NOT NULL);""")
# cursor.execute(""" INSERT INTO public.employees (emp_ID, first_name, last_name, salary, job_title, gender, hire_date) VALUES
#                    (17679,'Robert','Gilmore',110000,'Operations Director','Male','2018-09-04'),
#                    (26650,'Elvis','Ritter',86000,'Sales Manager','Male','2017-11-24'),
#                    (30840,'David','Barrow',85000,'Data Scientist','Male','2019-12-02'),
#                    (49714,'Hugo','Forester',55000,'IT Support Specialist','Male', '2019-11-22'),
#                    (51821,'Linda','Foster',95000,'Data Scientist','Female', '2019-04-29'),
#                    (67323,'Lisa','Wiener',75000,'Business Analyst','Female','2018-08-09'),
#                    (70950,'Rodney','Weaver',87000,'Project Manager','Male','2018-12-20'),
#                    (71329,'Gayle','Meyer',77000,'HR Manager','Female','2019-06-28'),
#                    (76589,'Jason','Christian',99000,'Project Manager','Male','2019-01-21'),
#                    (97927,'Billie','Lanning',67000,'Web Developer','Female','2018-06-25');""")
# cursor.execute("""CREATE TABLE IF NOT EXISTS public.departments (
#                     dept_ID INT,
#                     emp_ID INT,
#                     FOREIGN KEY (emp_ID) REFERENCES public.employees(emp_ID),
#                     dept_name TEXT NOT NULL);""")
# cursor.execute(""" INSERT INTO public.departments (dept_ID, emp_ID, dept_name) VALUES
#                     (13, 17679,'Operations'),
#                     (14, 26650,'Marketing'),
#                     (13, 30840,'Operations'),
#                     (12, 49714,'Technology'),
#                     (13, 51821,'Operations'),
#                     (14, 67323,'Marketing'),
#                     (11, 70950,'Administrative'),
#                     (13, 76589,'Operations'),
#                     (12, 97927,'Technology');""")


def query(query):
    try:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
            if cur.description:
                return cur.fetchall()
            else:
                return None
    except Exception as error:
        print(error)


# 1.Find the employees who get paid more than Rodney Weaver.
print(
    query(
        "SELECT * FROM employees WHERE salary > (SELECT salary FROM employees WHERE first_name = 'Rodney' AND last_name = 'Weaver')"
    )
)
# 2.Find the average, min and max salaries
res2 = query("SELECT AVG(salary), MIN(salary), MAX(salary) FROM employees")
print(res2)
print(f"Average salary: {res2[0][0]}")
print(f"Minimum salary: {res2[0][1]}")
print(f"Maximum salary: {res2[0][2]}")
# 3.Find the employees whose salary is more than 8700. Our query should return first name, last name, and salary info of the employees.
print(query("SELECT first_name, last_name, salary FROM employees WHERE salary > 8700"))
# 4.Find the employees (first name, last name from employees table) who work under the Operations department (departments table). Our query should return first name and last name info.
print(
    query(
        "SELECT first_name, last_name FROM employees WHERE emp_id IN (SELECT emp_id FROM departments WHERE dept_name ILIKE '%Operations%')"
    )
)
# 5.Find the employees (first name, last name from employees table) who work under the Technology department (departments table). Our query should return first name and last name info.
print(
    query(
        "SELECT first_name, last_name FROM employees WHERE emp_id IN (SELECT emp_id FROM departments WHERE dept_name ILIKE '%Technology%')"
    )
)
# 6.Find the average salary of female employees. I have gender field in employees table.
res6 = query("SELECT AVG(salary) FROM employees WHERE gender = 'Female'")
print(f"Average salary of female employees {res6[0][0]}")
# 7.Find the average salaries of each department.
res7 = query("SELECT job_title, AVG(salary) FROM employees GROUP BY job_title")
print(res7)
# 8.Find the oldest and newest employees. i have hire_date field in employees table.
res8 = query(
    "SELECT * FROM employees WHERE hire_date = (SELECT MIN(hire_date) FROM employees) or hire_date = (SELECT MAX(hire_date) FROM employees)"
)
print(f"Oldest employee: {res8[0][1]} {res8[0][2]}")
print(f"Newest employee: {res8[1][1]} {res8[1][2]}")
# 9.Find the hiring date and department of the highest paid employee
res9 = query(
    "SELECT hire_date, job_title FROM employees JOIN departments ON employees.emp_id = departments.emp_id WHERE salary = (SELECT MAX(salary) FROM employees)"
)
print(f"Hiring date of the highest paid employee: {res9[0][0]}")
# 10.Find the hiring date and department of the lowest paid employee
res10 = query(
    "SELECT hire_date, job_title FROM employees JOIN departments ON employees.emp_id = departments.emp_id WHERE salary = (SELECT MIN(salary) FROM employees)"
)
print(f"Hiring date of the lowest paid employee: {res10[0][0]}")
# connection.commit()
# # Bağlantıyı kapatın
# connection.close()
# print("Bağlantı kapatıldı.")

# Soru 1:
# cursor.execute("""select * from employees
#                 where salary > (select salary from employees where first_name='Rodney')"""
#                )
# records = cursor.fetchall()


# for row in records:
#     print("\n", row)
# connection.commit()
# connection.close()

# Soru 2:

# cursor.execute(
#     """select AVG(salary), max(salary), min(salary) from employees""")


# records = cursor.fetchall()
# for row in records:
#     print("\n", row)
# connection.commit()
# connection.close()

# Soru 3 :
# cursor.execute(
#     """select * from employees where salary > 87000""")
# records = cursor.fetchall()
# for row in records:
#     print("\n", row)
# connection.commit()
# connection.close()

# Soru 4 :
# select employees.first_name,employees.last_name from employees
# full join departments on employees.emp_id = departments.emp_id
# cursor.execute(
#     """select first_name,last_name from employees
# where emp_id in  (select emp_id from departments where dept_name = 'Operations')""")


# records = cursor.fetchall()
# for row in records:
#     print("\n", row)
# connection.commit()
# connection.close()

# Soru 5 :

# cursor.execute(
#     """SELECT e.first_name, e.last_name
# FROM employees as e
# JOIN departments d ON e.emp_id = d.emp_id
# WHERE d.dept_name = 'Technology';""")


# records = cursor.fetchall()
# for row in records:
#     print("\n", row)
# connection.commit()
# connection.close()
