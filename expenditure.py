class database:
    def build_database():
        cnx = mysql.connector.connect(user='root', password='',
                                      host='localhost')
        cur = cnx.cursor()
        cur.execute("create database if not exists expenditure")
        cnx.close()

    def build_table():
        cnx = mysql.connector.connect(user='root', password='',
                                      host='localhost', database="expenditure")
        cur = cnx.cursor()
        cur.execute(
            "create table if not exists expense (id int auto_increment primary key, iname varchar(255) ,icost float, edate date)")
        cnx.close()

    def insert_fields(n, c, d):
        cnx = mysql.connector.connect(user='root', password='',
                                      host='localhost', database="expenditure")
        cur = cnx.cursor()
        sql = "insert into expense(iname,icost,edate) values(%s,%s,%s)"
        val = (n, c, d)
        cur.execute(sql, val)
        cnx.commit()
        cnx.close()

class day:
    def day_expense():
        cost = []
        items = []
        today = datetime.date(datetime.now())
        cnx = mysql.connector.connect(user='root', password='',
                                      host='localhost', database="expenditure")
        cur = cnx.cursor()
        cur.execute("select * from expense")
        res = cur.fetchall()
        for i in range(len(res)):
            if (res[i][3] == today):
                items.append(res[i][1])
                cost.append(res[i][2])
        for j in range(len(items)):
            print(items[j], ':', cost[j])
        print("You spent ", sum(cost), " today")
        cnx.close()


class weekly:
    def week_expense():
        items = []
        cost = []
        today = datetime.now()
        month = today.month
        year = today.year
        day = today.day
        temp = day
        count = 0
        week_dates = []
        week_dates.append(day)
        if (month % 2 == 0):
            if (year % 4 != 0 and month == 2):
                while (count < 6):
                    week_dates.append((temp - 1) % 29)
                    if (week_dates.count(0) == 1):
                        index = week_dates.index(0)
                        del (week_dates[index])
                        count -= 1
                    temp -= 1
                    count += 1
            elif (year % 4 == 0 and month == 2):
                while (count < 6):
                    week_dates.append((temp - 1) % 30)
                    if (week_dates.count(0) == 1):
                        index = week_dates.index(0)
                        del (week_dates[index])
                        count -= 1
                    temp -= 1
                    count += 1
            else:
                while (count < 6):
                    week_dates.append((temp - 1) % 32)
                    if (week_dates.count(0) == 1):
                        index = week_dates.index(0)
                        del (week_dates[index])
                        count -= 1
                    temp -= 1
                    count += 1
        else:
            while (count < 6):
                week_dates.append((temp - 1) % 32)
                if (week_dates.count(0) == 1):
                    index = week_dates.index(0)
                    del (week_dates[index])
                    count -= 1
                temp -= 1
                count += 1
        cnx = mysql.connector.connect(user='root', password='',
                                      host='localhost',
                                      database="expenditure"
                                      )
        cur = cnx.cursor()
        cur.execute("select * from expense")
        res = cur.fetchall()
        for i in range(len(res)):
            date = str(res[1][3])
            date = date[8:10]
            if (int(date) in week_dates):
                items.append(res[i][1])
                cost.append(res[i][2])
        for j in range(len(items)):
            print(items[j], ':', cost[j])
        print("You spent ", sum(cost), " from the past 7 days.")
        cnx.close()


class monthly:
    def monthly_expense():
        items = []
        cost = []
        today = datetime.now()
        month = today.month
        cnx = mysql.connector.connect(user='root', password='',
                                      host='localhost',
                                      database="expenditure"
                                      )
        cur = cnx.cursor()
        cur.execute("select * from expense")
        res = cur.fetchall()
        for i in range(len(res)):
            date = str(res[1][3])
            date = date[5:7]
            if (int(date) == month):
                items.append(res[i][1])
                cost.append(res[i][2])
        for j in range(len(items)):
            print(items[j], ':', cost[j])
        print("You spent ", sum(cost), " this month.")
        cnx.close()


