# -----------------------------------------------------------------
# Working with psycopg2
# -----------------------------------------------------------------

import psycopg2
from prettytable import PrettyTable
import sys
import datetime


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


def view_previous_menu(guest_id):
    heading('List of previously booked products: ')
    view_previous(guest_id)


def view_previous(guest_id):
    tmpl = '''
        SELECT p.title, p.description, p.address, b.price, b.guest_id
          FROM Users as u
          JOIN Bookings as b ON b.guest_id = u.user_id
          JOIN Products as p ON p.product_id = b.product_id
         WHERE b.guest_id = %s and p.product_id IN (SELECT product_id
                                                      FROM Properties);
    '''
    cmd = cur.mogrify(tmpl, (guest_id, ))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(['title', 'description', 'address',
                         'price', 'guest_id'])
    print_rows(table, rows)
    print()


if __name__ == '__main__':
    try:
        # default database and user
        db, user = 'airbnb', 'isdb'
        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True
        cur = conn.cursor()
        print('User Story #10')
        US = '''
           As a:  Consumer
         I want:  View previously booked properties
        So That:  To rebook them or recommend them to a friend


        Complex
        '''
        print(US)
        print('The following lists the previously rented properties')
        print('guest_id... ')
        guest_id = 3
        print(guest_id)
        view_previous_menu(guest_id)
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))
