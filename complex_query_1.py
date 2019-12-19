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


def read_description_menu(product_id):
    heading('Description:')
    read_description(product_id)


def read_description(product_id):
    tmpl = '''
        SELECT u.first_name, p.product_id, h.description
          FROM Products as p
               JOIN Hosts as h ON h.user_id = p.host_id
               JOIN Users as u ON u.user_id = h.user_id
         WHERE p.product_id = %s;
    '''
    cmd = cur.mogrify(tmpl, (product_id,))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(['first_name', 'product_id', 'description'])
    print_rows(table, rows)
    print()


if __name__ == '__main__':
    try:
        # default database and user
        db, user = 'airbnb', 'isdb'
        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True
        cur = conn.cursor()
        print('User Story #1')
        US = '''
           As a:  Consumer
         I want:  To read about my the host I am intending to stay with it
        So That:  I can align my interests with the interests of the host


        Complex
        '''
        print(US)
        print('The following query gives you the description if given the product_id')
        print("Product_id:")
        product_id = 2
        print(product_id)
        read_description_menu(product_id)
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))
