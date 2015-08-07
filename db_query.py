import logging
from db_objects import Story, User, Task
from db_session import session


logging.basicConfig()
logger = logging.getLogger("db_query")
logger.setLevel(logging.DEBUG)

# Query by instance
logger.info('------ Query by instance ------')
for story in session.query(Story).order_by(Story.id).all():
    logger.info('ID = ' + str(story.id) + ', Story Title = '
                + story.story_title)

for task in session.query(Task).order_by(Task.id).all():
    logger.info('ID = ' + str(task.id) + ', Task Title = '
                + task.task_title + ', Story ID = '
                + str(task.story_id) + ', User ID = '
                + str(task.user_id))

# Query by attributes
logger.info('------ Query by attributes ------')
for id, user_name in (session.query(User.id, User.user_name).
                      order_by(User.id).all()):
    logger.info('ID = ' + str(id) + ', User Name = ' + user_name)

# Query with foreign key
logger.info('------ Query with foreign key ------')
for story in session.query(Story).order_by(Story.id).all():
    logger.info('ID = ' + str(story.id) + ', Story Title = '
                + story.story_title)
    for task in story.story_task_relation:
        logger.info("\tTask Title = " + task.task_title)

for task in session.query(Task).order_by(Task.id).all():
    logger.info('ID = ' + str(task.id) + ', Task Title = '
                + task.task_title + ', Story ID = '
                + str(task.story_id) + ', Story Title = '
                + task.task_story_relation.story_title + ', User ID = '
                + str(task.user_id) + ', User Name = '
                + task.task_user_relation.user_name)

# Query with association_proxy attribute
logger.info('------ Query with association_proxy attribute ------')
for story in session.query(Story).all():
    logger.info('Story ' + story.story_title + ' contains task list '
                + repr(story.task_titles))

for user in session.query(User).all():
    logger.info('User ' + user.user_name + ' owns task list '
                + repr(user.task_titles))

# Query with filter
logger.info('------ Querywith filter ------')
for story in session.query(Story).filter(Story.story_title == 'Story 002'):
    logger.info('ID of Story 002 is ' + str(story.id))

for task in session.query(Task).filter(Task.user_id == 2):
    logger.info('User 2 owns task ' + task.task_title)

# Query without joins
logger.info('------ Query without joins------')
for story, task in (session.query(Story, Task)
                    .filter(Story.id == Task.story_id)
                    .filter(Task.task_title == 'Task 007').all()):
    logger.info('Task 007 is in story ' + story.story_title)

# Query with joins
logger.info('------ Query with joins------')
for story in (session.query(Story).join(Task)
              .filter(Task.task_title == 'Task 007').all()):
    logger.info('Task 007 is in story ' + story.story_title)
