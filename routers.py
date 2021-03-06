from views.users_view import UsersView, UserView
from views.logout_view import LogoutView
from views.reset_pw import ResetPWView
from views.roles_view import RolesView, RoleView
from views.menus_view import MenusView, MenuView
from views.components_view import ComponentsView, ComponentView
from views.functions_view import FunctionsView, FunctionView
from views.auth_view import AuthView
from views.token_view import TokenView
from views.logs_view import LogsView
from views.white_url_view import WhiteUrlView
from views.back_service_view import BackServiceView

routers = [
    (UsersView.as_view(), '/users'),
    (UserView.as_view(), '/users/<uid:int>'),
    (LogoutView.as_view(), '/logout'),
    (ResetPWView.as_view(), '/reset_pw'),
    (RolesView.as_view(), '/roles'),
    (RoleView.as_view(), '/roles/<rid:int>'),
    (MenusView.as_view(), '/menus'),
    (MenuView.as_view(), '/menus/<mid:int>'),
    (ComponentsView.as_view(), '/components'),
    (ComponentView.as_view(), '/components/<cid:int>'),
    (FunctionsView.as_view(), '/functions'),
    (FunctionView.as_view(), '/functions/<fid:int>'),
    (AuthView.as_view(), '/auth'),
    (TokenView.as_view(), '/token'),
    (LogsView.as_view(), '/logs'),
    (WhiteUrlView.as_view(), '/white_url'),
    (BackServiceView.as_view(), '/services')
]
