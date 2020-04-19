import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
  render() {
    return (
      <div>
        <p>This is JSX from React!</p>
      </div>
    );
  }
}

ReactDOM.render(<App />, document.querySelector('#root'));
