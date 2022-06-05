# Changelog

## Release (2022-Jun-05 16:08:41)

### Updated addons:

- bureaucrat_helpdesk_lite (14.0.1.4.0 -> 14.0.1.5.0)
- crnd_wsd (14.0.1.73.0 -> 14.0.1.87.0)
- generic_request (14.0.1.133.0 -> 14.0.1.161.0)

### Notable changes:

#### crnd_wsd
##### Version 1.83.0

Added options in settings to choose the redirect way after request created


##### Version 1.78.0

The type of uploaded file, now also validated on backend side.
In order to make file upload restriction work properly on backend side,
now it is recommended to install [python-magic](https://pypi.org/project/python-magic/) python package,
that is used to detect mimetype of uploaded file on backend.
To make it work properly, it is also required to install system dependency libmagic
(to do it on Debian/Ubuntu run ```sudo apt-get install libmagic1```)


##### Version 1.76.0

Added a link to a request on the website to go to this request in the
internal interface for the allowed user group.


#### generic_request
##### Version 1.156.0

Added ability to search requests by following fields:
- author_id.phone
- author_id.mobile
- author_id.name
- partner_id.phone
- partner_id.mobile
- partner_id.name


##### Version 1.153.0

Merge the generic_request_parent as module into the generic_request module


##### Version 1.152.0

Merge the generic_request_reopen_as module into the generic_request module


##### Version 1.151.0

Added ability to specify access groups for request category and request type.
Previously this functionality was available only in crnd_wsd module, but now
it will be available in the core module.


##### Version 1.148.0

Changed status view in requests.
Now there is only the current status of request.


##### Version 1.146.0

Added option in configuration to show/hide searchpanel on requests view


##### Version 1.145.0

Changed 'Automatically create contacts for requests' option in the requests settings:
- now it allows to autocreate contact (if not exist) only for author of incoming message
 
Added options in the requests settings:
- availability to autocreate new contact (if not exist), mentioned in the CC header of incoming mail
- automatically subscribing the contacts, mentioned in the CC header on incoming mail


##### Version 1.142.0

Refactored the UI for changing stages of request and closing request.
Now, instead of changing request stage via statusbar widget in right-top corner of the form,
there will be buttons present in view (left-top corner of ther form) that will be used to move request via route.
Also, the names of that buttons (and their styles) could be configured on route level.
And when the route is closing route, then automatically will be show closing wizard with pre-selected route.
This way, it have to be more user-friendly.


##### Version 1.138.0

Added configuration option, that allows to select preferred view for requests: list or kanban.
Currently this works only for standard menu *Requests*


##### Version 1.137.0

Added *searchpanel* to requests, thus now it is possible to easily filter requests by category, type, service, tags and stage type.



