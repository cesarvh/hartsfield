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

@app.route('/api/user/<user_id>/url', methods=['GET', 'POST'])
def get_user_url(user_id=None):
    # TO DO: Actual fetching logic
    response = [{
            "user": 'Cesar Villalobos',
            "uid": '1',
            "signed_url": 'https://mockurl.berkeley.edu/9fed0c91c15a01c86cac2a6e74eede0e',
            "expiration_date": '2023-04-13T21:20:00.000Z'
        },
        {
            "user": 'Cesar Villalobos',
            "uid": '1',
            "signed_url": 'https://mockurl.berkeley.edu/406dae77319aa765d84e9f81dc586d71',
            "expiration_date": '2023-12-04T21:20:00.000Z'
        }
    ]
    return response

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

