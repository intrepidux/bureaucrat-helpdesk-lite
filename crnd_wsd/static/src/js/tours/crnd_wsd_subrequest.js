odoo.define('crnd_wsd.tour_crnd_wsd_subrequest', function (require) {
    'use strict';

    var base = require('web_editor.base');
    var tour = require('web_tour.tour');

    tour.register('tour_crnd_wsd_subrequest', {
        test: true,
        url: '/requests',
        wait_for: base.ready(),
    }, [
        {
            content: "Search for parent request'",
            trigger: '.wsd_request:has(div:contains("Demo parent request"))'+
                ':contains() .request_top .request-title .request-name',
        },
        {
            content: "Click on 'Subrequests' link",
            trigger: "#request-top-head-actions a[title='Subrequests']",
        },
        {
            content: "Search subrequest",
            trigger: ".wsd_request div:containsExact('Demo subrequest')",
        },
        {
            content: "Link to parent request",
            trigger: ".wsd_request .request_top " +
                ".request-title a.request-parent",
        },
        {
            content: "Check parent request",
            trigger: "#request-body-text-content:contains(" +
                "'Demo parent request')",
        },
    ]);
    return {};
});
