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
        'subheader' : 'Generic Solver'
    },

    'simplex' : {
        'name' : 'Simplex',
        'route' : '/solve/simplex',
        'subheader' : 'Generic Solver'
    },

    'problem' : {
        'name' : 'Problem',
        'route' : '/solve/simplex/problem',
        'subheader' : 'Problem-Specific Solver'
    },

    'about' : {
        'name' : 'About',
        'route' : '/about',
        'subheader' : 'About the App'
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
        'body' :
            '''
            This is a generic solver for <span class="text-primary">Quadratic Spline Interpolation (QSI).</span> Browse the succeeding tabs to check out the input and output of this web page. For other solvers, check out the <span class="text-primary">navigation bar</span> above.
            '''
    },

    # ** Input
    {
        'name' : 'input',
        'header' : 'Input ⚙️',
        'body' : 
            '''
            <ul class="list-group">
                <!-- Description -->
                <span class="mb-3">Below is a guide on how you should input your values.</span>

                <!-- X Values -->
                <li class="list-group-item">
                    <span class="fw-bold text-primary">X Values -</span> This serves as your <span class="text-secondary">independent vector.</span> Enter multiple numbers <span class="text-secondary">(size ≥ 1)</span>, which are separated by commas.
                </li>

                <!-- Y Values -->
                <li class="list-group-item">
                    <span class="fw-bold text-primary">Y Values -</span> This serves as your <span class="text-secondary">dependent vector.</span> Enter multiple numbers <span class="text-secondary">(size ≥ 1)</span>, which are separated by commas.
                </li>

                <!-- Value -->
                <li class="list-group-item">
                    <span class="fw-bold text-primary">Value -</span> This serves as your <span class="text-secondary">x value</span> or the single number to be evaluated by an interpolating polynomial.
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
            <ul class="list-group">
                <!-- Description -->
                <span class="mb-3">Below is a guide on what you'll be receiving as outputs.</span>

                <!-- Polynomials -->
                <li class="list-group-item">
                    <span class="fw-bold text-primary">Interpolating Polynomials -</span> This displays a table consisting of interpolating polynomials <span class="text-secondary">(Polynomial)</span> along with their respective intervals <span class="text-secondary">(Interval)</span>.
                </li>

                <!-- Approximate -->
                <li class="list-group-item">
                    <span class="fw-bold text-primary">Approximate -</span> This is the result of x when substituted in the appropriate interpolating polynomial. This displays a table, which contains the interval (covering x) <span class="text-secondary">(Interval)</span>, its respective polynomial <span class="text-secondary">(Polynomial)</span>, and y <span class="text-secondary">(Approximate Value)</span>.
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
        'body' :
            '''
            This is a generic solver for <span class="text-primary">Simplex Method.</span> Browse the succeeding tabs to check out the input and output of this web page. For other solvers, check out the <span class="text-primary">navigation bar</span> above.
            '''
    },

    # ** Input
    {
        'name' : 'input',
        'header' : 'Input ⚙️',
        'body' : 
            '''
            To get the desired result, you should follow the input's format. Below is a guide for your reference.
            <ul class="list-group mt-4">
                <!-- Constraints -->
                <li class="list-group-item">
                    <span class="fw-bold text-primary">Constraints -</span> This serves as the <span class="text-secondary">size of your constraints.</span> Enter a <span class="text-secondary">single number</span> as the size of your constraints.
                </li>

                <!-- Variables -->
                <li class="list-group-item">
                    <span class="fw-bold text-primary">Variables -</span> This serves as the <span class="text-secondary">size of your variables.</span> Enter a <span class="text-secondary">single number</span> as the size of your variables.
                </li>

                <!-- Initial Tableau -->
                <li class="list-group-item">
                    <span class="fw-bold text-primary">Initial Tableau -</span> This serves as the <span class="text-secondary">initial tableau.</span> The <span class="text-secondary">rows</span> of the tableau should be separated by a <span class="text-secondary">new line.</span> In each row, the numbers are separated by <span class="text-secondary">commas.</span>
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
                <!-- Optimal Value -->
                <li class="list-group-item">
                    <span class="fw-bold text-primary">Optimal Value -</span> This displays the <span class="text-secondary"> maximized or minimized optimal value based on the initial tableau.
                </li>

                <!-- Final Tableau -->
                <li class="list-group-item">
                    <span class="fw-bold text-primary">Final Tableau -</span> This serves as the final tableau after performing Simplex method. The <span class="text-secondary">basic solution</span> can also be found here.
                </li>

                <!-- Basic Solution -->
                <li class="list-group-item">
                    <span class="fw-bold text-primary">Basic Solution -</span> This serves as the <span class="text-secondary">last basic solution</span> based on the final tableau.
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
        'body' :
            '''
            This is the problem-specific solver for <span class="text-primary">Simplex Method.</span> Browse the succeeding tabs to check out the input and output of this web page. For other solvers, check out the <span class="text-primary">navigation bar</span> above.
            '''
    },

    # ** Problem
    {
        'name' : 'legend',
        'header' : 'Legend 🚢',
        'body' :
            '''
            Below is a guide for the acronyms of the plants and warehouses in the problem.

            <!-- Plants -->
            <table class="table text-center table-borderless table-striped">
                <thead>
                    <tr>
                        <th scope="col" class="text-primary"></th>
                        <th scope="col" class="text-primary">DEN</th>
                        <th scope="col" class="text-primary">PHO</th>
                        <th scope="col" class="text-primary">DAL</th>
                    </tr>
                </thead>

                <tbody>
                    <tr>
                        <td class="text-secondary">Plant</td>
                        <td>Denver, Colorado</td>
                        <td>Phoenix, Arizona</td>
                        <td>Dallas, Texas</td>
                    </tr>
                </tbody>
            </table>

            <!-- Warehouses -->
            <table class="table text-center table-borderless table-striped">
                <thead>
                    <tr>
                        <th scope="col" class="text-primary"></th>
                        <th scope="col" class="text-primary">SAC</th>
                        <th scope="col" class="text-primary">SL</th>
                        <th scope="col" class="text-primary">ALB</th>
                        <th scope="col" class="text-primary">CHI</th>
                        <th scope="col" class="text-primary">NYC</th>
                    </tr>
                </thead>

                <tbody>
                    <tr>
                        <td class="text-secondary">Warehouse</td>
                        <td>Sacramento, California</td>
                        <td>Salt Lake City, Utah</td>
                        <td>Albuquerque, New Mexico</td>
                        <td>Chicago, Illinois</td>
                        <td>New York City, New York</td>
                    </tr>
                </tbody>
            </table>
            '''
    },

    # ** Variables
    {
        'name' : 'variables',
        'header' : 'Variables 🗺️',
        'body' :
            '''
            <span class="text-primary">Z</span> represents the <span class="text-secondary">maximized/minimized</span> cost. On the other hand, the variables represent the <span class="text-secondary">number of shipped items</span> from a plant to a warehouse.

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
        'body' : 
            '''
            I wanted to explore more technologies other than R. Thus, I've resorted to Python as well as a framework that is fitting to this PL. At the same time, it is easy and convenient to learn and use. I strived to integrate creativity and functionality into this app.
            '''
    },

    # ** Design
    {
        'name' : 'design',
        'header' : 'How did I design this? 🎨',
        'body' :
            '''
            Due to time constraints, I've resorted to using <span class="text-secondary">Bootstrap</span> as my frontend library. Other than that, Bootstrap has the necessary components to provide a professional vibe to the app's interface. I've experimented with different themes and components to put both solves together in an interactive way.
            '''
    },

    # ** Development
    {
        'name' : 'development',
        'header' : 'How did I develop this? 💻',
        'body' : 
            '''
            All exercises in R were converted into Python. They served as modules in the form of external Python files. For the web pages, they were through templates, which served as their structure and design. The templates and modules can be directly connected to each other.
            '''
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
        'body' : 
            '''
            Hi! I'm <span class="text-primary">Bia!</span> I love <span class="text-secondary">design</span>, which makes UI/UX as one of my primary interests. Other than that, I love software development; my favorite PL is <span class="text-secondary">C#</span>. I visualize a future where things function creatively. This is not only limited in the visual aspect but also in the innovation part.
            '''
    },

    # ** Technologies Used
    {
        'icon' : 'technology.svg',
        'header': 'Technologies Used',
        'body' :
            '''
            For <span class="text-primary">frontend development,</span> I've utilized <span class="text-secondary">Bootstrap 5</span> to translate the mockups from Figma into HTML code. <br /> <br />
            
            For <span class="text-primary">backend development,</span> however, I've used <span class="text-secondary">Python</span> and <span class="text-secondary">Flask</span> for the scripts and integration, respectively. I've also used other libraries such as WTForms. <br />
            '''
    },

    # ** Dedication
    {
        'icon' : 'dedication.svg',
        'header': 'Dedication',
        'body' :
            '''
            To <span class="text-primary">Sir Lei,</span> <br />
            Thank you for the learnings in 150. I've been challenged with these exercises, and I was able to improve and hone my programming skills. <br /> <br />

            To <span class="text-primary">Junel,</span> <br />
            Thanks. I owe you one, bro.
            '''
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