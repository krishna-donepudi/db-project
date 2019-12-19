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
        table.add_row(row)
    print(table)


def list_properties_menu(check_in, check_out):
    heading('List of Properties:')
    list_properties(check_in, check_out)


def list_properties(check_in, check_out):
    tmpl = '''
        SELECT title, description, address, price, city_state_country, available_from, available_to
          FROM Products
         WHERE %s >= available_from and %s <= available_to;
    '''
    # check_in, check_out have to change to date type
    cmd = cur.mogrify(tmpl, (check_in, check_out))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(['title', 'description', 'address',
                         'price', 'city_state_country', 'available_from', 'available_to'])
    print_rows(table, rows)
    print()


if __name__ == '__main__':
    try:
        # default database and user
        db, user = 'airbnb', 'isdb'
        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True
        cur = conn.cursor()
        print('User Story #3')
        US = '''

        As a: Consumer
        I want: To specify the date range of my intended booking
        So that: I can look at properties and experiences available on those dates

        Simple
        '''
        print(US)
        print('The following query lists all properties and experiences in the dates that you require')
        # hard code values
        print('Check-in date... ')
        check_in = '01/01/01'  # change to date type
        print(check_in)
        print('Check-out date: ')
        check_out = '01/02/01'  # change to date type
        print(check_out)
        list_properties_menu(check_in, check_out)
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))
