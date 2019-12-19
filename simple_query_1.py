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


def list_properties_menu(location):
    heading('List of Properties:')
    list_properties(location)


def list_properties(location):
    tmpl = '''
        SELECT title, description, address, price, city_state_country
          FROM Products
         WHERE city_state_country = %s;
    '''
    cmd = cur.mogrify(tmpl, (location,))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(['title', 'description', 'address',
                         'price', 'city_state_country'])
    print_rows(table, rows)
    print()


if __name__ == '__main__':
    try:
        db, user = 'airbnb', 'isdb'
        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True
        cur = conn.cursor()
        print('User Story #2')
        US = '''
           As a:  Consumer
         I want:  To specify the location of my intended booking
        So That:  I can look at available properties and experiences in that location


        Simple
        '''
        print(US)
        print('The following query lists all properties and experiences in the location that you specify')
        # can hard code this
        print('Specifying location.... ')
        location = 'pittsburgh pa usa'
        print(location)
        list_properties_menu(location)
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))
