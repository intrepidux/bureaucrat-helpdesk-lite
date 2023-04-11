# Changelog

## Release 12.0.1.0.0 (2023-Apr-11 07:25:01)

### Added addons:

- bureaucrat_knowledge (12.0.0.33.0)
- bureaucrat_knowledge_website (12.0.0.14.0)
- generic_system_event (12.0.0.23.0)

### Updated addons:

- bureaucrat_helpdesk_lite (12.0.1.5.0 -> 12.0.1.6.0)
- crnd_service_desk (12.0.1.4.0 -> 12.0.1.5.0)
- crnd_wsd (12.0.1.94.0 -> 12.0.1.104.0)
- generic_request (12.0.1.181.0 -> 12.0.3.8.0)

### Notable changes:

#### bureaucrat_helpdesk_lite
##### Version 1.6.0

Now the bundle additionally includes `bureaucrat_knowledge` and `generic_service`


#### crnd_wsd
##### Version 1.102.0

Added response attachments on request form


##### Version 1.100.0

Remove resolution checking of request upload image


##### Version 1.98.0

Module `crnd_wsd_subrequest` was merged into the `crnd_wsd`


##### Version 1.97.0

Module `crnd_wsd_priority` was merged into the `crnd_wsd`


##### Version 1.96.0

***BUG220963***
Fix bug when request assigned on inactive channels


#### generic_request
##### Version 3.3.0

Add response attachment files when closing requests.


##### Version 3.0.0

- Merged services into the core
- Services in requests are now optional and could be enabled/disabled in settings.


##### Version 2.19.0

- Added ability to search timesheet reports by:
  - Request Stage Type
  - Request Channel
  - Request Partner
  - Activity
- Added new filters to timesheet reports:
  - Request Closed
  - Request Open
- Added ability to group timesheet reports by:
  - Request Stage Type
  - Request Stage
  - Request Channel


##### Version 2.14.0

- Added filter "Closed Today"


##### Version 2.12.0

***BUG220980***
- Fixed incorrect behavior of filters related to time


##### Version 2.10.0

Added new `company_id` field to request.
Currently, no access rules added for this field,
but this change will be starting point for
introducing multi-company support for requests.

The provided migration will automatically to automatically set company_id
based on following rules:
1. Try to get company for request's website
2. If not found get company from user who created the request.

If `company_id` field was added to request by other third-party module,
then it will not be changed.


##### Version 2.6.0

Added functionality that allows you to configure the automatic removal from the followers at the request of a previosly assigned user.
(Request FR2211959)


##### Version 2.5.0

Fixed bug with incorrect handling of record-created event actions.


##### Version 2.4.0

Added support for saving positions in diagram view


##### Version 2.3.0

***BUG220963***
Fix bug when request assigned on inactive channels


##### Version 2.2.0

- Change default order of requests:
    - Before, requests were ordered only by `date_created DESC`
    - After, requests will be ordered by `priority DESC, date_created DESC`
    - This, fixes regression introduces in 1.30.0 version (when priorities were merged to the core)
- Improve UI, selection of related types and services on category form now moved to separate pages.
  This way, it is much easier to configure systems with large amount of services and categories.


##### Version 2.0.0

Start using Generic System Events under the hood.

**Do not forget to take backup before updating.**


##### Version 1.187.0

Changed access restrictions.
Now in order to have access to Assign/Reassign and Change Parent Request the user must belong to `Request User` group.


##### Version 1.186.0

Added tracking visibility when changing `deadline` field


##### Version 1.185.0

Added new *Internal Notes* page on request form.
There team can add some internal notes related to request,
that will not be displayed on website for customer and
that will not be forgotten in chat history.


##### Version 1.182.0

New request event categories:
- *Deadline Tomorrow*
- *Deadline Today*
- *Deadline Overdue*



