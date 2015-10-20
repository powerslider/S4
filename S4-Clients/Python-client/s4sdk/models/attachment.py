# Copyright 2014, Ontotext AD

# This file is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
# You should have received a copy of the GNU Lesser General Public License
# along with this library; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA


class Attachment:
    def __init__(self):
        self.swaggerTypes = {
            'headers': 'javax.ws.rs.core.MultivaluedMap<java.lang.String, ' +
            'java.lang.String>',
            'object': 'Object',
            'content_type': 'MediaType',
            'data_handler': 'DataHandler',
            'content_id': 'str',
            'content_disposition': 'ContentDisposition'
        }

        self.headers = None
        self.object = None  # Object
        self.content_type = None  # MediaType
        self.data_handler = None  # DataHandler
        self.content_id = None  # str
        self.content_disposition = None  # ContentDisposition
