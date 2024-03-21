# 3GPP-CHATBOT-DATA-PROCESS

## The project developers

The project is developed by the third-year Information Technology students from Oulu University of Applied Sciences:

- **Antti-Jussi Niku**, [GitHub account](https://github.com/ArunJ0)
- **Mufida Alakulju**, [GitHub account](https://github.com/mufidaA)
- **Yinan Li**, [GitHub account](https://github.com/YinanLi1987)

## Introduction of the repository

This is the data process part of a company-oriented-project, the aim is to "Define and develop a market-leading 3GPP CR analytics application MVP(minimum viable product)". This repository includes three folders each responsible for a specific purpose.

- **1_mkd_from_docx**,the script used to convert the word file to mark down file.
- **2_Json_chunks**,the script used to chunk the mark down file into small pices.
- **3_data_insert**,the script used to embedding and inserting the Json file.

## Technologies used in each folder

- 1_mkd_from_docx:

  - **HTML & CSS**
  - [**Bootstrap**](https://github.com/twbs/bootstrap#readme) 5.2.2
  - [**React Bootstrap**](https://react-bootstrap.github.io/) 2.6.0

- 2_Json_chunks:

  - [**React.js**](https://reactjs.org/) 18.2.0

- 3_data_insert:

  - [**Node.js**](https://nodejs.org/en/) 19.0.1
  - [**Express.js**](https://github.com/expressjs/express) 4.18.2
  - [**Axios.js**](https://github.com/axios/axios#readme) 1.1.3

## How to implement the data process

**Step one:**

Download the project / clone the project repository

**Step two:**

Within the root folder, install the following dependencies:

- [**Axios.js**](https://github.com/axios/axios#readme) 1.1.3
- [**Chart.js**](https://www.chartjs.org/) 3.9.1
- [**react-chartjs-2**](https://github.com/reactchartjs/react-chartjs-2#readme) 4.3.1
- [**jwt-decode**](https://github.com/auth0/jwt-decode#readme) 3.1.2
- [**Bootstrap**](https://github.com/twbs/bootstrap#readme) 5.2.2
- [**react-dom**](https://www.npmjs.com/package/react-dom) 18.2.0
- [**react-router-dom**](https://www.npmjs.com/package/react-router-dom) 6.4.3

**Step three:**

Go to the server folder:

```
npm init -y
npm install express
```

Install the following dependencies:

- [**bcrypt**](https://github.com/dcodeIO/bcrypt.js#readme) 2.4.3
- [**body-parser**](https://github.com/expressjs/body-parser#readme) 1.20.1
- [**cors**](https://github.com/expressjs/cors#readme) 2.8.5
- [**jsonwebtoken**](https://github.com/auth0/node-jsonwebtoken#readme) 8.5.1
- [**mysql**](https://github.com/mysqljs/mysql#readme) 2.18.1
- [**passport**](https://github.com/jaredhanson/passport#readme) 0.6.0
- [**passport-http**](https://github.com/jaredhanson/passport-http#readme) 0.3.0
- [**passport-jwt**](https://github.com/themikenicholson/passport-jwt#readme) 4.0.0
- [**uuid**](https://github.com/uuidjs/uuid#readme) 9.0.0

**Step four:**

Create the local database :

- Start mysql and import the _charttest.sql_ file into your local database
- Create a _database.js_ file inside the server folder as follows, and modify the ‘xxxx’ part as needed:

```
const mysql = require("mysql");
        const connection = mysql.createConnection({
         host: "xxxx",
         user: "xxxx",
         password: "xxxx",
         database: "xxxx",
   });

module.exports = connection;
```

**Step five:**

To start the application, run the following command:

```
cd server
node index.js
cd ..
npm start

```
