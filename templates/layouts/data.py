u'''
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
        'description' : 'Solve the tableau using Simplx method.'
    },

    'problem' : {
        'name' : 'Problem',
        'route' : '/solve/simplex/problem',
        'subheader' : 'Problem-Specific Solver',
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
        'body' : 'Place a description here.'
    },

    # ** Input
    {
        'name' : 'input',
        'header' : 'Input ⚙️',
        'body' : 
            '''
            To get the desired result, you should follow the input's format. Below is a guide for your reference.
            <ul class="list-group mt-4">
                <!-- X Values -->
                <li class="list-group-item">
                    <span class="fw-bold text-primary">X Values:</span> This is your independent vector. It should contain multiple numbers <span class="fw-bold text-info">(size ≥ 1)</span>, which are separated by commas <span class="fw-bold text-info">( , ).</span>
                </li>

                <!-- Y Values -->
                <li class="list-group-item">
                    <span class="fw-bold text-primary">Y Values:</span> This is your dependent vector. It should contain multiple numbers <span class="fw-bold text-info">(size ≥ 1)</span>, which are separated by commas <span class="fw-bold text-info">( , ).</span>
                </li>

                <!-- Value -->
                <li class="list-group-item">
                    <span class="fw-bold text-primary">Value:</span> This is your x-value, which will be evaluated by the appropriate interpolating polynomial. This should be a single numerical value.
                </li>
            </ul>
            '''
    },

    # ** Output
    {
        'name' : 'output',
        'header' : 'Output ✨',
        'body' :
            '''
            Based on your input, you'll receive its corresponding output. Below is a guide for your reference.
            <ul class="list-group mt-4">
                <!-- Polynomials -->
                <li class="list-group-item">
                    <span class="fw-bold text-primary">Polynomials:</span> This displays a table consisting of interpolating polynomials <span class="fw-bold text-info">(Polynomial)</span> with their respective intervals <span class="fw-bold text-info">(Interval)</span>.
                </li>

                <!-- Approximate -->
                <li class="list-group-item">
                    <span class="fw-bold text-primary">Approximate:</span> This is the result of your x-value when substituted in the appropriate interpolating polynomial. This displays a table, which contains the interval of x <span class="fw-bold text-info">(Interval)</span>, its respective polynomial <span class="fw-bold text-info">(Polynomial)</span>, and the y-value <span class="fw-bold text-info">(Approximate Value)</span>.
                </li>
            </ul>
            '''
    }
]

'''
** Simplex Tabs (Generic)
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
        'body' : 'Place a description here.'
    },

    # ** Input
    {
        'name' : 'input',
        'header' : 'Input ⚙️',
        'body' : 
            '''
            To get the desired result, you should follow the input's format. Below is a guide for your reference.
            <ul class="list-group mt-4">
                <!-- X Values -->
                <li class="list-group-item">
                    <span class="fw-bold text-primary">X Values:</span> This is your independent vector. It should contain multiple numbers <span class="fw-bold text-info">(size ≥ 1)</span>, which are separated by commas <span class="fw-bold text-info">( , ).</span>
                </li>

                <!-- Y Values -->
                <li class="list-group-item">
                    <span class="fw-bold text-primary">Y Values:</span> This is your dependent vector. It should contain multiple numbers <span class="fw-bold text-info">(size ≥ 1)</span>, which are separated by commas <span class="fw-bold text-info">( , ).</span>
                </li>

                <!-- Value -->
                <li class="list-group-item">
                    <span class="fw-bold text-primary">Value:</span> This is your x-value, which will be evaluated by the appropriate interpolating polynomial. This should be a single numerical value.
                </li>
            </ul>
            '''
    },

    # ** Output
    {
        'name' : 'output',
        'header' : 'Output ✨',
        'body' :
            '''
            Based on your input, you'll receive its corresponding output. Below is a guide for your reference.
            <ul class="list-group mt-4">
                <!-- Polynomials -->
                <li class="list-group-item">
                    <span class="fw-bold text-primary">Polynomials:</span> This displays a table consisting of interpolating polynomials <span class="fw-bold text-info">(Polynomial)</span> with their respective intervals <span class="fw-bold text-info">(Interval)</span>.
                </li>

                <!-- Approximate -->
                <li class="list-group-item">
                    <span class="fw-bold text-primary">Approximate:</span> This is the result of your x-value when substituted in the appropriate interpolating polynomial. This displays a table, which contains the interval of x <span class="fw-bold text-info">(Interval)</span>, its respective polynomial <span class="fw-bold text-info">(Polynomial)</span>, and the y-value <span class="fw-bold text-info">(Approximate Value)</span>.
                </li>
            </ul>
            '''
    }
]

