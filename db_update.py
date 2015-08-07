import logging
from db_objects import Story, User, Task
from db_session import session


logging.basicConfig()
logger = logging.getLogger("db_query")
logger.setLevel(logging.DEBUG)


def query_task():
    task = (session.query(Task).join(Story).join(User)
            .filter(Story.story_title == 'Story 001')
            .filter(User.user_name == 'User 003')).one()
    logger.info('Task in Story 001 and owned by User 003 is '
                + task.task_title)
    return task

# Query one task
task = query_task()

# Update the task and query again
task.task_title = 'Changed Task Title'
session.commit()
query_task()

# Update the task back and query again
task.task_title = 'Task 003'
session.commit()
query_task()
