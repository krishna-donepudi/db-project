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


def send_message_menu(msg, guest_id, host_id):
    print('User Story #7')
    print('The following query sends messages to a client')
    send_message(msg, guest_id, host_id)


def send_message(msg, guest_id, host_id):
    # probably should hard code values
    tmpl = '''
        INSERT INTO Messages(message_content, guest_id, host_id)
             VALUES (%s, %s, %s);
    '''
    cmd = cur.mogrify(tmpl, (msg, guest_id, host_id))
    print_cmd(cmd)
    cur.execute(cmd)
    print('New message:')
    tmpl2 = '''
        SELECT message_content, guest_id, host_id
          FROM Messages
         ORDER by time DESC
         LIMIT 1;
    '''
    cmd2 = cur.mogrify(tmpl2)
    print_cmd(cmd2)
    cur.execute(cmd2)
    rows = cur.fetchall()
    table = PrettyTable(['message_content', 'guest_id', 'host_id'])
    print_rows(table, rows)
    print()


if __name__ == '__main__':
    try:
        # default database and user
        db, user = 'airbnb', 'isdb'
        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True
        cur = conn.cursor()
        # change model before changing query
        US = '''
        As a: Experience Host
        I want: Send messages to my clients
        So that: I can communicate a time to meet and place


        Simple
        '''
        print(US)
        print('message...')
        msg = 'I am stronger :) '
        print(msg)
        print('guest_id...')
        guest_id = 3
        print(guest_id)
        print('host_id...')
        host_id = 1
        print(host_id)
        send_message_menu(msg, guest_id, host_id)
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))
