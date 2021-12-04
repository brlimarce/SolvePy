'''
** data
| This is a helper file that contains
| the data for the subpages.
'''

'''
** Navigation Bar
| Key: First letter of the page
| Values: Name and route of the page
'''
pages = {
    'q' : {
        'name' : 'QSI',
        'route' : '/solve/qsi'
    },

    's' : {
        'name' : 'Simplex',
        'route' : '/solve/simplex'
    },

    'a' : {
        'name' : 'About',
        'route' : '/about'
    }
}

'''
** Tabs for QSI
| Pairs: Name, header, and body of each tab
'''
qsi_tabs = [
    # Tutorial
    { 
        'name' : 'tutorial',
        'header' : 'How do I use this solver? 🤔',
        'body' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ultrices et ipsum tellus. Sit mattis sem ac aliquet aenean amet nibh. Turpis eget lorem sem leo suscipit netus faucibus sed. Consectetur velit dolor sed sed. Ipsum enim laoreet odio accumsan nulla. Quam eget lorem magna id arcu. Ultricies odio feugiat semper purus sem sit magna sed gravida.'
    },

    # Input
    {
        'name' : 'input',
        'header' : 'What should I input? ⚙️',
        'body' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ultrices et ipsum tellus. Sit mattis sem ac aliquet aenean amet nibh. Turpis eget lorem sem leo suscipit netus faucibus sed. Consectetur velit dolor sed sed. Ipsum enim laoreet odio accumsan nulla. Quam eget lorem magna id arcu. Ultricies odio feugiat semper purus sem sit magna sed gravida.'
    },

    # Output
    {
        'name' : 'output',
        'header' : 'What should I receive? ✨',
        'body' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ultrices et ipsum tellus. Sit mattis sem ac aliquet aenean amet nibh. Turpis eget lorem sem leo suscipit netus faucibus sed. Consectetur velit dolor sed sed. Ipsum enim laoreet odio accumsan nulla. Quam eget lorem magna id arcu. Ultricies odio feugiat semper purus sem sit magna sed gravida.'
    }
]

'''
** Tabs for Simplex
| Pairs: Name, header, and body of each tab
'''
simplex_tabs = [
    # Tutorial
    { 
        'name' : 'tutorial',
        'header' : 'How do I use this solver? 🤔',
        'body' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ultrices et ipsum tellus. Sit mattis sem ac aliquet aenean amet nibh. Turpis eget lorem sem leo suscipit netus faucibus sed. Consectetur velit dolor sed sed. Ipsum enim laoreet odio accumsan nulla. Quam eget lorem magna id arcu. Ultricies odio feugiat semper purus sem sit magna sed gravida.'
    },

    # Problem
    {
        'name' : 'problem',
        'header' : 'What should I input? ⚙️',
        'body' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ultrices et ipsum tellus. Sit mattis sem ac aliquet aenean amet nibh. Turpis eget lorem sem leo suscipit netus faucibus sed. Consectetur velit dolor sed sed. Ipsum enim laoreet odio accumsan nulla. Quam eget lorem magna id arcu. Ultricies odio feugiat semper purus sem sit magna sed gravida.'
    },

    # Legend
    {
        'name' : 'legend',
        'header' : 'What should I receive? ✨',
        'body' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ultrices et ipsum tellus. Sit mattis sem ac aliquet aenean amet nibh. Turpis eget lorem sem leo suscipit netus faucibus sed. Consectetur velit dolor sed sed. Ipsum enim laoreet odio accumsan nulla. Quam eget lorem magna id arcu. Ultricies odio feugiat semper purus sem sit magna sed gravida.'
    }
]

'''
** Tabs for About
| Pairs: Name, header, and body of each tab
'''
about_tabs = [
    # Ideation
    { 
        'name' : 'ideation',
        'header' : 'How do I use this solver? 🤔',
        'body' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ultrices et ipsum tellus. Sit mattis sem ac aliquet aenean amet nibh. Turpis eget lorem sem leo suscipit netus faucibus sed. Consectetur velit dolor sed sed. Ipsum enim laoreet odio accumsan nulla. Quam eget lorem magna id arcu. Ultricies odio feugiat semper purus sem sit magna sed gravida.'
    },

    # Design
    {
        'name' : 'design',
        'header' : 'What should I input? ⚙️',
        'body' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ultrices et ipsum tellus. Sit mattis sem ac aliquet aenean amet nibh. Turpis eget lorem sem leo suscipit netus faucibus sed. Consectetur velit dolor sed sed. Ipsum enim laoreet odio accumsan nulla. Quam eget lorem magna id arcu. Ultricies odio feugiat semper purus sem sit magna sed gravida.'
    },

    # Development
    {
        'name' : 'development',
        'header' : 'What should I receive? ✨',
        'body' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ultrices et ipsum tellus. Sit mattis sem ac aliquet aenean amet nibh. Turpis eget lorem sem leo suscipit netus faucibus sed. Consectetur velit dolor sed sed. Ipsum enim laoreet odio accumsan nulla. Quam eget lorem magna id arcu. Ultricies odio feugiat semper purus sem sit magna sed gravida.'
    }
]

'''
** Tabs for About (Data)
| Pairs: Header and body of each card
'''
about_data = [
    {
        'header': 'About Me',
        'body' : 'Some quick example text to build on the card title and make up the bulk of the cards content.'
    },

    {
        'header': 'Technologies Used',
        'body' : 'Some quick example text to build on the card title and make up the bulk of the cards content.'
    },

    {
        'header': 'Dedication',
        'body' : 'Some quick example text to build on the card title and make up the bulk of the cards content.'
    }
]

'''
** Plants
| Key: Shortcut name of the plant
| Value: Full name of the place
'''
plants = [
    # Denver
    {
        'keyword' : 'DEN',
        'name' : 'Denver'
    },

    # Phoenix
    {
        'keyword' : 'PHO',
        'name' : 'Phoenix'
    },

    # Dallas
    {
        'keyword' : 'DAL',
        'name' : 'Dallas'
    }
]

'''
** Warehouses
| Key: Shortcut name of the warehouse
| Value: Full name of the place
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
| Key: Keyword for the option
| Value: Full name of the place
'''
simplex_options = {
    'tableau' : 'Display Initial Tableau',
    'shipped' : 'Get Number of Shipped Items'
}