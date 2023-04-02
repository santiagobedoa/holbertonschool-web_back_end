# [NodeJS Basics](https://intranet.hbtn.io/projects/615)

<html>
<div class="panel panel-default" id="project-description">
 <div class="panel-body">
  <p>
   <img alt="" loading="lazy" src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/1/82692897e15d9f03256f.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230402%2Feu-west-3%2Fs3%2Faws4_request&amp;X-Amz-Date=20230402T165741Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=6730a28dac68a4b4a4e50f795826d455555e78ebdd71ce3b60635bc232871f6d" style=""/>
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
    <a href="https://nodejs.org/en/docs/guides/getting-started-guide" target="_blank" title="Node JS getting started">
     Node JS getting started
    </a>
   </li>
   <li>
    <a href="https://node.readthedocs.io/en/latest/api/process/" target="_blank" title="Process API doc">
     Process API doc
    </a>
   </li>
   <li>
    <a href="https://nodejs.org/api/child_process.html" target="_blank" title="Child process">
     Child process
    </a>
   </li>
   <li>
    <a href="https://expressjs.com/en/starter/installing.html" target="_blank" title="Express getting started">
     Express getting started
    </a>
   </li>
   <li>
    <a href="https://mochajs.org/" target="_blank" title="Mocha documentation">
     Mocha documentation
    </a>
   </li>
   <li>
    <a href="https://github.com/remy/nodemon#nodemon" target="_blank" title="Nodemon documentation">
     Nodemon documentation
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
    run javascript using NodeJS
   </li>
   <li>
    use NodeJS modules
   </li>
   <li>
    use specific Node JS module to read files
   </li>
   <li>
    use
    <code>
     process
    </code>
    to access command line arguments and the environment
   </li>
   <li>
    create a small HTTP server using Node JS
   </li>
   <li>
    create a small HTTP server using Express JS
   </li>
   <li>
    create advanced routes with Express JS
   </li>
   <li>
    use ES6 with Node JS with Babel-node
   </li>
   <li>
    use Nodemon to develop faster
   </li>
  </ul>
  <h2>
   Requirements
  </h2>
  <ul>
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
    All your files will be interpreted/compiled on Ubuntu 18.04 LTS using
    <code>
     node
    </code>
    (version 12.x.x)
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
    Your code will be tested using
    <code>
     Jest
    </code>
    and the command
    <code>
     npm run test
    </code>
   </li>
   <li>
    Your code will be verified against lint using ESLint
   </li>
   <li>
    Your code needs to pass all the tests and lint. You can verify the entire project running
    <code>
     npm run full-test
    </code>
   </li>
   <li>
    All of your functions/classes must be exported by using this format:
    <code>
     module.exports = myFunction;
    </code>
   </li>
  </ul>
  <h2>
   Provided files
  </h2>
  <h3>
   <code>
    database.csv
   </code>
  </h3>
  <pre><code>firstname,lastname,age,field
Johann,Kerbrou,30,CS
Guillaume,Salou,30,SWE
Arielle,Salou,20,CS
Jonathan,Benou,30,CS
Emmanuel,Turlou,40,CS
Guillaume,Plessous,35,CS
Joseph,Crisou,34,SWE
Paul,Schneider,60,SWE
Tommy,Schoul,32,SWE
Katie,Shirou,21,CS
</code></pre>
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
  "name": "node_js_basics",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "lint": "./node_modules/.bin/eslint",
    "check-lint": "eslint [0-9]*.js",
    "test": "./node_modules/mocha/bin/mocha --require babel-register --exit",
    "dev": "nodemon --exec babel-node --presets babel-preset-env ./server.js ./database.csv"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "chai-http": "^4.3.0",
    "express": "^4.17.1"
  },
  "devDependencies": {
    "babel-cli": "^6.26.0",
    "babel-preset-env": "^1.7.0",
    "nodemon": "^2.0.2",
    "eslint": "^6.4.0",
    "eslint-config-airbnb-base": "^14.0.0",
    "eslint-plugin-import": "^2.18.2",
    "eslint-plugin-jest": "^22.17.0",
    "chai": "^4.2.0",
    "mocha": "^6.2.2",
    "request": "^2.88.0",
    "sinon": "^7.5.0"
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
    'max-classes-per-file': 'off',
    'no-underscore-dangle': 'off',
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
   and…
  </h3>
  <p>
   Don’t forget to run
   <code>
    $ npm install
   </code>
   when you have the
   <code>
    package.json
   </code>
  </p>
 </div>
</div>

[--LINK PROJECT--](https://intranet.hbtn.io/projects/615)
</html>