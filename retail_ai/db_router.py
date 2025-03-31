class ShopCustomerRouter:
    """
    A router to control database operations for shopkeepers and customers.
    """
    def db_for_read(self, model, **hints):
        """Point customer models to the 'customers' database."""
        if model._meta.app_label == 'customers':
            return 'customers'
        return 'default'

    def db_for_write(self, model, **hints):
        """Point customer models to the 'customers' database."""
        if model._meta.app_label == 'customers':
            return 'customers'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """Allow any relation if models are in the same database."""
        if obj1._meta.app_label == obj2._meta.app_label:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure models end up in the correct database."""
        if app_label == 'customers':
            return db == 'customers'
        return db == 'default'
