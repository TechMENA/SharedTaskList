from google.appengine.ext import ndb

# Create your models here.

class Task(ndb.Model):
    name = ndb.StringProperty()
    done = ndb.BooleanProperty()

class TaskList(ndb.Model):
    tasks = ndb.StructuredProperty(Task, repeated=True)
