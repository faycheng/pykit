# -*- coding:utf-8 -*-
import os
import polib
import arrow

from pykit.i18n import errors


INTERNATIONALIZATION_DOMAIN = 'INTERNATIONALIZATION_DOMAIN'
LOCALE_DIR = 'LOCALE_DIR'
LANGUAGE = 'LANG'


def gen(entries,
        project_id_version=None,
        report_msg_id_bugs_to=None,
        last_translator=None,
        language_team=None,
        mime_version=None,
        content_type=None,
        content_transfer_encoding=None,
        plural_forms=None
        ):
    po = polib.POFile()
    po.metadata = {
        'Project-Id-Version': project_id_version,
        'Report-Msgid-Bugs-To': report_msg_id_bugs_to,
        'POT-Creation-Date': arrow.now().isoformat(),
        'Last-Translator': last_translator,
        'Language-Team': language_team,
        'MIME-Version': mime_version,
        'Content-Type': content_type,
        'Content-Transfer-Encoding': content_transfer_encoding,
        'Plural-Forms': plural_forms
    }
    for entry in entries:
        po.append(entry)
    return po


def init_locale_dir():
    pass


def save(po, domain=None, locale_dir=None, lang=None):
    domain = domain or os.getenv(INTERNATIONALIZATION_DOMAIN, None)
    locale_dir = locale_dir or os.getenv(LOCALE_DIR, '{}/locale'.format(os.getcwd()))
    lang = lang or os.getenv(LANGUAGE, 'zh_CN')
    po_file_dir = '{locale}/{lang}/LC_MESSAGES/'.format(locale=locale_dir, lang=lang)
    po_file_path = '{locale}/{lang}/LC_MESSAGES/{domain}.po'.format(locale=locale_dir, lang=lang, domain=domain)
    if domain is None:
        raise errors.DomainNotExist
    if not os.path.exists(po_file_dir):
        os.makedirs(po_file_dir)
    po.save(po_file_path)


