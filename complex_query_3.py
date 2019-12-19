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


def most_booked_menu():
    heading('List of most booked experiences')
    most_booked()


def most_booked():
    tmpl = '''
       SELECT b.product_id, p.title, p.description, p.address, count(b.product_id)
        FROM Bookings as b
        JOIN Products as p ON p.product_id = b.product_id
       WHERE b.product_id in (SELECT product_id FROM Experiences)
       GROUP BY b.product_id, p.title, p.description, p.address
       ORDER BY count(b.product_id) DESC
       LIMIT 3;
    '''
    cmd = cur.mogrify(tmpl)
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(['product_id', 'title', 'description',
                         'address', 'booked count'])
    print_rows(table, rows)
    print()


if __name__ == '__main__':
    try:
        # default database and user
        db, user = 'airbnb', 'isdb'
        print('User Story #8')
        US = '''
           As a:  Consumer
         I want:  Get the top 3 most booked experience in all experiences
        So That:  I can see my competitor’s offering


        Complex
        '''
        print(US)
        print('The following query shows the most booked experience')
        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True
        cur = conn.cursor()
        most_booked_menu()
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))
