'''
** data
| This is a helper file that contains
| the data for the subpages.
'''

'''
** Navigation Bar
| This contains the information regarding
| the pages of the navigation bar.
- - -
| - key: Contain the page keyword.
| - name: Contain the display name in the navbar.
| - route: Contain the link of the page.
'''
pages = {
    'qsi' : {
        'name' : 'QSI',
        'route' : '/solve/qsi'
    },

    'simplex' : {
        'name' : 'Simplex',
        'route' : '/solve/simplex'
    },

    'about' : {
        'name' : 'About',
        'route' : '/about'
    }
}

'''
** QSI Tabs
| This contains the tab information in
| the qsi page.
- - -
| - name: Contain the name of the tab.
| - header: Contain the tab header.
| - body: Contain the tab's content.
'''
tabs_qsi = [
    # ** Tutorial
    { 
        'name' : 'tutorial',
        'header' : 'How do I use this solver? 🤔',
        'body' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ultrices et ipsum tellus. Sit mattis sem ac aliquet aenean amet nibh. Turpis eget lorem sem leo suscipit netus faucibus sed. Consectetur velit dolor sed sed. Ipsum enim laoreet odio accumsan nulla. Quam eget lorem magna id arcu. Ultricies odio feugiat semper purus sem sit magna sed gravida.'
    },

    # ** Input
    {
        'name' : 'input',
        'header' : 'What should I input? ⚙️',
        'body' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ultrices et ipsum tellus. Sit mattis sem ac aliquet aenean amet nibh. Turpis eget lorem sem leo suscipit netus faucibus sed. Consectetur velit dolor sed sed. Ipsum enim laoreet odio accumsan nulla. Quam eget lorem magna id arcu. Ultricies odio feugiat semper purus sem sit magna sed gravida.'
    },

    # ** Output
    {
        'name' : 'output',
        'header' : 'What should I receive? ✨',
        'body' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ultrices et ipsum tellus. Sit mattis sem ac aliquet aenean amet nibh. Turpis eget lorem sem leo suscipit netus faucibus sed. Consectetur velit dolor sed sed. Ipsum enim laoreet odio accumsan nulla. Quam eget lorem magna id arcu. Ultricies odio feugiat semper purus sem sit magna sed gravida.'
    }
]

'''
** Simplex Tabs
| This contains the tab information in
| the simplex page.
- - -
| - name: Contain the name of the tab.
| - header: Contain the tab header.
| - body: Contain the tab's content.
'''
tabs_simplex = [
    # ** Tutorial
    { 
        'name' : 'tutorial',
        'header' : 'How do I use this solver? 🤔',
        'body' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ultrices et ipsum tellus. Sit mattis sem ac aliquet aenean amet nibh. Turpis eget lorem sem leo suscipit netus faucibus sed. Consectetur velit dolor sed sed. Ipsum enim laoreet odio accumsan nulla. Quam eget lorem magna id arcu. Ultricies odio feugiat semper purus sem sit magna sed gravida.'
    },

    # ** Problem
    {
        'name' : 'problem',
        'header' : 'What should I input? ⚙️',
        'body' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ultrices et ipsum tellus. Sit mattis sem ac aliquet aenean amet nibh. Turpis eget lorem sem leo suscipit netus faucibus sed. Consectetur velit dolor sed sed. Ipsum enim laoreet odio accumsan nulla. Quam eget lorem magna id arcu. Ultricies odio feugiat semper purus sem sit magna sed gravida.'
    },

    # ** Legend
    {
        'name' : 'legend',
        'header' : 'What should I receive? ✨',
        'body' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ultrices et ipsum tellus. Sit mattis sem ac aliquet aenean amet nibh. Turpis eget lorem sem leo suscipit netus faucibus sed. Consectetur velit dolor sed sed. Ipsum enim laoreet odio accumsan nulla. Quam eget lorem magna id arcu. Ultricies odio feugiat semper purus sem sit magna sed gravida.'
    }
]

'''
** About Tabs
| This contains the tab information in
| the about page.
- - -
| - name: Contain the name of the tab.
| - header: Contain the tab header.
| - body: Contain the tab's content.
'''
tabs_about = [
    # ** Ideation
    { 
        'name' : 'ideation',
        'header' : 'How do I use this solver? 🤔',
        'body' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ultrices et ipsum tellus. Sit mattis sem ac aliquet aenean amet nibh. Turpis eget lorem sem leo suscipit netus faucibus sed. Consectetur velit dolor sed sed. Ipsum enim laoreet odio accumsan nulla. Quam eget lorem magna id arcu. Ultricies odio feugiat semper purus sem sit magna sed gravida.'
    },

    # ** Design
    {
        'name' : 'design',
        'header' : 'What should I input? ⚙️',
        'body' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ultrices et ipsum tellus. Sit mattis sem ac aliquet aenean amet nibh. Turpis eget lorem sem leo suscipit netus faucibus sed. Consectetur velit dolor sed sed. Ipsum enim laoreet odio accumsan nulla. Quam eget lorem magna id arcu. Ultricies odio feugiat semper purus sem sit magna sed gravida.'
    },

    # ** Development
    {
        'name' : 'development',
        'header' : 'What should I receive? ✨',
        'body' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ultrices et ipsum tellus. Sit mattis sem ac aliquet aenean amet nibh. Turpis eget lorem sem leo suscipit netus faucibus sed. Consectetur velit dolor sed sed. Ipsum enim laoreet odio accumsan nulla. Quam eget lorem magna id arcu. Ultricies odio feugiat semper purus sem sit magna sed gravida.'
    }
]

'''
** Profile Information
| This contains the information in
| the cards of the about page.
- - -
| - header: Contain the card's header.
| - body: Contain the card's content.
'''
profile = [
    # ** About Me
    {
        'header': 'About Me',
        'body' : 'Some quick example text to build on the card title and make up the bulk of the cards content.'
    },

    # ** Technologies Used
    {
        'header': 'Technologies Used',
        'body' : 'Some quick example text to build on the card title and make up the bulk of the cards content.'
    },

    # ** Dedication
    {
        'header': 'Dedication',
        'body' : 'Some quick example text to build on the card title and make up the bulk of the cards content.'
    }
]

'''
** Plants
| This contains information about the
| plants in the problem.
- - -
| - keyword: Contain the plant's acronym/keyword.
| - name: Contain the plant's city name.
'''
plants = [
    # ** Denver, Colorado
    {
        'keyword' : 'DEN',
        'name' : 'Denver'
    },

    # ** Phoenix, Arizona
    {
        'keyword' : 'PHO',
        'name' : 'Phoenix'
    },

    # ** Dallas, Texas
    {
        'keyword' : 'DAL',
        'name' : 'Dallas'
    }
]

'''
** Warehouses
| This contains the information about the
| warehouses in the problem.
- - -
| - key: Contain the warehouse's keyword.
| - value: Contain the warehouse's city name.
'''
warehouses = {
    'SAC' : 'Sacramento',
    'SL' : 'Salt Lake City',
    'ALB' : 'Albuquerque',
    'CHI' : 'Chicago',
    'NYC' : 'New York City'
}

'''
** Options for Simplex
| This contains options in displaying
| specific information in the simplex page.
- - -
| - key: Contain the option's keyword.
| - value: Contain the option's description.
'''
simplex_options = {
    'tableau' : 'Display Initial Tableau',
    'shipped' : 'Get Number of Shipped Items'
}