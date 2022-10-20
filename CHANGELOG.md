# Changelog

## Release 15.0.0.1.0 (2022-Oct-20 08:23:32)

### Updated addons:

- crnd_wsd (15.0.1.91.0 -> 15.0.1.94.0)
- generic_request (15.0.1.165.0 -> 15.0.1.180.0)

### Notable changes:

#### crnd_wsd
##### Version 1.94.0

- Added new option that allows to use Shared Link in email.
  This could be useful in case when needed to provide link to request,
  that will not require login from user.
- Refacored settings UI: move website settings to separate section
- *Layout for request creation steps* moved from website settings to request settings


#### generic_request
##### Version 1.178.0

Refactored settings UI: moved mail-related settings to separate section


##### Version 1.173.0

Fixed bug in event notifications, 
that happens when default notification settings set to False
and event messages of subrequest didn't  deliver to parent request.


##### Version 1.171.0

***FR2207947***

Added notifications about subrequest events, 
such as ```created```, ```assigned```, ```closed```, ```reopened```, in parent request.


##### Version 1.170.0

Improved appearance of request tags on kanban view


##### Version 1.167.0

Added settings menu for request mail templates




## Release (2022-Jul-04 19:23:08)

### Updated addons:

- crnd_wsd (15.0.1.87.0 -> 15.0.1.91.0)
- generic_request (15.0.1.161.0 -> 15.0.1.165.0)

### Notable changes:

#### generic_request
##### Version 1.164.1

Added ability to show/hide columns in tree view




## Release (2022-Jun-05 16:15:36)

### Updated addons:

- bureaucrat_helpdesk_lite (14.0.1.5.0 -> 15.0.1.5.0)
- crnd_service_desk (14.0.1.4.0 -> 15.0.1.4.0)
- crnd_wsd (14.0.1.87.0 -> 15.0.1.87.0)
- generic_request (14.0.1.161.0 -> 15.0.1.161.0)


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




## Release (2021-Sep-09 13:27:01)

### Updated addons:

- bureaucrat_helpdesk_lite (14.0.1.3.2 -> 14.0.1.4.0)
- crnd_wsd (14.0.1.68.0 -> 14.0.1.73.0)
- generic_request (14.0.1.123.0 -> 14.0.1.133.0)

### Notable changes:

#### crnd_wsd
##### Version 1.73.0

Added new field Access Groups on the request category / type.
If portal user belongs to one of groups mentioned in this field,
then he will be able to read this category or type.


##### Version 1.71.0

Added new option in settings, that could be used to allow unregistered users
create requests.
The only additional thing that have to be provided by unregistered user is his email and optionaly name.
To enable this option, navigate to *Requests / Configuration / Settings* and
choose *Allow to create request* in field *Website Service Desk (Public Visibility)*.
After this step, unregistered users will be able to create requests from your website


##### Version 1.70.0

Added support for new *tiles* layout for request creation process.

This setting could be enabled in *Website* settings menu
(look for *Bureaucrat Website Settings* section)

When new layout style for request creation process selected, then
Services, categories and types will be displayed as tiles (boxes) instead of
radio buttons.


##### Version 1.69.0

- Added ability to limit maximum size for uploads
- Added ability to limit file types (mime types) allowed for upload
- Improved handling of max request text symbols


#### generic_request
##### Version 1.131.0

- Do not allow to create requests from emails that come from email addresses that are aliases (managed by odoo).
  This is needed to avoid possible infinite loops when two emails start sending autoreplies to each other.
- Starting from this version in *Email* field on request, only email address will be saved.
  The author name will be saved in *Author name* field.
  Previously, author name was saved in *Author name* field, but it also was
  present in *Email* field in format ```Author name <author@email.com>```.


##### Version 1.126.0

Added I (info) button to author, partner, and user fields.
Click on this new button will shoe popover with additional info on partner/user,
that allows to easily and fast copy phone, email, or name of partner/author/user




## Release (2021-Jul-09 15:59:09)

### Updated addons:

- bureaucrat_helpdesk_lite (14.0.1.3.1 -> 14.0.1.3.2)


## Release (2021-Jul-09 15:04:47)

### Updated addons:

- bureaucrat_helpdesk_lite (14.0.1.2.0 -> 14.0.1.3.1)
- crnd_service_desk (14.0.1.3.0 -> 14.0.1.4.0)
- crnd_wsd (14.0.1.62.1 -> 14.0.1.68.0)
- generic_request (14.0.1.114.3 -> 14.0.1.123.0)

### Notable changes:

#### generic_request
##### Version 1.120.0

Show open/closed requests stat for request's partner and author




## Release (2021-May-28 16:08:52)

### Updated addons:

- crnd_wsd (14.0.1.53.0 -> 14.0.1.62.1)
- generic_request (14.0.1.99.0 -> 14.0.1.114.3)

### Notable changes:

#### crnd_wsd
##### Version 1.54.0

- Changeg *UploadFile* icon in text editor.
  Now this button has icon *paperclip* + textual name *Attach file*
- Added configurable helptext, that could be displayed below request text
  on request creation form on website. This text could be configured
  on request type level (see Website Request Text Help field)


#### generic_request
##### Version 1.114.0

- Add new request events (Request Archived / Request Unarchived).
- Add filters in search view.
- Add simplet tests.


##### Version 1.112.0

- Add field `active` to model request.request.
- Add a group whose users are allowed to archive / unarchive requests.


##### Version 1.111.0

#### Version 1.111.0
Added new request event types: 'author-changed' and 'partner-changed'.
 

##### Version 1.103.0

Added global configuration, that allows to chooses if it is needed to suggest
Global CC as recipients of request


##### Version 1.101.0

- Add `email_cc` data to suggested recipients.
- Add global option that allows to automatically create partners,
  if request created from incoming email, and author of email and cc of email
  are not present in odoo's contacts database




## Release (2021-Jan-20 12:24:29)

### Added addons:

- bureaucrat_helpdesk_lite (14.0.1.2.0)
- crnd_service_desk (14.0.1.3.0)
- crnd_wsd (14.0.1.53.0)
- generic_request (14.0.1.99.0)

