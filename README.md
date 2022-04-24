# disney-optimizer

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Frontend

In the disney-optimizer-frontend directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

## Backend

### Getting started

In the root of the project run `python3 -m venv venv` to build a virtual environment, then run `source venv/bin/activate` to activate it (`deactivate` at any time to leave).

To run the server locally run `python -m flask run -p 5000` to run on port 5000 which is what the local frontend is setup to talk to.

## Deploying

The app is deployed to heroku at [disney-optimizer.herokuapp.com](https://disney-optimizer.herokuapp.com/). To deploy first run: 

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

### Commit and push to heroku

Then add and commit all changes including the build and deploy using `git push heroku main`.

