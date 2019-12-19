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


def specify_dates_menu(product_id, av_from, av_to):
    print('Original dates:')
    tmpl = '''
        SELECT product_id, available_from, available_to
          FROM Products
         WHERE product_id = %s;
    '''
    cmd = cur.mogrify(tmpl, (product_id,))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(['product_id', 'available_from', 'available_to'])
    print_rows(table, rows)
    specify_dates(product_id, av_from, av_to)


def specify_dates(product_id, av_from, av_to):
    tmpl = '''
        UPDATE Products
           SET available_from = %s, available_to = %s
         WHERE product_id = %s;
    '''
    # make av_from and av_to date type and respect interface
    cmd = cur.mogrify(tmpl, (av_from, av_to, product_id))
    print_cmd(cmd)
    cur.execute(cmd)
    print('Updated dates:')
    tmpl2 = '''
        SELECT product_id, available_from, available_to
          FROM Products
         WHERE product_id = %s;
    '''
    cmd2 = cur.mogrify(tmpl2, (product_id, ))
    print_cmd(cmd2)
    cur.execute(cmd2)
    rows = cur.fetchall()
    table = PrettyTable(['product_id', 'available_from', 'available_to'])
    print_rows(table, rows)
    print()


if __name__ == '__main__':
    try:
        # default database and user
        db, user = 'airbnb', 'isdb'
        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True
        cur = conn.cursor()
        print('User Story #6')
        US = '''
        As a: Property Host
        I want: To update the date range of when my product is available
        So that: I can show the dates I can provide services/accommodation

        Simple
        '''
        print(US)
        print('The following query updates the dates at which a property is available')
        # hard code values
        print('Product id... ')
        product_id = 3
        print(product_id)
        print('Available from... ')
        av_from = '01/05/01'  # change to date type
        print(av_from)
        print('Available to... ')
        av_to = '03/02/01'  # change to date type
        print(av_to)
        specify_dates_menu(product_id, av_from, av_to)
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))