class quarterly:
    def quarterly_expense():
        items = []
        cost = []
        today = datetime.now()
        month = today.month
        temp = month
        count = 0
        months = []
        months.append(month)
        while (count < 2):
            months.append((temp - 1) % 13)
            if (months.count(0) == 1):
                index = months.index(0)
                del (months[index])
                count -= 1
            temp -= 1
            count += 1
        cnx = mysql.connector.connect(user='root', password='',
                                      host='localhost',
                                      database="expenditure"
                                      )

        cur = cnx.cursor()
        cur.execute("select * from expense")
        res = cur.fetchall()
        for i in range(len(res)):
            date = str(res[1][3])
            date = date[5:7]
            if (int(date) in months):
                items.append(res[i][1])
                cost.append(res[i][2])
        for j in range(len(items)):
            print(items[j], ':', cost[j])
        print("You spent ", sum(cost), " from the past 3 months.")
        cnx.close()


class halfyearly:
    def halfyearly_expense():
        items = []
        cost = []
        today = datetime.now()
        month = today.month
        temp = month
        count = 0
        week_dates = []
        week_dates.append(month)
        while (count < 5):
            week_dates.append((temp - 1) % 13)
            if (week_dates.count(0) == 1):
                index = week_dates.index(0)
                del (week_dates[index])
                count -= 1
            temp -= 1
            count += 1
        cnx = mysql.connector.connect(user='root', password='',
                                      host='localhost',
                                      database="expenditure"
                                      )

        cur = cnx.cursor()
        cur.execute("select * from expense")
        res = cur.fetchall()
        for i in range(len(res)):
            date = str(res[1][3])
            date = date[5:7]
            if (int(date) in week_dates):
                items.append(res[i][1])
                cost.append(res[i][2])
        for j in range(len(items)):
            print(items[j], ':', cost[j])
        print("You spent ", sum(cost), " from the past 6 months.")
        cnx.close()


class specific:
    def specific_day(day):
        cost = []
        items = []
        cnx = mysql.connector.connect(user='root', password='',
                                      host='localhost', database="expenditure")
        cur = cnx.cursor()
        cur.execute("select * from expense")
        res = cur.fetchall()
        for i in range(len(res)):
            if (str(res[i][3]) == day):
                items.append(res[i][1])
                cost.append(res[i][2])
        for j in range(len(items)):
            print(items[j], ':', cost[j])
        print("You spent ", sum(cost), " in ", day)
        cnx.close()

    def specific_month(m):
        items = []
        cost = []
        cnx = mysql.connector.connect(user='root', password='',
                                      host='localhost',
                                      database="expenditure"
                                      )
        cur = cnx.cursor()
        cur.execute("select * from expense")
        res = cur.fetchall()
        for i in range(len(res)):
            date = str(res[1][3])
            date = date[5:7]
            if (date == m):
                items.append(res[i][1])
                cost.append(res[i][2])
        for j in range(len(items)):
            print(items[j], ':', cost[j])
        print("You spent ", sum(cost), " in month ", m)
        cnx.close()

    def specific_year(year):
        items = []
        cost = []
        year = str(year[0:4])
        cnx = mysql.connector.connect(user='root', password='',
                                      host='localhost',
                                      database="expenditure"
                                      )
        cur = cnx.cursor()
        cur.execute("select * from expense")
        res = cur.fetchall()
        for i in range(len(res)):
            date = str(res[1][3])
            date = date[0:4]
            if (date == year):
                items.append(res[i][1])
                cost.append(res[i][2])
        for j in range(len(items)):
            print(items[j], ':', cost[j])
        print("You spent ", sum(cost), " in ", year)
        cnx.close()


class annual:
    def annual_expense():
        items = []
        cost = []
        today = datetime.now()
        year = today.year
        cnx = mysql.connector.connect(user='root', password='',
                                      host='localhost',
                                      database="expenditure"
                                      )
        cur = cnx.cursor()
        cur.execute("select * from expense")
        res = cur.fetchall()
        for i in range(len(res)):
            date = str(res[1][3])
            date = date[0:4]
            if (int(date) == year):
                items.append(res[i][1])
                cost.append(res[i][2])
        for j in range(len(items)):
            print(items[j], ':', cost[j])
        print("You spent ", sum(cost), " this year.")
        cnx.close()


def menu():
    print("Press enter to add spent items")
    print("Press 1 to know today's expenditure")
    print("Press 2 to know this week's expenditure")
    print("Press 3 to know this month's expenditure")
    print("Press 4 to know three month's expenditure")
    print("Press 5 to know six month's expenditure")
    print("Press 6 to know this year's expenditure")
    print("Press 7 to know some specific day, month, year expenditure")
    print("Press 8 to add spent items which you missed to add")
    print("Press any other key to exit")
