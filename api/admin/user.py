from adminlte.views import BaseAdminView


class UserView(BaseAdminView):
    column_editable_list = ['first_name', 'last_name', 'age']
    column_searchable_list = ['first_name', 'last_name', 'age']
    column_exclude_list = None
    column_details_exclude_list = None
    column_filters = ['first_name', 'last_name', 'age', 'created_at', 'updated_at']
    can_export = True
    can_view_details = True
    can_create = True
    can_edit = True
    can_delete = True
    edit_modal = True
    create_modal = True
    details_modal = True
