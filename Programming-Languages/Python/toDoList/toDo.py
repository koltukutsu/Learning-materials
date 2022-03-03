from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
import datetime


def add_tasks():
    """
    :return: new task
    """
    given_task = str(input('\nEnter task:\n'))
    given_date = str(input('Enter deadline:\n')).split('-')
    
    new_row = Table(task=given_task,
                    deadline=datetime.date(int(given_date[0]),    # YYYY
                                           int(given_date[1]),    # MM
                                           int(given_date[2])))    # DD
    print('the task has been added!\n')

    return new_row


def delete_tasks():
    """
    Deletes tasks from sql database
    :return: None
    """

    rows = session.query(Table).order_by(Table.deadline.asc()).all()
    tasks = rows[:]

    print('\nAll tasks:')
    if not tasks:
        print('Nothing to do!')
        print('')
    else:
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i].task}. {tasks[i].deadline.strftime('%d %b')}")
        print('')

    to_delete = int(input('Choose the number of the task you want to delete:'))
    session.delete(tasks[to_delete - 1])


def task_shower(flag):
    """
    1 means show the today's tasks
    2 means show the week's tasks
    3 means show all of the tasks
    :return: None, only prints
    """

    if flag == 1:   # TODO: need to show like WASH THE DISHED 28.APR
        rows = session.query(Table).filter(Table.deadline == datetime.datetime.today().date()).all()
        tasks = rows[:]
        print(datetime.datetime.today().strftime('\n%A %d %b:'))
        if not tasks:
            print('Nothing to do!\n')
        else:
            for i in range(len(tasks)):
                print(f'{i + 1}. {tasks[i].task}')

    elif flag == 2:     # TODO: Show the week
        for extra_day in range(7):
            date_to_use = datetime.datetime.today() + datetime.timedelta(extra_day)
            rows = session.query(Table).filter(Table.deadline == date_to_use.date()).all()
            tasks = rows[:]

            print(date_to_use.strftime('\n%A %d %b:'))
            if not tasks:
                print('Nothing to do!')
                if extra_day == 6:
                    print('')
            else:
                for i in range(len(tasks)):
                    print(f'{i + 1}. {tasks[i].task}')

    elif flag == 3:     # TODO: SHOW ALL
        rows = session.query(Table).order_by(Table.deadline.asc()).all()
        tasks = rows[:]

        print('\nAll tasks:')
        if not tasks:
            print('Nothing to do!')
            print('')
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i].task}. {tasks[i].deadline.strftime('%d %b')}")
            print('')
    elif flag == 4:
        rows = session.query(Table).filter(Table.deadline < datetime.datetime.today().date()).all()
        tasks = rows[:]

        if not tasks:
            print('Nothing to do!')
        else:
            print('\nMissed tasks:')
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i].task}. {tasks[i].deadline.strftime('%d %b')}")
            print('\n')

def start():
    """
    Starts the program
    :return: None
    """
    while True:
        print("1) Today's tasks", "2) Week's tasks", "3) All tasks", "4) Missed tasks", "5) Add task", "6) Delete task", "0) Exit", sep='\n')
        taken = str(input(""))

        if taken in '1234':     # TODO: DO not forget to add missed tasks to task_shower!!
            task_shower(int(taken))

        elif taken == '5':
            to_add = add_tasks()
            session.add(to_add)
            session.commit()

        elif taken == '6':
            delete_tasks()
            session.commit()

        elif taken == '0':
            print('Bye!')
            break

        else:
            print('Invalid Expression')


engine = create_engine('sqlite:///todo.db?check_same_thread=False')  # this is for creating the database
Base = declarative_base()  # this is for shaping database

Session = sessionmaker(bind=engine)  # binding is important, TODO: Do not miss the binding!
session = Session()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.datetime.today())
    
    def __repr__(self):
        return self.task

# ATTENTION: so that means that it is important to do things in order


Base.metadata.create_all(engine)  # now we made the database


start()
