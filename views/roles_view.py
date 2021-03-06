from sanic.response import json
from sanic.views import HTTPMethodView
from models.admin import Role, User, Component, Function, Menu


class RolesView(HTTPMethodView):
    async def get(self, request):
        roles, count = await Role.search(**request.ctx.query)
        return json(dict(data=[role.to_dict(exclude=['users', 'components', 'menus', 'functions']) for role in roles],
                         count=count, code=0, msg="成功"))

    async def post(self, request):
        data = request.json
        if not data.get('name'):
            return json(dict(code=-1, msg='关键参数不能为空'))
        er = await Role.get_or_none(name=data.get('name'))
        if er:
            return json(dict(code=-1, msg='此角色已注册！'))
        nr = Role(**data)
        await nr.save()
        return json(dict(code=0, msg='角色创建成功!'))


class RoleView(HTTPMethodView):
    async def post(self, request, rid):
        # 给角色分配资源
        data = request.json
        records = list(data.keys())[0]
        role = await Role.get_or_none(id=rid)
        if not role:
            return json(dict(code=-1, msg='角色不存在'))
        await getattr(getattr(role, records), 'clear')()
        if data.get(records):
            async for record in eval(f"{records.rstrip('s').capitalize()}.filter(id__in={data.get(records)})"):
                await getattr(getattr(role, records), 'add')(record)

        return json(dict(code=0, msg='更新成功'))

    async def put(self, request, rid):
        data = request.json
        r = await Role.get_or_none(id=rid)
        if not r:
            return json(dict(code=-1, msg='角色不存在'))
        if not data.get('name'):
            return json(dict(code=-1, msg='关键参数不能为空'))
        for k, v in data.items():
            if k == 'name':
                er = await Role.get_or_none(name=v)
                if er and r.name != v:
                    return json(dict(code=-1, msg='此角色已注册！'))
            setattr(r, k, v)
        await r.save()
        return json(dict(code=0, msg='更新成功'))

    async def delete(self, request, rid):
        r = await Role.get_or_none(id=rid)
        if not r:
            return json(dict(code=-1, msg='角色不存在'))
        await r.delete()
        return json(dict(code=0, msg='删除成功'))
