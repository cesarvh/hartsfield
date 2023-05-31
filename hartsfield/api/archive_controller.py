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

@app.route('/api/archives')
def retrieve_archives():
    # Returns the available archives of the currently-logged in user
    res = {
        "archiveList": {
            "uid": "1",
            "pageNum": "0",
            "pageSize": "20",
            "itemsInPage": "20",
            "totalItems": "3",
            "listItem": [
                {
                    "archiveID": "679c4d8b-1a97-4b18-a1ad",
                    "archiveFileName": "bigdata_101.tgz", 
                    "createdAt": "2015-12-01T21:20:00.000Z",
                    "sizeBytes": "30345"
                }, 
                {
                    "archiveId": "7ae3a5b0-7774-4052-8f3d", 
                    "archiveFileName": "bigdata_201.tgz",
                    "createdAt": "2015-12-01T21:20:00.000Z",
                    "sizeBytes": "12356"
                }, 
                {
                    "archiveId": "28c27b2d-b439-4617-a07a", 
                    "archiveFileName": "bigdata_301.tgz",
                    "createdAt": "2015-12-01T21:20:00.000Z", 
                    "sizeBytes": "54329"
                }
            ]
        }
    }

    return res