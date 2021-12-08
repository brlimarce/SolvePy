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
        'description' : 'Get the approximate and interpolating polynomials using QSI.'
    },

    'simplex' : {
        'name' : 'Simplex',
        'route' : '/solve/simplex',
        'subheader' : 'Generic Solver',
        'description' : 'Display a basic shipping log to maximize/minimize the cost using Simplex.'
    },

    'about' : {
        'name' : 'About',
        'route' : '/about',
        'subheader' : 'About the App',
        'description' : 'Know more about the inner workings of SolvePy!'
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
        'header' : 'How to use this solver? 🤔',
        'body' : 'This is a generic solver for Quadratic Spline Interpolation (QSI). Browse the tabs in this card to check the input and output. Click \'Display Output\' to display the outcome from your data. On the other hand, click \'Reset\' to clear the text fields.'
    },

    # ** Input
    {
        'name' : 'input',
        'header' : 'What should the input be? ⚙️',
        'body' : 'X Values and Y Values are vectors for independent and dependent variables, respectively. Both should contain multiple values separated by a comma as well as have equal sizes. On the other hand, value is the x value or the value to be evaluated by a particular function. It should be a single numerical value.'
    },

    # ** Output
    {
        'name' : 'output',
        'header' : 'What should the outcome be? ✨',
        'body' : 'The first output is a table of QSI interpolating polynomials, which contains the polynomial with its respective interval. The other output is the approximate value from the function, which is a row containing the interval, polynomial, and value itself.'
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
        'header' : 'How to use this solver? 🤔',
        'body' : 'This is a generic solver for Simplex method. Browse the tabs in this card to check the problem and legend. Also, this solver sets the type of method to maximization. On the other hand, you are also given options to display the initial tableau or the matrix containing the number of shipped items.'
    },

    # ** Problem
    {
        'name' : 'problem',
        'header' : 'What is the context of this solver? 🚢',
        'body' : 'Dedmond Integrated Valley Operations Company (DIVOC) is a production company for personal protective equipment (PPEs). One of the main products of DIVOC is a full-body PPE for hospitals and/or laboratories. The full-body PPEs are manufactured at three plants (Denver, Colorado; Phoenix, Arizona; and Dallas, Texas) and are then shipped by truck to five distribution warehouses in Sacramento, California; Salt Lake City, Utah; Albuquerque, New Mexico; Chicago, Illinois; and New York City, New York. Because shipping costs are a major expense, management is investigating a way to reduce them. Because of the world-wide pandemic, an estimate has been created as to the total output needed from each manufacturing plant and how each warehouse will require satisfying its customers. The CIO from DIVOC has created a spreadsheet of the shipping costs from each manufacturing plant to each warehouse as a baseline analysis.'
    },

    # ** Legend
    {
        'name' : 'legend',
        'header' : 'How should I be guided? 🗺️',
        'body' : 'x1, to x5 represent the number of shipped items from Denver to SAC, SL, ALB, CHI, and NYC, respectively. x6 to x10 represents the same order but from Phoenix, and x11 to x15 from Dallas to the same warehouses.'
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
        'body' : 'SolvePy came from a friend who suggested Python as a PL. Since we\'re using R for numerical analysis, the thought of Python provided some inspiration to look for a more modern approach. Thus, I have decided to merge HTML, CSS, and Python into one platform.'
    },

    # ** Design
    {
        'name' : 'design',
        'header' : 'How did I design this? 🎨',
        'body' : 'Due to time constraints and learning curve, I\'ve decided to rely on something I\'m comfortable to use, which is Bootstrap. Supposedly, the overall feel of the web app is professional yet easy to follow through the eye.'
    },

    # ** Development
    {
        'name' : 'development',
        'header' : 'How did I develop this? 💻',
        'body' : 'My previous R exercises were converted into Python. All of them serve as modules to be utilized by an external Python file for the app. Other than that, there are templates, which serve as the structure and design of all web pages. These templates are directly connected to the Python modules.'
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
        'icon' : 'about.svg',
        'header': 'About Me',
        'body' : 'Hello, I\'m Bia! I really love designing, which makes UI/UX one of my primary interests. Other than that, I also love software development. I visualize a future where functional things are done creatively not only in the aesthetic but also in innovation.'
    },

    # ** Technologies Used
    {
        'icon' : 'technology.svg',
        'header': 'Technologies Used',
        'body' : 'For frontend, I have used Bootstrap 5 to translate the mockups into HTML code. For backend, however, I have used Python for the scripts. Overall, I have used Flask to integrate Python into the HTML files.'
    },

    # ** Dedication
    {
        'icon' : 'dedication.svg',
        'header': 'Dedication',
        'body' : 'To Sir Lei, thank you for these wonderful learnings. To Junel, thanks a lot. I owe you one.'
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