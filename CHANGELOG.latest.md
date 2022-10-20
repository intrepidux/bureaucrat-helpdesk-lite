# Changelog

## Release 13.0.0.1.0 (2022-Oct-20 08:23:18)

### Updated addons:

- crnd_wsd (13.0.1.91.0 -> 13.0.1.94.0)
- generic_request (13.0.1.165.0 -> 13.0.1.180.0)

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



