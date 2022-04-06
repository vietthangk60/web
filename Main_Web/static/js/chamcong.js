setOptions({
        //locale: mobiscroll.localeEn,  // Specify language like: locale: mobiscroll.localePl or omit setting to use default
        theme: 'ios',                 // Specify theme like: theme: 'ios' or omit setting to use default
        themeVariant: 'light'         // More info about themeVariant: https://docs.mobiscroll.com/5-15-1/javascript/eventcalendar#opt-themeVariant
    });
    
    var calendar = eventcalendar('#demo-event-listing', {
        view: {                       // More info about view: https://docs.mobiscroll.com/5-15-1/javascript/eventcalendar#opt-view
            timeline: {
                type: 'week',
                eventList: true
            }
        },
        /*data: [{                      // More info about data: https://docs.mobiscroll.com/5-15-1/javascript/eventcalendar#opt-data
            start: '2022-03-20T00:00',
            end: '2022-03-23T00:00',
            allDay: true,
            title: 'Event 1',
            resource: 1
        }, {
            start: '2022-03-22T09:00',
            end: '2022-03-26T15:00',
            title: 'Event 2',
            resource: 2
        }, {
            start: '2022-03-25T00:00',
            end: '2022-04-01T00:00',
            allDay: true,
            title: 'Event 3',
            resource: 2
        }, {
            start: '2022-03-12T07:00',
            end: '2022-03-17T12:00',
            title: 'Event 4',
            resource: 2
        }, {
            start: '2022-03-29T00:00',
            end: '2022-04-04T00:00',
            allDay: true,
            title: 'Event 5',
            resource: 3
        }, {
            start: '2022-03-22T08:00',
            end: '2022-03-24T20:00',
            title: 'Event 6',
            resource: 4
        }, {
            start: '2022-03-20T00:00',
            end: '2022-03-23T00:00',
            allDay: true,
            title: 'Event 7',
            resource: 4
        }, {
            start: '2022-03-14T00:00',
            end: '2022-03-19T00:00',
            allDay: true,
            title: 'Event 8',
            resource: 5
        }, {
            start: '2022-03-28T00:00',
            end: '2022-04-05T00:00',
            allDay: true,
            title: 'Event 9',
            resource: 6
        }],*/
        resources: [{                 // More info about resources: https://docs.mobiscroll.com/5-15-1/javascript/eventcalendar#opt-resources
            id: 1,
            name: 'Bùi Ngọc Đăng',
            color: '#e20000'
        }, {
            id: 2,
            name: 'Nguyễn Văn B',
            color: '#60e81a'
        }, {
            id: 3,
            name: 'Nguyễn Văn C',
            color: '#3ba7ff'
        }, {
            id: 4,
            name: 'Nguyễn Văn D',
            color: '#e25dd2'
        }, {
            id: 5,
            name: 'Nguyễn Văn E',
            color: '#f1e920'
        }, {
            id: 6,
            name: 'Nguyễn Văn F',
            color: '#1ac38d'
        }, {
            id: 7,
            name: 'Nguyễn Văn G',
            color: '#60e81a'
        }, {
            id: 8,
            name: 'Nguyễn Văn H',
            color: '#3ba7ff'
        }, {
            id: 9,
            name: 'Nguyễn Văn I',
            color: '#e25dd2'
        }, {
            id: 10,
            name: 'Nguyễn Văn K',
            color: '#f1e920'
        }, {
            id: 11,
            name: 'Nguyễn Văn L',
            color: '#1ac38d'
        }, {
            id: 12,
            name: 'Nguyễn Văn M',
            color: '#60e81a'
        }, {
            id: 13,
            name: 'Nguyễn Văn N',
            color: '#3ba7ff'
        }, {
            id: 14,
            name: 'Nguyễn Văn O',
            color: '#e25dd2'
        }, {
            id: 15,
            name: 'Nguyễn Văn P',
            color: '#f1e920'
        }, {
            id: 16,
            name: 'Nguyễn Văn Q',
            color: '#1ac38d'
        }],
        renderHeader: function () {   // More info about renderHeader: https://docs.mobiscroll.com/5-15-1/javascript/eventcalendar#opt-renderHeader
            return '<div mbsc-calendar-nav class="md-event-listing-nav"></div>' +
                '<div class="md-event-listing-picker">' +
                //'<label>Work week<input mbsc-segmented type="radio" name="view" value="workweek" class="event-listing-view-change"></label>' +
                '<label>Week<input mbsc-segmented type="radio" name="view" value="week" class="event-listing-view-change" checked></label>' +
                '<label>Month<input mbsc-segmented type="radio" name="view" value="month" class="event-listing-view-change" ></label>' +
                '</div>' +
                '<div mbsc-calendar-prev class="md-event-listing-prev"></div>' +
                '<div mbsc-calendar-today class="md-event-listing-today"></div>' +
                '<div mbsc-calendar-next class="md-event-listing-next"></div>';
        }
    });
    
    document.querySelectorAll('.event-listing-view-change').forEach(function (elm) {
        elm.addEventListener('change', function (ev) {
            switch (ev.target.value) {
                case 'workweek':
                    calendar.setOptions({
                        view: {                       // More info about view: https://docs.mobiscroll.com/5-15-1/javascript/eventcalendar#opt-view
                            timeline: {
                                type: 'week',
                                eventList: true,
                                startDay: 1,
                                endDay: 6
                            }
                        }
                    })
                    break;
                case 'week':
                    calendar.setOptions({
                        view: {                       // More info about view: https://docs.mobiscroll.com/5-15-1/javascript/eventcalendar#opt-view
                            timeline: {
                                type: 'week',
                                eventList: true
                            }
                        }
                    })
                    break;
                case 'month':
                    calendar.setOptions({
                        view: {                       // More info about view: https://docs.mobiscroll.com/5-15-1/javascript/eventcalendar#opt-view
                            timeline: {
                                type: 'month',
                                eventList: true
                            }
                        }
                    })
                    break;
            }
        });
    });
    
    mobiscroll.util.http.getJson('https://trial.mobiscroll.com/timeline-events/', function (events) {
        calendar.setEvents(events);
    }, 'jsonp');

    