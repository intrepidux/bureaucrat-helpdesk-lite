# Changelog

## Release (2022-Jun-05 16:10:13)

### Updated addons:

- bureaucrat_helpdesk_lite (12.0.1.4.0 -> 12.0.1.5.0)
- crnd_wsd (12.0.1.73.0 -> 12.0.1.89.0)
- generic_request (12.0.1.133.0 -> 12.0.1.161.0)

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




## Release (2021-Sep-09 13:23:25)

### Updated addons:

- bureaucrat_helpdesk_lite (12.0.1.3.0 -> 12.0.1.4.0)
- crnd_wsd (12.0.1.68.0 -> 12.0.1.73.0)
- generic_request (12.0.1.123.0 -> 12.0.1.133.0)

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




## Release (2021-Jul-09 15:04:46)

### Updated addons:

- bureaucrat_helpdesk_lite (12.0.1.2.0 -> 12.0.1.3.0)
- crnd_service_desk (12.0.1.3.0 -> 12.0.1.4.0)
- crnd_wsd (12.0.1.62.0 -> 12.0.1.68.0)
- generic_request (12.0.1.114.0 -> 12.0.1.123.0)

### Notable changes:

#### generic_request
##### Version 1.120.0

Show open/closed requests stat for request's partner and author




## Release (2021-May-28 16:02:43)

### Updated addons:

- crnd_wsd (12.0.1.53.0 -> 12.0.1.62.0)
- generic_request (12.0.1.99.0 -> 12.0.1.114.0)

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




## Release (2021-Jan-18 13:28:00)

### Updated addons:

- crnd_wsd (12.0.1.47.0 -> 12.0.1.53.0)
- generic_request (12.0.1.80.1 -> 12.0.1.99.0)

### Notable changes:

#### crnd_wsd
##### Version 1.50.0

Added mult-site support for requests


#### generic_request
##### Version 1.99.0

Add global setting that could be used to show/hide request statistics on kanban views of
request-related objects like Request Category, Request type, etc


##### Version 1.89.0

Now requests created via xml-RPC or json RPC will get *API* channel automatically
(if not provided in creation parameters)


##### Version 1.85.0

- Added new search filters for requests
    - Today
    - 24 hours
    - Week
    - Month
    - Year
- Added new group by filters for request's search view
    - Assignee
    - Is Closed
- Added request statistics (requests open/closed for today, 24h, week, etc) to
  following models:
    - Request Type
    - Request Category
    - Request Channel
    - Request Kind


##### Version 1.84.0

Added *Requests* page to user form view, that is used to display request statistics for user.


##### Version 1.83.0

Added button to generate default stages and route on request type that has no
request stages.


##### Version 1.81.0

Added new request event types:
- Timetracking / Start Work
- Timetracking / Stop Work




## Release (2020-Sep-09 12:08:53)

### Updated addons:

- bureaucrat_helpdesk_lite (12.0.1.1.0 -> 12.0.1.2.0)
- crnd_wsd (12.0.1.41.1 -> 12.0.1.47.0)
- generic_request (12.0.1.62.0 -> 12.0.1.80.1)

### Notable changes:

#### crnd_wsd
##### Version 1.47.0

Automatically set channel to Website for requests created from website


#### generic_request
##### Version 1.72.0

Added new request stage type 'Progress'


##### Version 1.70.0

Added new field Channel to request. The field could be used to determine source of request Website / Web / Mail / Other
Automatically set correct channels for requests created from Web and E-mail


##### Version 1.68.0

Remove obsolete modules from settings page.
Obsolte modules are:
- `generic_request_action_condition`


##### Version 1.67.0

Added *kanban_state* feature to requests.
Now it is possible to define additional Blocked or Ready states on request.
Also, changes of kanban state triggers event *Kanban State*




## Release (2020-Jun-08 19:03:07)

### Updated addons:

- bureaucrat_helpdesk_lite (12.0.1.0.14 -> 12.0.1.1.0)
- crnd_service_desk (12.0.1.2.0 -> 12.0.1.3.0)
- crnd_wsd (12.0.1.26.0 -> 12.0.1.41.1)
- generic_request (12.0.1.40.0 -> 12.0.1.62.0)

### Notable changes:

#### crnd_wsd
##### Version 1.40.0

- Added ability to restrict max text size of request text on website UI and
    make this configurable through global options
- Added visual information about the number of characters entered


##### Version 1.37.0

Merge with crnd_wsd_timesheet addon


##### Version 1.32.0

Use different colors for deadline icon depending on deadline value


##### Version 1.29.0

Improved file uploading from website UI.
- automatically bind uploaded files and images to created request.
- open uploaded files in new tab in browse
- download uploaded documents (instead of displaying them)



##### Version 1.28.0

Show deadline on request page and in request list


#### generic_request
##### Version 1.58.0

Merge with generic_request_timesheet module


##### Version 1.56.0

Enable *create_edit* and *quick_create* features of *author* and *partner*
fields of request 


##### Version 1.54.0

Added ability to assign multiple requests with a single operations.
Just select requests from list view and call context action *Assign*.


##### Version 1.53.0

- Automatically move created stage to the end of list of stages.
  This is required to avoid case when new stage become first one and
  thus it become starting stage for requests.
- Better support for handling mails received from unknown contacts.
  In this case `email_from` will be saved on request
- Save `email_cc` on request (if first email contains `cc`)
- Automatically subscribe partners mentioned in ``CC`` header of incoming mail
- Implement partner suggestions for mailing for requests.
  Odoo will automatically suggest to subscribe partner and / or author of request
  if that is not following request yet


##### Version 1.52.0

Use different colors for deadline icon, depending on its value.


##### Version 1.47.0

Update form view of Request Type


##### Version 1.46.0

Module `generic_request_tag` merged into `generic_request`


##### Version 1.45.0

- Intoruced new field: *Deadline*
- Small improvements to UI
- Fixed regression, missing *Kind* field on request form view


##### Version 1.44.0

Fix regression in detection of author when creator is specified directly,
but author is not specified.


##### Version 1.41.0

Introduced *Request Creation Templates* feature,
that have to be used mostly by other modules to create requests with default values.




## Release (2020-Jan-14 12:09:49)

### Added addons:

- bureaucrat_helpdesk_lite (12.0.1.0.14)
- crnd_service_desk (12.0.1.2.0)
- crnd_wsd (12.0.1.26.0)
- generic_request (12.0.1.40.0)

