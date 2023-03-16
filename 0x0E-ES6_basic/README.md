# [ES6 Basics](https://intranet.hbtn.io/projects/577)

<html>
<div class="panel panel-default" id="project-description">
 <div class="panel-body">
  <p>
   <img alt="" loading="lazy" src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2019/12/08806026ef621f900121.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230316%2Feu-west-3%2Fs3%2Faws4_request&amp;X-Amz-Date=20230316T164808Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=2877bdcf029e3534c0a47db2860dbc50c453ae387b96d1bd924fe54567937684" style=""/>
  </p>
  <h2>
   Resources
  </h2>
  <p>
   <strong>
    Read or watch
   </strong>
   :
  </p>
  <ul>
   <li>
    <a href="https://www.w3schools.com/js/js_es6.asp" target="_blank" title="ECMAScript 6 - ECMAScript 2015">
     ECMAScript 6 - ECMAScript 2015
    </a>
   </li>
   <li>
    <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements" target="_blank" title="Statements and declarations">
     Statements and declarations
    </a>
   </li>
   <li>
    <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions" target="_blank" title="Arrow functions">
     Arrow functions
    </a>
   </li>
   <li>
    <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters" target="_blank" title="Default parameters">
     Default parameters
    </a>
   </li>
   <li>
    <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters" target="_blank" title="Rest parameter">
     Rest parameter
    </a>
   </li>
   <li>
    <a href="https://towardsdatascience.com/javascript-es6-iterables-and-iterators-de18b54f4d4?gi=1964f0355e05" target="_blank" title="Javascript ES6 — Iterables and Iterators">
     Javascript ES6 — Iterables and Iterators
    </a>
   </li>
  </ul>
  <h2>
   Learning Objectives
  </h2>
  <p>
   At the end of this project, you are expected to be able to
   <a href="https://fs.blog/feynman-learning-technique/" target="_blank" title="explain to anyone">
    explain to anyone
   </a>
   ,
   <strong>
    without the help of Google
   </strong>
   :
  </p>
  <ul>
   <li>
    What ES6 is
   </li>
   <li>
    New features introduced in ES6
   </li>
   <li>
    The difference between a constant and a variable
   </li>
   <li>
    Block-scoped variables
   </li>
   <li>
    Arrow functions and function parameters default to them
   </li>
   <li>
    Rest and spread function parameters
   </li>
   <li>
    String templating in ES6
   </li>
   <li>
    Object creation and their properties in ES6
   </li>
   <li>
    Iterators and for-of loops
   </li>
  </ul>
  <h2>
   Requirements
  </h2>
  <h3>
   General
  </h3>
  <ul>
   <li>
    All your files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x
   </li>
   <li>
    Allowed editors:
    <code>
     vi
    </code>
    ,
    <code>
     vim
    </code>
    ,
    <code>
     emacs
    </code>
    ,
    <code>
     Visual Studio Code
    </code>
   </li>
   <li>
    All your files should end with a new line
   </li>
   <li>
    A
    <code>
     README.md
    </code>
    file, at the root of the folder of the project, is mandatory
   </li>
   <li>
    Your code should use the
    <code>
     js
    </code>
    extension
   </li>
   <li>
    Your code will be tested using the
    <a href="https://jestjs.io/" target="_blank" title="Jest Testing Framework">
     Jest Testing Framework
    </a>
   </li>
   <li>
    Your code will be analyzed using the linter
    <a href="https://eslint.org/" target="_blank" title="ESLint">
     ESLint
    </a>
    along with specific rules that we’ll provide
   </li>
   <li>
    All of your functions must be exported
   </li>
  </ul>
  <h2>
   Setup
  </h2>
  <h3>
   Install NodeJS 12.11.x
  </h3>
  <p>
   (in your home directory):
  </p>
  <pre><code>curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
</code></pre>
  <pre><code>$ nodejs -v
v12.11.1
$ npm -v
6.11.3
</code></pre>
  <h3>
   Install Jest, Babel, and ESLint
  </h3>
  <p>
   in your project directory:
  </p>
  <ul>
   <li>
    Install Jest using:
    <code>
     npm install --save-dev jest
    </code>
   </li>
   <li>
    Install Babel using:
    <code>
     npm install --save-dev babel-jest @babel/core @babel/preset-env
    </code>
   </li>
   <li>
    Install ESLint using:
    <code>
     npm install --save-dev eslint
    </code>
   </li>
  </ul>
  <h2>
   Configuration files
  </h2>
  <h3>
   <code>
    package.json
   </code>
  </h3>
  <details>
   <summary>
    Click to show/hide file contents
   </summary>
   <pre>
<code>
{
  "scripts": {
    "lint": "./node_modules/.bin/eslint",
    "check-lint": "lint [0-9]*.js",
    "dev": "npx babel-node",
    "test": "jest",
    "full-test": "./node_modules/.bin/eslint [0-9]*.js &amp;&amp; jest"
  },
  "devDependencies": {
    "@babel/core": "^7.6.0",
    "@babel/node": "^7.8.0",
    "@babel/preset-env": "^7.6.0",
    "eslint": "^6.4.0",
    "eslint-config-airbnb-base": "^14.0.0",
    "eslint-plugin-import": "^2.18.2",
    "eslint-plugin-jest": "^22.17.0",
    "jest": "^24.9.0"
  }
}
</code>
</pre>
  </details>
  <h3>
   <code>
    babel.config.js
   </code>
  </h3>
  <details>
   <summary>
    Click to show/hide file contents
   </summary>
   <pre>
<code>
module.exports = {
  presets: [
    [
      '@babel/preset-env',
      {
        targets: {
          node: 'current',
        },
      },
    ],
  ],
};
</code>
</pre>
  </details>
  <h3>
   <code>
    .eslintrc.js
   </code>
  </h3>
  <details>
   <summary>
    Click to show/hide file contents
   </summary>
   <pre>
<code>
module.exports = {
  env: {
    browser: false,
    es6: true,
    jest: true,
  },
  extends: [
    'airbnb-base',
    'plugin:jest/all',
  ],
  globals: {
    Atomics: 'readonly',
    SharedArrayBuffer: 'readonly',
  },
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module',
  },
  plugins: ['jest'],
  rules: {
    'no-console': 'off',
    'no-shadow': 'off',
    'no-restricted-syntax': [
      'error',
      'LabeledStatement',
      'WithStatement',
    ],
  },
  overrides:[
    {
      files: ['*.js'],
      excludedFiles: 'babel.config.js',
    }
  ]
};
</code>
</pre>
  </details>
  <h3>
   Finally…
  </h3>
  <p>
   Don’t forget to run
   <code>
    npm install
   </code>
   from the terminal of your project folder to install all necessary project dependencies.
  </p>
 </div>
</div>

[--LINK PROJECT--](https://intranet.hbtn.io/projects/577)
</html>