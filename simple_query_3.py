# -----------------------------------------------------------------
# Working with psycopg2
# -----------------------------------------------------------------

import psycopg2
from prettytable import PrettyTable
import sys


def heading(str):
    print('-'*60)
    print("** %s:" % (str,))
    print('-'*60, '\n')


SHOW_CMD = True


def print_cmd(cmd):
    if SHOW_CMD:
        print(cmd.decode('utf-8'))


def print_rows(table, rows):
    for row in rows:
        price = int(row[0])
        table.add_row(("$%.2f"%price,))
    print(table)


def list_price_menu(location):
    heading('Average price: ')
    list_price(location)


def list_price(location):
    tmpl = '''
        SELECT avg(price)
          FROM Products
         WHERE city_state_country = %s;
    '''
    cmd = cur.mogrify(tmpl, (location,))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(['avg_price'])
    print_rows(table, rows)
    print()


if __name__ == '__main__':
    try:
        # default database and user
        db, user = 'airbnb', 'isdb'
        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True
        cur = conn.cursor()
        print('User Story #5')
        US = '''
        As a: Property Host
        I want: To look at the average price of Airbnb properties and experiences around my location
        So that: I can gauge the market demand and price my property or experience accordingly

        Simple
        '''
        print(US)
        print('The following query gives the average price of properties and experiences in a certain area')
        # hard code value
        print('Location for average price... ')
        location = 'pittsburgh pa usa'
        print(location)
        list_price_menu(location)

    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))
