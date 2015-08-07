from db_objects import Story, User, Task
from db_session import session

stories = [Story(id=1, story_title='Story 001'),
           Story(id=2, story_title='Story 002'),
           Story(id=3, story_title='Story 003')]
session.add(stories[0])
session.add(stories[1])
session.add(stories[2])

users = [User(id=1, user_name='User 001'),
         User(id=2, user_name='User 002'),
         User(id=3, user_name='User 003')]

tasks = [Task(id=1, task_title='Task 001', story_id=1, user_id=1),
         Task(id=2, task_title='Task 002', story_id=1, user_id=2),
         Task(id=3, task_title='Task 003', story_id=1, user_id=3),
         Task(id=4, task_title='Task 004', story_id=2, user_id=1),
         Task(id=5, task_title='Task 005', story_id=2, user_id=2),
         Task(id=6, task_title='Task 006', story_id=2, user_id=3),
         Task(id=7, task_title='Task 007', story_id=3, user_id=1),
         Task(id=8, task_title='Task 008', story_id=3, user_id=2),
         Task(id=9, task_title='Task 009', story_id=3, user_id=3)]

session.add_all(users + tasks)
session.commit()
