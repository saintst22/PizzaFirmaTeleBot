import sqlite3 as sq
from create_bot import bot


def sql_start():
    global base, cur
    base = sq.connect('pizza.db')
    cur = base.cursor()
    if base:
        print('Data base connect OK')
    base.execute('CREATE TABLE IF NOT EXISTS menu (img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read(message):
    for i_value in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, i_value[0],
                             f'{i_value[1]}\nОписание: {i_value[2]}\nЦена: {i_value[-1]}')


async def sql_read_2():
    return cur.execute('SELECT * FROM menu').fetchall()


async def sql_delete_command(data):
    cur.execute('DELETE FROM menu WHERE name == ?', (data,))
    base.commit()
