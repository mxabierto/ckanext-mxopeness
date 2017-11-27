import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.lib.helpers import resource_display_name


def get_data_fusion_endpoint():
    return "https://api.datos.gob.mx/v1/data-fusion"

def resource_display_name_clean(resource_dict):
    raw_name = resource_display_name(resource_dict)
    return raw_name.strip()

class MxopenessPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'mxopeness')
    
    def get_helpers(self):
        return {
            'get_data_fusion_endpoint': get_data_fusion_endpoint,
            'resource_display_name_clean': resource_display_name_clean
        }