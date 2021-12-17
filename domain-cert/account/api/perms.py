from django.contrib.auth.models import Permission,ContentType
from datetime import datetime,date
class PermsManage(object):
    def __init__(self):
        super(PermsManage, self).__init__() 

    def convert_to_dict(self,model):      
        for fieldName in model._meta.get_fields():
            try:
                fieldValue = getattr(model,fieldName.name)
                if type(fieldValue) is date or type(fieldValue) is datetime:
                    fieldValue = datetime.strftime(fieldValue, '%Y-%m-%d %H:%M:%S')
                setattr(model, fieldName.name, fieldValue)    
            except Exception as ex:
                pass

        data = {}
        data.update(model.__dict__)
        data.pop("_state", None)
        data.pop("script_file",None)
        data.pop("cron_script",None)
        data.pop("_cron_server_cache",None)
        data.pop("playbook_file",None)
        data.pop('_assets_cache',None)
        data.pop('sudo_passwd',None)
        data.pop('passwd',None)  
        data.pop('codename',None)  
        data.pop('content_type_id',None)  
        data.pop('_project_cache',None)
        data.pop('_network_assets_cache',None)
        data.pop('_server_assets_cache',None)            
        return data

    
    def get_apps(self):
        dataList = []
        for ds in ContentType.objects.all():
            dataList.append({"label":ds.app_label,"content_type":ds.id,"apps_name":ds.name})
        return dataList    
    
    def perms(self,content_type):
        perms = []
        for ds in Permission.objects.filter(content_type=content_type):
            perms.append(self.convert_to_dict(ds)) 
        return perms       
    
    def get_perms(self): 
        permsList = []
        for ds in self.get_apps():             
            if ds.get("label") in ["auth","contenttypes","admin","sessions"] or ds.get("label").startswith("django"):continue
            for ps in self.perms(content_type=ds.get("content_type")):
                ps["apps_name"] = ds.get("apps_name")
                permsList.append(ps)
        return permsList     