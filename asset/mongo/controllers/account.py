from django.db import transaction
from django.db.models import Q

from asset.mongo.models import MongoAccountModel
from account.controllers import user as user_ctl
from base import controllers as base_ctl
from utils.onlyone import onlyone


def get_accounts(mongo_id, keyword=None, page_num=None, page_size=None, operator=None):
    '''
    获取Account列表
    '''
    base_query = MongoAccountModel.objects.filter(mongo_id=mongo_id)
    if keyword:
        base_query = base_query.filter(username__icontains=keyword)
    total = base_query.count()
    objs = base_ctl.query_objs_by_page(base_query, page_num, page_size)
    has_password = False
    if operator and user_ctl.has_permission(operator.id, MongoAccountModel.PASSWORD_PERMISSION):
        has_password = True
    data_list = []
    for obj in objs:
        data = obj.to_dict(has_password=has_password)
        data_list.append(data)
    data = {
        'total': total,
        'data_list': data_list,
    }
    return data


def get_account(obj_id, operator=None):
    '''
    获取Account详情
    '''
    obj = base_ctl.get_obj(MongoAccountModel, obj_id)
    has_password = False
    if operator and user_ctl.has_permission(operator.id, MongoAccountModel.PASSWORD_PERMISSION):
        has_password = True
    data = obj.to_dict(has_password=has_password)
    data['mongo'] = obj.mongo.to_dict()
    return data


@onlyone.lock(MongoAccountModel.model_sign, 'obj_id', 'obj_id', 30)
def update_account(obj_id, password, operator=None):
    '''
    编辑账号
    '''
    data = {
        'password': password,
    }
    obj = base_ctl.update_obj(MongoAccountModel, obj_id, data, operator)
    data = obj.to_dict()
    return data
