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
from urllib.parse import urlencode, urljoin, urlparse


from flask import current_app as app, flash, redirect, session, request, url_for
import cas

service_url = 'http://localhost:5000/login'
encoded_url = service_url + "?next=" + urlencode({'url': '/api/account'})
cas_server = 'https://auth-test.berkeley.edu/cas/'

cas_client = cas.CASClient(
    version=3,
    service_url=encoded_url,
    server_url=cas_server
)

def _cas_client(target_url=None):
    cas_server = 'https://auth-test.berkeley.edu/cas/' # TO DO: Configure in configs
    service_url = url_for('.cas_login', _external=True)
    print (service_url)

    # One (possible) advantage this has over "request.base_url" is that it embeds the configured SERVER_NAME.
    if target_url:
        service_url = service_url + '?' + urlencode({'url': target_url})
    return cas.CASClientV3(server_url=cas_server, service_url=service_url)
    

@app.route('/cas/callback', methods=['GET', 'POST'])
def cas_login():
    # do the login
    if 'username' in session: 
        # Already logged in
        return redirect(url_for('account'))
    next = request.args.get('next')
    ticket = request.args.get('ticket')

    if not ticket:
        # No ticket, so we redirect to CAS login
        cas_login_url = cas_client.get_login_url()
        print('The url: ' + cas_login_url)
        return redirect(cas_login_url)
    
    # there is a ticket, so its coming from the callback
    print('ticket: ' + ticket)
    print('next' + next)

    user, attributes, pgtiou = cas_client.verify_ticket(ticket)

    print(user)
    print(attributes)
    print(pgtiou)

    if not user:
        return 'cant verify'
    
    else: 
        session['username'] = user
        print ("succ")
        return redirect(next)





# def login():
#     if 'username' in session:
#         # Already logged in
#         return redirect(url_for('profile'))

#     next = request.args.get('next')
#     ticket = request.args.get('ticket')
#     if not ticket:
#         # No ticket, the request come from end user, send to CAS login
#         cas_login_url = cas_client.get_login_url()
#         app.logger.debug('CAS login URL: %s', cas_login_url)
#         return redirect(cas_login_url)

#     # There is a ticket, the request come from CAS as callback.
#     # need call `verify_ticket()` to validate ticket and get user profile.
#     app.logger.debug('ticket: %s', ticket)
#     app.logger.debug('next: %s', next)

#     user, attributes, pgtiou = cas_client.verify_ticket(ticket)

#     app.logger.debug(
#         'CAS verify ticket response: user: %s, attributes: %s, pgtiou: %s', user, attributes, pgtiou)

#     if not user:
#         return 'Failed to verify ticket. <a href="/login">Login</a>'
#     else:  # Login successfully, redirect according `next` query parameter.
#         session['username'] = user
#         return redirect(next)