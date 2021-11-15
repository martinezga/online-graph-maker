

class MyRouter(object):
    """
    A router to control all database operations on models
    """
    route_app_labels = {'api'}
    db_list = ['graph_db']

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'graph_db'

        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'graph_db'

        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Determine if relationship is allowed between two objects."""

        # Allow any relation between two models.
        if obj1._meta.app_label in self.route_app_labels and \
            obj2._meta.app_label in self.route_app_labels:

            return True

        # No opinion if neither object is in the allowed app (defer to default or other routers).
        elif self.route_app_labels not in [obj1._meta.app_label, obj2._meta.app_label]:

            return None

        # Block relationship if one object is in the allowed app and the other isn't.
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Ensure that the api app's models get created on the right database.
        """
        if app_label in self.route_app_labels:
            # The allowed app should be migrated only on the graph_db database.

            return db == 'graph_db'

        elif db == 'graph_db':
            # Ensure that all other apps don't get migrated on the graph_db database.

            return False

        return True
