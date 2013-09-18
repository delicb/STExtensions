from collections import OrderedDict
import re
import json
import sublime
import sublime_plugin
from xml.etree import ElementTree as ET


NS = 'http://telventdms.com/automatedtesting/repository/'

# repo = etree.parse(r'D:\sources\AutoTests\3.4.1\Repos\builder.xml')
# root = repo.getroot()
# print(dir(root))
# print(root.find('{%s}item' % NS))
# print(root.getchildren())
# print(etree.tostring(repo, pretty_print=True))
# print(dir(repo.getroot()))
# print(repo.getroot().items())
# for i in repo.getroot():
    # print(i)
# print(dir(repo))


class RepoXmlToJson(sublime_plugin.TextCommand):
    def run(self, edit):
        content = self.view.substr(sublime.Region(0, self.view.size()))
        repo = ET.fromstring(re.sub(' xmlns="[^"]+"', '', content))
        print(json.dumps(self.process_item(repo.find('item')), indent=4))
        self.view.replace(edit, sublime.Region(0, self.view.size()),
                          json.dumps(self.process_item(repo.find('item')), indent=4))

    def process_item(self, item, mapping=None):
        if mapping is None:
            mapping = OrderedDict()
        mapping['name'] = item.attrib['name']

        searchtimeout = item.get('searchtimeout', None)
        if searchtimeout is not None:
            mapping['searchtimeout'] = int(searchtimeout)

        item_filters = item.get('filters', None)
        if item_filters is not None:
            mapping['filters'] = item_filters

        mapping['rules'] = {}
        for rule in item.find('path').findall('rule'):
            print(list(rule))
            for single_rule in list(rule):
                mapping['rules'][single_rule.tag] = single_rule.text
                rule_filters = single_rule.get('filters')
                if rule_filters is not None:
                    mapping['rules']['filters'] = rule_filters
        children = item.find('children')
        if children is not None and len(children) > 0:
            mapping['children'] = []
            for ch in children:
                mapping['children'].append(self.process_item(ch))
        return mapping
