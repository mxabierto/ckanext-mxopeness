import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


def get_data_fusion_endpoint():
    return "https://api.datos.gob.mx/v1/data-fusion"


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
            'get_data_fusion_endpoint': get_data_fusion_endpoint
        }