# -*- coding: utf-8 -*-

import hyde.plugin
import hyde.model

class JadePlugin(hyde.plugin.Plugin):
    def __init__(self, site):
        super(JadePlugin, self).__init__(site)
        self.site = site
        self.settings = hyde.model.Expando(
            getattr(self.site.config, self.plugin_name, {}))
        self.settings.include_file_pattern = "*.jade"
        self.settings.include_paths = []
        site.config.update(
            dict(
                jinja2=dict(
                    env=dict(jade_file_extensions=('.html',)),
                    extensions="pyjade.ext.jinja.PyJadeExtension")))

    def text_resource_complete(self, resource, text):
        if resource.source_file.kind == 'jade':
            resource.relative_deploy_path = resource.relative_deploy_path.replace(
                ".jade", ".html")
            resource.source_file.kind == 'html'
