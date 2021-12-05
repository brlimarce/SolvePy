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
** returns
| - key: Contain the page keyword.
| - name: Contain the display name in the navbar.
| - route: Contain the link of the page.
| - subheader: Contain the card header in home.
| - description: Contain the card description in home.
'''
pages = {
    'qsi' : {
        'name' : 'QSI',
        'route' : '/solve/qsi',
        'subheader' : 'Generic Solver',
        'description' : 'Loren ipsum'
    },

    'simplex' : {
        'name' : 'Simplex',
        'route' : '/solve/simplex',
        'subheader' : 'Generic Solver',
        'description' : 'Loren ipsum'
    },

    'about' : {
        'name' : 'About',
        'route' : '/about',
        'subheader' : 'About the App',
        'description' : 'Loren ipsum'
    }
}



'''
** QSI Tabs
| This contains the tab information in
| the qsi page.
- - -
** returns
| - name: Contain the name of the tab.
| - header: Contain the tab header.
| - body: Contain the tab's content.
'''
tabs_qsi = [
    # ** Tutorial
    { 
        'name' : 'tutorial',
        'header' : 'How do I use this solver? 🤔',
        'body' : 'Place the description here.'
    },

    # ** Input
    {
        'name' : 'input',
        'header' : 'What should I input? ⚙️',
        'body' : 'Place a description here.'
    },

    # ** Output
    {
        'name' : 'output',
        'header' : 'What should the outcome be? ✨',
        'body' : 'Place a description here.'
    }
]

'''
** Simplex Tabs
| This contains the tab information in
| the simplex page.
- - -
** returns
| - name: Contain the name of the tab.
| - header: Contain the tab header.
| - body: Contain the tab's content.
'''
tabs_simplex = [
    # ** Tutorial
    { 
        'name' : 'tutorial',
        'header' : 'How do I use this solver? 🤔',
        'body' : 'Place a description here.'
    },

    # ** Problem
    {
        'name' : 'problem',
        'header' : 'What is the context of this solver? 🚢',
        'body' : 'Place a description here.'
    },

    # ** Legend
    {
        'name' : 'legend',
        'header' : 'How should I be guided? 🗺️',
        'body' : 'Place a description here.'
    }
]

'''
** About Tabs
| This contains the tab information in
| the about page.
- - -
** returns
| - name: Contain the name of the tab.
| - header: Contain the tab header.
| - body: Contain the tab's content.
'''
tabs_about = [
    # ** Ideation
    { 
        'name' : 'ideation',
        'header' : 'Where did this idea come from? 💡',
        'body' : 'Place a description here.'
    },

    # ** Design
    {
        'name' : 'design',
        'header' : 'How did I design this? 🎨',
        'body' : 'Place a description here.'
    },

    # ** Development
    {
        'name' : 'development',
        'header' : 'How did I develop this? 💻',
        'body' : 'Place a description here.'
    }
]

'''
** Profile Information
| This contains the information in
| the cards of the about page.
- - -
** returns
| - header: Contain the card's header.
| - body: Contain the card's content.
'''
profile = [
    # ** About Me
    {
        'header': 'About Me 🥺',
        'body' : 'Place a description here.'
    },

    # ** Technologies Used
    {
        'header': 'Technologies Used 🐱‍💻',
        'body' : 'Place a description here.'
    },

    # ** Dedication
    {
        'header': 'Dedication ❤️',
        'body' : 'Place a description here.'
    }
]

'''
** Plants
| This contains information about the
| plants in the problem.
- - -
** returns
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
** returns
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
** returns
| - key: Contain the option's keyword.
| - value: Contain the option's description.
'''
simplex_options = {
    'tableau' : 'Display Initial Tableau',
    'shipped' : 'Get Number of Shipped Items'
}