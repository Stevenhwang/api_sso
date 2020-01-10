from sanic.response import text
from sanic import Blueprint
from models.admin import User, Role
import re

gateway_bp = Blueprint('gateway', version=2)


@gateway_bp.route('/auth_check')
async def auth_check(request):
    args = eval(str(request.args).replace('[', '').replace(']', ''))
    uid = args.get('uid')
    uri = args.get('uri')
    method = args.get('method')

    user = await User.get(id=uid)
    if user.is_super:
        return text("true")
    else:
        async for role in Role.filter(users=uid):
            for f in role.functions:
                if f.method_type == method and re.match(r'{}'.format(f.uri), uri) and f.status:
                    return text("true")
        return text("false")