'''
** Simplex Tabs (Problem-specific)
| This contains the tab information in
| the simplex page.
- - -
** returns
| - name: Contain the name of the tab.
| - header: Contain the tab header.
| - body: Contain the tab's content.
'''
tabs_problem = [
    # ** Tutorial
    { 
        'name' : 'tutorial',
        'header' : 'How to use this solver? 🤔',
        'body' : 'Place a description here.'
    },

    # ** Problem
    {
        'name' : 'legend',
        'header' : 'Legend 🚢',
        'body' :
            '''
            Below is a guide for the acronyms of the plants and warehouses in the problem.

            <!-- Plants -->
            <h5 class="text-secondary mt-4">Plants 🌱</h5>
            '''
    },

    # ** Variables
    {
        'name' : 'variables',
        'header' : 'Variables 🗺️',
        'body' :
            '''
            <span class="text-primary fw-bold">Z</span> represents the maximized/minimized cost. On the other hand, the variables represent the <span class="text-primary fw-bold">number of shipped items</span> from one plant to one warehouse.

            <!-- Variables (x1 to x5) -->
            <table class="table text-center table-borderless table-striped">
                <thead>
                    <tr>
                        <th scope="col" class="text-primary">x1</th>
                        <th scope="col" class="text-primary">x2</th>
                        <th scope="col" class="text-primary">x3</th>
                        <th scope="col" class="text-primary">x4</th>
                        <th scope="col" class="text-primary">x5</th>
                    </tr>
                </thead>

                <tbody>
                    <tr>
                        <td>DEN to SAC</td>
                        <td>DEN to SL</td>
                        <td>DEN to ALB</td>
                        <td>DEN to CHI</td>
                        <td>DEN to NYC</td>
                    </tr>
                </tbody>
            </table>

            <!-- Variables (x6 to x10) -->
            <table class="table text-center table-borderless table-striped">
                <thead>
                    <tr>
                        <th scope="col" class="text-primary">x6</th>
                        <th scope="col" class="text-primary">x7</th>
                        <th scope="col" class="text-primary">x8</th>
                        <th scope="col" class="text-primary">x9</th>
                        <th scope="col" class="text-primary">x10</th>
                    </tr>
                </thead>

                <tbody>
                    <tr>
                        <td>PHO to SAC</td>
                        <td>PHO to SL</td>
                        <td>PHO to ALB</td>
                        <td>PHO to CHI</td>
                        <td>PHO to NYC</td>
                    </tr>
                </tbody>
            </table>

            <!-- Variables (x11 to x15) -->
            <table class="table text-center table-borderless table-striped">
                <thead>
                    <tr>
                        <th scope="col" class="text-primary">x11</th>
                        <th scope="col" class="text-primary">x12</th>
                        <th scope="col" class="text-primary">x13</th>
                        <th scope="col" class="text-primary">x14</th>
                        <th scope="col" class="text-primary">x15</th>
                    </tr>
                </thead>

                <tbody>
                    <tr>
                        <td>DAL to SAC</td>
                        <td>DAL to SL</td>
                        <td>DAL to ALB</td>
                        <td>DAL to CHI</td>
                        <td>DAL to NYC</td>
                    </tr>
                </tbody>
            </table>
            '''
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
        'body' : '<span class="text-primary fw-bold">SolvePy</span> stemmed'
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