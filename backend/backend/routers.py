

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

        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Ensure that the api app's models get created on the right database.
        """
        if db == 'graph_db':
            # The allowed app should be migrated only on the graph_db database.
            if app_label in self.route_app_labels:
                return True            
            else:
                # Ensure that all other apps don't get migrated on the graph_db database.
                return False
        # Other database should not migrate graph_db app models            
        elif app_label in self.route_app_labels:
            return False
        # Otherwise no opinion, defer to other routers or default database
        return None