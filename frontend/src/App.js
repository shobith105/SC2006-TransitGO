import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import UserComponent from './components/UserComponent';

function App() {
    return (
        <Router>
            <div>
                <h1>My Mobile App</h1>
                <Switch>
                    <Route path="/users" component={UserComponent} />
                    {/* Add more routes here as needed */}
                </Switch>
            </div>
        </Router>
    );
}

export default App;