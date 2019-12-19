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


def save_product_menu(guest_id, product_id):
    print('Old saves:')
    tmpl = ''' 
        SELECT product_id, guest_id
          FROM Saves
         WHERE guest_id = %s
         ORDER BY saved_date DESC, saved_time DESC
    '''
    cmd = cur.mogrify(tmpl, (guest_id,))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(['product_id', 'guest_id'])
    print_rows(table, rows)
    save_product(guest_id, product_id)
    print('New saves:')
    tmpl2 = ''' 
        SELECT product_id, guest_id
          FROM Saves
         WHERE guest_id = %s
         ORDER BY saved_date DESC, saved_time DESC
    '''
    cmd2 = cur.mogrify(tmpl2, (guest_id,))
    print_cmd(cmd2)
    cur.execute(cmd2)
    rows2 = cur.fetchall()
    table2 = PrettyTable(['product_id', 'guest_id'])
    print_rows(table2, rows2)


def save_product(guest_id, product_id):
    x = datetime.datetime.now()
    date = (x.strftime("%x"))
    time = (x.strftime("%X"))
    # hard code values later
    tmpl = '''
        INSERT INTO Saves(guest_id, product_id, saved_date,saved_time)
        VALUES (%s, %s, %s, %s);
    '''
    cmd = cur.mogrify(tmpl, (guest_id, product_id, date, time))
    print_cmd(cmd)
    cur.execute(cmd)
    print()


if __name__ == '__main__':
    try:
        # default database and user
        db, user = 'airbnb', 'isdb'
        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True
        cur = conn.cursor()
        print('User Story #9')
        US = '''
        As a: Consumer
        I want: Save the locations I am interested in
        So that: To view places I was interested in

        Simple
        '''
        print(US)
        print('The following query saves a certain product for a given guest')
        print('guest_id...')
        guest_id = 3
        print(guest_id)
        print('product_id')
        product_id = 2
        print(product_id)
        save_product_menu(guest_id, product_id)
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))
