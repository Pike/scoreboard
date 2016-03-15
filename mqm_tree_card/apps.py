from __future__ import unicode_literals

from django.apps import AppConfig


class MqmTreeCardConfig(AppConfig):
    name = 'mqm_tree_card'
    css = '/static/mqm_tree_card/css/tree-card.css'
    js = '/static/mqm_tree_card/js/tree-card.js'
    template = 'mqm_tree_card/card.html'
