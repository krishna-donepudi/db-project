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
        product_id, title, description, address, price, location, rating = row

        table.add_row((product_id, title, description,
                                 address, price, location, "%.2f"%rating))
    print(table)


def list_properties_menu():
    print('User Story #4')
    print('The following query lists all properties based on average ratings')
    heading('List of Properties:')
    list_properties()


def list_properties():
    tmpl = '''
        SELECT p.product_id, p.title, p.description, p.address, p.price, p.city_state_country, avg(r.rating_score) as rating
          FROM Products as p
               JOIN Reviews as r ON r.product_id = p.product_id
         GROUP by p.product_id
         ORDER BY rating DESC;
    '''
    cmd = cur.mogrify(tmpl)
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(['product_id', 'title', 'description',
                         'address', 'price', 'location', 'rating'])
    print_rows(table, rows)
    print()


if __name__ == '__main__':
    try:
        # default database and user
        db, user = 'airbnb', 'isdb'
        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True
        cur = conn.cursor()
        US = '''
           As a:  Consumer
         I want:  To sort properties and experiences based on average rating
        So That:  I can look at the best properties and experiences first


        Complex
        '''
        print(US)
        list_properties_menu()
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))
