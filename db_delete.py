import logging
from db_objects import Story, User, Task
from db_session import session


logging.basicConfig()
logger = logging.getLogger("db_query")
logger.setLevel(logging.DEBUG)

# Query one task
task = (session.query(Task).join(Story).join(User)
        .filter(Story.story_title == 'Story 001')
        .filter(User.user_name == 'User 003')).one()
logger.info('Task in Story 001 and owned by User 003 is:')
logger.info('\tid = ' + str(task.id))
logger.info('\ttask_title = ' + task.task_title)
logger.info('\tstory_id = ' + str(task.story_id))
logger.info('\tuser_id = ' + str(task.user_id))

# Delete this task and query again
session.delete(task)
session.commit()
num = (session.query(Task).join(Story).join(User)
       .filter(Story.story_title == 'Story 001')
       .filter(User.user_name == 'User 003')).count()
logger.info(str(num) + " task queried")

# Add the task back and query again
session.add(Task(id=3, task_title='Task 003', story_id=1, user_id=3))
session.commit()
task = (session.query(Task).join(Story).join(User)
        .filter(Story.story_title == 'Story 001')
        .filter(User.user_name == 'User 003')).one()
logger.info('Task in Story 001 and owned by User 003 is:')
logger.info('\tid = ' + str(task.id))
logger.info('\ttask_title = ' + task.task_title)
logger.info('\tstory_id = ' + str(task.story_id))
logger.info('\tuser_id = ' + str(task.user_id))
