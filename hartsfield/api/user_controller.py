"""
Copyright ©2023. The Regents of the University of California (Regents). All Rights Reserved.
Permission to use, copy, modify, and distribute this software and its documentation
for educational, research, and not-for-profit purposes, without fee and without a
signed licensing agreement, is hereby granted, provided that the above copyright
notice, this paragraph and the following two paragraphs appear in all copies,
modifications, and distributions.
Contact The Office of Technology Licensing, UC Berkeley, 2150 Shattuck Avenue,
Suite 510, Berkeley, CA 94720-1620, (510) 643-7201, otl@berkeley.edu,
http://ipira.berkeley.edu/industry-info for commercial licensing opportunities.
IN NO EVENT SHALL REGENTS BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT, SPECIAL,
INCIDENTAL, OR CONSEQUENTIAL DAMAGES, INCLUDING LOST PROFITS, ARISING OUT OF
THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION, EVEN IF REGENTS HAS BEEN ADVISED
OF THE POSSIBILITY OF SUCH DAMAGE.
REGENTS SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE
SOFTWARE AND ACCOMPANYING DOCUMENTATION, IF ANY, PROVIDED HEREUNDER IS PROVIDED
"AS IS". REGENTS HAS NO OBLIGATION TO PROVIDE MAINTENANCE, SUPPORT, UPDATES,
ENHANCEMENTS, OR MODIFICATIONS.
"""
from flask import current_app as app

data = [
    {
        "user": 'Cesar Villalobos',
        "uid": '1',
        "class_name": 'Linguistics 101',
        "signed_url": 'https://storage.googleapis.com/ucb-datahub-archived-homedirs/2022-2-summer/datahub/castle-cesarvh.tar.gz?x-goog-signature=9af82f40f0c157a5b445a06f478bffff0fceefeb5d8346286e166d7f2b154c9f7c2a78ddf7c4aef3c56fdf406691482aba353667d1f8a1c0eb78e2eb426ce77f74a3b8214e82aba2db80e8f44bd3c642f030e9920b6bda524321f878fd06a531758c7d92f8efe28642845cfd62d181cbd0c88d1ba22461f7b1dcb901d71f838a69c99e09b069d595e3c2441f60bdb0dbb64f165e76f7785338da4ad4e16be4545fd94b4e37495a483976c5c3e487c960ad348346499773ad39872d6c01b5838788c9a8697195e3953ea7e018ee6bf448456881048e8610d863bdd3332109fa4640fd4f2cc47e1721d76d9a47e2f74ca44974e4f1ea59a588da0a8dc7f7d8b6fe&x-goog-algorithm=GOOG4-RSA-SHA256&x-goog-credential=urlsigner@ucb-datahub-2018.iam.gserviceaccount.com/20230428/us-central1/storage/goog4_request&x-goog-date=20230428T203337Z&x-goog-expires=604800&x-goog-signedheaders=host',
        "expiration_date": '2023-12-04T21:20:00.000Z',
        "datahub_name": 'cesarvh'
    },
    {
        "user": 'Jonathan',
        "uid": '2',
        "class_name": 'SysAdmin 101',
        "signed_url": 'https://storage.googleapis.com/ucb-datahub-archived-homedirs/2022-2-summer/datahub/castle-jfelder.tar.gz?x-goog-signature=9af82f40f0c157a5b445a06f478bffff0fceefeb5d8346286e166d7f2b154c9f7c2a78ddf7c4aef3c56fdf406691482aba353667d1f8a1c0eb78e2eb426ce77f74a3b8214e82aba2db80e8f44bd3c642f030e9920b6bda524321f878fd06a531758c7d92f8efe28642845cfd62d181cbd0c88d1ba22461f7b1dcb901d71f838a69c99e09b069d595e3c2441f60bdb0dbb64f165e76f7785338da4ad4e16be4545fd94b4e37495a483976c5c3e487c960ad348346499773ad39872d6c01b5838788c9a8697195e3953ea7e018ee6bf448456881048e8610d863bdd3332109fa4640fd4f2cc47e1721d76d9a47e2f74ca44974e4f1ea59a588da0a8dc7f7d8b6fe&x-goog-algorithm=GOOG4-RSA-SHA256&x-goog-credential=urlsigner@ucb-datahub-2018.iam.gserviceaccount.com/20230428/us-central1/storage/goog4_request&x-goog-date=20230428T203337Z&x-goog-expires=604800&x-goog-signedheaders=host',
        "expiration_date": '2024-11-03T22:20:00.000Z',
        "datahub_name": 'jfelder'
    },
    {
        "user": 'Tester',
        "uid": '1',
        "class_name": 'Biology 10',
        "signed_url": 'https://storage.googleapis.com/ucb-datahub-archived-homedirs/2022-2-summer/datahub/castle-2efunatake.tar.gz?x-goog-signature=9af82f40f0c157a5b445a06f478bffff0fceefeb5d8346286e166d7f2b154c9f7c2a78ddf7c4aef3c56fdf406691482aba353667d1f8a1c0eb78e2eb426ce77f74a3b8214e82aba2db80e8f44bd3c642f030e9920b6bda524321f878fd06a531758c7d92f8efe28642845cfd62d181cbd0c88d1ba22461f7b1dcb901d71f838a69c99e09b069d595e3c2441f60bdb0dbb64f165e76f7785338da4ad4e16be4545fd94b4e37495a483976c5c3e487c960ad348346499773ad39872d6c01b5838788c9a8697195e3953ea7e018ee6bf448456881048e8610d863bdd3332109fa4640fd4f2cc47e1721d76d9a47e2f74ca44974e4f1ea59a588da0a8dc7f7d8b6fe&x-goog-algorithm=GOOG4-RSA-SHA256&x-goog-credential=urlsigner@ucb-datahub-2018.iam.gserviceaccount.com/20230428/us-central1/storage/goog4_request&x-goog-date=20230428T203337Z&x-goog-expires=604800&x-goog-signedheaders=host',
        "expiration_date": '2023-11-11T19:20:00.000Z',
        "datahub_name": 'tester'
    },
    {
        "user": 'Richard',
        "uid": '3',
        "class_name": 'Linguistics 101',
        "signed_url": 'https://cloud.google.com/signedurl/rmillet/465347319aa7234231dc586d71',
        "expiration_date": '2024-01-01T01:20:00.000Z',
        "datahub_name": 'rmillet'
    }
]

@app.route('/api/user/<user_id>/url', methods=['GET', 'POST'])
def get_user_url(user_id=None):
    # TO DO: Actual fetching logic
    return [d for d in data if d['datahub_name'] == user_id]

@app.route('/api/user/<uid>/urls', methods=['GET', 'POST'])
def get_user_urls(uid=None):
    # TO DO: Actual fetching logic
    return [d for d in data if d['uid'] == uid]

@app.route('/api/account')
def account_details():
    # Returns the details of the user that is currently logged in
    res = {
	    "uid": '1',
	    "userName": "Cesar Villalobos",
	    "datahubName": "cesarvh",
        "isAdmin": True
    }
    return res