# -*- coding:utf-8 -*-
import json
import os
import sys

import click
import polib

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from pykit.i18n.extract import extract
from pykit.i18n import po


def parse_lang(ctx, param, value):
    if '.' in value:
        value = value.split('.')[0]
    return value


@click.group()
def cli():
    pass


@cli.command()
def init():
    locale_dir = click.prompt('+Locale Dir', type=str, default='{}/locale'.format(os.getcwd()))
    metadata = dict(
        project_id_version=click.prompt('-Project ID Version', type=str, default=''),
        report_msg_id_bugs_to=click.prompt('-Report Msgid Bugs to', type=str, default=''),
        last_translator=click.prompt('+Last Translator', type=str, default=os.environ.get('LOGNAME')),
        language_team=click.prompt('-Language Team', type=str, default=''),
        mime_version=click.prompt('+Mime Version', type=str, default='1.0'),
        content_type=click.prompt('+Content Type', type=str, default='text/plain; charset=UTF-8'),
        content_transfer_encoding=click.prompt('+Content Transfer Encoding', type=str, default='8bit'),
        plural_forms=click.prompt('+Plural Forms', type=str, default='nplurals=2; plural=(n != 1);'),
    )
    conf = {
        'locale_dir': locale_dir,
        'metadata': metadata
    }
    conf_file_path = '{}/i18n.json'.format(os.getcwd())
    if not os.path.exists(conf_file_path):
        fd = open(conf_file_path, 'a+')
        fd.close()
    fd = open(conf_file_path, 'w')
    fd.write(json.dumps(conf))
    fd.close()


# TODO extract 时没有处理复数的情况
@cli.command()
@click.option('--domain', prompt=True,
              default=lambda: os.environ.get('INTERNATIONALIZATION_DOMAIN', os.getcwd().split('/')[-1]))
@click.option('--lang', prompt=True, default=lambda: os.environ.get('LANG', 'zh_CN'), callback=parse_lang)
@click.option('--input_file', prompt=True, default='')
@click.option('--input_dir', prompt=True, default='')
def gen(domain, lang, input_file, input_dir):
    if input_dir and input_file:
        click.echo('duplication input:{} {}'.format(input_file, input_dir))
        click.abort()

    conf = json.load(open('{}/i18n.json'.format(os.getcwd())))
    locale_dir = conf['locale_dir']
    input_files = []
    if input_file:
        input_files.append(input_file)
    if input_dir:
        for root, _, files in os.walk(input_dir):
            input_files.extend([os.path.join(root, f) for f in files if f.endswith('.py')])
    po_msgs = []
    for file in input_files:
        extracted_msgs = extract(file, '_')
        po_msgs.extend(extracted_msgs)
    po_msgs = list(set(po_msgs))
    po_entries = [polib.POEntry(msgid=msg, msgstr="") for msg in po_msgs]
    p = po.gen(po_entries, **conf['metadata'])
    po.save(p, domain, locale_dir, lang)


@cli.command()
@click.option('--input_file', prompt=True, default='')
@click.option('--input_dir', prompt=True, default='')
def compile(input_file, input_dir):
    if input_file and input_dir:
        click.echo('duplication input:{} {}'.format(input_file, input_dir))
        sys.exit(1)
    input_files = []
    if input_file:
        input_files.append(input_file)
    if input_dir:
        for root, _, files in os.walk(input_dir):
            input_files.extend([os.path.join(root, f) for f in files if f.endswith('.po')])
    for file in input_files:
        p = polib.pofile(file)
        mo_file_path = file.replace('.po', '.mo')
        p.save_as_mofile(mo_file_path)


@cli.command()
@click.argument('domain')
@click.argument('lang')
@click.option('--locale_dir', prompt=True,
              default=lambda: os.environ.get('LOCALE_DIR', '{}/locale'.format(os.getcwd())))
def status(domain, lang, locale_dir):
    po_file_path = '{locale}/{lang}/LC_MESSAGES/{domain}.po'.format(locale=locale_dir, lang=lang, domain=domain)
    if not (os.path.exists(po_file_path) and os.path.isfile(po_file_path)):
        click.echo('Po file({}) not exist or not file'.format(po_file_path))
        sys.exit(1)
    p = polib.pofile(po_file_path)
    click.echo('Metadata:\n{} \n'.format('\n'.join(['{}: {}'.format(k, v) for k, v in p.metadata.items()])))
    click.echo('Translated Entries:\n{}\n'.format('\n'.join([str(entry) for entry in p.translated_entries()])))
    click.echo('Untranslated Entries:\n{}\n'.format('\n'.join([str(entry) for entry in p.untranslated_entries()])))


if __name__ == '__main__':
    cli()
